# Module Loss Sensitivity Report

Date: `2026-06-28`
Model: `/mnt/e/hf_cache/hub/models--HuggingFaceTB--SmolLM2-360M-Instruct/snapshots/a10cc1512eabd3dde888204e902eca88bddb4951`
Prompts: `16`
Max length: `96`
Quantized bits during probing: `4`
Group size: `128`
Status: `complete`
Measured modules: `225 / 225`

## Baseline

- FP16 mean NLL: `2.909208`
- FP16 PPL: `18.342273`
- Tokens: `1437`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 165, '8': 60} | 0.4942 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 38 | `lm_head` | 47185920 | 0.178012 | 0.000000003773 |
| 3 | `model.layers.31.mlp.down_proj` | 2457600 | 0.052999 | 0.000000021566 |
| 5 | `model.layers.30.mlp.up_proj` | 2457600 | 0.044204 | 0.000000017987 |
| 7 | `model.layers.3.mlp.down_proj` | 2457600 | 0.041568 | 0.000000016914 |
| 17 | `model.layers.31.mlp.up_proj` | 2457600 | 0.018985 | 0.000000007725 |
| 24 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.014304 | 0.000000005820 |
| 42 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.008197 | 0.000000003335 |
| 43 | `model.layers.1.mlp.down_proj` | 2457600 | 0.007648 | 0.000000003112 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.007512 | 0.000000024454 |
| 2 | `model.layers.0.self_attn.v_proj` | 307200 | 0.007215 | 0.000000023486 |
| 19 | `model.layers.12.self_attn.q_proj` | 921600 | 0.006369 | 0.000000006911 |
| 4 | `model.layers.2.self_attn.v_proj` | 307200 | 0.005587 | 0.000000018188 |
| 6 | `model.layers.14.self_attn.v_proj` | 307200 | 0.005396 | 0.000000017565 |
| 55 | `model.layers.2.mlp.gate_proj` | 2457600 | 0.005107 | 0.000000002078 |
| 56 | `model.layers.29.mlp.down_proj` | 2457600 | 0.005013 | 0.000000002040 |
| 58 | `model.layers.8.mlp.gate_proj` | 2457600 | 0.004783 | 0.000000001946 |
| 59 | `model.layers.26.mlp.gate_proj` | 2457600 | 0.004663 | 0.000000001898 |
| 8 | `model.layers.23.self_attn.v_proj` | 307200 | 0.004334 | 0.000000014107 |
| 63 | `model.layers.29.mlp.up_proj` | 2457600 | 0.004168 | 0.000000001696 |
| 9 | `model.layers.27.self_attn.v_proj` | 307200 | 0.004094 | 0.000000013325 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
