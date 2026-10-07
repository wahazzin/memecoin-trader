# Paper bot check-in (2026-10-07 22:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 21 / 1 / 0 | 17 | 12% | +0.3311 | -0.2102 | **-0.1465** | -2.4907 | 17.485 | -6.0% | 4 | 0 |
| `m1_random` | 5 / 1 / 0 | 4 | 50% | +0.2774 | -0.2182 | **+0.0296** | +0.1184 | 20.095 | -1.9% | 1 | 0 |

- Exit reasons: {'stop_loss': 14, 'take_profit': 6, 'no_volume_15m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 15
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.000, m1_random +0.018
- Circuit breakers fired: 1
- Stream gaps logged: 5

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
