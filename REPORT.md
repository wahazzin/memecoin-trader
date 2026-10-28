# Paper bot check-in (2026-10-28 00:25 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 427 / 63 / 9 | 426 | 23% | +0.2650 | -0.2238 | **-0.1090** | -46.4431 | 13.280 (top-ups 39.90) | -46.982 | 1 | 0 |
| `m1_random` | 389 / 44 / 38 | 388 | 22% | +0.2443 | -0.2181 | **-0.1180** | -45.7764 | 13.725 (top-ups 39.64) | -46.072 | 1 | 0 |

- Exit reasons: {'take_profit': 198, 'stop_loss': 546, 'no_volume_15m': 70}
- Sells priced by the verified curve formula because Jupiter had no route: 278
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.537, m1_random +3.294
- Circuit breakers fired: 42
- Stream gaps logged: 50135

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
