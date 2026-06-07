# CSI Trend Significance Gate

Date: `2026-06-07T10:31:38+00:00`
Status: **PASS**

## Summary

- points: `3`
- n range: `2 -> 8`
- bootstrap samples: `5000`
- minimum full-range gain lower CI bound: `0.1352`
- minimum full-range dominance probability: `0.9422`
- all full-range gain CIs positive: `True`
- all full-range dominance probabilities high: `True`

## Full-Range Trend

### n=2 -> n=8

| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |
|---|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.3725 | 0.6645 | 0.2920 | [0.2039, 0.3775] | 0.9422 | 1.0000 |
| top-20 Jaccard | 0.3797 | 0.6449 | 0.2651 | [0.1961, 0.3369] | 0.9778 | 1.0000 |
| positive-set Jaccard | 0.5485 | 0.7282 | 0.1797 | [0.1352, 0.2195] | 0.9644 | 1.0000 |

## Adjacent Steps

### n=2 -> n=4

| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |
|---|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.3725 | 0.4324 | 0.0599 | [-0.0486, 0.1761] | 0.6044 | 0.8608 |
| top-20 Jaccard | 0.3797 | 0.4672 | 0.0875 | [0.0187, 0.1646] | 0.7267 | 0.9952 |
| positive-set Jaccard | 0.5485 | 0.5734 | 0.0249 | [-0.0271, 0.0784] | 0.6089 | 0.8128 |

### n=4 -> n=8

| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |
|---|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.4324 | 0.6645 | 0.2321 | [0.1379, 0.3190] | 0.8622 | 1.0000 |
| top-20 Jaccard | 0.4672 | 0.6449 | 0.1777 | [0.0988, 0.2473] | 0.9022 | 1.0000 |
| positive-set Jaccard | 0.5734 | 0.7282 | 0.1548 | [0.1090, 0.1976] | 0.9378 | 1.0000 |

## Claim Boundary

Valid claim: for Qwen2.5-0.5B-Instruct under the fixed public prompt pool, the n=8 seed-pair stability distribution dominates n=2 for the audited CSI metrics, and independent bootstrap confidence intervals for mean gain are positive. Invalid claim: this proves a universal scaling law, downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
