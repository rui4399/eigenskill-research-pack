# CSI Cross-Scale Comparison Gate

Date: `2026-06-11T14:30:59+00:00`
Status: **PASS**

## Summary

- left: `qwen25_0p5b`
- right: `qwen25_1p5b`
- common n values: `[2, 4, 8]`
- right lower at all shared n/metrics: `True`

## Same-n Comparison

| n | metric | left | right | right - left |
|---:|---|---:|---:|---:|
| 2 | mean score/cost Spearman | 0.3725 | 0.1410 | -0.2315 |
| 2 | mean top-20 Jaccard | 0.3797 | 0.2604 | -0.1193 |
| 2 | mean positive-set Jaccard | 0.5485 | 0.4244 | -0.1240 |
| 4 | mean score/cost Spearman | 0.4324 | 0.2869 | -0.1455 |
| 4 | mean top-20 Jaccard | 0.4672 | 0.3313 | -0.1359 |
| 4 | mean positive-set Jaccard | 0.5734 | 0.5189 | -0.0545 |
| 8 | mean score/cost Spearman | 0.6645 | 0.4918 | -0.1727 |
| 8 | mean top-20 Jaccard | 0.6449 | 0.4401 | -0.2048 |
| 8 | mean positive-set Jaccard | 0.7282 | 0.5992 | -0.1291 |

## Full-Range Gain Comparison

| metric | n range | left gain | right gain | right gain - left gain |
|---|---|---:|---:|---:|
| mean score/cost Spearman | 2 -> 8 | 0.2920 | 0.3508 | 0.0588 |
| mean top-20 Jaccard | 2 -> 8 | 0.2651 | 0.1797 | -0.0855 |
| mean positive-set Jaccard | 2 -> 8 | 0.1797 | 0.1747 | -0.0050 |

## Interpretation

- In these artifacts, `qwen25_1p5b` is lower than `qwen25_0p5b` at every shared n and audited metric.
- Both scales still improve as calibration prompt count increases.
- The evidence supports a conservative scale-up replication of CSI, not a causal model-size claim.

## Claim Boundary

Valid claim: for the supplied same-prompt-pool Qwen2.5 curve artifacts, the right-hand scale has lower measured stability than the left-hand scale at the shared n values, while both curves improve from the smallest to the largest n. Invalid claim: this proves that model size alone causes lower stability, a universal scaling law, downstream retention, or SOTA quantization.

## Failures

- none
