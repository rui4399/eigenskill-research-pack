# Module Loss Sensitivity Report

Date: `2026-06-11`
Model: `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct`
Prompts: `8`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.826645`
- FP16 PPL: `16.888701`
- Tokens: `681`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4973 | 0.9994 | {'8': 53, '4': 144} | 0.6540 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 3 | `model.layers.1.mlp.down_proj` | 13762560 | 0.111053 | 0.000000008069 |
| 57 | `lm_head` | 233373696 | 0.067485 | 0.000000000289 |
| 12 | `model.layers.26.mlp.down_proj` | 13762560 | 0.046825 | 0.000000003402 |
| 18 | `model.layers.2.mlp.down_proj` | 13762560 | 0.028626 | 0.000000002080 |
| 32 | `model.layers.1.mlp.up_proj` | 13762560 | 0.014030 | 0.000000001019 |
| 33 | `model.layers.27.mlp.down_proj` | 13762560 | 0.012887 | 0.000000000936 |
| 39 | `model.layers.3.mlp.down_proj` | 13762560 | 0.008029 | 0.000000000583 |
| 40 | `model.layers.22.mlp.down_proj` | 13762560 | 0.007976 | 0.000000000580 |
| 42 | `model.layers.3.mlp.up_proj` | 13762560 | 0.007101 | 0.000000000516 |
| 1 | `model.layers.20.self_attn.v_proj` | 393472 | 0.005940 | 0.000000015096 |
| 47 | `model.layers.4.mlp.up_proj` | 13762560 | 0.005420 | 0.000000000394 |
| 48 | `model.layers.19.mlp.down_proj` | 13762560 | 0.005226 | 0.000000000380 |
| 51 | `model.layers.21.mlp.down_proj` | 13762560 | 0.004863 | 0.000000000353 |
| 52 | `model.layers.26.mlp.gate_proj` | 13762560 | 0.004459 | 0.000000000324 |
| 22 | `model.layers.25.self_attn.o_proj` | 2359296 | 0.004161 | 0.000000001764 |
| 54 | `model.layers.23.mlp.down_proj` | 13762560 | 0.004134 | 0.000000000300 |
| 55 | `model.layers.8.mlp.up_proj` | 13762560 | 0.004054 | 0.000000000295 |
| 56 | `model.layers.5.mlp.up_proj` | 13762560 | 0.004021 | 0.000000000292 |
| 58 | `model.layers.20.mlp.up_proj` | 13762560 | 0.003926 | 0.000000000285 |
| 2 | `model.layers.21.self_attn.v_proj` | 393472 | 0.003638 | 0.000000009247 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
