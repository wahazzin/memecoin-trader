# Paper bot check-in (2026-11-23 04:42 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 963 / 167 / 21 | 962 | 23% | +0.2753 | -0.2152 | **-0.1030** | -99.1269 | 18.366 (top-ups 97.55) | -100.426 | 1 | 0 |
| `m1_random` | 987 / 109 / 114 | 986 | 24% | +0.2538 | -0.2137 | **-0.0994** | -98.0139 | 18.011 (top-ups 96.30) | -98.558 | 1 | 0 |

- Exit reasons: {'take_profit': 478, 'stop_loss': 1274, 'no_volume_15m': 195, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 827
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.872, m1_random +6.625
- Circuit breakers fired: 94
- Stream gaps logged: 102133

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
