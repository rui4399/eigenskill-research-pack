# PPL Result Summary

| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |
|---|---|---|---:|---:|---:|---|
| default_prompts_8 | `Qwen/Qwen3-0.6B` | `fp16` | 285.9696 | 0.000000 | 1.0000 | `{"16": 197}` |
| default_prompts_8 | `Qwen/Qwen3-0.6B` | `uniform_int4` | 287.3424 | 0.004789 | 1.0048 | `{"4": 197}` |
| default_prompts_8 | `Qwen/Qwen3-0.6B` | `uniform_int3` | 2295.4069 | 2.082780 | 8.0268 | `{"3": 197}` |
| default_prompts_8 | `Qwen/Qwen3-0.6B` | `allocation_loss_sensitive_4to8` | 225.0283 | -0.239659 | 0.7869 | `{"4": 153, "8": 44}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `fp16` | 36.1380 | 0.000000 | 1.0000 | `{"16": 197}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `uniform_int4` | 52.9352 | 0.381723 | 1.4648 | `{"4": 197}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `uniform_int3` | 832.2634 | 3.136804 | 23.0301 | `{"3": 197}` |
| c4_64 | `Qwen/Qwen3-0.6B` | `allocation_loss_sensitive_4to8` | 47.5872 | 0.275218 | 1.3168 | `{"4": 153, "8": 44}` |

## Scope

These values come from the fake weight-quantization evaluator. They are
quality diagnostics, not packed-runtime latency, memory, or energy results.
