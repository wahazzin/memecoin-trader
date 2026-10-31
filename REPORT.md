# Paper bot check-in (2026-10-31 01:05 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 480 / 71 / 14 | 480 | 23% | +0.2647 | -0.2209 | **-0.1086** | -52.1399 | 7.590 (top-ups 39.90) | -52.674 | 0 | 0 |
| `m1_random` | 455 / 49 / 44 | 455 | 22% | +0.2454 | -0.2174 | **-0.1137** | -51.7175 | 7.792 (top-ups 39.64) | -52.005 | 0 | 0 |

- Exit reasons: {'take_profit': 223, 'stop_loss': 627, 'no_volume_15m': 85}
- Sells priced by the verified curve formula because Jupiter had no route: 327
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.857, m1_random +3.457
- Circuit breakers fired: 48
- Stream gaps logged: 58956

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
