# PPL Result Summary

| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |
|---|---|---|---:|---:|---:|---|
| WikiText2-16 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 11.2830 | 0.000000 | 1.0000 | `{"16": 197}` |
| WikiText2-16 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 15.8383 | 0.339133 | 1.4037 | `{"4": 197}` |
| WikiText2-16 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 381.7257 | 3.521405 | 33.8319 | `{"3": 197}` |
| WikiText2-16 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_2p` | 13.7652 | 0.198844 | 1.2200 | `{"4": 137, "8": 60}` |
| C4-32 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 17.8832 | 0.000000 | 1.0000 | `{"16": 197}` |
| C4-32 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 23.5711 | 0.276159 | 1.3181 | `{"4": 197}` |
| C4-32 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 289.1918 | 2.783229 | 16.1712 | `{"3": 197}` |
| C4-32 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_2p` | 22.8859 | 0.246660 | 1.2797 | `{"4": 137, "8": 60}` |

## Scope

These values come from the fake weight-quantization evaluator. They are
quality diagnostics, not packed-runtime latency, memory, or energy results.
