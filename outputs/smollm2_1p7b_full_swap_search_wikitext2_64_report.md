# Allocation Swap Search Report

Base allocation: `outputs/smollm2_1p7b_loss_sensitive_alloc_full_4to8_limit8_group128_summary.json`
Method: `loss_sensitive_4to8`
Prompts: `64`
Evaluated swaps: `8`

## Result

| method | PPL | mean NLL | swap |
|---|---:|---:|---|
| base | 14.8877 | 2.700537 | - |
| best | 14.8376 | 2.697162 | model.layers.12.self_attn.v_proj -> model.layers.22.self_attn.v_proj |

## Interpretation

This is a bounded one-step policy-improvement search using global PPL
feedback. It tests interaction-aware allocation beyond additive
one-module sensitivity, but it is still a fake-quant diagnostic.
