# Paper bot check-in (2026-10-26 01:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 403 / 59 / 9 | 403 | 24% | +0.2657 | -0.2220 | **-0.1034** | -41.6584 | 18.449 (top-ups 39.90) | -205.3% | 0 | 0 |
| `m1_random` | 339 / 39 / 38 | 339 | 22% | +0.2435 | -0.2168 | **-0.1176** | -39.8811 | 19.666 (top-ups 39.64) | -199.6% | 0 | 0 |

- Exit reasons: {'take_profit': 184, 'stop_loss': 496, 'no_volume_15m': 62}
- Sells priced by the verified curve formula because Jupiter had no route: 248
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.160
- Circuit breakers fired: 38
- Stream gaps logged: 42515

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
