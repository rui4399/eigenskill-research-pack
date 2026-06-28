# Chat Task Benchmark

Model: `/mnt/e/models/Qwen2.5-7B-Instruct-AWQ`
Tasks: `1`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 1 | 0.0000 | 0.0640 | 15.616679 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | false | `B` | `D` |
