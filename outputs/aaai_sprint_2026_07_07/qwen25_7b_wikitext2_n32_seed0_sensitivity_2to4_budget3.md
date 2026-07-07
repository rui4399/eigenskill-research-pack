# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-7B-Instruct`
Prompts: `32`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.434470`
- FP16 PPL: `11.409767`
- Tokens: `3532`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9997 | 0.9999 | {'4': 88, '2': 109} | 0.9612 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 22 | `lm_head` | 544997376 | 0.084234 | 0.000000000155 |
| 23 | `model.layers.26.mlp.down_proj` | 67895296 | 0.008727 | 0.000000000129 |
| 28 | `model.layers.9.mlp.down_proj` | 67895296 | 0.005090 | 0.000000000075 |
| 30 | `model.layers.26.mlp.up_proj` | 67895296 | 0.004503 | 0.000000000066 |
| 32 | `model.layers.27.mlp.gate_proj` | 67895296 | 0.003621 | 0.000000000053 |
| 33 | `model.layers.9.mlp.up_proj` | 67895296 | 0.003605 | 0.000000000053 |
| 34 | `model.layers.10.mlp.gate_proj` | 67895296 | 0.003352 | 0.000000000049 |
| 37 | `model.layers.2.mlp.gate_proj` | 67895296 | 0.003137 | 0.000000000046 |
| 38 | `model.layers.27.mlp.up_proj` | 67895296 | 0.003067 | 0.000000000045 |
| 1 | `model.layers.27.self_attn.v_proj` | 1835520 | 0.002850 | 0.000000001553 |
| 42 | `model.layers.25.mlp.up_proj` | 67895296 | 0.002661 | 0.000000000039 |
| 43 | `model.layers.15.mlp.gate_proj` | 67895296 | 0.002617 | 0.000000000039 |
| 44 | `model.layers.1.mlp.up_proj` | 67895296 | 0.002575 | 0.000000000038 |
| 45 | `model.layers.10.mlp.up_proj` | 67895296 | 0.002574 | 0.000000000038 |
| 46 | `model.layers.3.mlp.gate_proj` | 67895296 | 0.002526 | 0.000000000037 |
| 47 | `model.layers.14.mlp.down_proj` | 67895296 | 0.002524 | 0.000000000037 |
| 48 | `model.layers.18.mlp.up_proj` | 67895296 | 0.002438 | 0.000000000036 |
| 20 | `model.layers.19.self_attn.o_proj` | 12845056 | 0.002083 | 0.000000000162 |
| 50 | `model.layers.13.mlp.gate_proj` | 67895296 | 0.002068 | 0.000000000030 |
| 51 | `model.layers.0.mlp.down_proj` | 67895296 | 0.002037 | 0.000000000030 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
