# Paper bot check-in (2026-10-23 00:09 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 362 / 53 / 7 | 362 | 25% | +0.2671 | -0.2206 | **-0.1007** | -36.4422 | 8.933 (top-ups 25.51) | -181.4% | 0 | 0 |
| `m1_random` | 316 / 37 / 35 | 316 | 22% | +0.2494 | -0.2131 | **-0.1121** | -35.4301 | 10.106 (top-ups 25.42) | -176.0% | 0 | 0 |

- Exit reasons: {'take_profit': 170, 'stop_loss': 451, 'no_volume_15m': 57}
- Sells priced by the verified curve formula because Jupiter had no route: 222
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.342, m1_random +2.928
- Circuit breakers fired: 32
- Stream gaps logged: 30536

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
