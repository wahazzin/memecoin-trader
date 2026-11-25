# Paper bot check-in (2026-11-25 00:29 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1064 / 184 / 21 | 1063 | 23% | +0.2816 | -0.2152 | **-0.0993** | -105.5063 | 11.591 (top-ups 97.55) | -106.321 | 1 | 0 |
| `m1_random` | 1030 / 113 / 116 | 1029 | 24% | +0.2530 | -0.2124 | **-0.1003** | -103.1733 | 13.081 (top-ups 96.30) | -103.371 | 1 | 0 |

- Exit reasons: {'take_profit': 507, 'stop_loss': 1370, 'no_volume_15m': 214, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 902
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.142, m1_random +6.719
- Circuit breakers fired: 99
- Stream gaps logged: 109012

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 82 / 12 / 0 | 81 | 27% | +0.3499 | -0.2192 | **-0.0646** | -5.2346 | 11.591 (top-ups 97.55) | -7.144 | 1 | 0 |
| `m1_random` | 32 / 3 / 1 | 31 | 13% | +0.2343 | -0.1858 | **-0.1316** | -4.0795 | 13.081 (top-ups 96.30) | -3.847 | 1 | 0 |

- Exit reasons: {'stop_loss': 80, 'take_profit': 19, 'no_volume_15m': 13}
- Sells priced by the verified curve formula because Jupiter had no route: 62
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.256, m1_random +0.092
- Circuit breakers fired: 3
- Stream gaps logged: 5048

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
