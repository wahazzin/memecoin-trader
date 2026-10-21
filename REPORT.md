# Paper bot check-in (2026-10-21 01:17 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 343 / 52 / 6 | 341 | 25% | +0.2744 | -0.2187 | **-0.0943** | -32.1722 | 13.167 (top-ups 25.51) | -161.2% | 2 | 0 |
| `m1_random` | 277 / 33 / 31 | 277 | 21% | +0.2608 | -0.2122 | **-0.1131** | -31.3333 | 14.008 (top-ups 25.42) | -156.6% | 0 | 0 |

- Exit reasons: {'take_profit': 154, 'stop_loss': 412, 'no_volume_15m': 52}
- Sells priced by the verified curve formula because Jupiter had no route: 206
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.248, m1_random +2.526
- Circuit breakers fired: 28
- Stream gaps logged: 22989

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
