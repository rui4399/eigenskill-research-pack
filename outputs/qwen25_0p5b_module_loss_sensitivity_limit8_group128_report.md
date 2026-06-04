# Module Loss Sensitivity Report

Date: `2026-06-04`
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Prompts: `8`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`

## Baseline

- FP16 mean NLL: `2.702166`
- FP16 PPL: `14.911998`
- Tokens: `807`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 169} | 0.0000 |
| loss_sensitive_4to8 | 4.4969 | 0.9993 | {'4': 112, '8': 57} | 0.5901 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 91 | `lm_head` | 136134656 | 0.083164 | 0.000000000611 |
| 12 | `model.layers.2.mlp.down_proj` | 4358144 | 0.082522 | 0.000000018935 |
| 20 | `model.layers.21.mlp.down_proj` | 4358144 | 0.039495 | 0.000000009062 |
| 26 | `model.layers.3.mlp.down_proj` | 4358144 | 0.027064 | 0.000000006210 |
| 30 | `model.layers.23.mlp.down_proj` | 4358144 | 0.018734 | 0.000000004299 |
| 38 | `model.layers.1.mlp.gate_proj` | 4358144 | 0.013034 | 0.000000002991 |
| 1 | `model.layers.3.self_attn.v_proj` | 114816 | 0.012135 | 0.000000105694 |
| 2 | `model.layers.8.self_attn.v_proj` | 114816 | 0.010064 | 0.000000087654 |
| 45 | `model.layers.21.mlp.up_proj` | 4358144 | 0.009473 | 0.000000002174 |
| 47 | `model.layers.16.mlp.up_proj` | 4358144 | 0.008783 | 0.000000002015 |
| 49 | `model.layers.8.mlp.up_proj` | 4358144 | 0.008601 | 0.000000001974 |
| 51 | `model.layers.15.mlp.up_proj` | 4358144 | 0.008537 | 0.000000001959 |
| 52 | `model.layers.5.mlp.gate_proj` | 4358144 | 0.008391 | 0.000000001925 |
| 3 | `model.layers.16.self_attn.v_proj` | 114816 | 0.008378 | 0.000000072965 |
| 53 | `model.layers.20.mlp.gate_proj` | 4358144 | 0.008177 | 0.000000001876 |
| 54 | `model.layers.3.mlp.up_proj` | 4358144 | 0.008151 | 0.000000001870 |
| 55 | `model.layers.2.mlp.up_proj` | 4358144 | 0.007513 | 0.000000001724 |
| 56 | `model.layers.2.mlp.gate_proj` | 4358144 | 0.007304 | 0.000000001676 |
| 58 | `model.layers.22.mlp.up_proj` | 4358144 | 0.006620 | 0.000000001519 |
| 59 | `model.layers.15.mlp.down_proj` | 4358144 | 0.006610 | 0.000000001517 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
