# Module Loss Sensitivity Report

Date: `2026-06-16`
Model: `/mnt/e/hf_cache/hub/models--HuggingFaceTB--SmolLM2-360M-Instruct/snapshots/a10cc1512eabd3dde888204e902eca88bddb4951`
Prompts: `8`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `225 / 225`

## Baseline

- FP16 mean NLL: `2.825176`
- FP16 PPL: `16.863910`
- Tokens: `667`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 166, '8': 59} | 0.5347 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 48 | `lm_head` | 47185920 | 0.182144 | 0.000000003860 |
| 2 | `model.layers.3.mlp.down_proj` | 2457600 | 0.072187 | 0.000000029373 |
| 4 | `model.layers.30.mlp.up_proj` | 2457600 | 0.059820 | 0.000000024341 |
| 6 | `model.layers.31.mlp.down_proj` | 2457600 | 0.055462 | 0.000000022567 |
| 20 | `model.layers.31.mlp.up_proj` | 2457600 | 0.027717 | 0.000000011278 |
| 27 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.018938 | 0.000000007706 |
| 33 | `model.layers.2.mlp.gate_proj` | 2457600 | 0.013523 | 0.000000005503 |
| 38 | `model.layers.1.mlp.down_proj` | 2457600 | 0.012048 | 0.000000004902 |
| 43 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.011200 | 0.000000004557 |
| 46 | `model.layers.0.mlp.up_proj` | 2457600 | 0.010776 | 0.000000004385 |
| 1 | `model.layers.0.self_attn.v_proj` | 307200 | 0.010294 | 0.000000033508 |
| 3 | `model.layers.2.self_attn.v_proj` | 307200 | 0.008948 | 0.000000029127 |
| 25 | `model.layers.1.self_attn.q_proj` | 921600 | 0.007386 | 0.000000008014 |
| 58 | `model.layers.21.mlp.up_proj` | 2457600 | 0.007281 | 0.000000002963 |
| 5 | `model.layers.24.self_attn.v_proj` | 307200 | 0.006955 | 0.000000022639 |
| 61 | `model.layers.11.mlp.up_proj` | 2457600 | 0.006356 | 0.000000002586 |
| 62 | `model.layers.24.mlp.gate_proj` | 2457600 | 0.006348 | 0.000000002583 |
| 63 | `model.layers.22.mlp.down_proj` | 2457600 | 0.006139 | 0.000000002498 |
| 7 | `model.layers.13.self_attn.v_proj` | 307200 | 0.006096 | 0.000000019844 |
| 68 | `model.layers.4.mlp.down_proj` | 2457600 | 0.005873 | 0.000000002390 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
