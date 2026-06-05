# Calibration Split Instability Report

Left: `outputs/olmo2_0425_1b_module_loss_sensitivity_limit2_group128.json` (`WikiText2`)
Right: `outputs/olmo2_0425_1b_module_loss_sensitivity_c4_limit2_group128.json` (`C4`)

CSI is the mean of positive-set instability, sign instability, score-rank instability, and top-k instability. Higher means the calibration split is less reliable for bit allocation.

## Summary

| metric | value |
|---|---:|
| shared modules | 113 |
| left positive modules | 67 |
| right positive modules | 52 |
| both positive modules | 37 |
| either positive modules | 82 |
| positive-set Jaccard | 0.4512 |
| signed-delta sign agreement | 0.6018 |
| positive-delta Pearson | 0.4219 |
| positive-delta Spearman | 0.1902 |
| score/cost Pearson | 0.1063 |
| score/cost Spearman | 0.1845 |
| score/cost Kendall tau-a | 0.1792 |

## Calibration Split Instability

| metric | value |
|---|---:|
| positive-set instability | 0.5488 |
| signed-delta sign instability | 0.3982 |
| score-rank instability | 0.4078 |
| mean top-k Jaccard | 0.1640 |
| top-k instability | 0.8360 |
| CSI | 0.5477 |

## Top-K Score Overlap

| k | left top-k | right top-k | overlap | union | Jaccard | instability |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 10 | 2 | 18 | 0.1111 | 0.8889 |
| 20 | 20 | 20 | 4 | 36 | 0.1111 | 0.8889 |
| 40 | 40 | 40 | 17 | 63 | 0.2698 | 0.7302 |

This C++ audit treats calibration split instability as the primary diagnostic target, not as a side note. Random baselines remain sanity checks; the paper claim should be about robustness under calibration-source shift.
