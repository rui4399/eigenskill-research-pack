# PPL Result Summary

| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |
|---|---|---|---:|---:|---:|---|
| WikiText2-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 12.8516 | 0.000000 | 1.0000 | `{"16": 197}` |
| WikiText2-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 17.2441 | 0.294002 | 1.3418 | `{"4": 197}` |
| WikiText2-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 273.9454 | 3.059463 | 21.3161 | `{"3": 197}` |
| WikiText2-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_2p` | 16.1788 | 0.230234 | 1.2589 | `{"4": 137, "8": 60}` |
| WikiText2-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_8p` | 15.7520 | 0.203499 | 1.2257 | `{"4": 136, "8": 61}` |
| WikiText2-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_consensus_4to8` | 15.7966 | 0.206327 | 1.2292 | `{"4": 132, "8": 65}` |
| C4-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `fp16` | 18.1669 | 0.000000 | 1.0000 | `{"16": 197}` |
| C4-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int4` | 23.9949 | 0.278239 | 1.3208 | `{"4": 197}` |
| C4-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `uniform_int3` | 293.8201 | 2.783365 | 16.1734 | `{"3": 197}` |
| C4-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_2p` | 23.2682 | 0.247484 | 1.2808 | `{"4": 137, "8": 60}` |
| C4-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_4to8_8p` | 22.3620 | 0.207762 | 1.2309 | `{"4": 136, "8": 61}` |
| C4-64 | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | `loss_sensitive_consensus_4to8` | 22.4891 | 0.213428 | 1.2379 | `{"4": 132, "8": 65}` |

## Scope

These values come from the fake weight-quantization evaluator. They are
quality diagnostics, not packed-runtime latency, memory, or energy results.
