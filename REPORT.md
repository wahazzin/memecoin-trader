# Paper bot check-in (2026-10-20 00:53 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 319 / 47 / 6 | 318 | 25% | +0.2787 | -0.2206 | **-0.0934** | -29.7023 | 15.686 (top-ups 25.51) | -149.7% | 1 | 0 |
| `m1_random` | 252 / 30 / 29 | 252 | 20% | +0.2634 | -0.2126 | **-0.1162** | -29.2943 | 16.054 (top-ups 25.42) | -146.5% | 0 | 0 |

- Exit reasons: {'take_profit': 138, 'stop_loss': 381, 'no_volume_15m': 51}
- Sells priced by the verified curve formula because Jupiter had no route: 193
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.206, m1_random +2.150
- Circuit breakers fired: 26
- Stream gaps logged: 20678

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
