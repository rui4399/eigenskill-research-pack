# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-7B-Instruct`
Prompts: `64`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.422071`
- FP16 PPL: `11.269176`
- Tokens: `7141`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9997 | 0.9999 | {'2': 103, '4': 94} | 0.9662 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 26 | `lm_head` | 544997376 | 0.084827 | 0.000000000156 |
| 21 | `model.layers.26.mlp.down_proj` | 67895296 | 0.017180 | 0.000000000253 |
| 37 | `model.layers.27.mlp.up_proj` | 67895296 | 0.004269 | 0.000000000063 |
| 1 | `model.layers.27.self_attn.v_proj` | 1835520 | 0.004231 | 0.000000002305 |
| 38 | `model.layers.26.mlp.up_proj` | 67895296 | 0.003923 | 0.000000000058 |
| 39 | `model.layers.25.mlp.up_proj` | 67895296 | 0.003905 | 0.000000000058 |
| 40 | `model.layers.27.mlp.gate_proj` | 67895296 | 0.003721 | 0.000000000055 |
| 41 | `model.layers.10.mlp.gate_proj` | 67895296 | 0.003106 | 0.000000000046 |
| 42 | `model.layers.27.mlp.down_proj` | 67895296 | 0.003031 | 0.000000000045 |
| 44 | `model.layers.1.mlp.up_proj` | 67895296 | 0.002939 | 0.000000000043 |
| 46 | `model.layers.9.mlp.down_proj` | 67895296 | 0.002887 | 0.000000000043 |
| 50 | `model.layers.10.mlp.up_proj` | 67895296 | 0.002597 | 0.000000000038 |
| 2 | `model.layers.26.self_attn.v_proj` | 1835520 | 0.002382 | 0.000000001298 |
| 3 | `model.layers.13.self_attn.v_proj` | 1835520 | 0.002265 | 0.000000001234 |
| 53 | `model.layers.23.mlp.up_proj` | 67895296 | 0.002186 | 0.000000000032 |
| 24 | `model.layers.19.self_attn.o_proj` | 12845056 | 0.002133 | 0.000000000166 |
| 54 | `model.layers.13.mlp.gate_proj` | 67895296 | 0.002029 | 0.000000000030 |
| 55 | `model.layers.12.mlp.up_proj` | 67895296 | 0.001922 | 0.000000000028 |
| 57 | `model.layers.9.mlp.gate_proj` | 67895296 | 0.001885 | 0.000000000028 |
| 58 | `model.layers.24.mlp.gate_proj` | 67895296 | 0.001859 | 0.000000000027 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
