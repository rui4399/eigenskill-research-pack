# C++ ESMP Runtime Stratified Sweep

This report runs the existing C++ packed ESMP runtime on real Qwen3-0.6B Linear module packages.
It measures module-level GEMV and selected-row execution; it is not end-to-end token latency.

- total module runs: 42
- successful module runs: 42

## Summary By Module Family

| family | count | median full ms | median selected ms | median selected/full speedup | median compression vs FP32 |
|---|---:|---:|---:|---:|---:|
| attention | 24 | 5.520702 | 0.205620 | 16.3918 | 7.6409x |
| mlp | 18 | 9.231019 | 0.207805 | 46.3437 | 7.6415x |

## Summary By Layer Bucket

| bucket | count | median full ms | median selected ms | median selected/full speedup | median compression vs FP32 |
|---|---:|---:|---:|---:|---:|
| early | 14 | 6.367805 | 0.269351 | 17.5250 | 7.6411x |
| late | 14 | 7.431746 | 0.254317 | 16.8259 | 7.6414x |
| middle | 14 | 6.373200 | 0.188833 | 17.0703 | 7.6415x |

## Best Selected-Row Speedups

| rank | layer | module | shape | avg bits | compression | full ms | selected rows | selected ms | speedup |
|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | `mlp__up_proj` | 3072x1024 | 4.0000 | 7.6415x | 11.933423 | 64 | 0.211253 | 56.4888 |
| 2 | 1 | `mlp__up_proj` | 3072x1024 | 4.0000 | 7.6415x | 9.459231 | 64 | 0.183404 | 51.5759 |
| 3 | 1 | `mlp__gate_proj` | 3072x1024 | 8.0000 | 3.9083x | 14.691840 | 64 | 0.285200 | 51.5142 |
| 4 | 13 | `mlp__up_proj` | 3072x1024 | 4.0000 | 7.6415x | 9.188087 | 64 | 0.182533 | 50.3366 |
| 5 | 20 | `mlp__gate_proj` | 3072x1024 | 4.0000 | 7.6415x | 9.031375 | 64 | 0.180800 | 49.9523 |
| 6 | 7 | `mlp__up_proj` | 3072x1024 | 4.0000 | 7.6415x | 9.330151 | 64 | 0.189434 | 49.2528 |
| 7 | 7 | `mlp__gate_proj` | 3072x1024 | 4.0000 | 7.6415x | 9.204201 | 64 | 0.187968 | 48.9669 |
| 8 | 20 | `mlp__up_proj` | 3072x1024 | 4.0000 | 7.6415x | 8.894904 | 64 | 0.183949 | 48.3553 |
| 9 | 13 | `mlp__gate_proj` | 3072x1024 | 4.0000 | 7.6415x | 8.869519 | 64 | 0.187982 | 47.1828 |
| 10 | 27 | `mlp__up_proj` | 3072x1024 | 4.0000 | 7.6415x | 8.737401 | 64 | 0.192011 | 45.5047 |

## Fastest Selected-Row Runs

| rank | layer | module | shape | avg bits | selected rows | selected ms | full ms |
|---:|---:|---|---:|---:|---:|---:|---:|
| 1 | 27 | `self_attn__q_proj` | 2048x1024 | 4.0000 | 64 | 0.180110 | 5.795023 |
| 2 | 20 | `mlp__gate_proj` | 3072x1024 | 4.0000 | 64 | 0.180800 | 9.031375 |
| 3 | 13 | `self_attn__v_proj` | 1024x1024 | 4.0000 | 64 | 0.181667 | 3.185272 |
| 4 | 13 | `mlp__up_proj` | 3072x1024 | 4.0000 | 64 | 0.182533 | 9.188087 |
| 5 | 1 | `mlp__up_proj` | 3072x1024 | 4.0000 | 64 | 0.183404 | 9.459231 |
| 6 | 20 | `mlp__up_proj` | 3072x1024 | 4.0000 | 64 | 0.183949 | 8.894904 |
| 7 | 13 | `self_attn__q_proj` | 2048x1024 | 4.0000 | 64 | 0.184335 | 6.095600 |
| 8 | 7 | `self_attn__k_proj` | 1024x1024 | 4.0000 | 64 | 0.185854 | 2.964388 |
| 9 | 27 | `self_attn__k_proj` | 1024x1024 | 4.0000 | 64 | 0.186888 | 2.971495 |
| 10 | 7 | `mlp__gate_proj` | 3072x1024 | 4.0000 | 64 | 0.187968 | 9.204201 |

## Claim Boundary

- Valid claim: selected-row packed execution is consistently much faster than full packed GEMV for routed/bypass-like sparse row use.
- Invalid claim: this proves end-to-end LLM token acceleration. That still requires a fused runtime path.
