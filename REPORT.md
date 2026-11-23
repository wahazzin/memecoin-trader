# Paper bot check-in (2026-11-23 00:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 927 / 167 / 21 | 927 | 23% | +0.2756 | -0.2168 | **-0.1048** | -97.1076 | 20.062 (top-ups 97.55) | -98.481 | 0 | 0 |
| `m1_random` | 972 / 109 / 114 | 972 | 25% | +0.2538 | -0.2137 | **-0.0988** | -96.0250 | 5.817 (top-ups 82.11) | -96.452 | 0 | 0 |

- Exit reasons: {'take_profit': 467, 'stop_loss': 1240, 'no_volume_15m': 191, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 805
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.729, m1_random +6.521
- Circuit breakers fired: 94
- Stream gaps logged: 101997

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
