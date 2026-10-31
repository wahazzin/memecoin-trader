# Paper bot check-in (2026-10-31 01:25 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 484 / 71 / 14 | 483 | 24% | +0.2651 | -0.2209 | **-0.1062** | -51.2966 | 8.433 (top-ups 39.90) | -52.674 | 1 | 0 |
| `m1_random` | 457 / 49 / 44 | 457 | 22% | +0.2454 | -0.2179 | **-0.1145** | -52.3153 | 7.203 (top-ups 39.64) | -52.594 | 0 | 0 |

- Exit reasons: {'take_profit': 227, 'stop_loss': 628, 'no_volume_15m': 85}
- Sells priced by the verified curve formula because Jupiter had no route: 328
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.872, m1_random +3.457
- Circuit breakers fired: 48
- Stream gaps logged: 59032

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
