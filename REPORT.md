# Paper bot check-in (2026-11-11 00:56 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 685 / 114 / 19 | 684 | 23% | +0.2600 | -0.2191 | **-0.1112** | -76.0874 | 12.082 (top-ups 68.54) | -76.824 | 1 | 0 |
| `m1_random` | 741 / 85 / 102 | 741 | 24% | +0.2518 | -0.2116 | **-0.0990** | -73.3742 | 13.902 (top-ups 68.02) | -74.278 | 0 | 0 |

- Exit reasons: {'take_profit': 353, 'stop_loss': 931, 'no_volume_15m': 141}
- Sells priced by the verified curve formula because Jupiter had no route: 575
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +4.994
- Circuit breakers fired: 70
- Stream gaps logged: 80883

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
