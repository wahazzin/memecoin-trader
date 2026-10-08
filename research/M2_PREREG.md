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
