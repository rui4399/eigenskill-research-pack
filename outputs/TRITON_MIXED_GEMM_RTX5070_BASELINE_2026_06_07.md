# Triton Mixed GEMM RTX 5070 Baseline

Date: 2026-06-07

This is a non-ledger kernel probe for the ESMP/Triton runtime track. It records
the current physical mixed INT4/INT8 Triton kernel behavior on the local RTX
5070 Laptop GPU before deeper fused-kernel work. It is not an end-to-end LLM
runtime result and it is not a speedup claim.

## Environment

- device: NVIDIA GeForce RTX 5070 Laptop GPU
- PyTorch: 2.12.0+cu130
- Triton: 3.7.0
- guard: `run_with_gpu_guard.py --max-memory-ratio 0.90`

## Results

| shape | batch | grouped mixed ms | torch FP16 ms | grouped / FP16 speedup | grouped / rowwise speedup | compression vs FP16 | peak guard VRAM |
|---|---:|---:|---:|---:|---:|---:|---:|
| 4096 x 4096 | 16 | 0.083379 | 0.049523 | 0.5939x | 5.3033x | 3.5417x | 0.4635 |
| 1024 x 3072 | 16 | 0.045496 | 0.016924 | 0.3720x | 2.3888x | 3.5371x | 0.4518 |
| 4096 x 4096 | 128 | 0.188085 | 0.141914 | 0.7545x | 18.9217x | 3.5417x | 0.4690 |
| 4096 x 4096 | 512 | 1.006286 | 0.625873 | 0.6220x | 15.8070x | 3.5417x | 0.4998 |

## Interpretation

The grouped path substantially removes row-wise dynamic-dispatch overhead, but
it still loses to the strong torch FP16 baseline on all measured RTX 5070
shapes in this probe. This makes the next kernel milestone concrete:

1. fuse unpack, dequantization, and accumulation more tightly;
2. reduce the current two-launch INT4/INT8 grouped path where possible;
3. explore Tensor Core compatible accumulation layouts or a CUTLASS/Triton
   matmul formulation that avoids scalarized unpack overhead;
4. keep reporting FP16-relative latency and guarded VRAM together.

## Artifacts

- `outputs/triton_mixed_gemm_rtx5070_4096x4096_b16_2026_06_07.json`
- `outputs/triton_mixed_gemm_rtx5070_4096x4096_b16_guard_2026_06_07.json`
- `outputs/triton_mixed_gemm_rtx5070_1024x3072_b16_2026_06_07.json`
- `outputs/triton_mixed_gemm_rtx5070_1024x3072_b16_guard_2026_06_07.json`
- `outputs/triton_mixed_gemm_rtx5070_4096x4096_b128_2026_06_07.json`
- `outputs/triton_mixed_gemm_rtx5070_4096x4096_b128_guard_2026_06_07.json`
- `outputs/triton_mixed_gemm_rtx5070_4096x4096_b512_2026_06_07.json`
- `outputs/triton_mixed_gemm_rtx5070_4096x4096_b512_guard_2026_06_07.json`

## Claim Boundary

Valid claim: the current grouped Triton mixed INT4/INT8 kernel reduces row-wise
dispatch overhead and gives measured compression on RTX 5070 under a 90% VRAM
guard.

Invalid claim: this proves end-to-end LLM acceleration, production runtime
readiness, Tensor Core speedup, mobile deployment, or energy improvement.
