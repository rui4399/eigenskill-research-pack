# Sensitivity-Rate-Distortion Allocation Report

Seed: `20260606`
Layers: `24`
Groups per layer: `16`
Budget average bits: `3.6`

## Results

| method | avg_bits | budget_used | distortion | bit_hist |
|---|---:|---:|---:|---|
| uniform_int2 | 2.000 | 0.556 | 130.35769168 (16.000x uniform4) | {'2': 384, '3': 0, '4': 0, '8': 0} |
| uniform_int3 | 3.000 | 0.833 | 32.58942292 (4.000x uniform4) | {'2': 0, '3': 384, '4': 0, '8': 0} |
| uniform_int4 | 4.000 | 1.111 | 8.14735573 (1.000x uniform4) | {'2': 0, '3': 0, '4': 384, '8': 0} |
| random_budgeted | 3.599 | 1.000 | 61.11835124 (7.502x uniform4) | {'2': 156, '3': 80, '4': 89, '8': 59} |
| greedy_margin | 3.598 | 1.000 | 10.87862929 (1.335x uniform4) | {'2': 19, '3': 130, '4': 231, '8': 4} |
| rate_distortion | 3.598 | 1.000 | 10.87862929 (1.335x uniform4) | {'2': 19, '3': 130, '4': 231, '8': 4} |

## Interpretation

This scaffold validates the allocation objective, not real model quality.
The next step is to replace synthetic statistics with calibration-derived
activation, Hessian/Fisher, outlier, and hardware-cost statistics.
