# Paper bot check-in (2026-10-08 00:13 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 60 / 9 / 0 | 59 | 24% | +0.4143 | -0.1924 | **-0.0484** | -2.8573 | 17.271 | -17.1% | 1 | 0 |
| `m1_random` | 24 / 3 / 4 | 24 | 17% | +0.2307 | -0.2135 | **-0.1395** | -3.3479 | 16.645 | -17.4% | 0 | 0 |

- Exit reasons: {'take_profit': 22, 'stop_loss': 44, 'no_volume_15m': 17}
- Sells priced by the verified curve formula because Jupiter had no route: 40
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.327, m1_random +0.271
- Circuit breakers fired: 2
- Stream gaps logged: 32

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
