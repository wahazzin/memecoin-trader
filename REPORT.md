# Paper bot check-in (2026-10-25 00:08 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 383 / 55 / 7 | 381 | 24% | +0.2647 | -0.2210 | **-0.1025** | -39.0414 | 6.369 (top-ups 25.51) | -194.0% | 2 | 0 |
| `m1_random` | 331 / 37 / 37 | 331 | 22% | +0.2450 | -0.2159 | **-0.1157** | -38.2878 | 7.041 (top-ups 25.42) | -191.2% | 0 | 0 |

- Exit reasons: {'take_profit': 178, 'stop_loss': 474, 'no_volume_15m': 60}
- Sells priced by the verified curve formula because Jupiter had no route: 231
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.380, m1_random +3.135
- Circuit breakers fired: 36
- Stream gaps logged: 35976

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
