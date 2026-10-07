# Paper bot check-in (2026-10-07 22:43 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 27 / 4 / 0 | 21 | 24% | +0.5015 | -0.2308 | **-0.0565** | -1.1860 | 18.801 | -9.7% | 6 | 0 |
| `m1_random` | 5 / 1 / 1 | 4 | 50% | +0.2219 | -0.2006 | **+0.0107** | +0.0426 | 20.041 | -0.6% | 1 | 0 |

- Exit reasons: {'take_profit': 10, 'stop_loss': 14, 'no_volume_15m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 14
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.095, m1_random +0.030
- Circuit breakers fired: 0
- Stream gaps logged: 6

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
