# Paper bot check-in (2026-10-19 00:15 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 287 / 42 / 5 | 287 | 25% | +0.2883 | -0.2185 | **-0.0896** | -25.7095 | 20.288 (top-ups 25.51) | -128.6% | 0 | 0 |
| `m1_random` | 219 / 28 / 26 | 219 | 21% | +0.2409 | -0.2126 | **-0.1174** | -25.7035 | 20.104 (top-ups 25.42) | -126.9% | 0 | 0 |

- Exit reasons: {'take_profit': 128, 'stop_loss': 331, 'no_volume_15m': 47}
- Sells priced by the verified curve formula because Jupiter had no route: 170
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.065, m1_random +2.051
- Circuit breakers fired: 24
- Stream gaps logged: 18095

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
