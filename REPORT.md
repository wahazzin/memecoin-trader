# Paper bot check-in (2026-11-19 00:35 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 827 / 144 / 21 | 824 | 22% | +0.2622 | -0.2186 | **-0.1107** | -91.1805 | 11.705 (top-ups 83.24) | -91.894 | 3 | 0 |
| `m1_random` | 920 / 105 / 113 | 920 | 25% | +0.2555 | -0.2140 | **-0.0982** | -90.3291 | 11.522 (top-ups 82.11) | -90.747 | 0 | 0 |

- Exit reasons: {'take_profit': 433, 'stop_loss': 1142, 'no_volume_15m': 169}
- Sells priced by the verified curve formula because Jupiter had no route: 718
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.470, m1_random +6.383
- Circuit breakers fired: 86
- Stream gaps logged: 95066

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
