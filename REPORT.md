# Paper bot check-in (2026-10-20 03:01 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 330 / 47 / 6 | 330 | 25% | +0.2751 | -0.2205 | **-0.0944** | -31.1359 | 14.252 (top-ups 25.51) | -155.3% | 0 | 0 |
| `m1_random` | 259 / 32 / 30 | 259 | 22% | +0.2595 | -0.2127 | **-0.1106** | -28.6545 | 16.860 (top-ups 25.42) | -146.5% | 0 | 0 |

- Exit reasons: {'take_profit': 146, 'stop_loss': 392, 'no_volume_15m': 51}
- Sells priced by the verified curve formula because Jupiter had no route: 197
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.242, m1_random +2.280
- Circuit breakers fired: 27
- Stream gaps logged: 20741

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
