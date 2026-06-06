# ESMP Activation Reconstruction Report

Date: `2026-06-06`
Model: `Qwen/Qwen3-0.6B`
Package summary: `/mnt/c/Users/18042/Documents/Codex/2026-06-01/chatgpt-context-request-algorithm-system-co/github_publish/eigenskill-research-pack/outputs/real_system_packer_2026-06-05/qwen3_esmp/pack_summary.json`
Prompts: `2`
Max length: `64`
Sample rows per module: `32`
Device: `cuda`

## Aggregate

- Modules OK: `3/3`
- Median output rel-L2: `0.076153`
- P90 output rel-L2: `0.091643`
- Median normalized output MSE: `0.00579932`
- Median weight rel-L2: `0.150826`
- Median compression vs FP32: `7.6409x`
- Peak CUDA memory allocated by script: `1185.45 MiB`

## Family Summary

| family | modules | median output rel-L2 | median compression vs FP32 |
|---|---:|---:|---:|
| attention | 3 | 0.076153 | 7.6409x |

## Per-Module Results (3)

| module | bits | sample rows | output rel-L2 | norm MSE | weight rel-L2 | compression |
|---|---:|---:|---:|---:|---:|---:|
| `model.layers.0.self_attn.q_proj` | 4 | 32 | 0.095515 | 0.00912312 | 0.166855 | 7.6413x |
| `model.layers.0.self_attn.k_proj` | 4 | 32 | 0.076153 | 0.00579932 | 0.150826 | 7.6409x |
| `model.layers.0.self_attn.v_proj` | 8 | 32 | 0.009684 | 0.00009377 | 0.008363 | 3.9082x |

## Scope

- This evaluates ESMP package reconstruction on sampled real module activations.
- It is a local module-quality check, not an end-to-end packed LLM runtime.
- The next step is replacing the selected Linear modules during generation and measuring TTFT/tokens/s.
