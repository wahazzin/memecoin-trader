"""
paper.py -- the paper exchange. Every fill comes from a LIVE Jupiter quote (the real Solana swap router),
never from our own math. Costs that are not inside the quote are added from MEASURED values
(COST_FACTORS.md). Nothing here can sign or send a transaction: there is no wallet and no key.

Fill rule (COST_FACTORS #9/#10): quote now, quote again DELAY_S later, fill at the WORSE of the two.
If the second quote is worse than the slippage limit, the order counts as FAILED and the network +
priority fee is still charged.
"""
import time

import requests

JUP = ["https://lite-api.jup.ag/swap/v1/quote", "https://api.jup.ag/swap/v1/quote"]
SOL = "So11111111111111111111111111111111111111112"
DEC_TOKEN, LAMPORTS = 1e6, 1e9

# measured 2026-10-07 (research/measure_costs.py, 178 real trades) -- p90 used on purpose (pessimistic)
PRIORITY_SOL = 0.0015
NETWORK_SOL = 0.000005
RENT_SOL = 0.00203928        # SPL token account rent-exempt minimum (2,039,280 lamports), refunded on close
DELAY_S = 2.0
SLIPPAGE_BPS = 2000          # 20% like Setuh's buy setting; beyond this the order fails


def quote(inp, outp, amount_raw, timeout=10):
    last = None
    for host in JUP:
        try:
            r = requests.get(host, params={"inputMint": inp, "outputMint": outp, "amount": int(amount_raw),
                                           "slippageBps": SLIPPAGE_BPS}, timeout=timeout)
            js = r.json()
            if r.status_code == 200 and "outAmount" in js:
                return {"out": int(js["outAmount"]), "impact": float(js.get("priceImpactPct") or 0),
                        "route": [p["swapInfo"].get("label") for p in js.get("routePlan", [])], "t": time.time()}
            last = js.get("errorCode") or js.get("error") or r.status_code
        except Exception as e:
            last = type(e).__name__
    return {"error": str(last), "t": time.time()}


def _two_quotes(inp, outp, amount_raw, sleep=time.sleep):
    q1 = quote(inp, outp, amount_raw)
    sleep(DELAY_S)
    q2 = quote(inp, outp, amount_raw)
    return q1, q2


def buy(mint, sol, first_buy=True, sleep=time.sleep):
    """Paper buy `sol` SOL of `mint`. Returns an order record (status FILLED / FAILED / NO_ROUTE)."""
    q1, q2 = _two_quotes(SOL, mint, sol * LAMPORTS, sleep)
    rec = {"side": "buy", "mint": mint, "sol_in": sol, "q1": q1, "q2": q2, "ts": time.time()}
    fees = PRIORITY_SOL + NETWORK_SOL
    if "error" in q1 or "error" in q2:
        rec.update(status="NO_ROUTE", tokens=0, cost_sol=0.0)
        return rec
    worst = min(q1["out"], q2["out"])
    if q2["out"] < q1["out"] * (1 - SLIPPAGE_BPS / 1e4):
        rec.update(status="FAILED", tokens=0, cost_sol=fees, note="price moved past slippage before landing")
        return rec
    rent = RENT_SOL if first_buy else 0.0
    rec.update(status="FILLED", tokens=worst / DEC_TOKEN, cost_sol=sol + fees + rent, rent=rent,
               fees_outside_quote=fees, fill_quote="q1" if worst == q1["out"] else "q2")
    return rec


def sell(mint, tokens, close_account=True, sleep=time.sleep):
    """Paper sell `tokens` of `mint`. Proceeds = worse of two quotes, minus fees, plus rent refund."""
    q1, q2 = _two_quotes(mint, SOL, tokens * DEC_TOKEN, sleep)
    rec = {"side": "sell", "mint": mint, "tokens": tokens, "q1": q1, "q2": q2, "ts": time.time()}
    fees = PRIORITY_SOL + NETWORK_SOL
    if "error" in q1 or "error" in q2:
        rec.update(status="NO_ROUTE", proceeds_sol=0.0)
        return rec
    worst = min(q1["out"], q2["out"])
    if q2["out"] < q1["out"] * (1 - SLIPPAGE_BPS / 1e4):
        rec.update(status="FAILED", proceeds_sol=-fees, note="price moved past slippage before landing")
        return rec
    refund = RENT_SOL if close_account else 0.0
    rec.update(status="FILLED", proceeds_sol=worst / LAMPORTS - fees + refund, rent_refund=refund,
               fees_outside_quote=fees, fill_quote="q1" if worst == q1["out"] else "q2")
    return rec
