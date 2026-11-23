# Paper bot check-in (2026-11-23 01:17 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 935 / 167 / 21 | 935 | 23% | +0.2746 | -0.2160 | **-0.1047** | -97.9346 | 19.235 (top-ups 97.55) | -98.677 | 0 | 0 |
| `m1_random` | 975 / 109 / 114 | 975 | 25% | +0.2545 | -0.2138 | **-0.0986** | -96.0907 | 19.934 (top-ups 96.30) | -96.938 | 0 | 0 |

- Exit reasons: {'take_profit': 469, 'stop_loss': 1248, 'no_volume_15m': 192, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 811
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.753, m1_random +6.558
- Circuit breakers fired: 94
- Stream gaps logged: 102013

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
