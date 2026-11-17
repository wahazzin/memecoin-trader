# Paper bot check-in (2026-11-17 03:06 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 804 / 136 / 21 | 804 | 23% | +0.2598 | -0.2184 | **-0.1102** | -88.5971 | 14.329 (top-ups 83.24) | -89.276 | 0 | 0 |
| `m1_random` | 889 / 100 / 113 | 889 | 25% | +0.2563 | -0.2132 | **-0.0981** | -87.1973 | 15.017 (top-ups 82.11) | -87.514 | 0 | 0 |

- Exit reasons: {'take_profit': 422, 'stop_loss': 1105, 'no_volume_15m': 166}
- Sells priced by the verified curve formula because Jupiter had no route: 693
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.444, m1_random +6.183
- Circuit breakers fired: 83
- Stream gaps logged: 92242

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
