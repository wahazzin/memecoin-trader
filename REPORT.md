# Paper bot check-in (2026-11-10 00:27 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 657 / 106 / 17 | 657 | 23% | +0.2627 | -0.2182 | **-0.1077** | -70.7352 | 17.962 (top-ups 68.54) | -72.054 | 0 | 0 |
| `m1_random` | 709 / 83 / 99 | 708 | 24% | +0.2517 | -0.2103 | **-0.1000** | -70.8148 | 17.011 (top-ups 68.02) | -71.457 | 1 | 0 |

- Exit reasons: {'take_profit': 336, 'stop_loss': 893, 'no_volume_15m': 136}
- Sells priced by the verified curve formula because Jupiter had no route: 541
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.858
- Circuit breakers fired: 68
- Stream gaps logged: 79227

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
