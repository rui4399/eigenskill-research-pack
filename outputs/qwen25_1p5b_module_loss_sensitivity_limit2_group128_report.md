# SmolLM2 Module Loss Sensitivity Report

Date: `2026-06-04`
Model: `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct`
Prompts: `2`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`

## Baseline

- FP16 mean NLL: `1.745087`
- FP16 PPL: `5.726399`
- Tokens: `254`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9999 | {'4': 137, '8': 60} | 0.6020 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 75 | `lm_head` | 233373696 | 0.093741 | 0.000000000402 |
| 21 | `model.layers.26.mlp.down_proj` | 13762560 | 0.047007 | 0.000000003416 |
| 29 | `model.layers.2.mlp.down_proj` | 13762560 | 0.034742 | 0.000000002524 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.032466 | 0.000000082512 |
| 38 | `model.layers.3.mlp.up_proj` | 13762560 | 0.022985 | 0.000000001670 |
| 39 | `model.layers.3.mlp.down_proj` | 13762560 | 0.022533 | 0.000000001637 |
| 40 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.022066 | 0.000000001603 |
| 41 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.020737 | 0.000000001507 |
| 46 | `model.layers.27.mlp.down_proj` | 13762560 | 0.017165 | 0.000000001247 |
| 47 | `model.layers.2.mlp.up_proj` | 13762560 | 0.016813 | 0.000000001222 |
| 2 | `model.layers.2.self_attn.v_proj` | 393472 | 0.016008 | 0.000000040685 |
| 53 | `model.layers.1.mlp.up_proj` | 13762560 | 0.014961 | 0.000000001087 |
| 60 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.010606 | 0.000000000771 |
| 61 | `model.layers.26.mlp.up_proj` | 13762560 | 0.010263 | 0.000000000746 |
| 3 | `model.layers.3.self_attn.v_proj` | 393472 | 0.009128 | 0.000000023198 |
| 66 | `model.layers.0.mlp.up_proj` | 13762560 | 0.008913 | 0.000000000648 |
| 68 | `model.layers.6.mlp.up_proj` | 13762560 | 0.008219 | 0.000000000597 |
| 69 | `model.layers.15.mlp.up_proj` | 13762560 | 0.007246 | 0.000000000527 |
| 70 | `model.layers.21.mlp.gate_proj` | 13762560 | 0.007181 | 0.000000000522 |
| 71 | `model.layers.19.mlp.down_proj` | 13762560 | 0.006916 | 0.000000000503 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
