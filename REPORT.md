# Paper bot check-in (2026-10-24 00:37 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 378 / 55 / 7 | 378 | 25% | +0.2647 | -0.2210 | **-0.1015** | -38.3593 | 7.009 (top-ups 25.51) | -190.8% | 0 | 0 |
| `m1_random` | 327 / 37 / 36 | 326 | 22% | +0.2450 | -0.2138 | **-0.1125** | -36.6593 | 8.359 (top-ups 25.42) | -185.9% | 1 | 0 |

- Exit reasons: {'take_profit': 177, 'stop_loss': 469, 'no_volume_15m': 58}
- Sells priced by the verified curve formula because Jupiter had no route: 230
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.380, m1_random +3.135
- Circuit breakers fired: 34
- Stream gaps logged: 33276

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
