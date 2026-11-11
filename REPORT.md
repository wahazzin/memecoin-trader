# Paper bot check-in (2026-11-11 05:06 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 688 / 114 / 20 | 688 | 23% | +0.2592 | -0.2192 | **-0.1114** | -76.6401 | 11.644 (top-ups 68.54) | -77.262 | 0 | 0 |
| `m1_random` | 753 / 86 / 106 | 753 | 25% | +0.2505 | -0.2114 | **-0.0979** | -73.7513 | 14.059 (top-ups 68.02) | -74.355 | 0 | 0 |

- Exit reasons: {'take_profit': 357, 'stop_loss': 942, 'no_volume_15m': 142}
- Sells priced by the verified curve formula because Jupiter had no route: 585
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +5.030
- Circuit breakers fired: 71
- Stream gaps logged: 81188

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
