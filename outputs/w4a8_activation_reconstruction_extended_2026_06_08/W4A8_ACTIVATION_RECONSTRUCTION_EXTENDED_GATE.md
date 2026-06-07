# W4A8 Activation Reconstruction Gate

Status: **PASS**

## Source

- JSON: `outputs/w4a8_activation_reconstruction_extended_2026_06_08/w4a8_activation_reconstruction_extended.json`

## Summary

- modules OK: `24`
- median W4A8 rel-L2: `0.144851`
- p90 W4A8 rel-L2: `0.212923`
- max W4A8 rel-L2: `0.252123`
- median activation-added rel-L2 vs W4A16: `0.031801`
- max activation-added rel-L2 vs W4A16: `0.084533`
- median activation input rel-L2: `0.035115`
- median compression vs FP32: `7.6413x`
- peak CUDA memory ratio: `0.1467`

## Thresholds

- min_modules: `24`
- max_activation_added_rel_l2: `0.09`
- max_p90_w4a8_rel_l2: `0.3`
- min_median_compression: `3.5`
- max_memory_ratio: `0.9`

## Failures

- none

## Claim Boundary

Valid claim: selected real Qwen3 module activations have bounded added drift from A8 activation quantization.

Invalid claim: this gate does not prove end-to-end LLM acceleration, full-model quality retention, mobile deployment, or SOTA quantization.
