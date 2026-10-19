# Paper bot check-in (2026-10-19 00:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 295 / 43 / 5 | 294 | 25% | +0.2883 | -0.2179 | **-0.0922** | -27.1131 | 18.727 (top-ups 25.51) | -133.3% | 1 | 0 |
| `m1_random` | 222 / 28 / 26 | 221 | 21% | +0.2409 | -0.2117 | **-0.1175** | -25.9740 | 19.352 (top-ups 25.42) | -130.1% | 1 | 0 |

- Exit reasons: {'take_profit': 128, 'stop_loss': 339, 'no_volume_15m': 48}
- Sells priced by the verified curve formula because Jupiter had no route: 173
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.142, m1_random +2.051
- Circuit breakers fired: 24
- Stream gaps logged: 18194

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
