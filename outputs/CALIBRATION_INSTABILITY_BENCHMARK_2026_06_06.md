# Calibration Split Instability Benchmark

Date: `2026-06-06T15:43:15+00:00`
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

## Statistical Robustness

| statistic | mean | 95% CI low | 95% CI high |
|---|---:|---:|---:|
| score/cost Spearman | 0.0713 | -0.0440 | 0.1845 |
| positive-set Jaccard | 0.4349 | 0.4024 | 0.4512 |
| selected top-k Jaccard | 0.1022 | 0.0526 | 0.1429 |

- mean selected top-k random-expected Jaccard: `0.0680`
- mean observed/random-expected top-k ratio: `1.6000`

### Top-K Overlap vs Random Expectation

| case | k | observed Jaccard | random expected Jaccard | observed/expected |
|---|---:|---:|---:|---:|
| `qwen3_0p6b` | 20 | 0.0526 | 0.0535 | 0.9842 |
| `qwen3_1p7b` | 20 | 0.1429 | 0.0535 | 2.6714 |
| `olmo2_1b` | 20 | 0.1111 | 0.0971 | 1.1444 |

## Interpretation

This benchmark measures how much module-sensitivity rankings move when
the calibration distribution changes. Low score/cost rank correlation
or low sensitive-set overlap supports the calibration-robustness problem
definition; downstream PPL and task gates are still required before
claiming a better quantizer.

## Failures

- none
