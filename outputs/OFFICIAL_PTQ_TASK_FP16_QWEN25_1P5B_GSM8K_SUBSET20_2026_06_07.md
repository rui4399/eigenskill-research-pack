# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `20`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 2 / 20 | 0.1000 | 19.2592 | 0.194016 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `48` |
| baseline | `gsm8k_1` | `number` | false | `3` | `6` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `140000` |
| baseline | `gsm8k_3` | `number` | true | `540` | `540` |
| baseline | `gsm8k_4` | `number` | false | `20` | `30` |
| baseline | `gsm8k_5` | `number` | false | `64` | `800` |
| baseline | `gsm8k_6` | `number` | false | `260` | `180` |
| baseline | `gsm8k_7` | `number` | false | `160` | `360` |
| baseline | `gsm8k_8` | `number` | false | `45` | `150` |
| baseline | `gsm8k_9` | `number` | true | `460` | `460` |
| baseline | `gsm8k_10` | `number` | false | `366` | `240` |
| baseline | `gsm8k_11` | `number` | false | `694` | `194` |
| baseline | `gsm8k_12` | `number` | false | `13` | `24` |
| baseline | `gsm8k_13` | `number` | false | `18` | `16` |
| baseline | `gsm8k_14` | `number` | false | `60` | `15%` |
| baseline | `gsm8k_15` | `number` | false | `125` | `600` |
| baseline | `gsm8k_16` | `number` | false | `230` | `160` |
| baseline | `gsm8k_17` | `number` | false | `57500` | `46000` |
| baseline | `gsm8k_18` | `number` | false | `7` | `168` |
| baseline | `gsm8k_19` | `number` | false | `6` | `3` |
