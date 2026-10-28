# Paper bot check-in (2026-10-28 00:41 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 430 / 63 / 9 | 430 | 24% | +0.2634 | -0.2232 | **-0.1078** | -46.3334 | 13.413 (top-ups 39.90) | -46.982 | 0 | 0 |
| `m1_random` | 389 / 44 / 38 | 389 | 22% | +0.2443 | -0.2174 | **-0.1177** | -45.7978 | 13.727 (top-ups 39.64) | -46.072 | 0 | 0 |

- Exit reasons: {'take_profit': 199, 'stop_loss': 548, 'no_volume_15m': 72}
- Sells priced by the verified curve formula because Jupiter had no route: 281
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.583, m1_random +3.294
- Circuit breakers fired: 42
- Stream gaps logged: 50136

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
