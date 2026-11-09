# Paper bot check-in (2026-11-09 10:49 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 652 / 104 / 17 | 652 | 23% | +0.2586 | -0.2186 | **-0.1096** | -71.4326 | 16.872 (top-ups 68.54) | -72.034 | 0 | 0 |
| `m1_random` | 706 / 83 / 98 | 705 | 24% | +0.2515 | -0.2102 | **-0.1002** | -70.6142 | 17.214 (top-ups 68.02) | -70.966 | 1 | 0 |

- Exit reasons: {'take_profit': 332, 'stop_loss': 890, 'no_volume_15m': 135}
- Sells priced by the verified curve formula because Jupiter had no route: 536
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.858
- Circuit breakers fired: 67
- Stream gaps logged: 77500

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
