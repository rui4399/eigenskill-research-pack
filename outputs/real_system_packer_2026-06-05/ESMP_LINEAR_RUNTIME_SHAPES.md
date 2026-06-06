# ESMP Linear Runtime Shape Benchmark

Date: `2026-06-06`
Model: `Qwen/Qwen3-0.6B`
Modules: `3`
Batch shapes: `[1, 12, 64]`
Warmup/iters: `10/80`

## Summary By Runtime

| runtime | cases | median ms | mean ms | median speedup vs dense | median rel-L2 |
|---|---:|---:|---:|---:|---:|
| dense | 9 | 0.014725 | 0.016025 | 1.0000 | 0.000000 |
| cached | 9 | 0.016797 | 0.017905 | 0.8801 | 0.150103 |
| python_on_demand | 9 | 18.072527 | 18.277878 | 0.0009 | 0.150103 |
| triton_grouped | 9 | 0.051871 | 0.054061 | 0.2667 | 0.150103 |

## Per-Case Results

| module | batch | runtime | latency ms | speedup vs dense | rel-L2 vs dense |
|---|---:|---|---:|---:|---:|
| `model.layers.0.self_attn.k_proj` | 1 | cached | 0.014225 | 0.9726 | 0.144082 |
| `model.layers.0.self_attn.k_proj` | 1 | dense | 0.013835 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 1 | python_on_demand | 18.180514 | 0.0008 | 0.144082 |
| `model.layers.0.self_attn.k_proj` | 1 | triton_grouped | 0.051871 | 0.2667 | 0.144082 |
| `model.layers.0.self_attn.k_proj` | 12 | cached | 0.015248 | 1.0223 | 0.155920 |
| `model.layers.0.self_attn.k_proj` | 12 | dense | 0.015588 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 12 | python_on_demand | 18.072527 | 0.0009 | 0.155920 |
| `model.layers.0.self_attn.k_proj` | 12 | triton_grouped | 0.059412 | 0.2624 | 0.155920 |
| `model.layers.0.self_attn.k_proj` | 64 | cached | 0.023417 | 0.7518 | 0.150103 |
| `model.layers.0.self_attn.k_proj` | 64 | dense | 0.017604 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.k_proj` | 64 | python_on_demand | 17.919979 | 0.0010 | 0.150103 |
| `model.layers.0.self_attn.k_proj` | 64 | triton_grouped | 0.044620 | 0.3945 | 0.150103 |
| `model.layers.0.self_attn.q_proj` | 1 | cached | 0.015441 | 0.8801 | 0.167246 |
| `model.layers.0.self_attn.q_proj` | 1 | dense | 0.013590 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 1 | python_on_demand | 32.122879 | 0.0004 | 0.167246 |
| `model.layers.0.self_attn.q_proj` | 1 | triton_grouped | 0.048477 | 0.2803 | 0.167246 |
| `model.layers.0.self_attn.q_proj` | 12 | cached | 0.016812 | 1.0781 | 0.167377 |
| `model.layers.0.self_attn.q_proj` | 12 | dense | 0.018126 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 12 | python_on_demand | 33.257987 | 0.0005 | 0.167377 |
| `model.layers.0.self_attn.q_proj` | 12 | triton_grouped | 0.049480 | 0.3663 | 0.167377 |
| `model.layers.0.self_attn.q_proj` | 64 | cached | 0.018783 | 0.7808 | 0.168726 |
| `model.layers.0.self_attn.q_proj` | 64 | dense | 0.014666 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.q_proj` | 64 | python_on_demand | 31.799399 | 0.0005 | 0.168726 |
| `model.layers.0.self_attn.q_proj` | 64 | triton_grouped | 0.057563 | 0.2548 | 0.168726 |
| `model.layers.0.self_attn.v_proj` | 1 | cached | 0.014605 | 0.9521 | 0.008624 |
| `model.layers.0.self_attn.v_proj` | 1 | dense | 0.013905 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 1 | python_on_demand | 4.439187 | 0.0031 | 0.008624 |
| `model.layers.0.self_attn.v_proj` | 1 | triton_grouped | 0.062981 | 0.2208 | 0.008624 |
| `model.layers.0.self_attn.v_proj` | 12 | cached | 0.025814 | 0.8596 | 0.008317 |
| `model.layers.0.self_attn.v_proj` | 12 | dense | 0.022189 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 12 | python_on_demand | 4.521815 | 0.0049 | 0.008317 |
| `model.layers.0.self_attn.v_proj` | 12 | triton_grouped | 0.046188 | 0.4804 | 0.008317 |
| `model.layers.0.self_attn.v_proj` | 64 | cached | 0.016797 | 0.8766 | 0.008405 |
| `model.layers.0.self_attn.v_proj` | 64 | dense | 0.014725 | 1.0000 | 0.000000 |
| `model.layers.0.self_attn.v_proj` | 64 | python_on_demand | 4.186618 | 0.0035 | 0.008405 |
| `model.layers.0.self_attn.v_proj` | 64 | triton_grouped | 0.065961 | 0.2232 | 0.008405 |

## Interpretation Guardrails

- This is a real ESMP module-runtime benchmark, not an end-to-end LLM claim.
- Batch `1` approximates decode-step Linear calls; batch `12` approximates the current short-prompt prefill; batch `64` tests amortization.
- Triton speedups below dense mean the current grouped kernel needs fusion, shape-specific tuning, or a lower-launch-overhead path.
