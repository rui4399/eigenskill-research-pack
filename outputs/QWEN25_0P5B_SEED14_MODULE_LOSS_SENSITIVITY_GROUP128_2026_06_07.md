# Module Loss Sensitivity Report

Date: `2026-06-07`
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Prompts: `4`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `169 / 169`

## Baseline

- FP16 mean NLL: `3.443689`
- FP16 PPL: `31.302225`
- Tokens: `380`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 109, '8': 60} | 0.6380 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 86 | `lm_head` | 136134656 | 0.111270 | 0.000000000817 |
| 14 | `model.layers.21.mlp.down_proj` | 4358144 | 0.098043 | 0.000000022496 |
| 23 | `model.layers.2.mlp.down_proj` | 4358144 | 0.066116 | 0.000000015171 |
| 28 | `model.layers.3.mlp.down_proj` | 4358144 | 0.053431 | 0.000000012260 |
| 36 | `model.layers.23.mlp.down_proj` | 4358144 | 0.032649 | 0.000000007491 |
| 46 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.013419 | 0.000000003079 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.013288 | 0.000000115737 |
| 47 | `model.layers.16.mlp.down_proj` | 4358144 | 0.013124 | 0.000000003011 |
| 2 | `model.layers.15.self_attn.v_proj` | 114816 | 0.011332 | 0.000000098697 |
| 51 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.011199 | 0.000000002570 |
| 52 | `model.layers.6.mlp.down_proj` | 4358144 | 0.010796 | 0.000000002477 |
| 27 | `model.layers.23.self_attn.o_proj` | 802816 | 0.010558 | 0.000000013151 |
| 54 | `model.layers.18.mlp.gate_proj` | 4358144 | 0.010541 | 0.000000002419 |
| 3 | `model.layers.0.self_attn.v_proj` | 114816 | 0.010355 | 0.000000090187 |
| 55 | `model.layers.11.mlp.up_proj` | 4358144 | 0.009834 | 0.000000002257 |
| 56 | `model.layers.1.mlp.gate_proj` | 4358144 | 0.009456 | 0.000000002170 |
| 58 | `model.layers.1.mlp.up_proj` | 4358144 | 0.008958 | 0.000000002055 |
| 60 | `model.layers.16.mlp.gate_proj` | 4358144 | 0.008408 | 0.000000001929 |
| 4 | `model.layers.4.self_attn.v_proj` | 114816 | 0.008190 | 0.000000071330 |
| 62 | `model.layers.22.mlp.down_proj` | 4358144 | 0.007267 | 0.000000001667 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
