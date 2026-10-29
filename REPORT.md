# Paper bot check-in (2026-10-29 01:32 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 461 / 67 / 11 | 458 | 24% | +0.2690 | -0.2240 | **-0.1066** | -48.8437 | 10.902 (top-ups 39.90) | -49.862 | 3 | 0 |
| `m1_random` | 416 / 44 / 39 | 415 | 22% | +0.2464 | -0.2173 | **-0.1134** | -47.0652 | 12.456 (top-ups 39.64) | -47.983 | 1 | 0 |

- Exit reasons: {'take_profit': 212, 'stop_loss': 586, 'no_volume_15m': 75}
- Sells priced by the verified curve formula because Jupiter had no route: 301
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.773, m1_random +3.357
- Circuit breakers fired: 44
- Stream gaps logged: 52949

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
