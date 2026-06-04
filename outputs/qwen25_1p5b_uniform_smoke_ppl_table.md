# PPL Result Summary

| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |
|---|---|---|---:|---:|---:|---|
| WikiText2-16 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 11.2830 | 0.000000 | 1.0000 | `{"16": 197}` |
| WikiText2-16 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 15.8383 | 0.339133 | 1.4037 | `{"4": 197}` |
| WikiText2-16 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 381.7257 | 3.521405 | 33.8319 | `{"3": 197}` |

## Scope

These values come from the fake weight-quantization evaluator. They are
quality diagnostics, not packed-runtime latency, memory, or energy results.
