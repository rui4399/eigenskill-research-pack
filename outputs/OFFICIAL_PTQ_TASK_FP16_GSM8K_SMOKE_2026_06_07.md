# Chat Task Benchmark

Model: `Qwen/Qwen2.5-0.5B-Instruct`
Tasks: `4`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 4 | 0.0000 | 20.5511 | 0.410765 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `To determine how much Janet makes every day at the farmers' market, we need` |
| baseline | `gsm8k_1` | `number` | false | `3` | `4` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `$35,000` |
| baseline | `gsm8k_3` | `number` | false | `540` | `1800` |
