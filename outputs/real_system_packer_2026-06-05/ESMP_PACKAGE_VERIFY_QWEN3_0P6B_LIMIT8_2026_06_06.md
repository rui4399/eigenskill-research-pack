# ESMP Package Verification

Date: `2026-06-06T10:44:52+00:00`
Status: **PASS**
Summary: `outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json`
Model: `Qwen/Qwen3-0.6B`
Method: `loss_sensitive_budget`

## Aggregate

- checked modules: `8 / 8`
- missing files: `0`
- failed modules: `0`
- checked compression vs FP32: `6.279659x`

## Module Checks

| module | status | shape | avg bits | compression | notes |
|---|---:|---:|---:|---:|---|
| `model.layers.0.self_attn.q_proj` | **PASS** | 2048x1024 | 4.0000 | 7.6413x | ok |
| `model.layers.0.self_attn.k_proj` | **PASS** | 1024x1024 | 4.0000 | 7.6409x | ok |
| `model.layers.0.self_attn.v_proj` | **PASS** | 1024x1024 | 8.0000 | 3.9082x | ok |
| `model.layers.0.self_attn.o_proj` | **PASS** | 1024x2048 | 4.0000 | 7.8163x | ok |
| `model.layers.0.mlp.gate_proj` | **PASS** | 3072x1024 | 4.0000 | 7.6415x | ok |
| `model.layers.0.mlp.up_proj` | **PASS** | 3072x1024 | 4.0000 | 7.6415x | ok |
| `model.layers.0.mlp.down_proj` | **PASS** | 1024x3072 | 8.0000 | 3.9689x | ok |
| `model.layers.1.self_attn.q_proj` | **PASS** | 2048x1024 | 4.0000 | 7.6413x | ok |

## Failures

- none
