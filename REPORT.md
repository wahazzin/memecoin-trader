# Paper bot check-in (2026-10-09 18:14 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 95 / 12 / 0 | 95 | 22% | +0.3246 | -0.2085 | **-0.0907** | -8.6153 | 11.349 | -44.3% | 0 | 0 |
| `m1_random` | 49 / 8 / 8 | 49 | 12% | +0.1912 | -0.2150 | **-0.1652** | -8.0965 | 11.885 | -41.0% | 0 | 0 |

- Exit reasons: {'take_profit': 32, 'stop_loss': 88, 'no_volume_15m': 24}
- Sells priced by the verified curve formula because Jupiter had no route: 67
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.340, m1_random +0.543
- Circuit breakers fired: 6
- Stream gaps logged: 1433

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
