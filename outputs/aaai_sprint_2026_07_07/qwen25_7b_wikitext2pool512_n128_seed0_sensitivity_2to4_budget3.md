# Module Loss Sensitivity Report

Date: `2026-07-10`
Model: `E:\models\Qwen2.5-7B-Instruct`
Prompts: `128`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.639833`
- FP16 PPL: `14.010862`
- Tokens: `12720`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9977 | 0.9992 | {'2': 101, '4': 96} | 0.9459 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 26 | `lm_head` | 544997376 | 0.076651 | 0.000000000141 |
| 22 | `model.layers.26.mlp.down_proj` | 67895296 | 0.012689 | 0.000000000187 |
| 34 | `model.layers.1.mlp.up_proj` | 67895296 | 0.004852 | 0.000000000071 |
| 35 | `model.layers.27.mlp.gate_proj` | 67895296 | 0.004709 | 0.000000000069 |
| 37 | `model.layers.9.mlp.up_proj` | 67895296 | 0.004660 | 0.000000000069 |
| 1 | `model.layers.27.self_attn.v_proj` | 1835520 | 0.003364 | 0.000000001833 |
| 40 | `model.layers.25.mlp.up_proj` | 67895296 | 0.003230 | 0.000000000048 |
| 42 | `model.layers.26.mlp.up_proj` | 67895296 | 0.003009 | 0.000000000044 |
| 45 | `model.layers.9.mlp.down_proj` | 67895296 | 0.002882 | 0.000000000042 |
| 48 | `model.layers.4.mlp.up_proj` | 67895296 | 0.002690 | 0.000000000040 |
| 50 | `model.layers.10.mlp.up_proj` | 67895296 | 0.002607 | 0.000000000038 |
| 53 | `model.layers.16.mlp.down_proj` | 67895296 | 0.002331 | 0.000000000034 |
| 54 | `model.layers.24.mlp.gate_proj` | 67895296 | 0.002180 | 0.000000000032 |
| 55 | `model.layers.10.mlp.gate_proj` | 67895296 | 0.002133 | 0.000000000031 |
| 58 | `model.layers.8.mlp.down_proj` | 67895296 | 0.001941 | 0.000000000029 |
| 60 | `model.layers.3.mlp.gate_proj` | 67895296 | 0.001776 | 0.000000000026 |
| 61 | `model.layers.22.mlp.up_proj` | 67895296 | 0.001729 | 0.000000000025 |
| 2 | `model.layers.11.self_attn.v_proj` | 1835520 | 0.001720 | 0.000000000937 |
| 3 | `model.layers.5.self_attn.v_proj` | 1835520 | 0.001684 | 0.000000000917 |
| 62 | `model.layers.13.mlp.gate_proj` | 67895296 | 0.001657 | 0.000000000024 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
