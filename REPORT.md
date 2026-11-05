# Paper bot check-in (2026-11-05 00:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 581 / 92 / 16 | 581 | 23% | +0.2672 | -0.2193 | **-0.1096** | -63.6702 | 10.383 (top-ups 54.23) | -64.212 | 0 | 0 |
| `m1_random` | 593 / 68 / 72 | 593 | 23% | +0.2557 | -0.2138 | **-0.1053** | -62.4486 | 11.168 (top-ups 53.97) | -62.959 | 0 | 0 |

- Exit reasons: {'take_profit': 288, 'stop_loss': 774, 'no_volume_15m': 112}
- Sells priced by the verified curve formula because Jupiter had no route: 443
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.443
- Circuit breakers fired: 58
- Stream gaps logged: 71410

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
