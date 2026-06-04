# PPL Result Summary

| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |
|---|---|---|---:|---:|---:|---|
| WikiText2-128 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 13.1290 | 0.000000 | 1.0000 | `{"16": 197}` |
| WikiText2-128 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 17.4996 | 0.287354 | 1.3329 | `{"4": 197}` |
| WikiText2-128 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 232.6215 | 2.874587 | 17.7181 | `{"3": 197}` |
| WikiText2-128 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_2p` | 16.6503 | 0.237601 | 1.2682 | `{"4": 137, "8": 60}` |
| WikiText2-128 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_8p` | 16.0781 | 0.202631 | 1.2246 | `{"4": 136, "8": 61}` |
| WikiText2-128 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_consensus_4to8` | 16.1356 | 0.206202 | 1.2290 | `{"4": 132, "8": 65}` |

## Scope

These values come from the fake weight-quantization evaluator. They are
quality diagnostics, not packed-runtime latency, memory, or energy results.
