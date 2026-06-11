# Module Loss Sensitivity Report

Date: `2026-06-10`
Model: `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct`
Prompts: `2`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.566064`
- FP16 PPL: `13.014496`
- Tokens: `190`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 197} | 0.0000 |
| loss_sensitive_4to8 | 4.4963 | 0.9992 | {'4': 136, '8': 61} | 0.6322 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 10 | `model.layers.1.mlp.down_proj` | 13762560 | 0.102478 | 0.000000007446 |
| 66 | `lm_head` | 233373696 | 0.099403 | 0.000000000426 |
| 17 | `model.layers.2.mlp.down_proj` | 13762560 | 0.063744 | 0.000000004632 |
| 23 | `model.layers.26.mlp.down_proj` | 13762560 | 0.052637 | 0.000000003825 |
| 38 | `model.layers.27.mlp.up_proj` | 13762560 | 0.013404 | 0.000000000974 |
| 41 | `model.layers.26.mlp.up_proj` | 13762560 | 0.011270 | 0.000000000819 |
| 46 | `model.layers.3.mlp.gate_proj` | 13762560 | 0.009182 | 0.000000000667 |
| 49 | `model.layers.3.mlp.down_proj` | 13762560 | 0.008606 | 0.000000000625 |
| 50 | `model.layers.25.mlp.down_proj` | 13762560 | 0.008569 | 0.000000000623 |
| 28 | `model.layers.16.self_attn.o_proj` | 2359296 | 0.007544 | 0.000000003198 |
| 57 | `model.layers.1.mlp.up_proj` | 13762560 | 0.007007 | 0.000000000509 |
| 58 | `model.layers.23.mlp.down_proj` | 13762560 | 0.006826 | 0.000000000496 |
| 29 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.006565 | 0.000000002783 |
| 61 | `model.layers.22.mlp.down_proj` | 13762560 | 0.006433 | 0.000000000467 |
| 62 | `model.layers.4.mlp.up_proj` | 13762560 | 0.006413 | 0.000000000466 |
| 63 | `model.layers.13.mlp.up_proj` | 13762560 | 0.006318 | 0.000000000459 |
| 64 | `model.layers.24.mlp.up_proj` | 13762560 | 0.006260 | 0.000000000455 |
| 65 | `model.layers.5.mlp.up_proj` | 13762560 | 0.006195 | 0.000000000450 |
| 1 | `model.layers.7.self_attn.v_proj` | 393472 | 0.005659 | 0.000000014382 |
| 67 | `model.layers.3.mlp.up_proj` | 13762560 | 0.005558 | 0.000000000404 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
