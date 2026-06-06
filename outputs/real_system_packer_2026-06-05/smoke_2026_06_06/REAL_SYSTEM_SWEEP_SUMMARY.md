# Real-System Sweep Summary

All rows are produced by local scripts on the current machine. Speedups below 1.0 mean the low-bit path is slower than the baseline.

## Triton GPU Mixed GEMM

| rows | cols | batch | high_every | compression vs FP16 | rowwise ms | grouped ms | torch FP16 ms | grouped/FP16 | grouped/rowwise | grouped rel-L2 | max VRAM MiB |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048 | 1024 | 1 | 16 | 3.7034 | 0.025113 | 0.051862 | 0.019460 | 0.3752 | 0.4842 | 0.1363 | 3461 |
| 2048 | 1024 | 4 | 16 | 3.7034 | 0.033952 | 0.046589 | 0.013188 | 0.2831 | 0.7288 | 0.1381 | 3461 |
| 2048 | 1024 | 16 | 16 | 3.7034 | 0.184209 | 0.038270 | 0.018727 | 0.4893 | 4.8134 | 0.1373 | 3461 |
| 2048 | 1024 | 16 | 8 | 3.5009 | 0.124580 | 0.178266 | 0.041356 | 0.2320 | 0.6988 | 0.1327 | 3463 |
| 3072 | 1024 | 8 | 16 | 3.7034 | 0.088774 | 0.037978 | 0.013423 | 0.3534 | 2.3375 | 0.1376 | 3479 |
| 1024 | 3072 | 8 | 16 | 3.7441 | 0.059110 | 0.036414 | 0.014279 | 0.3921 | 1.6233 | 0.1491 | 3502 |

## C++ ESMP Runtime

| module file | rows | cols | avg bits | compression vs FP32 | full ms | active rows | selected ms | selected/full speedup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| model__layers__0__self_attn__q_proj.esmp | 2048 | 1024 | 4.0000 | 7.6413 | 6.299063 | 64 | 0.203517 | 30.9510 |
| model__layers__0__self_attn__v_proj.esmp | 1024 | 1024 | 8.0000 | 3.9082 | 4.807837 | 64 | 0.313321 | 15.3448 |
| model__layers__0__mlp__gate_proj.esmp | 3072 | 1024 | 4.0000 | 7.6415 | 9.675768 | 64 | 0.218822 | 44.2176 |
| model__layers__0__mlp__down_proj.esmp | 1024 | 3072 | 8.0000 | 3.9689 | 15.096786 | 64 | 0.887396 | 17.0125 |
| model__layers__10__self_attn__q_proj.esmp | 2048 | 1024 | 4.0000 | 7.6413 | 6.196306 | 64 | 0.195973 | 31.6182 |
| model__layers__10__mlp__gate_proj.esmp | 3072 | 1024 | 4.0000 | 7.6415 | 8.620198 | 64 | 0.182048 | 47.3512 |

## Interpretation Guardrails

- Triton grouped kernels measure packed-storage execution, but are still prototype kernels, not fused transformer runtime.
- ESMP C++ runtime numbers are CPU module-level GEMV numbers, not end-to-end LLM token latency.
- These results are valid evidence for systems bottleneck analysis and follow-up kernel design, not yet a SOTA quantization claim.
