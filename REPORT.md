# Paper bot check-in (2026-10-14 00:44 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 146 / 21 / 1 | 143 | 23% | +0.2964 | -0.2163 | **-0.0980** | -14.0071 | 19.666 (top-ups 13.81) | -74.4% | 3 | 0 |
| `m1_random` | 112 / 13 / 16 | 111 | 20% | +0.2252 | -0.2083 | **-0.1224** | -13.5850 | 20.455 (top-ups 14.10) | -70.7% | 1 | 0 |

- Exit reasons: {'take_profit': 58, 'stop_loss': 163, 'no_volume_15m': 33}
- Sells priced by the verified curve formula because Jupiter had no route: 98
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.463, m1_random +0.861
- Circuit breakers fired: 14
- Stream gaps logged: 6276

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
