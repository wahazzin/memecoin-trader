# Paper bot check-in (2026-11-02 21:25 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 539 / 81 / 14 | 539 | 23% | +0.2717 | -0.2175 | **-0.1059** | -57.0597 | 16.980 (top-ups 54.23) | -57.614 | 0 | 0 |
| `m1_random` | 520 / 54 / 57 | 520 | 23% | +0.2601 | -0.2191 | **-0.1094** | -56.8888 | 16.936 (top-ups 53.97) | -57.191 | 0 | 0 |

- Exit reasons: {'take_profit': 260, 'stop_loss': 705, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 380
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.047, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65039

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
