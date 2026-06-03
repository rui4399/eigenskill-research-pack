# Sensitivity-Rate-Distortion Allocation Report

Seed: `20260605`
Layers: `24`
Groups per layer: `16`
Budget average bits: `2.6`

## Results

| method | avg_bits | budget_used | distortion | bit_hist |
|---|---:|---:|---:|---|
| uniform_int2 | 2.000 | 0.769 | 145.73343621 (16.000x uniform4) | {'2': 384, '3': 0, '4': 0, '8': 0} |
| uniform_int3 | 3.000 | 1.154 | 36.43335905 (4.000x uniform4) | {'2': 0, '3': 384, '4': 0, '8': 0} |
| uniform_int4 | 4.000 | 1.538 | 9.10833976 (1.000x uniform4) | {'2': 0, '3': 0, '4': 384, '8': 0} |
| random_budgeted | 2.600 | 1.000 | 117.97953536 (12.953x uniform4) | {'2': 310, '3': 25, '4': 23, '8': 26} |
| greedy_margin | 2.598 | 0.999 | 44.66981840 (4.904x uniform4) | {'2': 186, '3': 164, '4': 34, '8': 0} |
| rate_distortion | 2.598 | 0.999 | 44.66981840 (4.904x uniform4) | {'2': 186, '3': 164, '4': 34, '8': 0} |

## Interpretation

This scaffold validates the allocation objective, not real model quality.
The next step is to replace synthetic statistics with calibration-derived
activation, Hessian/Fisher, outlier, and hardware-cost statistics.
