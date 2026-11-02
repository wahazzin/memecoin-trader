# Paper bot check-in (2026-11-02 03:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 531 / 81 / 14 | 531 | 23% | +0.2717 | -0.2171 | **-0.1039** | -55.1476 | 18.894 (top-ups 54.23) | -55.922 | 0 | 0 |
| `m1_random` | 503 / 53 / 56 | 503 | 23% | +0.2622 | -0.2177 | **-0.1080** | -54.3095 | 19.522 (top-ups 53.97) | -54.606 | 0 | 0 |

- Exit reasons: {'take_profit': 255, 'stop_loss': 685, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 374
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.046, m1_random +3.902
- Circuit breakers fired: 52
- Stream gaps logged: 61710

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
