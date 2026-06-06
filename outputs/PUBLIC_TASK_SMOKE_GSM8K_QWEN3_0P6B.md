# Chat Task Benchmark

Model: `Qwen/Qwen3-0.6B`
Tasks: `4`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 4 | 0.0000 | 22.8711 | 0.358800 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `<think>  </think>  Janet’s ducks lay 16 eggs per day. She eats 3 eggs for breakfast and` |
| baseline | `gsm8k_1` | `number` | false | `3` | `<think>  </think>  A robe takes 2 bolts of blue fiber and half that much white fiber. Half of 2` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `<think>  </think>  The original value of the house is $80,000. The value increased by ` |
| baseline | `gsm8k_3` | `number` | false | `540` | `<think>  </think>  James runs 60 meters per sprint and does 3 sprints a week.   So,` |
