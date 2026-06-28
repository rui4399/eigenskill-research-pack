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

- FP16 mean NLL: `2.377819`
- FP16 PPL: `10.781362`
- Tokens: `323`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 168, '8': 57} | 0.4784 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 36 | `lm_head` | 47185920 | 0.192659 | 0.000000004083 |
| 5 | `model.layers.30.mlp.up_proj` | 2457600 | 0.052309 | 0.000000021285 |
| 7 | `model.layers.3.mlp.down_proj` | 2457600 | 0.037788 | 0.000000015376 |
| 11 | `model.layers.31.mlp.down_proj` | 2457600 | 0.026563 | 0.000000010809 |
| 8 | `model.layers.0.self_attn.o_proj` | 921600 | 0.012882 | 0.000000013978 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.011034 | 0.000000035918 |
| 2 | `model.layers.23.self_attn.v_proj` | 307200 | 0.009336 | 0.000000030389 |
| 3 | `model.layers.22.self_attn.v_proj` | 307200 | 0.009095 | 0.000000029606 |
| 39 | `model.layers.12.mlp.up_proj` | 2457600 | 0.008425 | 0.000000003428 |
| 4 | `model.layers.27.self_attn.v_proj` | 307200 | 0.007165 | 0.000000023324 |
| 41 | `model.layers.13.mlp.down_proj` | 2457600 | 0.007111 | 0.000000002894 |
| 18 | `model.layers.18.self_attn.o_proj` | 921600 | 0.006982 | 0.000000007576 |
| 46 | `model.layers.31.mlp.up_proj` | 2457600 | 0.006481 | 0.000000002637 |
| 48 | `model.layers.23.mlp.down_proj` | 2457600 | 0.006434 | 0.000000002618 |
| 52 | `model.layers.20.mlp.up_proj` | 2457600 | 0.005956 | 0.000000002424 |
| 57 | `model.layers.1.mlp.gate_proj` | 2457600 | 0.005792 | 0.000000002357 |
| 59 | `model.layers.11.mlp.gate_proj` | 2457600 | 0.005776 | 0.000000002350 |
| 60 | `model.layers.24.mlp.up_proj` | 2457600 | 0.005625 | 0.000000002289 |
| 61 | `model.layers.4.mlp.down_proj` | 2457600 | 0.005536 | 0.000000002253 |
| 25 | `model.layers.13.self_attn.q_proj` | 921600 | 0.005489 | 0.000000005956 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
