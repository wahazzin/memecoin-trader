"""
w1.py -- Test W1 exactly as pre-registered in research/W1_PREREG.md:
  W1a: do the top-50 design-period wallets keep making money in the holdout (skill vs luck)?
  W1b: does copying them 2 s late, at real reserves and with all our costs, beat copying random wallets?
Usage: python -m research.w1 [--synthetic]
"""
import math
import os
import random
import sys
from collections import defaultdict

from research.m1 import buy_tokens, sell_value, PRIO, RENT, NET, from_recordings

OUT = os.path.join(os.path.dirname(__file__), "out", "w1")
SIZE, TOP_N, DELAY = 0.5, 50, 2.0
MIN_CLOSED, MAX_OPEN_SHARE, MIN_HOLDOUT = 20, 0.30, 5
CLOSED_FRAC, COPY_EXIT_FRAC = 0.90, 0.50
BOOT = 10_000


def fee_of(t):
    if t.get("fee_total_bps") is not None:                    # PumpSwap: fee tier from the event
        return t["fee_total_bps"] / 1e4
    return ((t.get("fee_bps") or 95) + (t.get("cfee_bps") or 30)) / 1e4


def _num(x):
    return 0.0 if x is None or (isinstance(x, float) and math.isnan(x)) else float(x)


def cash_flow(t):
    """SOL the wallet paid (buy, negative) or received (sell, positive), incl. the fees in the event."""
    if t.get("fee_total_bps") is not None:                    # PumpSwap row: fee from the bps in the event
        f = t["fee_total_bps"] / 1e4
        return -t["sol"] * (1 + f) if t["buy"] else t["sol"] * (1 - f)
    fees = _num(t.get("fee")) + _num(t.get("cfee"))
    if not fees:
        fees = t["sol"] * fee_of(t)
    return -(t["sol"] + fees) if t["buy"] else t["sol"] - fees


# ---------- wallet positions ----------
def positions(coins):
    """One row per (wallet, coin) inside the recorded window. Creator positions dropped."""
    rows = []
    for c in coins:
        acc = {}
        for i, t in enumerate(c["trades"]):
            u = t.get("user")
            if not u or u == c.get("creator"):
                continue
            p = acc.get(u)
            if p is None:
                if not t["buy"]:
                    continue                                    # tokens from elsewhere: not a position we can score
                p = acc[u] = {"wallet": u, "mint": c["mint"], "first_i": i, "ts": t["ts"],
                              "bought": 0.0, "sold": 0.0, "pnl": 0.0, "exit_i": None}
            if t["buy"]:
                p["bought"] += t["tok"]
            else:
                p["sold"] += t["tok"]
                if p["exit_i"] is None and p["sold"] >= COPY_EXIT_FRAC * p["bought"]:
                    p["exit_i"] = i                             # copy signal: wallet has sold half
            p["pnl"] += cash_flow(t)
        for p in acc.values():
            p["closed"] = p["bought"] > 0 and p["sold"] >= CLOSED_FRAC * p["bought"]
            rows.append(p)
    return rows


def split_cut(rows):
    days = sorted({int(r["ts"] // 86400) for r in rows})
    return days[int(len(days) * 0.6)] * 86400 if len(days) >= 2 else sorted(r["ts"] for r in rows)[len(rows) * 6 // 10]


def eligible(design):
    by = defaultdict(list)
    for p in design:
        by[p["wallet"]].append(p)
    out = {}
    for w, ps in by.items():
        closed = [p for p in ps if p["closed"]]
        if len(closed) >= MIN_CLOSED and 1 - len(closed) / len(ps) <= MAX_OPEN_SHARE:
            out[w] = sum(p["pnl"] for p in closed)
    return out


# ---------- copy simulation ----------
def copy_trade(tr, p, delay):
    """Buy 0.5 SOL at the first trade >= delay s after the wallet's first buy; sell at the first trade >= delay s
    after it has sold half (backstops: 60 min held, end of the recorded window). Returns net return or None."""
    t0 = tr[p["first_i"]]["ts"]
    i = next((k for k in range(p["first_i"] + 1, len(tr)) if tr[k]["ts"] >= t0 + delay), None)
    if i is None:
        return None
    e = tr[i]
    tok = buy_tokens(e["vsol"], e["vtok"], SIZE, fee_of(e))
    cost = SIZE + PRIO + RENT + NET
    x = None
    if p["exit_i"] is not None and p["exit_i"] > i:
        ts = tr[p["exit_i"]]["ts"]
        x = next((k for k in range(p["exit_i"] + 1, len(tr)) if tr[k]["ts"] >= ts + delay), None)
    if x is None or tr[x]["ts"] - e["ts"] > 3600:
        late = [k for k in range(i, len(tr)) if tr[k]["ts"] - e["ts"] <= 3600]
        x = late[-1]                                            # 60-min backstop / end of window
    xt = tr[x]
    proceeds = sell_value(xt["vsol"], xt["vtok"], tok, fee_of(xt)) - PRIO - NET + RENT
    return proceeds / cost - 1


# ---------- statistics ----------
def boot_ci(xs, rng, n=BOOT):
    if not xs:
        return float("nan"), float("nan")
    ms = sorted(sum(rng.choice(xs) for _ in xs) / len(xs) for _ in range(n))
    return ms[int(0.025 * n)], ms[int(0.975 * n)]


def boot_diff_ci(a, b, rng, n=BOOT):
    if not a or not b:
        return float("nan"), float("nan")
    ds = sorted(sum(rng.choice(a) for _ in a) / len(a) - sum(rng.choice(b) for _ in b) / len(b) for _ in range(n))
    return ds[int(0.025 * n)], ds[int(0.975 * n)]


def tstat(xs):
    if len(xs) < 10:
        return float("nan")
    m = sum(xs) / len(xs)
    s = math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
    return m / (s / math.sqrt(len(xs))) if s else float("nan")


def spearman(a, b):
    def rank(v):
        o = sorted(range(len(v)), key=lambda i: v[i])
        r = [0] * len(v)
        for k, i in enumerate(o):
            r[i] = k
        return r
    if len(a) < 3:
        return float("nan")
    ra, rb = rank(a), rank(b)
    n = len(a)
    return 1 - 6 * sum((x - y) ** 2 for x, y in zip(ra, rb)) / (n * (n * n - 1))


def hourly(rows):
    g = defaultdict(list)
    for ts, r in rows:
        g[int(ts // 3600)].append(r)
    return {h: sum(v) / len(v) for h, v in g.items()}


# ---------- the test ----------
def run(coins, label="", boot=BOOT):
    rng = random.Random(7)
    trades = {c["mint"]: c["trades"] for c in coins}
    pos = positions(coins)
    if not pos:
        return f"# W1 results {label}\n\nNo positions.", False, False
    cut = split_cut(pos)
    design = [p for p in pos if p["ts"] < cut]
    hold = [p for p in pos if p["ts"] >= cut]
    elig = eligible(design)
    top = [w for w, _ in sorted(elig.items(), key=lambda kv: -kv[1])[:TOP_N]]
    topset = set(top)
    hb = defaultdict(list)
    for p in hold:
        if p["closed"] and p["wallet"] in elig:
            hb[p["wallet"]].append(p["pnl"])
    hmean = {w: sum(v) / len(v) for w, v in hb.items() if len(v) >= MIN_HOLDOUT}
    top_h = [hmean[w] for w in top if w in hmean]
    rest_h = [m for w, m in hmean.items() if w not in topset]
    lo, hi = boot_ci(top_h, rng, boot)
    dlo, dhi = boot_diff_ci(top_h, rest_h, rng, boot)
    both = [w for w in hmean]
    rho = spearman([elig[w] for w in both], [hmean[w] for w in both])
    w1a = bool(top_h) and sum(top_h) / len(top_h) > 0 and lo > 0 and dlo > 0

    L = [f"# W1 results {label}", "",
         f"positions: {len(pos)} (design {len(design)}, holdout {len(hold)}); eligible wallets: {len(elig)}; "
         f"top group: {len(top)}; with ≥{MIN_HOLDOUT} holdout closed positions: top {len(top_h)}, others {len(rest_h)}", "",
         "## W1a — do the design-period top wallets keep winning in the holdout?", "",
         "| Group | Wallets | Mean holdout P&L / closed position (SOL) | 95% CI |", "|---|---|---|---|",
         f"| Top {TOP_N} | {len(top_h)} | {(sum(top_h) / len(top_h)) if top_h else float('nan'):+.4f} | {lo:+.4f} … {hi:+.4f} |",
         f"| Other eligible | {len(rest_h)} | {(sum(rest_h) / len(rest_h)) if rest_h else float('nan'):+.4f} | — |",
         "", f"Top minus others: 95% CI {dlo:+.4f} … {dhi:+.4f}. Spearman design vs holdout (all eligible, reported only): {rho:+.3f}",
         "", f"**W1a: {'PASS' if w1a else 'NO EVIDENCE'}**", "",
         "## W1b — copying them (buy/sell after the wallet, real reserves, all costs, 0.5 SOL)", "",
         "| Copy | Delay | n | Win rate | Expectancy/trade | t (hours) | vs random-wallet copy: diff | t |", "|---|---|---|---|---|---|---|---|"]

    pool = defaultdict(list)                                    # control: holdout positions of non-top eligible wallets
    for p in hold:
        if p["wallet"] in elig and p["wallet"] not in topset:
            pool[int(p["ts"] // 3600)].append(p)
    w1b = False
    for name, group in ((f"top {TOP_N}", topset), ("top 10", set(top[:10]))):
        for delay in (DELAY, 1.0, 5.0):
            crng = random.Random(13)
            rows, ctrl = [], []
            for p in hold:
                if p["wallet"] not in group:
                    continue
                r = copy_trade(trades[p["mint"]], p, delay)
                if r is None:
                    continue
                rows.append((p["ts"], r))
                cands = pool.get(int(p["ts"] // 3600))
                if cands:
                    q = crng.choice(cands)
                    rc = copy_trade(trades[q["mint"]], q, delay)
                    if rc is not None:
                        ctrl.append((q["ts"], rc))
            if not rows:
                L.append(f"| {name} | {delay:g} s | 0 | — | — | — | — | — |")
                continue
            h, hc = hourly(rows), hourly(ctrl)
            e = sum(r for _, r in rows) / len(rows)
            t = tstat(list(h.values()))
            d = [h[k] - hc[k] for k in h if k in hc]
            dm = sum(d) / len(d) if d else float("nan")
            dt = tstat(d)
            primary = name == f"top {TOP_N}" and delay == DELAY
            L.append(f"| {name}{' **(primary)**' if primary else ''} | {delay:g} s | {len(rows)} | "
                     f"{sum(r > 0 for _, r in rows) / len(rows):.0%} | {e:+.2%} | {t:+.2f} | {dm:+.2%} | {dt:+.2f} |")
            if primary:
                w1b = e > 0 and t >= 2 and dm > 0 and dt >= 2 and len(rows) >= 300
    L += ["", f"**W1b (primary: top {TOP_N}, {DELAY:g} s delay): {'PASS' if w1b else 'NO EVIDENCE'}**",
          "", "Pre-registered: W1a = top group's holdout mean > 0 AND beats other eligible wallets (95% bootstrap CIs "
          "above 0). W1b = copy expectancy > 0 with t ≥ 2 AND beats random-wallet copy with t ≥ 2, ≥ 300 copied trades. "
          "Rows other than the primary are reported only. See research/W1_PREREG.md."]
    return "\n".join(L), w1a, w1b


# ---------- synthetic validation ----------
def synthetic(effect, n_coins=3000, days=10):
    """Fake pump.fun coins on the real curve. ~30% of coins get a 10-minute rally later in life, then dump.
    effect=True: 50 'skilled' wallets buy those rallies as they start and sell near the top (skill that
    persists and is slow enough to copy). effect=False: the same 50 wallets trade at random like everyone."""
    rng = random.Random(21 if effect else 22)
    skilled = [f"S{i}" for i in range(50)]
    randoms = [f"R{i}" for i in range(1500)]
    coins = []
    span = days * 86400
    for ci in range(n_coins):
        created = 1.79e9 + ci * span / n_coins
        acts = []                                               # (t_offset, wallet, kind, size)
        rally = rng.random() < 0.30
        r0 = rng.uniform(600, 3000)
        for _ in range(15):
            w = rng.choice(randoms)
            tb = rng.uniform(5, 4800)
            acts.append((tb, w, "buy", rng.uniform(0.1, 1.0)))
            acts.append((tb + rng.uniform(60, 1200), w, "sell", 0))
        if rally:
            for k in range(60):                                 # rally: 10 min of buying, then a dump
                acts.append((r0 + 20 + k * 10, f"B{ci}", "buy", 0.8))
            for k in range(60):
                acts.append((r0 + 640 + k * 8, f"B{ci}", "sellpart", 0))
        for w in rng.sample(skilled, 3):
            if effect and rally:
                acts.append((r0 + rng.uniform(0, 15), w, "buy", rng.uniform(0.3, 1.0)))
                acts.append((r0 + rng.uniform(480, 560), w, "sell", 0))
            elif not effect and rng.random() < 0.3:
                tb = rng.uniform(5, 4800)
                acts.append((tb, w, "buy", rng.uniform(0.3, 1.0)))
                acts.append((tb + rng.uniform(60, 1200), w, "sell", 0))
        acts.sort()
        vsol, vtok = 30.0, 1.073e9
        held = defaultdict(float)
        tr = []
        for off, w, kind, size in acts:
            if off > 6000:
                continue
            if kind == "buy":
                sol = size / 1.0125
                tok = vtok - vsol * vtok / (vsol + sol)
                vsol += sol; vtok -= tok; held[w] += tok
                tr.append({"ts": created + off, "user": w, "buy": True, "sol": sol, "tok": tok, "vsol": vsol,
                           "vtok": vtok, "fee_bps": 95, "cfee_bps": 30})
            else:
                tok = held[w] if kind == "sell" else held[w] / 25
                if tok <= 0:
                    continue
                out = vsol - vsol * vtok / (vtok + tok)
                vsol -= out; vtok += tok; held[w] -= tok
                tr.append({"ts": created + off, "user": w, "buy": False, "sol": out, "tok": tok, "vsol": vsol,
                           "vtok": vtok, "fee_bps": 95, "cfee_bps": 30})
        for t in tr:
            t["price"] = t["vsol"] / t["vtok"]
        coins.append({"mint": f"m{ci}", "created": created, "creator": "dev", "trades": tr})
    return coins


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    if "--synthetic" in sys.argv:
        for eff in (True, False):
            text, a, b = run(synthetic(eff), f"(SYNTHETIC, planted effect={eff})", boot=2000)
            print(text, "\n")
    else:
        text, a, b = run(from_recordings())
        with open(os.path.join(OUT, "W1_results.md"), "w") as f:
            f.write(text + "\n")
        print(text)
