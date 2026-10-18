# Paper bot check-in (2026-10-18 00:53 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 281 / 41 / 4 | 281 | 26% | +0.2818 | -0.2186 | **-0.0904** | -25.4018 | 8.305 (top-ups 13.81) | -127.0% | 0 | 0 |
| `m1_random` | 217 / 28 / 26 | 217 | 21% | +0.2409 | -0.2123 | **-0.1162** | -25.2151 | 8.854 (top-ups 14.10) | -126.0% | 0 | 0 |

- Exit reasons: {'take_profit': 127, 'stop_loss': 324, 'no_volume_15m': 47}
- Sells priced by the verified curve formula because Jupiter had no route: 168
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.022, m1_random +2.051
- Circuit breakers fired: 23
- Stream gaps logged: 16730

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
