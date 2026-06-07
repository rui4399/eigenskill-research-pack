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

- FP16 mean NLL: `3.155487`
- FP16 PPL: `23.464465`
- Tokens: `352`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4988 | 0.9997 | {'4': 110, '8': 59} | 0.7131 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 19 | `model.layers.2.mlp.down_proj` | 4358144 | 0.096577 | 0.000000022160 |
| 23 | `model.layers.21.mlp.down_proj` | 4358144 | 0.075291 | 0.000000017276 |
| 28 | `model.layers.3.mlp.down_proj` | 4358144 | 0.061889 | 0.000000014201 |
| 97 | `lm_head` | 136134656 | 0.054824 | 0.000000000403 |
| 29 | `model.layers.23.mlp.down_proj` | 4358144 | 0.039269 | 0.000000009011 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.015716 | 0.000000136882 |
| 42 | `model.layers.22.mlp.down_proj` | 4358144 | 0.013218 | 0.000000003033 |
| 44 | `model.layers.6.mlp.up_proj` | 4358144 | 0.012411 | 0.000000002848 |
| 27 | `model.layers.1.self_attn.o_proj` | 802816 | 0.011736 | 0.000000014618 |
| 2 | `model.layers.12.self_attn.v_proj` | 114816 | 0.011389 | 0.000000099191 |
| 48 | `model.layers.23.mlp.up_proj` | 4358144 | 0.009720 | 0.000000002230 |
| 51 | `model.layers.5.mlp.up_proj` | 4358144 | 0.008712 | 0.000000001999 |
| 3 | `model.layers.10.self_attn.v_proj` | 114816 | 0.008622 | 0.000000075097 |
| 52 | `model.layers.16.mlp.down_proj` | 4358144 | 0.008586 | 0.000000001970 |
| 55 | `model.layers.6.mlp.gate_proj` | 4358144 | 0.008250 | 0.000000001893 |
| 57 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.007896 | 0.000000001812 |
| 4 | `model.layers.21.self_attn.v_proj` | 114816 | 0.007601 | 0.000000066198 |
| 59 | `model.layers.10.mlp.down_proj` | 4358144 | 0.007498 | 0.000000001721 |
| 61 | `model.layers.18.mlp.down_proj` | 4358144 | 0.007242 | 0.000000001662 |
| 62 | `model.layers.14.mlp.up_proj` | 4358144 | 0.007215 | 0.000000001656 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
