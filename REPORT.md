# Paper bot check-in (2026-11-19 00:50 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 836 / 146 / 21 | 836 | 22% | +0.2623 | -0.2171 | **-0.1098** | -91.8275 | 11.340 (top-ups 83.24) | -92.259 | 0 | 0 |
| `m1_random` | 925 / 106 / 114 | 925 | 25% | +0.2536 | -0.2133 | **-0.0977** | -90.3903 | 11.086 (top-ups 82.11) | -91.184 | 0 | 0 |

- Exit reasons: {'take_profit': 438, 'stop_loss': 1151, 'no_volume_15m': 172}
- Sells priced by the verified curve formula because Jupiter had no route: 730
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.518, m1_random +6.383
- Circuit breakers fired: 86
- Stream gaps logged: 95078

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
