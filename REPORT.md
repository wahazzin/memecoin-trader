# Paper bot check-in (2026-10-24 12:20 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 379 / 55 / 7 | 379 | 25% | +0.2647 | -0.2211 | **-0.1019** | -38.6055 | 6.763 (top-ups 25.51) | -192.0% | 0 | 0 |
| `m1_random` | 331 / 37 / 36 | 331 | 22% | +0.2450 | -0.2159 | **-0.1157** | -38.2878 | 7.041 (top-ups 25.42) | -191.2% | 0 | 0 |

- Exit reasons: {'take_profit': 178, 'stop_loss': 472, 'no_volume_15m': 60}
- Sells priced by the verified curve formula because Jupiter had no route: 230
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.380, m1_random +3.135
- Circuit breakers fired: 36
- Stream gaps logged: 34195

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
