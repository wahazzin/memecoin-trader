"""
probe_logs.py -- READ-ONLY: can we get every pump.fun trade for free by listening to the Solana network
directly (logsSubscribe on the pump.fun program) and decoding its TradeEvent? No key, no wallet.
"""
import asyncio
import base64
import json
import os
import struct
import time
from collections import Counter

from research import base58_lite as b58

PUMP = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"
OUT = os.path.join(os.path.dirname(__file__), "out", "probe")


def decode_trade(raw):
    """pump.fun TradeEvent: 8-byte discriminator, mint(32), sol u64, tokens u64, is_buy u8, user(32), ts i64,
    vSol u64, vTok u64, ... (newer versions append fields; we read only the stable prefix)."""
    if len(raw) < 8 + 32 + 8 + 8 + 1 + 32 + 8 + 16:
        return None
    o = 8
    mint = b58.encode(raw[o:o + 32]); o += 32
    sol, tok = struct.unpack_from("<QQ", raw, o); o += 16
    is_buy = raw[o]; o += 1
    user = b58.encode(raw[o:o + 32]); o += 32
    ts, vsol, vtok = struct.unpack_from("<qQQ", raw, o)
    if is_buy not in (0, 1) or not (1.6e9 < ts < 2.2e9):
        return None
    return {"mint": mint, "sol": sol / 1e9, "tokens": tok / 1e6, "buy": bool(is_buy), "user": user, "ts": ts,
            "vsol": vsol / 1e9, "vtok": vtok / 1e6, "price_sol": (vsol / 1e9) / (vtok / 1e6) if vtok else None}


async def run(url, seconds):
    import websockets
    msgs, trades, errs, discs = 0, [], [], Counter()
    t0 = time.time()
    try:
        async with websockets.connect(url, max_size=2 ** 24, ping_interval=20) as ws:
            await ws.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "logsSubscribe",
                                      "params": [{"mentions": [PUMP]}, {"commitment": "confirmed"}]}))
            while time.time() - t0 < seconds:
                try:
                    m = json.loads(await asyncio.wait_for(ws.recv(), timeout=20))
                except asyncio.TimeoutError:
                    continue
                msgs += 1
                v = m.get("params", {}).get("result", {}).get("value", {})
                if not v:
                    errs.append(m); continue
                if v.get("err"):
                    continue
                for line in v.get("logs", []):
                    if line.startswith("Program data: "):
                        raw = base64.b64decode(line[14:])
                        discs[raw[:8].hex()] += 1
                        t = decode_trade(raw)
                        if t:
                            t["sig"] = v.get("signature")
                            trades.append(t)
    except Exception as e:
        errs.append({"error": f"{type(e).__name__}: {e}"})
    return msgs, trades, errs, discs, time.time() - t0


def main():
    os.makedirs(OUT, exist_ok=True)
    lines = [f"# Probe 2: pump.fun trades straight from the Solana network ({time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())})", ""]
    for name, url in (("public mainnet RPC", "wss://api.mainnet-beta.solana.com"),):
        msgs, trades, errs, discs, secs = asyncio.run(run(url, 180))
        lines += [f"## {name}", f"- {secs:.0f}s, {msgs} log messages, {len(trades)} decoded trades "
                  f"(~{len(trades) / secs * 86400:,.0f}/day), {len(set(t['mint'] for t in trades))} coins",
                  f"- event discriminators seen: {discs.most_common(6)}",
                  f"- errors/other: {[str(e)[:200] for e in errs[:3]]}"]
        if trades:
            buys = sum(t["buy"] for t in trades)
            lines += [f"- buys {buys} / sells {len(trades) - buys}; median size "
                      f"{sorted(t['sol'] for t in trades)[len(trades) // 2]:.3f} SOL",
                      f"- sample: {json.dumps(trades[0])}"]
        with open(os.path.join(OUT, "logs_sample.json"), "w") as f:
            json.dump(trades[:300], f)
    with open(os.path.join(OUT, "probe_logs.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
