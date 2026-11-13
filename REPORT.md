# Paper bot check-in (2026-11-13 00:31 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 709 / 120 / 21 | 708 | 22% | +0.2569 | -0.2182 | **-0.1115** | -78.9576 | 9.294 (top-ups 68.54) | -79.612 | 1 | 0 |
| `m1_random` | 804 / 89 / 111 | 804 | 25% | +0.2596 | -0.2141 | **-0.0968** | -77.8654 | 9.937 (top-ups 68.02) | -78.243 | 0 | 0 |

- Exit reasons: {'take_profit': 377, 'stop_loss': 990, 'no_volume_15m': 145}
- Sells priced by the verified curve formula because Jupiter had no route: 608
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +5.597
- Circuit breakers fired: 74
- Stream gaps logged: 84620

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
