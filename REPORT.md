# Paper bot check-in (2026-11-23 06:37 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 977 / 171 / 21 | 976 | 23% | +0.2747 | -0.2146 | **-0.1023** | -99.8582 | 17.295 (top-ups 97.55) | -100.660 | 1 | 0 |
| `m1_random` | 991 / 109 / 114 | 991 | 24% | +0.2536 | -0.2135 | **-0.0995** | -98.5716 | 17.452 (top-ups 96.30) | -99.000 | 0 | 0 |

- Exit reasons: {'take_profit': 484, 'stop_loss': 1282, 'no_volume_15m': 200, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 837
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.886, m1_random +6.627
- Circuit breakers fired: 94
- Stream gaps logged: 102169

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
