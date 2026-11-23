# Pre-registration M1 — Do Setuh's scam checks actually avoid dying coins?

**Written 2026-10-07, before any recorded data was analysed** (the recorder started today; only data
quality was looked at). Git timestamp = proof. Changes only at the bottom, dated, before the test runs.

## 1. Question and prior

Setuh's edge is mostly *rug avoidance*. Test that alone first (project rule 9): among fresh pump.fun
coins at the same moment of their life, do coins that pass his checks die less often, and does a plain
mechanical trade on them do better than on all coins? This does NOT test his entry timing (that's M2).

Prior: moderate. Bundles and dev dumps are real and visible on-chain; but scammers adapt, and pump.fun
coins die so often that "less bad" may still be bad.

## 2. Data

Our own recording (recorder, phase 2): every pump.fun trade of every coin created while recording,
from its first trade. Coins created during a recorder gap (logged in status files) are excluded.
Minimum before running: **14 full days** of recording.

## 3. Checkpoint (when a coin is judged)

The first moment a coin, **age ≤ 40 min**, reaches **market cap ≥ 2.5× its launch market cap**
(launch ≈ 28 SOL → checkpoint ≈ 70 SOL, roughly Setuh's "final stretch ≥ ~$8k"). Each coin is judged
once. Everything below is computed only from trades **before** the checkpoint.

## 4. The checks (Setuh's, translated to data; fixed now)

| # | Check | Pass if |
|---|---|---|
| C1 | Biggest holder (excluding the bonding curve) | ≤ 4% of supply |
| C2 | Creator (dev) holding | ≤ 5% of supply |
| C3 | Equal-size buyers (bundle tell): among the 10 biggest holders, buy sizes in SOL | coefficient of variation ≥ 0.25 (not near-identical) |
| C4 | Launch candle: price ×2.5 within the first 60 s with zero sells | not true |
| C5 | Creator fee | ≤ 0.30% (higher fees = cost filter) |

Holdings = net tokens bought minus sold per wallet since creation (includes the dev's first buy).
Limitation stated now: wallet-to-wallet token transfers are not in the trade stream, so holdings can be
understated for wallets that receive transfers. Funding-source clustering (Setuh's "funded from the
same place") needs wallet history lookups and is left for M1b.

**PASS = C1–C5 all pass.**

## 5. Outcomes

1. **Dead:** within 60 min after the checkpoint, price falls to ≤ 20% of the checkpoint price before it
   ever reaches +50%.
2. **Mechanical trade:** buy 0.5 SOL at the checkpoint price (exact formula, verified vs Jupiter),
   exit at the first of: +50% price, −20% price, 15 min without a trade, 60 min. Costs: actual coin
   fee from events + measured overhead p90 (priority 0.0015 SOL/side, account rent 0.002 SOL,
   network fee). Fill = next trade's reserves after the trigger (no same-tick fills).

## 6. Splits

Chronological: **DESIGN = first 60% of days, HOLDOUT = last 40%**, holdout looked at once.

## 7. Verdict (fixed)

The checks **WORK** only if, in BOTH splits:
1. dead-rate(PASS) < dead-rate(FAIL), two-proportion z-test p < 0.01, and
2. mechanical expectancy per trade after all costs: PASS > ALL coins, difference with t ≥ 2
   (trades grouped by hour for the t-stat), and
3. ≥ 300 PASS coins in the holdout.

Each check C1–C5 is also reported alone (pass vs fail dead-rates), not as a pass criterion.
Whether the PASS trade is profitable in absolute terms is reported, but profitability is M2's question.

## 8. Ways we could fool ourselves

| Risk | Control |
|---|---|
| Lookahead | All checks use trades before the checkpoint only |
| Picking the checkpoint after seeing results | Fixed here (2.5× launch mcap, age ≤ 40 min) |
| Tuning thresholds | Setuh's own numbers, fixed here |
| One market regime | Chronological design/holdout; dates reported |
| Recorder gaps | Coins born in a gap excluded; gap list published |
| Fill realism | Formula verified vs Jupiter (0.0000% on 43 checks); next-trade fills; measured costs |

## Amendment A1 (2026-10-07, before any recorded data was analysed)

Found while validating the analysis code on synthetic data: on the bonding curve the price can't go
below the launch price, and the checkpoint is 2.5× launch, so the lowest possible price after the
checkpoint is ~40% of it. "Dead = price ≤ 20% of checkpoint" could never happen.
**New definition: dead = price ≤ 50% of the checkpoint price within 60 min, before reaching +50%**
(i.e. gave back most of the run toward the launch floor). Everything else unchanged.

Also fixed before data: data for M1 starts with the recorder run of **2026-10-07 ~20:45 UTC** (first run
with full signatures and 100-minute tick history). Earlier hours are excluded.

Code validation (`python -m research.m1 --synthetic`): planted effect → CHECKS WORK in both splits;
no effect → NO EVIDENCE. The analysis can detect a real effect and doesn't invent one.


## Amendment A2 (2026-10-08, before any recorded data was analysed)

From pump.fun's official docs + a live check: (1) coins whose quote is not SOL (~1% of trades; their SOL
reserve fields are 0) are **excluded**; (2) after a coin graduates, its trades on PumpSwap are now recorded
and used for the follow-up/exit, priced from the pool's effective reserves after each trade and charged the
PumpSwap fee shown in that trade's event (fees depend on market cap). Before this, a graduating coin would
have looked like it stopped trading. Recorder change effective with the run started 2026-10-08 ~08:45 UTC.
Code re-validated on synthetic data (planted effect → pass; none → no evidence).

## Amendment B-data (2026-11-23, approved by the owner, written before this test was ever run on real data)

No outcome of this test (dead rates, returns, wallet P&L, copy results) has been computed or looked at. Only
data-quality counts were looked at (how many coins each gap rule would keep; see below).

1. **Recorder gaps are measured from the data, not from the reconnect log.** The recorder logs every websocket
   reconnect of each of its three streams (12k+ per week, mostly 1–2 s); the original rule ("coin excluded if any
   logged gap falls in its window") would have dropped most coins for a logging reason. New rule: a **curve
   outage** is any interval > **30 s** with no recorded pump.fun bonding-curve trade in the whole market (the
   recorder sees ~8 curve trades per second; 28 of 43 such silences on 2026-11-20 coincide with a logged RPC
   reconnect, i.e. they are real holes). A **PumpSwap outage** is any interval > 120 s with no recorded PumpSwap
   trade. A coin is excluded if its window [created − 60 s, created + 6000 s] overlaps a curve outage, or overlaps
   a PumpSwap outage while the coin's curve vsol reached ≥ 100 SOL (near graduation at ~115). 30 s is the
   threshold proposed to the owner before any data was examined; it was not tuned. Data-quality check done while
   writing this (no outcomes): it keeps ~79% of coins on 2026-10-09 but only ~20% on November days, which had many
   holes (incl. ~5–6 h with almost no data on 2026-11-05 and 2026-11-20). Counts are printed with the results.
2. **Day-by-day loading.** The old loader held all ~22 GB of recordings in memory (impossible on a runner).
   `research/stream.py` loads 6 hours of births at a time (plus 1 h before and 2 h after, so every 100-minute
   window is complete), with identical per-coin data. Tested: on synthetic data the streamed path gives exactly
   the same tables/verdicts as the old path (tests/test_stream.py).
3. **Missing values.** The old loader passed pandas NaN for missing fields; the analysis code tests
   `fee_total_bps is not None` / `fee_bps or 95`, which NaN breaks (every curve-trade exit fee would have been NaN).
   Missing values are now None, as the code expects.
4. **Data window fixed now:** coins created 2026-10-07 20:45 UTC → 2026-11-22 23:59 UTC (47 calendar days).
   DESIGN/HOLDOUT = first 60% / last 40% of those days by the existing code (cut at day index int(0.6 × days)).
   Processing order is chronological (day, 6-hour chunk, mint); seeded random draws therefore differ from a
   whole-data run in global mint order. All rules, thresholds, seeds and verdict criteria are unchanged.
