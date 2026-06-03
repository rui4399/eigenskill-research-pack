# Sensitivity-Rate-Distortion Allocation Report

Seed: `20260604`
Layers: `24`
Groups per layer: `16`
Budget average bits: `3.2`

## Results

| method | avg_bits | budget_used | distortion | bit_hist |
|---|---:|---:|---:|---|
| uniform_int2 | 2.000 | 0.625 | 136.48796311 (16.000x uniform4) | {'2': 384, '3': 0, '4': 0, '8': 0} |
| uniform_int3 | 3.000 | 0.938 | 34.12199078 (4.000x uniform4) | {'2': 0, '3': 384, '4': 0, '8': 0} |
| uniform_int4 | 4.000 | 1.250 | 8.53049769 (1.000x uniform4) | {'2': 0, '3': 0, '4': 384, '8': 0} |
| random_budgeted | 3.200 | 1.000 | 80.88251482 (9.482x uniform4) | {'2': 224, '3': 54, '4': 58, '8': 48} |
| greedy_margin | 3.199 | 1.000 | 18.52517920 (2.172x uniform4) | {'2': 54, '3': 194, '4': 136, '8': 0} |
| rate_distortion | 3.199 | 1.000 | 18.52517920 (2.172x uniform4) | {'2': 54, '3': 194, '4': 136, '8': 0} |

## Interpretation

This scaffold validates the allocation objective, not real model quality.
The next step is to replace synthetic statistics with calibration-derived
activation, Hessian/Fisher, outlier, and hardware-cost statistics.
