# Module Loss Sensitivity Report

Date: `2026-07-08`
Model: `E:\models\Qwen2.5-1.5B-Instruct`
Prompts: `128`
Max length: `128`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `197 / 197`

## Baseline

- FP16 mean NLL: `2.574822`
- FP16 PPL: `13.128980`
- Tokens: `14234`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int2 | 2.0000 | 0.6667 | {'2': 197} | 0.0000 |
| loss_sensitive_4to8 | 2.9994 | 0.9998 | {'2': 95, '4': 102} | 0.9260 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 52 | `lm_head` | 233373696 | 0.089405 | 0.000000000383 |
| 3 | `model.layers.1.mlp.down_proj` | 13762560 | 0.055863 | 0.000000004059 |
| 14 | `model.layers.2.mlp.down_proj` | 13762560 | 0.034037 | 0.000000002473 |
| 17 | `model.layers.26.mlp.down_proj` | 13762560 | 0.030078 | 0.000000002186 |
| 34 | `model.layers.27.mlp.down_proj` | 13762560 | 0.011040 | 0.000000000802 |
| 46 | `model.layers.27.mlp.up_proj` | 13762560 | 0.006355 | 0.000000000462 |
| 1 | `model.layers.0.self_attn.v_proj` | 393472 | 0.006237 | 0.000000015851 |
| 47 | `model.layers.26.mlp.up_proj` | 13762560 | 0.006071 | 0.000000000441 |
| 57 | `model.layers.27.mlp.gate_proj` | 13762560 | 0.004617 | 0.000000000335 |
| 60 | `model.layers.1.mlp.up_proj` | 13762560 | 0.004398 | 0.000000000320 |
| 61 | `model.layers.3.mlp.up_proj` | 13762560 | 0.004380 | 0.000000000318 |
| 64 | `model.layers.2.mlp.gate_proj` | 13762560 | 0.003743 | 0.000000000272 |
| 66 | `model.layers.3.mlp.down_proj` | 13762560 | 0.003161 | 0.000000000230 |
| 23 | `model.layers.1.self_attn.o_proj` | 2359296 | 0.003074 | 0.000000001303 |
| 68 | `model.layers.9.mlp.up_proj` | 13762560 | 0.002900 | 0.000000000211 |
| 69 | `model.layers.23.mlp.gate_proj` | 13762560 | 0.002873 | 0.000000000209 |
| 27 | `model.layers.0.self_attn.o_proj` | 2359296 | 0.002686 | 0.000000001138 |
| 75 | `model.layers.23.mlp.up_proj` | 13762560 | 0.002397 | 0.000000000174 |
| 76 | `model.layers.11.mlp.down_proj` | 13762560 | 0.002330 | 0.000000000169 |
| 78 | `model.layers.22.mlp.down_proj` | 13762560 | 0.002244 | 0.000000000163 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
