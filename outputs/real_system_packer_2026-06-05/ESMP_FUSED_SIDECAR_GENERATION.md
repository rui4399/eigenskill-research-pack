# ESMP Fused Selected-Row Sidecar Generation Smoke

Date: `2026-06-06`

This experiment attaches the fused QKV selected-row ESMP runtime to real HF generation activations. It registers a pre-hook on selected `q_proj` modules, runs the fused selected-row packed kernel over the same hidden-state tensor used by Q/K/V, synchronizes with CUDA events, and discards the sidecar output.

This is not end-to-end LLM acceleration. It is a real decode-loop integration and overhead measurement for the fused selected-row runtime.

## Setup

- Model: `Qwen/Qwen3-0.6B`
- Loader: Hugging Face FP16 same-loader path
- Prompt tokens: `12`
- Generated tokens: `16`
- Sidecar suffixes: `q_proj,k_proj,v_proj`
- Selected rows per module: `64`
- Triton block config: `32x16x64`
- GPU guard: `--max-memory-ratio 0.90`

## Generation Results

| path | sync mode | sidecar layers | sidecar calls | TTFT s | elapsed s | tokens/s | sidecar CUDA sum ms | sidecar median ms/call | script peak CUDA MiB | guard peak MiB | guard ratio |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| HF same-loader baseline | n/a | 0 | 0 | 0.028981 | 0.543037 | 29.4639 | 0.0000 | 0.0000 | 1173.30 | 3582 | 0.4395 |
| fused ESMP sidecar | per-call | 1 | 16 | 0.041236 | 0.603245 | 26.5232 | 4.6900 | 0.2606 | 1173.43 | 3581 | 0.4393 |
| fused ESMP sidecar | per-call | 3 | 48 | 0.067467 | 0.801341 | 19.9665 | 11.2085 | 0.2218 | 1173.63 | 3588 | 0.4402 |
| fused ESMP sidecar | deferred-end | 1 | 16 | 0.038116 | 0.638191 | 25.0709 | 4.7119 | 0.2653 | 1173.43 | 3582 | 0.4395 |
| fused ESMP sidecar | deferred-end | 3 | 48 | 0.043812 | 0.672049 | 23.8078 | 10.2186 | 0.2062 | 1173.63 | 3583 | 0.4396 |

Generated text matched the baseline in all measured sidecar runs:

```text
 Also, explain the difference between mixed-precision and single-precision. | Also
```

## Sidecar Details

1-layer sidecar:

- Layer: `0`
- Modules: `model.layers.0.self_attn.q_proj`, `k_proj`, `v_proj`
- Selected rows total: `192`
- Low/high rows: `128 / 64`
- Calls: `16`
- Input shapes seen: `1x12x1024`, `1x1x1024`
- CUDA event timing: sum `4.6900 ms`, mean `0.2931 ms`, median `0.2606 ms`, p90 `0.4219 ms`, max `0.4900 ms`

3-layer sidecar:

- Layers: `0,1,7`
- Calls: `48`
- Selected rows total per layer: `192`
- Input shapes seen: `1x12x1024`, `1x1x1024`
- CUDA event timing: sum `11.2085 ms`, mean `0.2335 ms`, median `0.2218 ms`, p90 `0.3755 ms`, max `0.4682 ms`

3-layer deferred-sync sidecar:

- Layers: `0,1,7`
- Calls: `48`
- CUDA event timing: sum `10.2186 ms`, mean `0.2129 ms`, median `0.2062 ms`, p90 `0.2985 ms`, max `0.4407 ms`
- Throughput: `23.8078` tokens/s versus `19.9665` tokens/s for per-call synchronization

## Interpretation

- The fused selected-row ESMP kernel now runs inside the real HF generation/decode loop under a guarded GPU run.
- The measured sidecar overhead is visible but bounded. Per-call synchronization is pessimistic; deferred synchronization improves the 3-layer run from `19.97` to `23.81` tokens/s.
- Memory stayed essentially unchanged versus the same-loader baseline, around `44%` of the 8.15 GiB GPU.
- This supports the systems integration claim, not a final acceleration claim. The next required step is replacing or fusing real QKV computation rather than running the sidecar in addition to dense QKV.

## Files

```text
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_baseline_16tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_baseline_16tok_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_smoke.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_smoke_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_smoke_async.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_smoke_async_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_async.json
outputs/real_system_packer_2026-06-05/qwen3_fused_sidecar_generation_3layer_async_gpu_guard.json
```
