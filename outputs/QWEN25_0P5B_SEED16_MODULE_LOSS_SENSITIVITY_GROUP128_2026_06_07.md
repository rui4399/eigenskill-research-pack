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

- FP16 mean NLL: `3.339700`
- FP16 PPL: `28.210668`
- Tokens: `307`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 110, '8': 59} | 0.6974 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 19 | `model.layers.2.mlp.down_proj` | 4358144 | 0.116108 | 0.000000026642 |
| 87 | `lm_head` | 136134656 | 0.091345 | 0.000000000671 |
| 24 | `model.layers.3.mlp.down_proj` | 4358144 | 0.077611 | 0.000000017808 |
| 25 | `model.layers.21.mlp.down_proj` | 4358144 | 0.077467 | 0.000000017775 |
| 30 | `model.layers.23.mlp.down_proj` | 4358144 | 0.048193 | 0.000000011058 |
| 44 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.014286 | 0.000000003278 |
| 1 | `model.layers.12.self_attn.v_proj` | 114816 | 0.011936 | 0.000000103955 |
| 48 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.011239 | 0.000000002579 |
| 2 | `model.layers.4.self_attn.v_proj` | 114816 | 0.010617 | 0.000000092470 |
| 3 | `model.layers.8.self_attn.v_proj` | 114816 | 0.010532 | 0.000000091731 |
| 51 | `model.layers.14.mlp.up_proj` | 4358144 | 0.010104 | 0.000000002318 |
| 52 | `model.layers.22.mlp.gate_proj` | 4358144 | 0.009650 | 0.000000002214 |
| 53 | `model.layers.1.mlp.down_proj` | 4358144 | 0.009632 | 0.000000002210 |
| 54 | `model.layers.22.mlp.down_proj` | 4358144 | 0.009509 | 0.000000002182 |
| 55 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.009268 | 0.000000002127 |
| 57 | `model.layers.20.mlp.down_proj` | 4358144 | 0.008463 | 0.000000001942 |
| 58 | `model.layers.7.mlp.up_proj` | 4358144 | 0.008038 | 0.000000001844 |
| 59 | `model.layers.2.mlp.up_proj` | 4358144 | 0.007665 | 0.000000001759 |
| 32 | `model.layers.0.self_attn.o_proj` | 802816 | 0.007622 | 0.000000009494 |
| 60 | `model.layers.19.mlp.gate_proj` | 4358144 | 0.007583 | 0.000000001740 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
