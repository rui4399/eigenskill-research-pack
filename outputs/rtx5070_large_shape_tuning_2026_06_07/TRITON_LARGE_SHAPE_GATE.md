# Triton Mixed-GEMM Evidence Gate

Status: **FAIL**

This gate evaluates packed INT4/INT8 Triton kernel tuning outputs. It is not an end-to-end LLM runtime claim.

## Thresholds

- minimum valid configs: 27
- minimum FP16 wins: 0
- minimum best grouped/FP16 speedup: 0.7
- minimum row-wise wins: 20
- maximum grouped rel-L2: 0.2
- maximum guard VRAM ratio: 0.85

## Observed

- total configs: 27
- valid configs: 27
- FP16 wins: 0
- row-wise wins: 27
- best grouped/FP16 speedup: 0.677622568924967
- best grouped/row-wise speedup: 19.368162649233327
- best compression vs FP16: 3.7491990846681924
- max grouped rel-L2: 0.1522691398859024
- max guard VRAM ratio: 0.7293583609373083

## Best FP16-Winning Config

```json
{
  "rows": 4096,
  "cols": 4096,
  "batch": 128,
  "high_every": 16,
  "block_m": 32,
  "block_n": 32,
  "block_k": 64,
  "grouped_mixed_ms": 0.19398473333325228,
  "torch_fp16_ms": 0.1314484333335031,
  "rowwise_mixed_ms": 3.757127866666584,
  "grouped_speedup_vs_torch_fp16": 0.677622568924967,
  "grouped_speedup_vs_rowwise": 19.368162649233327,
  "compression_ratio_vs_fp16": 3.7491990846681924,
  "grouped_rel_l2": 0.1522691398859024,
  "guard_max_memory_used_ratio": 0.7293583609373083
}
```

## Failures

- best grouped/FP16 speedup 0.677622568924967 < 0.7
