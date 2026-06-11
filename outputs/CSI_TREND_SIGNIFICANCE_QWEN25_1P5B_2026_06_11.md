# CSI Trend Significance Gate

Date: `2026-06-11T11:04:26+00:00`
Status: **PASS**

## Summary

- points: `3`
- n range: `2 -> 8`
- bootstrap samples: `5000`
- minimum full-range gain lower CI bound: `0.1197`
- minimum full-range dominance probability: `0.9156`
- all full-range gain CIs positive: `True`
- all full-range dominance probabilities high: `True`

## Full-Range Trend

### n=2 -> n=8

| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |
|---|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.1410 | 0.4918 | 0.3508 | [0.2641, 0.4320] | 0.9644 | 1.0000 |
| top-20 Jaccard | 0.2604 | 0.4401 | 0.1797 | [0.1197, 0.2348] | 0.9156 | 1.0000 |
| positive-set Jaccard | 0.4244 | 0.5992 | 0.1747 | [0.1354, 0.2126] | 0.9867 | 1.0000 |

## Adjacent Steps

### n=2 -> n=4

| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |
|---|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.1410 | 0.2869 | 0.1459 | [0.0550, 0.2374] | 0.7867 | 0.9988 |
| top-20 Jaccard | 0.2604 | 0.3313 | 0.0709 | [0.0139, 0.1253] | 0.7822 | 0.9926 |
| positive-set Jaccard | 0.4244 | 0.5189 | 0.0944 | [0.0528, 0.1353] | 0.8978 | 1.0000 |

### n=4 -> n=8

| metric | left mean | right mean | mean gain | bootstrap 95% gain CI | P(right pair > left pair) | P(bootstrap gain > 0) |
|---|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.2869 | 0.4918 | 0.2049 | [0.1234, 0.2840] | 0.9022 | 1.0000 |
| top-20 Jaccard | 0.3313 | 0.4401 | 0.1088 | [0.0522, 0.1613] | 0.8333 | 1.0000 |
| positive-set Jaccard | 0.5189 | 0.5992 | 0.0803 | [0.0444, 0.1143] | 0.8622 | 1.0000 |

## Claim Boundary

Valid claim: for the supplied same-model calibration-seed-stability artifacts under a fixed prompt pool, the largest-n seed-pair stability distribution dominates the smallest-n distribution for the audited CSI metrics, and independent bootstrap confidence intervals for mean gain are positive. Invalid claim: this proves a universal scaling law, downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
