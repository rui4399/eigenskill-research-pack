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

- FP16 mean NLL: `3.087405`
- FP16 PPL: `21.920121`
- Tokens: `679`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 173, '8': 52} | 0.4776 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 28 | `lm_head` | 47185920 | 0.206098 | 0.000000004368 |
| 8 | `model.layers.31.mlp.down_proj` | 2457600 | 0.039778 | 0.000000016186 |
| 9 | `model.layers.3.mlp.down_proj` | 2457600 | 0.038631 | 0.000000015719 |
| 13 | `model.layers.30.mlp.up_proj` | 2457600 | 0.030819 | 0.000000012540 |
| 25 | `model.layers.31.mlp.up_proj` | 2457600 | 0.012546 | 0.000000005105 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.011517 | 0.000000037489 |
| 2 | `model.layers.23.self_attn.v_proj` | 307200 | 0.009120 | 0.000000029687 |
| 15 | `model.layers.12.self_attn.q_proj` | 921600 | 0.007450 | 0.000000008084 |
| 20 | `model.layers.0.self_attn.o_proj` | 921600 | 0.006621 | 0.000000007185 |
| 42 | `model.layers.24.mlp.up_proj` | 2457600 | 0.006397 | 0.000000002603 |
| 3 | `model.layers.8.self_attn.k_proj` | 307200 | 0.006234 | 0.000000020294 |
| 45 | `model.layers.28.mlp.down_proj` | 2457600 | 0.006166 | 0.000000002509 |
| 4 | `model.layers.14.self_attn.v_proj` | 307200 | 0.005944 | 0.000000019349 |
| 48 | `model.layers.0.mlp.down_proj` | 2457600 | 0.005793 | 0.000000002357 |
| 51 | `model.layers.0.mlp.up_proj` | 2457600 | 0.005522 | 0.000000002247 |
| 52 | `model.layers.24.mlp.gate_proj` | 2457600 | 0.005471 | 0.000000002226 |
| 5 | `model.layers.29.self_attn.v_proj` | 307200 | 0.005430 | 0.000000017674 |
| 6 | `model.layers.27.self_attn.v_proj` | 307200 | 0.005301 | 0.000000017256 |
| 7 | `model.layers.4.self_attn.v_proj` | 307200 | 0.005267 | 0.000000017144 |
| 56 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.004485 | 0.000000001825 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
