# CSI vs Calibration Size Gate

Date: `2026-06-28T10:47:57+00:00`
Status: **PASS**

## Summary

- curve points: `3`
- n range: `4 -> 16`
- mean score/cost Spearman gain: `0.3825`
- mean top-20 Jaccard gain: `0.1982`
- mean positive-set Jaccard gain: `0.2122`
- score/cost Spearman monotonic: `True`
- top-20 Jaccard monotonic: `True`
- positive-set Jaccard monotonic: `True`

## Curve Points

| n | source gate | cases | pairs | unique selections | mean Spearman | 95% CI | top-20 Jaccard | 95% CI | positive Jaccard | 95% CI |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | `outputs/calibration_seed_stability_smollm2_360m_n4_second_pool_2026_06_16.json` | 6 | 15 | 6 | 0.3133 | [0.2570, 0.3700] | 0.3779 | [0.3254, 0.4319] | 0.5390 | [0.5086, 0.5681] |
| 8 | `outputs/calibration_seed_stability_smollm2_360m_n8_second_pool_2026_06_16.json` | 6 | 15 | 6 | 0.4136 | [0.3474, 0.4765] | 0.4363 | [0.3955, 0.4779] | 0.5991 | [0.5659, 0.6305] |
| 16 | `outputs/calibration_seed_stability_smollm2_360m_n16_second_pool_2026_06_16.json` | 6 | 15 | 6 | 0.6959 | [0.6546, 0.7389] | 0.5761 | [0.5549, 0.5979] | 0.7512 | [0.7303, 0.7718] |

## Adjacent CI Separation

### mean score/cost Spearman
- n=4 -> n=8: `False`
- n=8 -> n=16: `True`

### mean top-20 Jaccard
- n=4 -> n=8: `False`
- n=8 -> n=16: `True`

### mean positive-set Jaccard
- n=4 -> n=8: `False`
- n=8 -> n=16: `True`

## Claim Boundary

Valid claim: for the supplied same-model calibration-seed-stability artifacts, the audited prompt-seed sensitivity rankings become more stable as calibration prompt count increases across the provided n values. Invalid claim: this curve alone proves downstream task retention, real quantized runtime speed, SOTA quantization, or large-model universality.

## Failures

- none
