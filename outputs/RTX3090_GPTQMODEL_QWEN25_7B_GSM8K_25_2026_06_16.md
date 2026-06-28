# Chat Task Benchmark

Model: `/mnt/e/models/Qwen2.5-7B-Instruct-GPTQ-Int4`
Tasks: `25`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 3 / 25 | 0.1200 | 11.0847 | 0.250194 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `15` |
| baseline | `gsm8k_1` | `number` | true | `3` | `3` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `270000` |
| baseline | `gsm8k_3` | `number` | false | `540` | `180` |
| baseline | `gsm8k_4` | `number` | false | `20` | `30` |
| baseline | `gsm8k_5` | `number` | false | `64` | `44` |
| baseline | `gsm8k_6` | `number` | false | `260` | `540` |
| baseline | `gsm8k_7` | `number` | false | `160` | `140` |
| baseline | `gsm8k_8` | `number` | false | `45` | `120` |
| baseline | `gsm8k_9` | `number` | false | `460` | `465` |
| baseline | `gsm8k_10` | `number` | false | `366` | `246` |
| baseline | `gsm8k_11` | `number` | false | `694` | `1494` |
| baseline | `gsm8k_12` | `number` | false | `13` | `15` |
| baseline | `gsm8k_13` | `number` | false | `18` | `15` |
| baseline | `gsm8k_14` | `number` | false | `60` | `55` |
| baseline | `gsm8k_15` | `number` | false | `125` | `137` |
| baseline | `gsm8k_16` | `number` | true | `230` | `230` |
| baseline | `gsm8k_17` | `number` | false | `57500` | `4600` |
| baseline | `gsm8k_18` | `number` | false | `7` | `12` |
| baseline | `gsm8k_19` | `number` | false | `6` | `3` |
| baseline | `gsm8k_20` | `number` | false | `15` | `16` |
| baseline | `gsm8k_21` | `number` | false | `14` | `19` |
| baseline | `gsm8k_22` | `number` | false | `7` | `5` |
| baseline | `gsm8k_23` | `number` | false | `8` | `16` |
| baseline | `gsm8k_24` | `number` | true | `26` | `26.00` |
