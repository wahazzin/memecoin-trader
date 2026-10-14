# Paper bot check-in (2026-10-14 01:24 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 159 / 22 / 1 | 159 | 23% | +0.2861 | -0.2119 | **-0.0960** | -15.2626 | 18.492 (top-ups 13.81) | -77.0% | 0 | 0 |
| `m1_random` | 115 / 14 / 17 | 115 | 20% | +0.2233 | -0.2059 | **-0.1201** | -13.8067 | 20.262 (top-ups 14.10) | -70.7% | 0 | 0 |

- Exit reasons: {'take_profit': 62, 'stop_loss': 175, 'no_volume_15m': 37}
- Sells priced by the verified curve formula because Jupiter had no route: 109
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.477, m1_random +0.946
- Circuit breakers fired: 14
- Stream gaps logged: 6276

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
