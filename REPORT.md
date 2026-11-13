# Paper bot check-in (2026-11-13 01:28 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 715 / 121 / 21 | 715 | 22% | +0.2559 | -0.2187 | **-0.1125** | -80.4073 | 7.864 (top-ups 68.54) | -81.044 | 0 | 0 |
| `m1_random` | 807 / 89 / 111 | 807 | 25% | +0.2593 | -0.2138 | **-0.0965** | -77.9094 | 9.893 (top-ups 68.02) | -78.288 | 0 | 0 |

- Exit reasons: {'take_profit': 378, 'stop_loss': 996, 'no_volume_15m': 148}
- Sells priced by the verified curve formula because Jupiter had no route: 613
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.214, m1_random +5.604
- Circuit breakers fired: 75
- Stream gaps logged: 84759

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
