# Paper bot check-in (2026-11-12 00:34 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 690 / 114 / 20 | 690 | 22% | +0.2592 | -0.2192 | **-0.1118** | -77.1092 | 11.175 (top-ups 68.54) | -77.731 | 0 | 0 |
| `m1_random` | 772 / 86 / 110 | 772 | 24% | +0.2504 | -0.2122 | **-0.0989** | -76.3827 | 11.427 (top-ups 68.02) | -76.753 | 0 | 0 |

- Exit reasons: {'take_profit': 361, 'stop_loss': 959, 'no_volume_15m': 142}
- Sells priced by the verified curve formula because Jupiter had no route: 588
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +5.268
- Circuit breakers fired: 72
- Stream gaps logged: 82080

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
