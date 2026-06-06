# Triton Mixed-GEMM Cross-Shape Tuning Summary

This report aggregates packed INT4/INT8 Triton GEMM tuning runs across Qwen-like Linear shapes.
It is a kernel benchmark summary, not an end-to-end transformer runtime result.

## Aggregate

- total configs: 96
- valid configs: 96
- configs faster than torch FP16: 10
- configs faster than row-wise dynamic mixed path: 78
- grouped/FP16 speedup median: 0.3664
- grouped/FP16 speedup p90: 1.0202
- grouped/FP16 speedup max: 2.7647
- grouped/row-wise speedup median: 1.7319
- grouped/row-wise speedup max: 5.1794
- compression vs FP16 median: 3.7034x
- grouped rel-L2 median: 0.1380
- max guard VRAM ratio: 0.4514

## Shape Summary

| shape | batch | high_every | configs | FP16 wins | row-wise wins | median grouped/FP16 | max grouped/FP16 | median grouped/row-wise | max grouped/row-wise | median rel-L2 | max VRAM ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1024x1024 | 8 | 16 | 12 | 2 | 4 | 0.3668 | 2.3350 | 0.9255 | 1.3910 | 0.1372 | 0.4315 |
| 1024x1024 | 16 | 16 | 12 | 0 | 12 | 0.3629 | 0.5394 | 1.5658 | 1.7934 | 0.1389 | 0.4321 |
| 1024x3072 | 8 | 16 | 12 | 3 | 9 | 0.3308 | 2.0627 | 1.3594 | 2.4468 | 0.1491 | 0.4369 |
| 1024x3072 | 16 | 16 | 12 | 0 | 9 | 0.3440 | 0.5302 | 1.9830 | 2.9196 | 0.1492 | 0.4363 |
| 2048x1024 | 8 | 16 | 12 | 1 | 9 | 0.3730 | 1.3194 | 1.6032 | 2.2437 | 0.1382 | 0.4381 |
| 2048x1024 | 16 | 16 | 12 | 1 | 12 | 0.3843 | 1.6543 | 3.0704 | 3.5292 | 0.1373 | 0.4514 |
| 3072x1024 | 8 | 16 | 12 | 1 | 11 | 0.3955 | 2.7647 | 2.2171 | 3.3826 | 0.1376 | 0.4385 |
| 3072x1024 | 16 | 16 | 12 | 2 | 12 | 0.3981 | 2.0067 | 4.4445 | 5.1794 | 0.1379 | 0.4369 |

## Top Grouped vs Torch FP16 Cases

| rank | shape | batch | high_every | BM | BN | BK | grouped ms | torch FP16 ms | speedup | compression vs FP16 | rel-L2 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3072x1024 | 8 | 16 | 32 | 32 | 64 | 0.037916 | 0.104826 | 2.7647 | 3.7034x | 0.1376 |
| 2 | 1024x1024 | 8 | 16 | 32 | 32 | 64 | 0.035458 | 0.082795 | 2.3350 | 3.7034x | 0.1372 |
| 3 | 1024x3072 | 8 | 16 | 16 | 16 | 128 | 0.039790 | 0.082072 | 2.0627 | 3.7441x | 0.1491 |
| 4 | 3072x1024 | 16 | 16 | 16 | 16 | 128 | 0.033276 | 0.066776 | 2.0067 | 3.7034x | 0.1379 |
| 5 | 2048x1024 | 16 | 16 | 16 | 8 | 128 | 0.037990 | 0.062845 | 1.6543 | 3.7034x | 0.1373 |
| 6 | 1024x3072 | 8 | 16 | 32 | 16 | 64 | 0.037572 | 0.061032 | 1.6244 | 3.7441x | 0.1491 |
| 7 | 1024x3072 | 8 | 16 | 16 | 32 | 128 | 0.040640 | 0.065274 | 1.6061 | 3.7441x | 0.1491 |
| 8 | 1024x1024 | 8 | 16 | 16 | 16 | 64 | 0.060078 | 0.083927 | 1.3970 | 3.7034x | 0.1372 |
| 9 | 2048x1024 | 8 | 16 | 32 | 8 | 128 | 0.036835 | 0.048601 | 1.3194 | 3.7034x | 0.1382 |
| 10 | 3072x1024 | 16 | 16 | 32 | 16 | 64 | 0.045761 | 0.048899 | 1.0686 | 3.7034x | 0.1379 |
| 11 | 1024x1024 | 8 | 16 | 16 | 8 | 64 | 0.033209 | 0.032271 | 0.9718 | 3.7034x | 0.1372 |
| 12 | 3072x1024 | 8 | 16 | 16 | 32 | 128 | 0.034937 | 0.025644 | 0.7340 | 3.7034x | 0.1376 |

## Claim Boundary

- Valid claim: grouped packed execution reduces row-wise dynamic overhead and can beat FP16 in a subset of tuned kernel shapes.
- Invalid claim: end-to-end LLM acceleration, SOTA quantization quality, or Tensor Core production runtime.
