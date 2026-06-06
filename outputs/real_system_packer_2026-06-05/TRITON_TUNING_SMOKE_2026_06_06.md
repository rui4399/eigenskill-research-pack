# Triton Mixed-GEMM Cross-Shape Tuning Summary

This report aggregates packed INT4/INT8 Triton GEMM tuning runs across Qwen-like Linear shapes.
It is a kernel benchmark summary, not an end-to-end transformer runtime result.

## Aggregate

- total configs: 24
- valid configs: 24
- configs faster than torch FP16: 2
- configs faster than row-wise dynamic mixed path: 21
- grouped/FP16 speedup median: 0.3843
- grouped/FP16 speedup p90: 0.6866
- grouped/FP16 speedup max: 1.6543
- grouped/row-wise speedup median: 2.2257
- grouped/row-wise speedup max: 3.5292
- compression vs FP16 median: 3.7034x
- grouped rel-L2 median: 0.1378
- max guard VRAM ratio: 0.4514

## Shape Summary

| shape | batch | high_every | configs | FP16 wins | row-wise wins | median grouped/FP16 | max grouped/FP16 | median grouped/row-wise | max grouped/row-wise | median rel-L2 | max VRAM ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2048x1024 | 8 | 16 | 12 | 1 | 9 | 0.3730 | 1.3194 | 1.6032 | 2.2437 | 0.1382 | 0.4381 |
| 2048x1024 | 16 | 16 | 12 | 1 | 12 | 0.3843 | 1.6543 | 3.0704 | 3.5292 | 0.1373 | 0.4514 |

## Top Grouped vs Torch FP16 Cases

| rank | shape | batch | high_every | BM | BN | BK | grouped ms | torch FP16 ms | speedup | compression vs FP16 | rel-L2 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2048x1024 | 16 | 16 | 16 | 8 | 128 | 0.037990 | 0.062845 | 1.6543 | 3.7034x | 0.1373 |
| 2 | 2048x1024 | 8 | 16 | 32 | 8 | 128 | 0.036835 | 0.048601 | 1.3194 | 3.7034x | 0.1382 |
| 3 | 2048x1024 | 8 | 16 | 16 | 16 | 128 | 0.036037 | 0.025587 | 0.7100 | 3.7034x | 0.1382 |
| 4 | 2048x1024 | 8 | 16 | 16 | 32 | 64 | 0.037620 | 0.023774 | 0.6319 | 3.7034x | 0.1382 |
| 5 | 2048x1024 | 16 | 16 | 32 | 16 | 64 | 0.037887 | 0.023776 | 0.6275 | 3.7034x | 0.1373 |
| 6 | 2048x1024 | 16 | 16 | 16 | 16 | 128 | 0.034964 | 0.021533 | 0.6158 | 3.7034x | 0.1373 |
| 7 | 2048x1024 | 16 | 16 | 32 | 32 | 128 | 0.036223 | 0.017705 | 0.4888 | 3.7034x | 0.1373 |
| 8 | 2048x1024 | 8 | 16 | 32 | 32 | 128 | 0.035898 | 0.016923 | 0.4714 | 3.7034x | 0.1382 |
| 9 | 2048x1024 | 8 | 16 | 32 | 32 | 64 | 0.050221 | 0.021596 | 0.4300 | 3.7034x | 0.1382 |
| 10 | 2048x1024 | 16 | 16 | 16 | 16 | 64 | 0.044880 | 0.018745 | 0.4177 | 3.7034x | 0.1373 |
| 11 | 2048x1024 | 8 | 16 | 32 | 16 | 128 | 0.036206 | 0.014591 | 0.4030 | 3.7034x | 0.1382 |
| 12 | 2048x1024 | 16 | 16 | 16 | 8 | 64 | 0.039512 | 0.015642 | 0.3959 | 3.7034x | 0.1373 |

## Claim Boundary

- Valid claim: grouped packed execution reduces row-wise dynamic overhead and can beat FP16 in a subset of tuned kernel shapes.
- Invalid claim: end-to-end LLM acceleration, SOTA quantization quality, or Tensor Core production runtime.
