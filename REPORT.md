# Paper bot check-in (2026-11-21 00:59 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 888 / 159 / 21 | 888 | 23% | +0.2744 | -0.2165 | **-0.1054** | -93.6011 | 9.486 (top-ups 83.24) | -95.922 | 0 | 0 |
| `m1_random` | 943 / 107 / 114 | 943 | 25% | +0.2528 | -0.2146 | **-0.0996** | -93.9421 | 7.905 (top-ups 82.11) | -94.365 | 0 | 0 |

- Exit reasons: {'take_profit': 448, 'stop_loss': 1199, 'no_volume_15m': 183, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 772
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.650, m1_random +6.456
- Circuit breakers fired: 90
- Stream gaps logged: 100261

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
