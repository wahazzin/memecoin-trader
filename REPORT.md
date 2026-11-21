# Paper bot check-in (2026-11-21 01:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 907 / 162 / 21 | 907 | 23% | +0.2773 | -0.2163 | **-0.1047** | -94.9979 | 7.866 (top-ups 83.24) | -95.956 | 0 | 0 |
| `m1_random` | 946 / 108 / 114 | 946 | 25% | +0.2528 | -0.2146 | **-0.0999** | -94.5513 | 7.294 (top-ups 82.11) | -94.976 | 0 | 0 |

- Exit reasons: {'take_profit': 453, 'stop_loss': 1214, 'no_volume_15m': 185, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 785
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.685, m1_random +6.458
- Circuit breakers fired: 90
- Stream gaps logged: 100261

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
