# Module Loss Sensitivity Report

Date: `2026-06-16`
Model: `/mnt/e/hf_cache/hub/models--HuggingFaceTB--SmolLM2-360M-Instruct/snapshots/a10cc1512eabd3dde888204e902eca88bddb4951`
Prompts: `4`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `225 / 225`

## Baseline

- FP16 mean NLL: `2.822713`
- FP16 PPL: `16.822431`
- Tokens: `357`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 170, '8': 55} | 0.4936 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 41 | `lm_head` | 47185920 | 0.193677 | 0.000000004105 |
| 4 | `model.layers.31.mlp.down_proj` | 2457600 | 0.049198 | 0.000000020019 |
| 7 | `model.layers.3.mlp.down_proj` | 2457600 | 0.042812 | 0.000000017420 |
| 13 | `model.layers.30.mlp.up_proj` | 2457600 | 0.036007 | 0.000000014651 |
| 38 | `model.layers.12.mlp.up_proj` | 2457600 | 0.010475 | 0.000000004262 |
| 40 | `model.layers.31.mlp.up_proj` | 2457600 | 0.010297 | 0.000000004190 |
| 1 | `model.layers.0.self_attn.v_proj` | 307200 | 0.008526 | 0.000000027755 |
| 2 | `model.layers.8.self_attn.v_proj` | 307200 | 0.008088 | 0.000000026327 |
| 3 | `model.layers.12.self_attn.k_proj` | 307200 | 0.008018 | 0.000000026101 |
| 23 | `model.layers.1.self_attn.o_proj` | 921600 | 0.007752 | 0.000000008412 |
| 46 | `model.layers.25.mlp.gate_proj` | 2457600 | 0.007552 | 0.000000003073 |
| 47 | `model.layers.6.mlp.up_proj` | 2457600 | 0.007508 | 0.000000003055 |
| 50 | `model.layers.24.mlp.down_proj` | 2457600 | 0.006581 | 0.000000002678 |
| 52 | `model.layers.1.mlp.down_proj` | 2457600 | 0.006293 | 0.000000002561 |
| 30 | `model.layers.13.self_attn.q_proj` | 921600 | 0.006239 | 0.000000006770 |
| 53 | `model.layers.23.mlp.down_proj` | 2457600 | 0.006233 | 0.000000002536 |
| 56 | `model.layers.7.mlp.up_proj` | 2457600 | 0.005972 | 0.000000002430 |
| 57 | `model.layers.9.mlp.up_proj` | 2457600 | 0.005749 | 0.000000002339 |
| 5 | `model.layers.24.self_attn.v_proj` | 307200 | 0.005749 | 0.000000018714 |
| 58 | `model.layers.5.mlp.down_proj` | 2457600 | 0.005666 | 0.000000002306 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
