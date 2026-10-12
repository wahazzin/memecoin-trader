# Paper bot check-in (2026-10-12 00:11 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 125 / 17 / 1 | 124 | 22% | +0.3167 | -0.2149 | **-0.0992** | -12.2975 | 7.761 | -62.4% | 1 | 0 |
| `m1_random` | 83 / 11 / 13 | 82 | 17% | +0.2173 | -0.2151 | **-0.1413** | -11.5836 | 8.524 | -57.9% | 1 | 0 |

- Exit reasons: {'take_profit': 45, 'stop_loss': 130, 'no_volume_15m': 31}
- Sells priced by the verified curve formula because Jupiter had no route: 92
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.375, m1_random +0.781
- Circuit breakers fired: 10
- Stream gaps logged: 3645

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
