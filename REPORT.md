# Paper bot check-in (2026-10-22 01:08 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 360 / 53 / 6 | 360 | 25% | +0.2671 | -0.2192 | **-0.0990** | -35.6357 | 9.741 (top-ups 25.51) | -177.4% | 0 | 0 |
| `m1_random` | 304 / 34 / 35 | 304 | 22% | +0.2510 | -0.2129 | **-0.1091** | -33.1770 | 12.161 (top-ups 25.42) | -167.0% | 0 | 0 |

- Exit reasons: {'take_profit': 167, 'stop_loss': 441, 'no_volume_15m': 56}
- Sells priced by the verified curve formula because Jupiter had no route: 219
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.342, m1_random +2.877
- Circuit breakers fired: 31
- Stream gaps logged: 26161

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
