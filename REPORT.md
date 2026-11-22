# Paper bot check-in (2026-11-22 00:25 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 916 / 162 / 21 | 916 | 23% | +0.2765 | -0.2162 | **-0.1048** | -96.0424 | 6.491 (top-ups 83.24) | -97.109 | 0 | 0 |
| `m1_random` | 948 / 108 / 114 | 948 | 25% | +0.2530 | -0.2146 | **-0.0997** | -94.5213 | 6.991 (top-ups 82.11) | -95.278 | 0 | 0 |

- Exit reasons: {'take_profit': 457, 'stop_loss': 1219, 'no_volume_15m': 187, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 794
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.714, m1_random +6.464
- Circuit breakers fired: 92
- Stream gaps logged: 101326

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
