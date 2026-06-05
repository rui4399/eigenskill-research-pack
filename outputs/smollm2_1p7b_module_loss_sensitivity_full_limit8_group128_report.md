# Module Loss Sensitivity Report

Date: `2026-06-05`
Model: `HuggingFaceTB/SmolLM2-1.7B-Instruct`
Prompts: `8`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `169 / 169`

## Baseline

- FP16 mean NLL: `2.454377`
- FP16 PPL: `11.639183`
- Tokens: `800`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.5000 | 1.0000 | {'4': 156, '8': 13} | 0.7179 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 1 | `model.layers.7.mlp.down_proj` | 16777216 | 0.179285 | 0.000000010686 |
| 7 | `lm_head` | 100663296 | 0.166202 | 0.000000001651 |
| 5 | `model.layers.22.mlp.down_proj` | 16777216 | 0.031041 | 0.000000001850 |
| 2 | `model.layers.0.self_attn.v_proj` | 4194304 | 0.022866 | 0.000000005452 |
| 8 | `model.layers.22.mlp.gate_proj` | 16777216 | 0.020970 | 0.000000001250 |
| 10 | `model.layers.23.mlp.up_proj` | 16777216 | 0.019180 | 0.000000001143 |
| 11 | `model.layers.22.mlp.up_proj` | 16777216 | 0.018871 | 0.000000001125 |
| 15 | `model.layers.0.mlp.gate_proj` | 16777216 | 0.013634 | 0.000000000813 |
| 23 | `model.layers.0.mlp.down_proj` | 16777216 | 0.008808 | 0.000000000525 |
| 3 | `model.layers.10.self_attn.v_proj` | 4194304 | 0.008682 | 0.000000002070 |
| 4 | `model.layers.23.self_attn.o_proj` | 4194304 | 0.007800 | 0.000000001860 |
| 6 | `model.layers.15.self_attn.v_proj` | 4194304 | 0.007368 | 0.000000001757 |
| 29 | `model.layers.21.mlp.up_proj` | 16777216 | 0.007199 | 0.000000000429 |
| 30 | `model.layers.14.mlp.up_proj` | 16777216 | 0.006543 | 0.000000000390 |
| 33 | `model.layers.3.mlp.down_proj` | 16777216 | 0.006244 | 0.000000000372 |
| 37 | `model.layers.12.mlp.up_proj` | 16777216 | 0.005416 | 0.000000000323 |
| 9 | `model.layers.16.self_attn.v_proj` | 4194304 | 0.004848 | 0.000000001156 |
| 42 | `model.layers.8.mlp.up_proj` | 16777216 | 0.004787 | 0.000000000285 |
| 43 | `model.layers.13.mlp.down_proj` | 16777216 | 0.004771 | 0.000000000284 |
| 45 | `model.layers.19.mlp.up_proj` | 16777216 | 0.004603 | 0.000000000274 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
