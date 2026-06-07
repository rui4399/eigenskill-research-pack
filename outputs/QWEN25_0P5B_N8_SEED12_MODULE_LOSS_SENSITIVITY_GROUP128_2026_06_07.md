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

- FP16 mean NLL: `3.246469`
- FP16 PPL: `25.699440`
- Tokens: `724`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4997 | 0.9999 | {'4': 109, '8': 60} | 0.7019 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 13 | `model.layers.2.mlp.down_proj` | 4358144 | 0.093713 | 0.000000021503 |
| 88 | `lm_head` | 136134656 | 0.082584 | 0.000000000607 |
| 18 | `model.layers.21.mlp.down_proj` | 4358144 | 0.080152 | 0.000000018391 |
| 19 | `model.layers.3.mlp.down_proj` | 4358144 | 0.077404 | 0.000000017761 |
| 30 | `model.layers.23.mlp.down_proj` | 4358144 | 0.036368 | 0.000000008345 |
| 45 | `model.layers.23.mlp.up_proj` | 4358144 | 0.012446 | 0.000000002856 |
| 49 | `model.layers.1.mlp.up_proj` | 4358144 | 0.010717 | 0.000000002459 |
| 1 | `model.layers.16.self_attn.v_proj` | 114816 | 0.010011 | 0.000000087187 |
| 2 | `model.layers.12.self_attn.v_proj` | 114816 | 0.009858 | 0.000000085858 |
| 53 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.008985 | 0.000000002062 |
| 25 | `model.layers.23.self_attn.o_proj` | 802816 | 0.008602 | 0.000000010715 |
| 54 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.008417 | 0.000000001931 |
| 55 | `model.layers.23.mlp.gate_proj` | 4358144 | 0.008246 | 0.000000001892 |
| 57 | `model.layers.22.mlp.down_proj` | 4358144 | 0.007851 | 0.000000001801 |
| 3 | `model.layers.4.self_attn.v_proj` | 114816 | 0.006899 | 0.000000060090 |
| 4 | `model.layers.3.self_attn.v_proj` | 114816 | 0.006584 | 0.000000057340 |
| 60 | `model.layers.15.mlp.up_proj` | 4358144 | 0.006535 | 0.000000001500 |
| 5 | `model.layers.21.self_attn.v_proj` | 114816 | 0.006513 | 0.000000056726 |
| 61 | `model.layers.5.mlp.up_proj` | 4358144 | 0.006237 | 0.000000001431 |
| 6 | `model.layers.10.self_attn.v_proj` | 114816 | 0.006121 | 0.000000053313 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
