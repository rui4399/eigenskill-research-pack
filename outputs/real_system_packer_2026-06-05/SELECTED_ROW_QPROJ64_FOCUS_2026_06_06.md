# ESMP Selected-Row Runtime Benchmark

Date: `2026-06-06`
Model: `Qwen/Qwen3-0.6B`
Modules: `1`
Batch shapes: `[12]`
Selected rows: `[64]`
Warmup/iters: `5/20`

## Summary By Runtime

| runtime | cases | median ms | mean ms | median speedup vs dense full | median speedup vs dense selected | median rel-L2 |
|---|---:|---:|---:|---:|---:|---:|
| dense_full | 1 | 0.022679 | 0.022679 | 1.0000 | 1.2314 | 0.000000 |
| dense_selected | 1 | 0.027927 | 0.027927 | 0.8121 | 1.0000 | 0.000000 |
| cached_selected | 1 | 0.019273 | 0.019273 | 1.1767 | 1.4490 | 0.177566 |
| triton_selected | 1 | 0.040010 | 0.040010 | 0.5668 | 0.6980 | 0.177566 |

## Per-Case Results

| module | batch | selected rows | runtime | latency ms | speedup vs dense full | speedup vs dense selected | rel-L2 |
|---|---:|---:|---|---:|---:|---:|---:|
| `model.layers.0.self_attn.q_proj` | 12 | 64 | cached_selected | 0.019273 | 1.1767 | 1.4490 | 0.177566 |
| `model.layers.0.self_attn.q_proj` | 12 | 64 | dense_full | 0.022679 | 1.0000 | 1.2314 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 12 | 64 | dense_selected | 0.027927 | 0.8121 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 12 | 64 | triton_selected | 0.040010 | 0.5668 | 0.6980 | 0.177566 |

## Interpretation Guardrails

- This benchmark measures selected output rows only; it is a routing/bypass microbenchmark, not full generation throughput.
- `speedup vs dense full` is the system-routing comparison: avoid materializing all rows when only a skill slice is needed.
- `speedup vs dense selected` is the kernel comparison against torch operating on the selected FP16 rows only.
