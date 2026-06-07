# Chat Task Benchmark

Model: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model`
Tasks: `20`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 20 | 0.0000 | 5.0626 | 0.493040 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `34` |
| baseline | `gsm8k_1` | `number` | false | `3` | `10` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `25` |
| baseline | `gsm8k_3` | `number` | false | `540` | `180` |
| baseline | `gsm8k_4` | `number` | false | `20` | `40` |
| baseline | `gsm8k_5` | `number` | false | `64` | `24` |
| baseline | `gsm8k_6` | `number` | false | `260` | `140` |
| baseline | `gsm8k_7` | `number` | false | `160` | `15` |
| baseline | `gsm8k_8` | `number` | false | `45` | `15` |
| baseline | `gsm8k_9` | `number` | false | `460` | `36` |
| baseline | `gsm8k_10` | `number` | false | `366` | `120` |
| baseline | `gsm8k_11` | `number` | false | `694` | `144` |
| baseline | `gsm8k_12` | `number` | false | `13` | `2` |
| baseline | `gsm8k_13` | `number` | false | `18` | `10` |
| baseline | `gsm8k_14` | `number` | false | `60` | `10` |
| baseline | `gsm8k_15` | `number` | false | `125` | `375` |
| baseline | `gsm8k_16` | `number` | false | `230` | `240` |
| baseline | `gsm8k_17` | `number` | false | `57500` | `4900` |
| baseline | `gsm8k_18` | `number` | false | `7` | `12` |
| baseline | `gsm8k_19` | `number` | false | `6` | `5` |
