# Paper bot check-in (2026-11-14 03:33 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 720 / 122 / 21 | 720 | 22% | +0.2559 | -0.2190 | **-0.1134** | -81.6817 | 6.588 (top-ups 68.54) | -82.317 | 0 | 0 |
| `m1_random` | 829 / 91 / 112 | 829 | 25% | +0.2572 | -0.2136 | **-0.0972** | -80.5404 | 7.516 (top-ups 68.02) | -80.664 | 0 | 0 |

- Exit reasons: {'take_profit': 388, 'stop_loss': 1012, 'no_volume_15m': 149}
- Sells priced by the verified curve formula because Jupiter had no route: 621
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.214, m1_random +5.766
- Circuit breakers fired: 77
- Stream gaps logged: 86826

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
