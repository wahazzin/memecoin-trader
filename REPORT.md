# Paper bot check-in (2026-10-11 00:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 121 / 16 / 1 | 120 | 22% | +0.3167 | -0.2159 | **-0.0961** | -11.5313 | 8.394 | -58.8% | 1 | 0 |
| `m1_random` | 65 / 10 / 12 | 65 | 12% | +0.2107 | -0.2147 | **-0.1623** | -10.5511 | 9.576 | -52.5% | 0 | 0 |

- Exit reasons: {'take_profit': 40, 'stop_loss': 118, 'no_volume_15m': 27}
- Sells priced by the verified curve formula because Jupiter had no route: 86
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.364, m1_random +0.626
- Circuit breakers fired: 8
- Stream gaps logged: 2588

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
