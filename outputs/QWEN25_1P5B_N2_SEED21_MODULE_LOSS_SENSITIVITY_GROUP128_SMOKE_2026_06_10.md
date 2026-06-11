# Module Loss Sensitivity Report

Date: `2026-06-10`
Model: `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct`
Prompts: `2`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `3.720419`
- FP16 PPL: `41.281671`
- Tokens: `156`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4973 | 0.9994 | {'8': 67, '4': 130} | 0.6472 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 21 | `model.layers.2.mlp.down_proj` | 13762560 | 0.075143 | 0.000000005460 |
| 102 | `lm_head` | 233373696 | 0.062429 | 0.000000000268 |
| 26 | `model.layers.1.mlp.down_proj` | 13762560 | 0.048462 | 0.000000003521 |
| 32 | `model.layers.26.mlp.down_proj` | 13762560 | 0.038551 | 0.000000002801 |
| 41 | `model.layers.1.mlp.up_proj` | 13762560 | 0.023853 | 0.000000001733 |
| 43 | `model.layers.1.mlp.gate_proj` | 13762560 | 0.020275 | 0.000000001473 |
| 47 | `model.layers.27.mlp.down_proj` | 13762560 | 0.018384 | 0.000000001336 |
| 56 | `model.layers.3.mlp.up_proj` | 13762560 | 0.014380 | 0.000000001045 |
| 57 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.013778 | 0.000000001001 |
| 1 | `model.layers.15.self_attn.v_proj` | 393472 | 0.012132 | 0.000000030833 |
| 63 | `model.layers.9.mlp.down_proj` | 13762560 | 0.010167 | 0.000000000739 |
| 64 | `model.layers.0.mlp.up_proj` | 13762560 | 0.010042 | 0.000000000730 |
| 65 | `model.layers.11.mlp.up_proj` | 13762560 | 0.009984 | 0.000000000725 |
| 24 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.009664 | 0.000000004096 |
| 2 | `model.layers.8.self_attn.v_proj` | 393472 | 0.008868 | 0.000000022539 |
| 66 | `model.layers.5.mlp.gate_proj` | 13762560 | 0.008717 | 0.000000000633 |
| 25 | `model.layers.7.self_attn.o_proj` | 2359296 | 0.008661 | 0.000000003671 |
| 69 | `model.layers.4.mlp.up_proj` | 13762560 | 0.008311 | 0.000000000604 |
| 27 | `model.layers.0.self_attn.q_proj` | 2360832 | 0.008247 | 0.000000003493 |
| 72 | `model.layers.12.mlp.up_proj` | 13762560 | 0.008179 | 0.000000000594 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
