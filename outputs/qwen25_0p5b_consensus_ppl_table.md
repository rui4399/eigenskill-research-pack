# PPL Result Summary

| dataset | model | config | PPL | delta NLL | ratio vs FP16 | bit hist |
|---|---|---|---:|---:|---:|---|
| WikiText2-128 | `Qwen/Qwen2.5-0.5B-Instruct` | `fp16` | 17.4294 | 0.000000 | 1.0000 | `{"16": 169}` |
| WikiText2-128 | `Qwen/Qwen2.5-0.5B-Instruct` | `uniform_int4` | 27.7411 | 0.464758 | 1.5916 | `{"4": 169}` |
| WikiText2-128 | `Qwen/Qwen2.5-0.5B-Instruct` | `uniform_int3` | 514.0862 | 3.384234 | 29.4954 | `{"3": 169}` |
| WikiText2-128 | `Qwen/Qwen2.5-0.5B-Instruct` | `loss_sensitive_4to8_2p` | 22.4605 | 0.253601 | 1.2887 | `{"4": 114, "8": 55}` |
| WikiText2-128 | `Qwen/Qwen2.5-0.5B-Instruct` | `loss_sensitive_4to8_8p` | 21.9762 | 0.231805 | 1.2609 | `{"4": 112, "8": 57}` |
| WikiText2-128 | `Qwen/Qwen2.5-0.5B-Instruct` | `loss_sensitive_consensus_4to8` | 22.0848 | 0.236732 | 1.2671 | `{"4": 109, "8": 60}` |
| C4-64 | `Qwen/Qwen2.5-0.5B-Instruct` | `fp16` | 23.9539 | 0.000000 | 1.0000 | `{"16": 169}` |
| C4-64 | `Qwen/Qwen2.5-0.5B-Instruct` | `uniform_int4` | 36.5128 | 0.421531 | 1.5243 | `{"4": 169}` |
| C4-64 | `Qwen/Qwen2.5-0.5B-Instruct` | `uniform_int3` | 779.2680 | 3.482223 | 32.5319 | `{"3": 169}` |
| C4-64 | `Qwen/Qwen2.5-0.5B-Instruct` | `loss_sensitive_4to8_2p` | 31.2151 | 0.264769 | 1.3031 | `{"4": 114, "8": 55}` |
| C4-64 | `Qwen/Qwen2.5-0.5B-Instruct` | `loss_sensitive_4to8_8p` | 30.7970 | 0.251285 | 1.2857 | `{"4": 112, "8": 57}` |
| C4-64 | `Qwen/Qwen2.5-0.5B-Instruct` | `loss_sensitive_consensus_4to8` | 30.8017 | 0.251437 | 1.2859 | `{"4": 109, "8": 60}` |

## Scope

These values come from the fake weight-quantization evaluator. They are
quality diagnostics, not packed-runtime latency, memory, or energy results.
