# W4A8 Activation Reconstruction Gate

Status: **PASS**

## Source

- JSON: `outputs/w4a8_activation_reconstruction_2026_06_08/w4a8_activation_reconstruction.json`

## Summary

- modules OK: `8`
- median W4A8 rel-L2: `0.123810`
- p90 W4A8 rel-L2: `0.190244`
- max W4A8 rel-L2: `0.201512`
- median activation-added rel-L2 vs W4A16: `0.023160`
- max activation-added rel-L2 vs W4A16: `0.048561`
- median activation input rel-L2: `0.023349`
- median compression vs FP32: `7.6411x`
- peak CUDA memory ratio: `0.1456`

## Thresholds

- min_modules: `8`
- max_activation_added_rel_l2: `0.05`
- max_p90_w4a8_rel_l2: `0.25`
- min_median_compression: `3.5`
- max_memory_ratio: `0.9`

## Failures

- none

## Claim Boundary

Valid claim: selected real Qwen3 module activations have bounded added drift from A8 activation quantization.

Invalid claim: this gate does not prove end-to-end LLM acceleration, full-model quality retention, mobile deployment, or SOTA quantization.
