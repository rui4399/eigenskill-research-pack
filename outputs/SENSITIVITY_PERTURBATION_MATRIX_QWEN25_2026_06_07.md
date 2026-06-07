# Sensitivity Perturbation Matrix Gate

Date: `2026-06-07T03:07:19+00:00`
Status: **PASS**

## Summary

- cases: `3`
- axes: `model_scale, sample_size`
- sample-size mean Spearman: `0.6356`
- sample-size min top-20 Jaccard: `0.4815`
- model-scale mean Spearman: `0.1273`
- model-scale mean top-20 Jaccard: `0.2903`
- perturbation separation margin: `0.5082`

## Cases

| axis | case | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `sample_size` | `qwen25_0p5b_limit2_vs_limit8` | 169 | 0.6641 | 0.7132 | 0.6000 |
| `sample_size` | `qwen25_1p5b_limit2_vs_limit8` | 197 | 0.6070 | 0.6835 | 0.4815 |
| `model_scale` | `qwen25_0p5b_vs_1p5b_limit2` | 169 | 0.1273 | 0.4828 | 0.2903 |

## Interpretation

Valid claim: in the measured Qwen2.5 sensitivity artifacts, increasing calibration sample count within the same model preserves sensitivity rankings substantially better than transferring the ranking across model scale. Invalid claim: this is downstream quality retention, a universal scaling law, or a production quantization method.

This gate separates two reviewer-critical questions. Calibration sample-size
perturbation tests whether a sensitivity estimate stabilizes as more examples
from the same model/setup are used. Model-scale perturbation tests whether the
same sensitivity ranking can be reused across model sizes. The current evidence
supports treating these as different failure modes.

## Failures

- none
