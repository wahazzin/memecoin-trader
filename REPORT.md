# Paper bot check-in (2026-10-26 00:57 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 400 / 59 / 9 | 399 | 25% | +0.2657 | -0.2219 | **-0.1021** | -40.7550 | 19.387 (top-ups 39.90) | -203.4% | 1 | 0 |
| `m1_random` | 339 / 39 / 38 | 339 | 22% | +0.2435 | -0.2168 | **-0.1176** | -39.8811 | 19.579 (top-ups 39.64) | -199.6% | 0 | 0 |

- Exit reasons: {'take_profit': 183, 'stop_loss': 494, 'no_volume_15m': 61}
- Sells priced by the verified curve formula because Jupiter had no route: 245
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.160
- Circuit breakers fired: 38
- Stream gaps logged: 42501

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
