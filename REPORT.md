# Paper bot check-in (2026-11-11 00:35 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 679 / 111 / 19 | 679 | 22% | +0.2613 | -0.2193 | **-0.1117** | -75.8363 | 12.689 (top-ups 68.54) | -76.217 | 0 | 0 |
| `m1_random` | 739 / 85 / 102 | 739 | 24% | +0.2502 | -0.2117 | **-0.0998** | -73.7647 | 14.051 (top-ups 68.02) | -74.129 | 0 | 0 |

- Exit reasons: {'take_profit': 351, 'stop_loss': 926, 'no_volume_15m': 141}
- Sells priced by the verified curve formula because Jupiter had no route: 571
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +4.994
- Circuit breakers fired: 70
- Stream gaps logged: 80827

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
