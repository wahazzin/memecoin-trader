# Paper bot check-in (2026-10-20 15:33 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 330 / 47 / 6 | 330 | 25% | +0.2751 | -0.2205 | **-0.0944** | -31.1359 | 14.252 (top-ups 25.51) | -155.3% | 0 | 0 |
| `m1_random` | 273 / 32 / 31 | 273 | 21% | +0.2597 | -0.2129 | **-0.1142** | -31.1824 | 14.160 (top-ups 25.42) | -155.9% | 0 | 0 |

- Exit reasons: {'take_profit': 148, 'stop_loss': 403, 'no_volume_15m': 52}
- Sells priced by the verified curve formula because Jupiter had no route: 201
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.242, m1_random +2.486
- Circuit breakers fired: 28
- Stream gaps logged: 21192

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
