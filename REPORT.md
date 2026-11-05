# Paper bot check-in (2026-11-05 11:51 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 584 / 92 / 16 | 584 | 22% | +0.2672 | -0.2187 | **-0.1097** | -64.0666 | 9.957 (top-ups 54.23) | -64.638 | 0 | 0 |
| `m1_random` | 627 / 69 / 77 | 627 | 24% | +0.2555 | -0.2108 | **-0.0993** | -62.2339 | 11.714 (top-ups 53.97) | -62.959 | 0 | 0 |

- Exit reasons: {'take_profit': 299, 'stop_loss': 795, 'no_volume_15m': 117}
- Sells priced by the verified curve formula because Jupiter had no route: 461
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.524
- Circuit breakers fired: 59
- Stream gaps logged: 71710

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
