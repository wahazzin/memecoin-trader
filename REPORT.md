# Paper bot check-in (2026-10-26 00:32 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 394 / 57 / 9 | 394 | 24% | +0.2617 | -0.2210 | **-0.1034** | -40.7517 | 19.350 (top-ups 39.90) | -200.9% | 0 | 0 |
| `m1_random` | 337 / 39 / 38 | 337 | 21% | +0.2450 | -0.2175 | **-0.1187** | -39.9869 | 19.560 (top-ups 39.64) | -199.6% | 0 | 0 |

- Exit reasons: {'take_profit': 181, 'stop_loss': 489, 'no_volume_15m': 61}
- Sells priced by the verified curve formula because Jupiter had no route: 242
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.432, m1_random +3.137
- Circuit breakers fired: 38
- Stream gaps logged: 42413

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
