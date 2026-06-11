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

- FP16 mean NLL: `2.527216`
- FP16 PPL: `12.518612`
- Tokens: `380`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9999 | {'8': 55, '4': 142} | 0.5539 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 60 | `lm_head` | 233373696 | 0.084807 | 0.000000000363 |
| 10 | `model.layers.1.mlp.down_proj` | 13762560 | 0.076496 | 0.000000005558 |
| 19 | `model.layers.26.mlp.down_proj` | 13762560 | 0.032549 | 0.000000002365 |
| 36 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.012592 | 0.000000000915 |
| 40 | `model.layers.27.mlp.down_proj` | 13762560 | 0.009123 | 0.000000000663 |
| 42 | `model.layers.5.mlp.up_proj` | 13762560 | 0.008584 | 0.000000000624 |
| 44 | `model.layers.26.mlp.gate_proj` | 13762560 | 0.007822 | 0.000000000568 |
| 46 | `model.layers.25.mlp.gate_proj` | 13762560 | 0.007158 | 0.000000000520 |
| 47 | `model.layers.12.mlp.down_proj` | 13762560 | 0.005970 | 0.000000000434 |
| 48 | `model.layers.22.mlp.down_proj` | 13762560 | 0.005775 | 0.000000000420 |
| 49 | `model.layers.8.mlp.up_proj` | 13762560 | 0.005669 | 0.000000000412 |
| 51 | `model.layers.20.mlp.up_proj` | 13762560 | 0.005493 | 0.000000000399 |
| 54 | `model.layers.24.mlp.up_proj` | 13762560 | 0.005215 | 0.000000000379 |
| 58 | `model.layers.4.mlp.down_proj` | 13762560 | 0.005056 | 0.000000000367 |
| 21 | `model.layers.26.self_attn.o_proj` | 2359296 | 0.004929 | 0.000000002089 |
| 63 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.004910 | 0.000000000357 |
| 1 | `model.layers.23.self_attn.v_proj` | 393472 | 0.004456 | 0.000000011324 |
| 67 | `model.layers.18.mlp.down_proj` | 13762560 | 0.004387 | 0.000000000319 |
| 2 | `model.layers.24.self_attn.v_proj` | 393472 | 0.004293 | 0.000000010910 |
| 69 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.004124 | 0.000000000300 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
