"""
m2.py -- Test M2 exactly as pre-registered in research/M2_PREREG.md (dip entry vs random entry, after costs).
Usage: python -m research.m2 [--synthetic]
"""
import hashlib
import math
import os
import random
import sys
from collections import defaultdict

from research.m1 import buy_tokens, sell_value, PRIO, RENT, NET, from_recordings

OUT = os.path.join(os.path.dirname(__file__), "out", "m2")
SIZE = 0.5
BANDS = {"dip40_50": (0.50, 0.60), "dip30_40": (0.60, 0.70), "dip50_60": (0.40, 0.50)}
PRIMARY = ("dip40_50", 2.0)


def fee_of(t):
    if t.get("fee_total_bps") is not None:                 # PumpSwap after graduation: fee tier from the event
        return t["fee_total_bps"] / 1e4
    return ((t.get("fee_bps") or 95) + (t.get("cfee_bps") or 30)) / 1e4


def trade_from(tr, i, tp, created):
    """Signal on trade i -> fill at trade i+1's reserves. Exits per spec. Returns net return or None."""
    if i + 1 >= len(tr):
        return None
    e = tr[i + 1]
    fee = fee_of(e)
    tok = buy_tokens(e["vsol"], e["vtok"], SIZE, fee)
    p_in, t_in = e["price"], e["ts"]
    cost_in = SIZE + PRIO + RENT + NET
    exit_t, prev = None, e
    j = i + 2
    while j < len(tr):
        t = tr[j]
        if t["ts"] - prev["ts"] > 900:
            exit_t = prev; break                       # 15 min without a trade
        if t["ts"] - t_in > 3600:
            exit_t = prev; break                       # 60 min max hold
        if t["price"] >= tp * p_in or t["price"] <= 0.8 * p_in:
            exit_t = tr[j + 1] if j + 1 < len(tr) else t   # filled at the NEXT trade (gap-through counted)
            break
        prev = t
        j += 1
    if exit_t is None:
        exit_t = prev
    proceeds = sell_value(exit_t["vsol"], exit_t["vtok"], tok, fee) - PRIO - NET + RENT
    return proceeds / cost_in - 1


def evaluate(coins):
    rows = []
    for c in coins:
        tr = c["trades"]
        if len(tr) < 5:
            continue
        launch, H, q = tr[0]["price"], 0.0, None
        entered = {}
        for i, t in enumerate(tr):
            if t["ts"] - c["created"] > 3600:
                break
            H = max(H, t["price"])
            if q is None and H >= 5 * launch:
                q = i
            if q is None or i <= q or not t["buy"]:
                continue
            for band, (lo, hi) in BANDS.items():
                if band not in entered and lo * H <= t["price"] <= hi * H:
                    entered[band] = i
        if q is None:
            continue
        cands = [i for i in range(q + 1, len(tr)) if tr[i]["buy"] and tr[i]["ts"] - c["created"] <= 3600]
        rnd = random.Random(int(hashlib.md5(c["mint"].encode()).hexdigest()[:8], 16))
        r_i = rnd.choice(cands) if cands else None
        for tp in (2.0, 1.5):
            if r_i is not None:
                ret = trade_from(tr, r_i, tp, c["created"])
                if ret is not None:
                    rows.append({"mint": c["mint"], "ts": tr[r_i]["ts"], "arm": "random", "tp": tp, "ret": ret})
            for band, i in entered.items():
                ret = trade_from(tr, i, tp, c["created"])
                if ret is not None:
                    rows.append({"mint": c["mint"], "ts": tr[i]["ts"], "arm": band, "tp": tp, "ret": ret})
    return rows


def hourly(rows):
    g = defaultdict(list)
    for r in rows:
        g[int(r["ts"] // 3600)].append(r["ret"])
    return {h: sum(v) / len(v) for h, v in g.items()}


def tstat(xs):
    if len(xs) < 10:
        return float("nan")
    m = sum(xs) / len(xs)
    s = math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
    return m / (s / math.sqrt(len(xs))) if s else float("nan")


def report(rows, label=""):
    rows.sort(key=lambda r: r["ts"])
    if not rows:
        return f"# M2 results {label}\n\nNo qualifying coins.", False
    days = sorted({int(r["ts"] // 86400) for r in rows})
    cut = days[int(len(days) * 0.6)] * 86400 if len(days) >= 2 else rows[len(rows) * 6 // 10]["ts"]
    L = [f"# M2 results {label}", "", f"days: {len(days)}", "",
         "| Split | Arm | Exit | n | Win rate | Expectancy/trade | t (hours) | vs random: diff | t |", "|---|---|---|---|---|---|---|---|---|"]
    verdict = []
    for split, sel in (("DESIGN", lambda r: r["ts"] < cut), ("HOLDOUT", lambda r: r["ts"] >= cut)):
        for tp in (2.0, 1.5):
            rnd = [r for r in rows if sel(r) and r["arm"] == "random" and r["tp"] == tp]
            hr = hourly(rnd)
            for arm in ("random",) + tuple(BANDS):
                g = [r for r in rows if sel(r) and r["arm"] == arm and r["tp"] == tp]
                if not g:
                    continue
                h = hourly(g)
                e = sum(r["ret"] for r in g) / len(g)
                t = tstat(list(h.values()))
                d = [h[k] - hr[k] for k in h if k in hr]
                dm = sum(d) / len(d) if d else float("nan")
                dt = tstat(d) if arm != "random" else float("nan")
                L.append(f"| {split} | {arm}{' **(primary)**' if (arm, tp) == PRIMARY else ''} | +{int((tp - 1) * 100)}% | {len(g)} | "
                         f"{sum(r['ret'] > 0 for r in g) / len(g):.0%} | {e:+.2%} | {t:+.2f} | "
                         f"{'—' if arm == 'random' else f'{dm:+.2%}'} | {'—' if arm == 'random' else f'{dt:+.2f}'} |")
                if (arm, tp) == PRIMARY:
                    verdict.append(e > 0 and t >= 2 and dm > 0 and dt >= 2 and (split == "DESIGN" or len(g) >= 300))
    ok = len(verdict) == 2 and all(verdict)
    L += ["", f"**Verdict (primary: 40–50% dip, +100% exit): {'PASS' if ok else 'NO EVIDENCE'}** "
          "(pre-registered: expectancy > 0 with t ≥ 2 AND beats random with t ≥ 2, both splits, ≥ 300 holdout entries)."]
    return "\n".join(L), ok


def synthetic(effect):
    """Fake coins: pump to ≥5x launch, dip, then rebound or die. effect=True: coins rebound after a 40–60% dip
    much more often than a fair game would allow; effect=False: after the dip, rebound odds are 'fair'."""
    rng = random.Random(11)
    coins = []
    for i in range(4000):
        created = 1.79e9 + i * 200
        vsol, vtok, tr, ts = 30.0, 1.073e9, [], created
        def step(target_vsol, n, seconds):
            nonlocal vsol, vtok, ts
            for _ in range(n):
                ts += rng.expovariate(1 / seconds)
                want = vsol + (target_vsol - vsol) / max(n, 1) * 3 + rng.gauss(0, 0.3)
                if want > vsol:
                    sol = want - vsol; tok = vtok - vsol * vtok / (vsol + sol); vsol += sol; vtok -= tok; buy = True
                else:
                    out = min(vsol - want, vsol - 30.01)
                    if out <= 0: continue
                    tok = vtok * vsol / (vsol - out) - vtok; vsol -= out; vtok += tok; sol = out; buy = False
                tr.append({"ts": ts, "user": f"u{rng.random()}", "buy": buy, "sol": sol, "tok": tok, "vsol": vsol,
                           "vtok": vtok, "price": vsol / vtok, "fee_bps": 95, "cfee_bps": 30})
        step(30.5, 3, 3)
        step(80, 40, 5)                        # pump: price ~7x launch
        step(58, 25, 5)                        # dip ~45% from the high
        p_rebound = 0.55 if effect else 0.17
        if rng.random() < p_rebound:
            step(120, 50, 6)                   # rebound well past 2x the dip price
        else:
            step(30.5, 50, 6)                  # dies back to the launch floor
        coins.append({"mint": f"m{i}", "created": created, "creator": "dev", "trades": tr})
    return coins


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    if "--synthetic" in sys.argv:
        for eff in (True, False):
            text, _ = report(evaluate(synthetic(eff)), f"(SYNTHETIC, planted effect={eff})")
            print(text, "\n")
    else:
        text, _ = report(evaluate(from_recordings()))
        with open(os.path.join(OUT, "M2_results.md"), "w") as f:
            f.write(text + "\n")
        print(text)
