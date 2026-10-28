# Paper bot check-in (2026-10-28 01:43 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 442 / 64 / 11 | 442 | 24% | +0.2704 | -0.2249 | **-0.1084** | -47.9068 | 11.833 (top-ups 39.90) | -48.428 | 0 | 0 |
| `m1_random` | 407 / 44 / 39 | 406 | 22% | +0.2500 | -0.2176 | **-0.1162** | -47.1844 | 13.120 (top-ups 39.64) | -46.677 | 1 | 0 |

- Exit reasons: {'take_profit': 205, 'stop_loss': 569, 'no_volume_15m': 74}
- Sells priced by the verified curve formula because Jupiter had no route: 291
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.700, m1_random +3.352
- Circuit breakers fired: 43
- Stream gaps logged: 50158

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
