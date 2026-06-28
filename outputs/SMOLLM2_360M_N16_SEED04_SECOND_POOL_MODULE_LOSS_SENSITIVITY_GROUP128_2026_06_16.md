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

- FP16 mean NLL: `2.919769`
- FP16 PPL: `18.537009`
- Tokens: `1399`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 168, '8': 57} | 0.5028 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 40 | `lm_head` | 47185920 | 0.170994 | 0.000000003624 |
| 3 | `model.layers.3.mlp.down_proj` | 2457600 | 0.049431 | 0.000000020114 |
| 4 | `model.layers.31.mlp.down_proj` | 2457600 | 0.043831 | 0.000000017835 |
| 5 | `model.layers.30.mlp.up_proj` | 2457600 | 0.042361 | 0.000000017237 |
| 21 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.019427 | 0.000000007905 |
| 23 | `model.layers.31.mlp.up_proj` | 2457600 | 0.017802 | 0.000000007244 |
| 43 | `model.layers.1.mlp.down_proj` | 2457600 | 0.007618 | 0.000000003100 |
| 45 | `model.layers.2.mlp.up_proj` | 2457600 | 0.006907 | 0.000000002811 |
| 1 | `model.layers.24.self_attn.v_proj` | 307200 | 0.006878 | 0.000000022389 |
| 49 | `model.layers.24.mlp.gate_proj` | 2457600 | 0.006490 | 0.000000002641 |
| 2 | `model.layers.8.self_attn.k_proj` | 307200 | 0.006489 | 0.000000021124 |
| 25 | `model.layers.1.self_attn.q_proj` | 921600 | 0.006463 | 0.000000007013 |
| 52 | `model.layers.22.mlp.down_proj` | 2457600 | 0.005887 | 0.000000002395 |
| 54 | `model.layers.27.mlp.down_proj` | 2457600 | 0.005834 | 0.000000002374 |
| 58 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.005500 | 0.000000002238 |
| 59 | `model.layers.26.mlp.gate_proj` | 2457600 | 0.005301 | 0.000000002157 |
| 29 | `model.layers.12.self_attn.q_proj` | 921600 | 0.005256 | 0.000000005703 |
| 61 | `model.layers.12.mlp.up_proj` | 2457600 | 0.005209 | 0.000000002119 |
| 6 | `model.layers.0.self_attn.v_proj` | 307200 | 0.005174 | 0.000000016842 |
| 66 | `model.layers.8.mlp.gate_proj` | 2457600 | 0.004888 | 0.000000001989 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
