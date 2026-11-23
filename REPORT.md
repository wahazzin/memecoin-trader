# Paper bot check-in (2026-11-23 06:10 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 976 / 170 / 21 | 975 | 23% | +0.2747 | -0.2147 | **-0.1023** | -99.7023 | 17.294 (top-ups 97.55) | -100.660 | 1 | 0 |
| `m1_random` | 990 / 109 / 114 | 990 | 24% | +0.2536 | -0.2132 | **-0.0991** | -98.0937 | 17.931 (top-ups 96.30) | -98.572 | 0 | 0 |

- Exit reasons: {'take_profit': 484, 'stop_loss': 1281, 'no_volume_15m': 199, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 836
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.886, m1_random +6.627
- Circuit breakers fired: 94
- Stream gaps logged: 102164

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
