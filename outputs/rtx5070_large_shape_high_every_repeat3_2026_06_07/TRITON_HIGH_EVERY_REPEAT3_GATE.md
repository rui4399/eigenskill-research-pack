# Triton Mixed-GEMM Evidence Gate

Status: **PASS**

This gate evaluates packed INT4/INT8 Triton kernel tuning outputs. It is not an end-to-end LLM runtime claim.

## Thresholds

- minimum valid configs: 8
- minimum FP16 wins: 0
- minimum best grouped/FP16 speedup: 0.6
- minimum row-wise wins: 8
- maximum grouped rel-L2: 0.2
- maximum guard VRAM ratio: 0.85

## Observed

- total configs: 8
- valid configs: 8
- FP16 wins: 0
- row-wise wins: 8
- best grouped/FP16 speedup: 0.6645724893135952
- best grouped/row-wise speedup: 17.727964594545025
- best compression vs FP16: 3.9214935375777884
- max grouped rel-L2: 0.15593664348125458
- max guard VRAM ratio: 0.5220218378113115

## Best FP16-Winning Config

```json
{
  "rows": 4096,
  "cols": 4096,
  "batch": 128,
  "high_every": 64,
  "block_m": 32,
  "block_n": 64,
  "block_k": 64,
  "grouped_mixed_ms": 0.2219381166665831,
  "torch_fp16_ms": 0.14749396666668227,
  "rowwise_mixed_ms": 3.581312283333441,
  "grouped_speedup_vs_torch_fp16": 0.6645724893135952,
  "grouped_speedup_vs_rowwise": 16.136535432143162,
  "compression_ratio_vs_fp16": 3.9214935375777884,
  "grouped_rel_l2": 0.15593664348125458,
  "guard_max_memory_used_ratio": 0.5149061464850938
}
```

## Failures

- none
