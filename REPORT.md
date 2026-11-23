# Paper bot check-in (2026-11-23 04:09 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 956 / 167 / 21 | 955 | 23% | +0.2760 | -0.2155 | **-0.1028** | -98.1435 | 19.281 (top-ups 97.55) | -100.426 | 1 | 0 |
| `m1_random` | 985 / 109 / 114 | 985 | 24% | +0.2545 | -0.2137 | **-0.0996** | -98.1047 | 17.920 (top-ups 96.30) | -98.532 | 0 | 0 |

- Exit reasons: {'take_profit': 476, 'stop_loss': 1269, 'no_volume_15m': 194, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 824
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.778, m1_random +6.625
- Circuit breakers fired: 94
- Stream gaps logged: 102131

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
