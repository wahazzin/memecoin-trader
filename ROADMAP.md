# ROADMAP — memecoin-trader

Owner decision 2026-10-07: project 3 starts now, because project 2 is live and only needs to run
(its next milestones are the weekly check-in on 2026-10-12 and the learner arms from 2026-11-09).

| Phase | Goal | Done when | Status |
|---|---|---|---|
| 0 — Learn the game | Study experienced traders, extract testable rules | Rules written as hypotheses with sources | ✅ Setuh (19 videos) studied 2026-10-07 |
| 1 — Data probe | Which free sources give new tokens, trades, holders, wallet funding, OHLCV | `probe.md` on `research-out` | ✅ 2026-10-07: every pump.fun trade free via Solana logsSubscribe; no paid key needed |
| 2 — Recorder | Record every new Pump.fun coin + its trades 24/7 (our own dataset, no survivorship) | Running unattended, data growing | 🔄 live since 2026-10-07 ~19:30 UTC; checking size + gaps over the first day |
| 3 — Cost model | Real costs measured from transactions; fills from the exact curve formula / live Jupiter quotes | Formula = Jupiter within tolerance | ✅ 2026-10-07: costs measured (COST_FACTORS.md); formula = Jupiter to 0.0000% on 43 checks |
| 4 — Filter test (M1) | Do the anti-bundle checks actually lower the rug rate? (alone, pre-registered) | Verdict | 📝 pre-registered + code validated 2026-10-07; runs after 14 days of data (~2026-10-21) |
| 5 — Entry/exit test | "40–50% dip from local high" rule on filtered coins, after costs, vs random entry | Verdict | ⬜ |
| 6 — Live paper bot | Forward paper test of pre-registered arms (M1 checks vs random control), real-time | 6–8 weeks of paper results | 🔄 live since 2026-10-08 (BOT_SPEC.md); first check-in report each week |
| 7 — AI / social layer | Narrative/community quality via AI, tested alone | Verdict | ⬜ later |

Real money is not on this roadmap.
