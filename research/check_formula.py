"""
check_formula.py -- READ-ONLY: does our bonding-curve formula (memebot/curve.py) give the same result as a
live Jupiter quote, for the same coin at the same moment? If yes, backtests on recorded data can use it.

For ~40 fresh pump.fun coins: read the curve account (reserves) -> quote Jupiter (buy 0.1 / 0.5 / 2 SOL,
and selling those tokens back) -> read the curve again. Only pairs where the reserves did NOT change
between the two reads count. Report the % difference formula vs Jupiter, per size, buy and sell.
"""
import asyncio
import base64
import json
import os
import struct
import time

import requests

from memebot.curve import buy_tokens, sell_sol

OUT = os.path.join(os.path.dirname(__file__), "out", "formula")
RPC = "https://api.mainnet-beta.solana.com"
JUP = "https://lite-api.jup.ag/swap/v1/quote"
SOL = "So11111111111111111111111111111111111111112"
DEC = 1e6


async def fresh(n=45, secs=150):
    import websockets
    out = []
    async with websockets.connect("wss://pumpportal.fun/api/data") as ws:
        await ws.send(json.dumps({"method": "subscribeNewToken"}))
        t0 = time.time()
        while len(out) < n and time.time() - t0 < secs:
            m = json.loads(await ws.recv())
            if m.get("txType") == "create" and m.get("bondingCurveKey"):
                out.append(m)
    return out


def curve(key):
    try:
        r = requests.post(RPC, json={"jsonrpc": "2.0", "id": 1, "method": "getAccountInfo",
                                     "params": [key, {"encoding": "base64", "commitment": "processed"}]}, timeout=20).json()
        raw = base64.b64decode(r["result"]["value"]["data"][0])
        vtok, vsol, rtok, rsol, supply = struct.unpack_from("<QQQQQ", raw, 8)
        return {"vtok": vtok / DEC, "vsol": vsol / 1e9, "complete": bool(raw[48])}
    except Exception:
        return None


def jq(inp, outp, amount):
    try:
        r = requests.get(JUP, params={"inputMint": inp, "outputMint": outp, "amount": int(amount),
                                      "slippageBps": 5000, "onlyDirectRoutes": "true"}, timeout=20)
        js = r.json()
        if r.status_code == 200 and js.get("routePlan", [{}])[0].get("swapInfo", {}).get("label") == "Pump.fun":
            return int(js["outAmount"])
    except Exception:
        pass
    return None


def main():
    os.makedirs(OUT, exist_ok=True)
    coins = asyncio.run(fresh())
    time.sleep(10)
    rows = []
    for m in coins:
        for size in (0.1, 0.5, 2.0):
            c1 = curve(m["bondingCurveKey"])
            if not c1 or c1["complete"]:
                break
            q_buy = jq(SOL, m["mint"], size * 1e9)
            q_sell = jq(m["mint"], SOL, q_buy) if q_buy else None
            c2 = curve(m["bondingCurveKey"])
            if not (q_buy and c2) or (c1["vsol"], c1["vtok"]) != (c2["vsol"], c2["vtok"]):
                rows.append({"coin": m["mint"], "size": size, "stable": False}); continue
            row = {"coin": m["mint"], "size": size, "stable": True, "vsol": c1["vsol"]}
            for fee in (0.0125, 0.0105, 0.0195, 0.0395):          # 0.95% + creator 0.30 / 0.10 / 1.0 / 3.0
                f_buy = buy_tokens(c1["vsol"], c1["vtok"], size, fee) * DEC
                row[f"buy_err_{fee}"] = 100 * (f_buy / q_buy - 1)
                if q_sell:
                    f_sell = sell_sol(c1["vsol"], c1["vtok"], q_buy / DEC, fee) * 1e9
                    row[f"sell_err_{fee}"] = 100 * (f_sell / q_sell - 1)
            rows.append(row)
            time.sleep(0.6)
    stable = [r for r in rows if r["stable"]]
    L = [f"# Formula vs live Jupiter quotes ({time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())})", "",
         f"{len(coins)} fresh coins, {len(rows)} attempts, {len(stable)} with unchanged reserves (usable).", "",
         "Error = formula ÷ Jupiter − 1, in %. Best-fitting total fee shown per row (the coin's own creator fee).", "",
         "| Size (SOL) | n | buy error: median / worst (best fee per coin) | sell error: median / worst |", "|---|---|---|---|"]
    for size in (0.1, 0.5, 2.0):
        g = [r for r in stable if r["size"] == size]
        if not g:
            continue
        best_b = [min((abs(v) for k, v in r.items() if k.startswith("buy_err")), default=None) for r in g]
        best_s = [min((abs(v) for k, v in r.items() if k.startswith("sell_err")), default=None) for r in g]
        best_b = sorted(x for x in best_b if x is not None)
        best_s = sorted(x for x in best_s if x is not None)
        med = lambda xs: xs[len(xs) // 2] if xs else float("nan")
        L.append(f"| {size} | {len(g)} | {med(best_b):.4f}% / {max(best_b) if best_b else float('nan'):.4f}% | "
                 f"{med(best_s):.4f}% / {max(best_s) if best_s else float('nan'):.4f}% |")
    fits = {}
    for r in stable:
        errs = {k.split("_")[-1]: abs(v) for k, v in r.items() if k.startswith("buy_err")}
        if errs:
            b = min(errs, key=errs.get); fits[b] = fits.get(b, 0) + 1
    L += ["", f"Best-fitting total fee per coin (buy side): {fits}",
          "", "Verdict rule (set before running): formula trusted for backtests if the median error ≤ 0.1% and the "
          "worst ≤ 0.5% at every size."]
    with open(os.path.join(OUT, "formula.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(OUT, "formula_rows.json"), "w") as f:
        json.dump(rows, f)
    print("\n".join(L))


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        import traceback
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, "formula.md"), "w") as f:
            f.write("# check_formula crashed\n\n```\n" + traceback.format_exc() + "\n```\n")
        raise
