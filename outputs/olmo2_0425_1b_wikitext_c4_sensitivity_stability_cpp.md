# Quant Sensitivity Split Stability

Left: `outputs/olmo2_0425_1b_module_loss_sensitivity_limit2_group128.json` (`WikiText2`)
Right: `outputs/olmo2_0425_1b_module_loss_sensitivity_c4_limit2_group128.json` (`C4`)

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

## Top-K Score Overlap

| k | left top-k | right top-k | overlap | union | Jaccard |
|---:|---:|---:|---:|---:|---:|
| 10 | 10 | 10 | 2 | 18 | 0.1111 |
| 20 | 20 | 20 | 4 | 36 | 0.1111 |
| 40 | 40 | 40 | 17 | 63 | 0.2698 |

This C++ audit mirrors the Python split-stability diagnostic. It supports the claim that single-split loss sensitivity is noisy and should be paired with downstream PPL evidence.
