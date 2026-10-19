# Paper bot check-in (2026-10-19 01:01 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 299 / 44 / 5 | 298 | 25% | +0.2891 | -0.2205 | **-0.0940** | -28.0002 | 17.338 (top-ups 25.51) | -140.1% | 1 | 0 |
| `m1_random` | 223 / 28 / 27 | 221 | 21% | +0.2409 | -0.2117 | **-0.1175** | -25.9740 | 19.404 (top-ups 25.42) | -130.1% | 2 | 0 |

- Exit reasons: {'take_profit': 128, 'stop_loss': 342, 'no_volume_15m': 49}
- Sells priced by the verified curve formula because Jupiter had no route: 176
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.142, m1_random +2.051
- Circuit breakers fired: 24
- Stream gaps logged: 18210

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
