# Paper bot check-in (2026-11-16 00:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 737 / 127 / 21 | 737 | 22% | +0.2539 | -0.2194 | **-0.1141** | -84.0654 | 18.888 (top-ups 83.24) | -84.712 | 0 | 0 |
| `m1_random` | 840 / 91 / 112 | 840 | 25% | +0.2572 | -0.2130 | **-0.0971** | -81.6031 | 20.000 (top-ups 82.11) | -82.273 | 0 | 0 |

- Exit reasons: {'take_profit': 397, 'stop_loss': 1028, 'no_volume_15m': 152}
- Sells priced by the verified curve formula because Jupiter had no route: 629
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.257, m1_random +6.022
- Circuit breakers fired: 80
- Stream gaps logged: 89493

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
