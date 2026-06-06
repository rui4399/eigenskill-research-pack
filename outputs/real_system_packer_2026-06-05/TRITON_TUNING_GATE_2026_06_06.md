# Triton Mixed-GEMM Evidence Gate

Status: **PASS**

This gate evaluates packed INT4/INT8 Triton kernel tuning outputs. It is not an end-to-end LLM runtime claim.

## Thresholds

- minimum valid configs: 24
- minimum FP16 wins: 2
- minimum best grouped/FP16 speedup: 1.2
- minimum row-wise wins: 20
- maximum grouped rel-L2: 0.2
- maximum guard VRAM ratio: 0.9

## Observed

- total configs: 24
- valid configs: 24
- FP16 wins: 2
- row-wise wins: 21
- best grouped/FP16 speedup: 1.654255104449623
- best grouped/row-wise speedup: 3.5291709906694066
- best compression vs FP16: 3.7034358047016274
- max grouped rel-L2: 0.13818664848804474
- max guard VRAM ratio: 0.4513556618819777

## Best FP16-Winning Config

```json
{
  "rows": 2048,
  "cols": 1024,
  "batch": 16,
  "high_every": 16,
  "block_m": 16,
  "block_n": 8,
  "block_k": 128,
  "grouped_mixed_ms": 0.03798966666674156,
  "torch_fp16_ms": 0.06284459999979693,
  "rowwise_mixed_ms": 0.12005316666687804,
  "grouped_speedup_vs_torch_fp16": 1.654255104449623,
  "grouped_speedup_vs_rowwise": 3.1601531995535987,
  "compression_ratio_vs_fp16": 3.7034358047016274,
  "grouped_rel_l2": 0.13734383881092072,
  "guard_max_memory_used_ratio": 0.44301312722365355
}
```

## Failures

- none
