# Paper bot check-in (2026-10-13 05:23 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 135 / 21 / 1 | 135 | 22% | +0.2979 | -0.2161 | **-0.1019** | -13.7565 | 6.189 | -69.6% | 0 | 0 |
| `m1_random` | 108 / 13 / 15 | 108 | 19% | +0.2167 | -0.2091 | **-0.1303** | -14.0702 | 5.903 | -70.7% | 0 | 0 |

- Exit reasons: {'take_profit': 53, 'stop_loss': 158, 'no_volume_15m': 32}
- Sells priced by the verified curve formula because Jupiter had no route: 95
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.403, m1_random +0.861
- Circuit breakers fired: 14
- Stream gaps logged: 5083

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
