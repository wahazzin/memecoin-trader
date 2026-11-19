# Paper bot check-in (2026-11-19 01:58 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 864 / 152 / 21 | 863 | 22% | +0.2720 | -0.2168 | **-0.1075** | -92.7458 | 10.037 (top-ups 83.24) | -93.593 | 1 | 0 |
| `m1_random` | 932 / 106 / 114 | 932 | 25% | +0.2538 | -0.2131 | **-0.0974** | -90.7749 | 11.075 (top-ups 82.11) | -91.195 | 0 | 0 |

- Exit reasons: {'take_profit': 444, 'stop_loss': 1175, 'no_volume_15m': 176}
- Sells priced by the verified curve formula because Jupiter had no route: 754
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.604, m1_random +6.383
- Circuit breakers fired: 87
- Stream gaps logged: 95130

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
