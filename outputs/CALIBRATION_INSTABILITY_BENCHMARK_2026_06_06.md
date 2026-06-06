# Calibration Split Instability Benchmark

Date: `2026-06-06T11:06:37+00:00`
Status: **PASS**

## Aggregate

- cases: `3`
- unstable cases: `3`
- mean score/cost Spearman: `0.0713`
- mean positive-set Jaccard: `0.4349`
- mean top-20 Jaccard: `0.1022`

## Cases

| case | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard | unstable |
|---|---:|---:|---:|---:|---:|
| `qwen3_0p6b` | 197 | -0.0440 | 0.4024 | 0.0526 | True |
| `qwen3_1p7b` | 197 | 0.0734 | 0.4512 | 0.1429 | True |
| `olmo2_1b` | 113 | 0.1845 | 0.4512 | 0.1111 | True |

## Interpretation

This benchmark measures how much module-sensitivity rankings move when
the calibration distribution changes. Low score/cost rank correlation
or low sensitive-set overlap supports the calibration-robustness problem
definition; downstream PPL and task gates are still required before
claiming a better quantizer.

## Failures

- none
