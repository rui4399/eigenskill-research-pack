# Module Loss Sensitivity Report

Date: `2026-06-28`
Model: `/mnt/e/hf_cache/hub/models--HuggingFaceTB--SmolLM2-360M-Instruct/snapshots/a10cc1512eabd3dde888204e902eca88bddb4951`
Prompts: `8`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `225 / 225`

## Baseline

- FP16 mean NLL: `3.169985`
- FP16 PPL: `23.807136`
- Tokens: `728`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 164, '8': 61} | 0.5446 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 49 | `lm_head` | 47185920 | 0.148243 | 0.000000003142 |
| 2 | `model.layers.31.mlp.down_proj` | 2457600 | 0.075244 | 0.000000030617 |
| 7 | `model.layers.3.mlp.down_proj` | 2457600 | 0.044632 | 0.000000018161 |
| 11 | `model.layers.30.mlp.up_proj` | 2457600 | 0.038416 | 0.000000015631 |
| 23 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.022228 | 0.000000009045 |
| 25 | `model.layers.31.mlp.up_proj` | 2457600 | 0.019742 | 0.000000008033 |
| 1 | `model.layers.1.self_attn.v_proj` | 307200 | 0.012553 | 0.000000040862 |
| 39 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.010776 | 0.000000004385 |
| 26 | `model.layers.1.self_attn.q_proj` | 921600 | 0.007220 | 0.000000007834 |
| 56 | `model.layers.8.mlp.gate_proj` | 2457600 | 0.007008 | 0.000000002852 |
| 57 | `model.layers.22.mlp.down_proj` | 2457600 | 0.006999 | 0.000000002848 |
| 3 | `model.layers.5.self_attn.v_proj` | 307200 | 0.006778 | 0.000000022064 |
| 4 | `model.layers.1.self_attn.k_proj` | 307200 | 0.006727 | 0.000000021897 |
| 5 | `model.layers.3.self_attn.k_proj` | 307200 | 0.006352 | 0.000000020677 |
| 62 | `model.layers.26.mlp.gate_proj` | 2457600 | 0.006166 | 0.000000002509 |
| 6 | `model.layers.24.self_attn.v_proj` | 307200 | 0.006062 | 0.000000019734 |
| 63 | `model.layers.27.mlp.down_proj` | 2457600 | 0.005924 | 0.000000002411 |
| 33 | `model.layers.12.self_attn.q_proj` | 921600 | 0.005828 | 0.000000006324 |
| 8 | `model.layers.11.self_attn.v_proj` | 307200 | 0.005480 | 0.000000017840 |
| 68 | `model.layers.10.mlp.gate_proj` | 2457600 | 0.005159 | 0.000000002099 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
