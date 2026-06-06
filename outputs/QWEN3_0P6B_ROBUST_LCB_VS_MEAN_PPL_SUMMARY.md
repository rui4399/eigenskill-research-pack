# PPL Result Summary

| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |
|---|---|---|---:|---:|---:|---|
| wikitext2_64_len96 | `Qwen/Qwen3-0.6B` | `fp16` | 33.9865 | 0.000000 | 1.0000 | `{"16": 197}` |
| wikitext2_64_len96 | `Qwen/Qwen3-0.6B` | `uniform_int4` | 54.6542 | 0.475062 | 1.6081 | `{"4": 197}` |
| wikitext2_64_len96 | `Qwen/Qwen3-0.6B` | `wikitext_c4_mean_consensus` | 45.6559 | 0.295168 | 1.3434 | `{"4": 151, "8": 46}` |
| wikitext2_64_len96 | `Qwen/Qwen3-0.6B` | `wikitext_c4_robust_lcb` | 49.2223 | 0.370384 | 1.4483 | `{"4": 159, "8": 38}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `fp16` | 36.1380 | 0.000000 | 1.0000 | `{"16": 197}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `uniform_int4` | 52.9352 | 0.381723 | 1.4648 | `{"4": 197}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `wikitext_c4_mean_consensus` | 44.9290 | 0.217738 | 1.2433 | `{"4": 151, "8": 46}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `wikitext_c4_robust_lcb` | 47.1293 | 0.265550 | 1.3041 | `{"4": 159, "8": 38}` |

## Scope

These values come from the fake weight-quantization evaluator. They are
quality diagnostics, not packed-runtime latency, memory, or energy results.
