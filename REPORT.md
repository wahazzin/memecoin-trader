# Paper bot check-in (2026-10-11 05:24 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 122 / 16 / 1 | 122 | 22% | +0.3167 | -0.2139 | **-0.0965** | -11.7687 | 8.186 | -59.8% | 0 | 0 |
| `m1_random` | 80 / 11 / 12 | 80 | 16% | +0.2185 | -0.2139 | **-0.1437** | -11.4942 | 8.482 | -57.9% | 0 | 0 |

- Exit reasons: {'take_profit': 44, 'stop_loss': 127, 'no_volume_15m': 31}
- Sells priced by the verified curve formula because Jupiter had no route: 92
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.364, m1_random +0.744
- Circuit breakers fired: 10
- Stream gaps logged: 2604

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
