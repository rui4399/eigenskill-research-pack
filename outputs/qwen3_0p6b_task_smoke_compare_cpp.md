# Task Accuracy Comparison

Baseline: `fp16`

| label | model | total | exact | accuracy | delta vs baseline | retention |
|---|---|---:|---:|---:|---:|---:|
| `fp16` | `Qwen/Qwen3-0.6B` | 5 | 3 | 0.6000 | 0.0000 | 1.0000 |

## Per-Task Accuracy

| task | baseline accuracy | fp16 |
|---|---:|---:|
| gsm8k_smoke | 0.5000 | 0.5000 |
| ifeval_smoke | 0.0000 | 0.0000 |
| mmlu_smoke | 1.0000 | 1.0000 |

## Interpretation

Use this C++ report as the task-level gate for future quantized runs. A paper-facing result should preserve task accuracy against FP16 while also beating uniform INT4 and any budget-matched random or structural allocation baselines.
