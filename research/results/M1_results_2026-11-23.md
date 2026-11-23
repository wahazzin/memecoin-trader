# M1 results 

21590 coins reached the checkpoint; days: 47

| Split | PASS coins | dead-rate PASS | dead-rate FAIL | p (PASS<FAIL) | expectancy PASS | expectancy ALL | t (hours) | verdict parts |
|---|---|---|---|---|---|---|---|---|
| DESIGN | 4306 | 62.6% | 59.0% | 1.0000 | -18.01% | -13.56% | -6.06 (425h) | dead ✗ · expectancy ✗ · n ✓ |
| HOLDOUT | 1266 | 66.7% | 60.2% | 1.0000 | -21.05% | -15.41% | -5.67 (241h) | dead ✗ · expectancy ✗ · n ✓ |

Each check alone (whole sample, dead-rate pass vs fail):

- C1: pass 62.4% vs fail 59.4% (n pass 7091, p 1.0000)
- C2: pass 59.6% vs fail 64.6% (n pass 18331, p 0.0000)
- C3: pass 60.5% vs fail 58.1% (n pass 20174, p 0.9636)
- C4: pass 62.9% vs fail 52.2% (n pass 16408, p 1.0000)
- C5: pass 60.4% vs fail 59.7% (n pass 21528, p 0.5448)

**Verdict: NO EVIDENCE** (pre-registered: both splits must pass).

Data quality (amendment B-data): {'curve_outages': 1060, 'swap_outages': 583, 'curve_outage_s': 194940, 'coins': 270932, 'excluded_swap_outage': 16902, 'excluded_curve_outage': 278497}

