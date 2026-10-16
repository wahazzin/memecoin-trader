# Paper bot check-in (2026-10-16 03:21 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 241 / 31 / 2 | 241 | 24% | +0.2887 | -0.2136 | **-0.0906** | -21.8369 | 11.892 (top-ups 13.81) | -109.4% | 0 | 0 |
| `m1_random` | 192 / 24 / 24 | 191 | 22% | +0.2348 | -0.2104 | **-0.1125** | -21.4881 | 12.666 (top-ups 14.10) | -107.1% | 1 | 0 |

- Exit reasons: {'take_profit': 107, 'stop_loss': 283, 'no_volume_15m': 42}
- Sells priced by the verified curve formula because Jupiter had no route: 145
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.948, m1_random +1.697
- Circuit breakers fired: 19
- Stream gaps logged: 9478

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
