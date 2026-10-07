# Paper bot check-in (2026-10-07 21:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 12 / 2 / 1 | 9 | 11% | +0.3370 | -0.2830 | **-0.2141** | -1.9272 | 16.942 | -10.2% | 3 | 2 |
| `m1_random` | 14 / 1 / 3 | 10 | 30% | +0.1938 | -0.2214 | **-0.0969** | -0.9688 | 18.941 | -5.1% | 4 | 0 |

- Exit reasons: {'stop_loss': 14, 'take_profit': 2, 'no_volume_15m': 3}
- Sells priced by the verified curve formula because Jupiter had no route: 3
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_random +0.107, m1_pass +0.009
- Circuit breakers fired: 1
- Stream gaps logged: 0

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
