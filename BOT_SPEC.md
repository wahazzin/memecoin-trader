# BOT SPEC — live paper bot v0.1 (forward test), written 2026-10-07 before it ever ran

Paper only. No wallet, no keys; the code cannot sign or send a transaction (a unit test checks this).

## What it does
1. Listens live to every pump.fun trade (Solana logsSubscribe) and every new coin (PumpPortal).
2. For each coin born while it listens, waits for the **M1 checkpoint** (age ≤ 40 min, price ≥ 2.5× launch)
   and runs the **same check code** as the pre-registered M1 test (`research/m1.py: coin_checks`).
3. Arms (20 SOL paper bankroll each, 0.5 SOL per trade, max 10 open):
   - `m1_pass`: buys when ALL checks pass.
   - `m1_random` (control): buys a random 10% of ALL checkpoint coins, checks ignored.
4. Exits (both arms): price +50% / −20% from entry, 15 min without a trade, or 60 min held.
5. **Fills:** live Jupiter quote now and 2 s later, fill at the worse one; if the second is >20% worse the
   order FAILS and fees are still paid. Plus measured costs not in the quote: priority fee 0.0015 SOL/side
   (p90), network fee, token-account rent 0.00204 SOL refunded on sell. "No route" = can't trade, logged.
6. **Circuit breaker:** an arm that loses 15% of its day-start equity stops buying for the rest of the UTC day.

## What counts as a result
The forward test is `m1_pass` vs `m1_random` (same entry moment). Judged on expectancy per trade after all
costs (rule 6), after at least 6 weeks of paper trading (rule 1), next to the M1 backtest verdict.
Weekly check-in: `memebot/report.py` (trades, win rate, avg win vs loss, expectancy, drawdown, breakers).

## Smoke tests before going live (2026-10-07/08, 4 runs × 15–20 min, throwaway state)
Found and fixed: equity valued at last price instead of real sell value; positions stuck because Jupiter
often has no sell route for fresh coins (now priced from the coin's on-chain curve, marked); one feed
field gave a wallet instead of the curve address (curve address now derived from the mint and its owner
verified). Last smoke: 26 buys, 21 sells, 0 stuck, circuit breaker fired correctly once.
Observed: prices at the checkpoint move ±50% within 2 s; the −20% stop often fills far lower when a coin
dumps. Smoke results are NOT evidence (minutes of data, thrown away).

## Known limits (stated, not hidden)
- Being first vs competing bots can't be paper-tested (COST_FACTORS #17).
- The 2-second delay is a fixed choice, not a measurement (a real landing time needs real transactions).
- After a coin graduates, its pump.fun trade stream stops; exits then fall to the 15-min/60-min rules and
  are filled by Jupiter via PumpSwap.

## Amendment B1 (2026-10-13): weekly paper top-up

**Why:** after ~6 days both arms were down ~70% (m1_pass 6.19 SOL, m1_random 5.90 SOL from 20). With a
small bankroll the 15% daily circuit breaker trips after only a few stops, so the arms trade less and the
forward test collects fewer trades. The thing being tested is **expectancy per trade** (m1_pass vs
m1_random), which doesn't depend on bankroll size, so refilling paper money keeps the test collecting data
without changing any rule. Owner approved 2026-10-13.

**Rule:** once per ISO week (UTC), at the first check of the week, each arm's paper cash is topped up so
its equity is back at 20 SOL. The first top-up happens as soon as this code runs (week 2026-W42). Both arms
get the identical rule. Entry rules, checks, exits, sizes, costs and the circuit breaker are unchanged.
A top-up is added to the day's start equity, so a deposit never hides or triggers a circuit breaker.

**Honesty:** every top-up is logged (`TOP_UP` in events.jsonl). The report shows total top-ups per arm and
computes max drawdown with them removed. Total P&L comes from closed trades only, so top-ups can't
flatter it. Real money would never be "topped up" to hide losses: at go-live the bankroll is fixed.

## Amendment B2 (2026-11-23): exits measured from the price actually paid

**Why:** the +50% / −20% exits were measured from the stream price at the moment of entry. At the checkpoint a
coin's price moves ±50% within 2 s and our fill is the worse of two quotes 2 s apart, so the price paid is often far
from the stream price. Result: 83 of 394 "take-profit" exits up to 2026-11-16 (21%) closed at a LOSS (median −28%,
~8 s after entry), and stops fired relative to a price we never paid. Found in the weekly reviews (W46/W47);
owner approved 2026-11-23, before any B2 result existed.

**Rule:** take-profit when the stream price ≥ 1.5 × `paid_price`; stop-loss when ≤ 0.8 × `paid_price`
(`paid_price` = SOL per token actually paid, before the 1.25% pump.fun fee, already stored since 2026-10-07).
Identical for both arms. Entries, checks, sizes, costs, time exits, circuit breaker and B1 top-ups unchanged.
Sell records carry `exit_ref`.

**Honesty:** this changes the exit rule, so the m1_pass vs m1_random comparison **restarts at 2026-11-24 00:00
UTC** (first full UTC day on which every running bot has the B2 code). The 6-week minimum (rule 1) counts again
from that date → earliest judgement ≈ 2027-01-05. Trades before B2 stay in the log and are reported separately;
they are never merged into the B2 numbers. `memebot/report.py` adds a "Since amendment B2" table.

**Data-feed fix shipped with B2 (same date):** new coins were taken only from PumpPortal. A live check
(research/probe_create, 2026-11-23 08:06–08:09 UTC) decoded **48** new coins from pump.fun's own on-chain
CreateEvents vs **12** from PumpPortal (11 in both; creator and symbol agreed 11/11). So the bot (and recorder) saw
only a fraction of new coins, and nothing at all while PumpPortal was down (2026-11-20 10:37–16:00 UTC). From B2
on, both sources are used (first one wins). Same feed for both arms; non-SOL coins are still skipped.
