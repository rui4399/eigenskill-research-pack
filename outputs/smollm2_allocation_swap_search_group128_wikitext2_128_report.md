# Allocation Swap Search Report

Base allocation: `outputs/smollm2_loss_sensitive_alloc_4to8_limit4_group128_summary.json`
Method: `loss_sensitive_4to8`
Prompts: `128`
Evaluated swaps: `8`

## Result

| method | PPL | mean NLL | swap |
|---|---:|---:|---|
| base | 24.1374 | 3.183762 | - |
| best | 24.0661 | 3.180804 | model.layers.17.self_attn.v_proj -> model.layers.24.self_attn.v_proj |

## Interpretation

This is a bounded one-step policy-improvement search using global PPL
feedback. It tests interaction-aware allocation beyond additive
one-module sensitivity, but it is still a fake-quant diagnostic.
