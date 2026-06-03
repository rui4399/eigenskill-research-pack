# Sensitivity-Rate-Distortion Allocation Report

Seed: `20260604`
Layers: `225`
Groups per layer: `None`
Budget average bits: `4.5`

## Results

| method | avg_bits | budget_used | distortion | bit_hist |
|---|---:|---:|---:|---|
| uniform_int2 | 2.000 | 0.444 | 678.06004110 (16.000x uniform4) | {'2': 225, '4': 0, '8': 0} |
| uniform_int3 | 3.000 | 0.667 | 169.51501027 (4.000x uniform4) | {'3': 225, '4': 0, '8': 0} |
| uniform_int4 | 4.000 | 0.889 | 42.37875257 (1.000x uniform4) | {'4': 225, '8': 0} |
| random_budgeted | 4.499 | 1.000 | 13.29794253 (0.314x uniform4) | {'4': 188, '8': 37} |
| greedy_margin | 4.499 | 1.000 | 0.49442778 (0.012x uniform4) | {'4': 172, '8': 53} |
| rate_distortion | 4.499 | 1.000 | 0.49442778 (0.012x uniform4) | {'4': 172, '8': 53} |

## Interpretation

This scaffold validates the allocation objective, not real model quality.
The next step is to replace synthetic statistics with calibration-derived
activation, Hessian/Fisher, outlier, and hardware-cost statistics.
