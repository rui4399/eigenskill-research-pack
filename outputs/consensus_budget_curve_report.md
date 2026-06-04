# Consensus Budget Curve

This table evaluates the same cross-dataset consensus allocator at multiple
average-bit budgets. It is a short-slice PyTorch fake-quant diagnostic,
not a packed runtime or hardware result.

| dataset | model | config | avg bits | PPL | PPL gain vs uniform INT4 | uniform gap closed | bit hist |
|---|---|---|---:|---:|---:|---:|---|
| Qwen3-1.7B-WikiText2-64 | `Qwen/Qwen3-1.7B` | `fp16` | 16.0000 | 22.4960 | 9.3394 | 1.0000 | `{"16": 197}` |
| Qwen3-1.7B-WikiText2-64 | `Qwen/Qwen3-1.7B` | `uniform_int4` | 4.0000 | 31.8353 | 0.0000 | 0.0000 | `{"4": 197}` |
| Qwen3-1.7B-WikiText2-64 | `Qwen/Qwen3-1.7B` | `consensus_budget_4p25` | 4.2487 | 28.0753 | 3.7600 | 0.4026 | `{"4": 165, "8": 32}` |
| Qwen3-1.7B-WikiText2-64 | `Qwen/Qwen3-1.7B` | `consensus_budget_4p50` | 4.4973 | 27.3180 | 4.5173 | 0.4837 | `{"4": 147, "8": 50}` |
| Qwen3-1.7B-WikiText2-64 | `Qwen/Qwen3-1.7B` | `consensus_budget_4p75` | 4.7460 | 26.6163 | 5.2191 | 0.5588 | `{"4": 130, "8": 67}` |
| Qwen3-1.7B-C4-64 | `Qwen/Qwen3-1.7B` | `fp16` | 16.0000 | 26.8745 | 5.5594 | 1.0000 | `{"16": 197}` |
| Qwen3-1.7B-C4-64 | `Qwen/Qwen3-1.7B` | `uniform_int4` | 4.0000 | 32.4338 | 0.0000 | 0.0000 | `{"4": 197}` |
| Qwen3-1.7B-C4-64 | `Qwen/Qwen3-1.7B` | `consensus_budget_4p25` | 4.2487 | 30.4752 | 1.9587 | 0.3523 | `{"4": 165, "8": 32}` |
| Qwen3-1.7B-C4-64 | `Qwen/Qwen3-1.7B` | `consensus_budget_4p50` | 4.4973 | 29.9230 | 2.5108 | 0.4516 | `{"4": 147, "8": 50}` |
| Qwen3-1.7B-C4-64 | `Qwen/Qwen3-1.7B` | `consensus_budget_4p75` | 4.7460 | 29.2500 | 3.1839 | 0.5727 | `{"4": 130, "8": 67}` |
| OLMo2-1B-WikiText2-64 | `allenai/OLMo-2-0425-1B-Instruct` | `fp16` | 16.0000 | 20.1585 | 3.9725 | 1.0000 | `{"16": 113}` |
| OLMo2-1B-WikiText2-64 | `allenai/OLMo-2-0425-1B-Instruct` | `uniform_int4` | 4.0000 | 24.1311 | 0.0000 | 0.0000 | `{"4": 113}` |
| OLMo2-1B-WikiText2-64 | `allenai/OLMo-2-0425-1B-Instruct` | `consensus_budget_4p25` | 4.2492 | 23.2779 | 0.8532 | 0.2148 | `{"4": 97, "8": 16}` |
| OLMo2-1B-WikiText2-64 | `allenai/OLMo-2-0425-1B-Instruct` | `consensus_budget_4p50` | 4.4984 | 22.5113 | 1.6198 | 0.4078 | `{"4": 87, "8": 26}` |
| OLMo2-1B-WikiText2-64 | `allenai/OLMo-2-0425-1B-Instruct` | `consensus_budget_4p75` | 4.7475 | 22.1464 | 1.9846 | 0.4996 | `{"4": 80, "8": 33}` |
| OLMo2-1B-C4-64 | `allenai/OLMo-2-0425-1B-Instruct` | `fp16` | 16.0000 | 34.0696 | 4.7329 | 1.0000 | `{"16": 113}` |
| OLMo2-1B-C4-64 | `allenai/OLMo-2-0425-1B-Instruct` | `uniform_int4` | 4.0000 | 38.8025 | 0.0000 | 0.0000 | `{"4": 113}` |
| OLMo2-1B-C4-64 | `allenai/OLMo-2-0425-1B-Instruct` | `consensus_budget_4p25` | 4.2492 | 37.9817 | 0.8208 | 0.1734 | `{"4": 97, "8": 16}` |
| OLMo2-1B-C4-64 | `allenai/OLMo-2-0425-1B-Instruct` | `consensus_budget_4p50` | 4.4984 | 37.2835 | 1.5190 | 0.3209 | `{"4": 87, "8": 26}` |
| OLMo2-1B-C4-64 | `allenai/OLMo-2-0425-1B-Instruct` | `consensus_budget_4p75` | 4.7475 | 37.1610 | 1.6415 | 0.3468 | `{"4": 80, "8": 33}` |

## Interpretation

A useful allocation curve should improve as more high-precision budget is
released. Non-monotonic points should be treated as calibration noise or
module-interaction evidence rather than hidden as failed runs.
