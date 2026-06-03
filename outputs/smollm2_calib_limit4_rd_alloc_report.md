# Sensitivity-Rate-Distortion Allocation Report

Seed: `20260604`
Layers: `225`
Groups per layer: `None`
Budget average bits: `3.2`

## Results

| method | avg_bits | budget_used | distortion | bit_hist |
|---|---:|---:|---:|---|
| uniform_int2 | 2.000 | 0.625 | 678.06004110 (16.000x uniform4) | {'2': 225, '3': 0, '4': 0, '8': 0} |
| uniform_int3 | 3.000 | 0.938 | 169.51501027 (4.000x uniform4) | {'2': 0, '3': 225, '4': 0, '8': 0} |
| uniform_int4 | 4.000 | 1.250 | 42.37875257 (1.000x uniform4) | {'2': 0, '3': 0, '4': 225, '8': 0} |
| random_budgeted | 3.200 | 1.000 | 233.62059058 (5.513x uniform4) | {'2': 137, '3': 24, '4': 34, '8': 30} |
| greedy_margin | 3.199 | 1.000 | 0.68940810 (0.016x uniform4) | {'2': 67, '3': 35, '4': 113, '8': 10} |
| rate_distortion | 3.199 | 1.000 | 0.68940810 (0.016x uniform4) | {'2': 67, '3': 35, '4': 113, '8': 10} |

## Interpretation

This scaffold validates the allocation objective, not real model quality.
The next step is to replace synthetic statistics with calibration-derived
activation, Hessian/Fisher, outlier, and hardware-cost statistics.
