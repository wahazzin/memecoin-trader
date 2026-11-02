# Paper bot check-in (2026-11-02 01:04 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 515 / 76 / 14 | 515 | 23% | +0.2725 | -0.2192 | **-0.1047** | -53.9039 | 20.146 (top-ups 54.23) | -54.647 | 0 | 0 |
| `m1_random` | 500 / 53 / 53 | 500 | 23% | +0.2622 | -0.2181 | **-0.1076** | -53.8157 | 20.016 (top-ups 53.97) | -54.128 | 0 | 0 |

- Exit reasons: {'take_profit': 251, 'stop_loss': 672, 'no_volume_15m': 92}
- Sells priced by the verified curve formula because Jupiter had no route: 361
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.016, m1_random +3.898
- Circuit breakers fired: 52
- Stream gaps logged: 61659

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
