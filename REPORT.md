# Paper bot check-in (2026-10-08 00:08 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 58 / 9 / 0 | 57 | 23% | +0.4138 | -0.1963 | **-0.0571** | -3.2561 | 16.873 | -17.1% | 1 | 0 |
| `m1_random` | 24 / 2 / 4 | 24 | 17% | +0.2307 | -0.2135 | **-0.1395** | -3.3479 | 16.646 | -17.4% | 0 | 0 |

- Exit reasons: {'take_profit': 20, 'stop_loss': 44, 'no_volume_15m': 17}
- Sells priced by the verified curve formula because Jupiter had no route: 39
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.226, m1_random +0.271
- Circuit breakers fired: 2
- Stream gaps logged: 31

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
