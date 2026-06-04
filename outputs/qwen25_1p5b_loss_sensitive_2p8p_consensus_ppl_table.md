# PPL Result Summary

| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |
|---|---|---|---:|---:|---:|---|
| WikiText2-16-2p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 11.2830 | 0.000000 | 1.0000 | `{"16": 197}` |
| WikiText2-16-2p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 15.8383 | 0.339133 | 1.4037 | `{"4": 197}` |
| WikiText2-16-2p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 381.7257 | 3.521405 | 33.8319 | `{"3": 197}` |
| WikiText2-16-2p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_2p` | 13.7652 | 0.198844 | 1.2200 | `{"4": 137, "8": 60}` |
| C4-32-2p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 17.8832 | 0.000000 | 1.0000 | `{"16": 197}` |
| C4-32-2p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 23.5711 | 0.276159 | 1.3181 | `{"4": 197}` |
| C4-32-2p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 289.1918 | 2.783229 | 16.1712 | `{"3": 197}` |
| C4-32-2p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_2p` | 22.8859 | 0.246660 | 1.2797 | `{"4": 137, "8": 60}` |
| WikiText2-16-8p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 11.2830 | 0.000000 | 1.0000 | `{"16": 197}` |
| WikiText2-16-8p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 15.8383 | 0.339133 | 1.4037 | `{"4": 197}` |
| WikiText2-16-8p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 381.7257 | 3.521405 | 33.8319 | `{"3": 197}` |
| WikiText2-16-8p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_limit8` | 13.7622 | 0.198625 | 1.2197 | `{"4": 136, "8": 61}` |
| C4-32-8p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 17.8832 | 0.000000 | 1.0000 | `{"16": 197}` |
| C4-32-8p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 23.5711 | 0.276159 | 1.3181 | `{"4": 197}` |
| C4-32-8p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 289.1918 | 2.783229 | 16.1712 | `{"3": 197}` |
| C4-32-8p | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_limit8` | 21.9642 | 0.205554 | 1.2282 | `{"4": 136, "8": 61}` |
| WikiText2-16-consensus | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 11.2830 | 0.000000 | 1.0000 | `{"16": 197}` |
| WikiText2-16-consensus | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 15.8383 | 0.339133 | 1.4037 | `{"4": 197}` |
| WikiText2-16-consensus | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 381.7257 | 3.521405 | 33.8319 | `{"3": 197}` |
| WikiText2-16-consensus | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_consensus_4to8` | 13.7140 | 0.195119 | 1.2155 | `{"4": 132, "8": 65}` |
| C4-32-consensus | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 17.8832 | 0.000000 | 1.0000 | `{"16": 197}` |
| C4-32-consensus | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 23.5711 | 0.276159 | 1.3181 | `{"4": 197}` |
| C4-32-consensus | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 289.1918 | 2.783229 | 16.1712 | `{"3": 197}` |
| C4-32-consensus | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_consensus_4to8` | 22.1526 | 0.214092 | 1.2387 | `{"4": 132, "8": 65}` |

## Scope

These values come from the fake weight-quantization evaluator. They are
quality diagnostics, not packed-runtime latency, memory, or energy results.
