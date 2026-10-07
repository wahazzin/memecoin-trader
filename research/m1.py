"""
m1.py -- Test M1 exactly as pre-registered in research/M1_PREREG.md.
Usage: python -m research.m1 [--synthetic]     (data: GitHub release recordings)
"""
import math
import os
import sys
from collections import defaultdict

OUT = os.path.join(os.path.dirname(__file__), "out", "m1")
SUPPLY = 1e9
PRIO, RENT, NET = 0.0015, 0.002, 0.000005        # measured p90 priority/side, account rent, network fee
SIZE = 0.5


def coin_checks(tr, creator):
    """tr: list of trade dicts BEFORE the checkpoint (time order). Returns dict of check -> pass(bool)."""
    hold, spent = defaultdict(float), defaultdict(float)
    for t in tr:
        hold[t["user"]] += t["tok"] if t["buy"] else -t["tok"]
        if t["buy"]:
            spent[t["user"]] += t["sol"]
    top = sorted(hold.items(), key=lambda x: -x[1])[:10]
    biggest = top[0][1] / SUPPLY if top else 0
    dev = hold.get(creator, 0) / SUPPLY
    sizes = [spent[u] for u, _ in top if spent[u] > 0]
    cv = (math.sqrt(sum((x - sum(sizes) / len(sizes)) ** 2 for x in sizes) / len(sizes)) / (sum(sizes) / len(sizes))
          if len(sizes) >= 3 else 1.0)
    p0, t0 = tr[0]["price"], tr[0]["ts"]
    first60 = [t for t in tr if t["ts"] - t0 <= 60]
    rocket = any(t["price"] >= 2.5 * p0 for t in first60) and not any(not t["buy"] for t in first60)
    cfee = max((t.get("cfee_bps") or 0) for t in tr)
    return {"C1": biggest <= 0.04, "C2": dev <= 0.05, "C3": cv >= 0.25, "C4": not rocket, "C5": cfee <= 30}


def sell_value(vsol, vtok, tok, fee):
    return (vsol - vsol * vtok / (vtok + tok)) * (1 - fee)


def buy_tokens(vsol, vtok, sol, fee):
    net = sol / (1 + fee)
    return vtok - vsol * vtok / (vsol + net)


def outcomes(after, p_cp, fee, cp_ts):
    """after: trades AFTER the checkpoint (time order). Dead flag + mechanical trade net return."""
    dead = None
    for t in after:
        if t["ts"] - cp_ts > 3600:
            break
        if t["price"] >= 1.5 * p_cp:
            dead = False; break
        if t["price"] <= 0.5 * p_cp:      # amended 2026-10-07 before any data: see M1_PREREG.md bottom
            dead = True; break
    if dead is None:
        dead = False
    if not after:
        return dead, None
    e = after[0]                                   # fill at the next trade's reserves (no same-tick fill)
    tok = buy_tokens(e["vsol"], e["vtok"], SIZE, fee)
    cost_in = SIZE + PRIO + RENT + NET
    p_in = e["price"]
    exit_t, last_ts = None, e["ts"]
    for t in after[1:]:
        if t["ts"] - last_ts > 900 or t["ts"] - e["ts"] > 3600:
            exit_t = prev; break                   # 15 min without a trade / 60 min: exit at the last state
        prev = t
        last_ts = t["ts"]
        if t["price"] >= 1.5 * p_in or t["price"] <= 0.8 * p_in:
            exit_t = t; break
    else:
        exit_t = after[-1] if len(after) > 1 else e
    proceeds = sell_value(exit_t["vsol"], exit_t["vtok"], tok, fee) - PRIO - NET + RENT   # rent refunded on close
    return dead, proceeds / cost_in - 1


def evaluate(coins):
    """coins: list of {mint, created, creator, trades:[...]} -> list of per-coin result rows."""
    rows = []
    for c in coins:
        tr = c["trades"]
        if len(tr) < 3:
            continue
        launch = tr[0]["price"]
        cp = next((i for i, t in enumerate(tr) if t["ts"] - c["created"] <= 2400 and t["price"] >= 2.5 * launch), None)
        if cp is None:
            continue
        before, after = tr[:cp + 1], tr[cp + 1:]
        chk = coin_checks(before, c["creator"])
        fee = (max((t.get("fee_bps") or 95) for t in before) + max((t.get("cfee_bps") or 30) for t in before)) / 1e4
        dead, ret = outcomes(after, tr[cp]["price"], fee, tr[cp]["ts"])
        rows.append({"mint": c["mint"], "ts": tr[cp]["ts"], "pass": all(chk.values()), **chk, "dead": dead, "ret": ret})
    return rows


def ztest(a, b):
    """two-proportion z: a, b = lists of bools. Returns (pa, pb, p_value one-sided pa<pb)."""
    na, nb = len(a), len(b)
    if not na or not nb:
        return float("nan"), float("nan"), float("nan")
    pa, pb = sum(a) / na, sum(b) / nb
    p = (sum(a) + sum(b)) / (na + nb)
    se = math.sqrt(p * (1 - p) * (1 / na + 1 / nb)) or 1e-9
    z = (pa - pb) / se
    return pa, pb, 0.5 * math.erfc(-z / math.sqrt(2))


def hour_t(rows_a, rows_b):
    """t-stat of mean(ret A) - mean(ret B), returns grouped by hour (per-hour means as observations)."""
    def per_hour(rows):
        g = defaultdict(list)
        for r in rows:
            if r["ret"] is not None:
                g[int(r["ts"] // 3600)].append(r["ret"])
        return {h: sum(v) / len(v) for h, v in g.items()}
    ha, hb = per_hour(rows_a), per_hour(rows_b)
    d = [ha[h] - hb[h] for h in ha if h in hb]
    if len(d) < 10:
        return float("nan"), len(d)
    m = sum(d) / len(d)
    s = math.sqrt(sum((x - m) ** 2 for x in d) / (len(d) - 1))
    return (m / (s / math.sqrt(len(d))) if s else float("nan")), len(d)


def report(rows, label=""):
    rows.sort(key=lambda r: r["ts"])
    days = sorted({int(r["ts"] // 86400) for r in rows})
    cut = days[int(len(days) * 0.6)] * 86400 if len(days) >= 2 else rows[len(rows) * 6 // 10]["ts"]
    L = [f"# M1 results {label}", "", f"{len(rows)} coins reached the checkpoint; days: {len(days)}", "",
         "| Split | PASS coins | dead-rate PASS | dead-rate FAIL | p (PASS<FAIL) | expectancy PASS | expectancy ALL | t (hours) | verdict parts |",
         "|---|---|---|---|---|---|---|---|---|"]
    ok = []
    for name, sel in (("DESIGN", lambda r: r["ts"] < cut), ("HOLDOUT", lambda r: r["ts"] >= cut)):
        s = [r for r in rows if sel(r)]
        P, F = [r for r in s if r["pass"]], [r for r in s if not r["pass"]]
        pa, pb, p = ztest([r["dead"] for r in P], [r["dead"] for r in F])
        rp = [r["ret"] for r in P if r["ret"] is not None]
        ra = [r["ret"] for r in s if r["ret"] is not None]
        ep = sum(rp) / len(rp) if rp else float("nan")
        ea = sum(ra) / len(ra) if ra else float("nan")
        t, n = hour_t(P, s)
        parts = (p < 0.01, t >= 2, len(P) >= 300 if name == "HOLDOUT" else True)
        ok.append(all(parts))
        L.append(f"| {name} | {len(P)} | {pa:.1%} | {pb:.1%} | {p:.4f} | {ep:+.2%} | {ea:+.2%} | {t:+.2f} ({n}h) | "
                 f"dead {'✓' if parts[0] else '✗'} · expectancy {'✓' if parts[1] else '✗'} · n {'✓' if parts[2] else '✗'} |")
    L += ["", "Each check alone (whole sample, dead-rate pass vs fail):", ""]
    for c in ("C1", "C2", "C3", "C4", "C5"):
        pa, pb, p = ztest([r["dead"] for r in rows if r[c]], [r["dead"] for r in rows if not r[c]])
        L.append(f"- {c}: pass {pa:.1%} vs fail {pb:.1%} (n pass {sum(r[c] for r in rows)}, p {p:.4f})")
    L += ["", f"**Verdict: {'CHECKS WORK' if all(ok) else 'NO EVIDENCE'}** (pre-registered: both splits must pass)."]
    return "\n".join(L), all(ok)


def synthetic(effect):
    """Fake coins for validating the code: normal coins = many small buyers; bundled coins = plus 8 identical
    big wallets (fail C1 and C3). If effect=True bundled coins die twice as often after the checkpoint."""
    import random
    random.seed(7)
    coins = []
    for i in range(5000):
        created = 1.79e9 + i * 150
        bundled = random.random() < 0.5
        vsol, vtok, tr, ts = 30.0, 1.073e9, [], created
        def trade(buy, sol, user):
            nonlocal vsol, vtok
            if buy:
                tok = vtok - vsol * vtok / (vsol + sol); vsol += sol; vtok -= tok
            else:
                tok = sol * vtok / vsol; out = vsol - vsol * vtok / (vtok + tok); vsol -= out; vtok += tok; sol = out
            tr.append({"ts": ts, "user": user, "buy": buy, "sol": sol, "tok": tok, "vsol": vsol, "vtok": vtok,
                       "price": vsol / vtok, "fee_bps": 95, "cfee_bps": 30})
        trade(True, 0.2, "dev")
        k = 0
        if bundled:
            for j in range(8):
                ts += 1; trade(True, 1.2, f"b{i}_{j}")
        while vsol < 50:                                         # many small buyers until past the checkpoint
            ts += random.expovariate(1 / 6); k += 1
            trade(random.random() < 0.8, min(random.lognormvariate(-2.2, 1.0), 0.9), f"u{i}_{k}")
        die = random.random() < ((0.6 if bundled else 0.3) if effect else 0.45)
        for j in range(200):
            ts += random.expovariate(1 / 8)
            if die and vsol > 31:
                trade(False, min(random.uniform(0.3, 1.5), vsol - 30.5), f"s{i}_{j}")
            elif not die:
                trade(random.random() < 0.55, random.uniform(0.05, 0.4), f"v{i}_{j}")
        coins.append({"mint": f"m{i}", "created": created, "creator": "dev", "trades": tr})
    return coins


def from_recordings():
    from memebot.data import download, load
    dest = os.path.join(os.path.dirname(__file__), "out", "raw")
    download(os.environ.get("GITHUB_REPOSITORY", "wahazzin/memecoin-trader"), dest, os.environ.get("GITHUB_TOKEN"),
             since=os.environ.get("M1_SINCE", "2026-10-07"))
    d = load(dest)
    tr, cr = d["trades"], d["creates"]
    gaps = sorted(g["at"] for g in d["gaps"])
    coins = []
    for mint, g in tr.groupby("mint"):
        c = cr[cr.mint == mint]
        if c.empty:
            continue                                   # born before recording: excluded
        created = int(c.ts.iloc[0])
        if any(created - 60 <= x <= created + 6000 for x in gaps):
            continue                                   # life overlaps a recorder gap: excluded
        coins.append({"mint": mint, "created": created, "creator": c.creator.iloc[0],
                      "trades": g.sort_values(["slot", "ts"]).to_dict("records")})
    return coins


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    if "--synthetic" in sys.argv:
        for eff in (True, False):
            text, _ = report(evaluate(synthetic(eff)), f"(SYNTHETIC, planted effect={eff})")
            print(text, "\n")
    else:
        text, _ = report(evaluate(from_recordings()))
        with open(os.path.join(OUT, "M1_results.md"), "w") as f:
            f.write(text + "\n")
        print(text)
