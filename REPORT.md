# Paper bot check-in (2026-11-16 11:17 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 760 / 129 / 21 | 760 | 22% | +0.2558 | -0.2203 | **-0.1132** | -86.0010 | 16.946 (top-ups 83.24) | -86.653 | 0 | 0 |
| `m1_random` | 867 / 96 / 112 | 867 | 25% | +0.2571 | -0.2144 | **-0.0980** | -84.9812 | 16.891 (top-ups 82.11) | -85.378 | 0 | 0 |

- Exit reasons: {'take_profit': 411, 'stop_loss': 1061, 'no_volume_15m': 155}
- Sells priced by the verified curve formula because Jupiter had no route: 655
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.350, m1_random +6.131
- Circuit breakers fired: 82
- Stream gaps logged: 90070

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
