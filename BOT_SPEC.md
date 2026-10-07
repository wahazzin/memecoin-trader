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

## Known limits (stated, not hidden)
- Being first vs competing bots can't be paper-tested (COST_FACTORS #17).
- The 2-second delay is a fixed choice, not a measurement (a real landing time needs real transactions).
- After a coin graduates, its pump.fun trade stream stops; exits then fall to the 15-min/60-min rules and
  are filled by Jupiter via PumpSwap.
