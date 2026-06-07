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

- FP16 mean NLL: `3.577449`
- FP16 PPL: `35.782137`
- Tokens: `182`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4969 | 0.9993 | {'4': 113, '8': 56} | 0.7480 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 19 | `model.layers.2.mlp.down_proj` | 4358144 | 0.102066 | 0.000000023420 |
| 24 | `model.layers.21.mlp.down_proj` | 4358144 | 0.085218 | 0.000000019554 |
| 33 | `model.layers.23.mlp.down_proj` | 4358144 | 0.054946 | 0.000000012608 |
| 93 | `lm_head` | 136134656 | 0.042439 | 0.000000000312 |
| 36 | `model.layers.3.mlp.down_proj` | 4358144 | 0.033346 | 0.000000007651 |
| 44 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.016906 | 0.000000003879 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.015493 | 0.000000134941 |
| 2 | `model.layers.12.self_attn.v_proj` | 114816 | 0.012868 | 0.000000112077 |
| 3 | `model.layers.8.self_attn.v_proj` | 114816 | 0.012615 | 0.000000109873 |
| 46 | `model.layers.0.mlp.up_proj` | 4358144 | 0.012200 | 0.000000002799 |
| 47 | `model.layers.22.mlp.up_proj` | 4358144 | 0.011919 | 0.000000002735 |
| 4 | `model.layers.0.self_attn.v_proj` | 114816 | 0.011894 | 0.000000103592 |
| 32 | `model.layers.0.self_attn.o_proj` | 802816 | 0.011579 | 0.000000014423 |
| 50 | `model.layers.13.mlp.up_proj` | 4358144 | 0.010052 | 0.000000002306 |
| 5 | `model.layers.4.self_attn.v_proj` | 114816 | 0.009898 | 0.000000086212 |
| 51 | `model.layers.11.mlp.up_proj` | 4358144 | 0.009829 | 0.000000002255 |
| 54 | `model.layers.1.mlp.down_proj` | 4358144 | 0.009353 | 0.000000002146 |
| 55 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.008134 | 0.000000001866 |
| 56 | `model.layers.21.mlp.up_proj` | 4358144 | 0.008039 | 0.000000001844 |
| 57 | `model.layers.2.mlp.up_proj` | 4358144 | 0.007815 | 0.000000001793 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
