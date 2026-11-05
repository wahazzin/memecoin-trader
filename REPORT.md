# Paper bot check-in (2026-11-05 17:39 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 584 / 92 / 16 | 584 | 22% | +0.2672 | -0.2187 | **-0.1097** | -64.0666 | 9.957 (top-ups 54.23) | -64.638 | 0 | 0 |
| `m1_random` | 655 / 73 / 81 | 654 | 25% | +0.2550 | -0.2122 | **-0.0971** | -63.5279 | 10.179 (top-ups 53.97) | -64.033 | 1 | 0 |

- Exit reasons: {'take_profit': 309, 'stop_loss': 810, 'no_volume_15m': 119}
- Sells priced by the verified curve formula because Jupiter had no route: 468
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.706
- Circuit breakers fired: 59
- Stream gaps logged: 72680

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
