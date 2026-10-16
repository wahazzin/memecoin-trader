# Paper bot check-in (2026-10-16 00:53 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 221 / 29 / 1 | 220 | 25% | +0.2908 | -0.2094 | **-0.0843** | -18.5526 | 15.186 (top-ups 13.81) | -101.4% | 1 | 0 |
| `m1_random` | 173 / 23 / 23 | 173 | 21% | +0.2374 | -0.2083 | **-0.1130** | -19.5433 | 14.506 (top-ups 14.10) | -101.5% | 0 | 0 |

- Exit reasons: {'take_profit': 95, 'stop_loss': 257, 'no_volume_15m': 41}
- Sells priced by the verified curve formula because Jupiter had no route: 136
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.812, m1_random +1.549
- Circuit breakers fired: 18
- Stream gaps logged: 9000

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
