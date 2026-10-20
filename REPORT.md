# Paper bot check-in (2026-10-20 01:34 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 329 / 47 / 6 | 328 | 26% | +0.2751 | -0.2204 | **-0.0935** | -30.6804 | 15.108 (top-ups 25.51) | -152.6% | 1 | 0 |
| `m1_random` | 255 / 31 / 29 | 255 | 21% | +0.2609 | -0.2126 | **-0.1123** | -28.6398 | 16.707 (top-ups 25.42) | -146.5% | 0 | 0 |

- Exit reasons: {'take_profit': 144, 'stop_loss': 388, 'no_volume_15m': 51}
- Sells priced by the verified curve formula because Jupiter had no route: 197
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.242, m1_random +2.234
- Circuit breakers fired: 26
- Stream gaps logged: 20678

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
