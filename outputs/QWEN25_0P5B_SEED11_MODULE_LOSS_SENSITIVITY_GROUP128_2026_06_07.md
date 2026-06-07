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

- FP16 mean NLL: `3.268824`
- FP16 PPL: `26.280417`
- Tokens: `344`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4960 | 0.9991 | {'4': 107, '8': 62} | 0.7503 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 18 | `model.layers.2.mlp.down_proj` | 4358144 | 0.093029 | 0.000000021346 |
| 22 | `model.layers.21.mlp.down_proj` | 4358144 | 0.079950 | 0.000000018345 |
| 28 | `model.layers.3.mlp.down_proj` | 4358144 | 0.065185 | 0.000000014957 |
| 32 | `model.layers.23.mlp.down_proj` | 4358144 | 0.045576 | 0.000000010458 |
| 98 | `lm_head` | 136134656 | 0.044715 | 0.000000000328 |
| 41 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.017564 | 0.000000004030 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.015989 | 0.000000139259 |
| 2 | `model.layers.12.self_attn.v_proj` | 114816 | 0.011596 | 0.000000101000 |
| 3 | `model.layers.8.self_attn.v_proj` | 114816 | 0.011096 | 0.000000096643 |
| 50 | `model.layers.13.mlp.up_proj` | 4358144 | 0.009710 | 0.000000002228 |
| 51 | `model.layers.0.mlp.up_proj` | 4358144 | 0.009580 | 0.000000002198 |
| 53 | `model.layers.21.mlp.up_proj` | 4358144 | 0.009147 | 0.000000002099 |
| 4 | `model.layers.3.self_attn.v_proj` | 114816 | 0.009118 | 0.000000079411 |
| 55 | `model.layers.1.mlp.up_proj` | 4358144 | 0.008841 | 0.000000002029 |
| 5 | `model.layers.21.self_attn.v_proj` | 114816 | 0.008418 | 0.000000073318 |
| 59 | `model.layers.22.mlp.up_proj` | 4358144 | 0.007581 | 0.000000001739 |
| 33 | `model.layers.12.self_attn.o_proj` | 802816 | 0.007233 | 0.000000009010 |
| 61 | `model.layers.15.mlp.up_proj` | 4358144 | 0.007080 | 0.000000001625 |
| 6 | `model.layers.10.self_attn.v_proj` | 114816 | 0.007022 | 0.000000061161 |
| 62 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.006921 | 0.000000001588 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
