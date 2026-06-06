# End-to-End Generation System Metrics

This report summarizes measured generation artifacts. It does not create a new benchmark run.
Use it to keep TTFT, tokens/s, memory, and package-compression claims tied to concrete JSON files.

Baseline for ratios: `same_loader_warm_16tok`

| case | mode | max new | replaced | TTFT s | TPS | peak GPU MiB | TTFT speedup | TPS ratio | memory delta MiB | compression vs FP32 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| direct_fp16_cold_16tok | n/a | 16 | 0 | 1.3658 | 7.3098 | 2028.1396 | 0.0254 | 0.2918 | 854.8403 | n/a |
| same_loader_cold_16tok | hf_same_loader | 16 | 0 | 0.9489 | 9.5277 | 1173.2993 | 0.0366 | 0.3803 | 0.0000 | n/a |
| same_loader_warm_16tok | hf_same_loader | 16 | 0 | 0.0347 | 25.0523 | 1173.2993 | 1.0000 | 1.0000 | 0.0000 | n/a |
| cached_3mod_cold_16tok | cached_dequant | 16 | 3 | 0.8583 | 9.1542 | 1175.2993 | 0.0404 | 0.3654 | 2.0000 | 6.1682 |
| cached_3mod_warm_16tok | cached | 16 | 3 | 0.0320 | 28.8295 | 1175.2993 | 1.0831 | 1.1508 | 2.0000 | 6.1682 |
| triton_3mod_cold_16tok | triton_grouped | 16 | 3 | 1.9611 | 4.9957 | 1169.8462 | 0.0177 | 0.1994 | -3.4531 | 6.1682 |
| fused_qkv_3layer_warm_16tok | hf_generation_with_fused_esmp_qkv_replacement | 16 | 3 | 0.0315 | 25.8158 | 1156.4868 | 1.1022 | 1.0305 | -16.8125 | 7.0778 |

## Claim Boundary

- Valid claim: these JSON artifacts record local TTFT, tokens/s, peak allocated GPU memory, and selected-module compression for the listed smoke cases.
- Invalid claim: these numbers prove production acceleration, mobile latency, energy savings, or model-quality retention.

## Source Files

- `direct_fp16_cold_16tok`: `outputs\real_system_packer_2026-06-05\qwen3_fp16_16tok_latency.json`
- `same_loader_cold_16tok`: `outputs\real_system_packer_2026-06-05\qwen3_same_loader_16tok_latency.json`
- `same_loader_warm_16tok`: `outputs\real_system_packer_2026-06-05\qwen3_same_loader_16tok_warm_latency.json`
- `cached_3mod_cold_16tok`: `outputs\real_system_packer_2026-06-05\qwen3_esmp_swapped_3mod_cached_latency.json`
- `cached_3mod_warm_16tok`: `outputs\real_system_packer_2026-06-05\qwen3_esmp_swapped_3mod_cached_warm_latency.json`
- `triton_3mod_cold_16tok`: `outputs\real_system_packer_2026-06-05\qwen3_esmp_swapped_3mod_triton_latency.json`
- `fused_qkv_3layer_warm_16tok`: `outputs\real_system_packer_2026-06-05\qwen3_fused_qkv_generation_3layer_16tok.json`
