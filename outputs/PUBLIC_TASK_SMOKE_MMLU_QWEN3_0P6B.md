# Chat Task Benchmark

Model: `Qwen/Qwen3-0.6B`
Tasks: `4`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 4 | 0.0000 | 20.8940 | 0.344514 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | false | `B` | `<think>  </think>  A. 0` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `<think>  </think>  A. 8` |
| baseline | `mmlu_2` | `mcq` | false | `D` | `<think>  </think>  C. 0` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `<think>  </think>  The correct answer is` |
