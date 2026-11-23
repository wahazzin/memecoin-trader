# Paper bot check-in (2026-11-23 05:44 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 970 / 167 / 21 | 970 | 23% | +0.2755 | -0.2149 | **-0.1026** | -99.5592 | 17.603 (top-ups 97.55) | -100.519 | 0 | 0 |
| `m1_random` | 989 / 109 / 114 | 989 | 24% | +0.2536 | -0.2134 | **-0.0991** | -98.0105 | 18.015 (top-ups 96.30) | -98.572 | 0 | 0 |

- Exit reasons: {'take_profit': 481, 'stop_loss': 1279, 'no_volume_15m': 198, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 832
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.886, m1_random +6.625
- Circuit breakers fired: 94
- Stream gaps logged: 102144

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
