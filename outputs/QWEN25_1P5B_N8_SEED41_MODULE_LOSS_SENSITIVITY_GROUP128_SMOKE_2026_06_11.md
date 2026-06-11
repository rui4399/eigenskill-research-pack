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

- FP16 mean NLL: `2.646808`
- FP16 PPL: `14.108930`
- Tokens: `723`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9999 | {'4': 133, '8': 64} | 0.5728 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 59 | `lm_head` | 233373696 | 0.082673 | 0.000000000354 |
| 6 | `model.layers.1.mlp.down_proj` | 13762560 | 0.081471 | 0.000000005920 |
| 15 | `model.layers.26.mlp.down_proj` | 13762560 | 0.040534 | 0.000000002945 |
| 37 | `model.layers.27.mlp.down_proj` | 13762560 | 0.010227 | 0.000000000743 |
| 38 | `model.layers.2.mlp.down_proj` | 13762560 | 0.010073 | 0.000000000732 |
| 45 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.009143 | 0.000000000664 |
| 49 | `model.layers.4.mlp.up_proj` | 13762560 | 0.008467 | 0.000000000615 |
| 55 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.006691 | 0.000000000486 |
| 56 | `model.layers.5.mlp.up_proj` | 13762560 | 0.005857 | 0.000000000426 |
| 57 | `model.layers.27.mlp.up_proj` | 13762560 | 0.005855 | 0.000000000425 |
| 58 | `model.layers.23.mlp.down_proj` | 13762560 | 0.005138 | 0.000000000373 |
| 19 | `model.layers.26.self_attn.o_proj` | 2359296 | 0.004811 | 0.000000002039 |
| 62 | `model.layers.22.mlp.down_proj` | 13762560 | 0.004748 | 0.000000000345 |
| 63 | `model.layers.12.mlp.down_proj` | 13762560 | 0.004582 | 0.000000000333 |
| 64 | `model.layers.20.mlp.up_proj` | 13762560 | 0.004537 | 0.000000000330 |
| 65 | `model.layers.24.mlp.up_proj` | 13762560 | 0.004465 | 0.000000000324 |
| 1 | `model.layers.24.self_attn.v_proj` | 393472 | 0.004401 | 0.000000011184 |
| 67 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.004048 | 0.000000000294 |
| 25 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.003679 | 0.000000001559 |
| 70 | `model.layers.4.mlp.down_proj` | 13762560 | 0.003665 | 0.000000000266 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
