# Paper bot check-in (2026-11-23 01:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 936 / 167 / 21 | 936 | 23% | +0.2746 | -0.2160 | **-0.1049** | -98.1427 | 19.027 (top-ups 97.55) | -98.885 | 0 | 0 |
| `m1_random` | 976 / 109 / 114 | 976 | 25% | +0.2545 | -0.2139 | **-0.0987** | -96.3460 | 19.934 (top-ups 96.30) | -96.938 | 0 | 0 |

- Exit reasons: {'take_profit': 469, 'stop_loss': 1250, 'no_volume_15m': 192, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 812
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.753, m1_random +6.579
- Circuit breakers fired: 94
- Stream gaps logged: 102013

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
