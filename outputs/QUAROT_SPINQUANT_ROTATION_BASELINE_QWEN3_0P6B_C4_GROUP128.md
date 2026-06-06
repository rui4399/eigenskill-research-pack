# Rotation Family Baseline Proxy

Date: `2026-06-06T14:04:52+00:00`
Method: `quarot_spinquant_style_rotation_baseline_proxy`
Source: `outputs\qwen3_0p6b_c4_module_loss_sensitivity_limit4_group128.json`
Model: `Qwen/Qwen3-0.6B`
Records: `197`
Rotated modules: `85`
Rotated cost fraction: `0.348362`
Projected sensitivity reduction: `0.101966`

## Policy Histogram

| policy | count |
|---|---:|
| `none` | 112 |
| `quarot_static_hadamard_proxy` | 25 |
| `spinquant_learned_rotation_proxy` | 60 |

## Top Rotated Modules

| module | role | policy | sensitivity | projected reduction |
|---|---|---|---:|---:|
| `model.layers.0.self_attn.v_proj` | `v_proj` | `spinquant_learned_rotation_proxy` | 0.02503186 | 0.00550701 |
| `model.layers.2.mlp.down_proj` | `down_proj` | `spinquant_learned_rotation_proxy` | 0.02743238 | 0.00493783 |
| `model.layers.2.self_attn.v_proj` | `v_proj` | `spinquant_learned_rotation_proxy` | 0.01381147 | 0.00303852 |
| `model.layers.4.mlp.gate_proj` | `gate_proj` | `spinquant_learned_rotation_proxy` | 0.01020235 | 0.00183642 |
| `model.layers.3.mlp.gate_proj` | `gate_proj` | `spinquant_learned_rotation_proxy` | 0.00849330 | 0.00152879 |
| `model.layers.11.self_attn.k_proj` | `k_proj` | `spinquant_learned_rotation_proxy` | 0.00687188 | 0.00151181 |
| `model.layers.7.mlp.up_proj` | `up_proj` | `spinquant_learned_rotation_proxy` | 0.00826490 | 0.00148768 |
| `model.layers.3.mlp.up_proj` | `up_proj` | `spinquant_learned_rotation_proxy` | 0.00787938 | 0.00141829 |
| `model.layers.7.mlp.gate_proj` | `gate_proj` | `spinquant_learned_rotation_proxy` | 0.00782174 | 0.00140791 |
| `model.layers.5.mlp.gate_proj` | `gate_proj` | `spinquant_learned_rotation_proxy` | 0.00760359 | 0.00136865 |
| `model.layers.3.self_attn.q_proj` | `q_proj` | `spinquant_learned_rotation_proxy` | 0.00569373 | 0.00125262 |
| `model.layers.1.mlp.gate_proj` | `gate_proj` | `spinquant_learned_rotation_proxy` | 0.00667763 | 0.00120197 |

## Claim Boundary

- Valid claim: this is an executable QuaRot/SpinQuant-style rotation/outlier-mitigation proxy over measured module sensitivity records. Invalid claim: this is a faithful official QuaRot or SpinQuant implementation, an activation-rotation kernel, or a quality-retention proof.
