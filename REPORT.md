# Paper bot check-in (2026-11-01 00:54 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 505 / 74 / 14 | 505 | 23% | +0.2630 | -0.2199 | **-0.1070** | -54.0564 | 5.667 (top-ups 39.90) | -54.596 | 0 | 0 |
| `m1_random` | 463 / 50 / 45 | 463 | 22% | +0.2558 | -0.2184 | **-0.1119** | -51.8158 | 7.692 (top-ups 39.64) | -53.152 | 0 | 0 |

- Exit reasons: {'take_profit': 236, 'stop_loss': 644, 'no_volume_15m': 88}
- Sells priced by the verified curve formula because Jupiter had no route: 344
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.981, m1_random +3.457
- Circuit breakers fired: 51
- Stream gaps logged: 59768

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
