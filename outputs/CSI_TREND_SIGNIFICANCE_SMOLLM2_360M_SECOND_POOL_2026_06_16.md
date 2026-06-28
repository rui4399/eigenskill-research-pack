# CSI Trend Significance Gate

Date: `2026-06-28T10:47:57+00:00`
Status: **PASS**

## Summary

- points: `3`
- n range: `4 -> 16`
- bootstrap samples: `5000`
- minimum full-range gain lower CI bound: `0.1395`
- minimum full-range dominance probability: `0.9644`
- all full-range gain CIs positive: `True`
- all full-range dominance probabilities high: `True`

## Full-Range Trend

### n=4 -> n=16

| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |
|---|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.3133 | 0.6959 | 0.3825 | [0.3118, 0.4511] | 1.0000 | 1.0000 |
| top-20 Jaccard | 0.3779 | 0.5761 | 0.1982 | [0.1395, 0.2554] | 0.9644 | 1.0000 |
| positive-set Jaccard | 0.5390 | 0.7512 | 0.2122 | [0.1758, 0.2491] | 1.0000 | 1.0000 |

## Adjacent Steps

### n=4 -> n=8

| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |
|---|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.3133 | 0.4136 | 0.1003 | [0.0127, 0.1866] | 0.7111 | 0.9870 |
| top-20 Jaccard | 0.3779 | 0.4363 | 0.0585 | [-0.0075, 0.1267] | 0.6578 | 0.9592 |
| positive-set Jaccard | 0.5390 | 0.5991 | 0.0600 | [0.0149, 0.1031] | 0.7311 | 0.9954 |

### n=8 -> n=16

| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |
|---|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.4136 | 0.6959 | 0.2822 | [0.2063, 0.3595] | 0.9867 | 1.0000 |
| top-20 Jaccard | 0.4363 | 0.5761 | 0.1397 | [0.0922, 0.1865] | 0.9178 | 1.0000 |
| positive-set Jaccard | 0.5991 | 0.7512 | 0.1522 | [0.1147, 0.1900] | 1.0000 | 1.0000 |

## Claim Boundary

Valid claim: for the supplied same-model calibration-seed-stability artifacts under a fixed prompt pool, the largest-n seed-pair stability distribution dominates the smallest-n distribution for the audited CSI metrics, and independent bootstrap confidence intervals for mean gain are positive. Invalid claim: this proves a universal scaling law, downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
