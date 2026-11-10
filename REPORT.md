# Paper bot check-in (2026-11-10 02:32 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 673 / 110 / 19 | 673 | 23% | +0.2613 | -0.2189 | **-0.1104** | -74.3221 | 13.971 (top-ups 68.54) | -74.941 | 0 | 0 |
| `m1_random` | 715 / 84 / 101 | 715 | 24% | +0.2513 | -0.2108 | **-0.1003** | -71.6900 | 16.130 (top-ups 68.02) | -72.050 | 0 | 0 |

- Exit reasons: {'take_profit': 341, 'stop_loss': 908, 'no_volume_15m': 139}
- Sells priced by the verified curve formula because Jupiter had no route: 555
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.191, m1_random +4.911
- Circuit breakers fired: 69
- Stream gaps logged: 79260

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
