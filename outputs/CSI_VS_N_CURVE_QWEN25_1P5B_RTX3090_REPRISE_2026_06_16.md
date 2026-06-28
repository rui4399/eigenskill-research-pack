# CSI vs Calibration Size Gate

Date: `2026-06-16T14:23:38+00:00`
Status: **PASS**

## Summary

- curve points: `3`
- n range: `2 -> 8`
- mean score/cost Spearman gain: `0.3508`
- mean top-20 Jaccard gain: `0.1797`
- mean positive-set Jaccard gain: `0.1747`
- score/cost Spearman monotonic: `True`
- top-20 Jaccard monotonic: `True`
- positive-set Jaccard monotonic: `True`

## Curve Points

| n | source gate | cases | pairs | unique selections | mean Spearman | 95% CI | top-20 Jaccard | 95% CI | positive Jaccard | 95% CI |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | `outputs/calibration_seed_stability_qwen25_1p5b_n2_2026_06_10.json` | 6 | 15 | 6 | 0.1410 | [0.0779, 0.2133] | 0.2604 | [0.2213, 0.3060] | 0.4244 | [0.3954, 0.4564] |
| 4 | `outputs/calibration_seed_stability_qwen25_1p5b_n4_2026_06_11.json` | 6 | 15 | 6 | 0.2869 | [0.2312, 0.3506] | 0.3313 | [0.2973, 0.3697] | 0.5189 | [0.4954, 0.5449] |
| 8 | `outputs/calibration_seed_stability_qwen25_1p5b_n8_2026_06_11.json` | 6 | 15 | 6 | 0.4918 | [0.4432, 0.5458] | 0.4401 | [0.3979, 0.4777] | 0.5992 | [0.5773, 0.6221] |

## Adjacent CI Separation

### mean score/cost Spearman
- n=2 -> n=4: `True`
- n=4 -> n=8: `True`

### mean top-20 Jaccard
- n=2 -> n=4: `False`
- n=4 -> n=8: `True`

### mean positive-set Jaccard
- n=2 -> n=4: `True`
- n=4 -> n=8: `True`

## Claim Boundary

Valid claim: for the supplied same-model calibration-seed-stability artifacts, the audited prompt-seed sensitivity rankings become more stable as calibration prompt count increases across the provided n values. Invalid claim: this curve alone proves downstream task retention, real quantized runtime speed, SOTA quantization, or large-model universality.

## Failures

- none
