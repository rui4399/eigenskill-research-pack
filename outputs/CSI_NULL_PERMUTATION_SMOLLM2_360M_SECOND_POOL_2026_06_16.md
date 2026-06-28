# CSI Null Permutation Gate

Date: `2026-06-28T10:47:58+00:00`
Status: **PASS**

## Summary

- n range: `4 -> 16`
- points: `3`
- permutation samples: `5000`
- minimum observed gain: `0.1982`
- maximum Holm-adjusted p-value: `0.00059988`
- all observed gains positive: `True`
- all Holm-adjusted p-values significant: `True`

## Full-Range Permutation Tests

| metric | n=2 mean | n=8 mean | observed gain | dominance | raw p | Holm p | extreme count / samples |
|---|---:|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.3133 | 0.6959 | 0.3825 | 1.0000 | 0.00019996 | 0.00059988 | 0/5000 |
| top-20 Jaccard | 0.3779 | 0.5761 | 0.1982 | 0.9644 | 0.00019996 | 0.00059988 | 0/5000 |
| positive-set Jaccard | 0.5390 | 0.7512 | 0.2122 | 1.0000 | 0.00019996 | 0.00059988 | 0/5000 |

## Claim Boundary

Valid claim: under a Monte-Carlo permutation label-shuffle null, the measured largest-n stability metrics are unlikely to arise by chance from the pooled smallest-n/largest-n seed-pair values for the supplied artifacts. Invalid claim: this proves a universal scaling law, downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
