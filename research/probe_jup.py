"""
probe_jup.py -- READ-ONLY: does Jupiter's quote API give real executable quotes for brand-new pump.fun
coins (bonding curve) and migrated ones? A quote is what the real router would fill RIGHT NOW for a
given size, incl. price impact and route fees. No wallet, no swap.
"""
import asyncio
import json
import os
import time

import requests

OUT = os.path.join(os.path.dirname(__file__), "out", "probe")
SOL = "So11111111111111111111111111111111111111112"
HOSTS = ["https://lite-api.jup.ag/swap/v1/quote", "https://api.jup.ag/swap/v1/quote", "https://quote-api.jup.ag/v6/quote"]


async def new_mints(n=8, secs=90):
    import websockets
    out = []
    async with websockets.connect("wss://pumpportal.fun/api/data") as ws:
        await ws.send(json.dumps({"method": "subscribeNewToken"}))
        t0 = time.time()
        while len(out) < n and time.time() - t0 < secs:
            m = json.loads(await ws.recv())
            if m.get("txType") == "create":
                out.append(m)
    return out


def quote(host, inp, outp, amount, timeout=20):
    r = requests.get(host, params={"inputMint": inp, "outputMint": outp, "amount": int(amount), "slippageBps": 500},
                     timeout=timeout)
    try:
        js = r.json()
    except Exception:
        js = r.text[:200]
    return r.status_code, js


def main():
    os.makedirs(OUT, exist_ok=True)
    L = [f"# Probe 3: Jupiter quotes ({time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())})", ""]
    mints = asyncio.run(new_mints())
    L.append(f"- fresh pump.fun coins captured: {len(mints)}")
    host_ok = None
    for h in HOSTS:
        sc, js = quote(h, SOL, "EPjFWdd5AufqzSqLzh7JKwqjVwtJpTsxNw9dSLE6Dt1v", 1e8)   # SOL->USDC sanity check
        L.append(f"- {h}: SOL→USDC HTTP {sc} {str(js)[:160]}")
        if sc == 200 and host_ok is None:
            host_ok = h
    if not host_ok:
        L.append("- **no working Jupiter host**")
    else:
        time.sleep(20)                       # let the new coins exist for a bit
        for m in mints:
            sc, js = quote(host_ok, SOL, m["mint"], 0.1e9)
            line = f"- new coin {(m.get('symbol') or '')[:12]!r} age ~{int(time.time()) % 1000}s: buy 0.1 SOL → HTTP {sc}"
            if sc == 200 and isinstance(js, dict):
                route = [r["swapInfo"].get("label") for r in js.get("routePlan", [])]
                line += f", out {js.get('outAmount')}, impact {js.get('priceImpactPct')}, route {route}"
                sc2, js2 = quote(host_ok, m["mint"], SOL, int(js["outAmount"]))
                if sc2 == 200:
                    back = int(js2["outAmount"]) / 1e9
                    line += f" | sell straight back → {back:.5f} SOL (round trip {100 * (back / 0.1 - 1):+.2f}%)"
                else:
                    line += f" | sell back HTTP {sc2} {str(js2)[:100]}"
            else:
                line += f" {str(js)[:160]}"
            L.append(line)
            time.sleep(1.2)
        js = requests.get("https://api.geckoterminal.com/api/v2/networks/solana/dexes/pumpswap/pools?page=1", timeout=30).json()
        for p in js.get("data", [])[:3]:
            tok = p["relationships"]["base_token"]["data"]["id"].split("_", 1)[1]
            sc, q = quote(host_ok, SOL, tok, 0.5e9)
            L.append(f"- migrated coin {p['attributes']['name'][:30]!r}: buy 0.5 SOL → HTTP {sc}, impact "
                     f"{q.get('priceImpactPct') if isinstance(q, dict) else q}, route "
                     f"{[r['swapInfo'].get('label') for r in q.get('routePlan', [])] if isinstance(q, dict) else ''}")
            time.sleep(1.2)
        n, ok, t = 0, 0, time.time()
        while time.time() - t < 30:
            sc, _ = quote(host_ok, SOL, "EPjFWdd5AufqzSqLzh7JKwqjVwtJpTsxNw9dSLE6Dt1v", 1e8); n += 1; ok += sc == 200
        L.append(f"- rate test: {ok}/{n} quotes OK in 30 s")
    with open(os.path.join(OUT, "probe_jup.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    try:
        main()
    except BaseException as e:
        import traceback
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, "probe_jup.md"), "w") as f:
            f.write("# Probe 3 crashed\n\n```\n" + traceback.format_exc() + "\n```\n")
        raise
