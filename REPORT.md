# Paper bot check-in (2026-10-24 00:16 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 372 / 54 / 7 | 371 | 25% | +0.2615 | -0.2213 | **-0.1016** | -37.6969 | 7.748 (top-ups 25.51) | -187.2% | 1 | 0 |
| `m1_random` | 324 / 37 / 36 | 324 | 22% | +0.2482 | -0.2138 | **-0.1140** | -36.9223 | 8.407 (top-ups 25.42) | -184.4% | 0 | 0 |

- Exit reasons: {'take_profit': 173, 'stop_loss': 464, 'no_volume_15m': 58}
- Sells priced by the verified curve formula because Jupiter had no route: 227
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.343, m1_random +2.978
- Circuit breakers fired: 34
- Stream gaps logged: 33226

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
