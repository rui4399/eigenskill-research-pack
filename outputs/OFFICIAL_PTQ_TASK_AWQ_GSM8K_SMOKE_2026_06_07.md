# Chat Task Benchmark

Model: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model`
Tasks: `4`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 4 | 0.0000 | 4.5937 | 0.724255 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `34` |
| baseline | `gsm8k_1` | `number` | false | `3` | `10` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `25` |
| baseline | `gsm8k_3` | `number` | false | `540` | `180` |
