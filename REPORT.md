# Paper bot check-in (2026-10-29 00:15 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 446 / 64 / 11 | 445 | 23% | +0.2704 | -0.2241 | **-0.1085** | -48.2985 | 11.385 (top-ups 39.90) | -48.877 | 1 | 0 |
| `m1_random` | 411 / 44 / 39 | 411 | 22% | +0.2463 | -0.2181 | **-0.1153** | -47.3841 | 12.138 (top-ups 39.64) | -47.983 | 0 | 0 |

- Exit reasons: {'take_profit': 206, 'stop_loss': 576, 'no_volume_15m': 74}
- Sells priced by the verified curve formula because Jupiter had no route: 292
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.700, m1_random +3.357
- Circuit breakers fired: 44
- Stream gaps logged: 52796

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
