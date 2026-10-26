# Paper bot check-in (2026-10-26 02:24 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 407 / 59 / 9 | 407 | 24% | +0.2657 | -0.2234 | **-0.1056** | -42.9875 | 16.765 (top-ups 39.90) | -213.6% | 0 | 0 |
| `m1_random` | 345 / 39 / 38 | 344 | 21% | +0.2435 | -0.2173 | **-0.1195** | -41.1205 | 18.427 (top-ups 39.64) | -205.2% | 1 | 0 |

- Exit reasons: {'take_profit': 185, 'stop_loss': 503, 'no_volume_15m': 63}
- Sells priced by the verified curve formula because Jupiter had no route: 254
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.166
- Circuit breakers fired: 39
- Stream gaps logged: 42751

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
