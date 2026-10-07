# Paper bot check-in (2026-10-07 23:03 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 49 / 7 / 0 | 46 | 20% | +0.4864 | -0.1997 | **-0.0655** | -3.0112 | 16.898 | -17.0% | 3 | 0 |
| `m1_random` | 9 / 2 / 1 | 7 | 43% | +0.1696 | -0.1646 | **-0.0214** | -0.1496 | 19.783 | -1.9% | 2 | 0 |

- Exit reasons: {'take_profit': 15, 'stop_loss': 30, 'no_volume_15m': 8}
- Sells priced by the verified curve formula because Jupiter had no route: 27
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.192, m1_random +0.030
- Circuit breakers fired: 1
- Stream gaps logged: 7

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
