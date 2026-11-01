# Paper bot check-in (2026-11-01 00:13 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 496 / 73 / 14 | 496 | 24% | +0.2635 | -0.2205 | **-0.1064** | -52.7574 | 6.969 (top-ups 39.90) | -53.558 | 0 | 0 |
| `m1_random` | 458 / 50 / 45 | 458 | 22% | +0.2454 | -0.2179 | **-0.1147** | -52.5541 | 6.956 (top-ups 39.64) | -52.843 | 0 | 0 |

- Exit reasons: {'take_profit': 230, 'stop_loss': 637, 'no_volume_15m': 87}
- Sells priced by the verified curve formula because Jupiter had no route: 335
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.945, m1_random +3.457
- Circuit breakers fired: 50
- Stream gaps logged: 59741

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
