# Paper bot check-in (2026-11-15 02:13 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 730 / 126 / 21 | 730 | 22% | +0.2540 | -0.2193 | **-0.1136** | -82.9546 | 5.307 (top-ups 68.54) | -83.601 | 0 | 0 |
| `m1_random` | 836 / 91 / 112 | 836 | 25% | +0.2571 | -0.2138 | **-0.0977** | -81.7043 | 6.091 (top-ups 68.02) | -82.089 | 0 | 0 |

- Exit reasons: {'take_profit': 393, 'stop_loss': 1023, 'no_volume_15m': 150}
- Sells priced by the verified curve formula because Jupiter had no route: 625
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.214, m1_random +5.905
- Circuit breakers fired: 79
- Stream gaps logged: 88285

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
