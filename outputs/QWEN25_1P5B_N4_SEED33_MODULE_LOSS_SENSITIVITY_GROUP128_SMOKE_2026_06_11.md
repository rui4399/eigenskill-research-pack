# Module Loss Sensitivity Report

Date: `2026-06-11`
Model: `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct`
Prompts: `4`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.634608`
- FP16 PPL: `13.937848`
- Tokens: `372`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4953 | 0.9989 | {'4': 136, '8': 61} | 0.7161 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 8 | `model.layers.1.mlp.down_proj` | 13762560 | 0.123846 | 0.000000008999 |
| 18 | `model.layers.26.mlp.down_proj` | 13762560 | 0.057978 | 0.000000004213 |
| 20 | `model.layers.2.mlp.down_proj` | 13762560 | 0.056265 | 0.000000004088 |
| 94 | `lm_head` | 233373696 | 0.041492 | 0.000000000178 |
| 43 | `model.layers.27.mlp.down_proj` | 13762560 | 0.013182 | 0.000000000958 |
| 14 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.011097 | 0.000000004704 |
| 51 | `model.layers.23.mlp.down_proj` | 13762560 | 0.009055 | 0.000000000658 |
| 52 | `model.layers.22.mlp.down_proj` | 13762560 | 0.008957 | 0.000000000651 |
| 53 | `model.layers.6.mlp.gate_proj` | 13762560 | 0.008851 | 0.000000000643 |
| 56 | `model.layers.4.mlp.up_proj` | 13762560 | 0.008435 | 0.000000000613 |
| 60 | `model.layers.1.mlp.up_proj` | 13762560 | 0.007598 | 0.000000000552 |
| 61 | `model.layers.5.mlp.up_proj` | 13762560 | 0.007154 | 0.000000000520 |
| 1 | `model.layers.25.self_attn.v_proj` | 393472 | 0.005904 | 0.000000015004 |
| 65 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.005621 | 0.000000000408 |
| 30 | `model.layers.21.self_attn.o_proj` | 2359296 | 0.005537 | 0.000000002347 |
| 66 | `model.layers.12.mlp.down_proj` | 13762560 | 0.005440 | 0.000000000395 |
| 67 | `model.layers.17.mlp.up_proj` | 13762560 | 0.005339 | 0.000000000388 |
| 68 | `model.layers.20.mlp.up_proj` | 13762560 | 0.005282 | 0.000000000384 |
| 69 | `model.layers.23.mlp.up_proj` | 13762560 | 0.004925 | 0.000000000358 |
| 2 | `model.layers.24.self_attn.v_proj` | 393472 | 0.004913 | 0.000000012487 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
