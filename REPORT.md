# Paper bot check-in (2026-10-13 00:09 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 130 / 20 / 1 | 130 | 22% | +0.3020 | -0.2158 | **-0.1003** | -13.0347 | 6.913 | -66.1% | 0 | 0 |
| `m1_random` | 105 / 13 / 15 | 105 | 19% | +0.2167 | -0.2114 | **-0.1298** | -13.6321 | 6.341 | -68.5% | 0 | 0 |

- Exit reasons: {'take_profit': 52, 'stop_loss': 151, 'no_volume_15m': 32}
- Sells priced by the verified curve formula because Jupiter had no route: 95
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.375, m1_random +0.857
- Circuit breakers fired: 12
- Stream gaps logged: 5005

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
