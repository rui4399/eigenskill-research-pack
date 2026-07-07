# Module Loss Sensitivity Report

Date: `2026-07-07`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `32`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.601212`
- FP16 PPL: `13.480064`
- Tokens: `3532`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9983 | 0.9994 | {'2': 102, '4': 95} | 0.9186 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 49 | `lm_head` | 233373696 | 0.102001 | 0.000000000437 |
| 8 | `model.layers.1.mlp.down_proj` | 13762560 | 0.051163 | 0.000000003718 |
| 18 | `model.layers.26.mlp.down_proj` | 13762560 | 0.030754 | 0.000000002235 |
| 21 | `model.layers.2.mlp.down_proj` | 13762560 | 0.028850 | 0.000000002096 |
| 30 | `model.layers.27.mlp.down_proj` | 13762560 | 0.010543 | 0.000000000766 |
| 41 | `model.layers.1.mlp.up_proj` | 13762560 | 0.006872 | 0.000000000499 |
| 44 | `model.layers.26.mlp.up_proj` | 13762560 | 0.006424 | 0.000000000467 |
| 45 | `model.layers.27.mlp.up_proj` | 13762560 | 0.006378 | 0.000000000463 |
| 46 | `model.layers.2.mlp.up_proj` | 13762560 | 0.006337 | 0.000000000460 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.005170 | 0.000000013139 |
| 54 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.004988 | 0.000000000362 |
| 57 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.004586 | 0.000000000333 |
| 60 | `model.layers.3.mlp.down_proj` | 13762560 | 0.004266 | 0.000000000310 |
| 61 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.004247 | 0.000000000309 |
| 64 | `model.layers.3.mlp.up_proj` | 13762560 | 0.004030 | 0.000000000293 |
| 66 | `model.layers.23.mlp.down_proj` | 13762560 | 0.003674 | 0.000000000267 |
| 67 | `model.layers.4.mlp.down_proj` | 13762560 | 0.003534 | 0.000000000257 |
| 68 | `model.layers.4.mlp.up_proj` | 13762560 | 0.003415 | 0.000000000248 |
| 71 | `model.layers.23.mlp.up_proj` | 13762560 | 0.003253 | 0.000000000236 |
| 72 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.003230 | 0.000000000235 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
