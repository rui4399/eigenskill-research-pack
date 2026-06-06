# ESMP-Swapped Generation Smoke

Date: `2026-06-06`

Model: `Qwen/Qwen3-0.6B`

Prompt: `Explain mixed-precision quantization in one concise paragraph.`

Max new tokens: `16`

This is a minimal end-to-end wiring check. It replaces only the first three attention projection modules from layer 0 (`q_proj`, `k_proj`, `v_proj`) with modules backed by the real `ESMPQ001` package. It is not yet a high-performance packed LLM runtime.

## Primary Sequential Results

| path | replaced modules | selected package compression vs FP32 | TTFT s | elapsed s | tokens/s | script peak CUDA MiB | guard peak MiB | guard ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HF same-loader baseline | 0 | n/a | 0.9489 | 1.6793 | 9.5277 | 1173.30 | 3543 | 0.4347 |
| ESMP cached dequant | 3 | 6.1682x | 0.9542 | 1.7212 | 9.2958 | 1175.30 | 3556 | 0.4363 |
| ESMP on-demand dequant | 3 | 6.1682x | 1.1813 | 2.9897 | 5.3516 | 1170.33 | 3545 | 0.4349 |
| ESMP Triton grouped | 3 | 6.1682x | 1.9611 | 3.2027 | 4.9957 | 1169.85 | 3551 | 0.4357 |

Generated text is identical across all four primary cold runs:

```text
 Also, explain the difference between mixed-precision and single-precision. | Also
```

## One-Warmup Results

Each path ran one unmeasured generation in the same process before the measured run. Use this table as a steady-state wiring signal, not as a deployment TTFT claim.

| path | replaced modules | runtime | TTFT s | elapsed s | tokens/s | script peak CUDA MiB | guard peak MiB | guard ratio |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| HF same-loader baseline | 0 | dense | 0.0347 | 0.6387 | 25.0523 | 1173.30 | 3559 | 0.4366 |
| ESMP cached dequant | 3 | dense cached dequant | 0.0320 | 0.5550 | 28.8295 | 1175.30 | 3543 | 0.4347 |
| ESMP on-demand dequant | 3 | Python dequant per forward | 0.1543 | 1.7552 | 9.1157 | 1170.33 | 3544 | 0.4348 |
| ESMP Triton grouped | 3 | packed grouped Triton kernel | 0.0458 | 0.7484 | 21.3777 | 1169.85 | 3548 | 0.4353 |

## Interpretation

- The ESMP package can now be connected to the generation path without breaking output for the tested module subset.
- Cached dequant is close to the same-loader HF baseline for this tiny 3-module swap, but it stores dense dequantized weights and therefore is not the final compressed runtime.
- On-demand Python dequant keeps the ESMP package boundary but is much slower. This is direct evidence that the next serious step is replacing Python dequant with a real CUDA/Triton or C++ runtime kernel in the forward path.
- The Triton grouped runtime is now wired into generation and beats Python on-demand after warmup, but for this small 3-module case it still trails dense/cached execution. The likely causes are small batch/sequence sizes, per-call launch overhead, and lack of transformer-level fusion.
- The memory numbers should not be overclaimed: only 3 modules are swapped, and the rest of Qwen3-0.6B remains dense HF FP16.

## Files

```text
outputs/real_system_packer_2026-06-05/qwen3_same_loader_16tok_latency.json
outputs/real_system_packer_2026-06-05/qwen3_same_loader_16tok_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_cached_latency_seq.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_cached_gpu_guard_seq.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_ondemand_latency.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_ondemand_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_triton_latency.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_triton_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_same_loader_16tok_warm_latency.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_cached_warm_latency.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_ondemand_warm_latency.json
outputs/real_system_packer_2026-06-05/qwen3_esmp_swapped_3mod_triton_warm_latency.json
```

Note: earlier non-`seq` baseline/cached files were produced during a concurrent run and should not be used for timing claims.
