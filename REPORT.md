# Paper bot check-in (2026-10-10 00:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 104 / 15 / 0 | 103 | 22% | +0.3133 | -0.2168 | **-0.0984** | -10.1398 | 9.794 | -51.9% | 1 | 0 |
| `m1_random` | 53 / 9 / 8 | 52 | 12% | +0.1912 | -0.2180 | **-0.1708** | -8.8831 | 11.096 | -45.0% | 1 | 0 |

- Exit reasons: {'take_profit': 35, 'stop_loss': 96, 'no_volume_15m': 24}
- Sells priced by the verified curve formula because Jupiter had no route: 74
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.362, m1_random +0.546
- Circuit breakers fired: 7
- Stream gaps logged: 2007

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
