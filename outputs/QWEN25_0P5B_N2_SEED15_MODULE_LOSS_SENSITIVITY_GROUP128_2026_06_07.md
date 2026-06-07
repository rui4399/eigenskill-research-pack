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

- FP16 mean NLL: `3.188858`
- FP16 PPL: `24.260707`
- Tokens: `162`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 110, '8': 59} | 0.7303 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 19 | `model.layers.2.mlp.down_proj` | 4358144 | 0.127200 | 0.000000029187 |
| 24 | `model.layers.3.mlp.down_proj` | 4358144 | 0.103785 | 0.000000023814 |
| 32 | `model.layers.21.mlp.down_proj` | 4358144 | 0.066005 | 0.000000015145 |
| 98 | `lm_head` | 136134656 | 0.054448 | 0.000000000400 |
| 38 | `model.layers.23.mlp.down_proj` | 4358144 | 0.028914 | 0.000000006634 |
| 27 | `model.layers.1.self_attn.o_proj` | 802816 | 0.015205 | 0.000000018940 |
| 45 | `model.layers.19.mlp.up_proj` | 4358144 | 0.015076 | 0.000000003459 |
| 1 | `model.layers.12.self_attn.v_proj` | 114816 | 0.013676 | 0.000000119116 |
| 52 | `model.layers.20.mlp.down_proj` | 4358144 | 0.013273 | 0.000000003046 |
| 53 | `model.layers.16.mlp.up_proj` | 4358144 | 0.013219 | 0.000000003033 |
| 54 | `model.layers.16.mlp.down_proj` | 4358144 | 0.012528 | 0.000000002875 |
| 56 | `model.layers.10.mlp.down_proj` | 4358144 | 0.012205 | 0.000000002800 |
| 57 | `model.layers.22.mlp.down_proj` | 4358144 | 0.011996 | 0.000000002753 |
| 58 | `model.layers.23.mlp.up_proj` | 4358144 | 0.011711 | 0.000000002687 |
| 59 | `model.layers.14.mlp.up_proj` | 4358144 | 0.011258 | 0.000000002583 |
| 63 | `model.layers.21.mlp.up_proj` | 4358144 | 0.010573 | 0.000000002426 |
| 64 | `model.layers.15.mlp.up_proj` | 4358144 | 0.010557 | 0.000000002422 |
| 65 | `model.layers.1.mlp.up_proj` | 4358144 | 0.010225 | 0.000000002346 |
| 2 | `model.layers.16.self_attn.v_proj` | 114816 | 0.009719 | 0.000000084650 |
| 3 | `model.layers.21.self_attn.v_proj` | 114816 | 0.009053 | 0.000000078845 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
