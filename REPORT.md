# Paper bot check-in (2026-10-25 00:19 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 385 / 57 / 8 | 385 | 24% | +0.2643 | -0.2204 | **-0.1021** | -39.3014 | 6.063 (top-ups 25.51) | -195.5% | 0 | 0 |
| `m1_random` | 331 / 38 / 37 | 331 | 22% | +0.2450 | -0.2159 | **-0.1157** | -38.2878 | 7.040 (top-ups 25.42) | -191.2% | 0 | 0 |

- Exit reasons: {'take_profit': 179, 'stop_loss': 476, 'no_volume_15m': 61}
- Sells priced by the verified curve formula because Jupiter had no route: 234
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.380, m1_random +3.135
- Circuit breakers fired: 36
- Stream gaps logged: 35980

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
