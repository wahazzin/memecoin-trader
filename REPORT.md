# Paper bot check-in (2026-11-21 01:20 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 898 / 162 / 21 | 897 | 23% | +0.2745 | -0.2166 | **-0.1054** | -94.5698 | 8.395 (top-ups 83.24) | -95.922 | 1 | 0 |
| `m1_random` | 946 / 107 / 114 | 945 | 25% | +0.2528 | -0.2148 | **-0.1000** | -94.5294 | 7.293 (top-ups 82.11) | -94.976 | 1 | 0 |

- Exit reasons: {'take_profit': 450, 'stop_loss': 1208, 'no_volume_15m': 183, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 776
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.685, m1_random +6.458
- Circuit breakers fired: 90
- Stream gaps logged: 100261

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
