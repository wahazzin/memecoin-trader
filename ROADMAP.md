# ROADMAP — memecoin-trader

Owner decision 2026-10-07: project 3 starts now, because project 2 is live and only needs to run
(its next milestones are the weekly check-in on 2026-10-12 and the learner arms from 2026-11-09).

| Phase | Goal | Done when | Status |
|---|---|---|---|
| 0 — Learn the game | Study experienced traders, extract testable rules | Rules written as hypotheses with sources | ✅ Setuh (19 videos) studied 2026-10-07 |
| 1 — Data probe | Which free sources give new tokens, trades, holders, wallet funding, OHLCV | `probe.md` on `research-out` | ✅ 2026-10-07: every pump.fun trade free via Solana logsSubscribe; no paid key needed |
| 2 — Recorder | Record every new Pump.fun coin + its trades 24/7 (our own dataset, no survivorship) | Running unattended, data growing | 🔄 live since 2026-10-07 ~19:30 UTC; checking size + gaps over the first day |
| 3 — Cost model | Fees + priority fees + slippage simulated from the bonding curve formula | Fills match real trades within tolerance | ⬜ |
| 4 — Filter test | Do the anti-bundle checks actually lower the rug rate? (alone, pre-registered) | Verdict | ⬜ |
| 5 — Entry/exit test | "40–50% dip from local high" rule on filtered coins, after costs, vs random entry | Verdict | ⬜ |
| 6 — Live paper bot | Only rules that passed, simulated in real time | 6–8 weeks of paper results | ⬜ |
| 7 — AI / social layer | Narrative/community quality via AI, tested alone | Verdict | ⬜ later |

Real money is not on this roadmap.
