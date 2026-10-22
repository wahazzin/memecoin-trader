# Paper bot check-in (2026-10-22 18:50 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 360 / 53 / 6 | 360 | 25% | +0.2671 | -0.2192 | **-0.0990** | -35.6357 | 9.741 (top-ups 25.51) | -177.4% | 0 | 0 |
| `m1_random` | 315 / 36 / 35 | 315 | 22% | +0.2494 | -0.2132 | **-0.1118** | -35.2260 | 10.106 (top-ups 25.42) | -176.0% | 0 | 0 |

- Exit reasons: {'take_profit': 170, 'stop_loss': 448, 'no_volume_15m': 57}
- Sells priced by the verified curve formula because Jupiter had no route: 220
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.342, m1_random +2.928
- Circuit breakers fired: 32
- Stream gaps logged: 29959

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
