# ESMP Fused Selected-Row Runtime Benchmark

Date: `2026-06-05T20:46:20Z`
Model: `Qwen/Qwen3-0.6B`
Layers: `[0]`
Module suffixes: `['q_proj', 'k_proj', 'v_proj']`
Batch shapes: `[1]`
Selected rows per module: `[16]`
Warmup/iters: `2/5`

## Summary By Runtime

| runtime | cases | median ms | p90 ms | median speedup vs dense full concat | median speedup vs dense selected concat | median speedup vs triton separate | median rel-L2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| dense_full_concat | 1 | 0.035147 | 0.035147 | 1.0000 | 0.6888 | 6.1851 | 0.000000 |
| dense_selected_concat | 1 | 0.024210 | 0.024210 | 1.4517 | 1.0000 | 8.9792 | 0.000000 |
| cached_selected_concat | 1 | 0.018988 | 0.018988 | 1.8510 | 1.2750 | 11.4486 | 0.091802 |
| triton_separate_selected | 1 | 0.217387 | 0.217387 | 0.1617 | 0.1114 | 1.0000 | 0.091802 |
| triton_fused_selected | 1 | 0.081580 | 0.081580 | 0.4308 | 0.2968 | 2.6647 | 0.091802 |

## Fused Wins

- Fused faster than triton separate: `1 / 1`
- Fused faster than dense full concat: `0 / 1`
- Fused faster than dense selected concat: `0 / 1`
- Best fused speedup vs triton separate: `2.6647x`
- Best fused speedup vs dense full concat: `0.4308x`

## Per-Case Results

| layer | batch | selected/module | runtime | latency ms | speedup vs full concat | speedup vs selected concat | speedup vs triton separate | rel-L2 |
|---:|---:|---:|---|---:|---:|---:|---:|---:|
| 0 | 1 | 16 | cached_selected_concat | 0.018988 | 1.8510 | 1.2750 | 11.4486 | 0.091802 |
| 0 | 1 | 16 | dense_full_concat | 0.035147 | 1.0000 | 0.6888 | 6.1851 | 0.000000 |
| 0 | 1 | 16 | dense_selected_concat | 0.024210 | 1.4517 | 1.0000 | 8.9792 | 0.000000 |
| 0 | 1 | 16 | triton_fused_selected | 0.081580 | 0.4308 | 0.2968 | 2.6647 | 0.091802 |
| 0 | 1 | 16 | triton_separate_selected | 0.217387 | 0.1617 | 0.1114 | 1.0000 | 0.091802 |

## Interpretation Guardrails

- This is a same-input multi-module selected-row microbenchmark, not end-to-end LLM acceleration.
- `dense_full_concat` and `dense_selected_concat` are strong one-launch torch baselines built from concatenated FP16 weights.
- `triton_fused_selected` reduces ESMP launch count across QKV-style modules by concatenating selected packed rows ahead of time.
