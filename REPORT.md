# Paper bot check-in (2026-10-15 00:04 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 179 / 22 / 1 | 178 | 23% | +0.2884 | -0.2110 | **-0.0960** | -17.0792 | 16.615 (top-ups 13.81) | -86.2% | 1 | 0 |
| `m1_random` | 146 / 19 / 21 | 145 | 20% | +0.2338 | -0.2066 | **-0.1186** | -17.1904 | 16.821 (top-ups 14.10) | -86.5% | 1 | 0 |

- Exit reasons: {'take_profit': 73, 'stop_loss': 213, 'no_volume_15m': 37}
- Sells priced by the verified curve formula because Jupiter had no route: 116
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.632, m1_random +1.404
- Circuit breakers fired: 16
- Stream gaps logged: 7517

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
