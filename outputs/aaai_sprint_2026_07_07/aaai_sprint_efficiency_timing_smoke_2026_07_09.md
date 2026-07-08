# AAAI Sprint Efficiency Timing Smoke

Generated: 2026-07-09

measure_module_quant_sensitivity.py, 4 WikiText2 prompts, max_length 128, one Linear module, float16 CUDA, probe_bits=4, group_size=128, lowmem_row_chunk=16

| Model | Wall-clock seconds | Prompts | Measured modules | Tokens | Exit | Artifact |
|---|---:|---:|---:|---:|---:|---|
| 1p5b | 12.931 | 4 | 1 | 401 | 0 | `qwen25_1p5b_efficiency_timing_smoke_2026_07_09.json` |
| 3b | 15.102 | 4 | 1 | 401 | 0 | `qwen25_3b_efficiency_timing_smoke_2026_07_09.json` |
| 7b | 37.691 | 4 | 1 | 401 | 0 | `qwen25_7b_efficiency_timing_smoke_2026_07_09.json` |

## Boundary

This is a reproducible timing smoke across scales, not a full efficiency benchmark over all modules or full downstream evaluation.
