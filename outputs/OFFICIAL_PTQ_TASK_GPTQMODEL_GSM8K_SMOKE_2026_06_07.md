# Chat Task Benchmark

Model: `outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model`
Tasks: `4`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 4 | 0.0000 | 7.2988 | 0.551946 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `30` |
| baseline | `gsm8k_1` | `number` | false | `3` | `10` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `20%` |
| baseline | `gsm8k_3` | `number` | false | `540` | `180` |
