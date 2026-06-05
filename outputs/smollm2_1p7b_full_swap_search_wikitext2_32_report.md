# Allocation Swap Search Report

Base allocation: `outputs/smollm2_1p7b_loss_sensitive_alloc_full_4to8_limit8_group128_summary.json`
Method: `loss_sensitive_4to8`
Prompts: `32`
Evaluated swaps: `4`

## Result

| method | PPL | mean NLL | swap |
|---|---:|---:|---|
| base | 15.1207 | 2.716065 | - |
| best | 15.1207 | 2.716065 | - -> - |

## Interpretation

This is a bounded one-step policy-improvement search using global PPL
feedback. It tests interaction-aware allocation beyond additive
one-module sensitivity, but it is still a fake-quant diagnostic.
