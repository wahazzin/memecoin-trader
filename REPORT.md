# Paper bot check-in (2026-10-25 00:44 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 387 / 57 / 8 | 387 | 24% | +0.2643 | -0.2205 | **-0.1027** | -39.7568 | 5.606 (top-ups 25.51) | -197.7% | 0 | 0 |
| `m1_random` | 334 / 38 / 37 | 334 | 22% | +0.2450 | -0.2158 | **-0.1165** | -38.9005 | 6.427 (top-ups 25.42) | -194.2% | 0 | 0 |

- Exit reasons: {'take_profit': 179, 'stop_loss': 481, 'no_volume_15m': 61}
- Sells priced by the verified curve formula because Jupiter had no route: 236
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.380, m1_random +3.135
- Circuit breakers fired: 37
- Stream gaps logged: 35984

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
