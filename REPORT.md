# Paper bot check-in (2026-11-09 03:55 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 646 / 103 / 17 | 646 | 23% | +0.2601 | -0.2181 | **-0.1086** | -70.1348 | 18.171 (top-ups 68.54) | -71.117 | 0 | 0 |
| `m1_random` | 692 / 80 / 92 | 692 | 24% | +0.2517 | -0.2102 | **-0.0987** | -68.3248 | 19.506 (top-ups 68.02) | -68.684 | 0 | 0 |

- Exit reasons: {'take_profit': 327, 'stop_loss': 877, 'no_volume_15m': 134}
- Sells priced by the verified curve formula because Jupiter had no route: 526
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.831
- Circuit breakers fired: 66
- Stream gaps logged: 77462

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
