# Paper bot check-in (2026-10-16 01:34 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 233 / 31 / 2 | 233 | 24% | +0.2907 | -0.2149 | **-0.0912** | -21.2528 | 12.806 (top-ups 13.81) | -104.9% | 0 | 0 |
| `m1_random` | 179 / 24 / 24 | 179 | 21% | +0.2383 | -0.2085 | **-0.1137** | -20.3461 | 13.700 (top-ups 14.10) | -102.0% | 0 | 0 |

- Exit reasons: {'take_profit': 99, 'stop_loss': 271, 'no_volume_15m': 42}
- Sells priced by the verified curve formula because Jupiter had no route: 140
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.852, m1_random +1.589
- Circuit breakers fired: 18
- Stream gaps logged: 9217

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
