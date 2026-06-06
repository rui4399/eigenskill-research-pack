# Rotation Family Baseline Proxy

Date: `2026-06-06T14:04:52+00:00`
Method: `quarot_spinquant_style_rotation_baseline_proxy`
Source: `outputs\qwen3_0p6b_module_loss_sensitivity_limit4_group128.json`
Model: `Qwen/Qwen3-0.6B`
Records: `197`
Rotated modules: `82`
Rotated cost fraction: `0.348362`
Projected sensitivity reduction: `0.084759`

## Policy Histogram

| policy | count |
|---|---:|
| `none` | 115 |
| `quarot_static_hadamard_proxy` | 24 |
| `spinquant_learned_rotation_proxy` | 58 |

## Top Rotated Modules

| module | role | policy | sensitivity | projected reduction |
|---|---|---|---:|---:|
| `model.layers.1.mlp.gate_proj` | `gate_proj` | `spinquant_learned_rotation_proxy` | 0.04511980 | 0.00812156 |
| `model.layers.2.mlp.up_proj` | `up_proj` | `spinquant_learned_rotation_proxy` | 0.03363195 | 0.00605375 |
| `model.layers.0.mlp.up_proj` | `up_proj` | `spinquant_learned_rotation_proxy` | 0.02386099 | 0.00429498 |
| `model.layers.4.self_attn.v_proj` | `v_proj` | `spinquant_learned_rotation_proxy` | 0.01902712 | 0.00418597 |
| `model.layers.10.self_attn.k_proj` | `k_proj` | `spinquant_learned_rotation_proxy` | 0.01639271 | 0.00360640 |
| `model.layers.3.mlp.up_proj` | `up_proj` | `spinquant_learned_rotation_proxy` | 0.01731652 | 0.00311697 |
| `model.layers.16.self_attn.v_proj` | `v_proj` | `spinquant_learned_rotation_proxy` | 0.01262097 | 0.00277661 |
| `model.layers.11.self_attn.o_proj` | `o_proj` | `quarot_static_hadamard_proxy` | 0.01507292 | 0.00241167 |
| `model.layers.1.self_attn.v_proj` | `v_proj` | `spinquant_learned_rotation_proxy` | 0.01031167 | 0.00226857 |
| `model.layers.2.self_attn.o_proj` | `o_proj` | `quarot_static_hadamard_proxy` | 0.01371866 | 0.00219499 |
| `model.layers.14.self_attn.q_proj` | `q_proj` | `spinquant_learned_rotation_proxy` | 0.00991602 | 0.00218153 |
| `model.layers.6.self_attn.q_proj` | `q_proj` | `spinquant_learned_rotation_proxy` | 0.00870468 | 0.00191503 |

## Claim Boundary

- Valid claim: this is an executable QuaRot/SpinQuant-style rotation/outlier-mitigation proxy over measured module sensitivity records. Invalid claim: this is a faithful official QuaRot or SpinQuant implementation, an activation-rotation kernel, or a quality-retention proof.
