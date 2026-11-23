# Pre-registration M2 — Does "buy the 40–50% dip from the local high" work after costs?

**Written 2026-10-08, before any recorded data was analysed.** Git timestamp = proof. Changes only at
the bottom, dated, before the test runs.

## 1. Question and prior

Setuh's main entry: after a fresh coin makes a local high, buy a 40–50% drop from that high once buying
returns ("never top blast"). Gemini watched all his videos: **not one live trade on screen can be shown to
be a 40–50% dip entry**; the rule rests on hand-picked hindsight charts (e.g. Gnome 16k → 9k, ~44%).
Tested ALONE first (rule 9): no scam checks in the primary test.

Prior: low. Buying dips in coins that mostly die is catching knives; any edge must beat ~3% round-trip
costs on 0.5 SOL and the gap-through on stops (his own screen losses: −36%, −52%, −74%).

## 2. Data

Same as M1: our own recording, coins born while recording, from their first trade; coins whose life
overlaps a recorder gap are excluded; data from 2026-10-07 ~20:45 UTC; minimum 14 full days.

## 3. Signal (fixed)

Prices are market caps in multiples of the coin's launch price (thresholds follow the SOL price, as
Setuh says; launch ≈ 28 SOL ≈ his $2.4–4k).

1. Track the running high H since launch. The coin qualifies once **H ≥ 5× launch** (≈ his "ATH ≥ 15k").
2. **Dip band (primary): price between 50% and 60% of H** (= a 40–50% dip). Secondary bands, reported only:
   30–40% dip and 50–60% dip.
3. **Entry:** the first BUY trade (buying returns) while the price is inside the band, coin age ≤ 60 min.
   Fill at the next trade's reserves (exact curve formula, verified = Jupiter). One entry per coin per band.

## 4. Exits (fixed)

Primary: **+100% (2×)** from entry price (his most common on-screen exit), **−20% stop** (filled at the next
trade's real reserves, so gaps through are counted), 15 min without a trade, 60 min max hold.
Secondary (reported only): +50% take-profit instead of +100%.

## 5. Costs

Coin's actual fee from events (1.25% standard, higher creator fees as recorded) per side, priority fee
0.0015 SOL/side (measured p90), network fee, account rent 0.00204 SOL refunded on close. Size 0.5 SOL.

## 6. Control (the bar to beat)

**Random entry:** for each qualifying coin (H ≥ 5× launch), one entry at a uniformly random BUY trade
between qualification and age 60 min, same exits and costs. If the dip rule is real, it beats this.

## 7. Splits and verdict (fixed)

Chronological DESIGN (first 60% of days) / HOLDOUT (last 40%), holdout looked at once.
**PASS only if, in BOTH splits:**
1. expectancy per trade after all costs > 0, t ≥ 2 (trades grouped by hour), and
2. expectancy − random control expectancy > 0, t ≥ 2 (hour-matched), and
3. ≥ 300 entries in the holdout.
Otherwise NO EVIDENCE. Secondary bands / exits are reported but cannot produce a pass (3 bands × 2 exits
= 6 looks; only the pre-named primary counts).

A pass makes it a candidate paper-bot arm (forward test, separately specified). Combining it with the M1
checks is a later test (M3), only if both pass alone.

## 8. Ways we could fool ourselves

| Risk | Control |
|---|---|
| Hindsight charts (his examples) | Every coin that qualifies is tested, winners and losers |
| Tuning the band | Primary band fixed from his words; others reported only |
| Stops filling at exactly −20% | Fill at next real trade after the trigger |
| Regime | Chronological split, dates reported |
| Survivorship | Coins recorded from birth, including the ones that die |


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
