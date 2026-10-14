# Paper bot check-in (2026-10-14 00:18 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 140 / 21 / 1 | 139 | 22% | +0.2953 | -0.2187 | **-0.1041** | -14.4655 | 19.033 (top-ups 13.81) | -74.4% | 1 | 0 |
| `m1_random` | 109 / 13 / 16 | 109 | 19% | +0.2298 | -0.2091 | **-0.1246** | -13.5770 | 20.493 (top-ups 14.10) | -70.7% | 0 | 0 |

- Exit reasons: {'take_profit': 55, 'stop_loss': 161, 'no_volume_15m': 32}
- Sells priced by the verified curve formula because Jupiter had no route: 95
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.463, m1_random +0.861
- Circuit breakers fired: 14
- Stream gaps logged: 6276

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
