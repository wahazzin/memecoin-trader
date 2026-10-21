# Paper bot check-in (2026-10-21 00:36 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 334 / 52 / 6 | 334 | 25% | +0.2757 | -0.2200 | **-0.0939** | -31.3532 | 14.031 (top-ups 25.51) | -157.2% | 0 | 0 |
| `m1_random` | 276 / 32 / 31 | 276 | 21% | +0.2608 | -0.2130 | **-0.1134** | -31.3039 | 14.039 (top-ups 25.42) | -156.5% | 0 | 0 |

- Exit reasons: {'take_profit': 151, 'stop_loss': 407, 'no_volume_15m': 52}
- Sells priced by the verified curve formula because Jupiter had no route: 202
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.242, m1_random +2.526
- Circuit breakers fired: 28
- Stream gaps logged: 22924

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
