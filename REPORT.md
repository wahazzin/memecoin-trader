# Paper bot check-in (2026-11-01 12:14 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 505 / 74 / 14 | 505 | 23% | +0.2630 | -0.2199 | **-0.1070** | -54.0564 | 5.667 (top-ups 39.90) | -54.596 | 0 | 0 |
| `m1_random` | 493 / 53 / 52 | 493 | 23% | +0.2647 | -0.2180 | **-0.1073** | -52.9151 | 6.587 (top-ups 39.64) | -53.210 | 0 | 0 |

- Exit reasons: {'take_profit': 246, 'stop_loss': 661, 'no_volume_15m': 91}
- Sells priced by the verified curve formula because Jupiter had no route: 355
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.981, m1_random +3.833
- Circuit breakers fired: 51
- Stream gaps logged: 59954

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
