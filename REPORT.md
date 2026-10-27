# Paper bot check-in (2026-10-27 01:13 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 420 / 61 / 9 | 420 | 24% | +0.2657 | -0.2240 | **-0.1085** | -45.5884 | 14.161 (top-ups 39.90) | -46.101 | 0 | 0 |
| `m1_random` | 364 / 42 / 38 | 364 | 22% | +0.2384 | -0.2175 | **-0.1186** | -43.1642 | 16.379 (top-ups 39.64) | -43.418 | 0 | 0 |

- Exit reasons: {'take_profit': 192, 'stop_loss': 527, 'no_volume_15m': 65}
- Sells priced by the verified curve formula because Jupiter had no route: 266
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.202
- Circuit breakers fired: 41
- Stream gaps logged: 47325

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
