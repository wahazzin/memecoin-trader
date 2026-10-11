# Paper bot check-in (2026-10-11 02:53 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 122 / 16 / 1 | 122 | 22% | +0.3167 | -0.2139 | **-0.0965** | -11.7687 | 8.186 | -59.8% | 0 | 0 |
| `m1_random` | 78 / 11 / 12 | 78 | 17% | +0.2185 | -0.2153 | **-0.1430** | -11.1518 | 8.824 | -56.2% | 0 | 0 |

- Exit reasons: {'take_profit': 44, 'stop_loss': 125, 'no_volume_15m': 31}
- Sells priced by the verified curve formula because Jupiter had no route: 92
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.364, m1_random +0.690
- Circuit breakers fired: 9
- Stream gaps logged: 2588

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
