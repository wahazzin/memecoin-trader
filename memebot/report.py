"""report.py -- paper bot check-in (project rule 2): per arm trades, win rate, avg win vs avg loss,
expectancy, drawdown, circuit breakers, stuck positions. Usage: python -m memebot.report --state paper_state"""
import argparse
import json
import os
import time


def read(path):
    return [json.loads(l) for l in open(path)] if os.path.exists(path) else []


def build(state, since=0):
    orders = [o for o in read(os.path.join(state, "orders.jsonl")) if o.get("ts", 0) >= since]
    eq = read(os.path.join(state, "equity.jsonl"))
    ev = read(os.path.join(state, "events.jsonl"))
    pos = json.load(open(os.path.join(state, "positions.json"))) if os.path.exists(os.path.join(state, "positions.json")) else {}
    L = [f"# Paper bot check-in ({time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())})", "",
         "> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).", "",
         "| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for arm in sorted({o.get("arm") for o in orders} | set(pos)):
        bo = [o for o in orders if o.get("arm") == arm and o["side"] == "buy"]
        cl = [o for o in orders if o.get("arm") == arm and o["side"] == "sell" and o["status"] == "FILLED"]
        pnl = [o["pnl_sol"] for o in cl]
        wins, losses = [x for x in pnl if x > 0], [x for x in pnl if x <= 0]
        wr = len(wins) / len(pnl) if pnl else None
        aw = sum(wins) / len(wins) if wins else 0.0
        al = sum(losses) / len(losses) if losses else 0.0
        exp_ = (wr * aw + (1 - wr) * al) if wr is not None else None
        e = [x["equity"] for x in eq if x["arm"] == arm]
        peak, mdd = -1e9, 0.0
        for v in e:
            peak = max(peak, v); mdd = min(mdd, v / peak - 1)
        stuck = sum(1 for p in pos.get(arm, {}).values() if p.get("stuck_since"))
        f = lambda x: "—" if x is None else f"{x:+.4f}"
        L.append(f"| `{arm}` | {sum(o['status'] == 'FILLED' for o in bo)} / {sum(o['status'] == 'FAILED' for o in bo)} / "
                 f"{sum(o['status'] == 'NO_ROUTE' for o in bo)} | {len(pnl)} | {'—' if wr is None else f'{wr:.0%}'} | {f(aw)} | {f(al)} | "
                 f"**{f(exp_)}** | {sum(pnl):+.4f} | {e[-1] if e else 0:.3f} | {mdd:.1%} | {len(pos.get(arm, {}))} | {stuck} |")
    fb = sum(1 for o in orders if o.get("source") == "curve_formula")
    # sensitivity: P&L if every fill had used the FIRST quote (no 2 s delay) -- shows how much the delay costs
    alt = {}
    for o in orders:
        if o["side"] == "sell" and o["status"] == "FILLED" and o.get("source") == "jupiter" and "out" in o.get("q1", {}):
            d = o["q1"]["out"] / 1e9 - (o["proceeds_sol"] - o.get("rent_refund", 0) + 0.0015 + 0.000005)
            alt[o.get("arm")] = alt.get(o.get("arm"), 0) + d
    cb = [x for x in ev if x.get("type") == "CIRCUIT_BREAKER" and x.get("ts", 0) >= since]
    gaps = [x for x in ev if x.get("type") == "GAP" and x.get("ts", 0) >= since]
    reasons = {}
    for o in orders:
        if o["side"] == "sell" and o["status"] == "FILLED":
            reasons[o.get("why")] = reasons.get(o.get("why"), 0) + 1
    L += ["", f"- Exit reasons: {reasons or '—'}",
          f"- Sells priced by the verified curve formula because Jupiter had no route: {fb}",
          f"- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: "
          + (", ".join(f"{k} {v:+.3f}" for k, v in alt.items()) or "—"), f"- Circuit breakers fired: {len(cb)}", f"- Stream gaps logged: {len(gaps)}",
          "", "Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).",
          "The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md."]
    return "\n".join(L)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", default="paper_state")
    ap.add_argument("--days", type=float, default=0)
    a = ap.parse_args()
    since = time.time() - a.days * 86400 if a.days else 0
    text = build(a.state, since)
    with open(os.path.join(a.state, "REPORT.md"), "w") as f:
        f.write(text + "\n")
    print(text)
