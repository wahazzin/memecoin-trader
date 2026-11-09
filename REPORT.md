# Paper bot check-in (2026-11-09 04:42 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 652 / 104 / 17 | 652 | 23% | +0.2586 | -0.2186 | **-0.1096** | -71.4326 | 17.132 (top-ups 68.54) | -71.774 | 0 | 0 |
| `m1_random` | 694 / 80 / 93 | 694 | 24% | +0.2517 | -0.2101 | **-0.0990** | -68.6934 | 19.138 (top-ups 68.02) | -69.042 | 0 | 0 |

- Exit reasons: {'take_profit': 328, 'stop_loss': 884, 'no_volume_15m': 134}
- Sells priced by the verified curve formula because Jupiter had no route: 533
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.831
- Circuit breakers fired: 66
- Stream gaps logged: 77474

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
