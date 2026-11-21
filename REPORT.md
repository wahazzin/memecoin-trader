# Paper bot check-in (2026-11-21 00:43 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 884 / 159 / 21 | 884 | 22% | +0.2739 | -0.2165 | **-0.1067** | -94.3079 | 8.562 (top-ups 83.24) | -95.922 | 0 | 0 |
| `m1_random` | 943 / 106 / 114 | 943 | 25% | +0.2528 | -0.2146 | **-0.0996** | -93.9421 | 7.906 (top-ups 82.11) | -94.363 | 0 | 0 |

- Exit reasons: {'take_profit': 446, 'stop_loss': 1197, 'no_volume_15m': 183, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 769
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.650, m1_random +6.456
- Circuit breakers fired: 90
- Stream gaps logged: 100261

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
