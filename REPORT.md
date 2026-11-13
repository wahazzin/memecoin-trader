# Paper bot check-in (2026-11-13 21:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 715 / 121 / 21 | 715 | 22% | +0.2559 | -0.2187 | **-0.1125** | -80.4073 | 7.864 (top-ups 68.54) | -81.044 | 0 | 0 |
| `m1_random` | 821 / 90 / 112 | 821 | 25% | +0.2578 | -0.2132 | **-0.0968** | -79.4378 | 8.360 (top-ups 68.02) | -79.820 | 0 | 0 |

- Exit reasons: {'take_profit': 384, 'stop_loss': 1003, 'no_volume_15m': 149}
- Sells priced by the verified curve formula because Jupiter had no route: 615
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.214, m1_random +5.663
- Circuit breakers fired: 76
- Stream gaps logged: 86422

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
