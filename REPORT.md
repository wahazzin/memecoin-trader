# Paper bot check-in (2026-10-29 01:37 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 464 / 67 / 12 | 461 | 24% | +0.2670 | -0.2239 | **-0.1068** | -49.2221 | 10.637 (top-ups 39.90) | -49.862 | 3 | 0 |
| `m1_random` | 417 / 44 / 40 | 416 | 22% | +0.2464 | -0.2177 | **-0.1139** | -47.3850 | 12.115 (top-ups 39.64) | -47.983 | 1 | 0 |

- Exit reasons: {'take_profit': 212, 'stop_loss': 589, 'no_volume_15m': 76}
- Sells priced by the verified curve formula because Jupiter had no route: 305
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.773, m1_random +3.357
- Circuit breakers fired: 44
- Stream gaps logged: 52957

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
