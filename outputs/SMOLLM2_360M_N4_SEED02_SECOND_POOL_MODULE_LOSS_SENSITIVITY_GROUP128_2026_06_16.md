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

- FP16 mean NLL: `3.536049`
- FP16 PPL: `34.331001`
- Tokens: `336`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 170, '8': 55} | 0.4426 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 38 | `lm_head` | 47185920 | 0.273283 | 0.000000005792 |
| 12 | `model.layers.30.mlp.up_proj` | 2457600 | 0.040749 | 0.000000016581 |
| 15 | `model.layers.3.mlp.down_proj` | 2457600 | 0.037401 | 0.000000015219 |
| 16 | `model.layers.31.mlp.down_proj` | 2457600 | 0.035791 | 0.000000014563 |
| 27 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.021864 | 0.000000008897 |
| 39 | `model.layers.1.mlp.down_proj` | 2457600 | 0.014210 | 0.000000005782 |
| 41 | `model.layers.27.mlp.down_proj` | 2457600 | 0.014096 | 0.000000005736 |
| 46 | `model.layers.2.mlp.down_proj` | 2457600 | 0.011138 | 0.000000004532 |
| 1 | `model.layers.7.self_attn.v_proj` | 307200 | 0.010720 | 0.000000034897 |
| 49 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.009685 | 0.000000003941 |
| 2 | `model.layers.14.self_attn.v_proj` | 307200 | 0.009382 | 0.000000030540 |
| 51 | `model.layers.30.mlp.gate_proj` | 2457600 | 0.009290 | 0.000000003780 |
| 54 | `model.layers.3.mlp.up_proj` | 2457600 | 0.008631 | 0.000000003512 |
| 26 | `model.layers.12.self_attn.q_proj` | 921600 | 0.008265 | 0.000000008968 |
| 61 | `model.layers.28.mlp.gate_proj` | 2457600 | 0.007669 | 0.000000003121 |
| 63 | `model.layers.31.mlp.up_proj` | 2457600 | 0.007410 | 0.000000003015 |
| 33 | `model.layers.8.self_attn.o_proj` | 921600 | 0.006999 | 0.000000007594 |
| 3 | `model.layers.23.self_attn.v_proj` | 307200 | 0.006947 | 0.000000022614 |
| 4 | `model.layers.8.self_attn.k_proj` | 307200 | 0.006852 | 0.000000022306 |
| 34 | `model.layers.7.self_attn.q_proj` | 921600 | 0.006845 | 0.000000007428 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
