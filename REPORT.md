# Paper bot check-in (2026-11-23 00:51 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 929 / 167 / 21 | 929 | 23% | +0.2756 | -0.2167 | **-0.1049** | -97.4366 | 19.733 (top-ups 97.55) | -98.481 | 0 | 0 |
| `m1_random` | 974 / 109 / 114 | 974 | 25% | +0.2538 | -0.2138 | **-0.0991** | -96.5106 | 19.787 (top-ups 96.30) | -96.665 | 0 | 0 |

- Exit reasons: {'take_profit': 467, 'stop_loss': 1244, 'no_volume_15m': 191, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 807
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.729, m1_random +6.530
- Circuit breakers fired: 94
- Stream gaps logged: 101997

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
