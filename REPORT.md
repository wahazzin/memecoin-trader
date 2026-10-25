# Paper bot check-in (2026-10-25 14:12 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 387 / 57 / 8 | 387 | 24% | +0.2643 | -0.2205 | **-0.1027** | -39.7568 | 5.606 (top-ups 25.51) | -197.7% | 0 | 0 |
| `m1_random` | 336 / 39 / 38 | 336 | 21% | +0.2450 | -0.2166 | **-0.1177** | -39.5472 | 5.779 (top-ups 25.42) | -197.4% | 0 | 0 |

- Exit reasons: {'take_profit': 179, 'stop_loss': 483, 'no_volume_15m': 61}
- Sells priced by the verified curve formula because Jupiter had no route: 236
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.380, m1_random +3.137
- Circuit breakers fired: 38
- Stream gaps logged: 39377

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
