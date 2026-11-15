# Paper bot check-in (2026-11-15 00:18 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 721 / 122 / 21 | 721 | 22% | +0.2559 | -0.2188 | **-0.1135** | -81.8021 | 6.468 (top-ups 68.54) | -82.438 | 0 | 0 |
| `m1_random` | 831 / 91 / 112 | 831 | 25% | +0.2571 | -0.2140 | **-0.0972** | -80.7924 | 7.003 (top-ups 68.02) | -81.178 | 0 | 0 |

- Exit reasons: {'take_profit': 389, 'stop_loss': 1014, 'no_volume_15m': 149}
- Sells priced by the verified curve formula because Jupiter had no route: 621
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.214, m1_random +5.766
- Circuit breakers fired: 78
- Stream gaps logged: 88240

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
