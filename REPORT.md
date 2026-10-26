# Paper bot check-in (2026-10-26 00:11 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 389 / 57 / 8 | 389 | 24% | +0.2642 | -0.2202 | **-0.1019** | -39.6423 | 20.256 (top-ups 39.90) | -197.7% | 0 | 0 |
| `m1_random` | 336 / 39 / 38 | 336 | 21% | +0.2450 | -0.2166 | **-0.1177** | -39.5472 | 5.779 (top-ups 25.42) | -197.4% | 0 | 0 |

- Exit reasons: {'take_profit': 179, 'stop_loss': 485, 'no_volume_15m': 61}
- Sells priced by the verified curve formula because Jupiter had no route: 237
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.432, m1_random +3.137
- Circuit breakers fired: 38
- Stream gaps logged: 42309

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
