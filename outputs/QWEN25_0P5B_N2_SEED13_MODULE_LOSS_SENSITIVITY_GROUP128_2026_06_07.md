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

- FP16 mean NLL: `3.273919`
- FP16 PPL: `26.414651`
- Tokens: `162`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4969 | 0.9993 | {'4': 112, '8': 57} | 0.6509 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 71 | `lm_head` | 136134656 | 0.141042 | 0.000000001036 |
| 19 | `model.layers.3.mlp.down_proj` | 4358144 | 0.087124 | 0.000000019991 |
| 21 | `model.layers.2.mlp.down_proj` | 4358144 | 0.085919 | 0.000000019715 |
| 23 | `model.layers.21.mlp.down_proj` | 4358144 | 0.073575 | 0.000000016882 |
| 36 | `model.layers.23.mlp.down_proj` | 4358144 | 0.026017 | 0.000000005970 |
| 42 | `model.layers.23.mlp.up_proj` | 4358144 | 0.019448 | 0.000000004462 |
| 43 | `model.layers.22.mlp.gate_proj` | 4358144 | 0.014994 | 0.000000003440 |
| 46 | `model.layers.20.mlp.down_proj` | 4358144 | 0.013838 | 0.000000003175 |
| 48 | `model.layers.19.mlp.gate_proj` | 4358144 | 0.012296 | 0.000000002821 |
| 1 | `model.layers.5.self_attn.v_proj` | 114816 | 0.012114 | 0.000000105511 |
| 52 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.011712 | 0.000000002687 |
| 53 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.011680 | 0.000000002680 |
| 2 | `model.layers.8.self_attn.v_proj` | 114816 | 0.010965 | 0.000000095504 |
| 3 | `model.layers.21.self_attn.v_proj` | 114816 | 0.010275 | 0.000000089492 |
| 55 | `model.layers.14.mlp.up_proj` | 4358144 | 0.009841 | 0.000000002258 |
| 4 | `model.layers.7.self_attn.v_proj` | 114816 | 0.009509 | 0.000000082823 |
| 5 | `model.layers.12.self_attn.v_proj` | 114816 | 0.009474 | 0.000000082519 |
| 57 | `model.layers.1.mlp.up_proj` | 4358144 | 0.009213 | 0.000000002114 |
| 58 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.008894 | 0.000000002041 |
| 6 | `model.layers.10.self_attn.v_proj` | 114816 | 0.008888 | 0.000000077414 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
