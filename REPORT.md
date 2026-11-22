# Paper bot check-in (2026-11-22 00:51 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 920 / 163 / 21 | 920 | 23% | +0.2752 | -0.2166 | **-0.1049** | -96.5121 | 6.351 (top-ups 83.24) | -97.278 | 0 | 0 |
| `m1_random` | 949 / 108 / 114 | 949 | 25% | +0.2528 | -0.2146 | **-0.0994** | -94.3132 | 7.530 (top-ups 82.11) | -95.278 | 0 | 0 |

- Exit reasons: {'take_profit': 460, 'stop_loss': 1221, 'no_volume_15m': 187, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 795
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.729, m1_random +6.464
- Circuit breakers fired: 92
- Stream gaps logged: 101346

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
