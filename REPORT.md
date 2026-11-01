# Paper bot check-in (2026-11-01 00:23 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 498 / 74 / 14 | 498 | 24% | +0.2630 | -0.2202 | **-0.1057** | -52.6535 | 7.070 (top-ups 39.90) | -53.558 | 0 | 0 |
| `m1_random` | 459 / 50 / 45 | 459 | 22% | +0.2454 | -0.2182 | **-0.1152** | -52.8637 | 6.644 (top-ups 39.64) | -53.152 | 0 | 0 |

- Exit reasons: {'take_profit': 232, 'stop_loss': 638, 'no_volume_15m': 87}
- Sells priced by the verified curve formula because Jupiter had no route: 337
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.945, m1_random +3.457
- Circuit breakers fired: 50
- Stream gaps logged: 59742

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
