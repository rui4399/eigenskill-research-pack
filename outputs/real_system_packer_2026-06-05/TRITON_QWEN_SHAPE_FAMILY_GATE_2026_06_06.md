# Triton Mixed-GEMM Evidence Gate

Status: **PASS**

This gate evaluates packed INT4/INT8 Triton kernel tuning outputs. It is not an end-to-end LLM runtime claim.

## Thresholds

- minimum valid configs: 96
- minimum FP16 wins: 8
- minimum best grouped/FP16 speedup: 2.0
- minimum row-wise wins: 70
- maximum grouped rel-L2: 0.2
- maximum guard VRAM ratio: 0.9

## Observed

- total configs: 96
- valid configs: 96
- FP16 wins: 10
- row-wise wins: 78
- best grouped/FP16 speedup: 2.7646927469778215
- best grouped/row-wise speedup: 5.179413564992068
- best compression vs FP16: 3.7440585009140768
- max grouped rel-L2: 0.14919528365135193
- max guard VRAM ratio: 0.4513556618819777

## Best FP16-Winning Config

```json
{
  "rows": 3072,
  "cols": 1024,
  "batch": 8,
  "high_every": 16,
  "block_m": 32,
  "block_n": 32,
  "block_k": 64,
  "grouped_mixed_ms": 0.03791610000121182,
  "torch_fp16_ms": 0.10482636666703608,
  "rowwise_mixed_ms": 0.10085883333393515,
  "grouped_speedup_vs_torch_fp16": 2.7646927469778215,
  "grouped_speedup_vs_rowwise": 2.6600529413814096,
  "compression_ratio_vs_fp16": 3.7034358047016274,
  "grouped_rel_l2": 0.13764163851737976,
  "guard_max_memory_used_ratio": 0.4366335418966998
}
```

## Failures

- none
