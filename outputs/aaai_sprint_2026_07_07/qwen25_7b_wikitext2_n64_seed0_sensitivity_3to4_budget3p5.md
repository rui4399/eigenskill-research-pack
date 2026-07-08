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

- FP16 mean NLL: `2.362931`
- FP16 PPL: `10.622044`
- Tokens: `6986`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int3 | 3.0000 | 0.8571 | {'3': 197} | 0.0000 |
| loss_sensitive_4to8 | 3.4999 | 1.0000 | {'3': 103, '4': 94} | 0.9612 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 23 | `lm_head` | 544997376 | 0.081905 | 0.000000000150 |
| 21 | `model.layers.26.mlp.down_proj` | 67895296 | 0.014008 | 0.000000000206 |
| 35 | `model.layers.9.mlp.down_proj` | 67895296 | 0.004543 | 0.000000000067 |
| 37 | `model.layers.27.mlp.gate_proj` | 67895296 | 0.003889 | 0.000000000057 |
| 1 | `model.layers.27.self_attn.v_proj` | 1835520 | 0.003626 | 0.000000001975 |
| 39 | `model.layers.27.mlp.up_proj` | 67895296 | 0.003469 | 0.000000000051 |
| 40 | `model.layers.26.mlp.up_proj` | 67895296 | 0.003337 | 0.000000000049 |
| 44 | `model.layers.1.mlp.up_proj` | 67895296 | 0.002953 | 0.000000000043 |
| 46 | `model.layers.10.mlp.gate_proj` | 67895296 | 0.002749 | 0.000000000040 |
| 47 | `model.layers.9.mlp.up_proj` | 67895296 | 0.002516 | 0.000000000037 |
| 49 | `model.layers.25.mlp.up_proj` | 67895296 | 0.002336 | 0.000000000034 |
| 51 | `model.layers.20.mlp.down_proj` | 67895296 | 0.002330 | 0.000000000034 |
| 2 | `model.layers.26.self_attn.v_proj` | 1835520 | 0.002169 | 0.000000001182 |
| 53 | `model.layers.10.mlp.up_proj` | 67895296 | 0.002157 | 0.000000000032 |
| 54 | `model.layers.3.mlp.gate_proj` | 67895296 | 0.002031 | 0.000000000030 |
| 55 | `model.layers.13.mlp.gate_proj` | 67895296 | 0.001964 | 0.000000000029 |
| 56 | `model.layers.2.mlp.gate_proj` | 67895296 | 0.001939 | 0.000000000029 |
| 57 | `model.layers.14.mlp.down_proj` | 67895296 | 0.001849 | 0.000000000027 |
| 58 | `model.layers.15.mlp.gate_proj` | 67895296 | 0.001805 | 0.000000000027 |
| 60 | `model.layers.24.mlp.gate_proj` | 67895296 | 0.001706 | 0.000000000025 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
