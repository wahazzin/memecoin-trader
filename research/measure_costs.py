"""
measure_costs.py -- MEASURE (not assume) what real pump.fun traders actually pay per trade, from real
transactions on the blockchain. Read-only.

1. Listen to live pump.fun trades for a few minutes (full transaction signatures).
2. Fetch a sample of those transactions and, for the trader (fee payer), split their SOL balance change into:
   trade amount + pump.fun fee + creator fee (from the event)  |  network fee  |  priority fee
   |  Jito tips  |  new account rent  |  anything left unexplained ("other", e.g. terminal/bot fees)
3. Report medians / percentiles by trade size, plus the zero-fee trades separately.
Output: research/out/costs/costs.md + costs.csv
"""
import asyncio
import base64
import csv
import json
import os
import random
import time

import requests

from memebot.decode import events as decode_events

OUT = os.path.join(os.path.dirname(__file__), "out", "costs")
RPC = os.environ.get("SOLANA_RPC", "https://api.mainnet-beta.solana.com")
WS = os.environ.get("SOLANA_WS", "wss://api.mainnet-beta.solana.com")
PUMP = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"
JITO_TIPS = {"96gYZGLnJYVFmbjzopPSU6QiEV5fGqZNyN9nmNhvrZU5", "HFqU5x63VTqvQss8hp11i4wVV8bD44PvwucfZ2bU7gRe",
             "Cw8CFyM9FkoMi7K7Crf6HNQqf4uEMzpKw6QNghXLvLkY", "ADaUMid9yfUytqMBgopwjb2DTLSokTSzL1zt6iGPaS49",
             "DfXygSm4jCyNCybVYYK6DwvWqjKee8pbDmJGcLWNDXjh", "ADuUkR4vqLUMWXxW9gh6D6L8pMSawimctcNZ5pGwDcEt",
             "DttWaMuVvTiduZRnguLF7jNxTgiMBZ1hyAumKUiL2KRL", "3AVi9Tg9Uo68tJfuvoKvqKNWKkC5wPdSSdeBnizKZ6jT"}


async def listen(seconds):
    import websockets
    got = {}
    t0 = time.time()
    while time.time() - t0 < seconds:
        try:
            async with websockets.connect(WS, max_size=2 ** 24, ping_interval=20) as ws:
                await ws.send(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "logsSubscribe",
                                          "params": [{"mentions": [PUMP]}, {"commitment": "confirmed"}]}))
                while time.time() - t0 < seconds:
                    m = json.loads(await asyncio.wait_for(ws.recv(), timeout=30))
                    v = (m.get("params", {}).get("result", {}) or {}).get("value") or {}
                    if not v or v.get("err"):
                        continue
                    tr = [d for k, d in decode_events(v.get("logs", [])) if k == "trade"]
                    if len(tr) == 1:                      # one trade per tx keeps the attribution clean
                        got[v["signature"]] = tr[0]
        except Exception as e:
            print("ws:", type(e).__name__)
            await asyncio.sleep(2)
    return got


def rpc(method, params):
    for _ in range(5):
        try:
            r = requests.post(RPC, json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params}, timeout=30)
            if r.status_code == 429:
                time.sleep(2); continue
            return r.json().get("result")
        except Exception:
            time.sleep(1)
    return None


def breakdown(sig, ev):
    tx = rpc("getTransaction", [sig, {"maxSupportedTransactionVersion": 0, "encoding": "jsonParsed",
                                      "commitment": "confirmed"}])
    if not tx or not tx.get("meta") or tx["meta"].get("err"):
        return None
    meta, msg = tx["meta"], tx["transaction"]["message"]
    keys = [k["pubkey"] if isinstance(k, dict) else k for k in msg["accountKeys"]]
    payer = keys[0]
    if payer != ev["user"]:
        return {"skip": "payer_is_not_trader"}            # relayed/bot-paid tx: attribution unclear
    nsig = len(tx["transaction"]["signatures"])
    delta = (meta["postBalances"][0] - meta["preBalances"][0]) / 1e9   # trader's SOL change (negative = spent)
    network = 5000 * nsig / 1e9
    priority = meta["fee"] / 1e9 - network
    tips, rent, transfers_out = 0.0, 0.0, 0.0
    ixs = list(msg.get("instructions", []))
    for inner in meta.get("innerInstructions", []) or []:
        ixs += inner.get("instructions", [])
    for ix in ixs:
        p = ix.get("parsed") if isinstance(ix, dict) else None
        if not isinstance(p, dict):
            continue
        info, typ = p.get("info", {}), p.get("type")
        if typ == "transfer" and info.get("source") == payer and "lamports" in info:
            amt = info["lamports"] / 1e9
            if info.get("destination") in JITO_TIPS:
                tips += amt
            else:
                transfers_out += amt
        if typ in ("createAccount", "createAccountWithSeed") and info.get("source") == payer:
            rent += info.get("lamports", 0) / 1e9
    # rent paid via the ATA program shows up as createAccount inner ix (counted above)
    fee_pump = (ev.get("fee") or 0) + (ev.get("cfee") or 0)
    if ev["buy"]:
        explained = -(ev["sol"] + fee_pump) - meta["fee"] / 1e9 - tips - rent
    else:
        explained = (ev["sol"] - fee_pump) - meta["fee"] / 1e9 - tips - rent
    other = explained - delta          # >0: trader lost more than explained (e.g. terminal fee); <0: got rent back etc.
    return {"sig": sig, "buy": ev["buy"], "sol": ev["sol"], "pump_fee": ev.get("fee"), "creator_fee": ev.get("cfee"),
            "fee_bps": ev.get("fee_bps"), "cfee_bps": ev.get("cfee_bps"), "network": network, "priority": priority,
            "jito_tip": tips, "rent": rent, "other_unexplained": other, "trader_delta": delta, "n_sigs": nsig}


def pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))] if xs else float("nan")


def main():
    os.makedirs(OUT, exist_ok=True)
    got = asyncio.run(listen(240))
    sigs = list(got)
    random.seed(1)
    zero = [s for s in sigs if not got[s].get("fee_bps")]
    nonzero = [s for s in sigs if got[s].get("fee_bps")]
    sample = random.sample(nonzero, min(350, len(nonzero))) + random.sample(zero, min(80, len(zero)))
    rows, skipped = [], {}
    for i, s in enumerate(sample):
        b = breakdown(s, got[s])
        if b is None:
            skipped["no_tx"] = skipped.get("no_tx", 0) + 1
        elif "skip" in b:
            skipped[b["skip"]] = skipped.get(b["skip"], 0) + 1
        else:
            rows.append(b)
        time.sleep(0.15)
    with open(os.path.join(OUT, "costs.csv"), "w", newline="") as f:
        if rows:
            w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    L = [f"# Measured costs of real pump.fun trades ({time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())})", "",
         f"Listened 4 min: {len(sigs)} single-trade transactions ({len(zero)} with 0 fee in the event). "
         f"Fetched {len(sample)}, usable {len(rows)}, skipped {skipped}.", "",
         "All amounts in SOL. Percent columns = cost as % of the trade size. Medians (p50) and p90.", ""]
    groups = [("buys < 0.2 SOL", lambda r: r["buy"] and r["sol"] < 0.2 and r["fee_bps"]),
              ("buys 0.2–1 SOL", lambda r: r["buy"] and 0.2 <= r["sol"] < 1 and r["fee_bps"]),
              ("buys ≥ 1 SOL", lambda r: r["buy"] and r["sol"] >= 1 and r["fee_bps"]),
              ("sells (all sizes)", lambda r: not r["buy"] and r["fee_bps"]),
              ("event shows 0 fee", lambda r: not r["fee_bps"])]
    L += ["| Group | n | pump+creator fee % | priority fee SOL p50 / p90 | Jito tip SOL p50 / p90 | new-account rent SOL (share of trades paying it) | unexplained SOL p50 / p90 | **total overhead % of size p50 / p90** |",
          "|---|---|---|---|---|---|---|---|"]
    for name, f in groups:
        g = [r for r in rows if f(r)]
        if not g:
            L.append(f"| {name} | 0 | | | | | | |"); continue
        feep = [100 * ((r["pump_fee"] or 0) + (r["creator_fee"] or 0)) / r["sol"] for r in g if r["sol"]]
        over = [100 * (r["network"] + r["priority"] + r["jito_tip"] + r["rent"] + max(r["other_unexplained"], 0)) / r["sol"]
                for r in g if r["sol"]]
        paying_rent = [r["rent"] for r in g if r["rent"] > 0]
        L.append(f"| {name} | {len(g)} | {pct(feep, .5):.2f}% | {pct([r['priority'] for r in g], .5):.6f} / {pct([r['priority'] for r in g], .9):.6f} | "
                 f"{pct([r['jito_tip'] for r in g], .5):.6f} / {pct([r['jito_tip'] for r in g], .9):.6f} | "
                 f"{pct(paying_rent, .5) if paying_rent else 0:.6f} ({100 * len(paying_rent) / len(g):.0f}%) | "
                 f"{pct([r['other_unexplained'] for r in g], .5):.6f} / {pct([r['other_unexplained'] for r in g], .9):.6f} | "
                 f"**{pct(over, .5):.2f}% / {pct(over, .9):.2f}%** |")
    L += ["", "Overhead = network + priority + Jito tip + new-account rent + unexplained (if positive). "
          "Pump/creator fees are separate (in the Jupiter quote). Rent is refundable only if the account is closed later."]
    with open(os.path.join(OUT, "costs.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        import traceback
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, "costs.md"), "w") as f:
            f.write("# measure_costs crashed\n\n```\n" + traceback.format_exc() + "\n```\n")
        raise
