# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `64`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.978135`
- FP16 PPL: `19.651134`
- Tokens: `7447`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9999 | 1.0000 | {'4': 112, '2': 85} | 0.9233 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 42 | `lm_head` | 233373696 | 0.106154 | 0.000000000455 |
| 5 | `model.layers.1.mlp.down_proj` | 13762560 | 0.054895 | 0.000000003989 |
| 11 | `model.layers.26.mlp.down_proj` | 13762560 | 0.034604 | 0.000000002514 |
| 14 | `model.layers.2.mlp.down_proj` | 13762560 | 0.030468 | 0.000000002214 |
| 28 | `model.layers.26.mlp.up_proj` | 13762560 | 0.012228 | 0.000000000889 |
| 38 | `model.layers.27.mlp.down_proj` | 13762560 | 0.009030 | 0.000000000656 |
| 52 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.004256 | 0.000000000309 |
| 53 | `model.layers.1.mlp.up_proj` | 13762560 | 0.004224 | 0.000000000307 |
| 57 | `model.layers.26.mlp.gate_proj` | 13762560 | 0.003674 | 0.000000000267 |
| 59 | `model.layers.27.mlp.up_proj` | 13762560 | 0.003381 | 0.000000000246 |
| 21 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.003317 | 0.000000001406 |
| 69 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.002731 | 0.000000000198 |
| 71 | `model.layers.22.mlp.gate_proj` | 13762560 | 0.002716 | 0.000000000197 |
| 73 | `model.layers.22.mlp.up_proj` | 13762560 | 0.002694 | 0.000000000196 |
| 75 | `model.layers.3.mlp.up_proj` | 13762560 | 0.002613 | 0.000000000190 |
| 78 | `model.layers.19.mlp.up_proj` | 13762560 | 0.002403 | 0.000000000175 |
| 80 | `model.layers.20.mlp.up_proj` | 13762560 | 0.002324 | 0.000000000169 |
| 83 | `model.layers.21.mlp.up_proj` | 13762560 | 0.002240 | 0.000000000163 |
| 84 | `model.layers.23.mlp.down_proj` | 13762560 | 0.002186 | 0.000000000159 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.002087 | 0.000000005305 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
