# Paper bot check-in (2026-10-16 02:50 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 241 / 31 / 2 | 241 | 24% | +0.2887 | -0.2136 | **-0.0906** | -21.8369 | 11.892 (top-ups 13.81) | -109.4% | 0 | 0 |
| `m1_random` | 182 / 24 / 24 | 182 | 21% | +0.2383 | -0.2111 | **-0.1173** | -21.3474 | 12.697 (top-ups 14.10) | -106.9% | 0 | 0 |

- Exit reasons: {'take_profit': 103, 'stop_loss': 278, 'no_volume_15m': 42}
- Sells priced by the verified curve formula because Jupiter had no route: 142
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.948, m1_random +1.602
- Circuit breakers fired: 19
- Stream gaps logged: 9419

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
