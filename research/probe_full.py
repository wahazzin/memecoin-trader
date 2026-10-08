"""probe_full.py -- READ-ONLY check of the open questions from pump.fun's docs, on live data:
1. does TradeEvent `fee` include `buyback_fee`?  2. non-SOL quote coins: how common, what are vsol/vquote?
3. are PumpSwap (pump_amm) trades visible in logsSubscribe, and are pool reserves before or after the trade?
4. synthetic-migration PostCompleteBuy events / migrations seen."""
import asyncio
import base64
import json
import os
import time
from collections import Counter, defaultdict

from memebot.decode import events, SOL_MINTS

OUT = os.path.join(os.path.dirname(__file__), "out", "probe")
WS = "wss://api.mainnet-beta.solana.com"
PROGS = {"pump": "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P", "amm": "pAMMBay6oceH9fJKBRHGP5D4bD4sWpmSwMn52FMfXEA"}


async def listen(prog, secs):
    import websockets
    got, raw_disc, n = [], Counter(), 0
    t0 = time.time()
    async with websockets.connect(WS, max_size=2 ** 24, ping_interval=20) as ws:
        await ws.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "logsSubscribe",
                                  "params": [{"mentions": [PROGS[prog]]}, {"commitment": "confirmed"}]}))
        while time.time() - t0 < secs:
            try:
                m = json.loads(await asyncio.wait_for(ws.recv(), timeout=20))
            except Exception:
                break
            v = (m.get("params", {}).get("result", {}) or {}).get("value") or {}
            if not v or v.get("err"):
                continue
            n += 1
            for line in v.get("logs", []):
                if line.startswith("Program data: "):
                    raw_disc[base64.b64decode(line[14:])[:8].hex()] += 1
            for kind, d in events(v.get("logs", [])):
                got.append((kind, d, v.get("signature")))
    return n, got, raw_disc


def main():
    os.makedirs(OUT, exist_ok=True)
    L = [f"# Probe: open questions from pump.fun docs ({time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())})", ""]
    n, got, disc = asyncio.run(listen("pump", 120))
    tr = [d for k, d, _ in got if k == "trade"]
    L.append(f"## pump program, 120 s: {n} txs, {len(tr)} trades, kinds {dict(Counter(k for k, _, _ in got))}")
    sol = [t for t in tr if t.get("quote_mint") in SOL_MINTS]
    other = [t for t in tr if t.get("quote_mint") and t.get("quote_mint") not in SOL_MINTS]
    L.append(f"- quote mints: {Counter(t.get('quote_mint', 'n/a')[:8] for t in tr).most_common(6)}")
    L.append(f"- SOL coins {len(sol)}, non-SOL coins {len(other)} ({len({t['mint'] for t in other})} coins)")
    if other:
        o = other[0]
        L.append(f"- non-SOL sample: vsol {o['vsol']}, sol {o['sol']}, vquote_raw {o.get('vquote_raw')}, quote_amount_raw {o.get('quote_amount_raw')}, quote {o.get('quote_mint')}")
    def chk(t):
        if not t["sol"] or not t.get("fee_bps"):
            return None
        return (t["fee"] / t["sol"] * 1e4, (t["fee"] + t.get("buyback", 0)) / t["sol"] * 1e4)
    r = [x for x in (chk(t) for t in sol) if x]
    bb = [t for t in sol if t.get("buyback")]
    L.append(f"- trades with buyback>0: {len(bb)}/{len(sol)}; buyback_bps values {Counter(t.get('buyback_bps') for t in sol).most_common(4)}")
    if r:
        med = lambda xs: sorted(xs)[len(xs) // 2]
        L.append(f"- fee/sol in bps: median {med([a for a, _ in r]):.2f} (fee alone) vs {med([b for _, b in r]):.2f} (fee + buyback); event fee_bps {Counter(t['fee_bps'] for t in sol).most_common(3)}")
    L.append(f"- cashback_bps {Counter(t.get('cashback_bps') for t in sol).most_common(3)}, holder_rewards_bps {Counter(t.get('holder_rewards_bps') for t in sol).most_common(3)}, ix {Counter(t.get('ix') for t in sol).most_common(5)}, mayhem {sum(1 for t in sol if t.get('mayhem'))}")
    zero = [t for t in tr if t['sol'] == 0]
    L.append(f"- zero-SOL trades: {len(zero)} (non-SOL share among them: {sum(1 for t in zero if t.get('quote_mint') not in SOL_MINTS)})")
    L.append(f"- migrations {sum(1 for k,_,_ in got if k=='migrated')}, post-complete buys {sum(1 for k,_,_ in got if k=='postbuy')}, completes {sum(1 for k,_,_ in got if k=='complete')}")
    n2, got2, disc2 = asyncio.run(listen("amm", 60))
    at = [d for k, d, _ in got2 if k == "amm_trade"]
    L += ["", f"## pump_amm (PumpSwap), 60 s: {n2} txs, {len(at)} trades decoded from logs, pool creates {sum(1 for k,_,_ in got2 if k=='amm_create')}",
          f"- 'Program data' discriminators seen: {disc2.most_common(5)}"]
    by = defaultdict(list)
    for d in at:
        by[d["pool"]].append(d)
    seq = before = after = 0
    for pool, xs in by.items():
        for a, b in zip(xs, xs[1:]):
            # if reserves are AFTER the trade, b's reported reserves should differ from a's by b's own trade
            seq += 1
            da = b["pool_base_raw"] - a["pool_base_raw"]
            own = (-1 if b["buy"] else 1) * round(b["tok"] * 1e6)
            prev_own = (-1 if a["buy"] else 1) * round(a["tok"] * 1e6)
            if abs(da - prev_own) <= 2:
                before += 1
            elif abs(da - own) <= 2:
                after += 1
    L.append(f"- reserves timing on consecutive trades in the same pool: {seq} pairs, consistent with BEFORE-trade {before}, AFTER-trade {after}")
    if at:
        s = at[0]
        L.append(f"- sample: fee bps total {s['fee_bps_total']} (lp {s['lp_bps']} / protocol {s['protocol_bps']} / creator {s['creator_bps']}), vquote_raw {s['vquote_raw']}")
        L.append(f"- fee totals seen: {Counter(d['fee_bps_total'] for d in at).most_common(6)}")
    open(os.path.join(OUT, "probe_full.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        import traceback
        os.makedirs(OUT, exist_ok=True)
        open(os.path.join(OUT, "probe_full.md"), "w").write("crashed\n```\n" + traceback.format_exc() + "\n```\n")
        raise
