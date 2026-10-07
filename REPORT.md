# Paper bot check-in (2026-10-07 22:38 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 19 / 3 / 0 | 12 | 25% | +0.4658 | -0.2856 | **-0.0977** | -1.1728 | 18.601 | -9.7% | 7 | 0 |
| `m1_random` | 5 / 1 / 1 | 3 | 67% | +0.2219 | -0.3014 | **+0.0475** | +0.1425 | 20.119 | -0.2% | 2 | 0 |

- Exit reasons: {'take_profit': 5, 'stop_loss': 10}
- Sells priced by the verified curve formula because Jupiter had no route: 7
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.051, m1_random +0.000
- Circuit breakers fired: 0
- Stream gaps logged: 2

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
