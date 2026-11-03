# Paper bot check-in (2026-11-03 00:42 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 544 / 82 / 14 | 544 | 23% | +0.2713 | -0.2181 | **-0.1065** | -57.9576 | 16.081 (top-ups 54.23) | -58.740 | 0 | 0 |
| `m1_random` | 522 / 55 / 57 | 522 | 23% | +0.2599 | -0.2193 | **-0.1091** | -56.9760 | 16.848 (top-ups 53.97) | -57.280 | 0 | 0 |

- Exit reasons: {'take_profit': 263, 'stop_loss': 709, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 382
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.055, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65701

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
