# Paper bot check-in (2026-11-21 09:00 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 913 / 162 / 21 | 913 | 23% | +0.2763 | -0.2162 | **-0.1051** | -95.9499 | 6.914 (top-ups 83.24) | -96.685 | 0 | 0 |
| `m1_random` | 947 / 108 / 114 | 947 | 24% | +0.2528 | -0.2146 | **-0.1001** | -94.8279 | 7.016 (top-ups 82.11) | -95.254 | 0 | 0 |

- Exit reasons: {'take_profit': 455, 'stop_loss': 1218, 'no_volume_15m': 186, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 791
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.685, m1_random +6.464
- Circuit breakers fired: 92
- Stream gaps logged: 100399

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
