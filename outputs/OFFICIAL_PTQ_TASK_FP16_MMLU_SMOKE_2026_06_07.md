# Chat Task Benchmark

Model: `Qwen/Qwen2.5-0.5B-Instruct`
Tasks: `4`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 1 / 4 | 0.2500 | 25.2172 | 0.359683 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | false | `B` | `C. 2` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `To find the index of \( \langle` |
| baseline | `mmlu_2` | `mcq` | false | `D` | `C. 0,1` |
| baseline | `mmlu_3` | `mcq` | true | `B` | `B. False, False` |
