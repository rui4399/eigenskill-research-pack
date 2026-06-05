# Module Loss Sensitivity Report

Date: `2026-06-05`
Model: `HuggingFaceTB/SmolLM2-1.7B-Instruct`
Prompts: `8`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `32 / 32`

## Baseline

- FP16 mean NLL: `2.454377`
- FP16 PPL: `11.639183`
- Tokens: `800`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 32} | 0.0000 |
| loss_sensitive_4to8 | 4.4706 | 0.9935 | {'4': 27, '8': 5} | 0.6298 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 1 | `model.layers.0.self_attn.v_proj` | 4194304 | 0.022866 | 0.000000005452 |
| 2 | `model.layers.0.mlp.gate_proj` | 16777216 | 0.013634 | 0.000000000813 |
| 5 | `model.layers.0.mlp.down_proj` | 16777216 | 0.008808 | 0.000000000525 |
| 6 | `model.layers.3.mlp.down_proj` | 16777216 | 0.006244 | 0.000000000372 |
| 12 | `model.layers.3.mlp.gate_proj` | 16777216 | 0.002913 | 0.000000000174 |
| 3 | `model.layers.4.self_attn.k_proj` | 4194304 | 0.002639 | 0.000000000629 |
| 4 | `model.layers.0.self_attn.k_proj` | 4194304 | 0.002565 | 0.000000000612 |
| 13 | `model.layers.2.mlp.gate_proj` | 16777216 | 0.002139 | 0.000000000127 |
| 7 | `model.layers.1.self_attn.q_proj` | 4194304 | 0.001524 | 0.000000000363 |
| 8 | `model.layers.3.self_attn.v_proj` | 4194304 | 0.001304 | 0.000000000311 |
| 9 | `model.layers.3.self_attn.o_proj` | 4194304 | 0.001263 | 0.000000000301 |
| 10 | `model.layers.2.self_attn.k_proj` | 4194304 | 0.001262 | 0.000000000301 |
| 11 | `model.layers.0.self_attn.q_proj` | 4194304 | 0.001001 | 0.000000000239 |
| 14 | `model.layers.2.self_attn.q_proj` | 4194304 | 0.000469 | 0.000000000112 |
| 15 | `model.layers.0.self_attn.o_proj` | 4194304 | -0.001630 | 0.000000000000 |
| 16 | `model.layers.0.mlp.up_proj` | 16777216 | -0.005049 | 0.000000000000 |
| 17 | `model.layers.1.self_attn.k_proj` | 4194304 | -0.004400 | 0.000000000000 |
| 18 | `model.layers.1.self_attn.v_proj` | 4194304 | -0.001217 | 0.000000000000 |
| 19 | `model.layers.1.self_attn.o_proj` | 4194304 | -0.002958 | 0.000000000000 |
| 20 | `model.layers.1.mlp.gate_proj` | 16777216 | -0.001113 | 0.000000000000 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
