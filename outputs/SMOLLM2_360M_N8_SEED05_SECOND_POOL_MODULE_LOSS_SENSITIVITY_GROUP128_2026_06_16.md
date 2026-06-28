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

- FP16 mean NLL: `3.238861`
- FP16 PPL: `25.504659`
- Tokens: `700`

## Allocation Summary

| method | avg bits | budget used | bit histogram | protected positive delta |
|---|---:|---:|---|---:|
| uniform_int4 | 4.0000 | 0.8889 | {'4': 225} | 0.0000 |
| loss_sensitive_4to8 | 4.4993 | 0.9998 | {'4': 175, '8': 50} | 0.5390 |

## Top 20 Sensitive Modules

| rank | module | params | delta NLL | delta NLL / param |
|---:|---|---:|---:|---:|
| 37 | `lm_head` | 47185920 | 0.176795 | 0.000000003747 |
| 2 | `model.layers.31.mlp.down_proj` | 2457600 | 0.064072 | 0.000000026071 |
| 4 | `model.layers.3.mlp.down_proj` | 2457600 | 0.057472 | 0.000000023385 |
| 7 | `model.layers.30.mlp.up_proj` | 2457600 | 0.042409 | 0.000000017256 |
| 10 | `model.layers.31.mlp.up_proj` | 2457600 | 0.036179 | 0.000000014721 |
| 27 | `model.layers.1.mlp.down_proj` | 2457600 | 0.013299 | 0.000000005411 |
| 28 | `model.layers.31.mlp.gate_proj` | 2457600 | 0.012103 | 0.000000004925 |
| 33 | `model.layers.2.mlp.gate_proj` | 2457600 | 0.010490 | 0.000000004268 |
| 1 | `model.layers.7.self_attn.v_proj` | 307200 | 0.009048 | 0.000000029454 |
| 41 | `model.layers.0.mlp.gate_proj` | 2457600 | 0.008087 | 0.000000003291 |
| 42 | `model.layers.24.mlp.gate_proj` | 2457600 | 0.007844 | 0.000000003192 |
| 3 | `model.layers.24.self_attn.v_proj` | 307200 | 0.007780 | 0.000000025324 |
| 22 | `model.layers.12.self_attn.q_proj` | 921600 | 0.006792 | 0.000000007369 |
| 45 | `model.layers.24.mlp.down_proj` | 2457600 | 0.006359 | 0.000000002588 |
| 5 | `model.layers.28.self_attn.v_proj` | 307200 | 0.005947 | 0.000000019358 |
| 46 | `model.layers.28.mlp.down_proj` | 2457600 | 0.005923 | 0.000000002410 |
| 6 | `model.layers.12.self_attn.k_proj` | 307200 | 0.005699 | 0.000000018550 |
| 52 | `model.layers.6.mlp.down_proj` | 2457600 | 0.005436 | 0.000000002212 |
| 8 | `model.layers.14.self_attn.v_proj` | 307200 | 0.005217 | 0.000000016981 |
| 57 | `model.layers.5.mlp.down_proj` | 2457600 | 0.004955 | 0.000000002016 |

## Scope

- This is a per-module fake-quant diagnostic, not a production quantizer.
- It measures short-prompt loss sensitivity and writes an allocation file
  that can be evaluated by `eval_weight_quant_ppl.py`.
- Memory/latency claims still require real compressed storage or a
  quantized runtime.
