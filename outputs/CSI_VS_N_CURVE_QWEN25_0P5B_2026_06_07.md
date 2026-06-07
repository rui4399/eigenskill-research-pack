# CSI vs Calibration Size Gate

Date: `2026-06-07T08:12:38+00:00`
Status: **PASS**

## Summary

- curve points: `3`
- n range: `2 -> 8`
- mean score/cost Spearman gain: `0.2920`
- mean top-20 Jaccard gain: `0.2651`
- mean positive-set Jaccard gain: `0.1797`
- score/cost Spearman monotonic: `True`
- top-20 Jaccard monotonic: `True`
- positive-set Jaccard monotonic: `True`

## Curve Points

| n | source gate | cases | pairs | unique selections | mean Spearman | 95% CI | top-20 Jaccard | 95% CI | positive Jaccard | 95% CI |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | `outputs\calibration_seed_stability_qwen25_0p5b_n2_2026_06_07.json` | 6 | 15 | 6 | 0.3725 | [0.2960, 0.4519] | 0.3797 | [0.3336, 0.4270] | 0.5485 | [0.5151, 0.5852] |
| 4 | `outputs\calibration_seed_stability_qwen25_0p5b_2026_06_07.json` | 6 | 15 | 6 | 0.4324 | [0.3557, 0.5174] | 0.4672 | [0.4200, 0.5292] | 0.5734 | [0.5375, 0.6120] |
| 8 | `outputs\calibration_seed_stability_qwen25_0p5b_n8_2026_06_07.json` | 6 | 15 | 6 | 0.6645 | [0.6236, 0.7048] | 0.6449 | [0.5962, 0.6915] | 0.7282 | [0.7050, 0.7520] |

## Adjacent CI Separation

### mean score/cost Spearman
- n=2 -> n=4: `False`
- n=4 -> n=8: `True`

### mean top-20 Jaccard
- n=2 -> n=4: `False`
- n=4 -> n=8: `True`

### mean positive-set Jaccard
- n=2 -> n=4: `False`
- n=4 -> n=8: `True`

## Claim Boundary

Valid claim: on Qwen2.5-0.5B-Instruct and this public WikiText2 prompt pool, six deterministic prompt seeds show that sensitivity-ranking stability improves as calibration prompt count increases from n=2 to n=8. Invalid claim: this curve alone proves downstream task retention, real quantized runtime speed, or large-model universality.

## Failures

- none
