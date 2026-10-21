# Paper bot check-in (2026-10-21 03:36 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 350 / 53 / 6 | 350 | 25% | +0.2727 | -0.2168 | **-0.0951** | -33.2851 | 12.094 (top-ups 25.51) | -165.9% | 0 | 0 |
| `m1_random` | 289 / 34 / 32 | 289 | 21% | +0.2584 | -0.2123 | **-0.1113** | -32.1719 | 13.166 (top-ups 25.42) | -162.4% | 0 | 0 |

- Exit reasons: {'take_profit': 160, 'stop_loss': 424, 'no_volume_15m': 55}
- Sells priced by the verified curve formula because Jupiter had no route: 217
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.257, m1_random +2.611
- Circuit breakers fired: 29
- Stream gaps logged: 23201

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
