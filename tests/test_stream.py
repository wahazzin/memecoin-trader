"""Amendment B-data (2026-11-23): the day-by-day path must give the SAME verdicts/tables as the old all-at-once
path, and the data-based outage rule must exclude exactly the coins whose window overlaps an outage."""
import os
import sys
import unittest
from datetime import date

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research import m1, m2, stream, w1  # noqa: E402


def by_day(coins):
    days = {}
    for c in sorted(coins, key=lambda c: (int(c["created"] // 86400), c["mint"])):
        days.setdefault(int(c["created"] // 86400), []).append(c)
    return days


class TestStreamEquivalence(unittest.TestCase):
    def check_w1(self, effect):
        coins = w1.synthetic(effect)
        days = by_day(coins)
        ordered = [c for d in sorted(days) for c in days[d]]
        old_text, a, b = w1.run(ordered, boot=300)
        pos_days = sorted({int(p["ts"] // 86400) for p in w1.positions(ordered)})
        src = lambda only: ((d, days.get(d, [])) for d in pos_days if d in only)
        new_text, a2, b2 = w1.run_stream(src, pos_days, boot=300)
        self.assertEqual((a, b), (a2, b2))
        self.assertEqual(old_text, new_text)

    def test_w1_stream_equals_old_planted(self):
        self.check_w1(True)

    def test_w1_stream_equals_old_none(self):
        self.check_w1(False)

    def test_m1_m2_generator_equals_list(self):
        coins = m1.synthetic(True)[:800]
        self.assertEqual(m1.report(m1.evaluate(iter(coins)))[0], m1.report(m1.evaluate(coins))[0])
        coins = m2.synthetic(True)[:800]
        self.assertEqual(m2.report(m2.evaluate(iter(coins)))[0], m2.report(m2.evaluate(coins))[0])


class TestOutageRule(unittest.TestCase):
    def frames(self):
        d = date(2026, 11, 10)
        t0 = stream._hour_ts(d, 0)
        rows = []
        # whole-market curve trades every 2 s, except a 45 s hole at t0+20000 (outage)
        for k, ts in enumerate([x for x in range(t0 - 3600, t0 + 26 * 3600, 2) if not (t0 + 20000 < x < t0 + 20045)]):
            rows.append({"ts": ts, "mint": "BG", "user": f"u{k}", "buy": True, "sol": .1, "tok": 1.0, "vsol": 40.0,
                         "vtok": 9e8, "venue": None, "slot": ts, "sig": f"s{k}", "price": 1e-7})
        for ts in range(t0 - 3600, t0 + 26 * 3600, 30):
            rows.append({"ts": ts, "mint": "SW", "user": "p", "buy": True, "sol": .1, "tok": 1.0, "vsol": 50.0,
                         "vtok": 9e8, "venue": "pumpswap", "slot": ts, "sig": f"w{ts}", "price": 1e-7})
        def coin(mint, c0, vmax):
            out = [{"ts": c0 + 10 * i, "mint": mint, "user": "a", "buy": True, "sol": .1, "tok": 1.0,
                    "vsol": 31.0 + (vmax - 31.0) * i / 9, "vtok": 9e8, "venue": None, "slot": c0 + 10 * i,
                    "sig": f"{mint}{i}", "price": 1e-7} for i in range(10)]
            return out
        rows += coin("OK1", t0 + 1000, 60) + coin("HIT", t0 + 18000, 60) + coin("LATE", t0 + 26000, 60)
        tr = pd.DataFrame(rows).sort_values(["slot", "ts"]).reset_index(drop=True)
        cr = pd.DataFrame([{"ts": t0 + 1000, "mint": "OK1", "creator": "dev"},
                           {"ts": t0 + 18000, "mint": "HIT", "creator": "dev"},
                           {"ts": t0 + 26000, "mint": "LATE", "creator": "dev"},
                           {"ts": t0 + 90000, "mint": "NEXTDAY", "creator": "dev"}])
        return d, t0, tr, cr

    def test_outage_excludes_only_overlapping_coins(self):
        d, t0, tr, cr = self.frames()
        st = {}
        coins = list(stream.coins_from_frames(tr, cr, t0, t0 + 86400, t0 - 3600, t0 + 26 * 3600, st))
        mints = [c["mint"] for c in coins]
        self.assertIn("OK1", mints)
        self.assertIn("LATE", mints)                      # created after the hole: window doesn't overlap
        self.assertNotIn("HIT", mints)                    # window [17940, 24000] contains the 45 s hole
        self.assertNotIn("NEXTDAY", mints)                # created on the next day: not this day's coin
        self.assertEqual(st["excluded_curve_outage"], 1)

    def test_swap_outage_only_matters_near_graduation(self):
        d, t0, tr, cr = self.frames()
        tr = tr[~((tr.venue == "pumpswap") & (tr.ts > t0 + 1500) & (tr.ts < t0 + 1800))]   # 300 s swap hole
        tr2 = tr.copy()
        coins = list(stream.coins_from_frames(tr2, cr, t0, t0 + 86400, t0 - 3600, t0 + 26 * 3600))
        self.assertIn("OK1", [c["mint"] for c in coins])  # never near graduation (vsol max 60)
        tr3 = tr.copy()
        tr3.loc[tr3.mint == "OK1", "vsol"] = 105.0
        coins = list(stream.coins_from_frames(tr3, cr, t0, t0 + 86400, t0 - 3600, t0 + 26 * 3600))
        self.assertNotIn("OK1", [c["mint"] for c in coins])

    def test_missing_values_become_none(self):
        d, t0, tr, cr = self.frames()
        tr["fee_total_bps"] = float("nan")
        tr["fee_bps"] = float("nan")
        c = next(c for c in stream.coins_from_frames(tr, cr, t0, t0 + 86400, t0 - 3600, t0 + 26 * 3600) if c["mint"] == "OK1")
        t = c["trades"][-1]
        self.assertIsNone(t["fee_total_bps"]); self.assertIsNone(t["venue"])
        self.assertEqual(m1.outcomes(c["trades"][1:], c["trades"][0]["price"], 0.0125, c["trades"][0]["ts"])[1] ==
                         m1.outcomes(c["trades"][1:], c["trades"][0]["price"], 0.0125, c["trades"][0]["ts"])[1], True)  # not NaN

    def test_silences_edges(self):
        self.assertEqual(stream.silences([100, 110], 0, 200, 30), [(0, 100), (110, 200)])
        self.assertEqual(stream.silences([10, 30, 50], 0, 60, 30), [])


if __name__ == "__main__":
    unittest.main()
