# Paper bot check-in (2026-10-21 00:26 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 333 / 50 / 6 | 333 | 26% | +0.2757 | -0.2203 | **-0.0937** | -31.1981 | 14.187 (top-ups 25.51) | -157.2% | 0 | 0 |
| `m1_random` | 276 / 32 / 31 | 276 | 21% | +0.2608 | -0.2130 | **-0.1134** | -31.3039 | 14.325 (top-ups 25.42) | -155.9% | 0 | 0 |

- Exit reasons: {'take_profit': 150, 'stop_loss': 407, 'no_volume_15m': 52}
- Sells priced by the verified curve formula because Jupiter had no route: 202
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.242, m1_random +2.526
- Circuit breakers fired: 28
- Stream gaps logged: 22907

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
