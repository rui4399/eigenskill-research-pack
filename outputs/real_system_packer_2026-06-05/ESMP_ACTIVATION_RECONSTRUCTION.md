# ESMP Activation Reconstruction Report

Date: `2026-06-06`
Model: `Qwen/Qwen3-0.6B`
Package summary: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json`
Prompts: `4`
Max length: `96`
Sample rows per module: `64`
Device: `cuda`

## Aggregate

- Modules OK: `42/42`
- Median output rel-L2: `0.126047`
- P90 output rel-L2: `0.202799`
- Median normalized output MSE: `0.01589342`
- Median weight rel-L2: `0.155509`
- Median compression vs FP32: `7.6413x`
- Peak CUDA memory allocated by script: `1194.52 MiB`

## Family Summary

| family | modules | median output rel-L2 | median compression vs FP32 |
|---|---:|---:|---:|
| attention | 24 | 0.117775 | 7.6409x |
| mlp | 18 | 0.143339 | 7.6415x |

## Per-Module Results (42)

| module | bits | sample rows | output rel-L2 | norm MSE | weight rel-L2 | compression |
|---|---:|---:|---:|---:|---:|---:|
| `model.layers.20.self_attn.v_proj` | 4 | 64 | 0.283618 | 0.08043891 | 0.189248 | 7.6409x |
| `model.layers.13.self_attn.o_proj` | 4 | 64 | 0.276995 | 0.07672641 | 0.173153 | 7.8163x |
| `model.layers.13.mlp.down_proj` | 4 | 64 | 0.220783 | 0.04874523 | 0.196800 | 7.8766x |
| `model.layers.1.mlp.up_proj` | 4 | 64 | 0.208180 | 0.04333875 | 0.152634 | 7.6415x |
| `model.layers.20.mlp.down_proj` | 4 | 64 | 0.203183 | 0.04128322 | 0.201509 | 7.8766x |
| `model.layers.7.mlp.down_proj` | 4 | 64 | 0.199340 | 0.03973662 | 0.191008 | 7.8766x |
| `model.layers.7.self_attn.v_proj` | 4 | 64 | 0.195561 | 0.03824403 | 0.159974 | 7.6409x |
| `model.layers.13.mlp.up_proj` | 4 | 64 | 0.192406 | 0.03701996 | 0.155792 | 7.6415x |
| `model.layers.27.mlp.up_proj` | 4 | 64 | 0.186607 | 0.03482206 | 0.155976 | 7.6415x |
| `model.layers.7.self_attn.o_proj` | 4 | 64 | 0.184458 | 0.03402480 | 0.168773 | 7.8163x |
| `model.layers.20.self_attn.o_proj` | 4 | 64 | 0.171461 | 0.02939880 | 0.183830 | 7.8163x |
| `model.layers.7.mlp.up_proj` | 4 | 64 | 0.170109 | 0.02893696 | 0.150891 | 7.6415x |
| `model.layers.27.self_attn.o_proj` | 4 | 64 | 0.168721 | 0.02846675 | 0.158777 | 7.8163x |
| `model.layers.1.self_attn.v_proj` | 4 | 64 | 0.162924 | 0.02654418 | 0.150430 | 7.6409x |
| `model.layers.0.mlp.up_proj` | 4 | 64 | 0.161309 | 0.02602058 | 0.152933 | 7.6415x |
| `model.layers.20.mlp.up_proj` | 4 | 64 | 0.157096 | 0.02467922 | 0.160515 | 7.6415x |
| `model.layers.1.self_attn.o_proj` | 4 | 64 | 0.151212 | 0.02286501 | 0.167981 | 7.8163x |
| `model.layers.0.self_attn.o_proj` | 4 | 64 | 0.144144 | 0.02077759 | 0.189837 | 7.8163x |
| `model.layers.20.mlp.gate_proj` | 4 | 64 | 0.129582 | 0.01679162 | 0.169780 | 7.6415x |
| `model.layers.13.self_attn.q_proj` | 4 | 64 | 0.129365 | 0.01673543 | 0.152416 | 7.6413x |
| `model.layers.13.mlp.gate_proj` | 4 | 64 | 0.128387 | 0.01648325 | 0.158504 | 7.6415x |
| `model.layers.7.self_attn.q_proj` | 4 | 64 | 0.123708 | 0.01530358 | 0.154523 | 7.6413x |
| `model.layers.27.mlp.gate_proj` | 4 | 64 | 0.119069 | 0.01417748 | 0.161848 | 7.6415x |
| `model.layers.1.self_attn.q_proj` | 4 | 64 | 0.117814 | 0.01388010 | 0.156059 | 7.6413x |
| `model.layers.7.self_attn.k_proj` | 4 | 64 | 0.117737 | 0.01386202 | 0.155225 | 7.6409x |
| `model.layers.27.self_attn.q_proj` | 4 | 64 | 0.112142 | 0.01257573 | 0.150758 | 7.6413x |
| `model.layers.27.self_attn.k_proj` | 4 | 64 | 0.101359 | 0.01027373 | 0.156762 | 7.6409x |
| `model.layers.7.mlp.gate_proj` | 4 | 64 | 0.099068 | 0.00981444 | 0.148005 | 7.6415x |
| `model.layers.0.self_attn.q_proj` | 4 | 64 | 0.097103 | 0.00942902 | 0.166855 | 7.6413x |
| `model.layers.0.mlp.gate_proj` | 4 | 64 | 0.095733 | 0.00916490 | 0.152086 | 7.6415x |
| `model.layers.13.self_attn.v_proj` | 4 | 64 | 0.095145 | 0.00905260 | 0.151381 | 7.6409x |
| `model.layers.1.self_attn.k_proj` | 4 | 64 | 0.089171 | 0.00795140 | 0.154405 | 7.6409x |
| `model.layers.13.self_attn.k_proj` | 4 | 64 | 0.076549 | 0.00585971 | 0.161807 | 7.6409x |
| `model.layers.0.self_attn.k_proj` | 4 | 64 | 0.076405 | 0.00583775 | 0.150826 | 7.6409x |
| `model.layers.27.self_attn.v_proj` | 8 | 64 | 0.014345 | 0.00020578 | 0.008388 | 3.9082x |
| `model.layers.0.self_attn.v_proj` | 8 | 64 | 0.009847 | 0.00009697 | 0.008363 | 3.9082x |
| `model.layers.20.self_attn.k_proj` | 8 | 64 | 0.009636 | 0.00009286 | 0.009717 | 3.9082x |
| `model.layers.1.mlp.down_proj` | 8 | 64 | 0.009441 | 0.00008913 | 0.010328 | 3.9689x |
| `model.layers.0.mlp.down_proj` | 8 | 64 | 0.008772 | 0.00007694 | 0.009731 | 3.9689x |
| `model.layers.20.self_attn.q_proj` | 8 | 64 | 0.008432 | 0.00007110 | 0.008973 | 3.9083x |
| `model.layers.27.mlp.down_proj` | 8 | 64 | 0.005765 | 0.00003323 | 0.011026 | 3.9689x |
| `model.layers.1.mlp.gate_proj` | 8 | 64 | 0.004297 | 0.00001846 | 0.008160 | 3.9083x |

## Scope

- This evaluates ESMP package reconstruction on sampled real module activations.
- It is a local module-quality check, not an end-to-end packed LLM runtime.
- The next step is replacing the selected Linear modules during generation and measuring TTFT/tokens/s.
