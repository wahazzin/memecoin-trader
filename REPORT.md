# Paper bot check-in (2026-10-19 00:51 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 297 / 43 / 5 | 296 | 25% | +0.2883 | -0.2194 | **-0.0942** | -27.8762 | 17.635 (top-ups 25.51) | -138.7% | 1 | 0 |
| `m1_random` | 222 / 28 / 26 | 221 | 21% | +0.2409 | -0.2117 | **-0.1175** | -25.9740 | 19.393 (top-ups 25.42) | -130.1% | 1 | 0 |

- Exit reasons: {'take_profit': 128, 'stop_loss': 341, 'no_volume_15m': 48}
- Sells priced by the verified curve formula because Jupiter had no route: 175
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.142, m1_random +2.051
- Circuit breakers fired: 24
- Stream gaps logged: 18200

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
