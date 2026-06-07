# Module Loss Sensitivity Report

Date: `2026-06-07`
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Prompts: `2`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `169 / 169`

## Baseline

- FP16 mean NLL: `3.859176`
- FP16 PPL: `47.426264`
- Tokens: `190`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 116, '8': 53} | 0.5839 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 66 | `lm_head` | 136134656 | 0.183937 | 0.000000001351 |
| 20 | `model.layers.21.mlp.down_proj` | 4358144 | 0.081789 | 0.000000018767 |
| 23 | `model.layers.2.mlp.down_proj` | 4358144 | 0.054861 | 0.000000012588 |
| 26 | `model.layers.3.mlp.down_proj` | 4358144 | 0.034420 | 0.000000007898 |
| 1 | `model.layers.0.self_attn.v_proj` | 114816 | 0.021723 | 0.000000189194 |
| 34 | `model.layers.1.mlp.up_proj` | 4358144 | 0.020314 | 0.000000004661 |
| 37 | `model.layers.23.mlp.down_proj` | 4358144 | 0.019519 | 0.000000004479 |
| 38 | `model.layers.23.mlp.up_proj` | 4358144 | 0.018032 | 0.000000004137 |
| 19 | `model.layers.23.self_attn.o_proj` | 802816 | 0.017085 | 0.000000021282 |
| 41 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.015020 | 0.000000003446 |
| 43 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.014444 | 0.000000003314 |
| 46 | `model.layers.19.mlp.gate_proj` | 4358144 | 0.012588 | 0.000000002888 |
| 2 | `model.layers.15.self_attn.v_proj` | 114816 | 0.012064 | 0.000000105068 |
| 49 | `model.layers.7.mlp.up_proj` | 4358144 | 0.009910 | 0.000000002274 |
| 52 | `model.layers.1.mlp.down_proj` | 4358144 | 0.009194 | 0.000000002110 |
| 53 | `model.layers.8.mlp.up_proj` | 4358144 | 0.008992 | 0.000000002063 |
| 3 | `model.layers.21.self_attn.v_proj` | 114816 | 0.008779 | 0.000000076463 |
| 55 | `model.layers.14.mlp.gate_proj` | 4358144 | 0.008731 | 0.000000002003 |
| 25 | `model.layers.22.self_attn.o_proj` | 802816 | 0.008729 | 0.000000010873 |
| 4 | `model.layers.6.self_attn.v_proj` | 114816 | 0.008725 | 0.000000075995 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
