# Paper bot check-in (2026-11-25 00:13 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1056 / 184 / 21 | 1055 | 23% | +0.2827 | -0.2142 | **-0.0983** | -103.7441 | 13.686 (top-ups 97.55) | -104.226 | 1 | 0 |
| `m1_random` | 1024 / 113 / 116 | 1024 | 24% | +0.2530 | -0.2126 | **-0.0998** | -102.2357 | 13.854 (top-ups 96.30) | -102.598 | 0 | 0 |

- Exit reasons: {'take_profit': 504, 'stop_loss': 1360, 'no_volume_15m': 214, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 897
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.111, m1_random +6.719
- Circuit breakers fired: 98
- Stream gaps logged: 108936

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 74 / 12 / 0 | 73 | 27% | +0.3703 | -0.2053 | **-0.0476** | -3.4724 | 13.686 (top-ups 97.55) | -5.049 | 1 | 0 |
| `m1_random` | 26 / 3 / 1 | 26 | 15% | +0.2343 | -0.1854 | **-0.1208** | -3.1419 | 13.854 (top-ups 96.30) | -3.074 | 0 | 0 |

- Exit reasons: {'stop_loss': 70, 'take_profit': 16, 'no_volume_15m': 13}
- Sells priced by the verified curve formula because Jupiter had no route: 57
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.226, m1_random +0.092
- Circuit breakers fired: 2
- Stream gaps logged: 4972

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
