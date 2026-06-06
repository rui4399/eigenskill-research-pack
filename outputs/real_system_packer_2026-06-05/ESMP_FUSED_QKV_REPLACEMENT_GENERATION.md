# ESMP Fused QKV Replacement Generation Smoke

Date: `2026-06-06`

This experiment replaces selected Qwen3 QKV projections with a shared fused ESMP runtime. Unlike the sidecar experiment, this path actually replaces the model's `q_proj`, `k_proj`, and `v_proj` modules for selected layers. The first wrapper call computes concatenated packed Q/K/V output once; the following K/V wrappers return cached slices.

This is still a controlled smoke, not a production transformer runtime. It verifies that a real packed fused QKV replacement can run inside Hugging Face generation while reporting TTFT, throughput, memory, cache behavior, compression, and text effects.

## Setup

- Model: `Qwen/Qwen3-0.6B`
- Loader: Hugging Face FP16 same-loader path
- Replacement: fused packed ESMP QKV for selected layers
- Runtime: Triton grouped INT4/INT8 packed rows
- Sync mode: deferred event sync (`--sync-mode end`)
- Triton block config: `32x16x64`
- GPU guard: `--max-memory-ratio 0.90`

## Generation Results

| path | replaced layers | max new tokens | TTFT s | elapsed s | tokens/s | speed vs baseline | generated text match | script peak CUDA MiB | guard peak MiB | guard ratio |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| HF same-loader baseline | 0 | 16 | 0.028808 | 0.774345 | 20.6626 | 1.0000x | reference | 1173.30 | 3582 | 0.4395 |
| fused ESMP QKV replacement | 1 | 16 | 0.033764 | 0.488582 | 32.7479 | 1.5850x | exact match | 1168.36 | 3586 | 0.4399 |
| fused ESMP QKV replacement | 3 | 16 | 0.031471 | 0.619774 | 25.8158 | 1.2494x | changed, same topic | 1156.49 | 3592 | 0.4407 |
| HF same-loader baseline | 0 | 64 | 0.048212 | 2.391258 | 26.7642 | 1.0000x | reference | 1178.55 | 3591 | 0.4406 |
| fused ESMP QKV replacement | 1 | 64 | 0.032971 | 2.116118 | 30.2441 | 1.1300x | prefix match, then diverges | 1173.61 | 3587 | 0.4401 |
| fused ESMP QKV replacement | 3 | 64 | 0.032545 | 2.412621 | 26.5272 | 0.9911x | changed, same topic | 1161.74 | 3593 | 0.4408 |

## Replacement Runtime Behavior

1-layer, 64-token run:

- Replaced modules: layer-0 `q_proj`, `k_proj`, `v_proj`
- Raw FP32 bytes represented: `16,777,216`
- ESMP package bytes: `2,719,936`
- Compression vs FP32: `6.1682x`
- Wrapper calls: `192`
- Fused compute calls: `64`
- Cache hits / misses: `128 / 64`
- CUDA event timing: sum `13.0380 ms`, mean `0.2037 ms`, median `0.1929 ms`, p90 `0.2486 ms`, max `0.5085 ms`

3-layer, 64-token run:

- Replaced layers: `0,1,7`
- Raw FP32 bytes represented: `50,331,648`
- ESMP package bytes: `7,111,232`
- Compression vs FP32: `7.0778x`
- Wrapper calls: `576`
- Fused compute calls: `192`
- Cache hits / misses: `384 / 192`
- CUDA event timing: sum `29.2797 ms`, mean `0.1525 ms`, median `0.1420 ms`, p90 `0.2285 ms`, max `0.6129 ms`

The cache behavior confirms that each Q/K/V triplet is fused as intended: Q computes the packed concatenated projection, while K/V read cached slices.

## Text Effects

The 16-token 1-layer replacement produced the same text as the baseline. Longer or deeper replacement runs diverged while staying on the same broad topic. This is expected from approximate INT4/INT8 QKV replacement and should be treated as a quality risk, not hidden.

For publication claims, the honest statement is:

- The fused ESMP QKV replacement is executable inside real HF generation.
- It can reduce runtime for shallow replacement and remain near baseline for 3-layer replacement on this short prompt.
- It is not yet quality-preserving enough to claim transparent end-to-end quantized generation.

## Files

```text
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_baseline_16tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_baseline_16tok_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_baseline_64tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_baseline_64tok_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer_64tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_1layer_64tok_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_3layer_16tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_3layer_16tok_gpu_guard.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_3layer_64tok.json
outputs/real_system_packer_2026-06-05/qwen3_fused_qkv_generation_3layer_64tok_gpu_guard.json
```
