# Paper bot check-in (2026-10-07 22:58 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 49 / 7 / 0 | 45 | 20% | +0.4864 | -0.1960 | **-0.0595** | -2.6782 | 17.161 | -15.7% | 4 | 0 |
| `m1_random` | 7 / 2 / 1 | 7 | 43% | +0.1696 | -0.1646 | **-0.0214** | -0.1496 | 19.847 | -1.9% | 0 | 0 |

- Exit reasons: {'take_profit': 15, 'stop_loss': 29, 'no_volume_15m': 8}
- Sells priced by the verified curve formula because Jupiter had no route: 27
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.192, m1_random +0.030
- Circuit breakers fired: 0
- Stream gaps logged: 7

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
