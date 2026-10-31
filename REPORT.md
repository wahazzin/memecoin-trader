# Paper bot check-in (2026-10-31 01:31 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 484 / 71 / 14 | 484 | 24% | +0.2651 | -0.2207 | **-0.1063** | -51.4411 | 8.289 (top-ups 39.90) | -52.674 | 0 | 0 |
| `m1_random` | 457 / 49 / 44 | 457 | 22% | +0.2454 | -0.2179 | **-0.1145** | -52.3153 | 7.194 (top-ups 39.64) | -52.603 | 0 | 0 |

- Exit reasons: {'take_profit': 227, 'stop_loss': 629, 'no_volume_15m': 85}
- Sells priced by the verified curve formula because Jupiter had no route: 328
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.872, m1_random +3.457
- Circuit breakers fired: 48
- Stream gaps logged: 59039

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
