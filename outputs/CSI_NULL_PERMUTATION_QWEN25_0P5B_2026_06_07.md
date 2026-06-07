# CSI Null Permutation Gate

Date: `2026-06-07T10:58:30+00:00`
Status: **PASS**

## Summary

- n range: `2 -> 8`
- points: `3`
- permutation samples: `20000`
- minimum observed gain: `0.1797`
- maximum Holm-adjusted p-value: `0.000149993`
- all observed gains positive: `True`
- all Holm-adjusted p-values significant: `True`

## Full-Range Permutation Tests

| metric | n=2 mean | n=8 mean | observed gain | dominance | raw p | Holm p | extreme count / samples |
|---|---:|---:|---:|---:|---:|---:|---:|
| score/cost Spearman | 0.3725 | 0.6645 | 0.2920 | 0.9422 | 4.99975e-05 | 0.000149993 | 0/20000 |
| top-20 Jaccard | 0.3797 | 0.6449 | 0.2651 | 0.9778 | 4.99975e-05 | 0.000149993 | 0/20000 |
| positive-set Jaccard | 0.5485 | 0.7282 | 0.1797 | 0.9644 | 4.99975e-05 | 0.000149993 | 0/20000 |

## Claim Boundary

Valid claim: under a Monte-Carlo permutation label-shuffle null, the measured Qwen2.5-0.5B n=8 stability metrics are unlikely to arise by chance from the pooled n=2/n=8 seed-pair values. Invalid claim: this proves a universal scaling law, downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
