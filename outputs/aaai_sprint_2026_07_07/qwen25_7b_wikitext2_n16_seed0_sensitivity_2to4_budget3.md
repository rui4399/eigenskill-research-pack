# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-7B-Instruct`
Prompts: `16`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.440066`
- FP16 PPL: `11.473792`
- Tokens: `1866`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9982 | 0.9994 | {'4': 97, '2': 100} | 0.9641 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 27 | `lm_head` | 544997376 | 0.100616 | 0.000000000185 |
| 24 | `model.layers.26.mlp.down_proj` | 67895296 | 0.015074 | 0.000000000222 |
| 26 | `model.layers.27.mlp.down_proj` | 67895296 | 0.013108 | 0.000000000193 |
| 37 | `model.layers.9.mlp.down_proj` | 67895296 | 0.006220 | 0.000000000092 |
| 1 | `model.layers.27.self_attn.v_proj` | 1835520 | 0.005465 | 0.000000002977 |
| 41 | `model.layers.25.mlp.up_proj` | 67895296 | 0.004678 | 0.000000000069 |
| 45 | `model.layers.27.mlp.gate_proj` | 67895296 | 0.003893 | 0.000000000057 |
| 46 | `model.layers.26.mlp.up_proj` | 67895296 | 0.003823 | 0.000000000056 |
| 49 | `model.layers.12.mlp.gate_proj` | 67895296 | 0.003445 | 0.000000000051 |
| 2 | `model.layers.5.self_attn.v_proj` | 1835520 | 0.003194 | 0.000000001740 |
| 50 | `model.layers.6.mlp.up_proj` | 67895296 | 0.003083 | 0.000000000045 |
| 51 | `model.layers.9.mlp.gate_proj` | 67895296 | 0.002948 | 0.000000000043 |
| 53 | `model.layers.16.mlp.down_proj` | 67895296 | 0.002754 | 0.000000000041 |
| 54 | `model.layers.14.mlp.down_proj` | 67895296 | 0.002660 | 0.000000000039 |
| 55 | `model.layers.23.mlp.up_proj` | 67895296 | 0.002634 | 0.000000000039 |
| 25 | `model.layers.0.self_attn.o_proj` | 12845056 | 0.002601 | 0.000000000203 |
| 56 | `model.layers.13.mlp.gate_proj` | 67895296 | 0.002479 | 0.000000000037 |
| 57 | `model.layers.16.mlp.gate_proj` | 67895296 | 0.002470 | 0.000000000036 |
| 58 | `model.layers.10.mlp.up_proj` | 67895296 | 0.002468 | 0.000000000036 |
| 59 | `model.layers.5.mlp.up_proj` | 67895296 | 0.002460 | 0.000000000036 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
