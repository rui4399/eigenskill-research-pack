# Module Loss Sensitivity Report

Date: `2026-06-07`
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Prompts: `8`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `169 / 169`

## Baseline

- FP16 mean NLL: `3.259367`
- FP16 PPL: `26.033061`
- Tokens: `690`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 109, '8': 60} | 0.6863 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 16 | `model.layers.2.mlp.down_proj` | 4358144 | 0.103266 | 0.000000023695 |
| 88 | `lm_head` | 136134656 | 0.092872 | 0.000000000682 |
| 19 | `model.layers.21.mlp.down_proj` | 4358144 | 0.091351 | 0.000000020961 |
| 25 | `model.layers.3.mlp.down_proj` | 4358144 | 0.062945 | 0.000000014443 |
| 30 | `model.layers.23.mlp.down_proj` | 4358144 | 0.045342 | 0.000000010404 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.013222 | 0.000000115159 |
| 48 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.010302 | 0.000000002364 |
| 2 | `model.layers.10.self_attn.v_proj` | 114816 | 0.009795 | 0.000000085311 |
| 3 | `model.layers.12.self_attn.v_proj` | 114816 | 0.009457 | 0.000000082365 |
| 50 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.009415 | 0.000000002160 |
| 51 | `model.layers.0.mlp.up_proj` | 4358144 | 0.009389 | 0.000000002154 |
| 54 | `model.layers.23.mlp.up_proj` | 4358144 | 0.008467 | 0.000000001943 |
| 55 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.008395 | 0.000000001926 |
| 56 | `model.layers.15.mlp.up_proj` | 4358144 | 0.008152 | 0.000000001871 |
| 4 | `model.layers.21.self_attn.v_proj` | 114816 | 0.007598 | 0.000000066177 |
| 5 | `model.layers.3.self_attn.v_proj` | 114816 | 0.007483 | 0.000000065171 |
| 59 | `model.layers.22.mlp.down_proj` | 4358144 | 0.007358 | 0.000000001688 |
| 60 | `model.layers.22.mlp.gate_proj` | 4358144 | 0.006858 | 0.000000001574 |
| 61 | `model.layers.1.mlp.up_proj` | 4358144 | 0.006503 | 0.000000001492 |
| 6 | `model.layers.0.self_attn.v_proj` | 114816 | 0.006494 | 0.000000056557 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
