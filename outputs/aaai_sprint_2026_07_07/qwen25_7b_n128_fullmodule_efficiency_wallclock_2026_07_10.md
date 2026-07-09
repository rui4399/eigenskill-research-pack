# Qwen2.5-7B n128 Full-Module Efficiency Wall-Clock

Generated: 2026-07-10

Boundary: wall-clock values are from completed local command runs for full-module Qwen2.5-7B n128 sensitivity. This is not a full downstream evaluation timing table and does not cover 14B fake-quant.

| Seed | Modules | Tool wall time sec | Script elapsed sec | Avg bits | Bit hist | Artifact |
|---:|---:|---:|---:|---:|---|---|
| 0 | 197 | 1246.1 | 1221.13 | 2.9977 | {'2': 101, '4': 96} | `qwen25_7b_wikitext2pool512_n128_seed0_sensitivity_2to4_budget3.json` |
| 1 | 197 | 1224.3 | 1203.97 | 2.9997 | {'2': 97, '4': 100} | `qwen25_7b_wikitext2pool512_n128_seed1_sensitivity_2to4_budget3.json` |

Mean tool wall time: `1235.2` seconds.
