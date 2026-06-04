# Sensitivity Split Stability

Left: `outputs/qwen3_1p7b_module_loss_sensitivity_limit2_group128.json`
Right: `outputs/qwen3_1p7b_module_loss_sensitivity_c4_limit2_group128.json`

## Summary

| metric | value |
|---|---:|
| shared modules | 197 |
| left positive modules | 120 |
| right positive modules | 118 |
| both positive modules | 74 |
| either positive modules | 164 |
| positive-set Jaccard | 0.4512 |
| signed-delta sign agreement | 0.5431 |
| positive-delta Pearson | 0.3302 |
| positive-delta Spearman | 0.0403 |
| score/cost Pearson | 0.2286 |
| score/cost Spearman | 0.0734 |
| score/cost Kendall tau-a | 0.0671 |

## Top-K Score Overlap

| k | left top-k | right top-k | overlap | union | Jaccard |
|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 10 | 1 | 19 | 0.0526 |
| 20 | 20 | 20 | 5 | 35 | 0.1429 |
| 40 | 40 | 40 | 10 | 70 | 0.1429 |
| 60 | 60 | 60 | 20 | 100 | 0.2000 |

## Interpretation

Low rank correlation or low top-k overlap means the calibration split is
noisy; it does not by itself prove poor downstream PPL. The consensus
allocation should therefore be judged by both this stability audit and
the downstream PPL evidence matrix.
