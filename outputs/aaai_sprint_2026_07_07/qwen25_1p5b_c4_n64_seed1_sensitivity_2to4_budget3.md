# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `64`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.944022`
- FP16 PPL: `18.992075`
- Tokens: `7476`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9983 | 0.9994 | {'4': 105, '2': 92} | 0.9373 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 45 | `lm_head` | 233373696 | 0.093779 | 0.000000000402 |
| 4 | `model.layers.1.mlp.down_proj` | 13762560 | 0.064081 | 0.000000004656 |
| 9 | `model.layers.26.mlp.down_proj` | 13762560 | 0.043621 | 0.000000003170 |
| 14 | `model.layers.2.mlp.down_proj` | 13762560 | 0.033769 | 0.000000002454 |
| 30 | `model.layers.26.mlp.up_proj` | 13762560 | 0.011444 | 0.000000000832 |
| 33 | `model.layers.27.mlp.down_proj` | 13762560 | 0.010083 | 0.000000000733 |
| 52 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.003757 | 0.000000000273 |
| 22 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.003502 | 0.000000001485 |
| 54 | `model.layers.26.mlp.gate_proj` | 13762560 | 0.003387 | 0.000000000246 |
| 55 | `model.layers.1.mlp.up_proj` | 13762560 | 0.003352 | 0.000000000244 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.003212 | 0.000000008162 |
| 56 | `model.layers.23.mlp.down_proj` | 13762560 | 0.003126 | 0.000000000227 |
| 57 | `model.layers.22.mlp.up_proj` | 13762560 | 0.002801 | 0.000000000204 |
| 2 | `model.layers.21.self_attn.v_proj` | 393472 | 0.002375 | 0.000000006035 |
| 61 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.002364 | 0.000000000172 |
| 63 | `model.layers.19.mlp.down_proj` | 13762560 | 0.002335 | 0.000000000170 |
| 67 | `model.layers.21.mlp.up_proj` | 13762560 | 0.002131 | 0.000000000155 |
| 3 | `model.layers.11.self_attn.v_proj` | 393472 | 0.002078 | 0.000000005280 |
| 71 | `model.layers.25.mlp.up_proj` | 13762560 | 0.001955 | 0.000000000142 |
| 72 | `model.layers.22.mlp.down_proj` | 13762560 | 0.001929 | 0.000000000140 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
