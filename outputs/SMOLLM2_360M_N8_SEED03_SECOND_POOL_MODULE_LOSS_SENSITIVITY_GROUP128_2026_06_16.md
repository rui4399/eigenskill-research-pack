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

- FP16 mean NLL: `3.070017`
- FP16 PPL: `21.542260`
- Tokens: `659`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 168, '8': 57} | 0.4680 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 33 | `lm_head` | 47185920 | 0.235097 | 0.000000004982 |
| 7 | `model.layers.31.mlp.down_proj` | 2457600 | 0.051265 | 0.000000020860 |
| 8 | `model.layers.30.mlp.up_proj` | 2457600 | 0.044898 | 0.000000018269 |
| 10 | `model.layers.3.mlp.down_proj` | 2457600 | 0.038929 | 0.000000015840 |
| 24 | `model.layers.31.mlp.up_proj` | 2457600 | 0.016852 | 0.000000006857 |
| 32 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.012667 | 0.000000005154 |
| 35 | `model.layers.0.mlp.up_proj` | 2457600 | 0.010127 | 0.000000004121 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.008858 | 0.000000028836 |
| 42 | `model.layers.27.mlp.down_proj` | 2457600 | 0.008164 | 0.000000003322 |
| 44 | `model.layers.24.mlp.up_proj` | 2457600 | 0.007889 | 0.000000003210 |
| 47 | `model.layers.12.mlp.up_proj` | 2457600 | 0.007573 | 0.000000003081 |
| 2 | `model.layers.3.self_attn.k_proj` | 307200 | 0.007268 | 0.000000023660 |
| 3 | `model.layers.14.self_attn.v_proj` | 307200 | 0.006911 | 0.000000022497 |
| 4 | `model.layers.22.self_attn.v_proj` | 307200 | 0.006904 | 0.000000022473 |
| 22 | `model.layers.12.self_attn.q_proj` | 921600 | 0.006704 | 0.000000007274 |
| 5 | `model.layers.23.self_attn.v_proj` | 307200 | 0.006586 | 0.000000021438 |
| 6 | `model.layers.8.self_attn.k_proj` | 307200 | 0.006560 | 0.000000021354 |
| 26 | `model.layers.2.self_attn.q_proj` | 921600 | 0.005558 | 0.000000006030 |
| 27 | `model.layers.0.self_attn.o_proj` | 921600 | 0.005426 | 0.000000005887 |
| 9 | `model.layers.29.self_attn.v_proj` | 307200 | 0.005042 | 0.000000016412 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
