# Sensitivity-Rate-Distortion Allocation Report

Seed: `20260604`
Layers: `225`
Groups per layer: `None`
Budget average bits: `2.8`

## Results

| method | avg_bits | budget_used | distortion | bit_hist |
|---|---:|---:|---:|---|
| uniform_int2 | 2.000 | 0.714 | 678.06004110 (16.000x uniform4) | {'2': 225, '3': 0, '4': 0, '8': 0} |
| uniform_int3 | 3.000 | 1.071 | 169.51501027 (4.000x uniform4) | {'2': 0, '3': 225, '4': 0, '8': 0} |
| uniform_int4 | 4.000 | 1.429 | 42.37875257 (1.000x uniform4) | {'2': 0, '3': 0, '4': 225, '8': 0} |
| random_budgeted | 2.800 | 1.000 | 234.06147887 (5.523x uniform4) | {'2': 173, '3': 17, '4': 16, '8': 19} |
| greedy_margin | 2.799 | 1.000 | 1.01598835 (0.024x uniform4) | {'2': 97, '3': 63, '4': 61, '8': 4} |
| rate_distortion | 2.799 | 1.000 | 1.01598835 (0.024x uniform4) | {'2': 97, '3': 63, '4': 61, '8': 4} |

## Interpretation

This scaffold validates the allocation objective, not real model quality.
The next step is to replace synthetic statistics with calibration-derived
activation, Hessian/Fisher, outlier, and hardware-cost statistics.
