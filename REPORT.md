# Paper bot check-in (2026-10-29 00:09 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 444 / 64 / 11 | 444 | 23% | +0.2704 | -0.2247 | **-0.1087** | -48.2642 | 11.476 (top-ups 39.90) | -48.786 | 0 | 0 |
| `m1_random` | 411 / 44 / 39 | 411 | 22% | +0.2463 | -0.2181 | **-0.1153** | -47.3841 | 12.138 (top-ups 39.64) | -47.983 | 0 | 0 |

- Exit reasons: {'take_profit': 206, 'stop_loss': 575, 'no_volume_15m': 74}
- Sells priced by the verified curve formula because Jupiter had no route: 291
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.700, m1_random +3.357
- Circuit breakers fired: 44
- Stream gaps logged: 52782

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
