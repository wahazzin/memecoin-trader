# Paper bot check-in (2026-10-31 05:49 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 494 / 72 / 14 | 494 | 23% | +0.2634 | -0.2209 | **-0.1072** | -52.9451 | 6.782 (top-ups 39.90) | -53.480 | 0 | 0 |
| `m1_random` | 458 / 49 / 44 | 458 | 22% | +0.2454 | -0.2179 | **-0.1147** | -52.5541 | 6.956 (top-ups 39.64) | -52.843 | 0 | 0 |

- Exit reasons: {'take_profit': 230, 'stop_loss': 635, 'no_volume_15m': 87}
- Sells priced by the verified curve formula because Jupiter had no route: 333
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.945, m1_random +3.457
- Circuit breakers fired: 50
- Stream gaps logged: 59226

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
