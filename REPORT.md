# Paper bot check-in (2026-10-27 11:36 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 420 / 61 / 9 | 420 | 24% | +0.2657 | -0.2240 | **-0.1085** | -45.5884 | 14.161 (top-ups 39.90) | -46.101 | 0 | 0 |
| `m1_random` | 387 / 44 / 38 | 387 | 22% | +0.2443 | -0.2176 | **-0.1173** | -45.4014 | 14.123 (top-ups 39.64) | -45.674 | 0 | 0 |

- Exit reasons: {'take_profit': 197, 'stop_loss': 540, 'no_volume_15m': 70}
- Sells priced by the verified curve formula because Jupiter had no route: 273
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.294
- Circuit breakers fired: 42
- Stream gaps logged: 48091

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
