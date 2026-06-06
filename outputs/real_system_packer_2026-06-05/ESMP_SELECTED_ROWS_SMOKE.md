# ESMP Selected-Row Runtime Benchmark

Date: `2026-06-06`
Model: `Qwen/Qwen3-0.6B`
Modules: `1`
Batch shapes: `[1]`
Selected rows: `[16]`
Warmup/iters: `2/5`

## Summary By Runtime

| runtime | cases | median ms | mean ms | median speedup vs dense full | median speedup vs dense selected | median rel-L2 |
|---|---:|---:|---:|---:|---:|---:|
| dense_full | 1 | 0.025016 | 0.025016 | 1.0000 | 0.8593 | 0.000000 |
| dense_selected | 1 | 0.021495 | 0.021495 | 1.1638 | 1.0000 | 0.000000 |
| cached_selected | 1 | 0.036780 | 0.036780 | 0.6801 | 0.5844 | 0.104553 |
| triton_selected | 1 | 0.050833 | 0.050833 | 0.4921 | 0.4229 | 0.104553 |

## Per-Case Results

| module | batch | selected rows | runtime | latency ms | speedup vs dense full | speedup vs dense selected | rel-L2 |
|---|---:|---:|---|---:|---:|---:|---:|
| `model.layers.0.self_attn.q_proj` | 1 | 16 | cached_selected | 0.036780 | 0.6801 | 0.5844 | 0.104553 |
| `model.layers.0.self_attn.q_proj` | 1 | 16 | dense_full | 0.025016 | 1.0000 | 0.8593 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 1 | 16 | dense_selected | 0.021495 | 1.1638 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 1 | 16 | triton_selected | 0.050833 | 0.4921 | 0.4229 | 0.104553 |

## Interpretation Guardrails

- This benchmark measures selected output rows only; it is a routing/bypass microbenchmark, not full generation throughput.
- `speedup vs dense full` is the system-routing comparison: avoid materializing all rows when only a skill slice is needed.
- `speedup vs dense selected` is the kernel comparison against torch operating on the selected FP16 rows only.
