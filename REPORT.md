# Paper bot check-in (2026-11-23 02:35 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 947 / 167 / 21 | 947 | 23% | +0.2736 | -0.2153 | **-0.1048** | -99.2925 | 17.873 (top-ups 97.55) | -100.040 | 0 | 0 |
| `m1_random` | 982 / 109 / 114 | 982 | 24% | +0.2545 | -0.2134 | **-0.0990** | -97.2499 | 18.775 (top-ups 96.30) | -97.677 | 0 | 0 |

- Exit reasons: {'take_profit': 472, 'stop_loss': 1262, 'no_volume_15m': 194, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 820
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.772, m1_random +6.598
- Circuit breakers fired: 94
- Stream gaps logged: 102060

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
