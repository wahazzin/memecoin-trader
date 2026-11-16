# Paper bot check-in (2026-11-16 09:11 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 760 / 129 / 21 | 760 | 22% | +0.2558 | -0.2203 | **-0.1132** | -86.0010 | 16.946 (top-ups 83.24) | -86.653 | 0 | 0 |
| `m1_random` | 861 / 96 / 112 | 861 | 25% | +0.2568 | -0.2139 | **-0.0980** | -84.3870 | 17.485 (top-ups 82.11) | -84.787 | 0 | 0 |

- Exit reasons: {'take_profit': 409, 'stop_loss': 1057, 'no_volume_15m': 155}
- Sells priced by the verified curve formula because Jupiter had no route: 655
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.350, m1_random +6.131
- Circuit breakers fired: 81
- Stream gaps logged: 90026

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
