# Paper bot check-in (2026-10-15 01:00 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 199 / 27 / 1 | 198 | 23% | +0.2810 | -0.2080 | **-0.0944** | -18.6901 | 15.263 (top-ups 13.81) | -92.9% | 1 | 0 |
| `m1_random` | 152 / 20 / 21 | 152 | 20% | +0.2462 | -0.2045 | **-0.1126** | -17.1105 | 16.946 (top-ups 14.10) | -87.1% | 0 | 0 |

- Exit reasons: {'take_profit': 80, 'stop_loss': 231, 'no_volume_15m': 39}
- Sells priced by the verified curve formula because Jupiter had no route: 123
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.700, m1_random +1.404
- Circuit breakers fired: 16
- Stream gaps logged: 7553

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
