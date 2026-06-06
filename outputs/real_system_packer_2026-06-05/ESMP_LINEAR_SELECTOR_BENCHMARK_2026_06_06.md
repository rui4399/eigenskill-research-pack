# ESMP Linear Runtime Shape Benchmark

Date: `2026-06-06`
Model: `Qwen/Qwen3-0.6B`
Modules: `1`
Batch shapes: `[1, 12]`
Warmup/iters: `2/8`

## Summary By Runtime

| runtime | cases | median ms | mean ms | median speedup vs dense | median rel-L2 |
|---|---:|---:|---:|---:|---:|
| dense | 2 | 0.017213 | 0.017213 | 1.0000 | 0.000000 |
| cached | 2 | 0.018725 | 0.018725 | 0.9348 | 0.167311 |
| python_on_demand | 2 | 32.305268 | 32.305268 | 0.0005 | 0.167311 |
| triton_grouped | 2 | 0.072730 | 0.072730 | 0.2404 | 0.167311 |

## Per-Case Results

| module | batch | runtime | latency ms | speedup vs dense | rel-L2 vs dense | selector calls |
|---|---:|---|---:|---:|---:|---:|
| `model.layers.0.self_attn.q_proj` | 1 | cached | 0.016635 | 1.0745 | 0.167246 | 0 |
| `model.layers.0.self_attn.q_proj` | 1 | dense | 0.017875 | 1.0000 | 0.000000 | 0 |
| `model.layers.0.self_attn.q_proj` | 1 | python_on_demand | 30.980503 | 0.0006 | 0.167246 | 0 |
| `model.layers.0.self_attn.q_proj` | 1 | triton_grouped | 0.064944 | 0.2752 | 0.167246 | 11 |
| `model.layers.0.self_attn.q_proj` | 12 | cached | 0.020815 | 0.7951 | 0.167377 | 0 |
| `model.layers.0.self_attn.q_proj` | 12 | dense | 0.016550 | 1.0000 | 0.000000 | 0 |
| `model.layers.0.self_attn.q_proj` | 12 | python_on_demand | 33.630033 | 0.0005 | 0.167377 | 0 |
| `model.layers.0.self_attn.q_proj` | 12 | triton_grouped | 0.080517 | 0.2056 | 0.167377 | 11 |

## Interpretation Guardrails

- This is a real ESMP module-runtime benchmark, not an end-to-end LLM claim.
- Batch `1` approximates decode-step Linear calls; batch `12` approximates the current short-prompt prefill; batch `64` tests amortization.
- Triton speedups below dense mean the current grouped kernel needs fusion, shape-specific tuning, or a lower-launch-overhead path.
