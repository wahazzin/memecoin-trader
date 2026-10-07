# Paper bot check-in (2026-10-07 22:33 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 14 / 1 / 0 | 8 | 12% | +0.7042 | -0.3007 | **-0.1751** | -1.4010 | 18.382 | -9.7% | 6 | 0 |
| `m1_random` | 2 / 1 / 1 | 1 | 100% | +0.1564 | +0.0000 | **+0.1564** | +0.1564 | 20.132 | -0.1% | 1 | 0 |

- Exit reasons: {'take_profit': 2, 'stop_loss': 7}
- Sells priced by the verified curve formula because Jupiter had no route: 4
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.051
- Circuit breakers fired: 0
- Stream gaps logged: 0

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
