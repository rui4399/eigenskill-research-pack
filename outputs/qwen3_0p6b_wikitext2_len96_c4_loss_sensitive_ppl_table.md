# PPL Result Summary

| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |
|---|---|---|---:|---:|---:|---|
| wikitext2_64_len96 | `Qwen/Qwen3-0.6B` | `fp16` | 33.9865 | 0.000000 | 1.0000 | `{"16": 197}` |
| wikitext2_64_len96 | `Qwen/Qwen3-0.6B` | `uniform_int4` | 54.6542 | 0.475062 | 1.6081 | `{"4": 197}` |
| wikitext2_64_len96 | `Qwen/Qwen3-0.6B` | `uniform_int3` | 951.6108 | 3.332193 | 27.9997 | `{"3": 197}` |
| wikitext2_64_len96 | `Qwen/Qwen3-0.6B` | `allocation_loss_sensitive_4to8` | 49.5352 | 0.376721 | 1.4575 | `{"4": 153, "8": 44}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `fp16` | 36.1380 | 0.000000 | 1.0000 | `{"16": 197}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `uniform_int4` | 52.9352 | 0.381723 | 1.4648 | `{"4": 197}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `uniform_int3` | 832.2634 | 3.136804 | 23.0301 | `{"3": 197}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `allocation_loss_sensitive_4to8` | 47.5872 | 0.275218 | 1.3168 | `{"4": 153, "8": 44}` |

## Scope

These values come from the fake weight-quantization evaluator. They are
quality diagnostics, not packed-runtime latency, memory, or energy results.
