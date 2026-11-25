# Paper bot check-in (2026-11-25 00:18 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1057 / 184 / 21 | 1056 | 23% | +0.2819 | -0.2142 | **-0.0982** | -103.6622 | 13.472 (top-ups 97.55) | -104.440 | 1 | 0 |
| `m1_random` | 1028 / 113 / 116 | 1028 | 24% | +0.2530 | -0.2124 | **-0.1001** | -102.9091 | 13.779 (top-ups 96.30) | -102.674 | 0 | 0 |

- Exit reasons: {'take_profit': 506, 'stop_loss': 1363, 'no_volume_15m': 214, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 899
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.111, m1_random +6.719
- Circuit breakers fired: 98
- Stream gaps logged: 108963

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 75 / 12 / 0 | 74 | 28% | +0.3566 | -0.2053 | **-0.0458** | -3.3905 | 13.472 (top-ups 97.55) | -5.262 | 1 | 0 |
| `m1_random` | 30 / 3 / 1 | 30 | 13% | +0.2343 | -0.1828 | **-0.1272** | -3.8153 | 13.779 (top-ups 96.30) | -3.149 | 0 | 0 |

- Exit reasons: {'stop_loss': 73, 'take_profit': 18, 'no_volume_15m': 13}
- Sells priced by the verified curve formula because Jupiter had no route: 59
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.226, m1_random +0.092
- Circuit breakers fired: 2
- Stream gaps logged: 4999

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
