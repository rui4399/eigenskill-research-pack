# CSI Null Permutation Gate

Date: `2026-06-11T11:04:27+00:00`
Status: **PASS**

## Summary

- n range: `2 -> 8`
- points: `3`
- permutation samples: `20000`
- minimum observed gain: `0.1747`
- maximum Holm-adjusted p-value: `0.000149993`
- all observed gains positive: `True`
- all Holm-adjusted p-values significant: `True`

## Full-Range Permutation Tests

| metric | n=2 mean | n=8 mean | observed gain | dominance | raw p | Holm p | extreme count / samples |
|---|---:|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.1410 | 0.4918 | 0.3508 | 0.9644 | 4.99975e-05 | 0.000149993 | 0/20000 |
| top-20 Jaccard | 0.2604 | 0.4401 | 0.1797 | 0.9156 | 4.99975e-05 | 0.000149993 | 0/20000 |
| positive-set Jaccard | 0.4244 | 0.5992 | 0.1747 | 0.9867 | 4.99975e-05 | 0.000149993 | 0/20000 |

## Claim Boundary

Valid claim: under a Monte-Carlo permutation label-shuffle null, the measured largest-n stability metrics are unlikely to arise by chance from the pooled smallest-n/largest-n seed-pair values for the supplied artifacts. Invalid claim: this proves a universal scaling law, downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
