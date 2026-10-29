# Paper bot check-in (2026-10-29 00:51 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 452 / 65 / 11 | 452 | 23% | +0.2700 | -0.2239 | **-0.1081** | -48.8397 | 10.899 (top-ups 39.90) | -49.363 | 0 | 0 |
| `m1_random` | 414 / 44 / 39 | 414 | 22% | +0.2468 | -0.2173 | **-0.1142** | -47.2792 | 12.242 (top-ups 39.64) | -47.983 | 0 | 0 |

- Exit reasons: {'take_profit': 209, 'stop_loss': 583, 'no_volume_15m': 74}
- Sells priced by the verified curve formula because Jupiter had no route: 296
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.773, m1_random +3.357
- Circuit breakers fired: 44
- Stream gaps logged: 52889

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
