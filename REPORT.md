# Paper bot check-in (2026-11-25 00:02 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1047 / 184 / 21 | 1047 | 23% | +0.2835 | -0.2139 | **-0.0980** | -102.5545 | 14.288 (top-ups 97.55) | -103.626 | 0 | 0 |
| `m1_random` | 1022 / 113 / 116 | 1022 | 24% | +0.2530 | -0.2129 | **-0.0998** | -102.0366 | 14.356 (top-ups 96.30) | -102.096 | 0 | 0 |

- Exit reasons: {'take_profit': 503, 'stop_loss': 1351, 'no_volume_15m': 214, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 894
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.045, m1_random +6.672
- Circuit breakers fired: 98
- Stream gaps logged: 108879

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 65 / 12 / 0 | 65 | 28% | +0.3903 | -0.1980 | **-0.0351** | -2.2828 | 14.288 (top-ups 97.55) | -4.449 | 0 | 0 |
| `m1_random` | 24 / 3 / 1 | 24 | 17% | +0.2343 | -0.1940 | **-0.1226** | -2.9429 | 14.356 (top-ups 96.30) | -2.572 | 0 | 0 |

- Exit reasons: {'stop_loss': 61, 'take_profit': 15, 'no_volume_15m': 13}
- Sells priced by the verified curve formula because Jupiter had no route: 54
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.159, m1_random +0.046
- Circuit breakers fired: 2
- Stream gaps logged: 4915

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
