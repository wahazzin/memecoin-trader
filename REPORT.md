# Paper bot check-in (2026-11-13 03:12 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 715 / 121 / 21 | 715 | 22% | +0.2559 | -0.2187 | **-0.1125** | -80.4073 | 7.864 (top-ups 68.54) | -81.044 | 0 | 0 |
| `m1_random` | 810 / 89 / 112 | 810 | 25% | +0.2584 | -0.2137 | **-0.0966** | -78.2177 | 9.583 (top-ups 68.02) | -78.597 | 0 | 0 |

- Exit reasons: {'take_profit': 381, 'stop_loss': 996, 'no_volume_15m': 148}
- Sells priced by the verified curve formula because Jupiter had no route: 614
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.214, m1_random +5.634
- Circuit breakers fired: 75
- Stream gaps logged: 84957

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
