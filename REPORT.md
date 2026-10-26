# Paper bot check-in (2026-10-26 00:52 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 399 / 58 / 9 | 398 | 25% | +0.2657 | -0.2212 | **-0.1013** | -40.3292 | 18.843 (top-ups 39.90) | -203.4% | 1 | 0 |
| `m1_random` | 338 / 39 / 38 | 337 | 21% | +0.2450 | -0.2175 | **-0.1187** | -39.9869 | 19.560 (top-ups 39.64) | -199.6% | 1 | 0 |

- Exit reasons: {'take_profit': 182, 'stop_loss': 492, 'no_volume_15m': 61}
- Sells priced by the verified curve formula because Jupiter had no route: 244
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.137
- Circuit breakers fired: 38
- Stream gaps logged: 42489

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
