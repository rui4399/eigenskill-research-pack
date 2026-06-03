# Rate-Distortion Allocation Sweep

Date: 2026-06-04

This is a synthetic scaffold for the next EigenSkill-Q experiment track. It does
not measure real model quality yet. Its purpose is to validate the allocation
API and reporting format before plugging in calibration-derived sensitivity,
activation, Hessian/Fisher, outlier, and hardware-cost statistics.

## Commands

```powershell
python train_python\rate_distortion_allocator.py `
  --budget-avg-bits 2.6 `
  --seed 20260605 `
  --out-json outputs\rate_distortion_allocation_budget26_summary.json `
  --out-md outputs\rate_distortion_allocation_budget26_report.md

python train_python\rate_distortion_allocator.py `
  --budget-avg-bits 3.2 `
  --seed 20260604 `
  --out-json outputs\rate_distortion_allocation_summary.json `
  --out-md outputs\rate_distortion_allocation_report.md

python train_python\rate_distortion_allocator.py `
  --budget-avg-bits 3.6 `
  --seed 20260606 `
  --out-json outputs\rate_distortion_allocation_budget36_summary.json `
  --out-md outputs\rate_distortion_allocation_budget36_report.md
```

## Budget Sweep

| budget avg bits | method | avg_bits | budget_used | distortion | bit histogram |
|---:|---|---:|---:|---:|---|
| 2.6 | random_budgeted | 2.600 | 1.000 | 117.97953536 | 2:310, 3:25, 4:23, 8:26 |
| 2.6 | rate_distortion | 2.598 | 0.999 | 44.66981840 | 2:186, 3:164, 4:34, 8:0 |
| 3.2 | random_budgeted | 3.200 | 1.000 | 80.88251482 | 2:224, 3:54, 4:58, 8:48 |
| 3.2 | rate_distortion | 3.199 | 1.000 | 18.52517920 | 2:54, 3:194, 4:136, 8:0 |
| 3.6 | random_budgeted | 3.599 | 1.000 | 61.11835124 | 2:156, 3:80, 4:89, 8:59 |
| 3.6 | rate_distortion | 3.598 | 1.000 | 10.87862929 | 2:19, 3:130, 4:231, 8:4 |

## Interpretation

The rate-distortion allocator consistently improves synthetic weighted
distortion over random budgeted allocation at the same average-bit budget. The
result is expected because the synthetic objective is exactly matched to the
allocator. The useful outcome is the executable interface:

```text
GroupStat(layer, group, sensitivity, variance, cost, outlier)
    -> allocation over {2, 3, 4, 8}
    -> memory/distortion/report
```

The next implementation step is to replace synthetic `GroupStat` values with
real calibration statistics from a small open model.
