# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `20`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 2 / 20 | 0.1000 | 14.5865 | 0.271346 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `16` |
| baseline | `gsm8k_1` | `number` | false | `3` | `6` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `170000` |
| baseline | `gsm8k_3` | `number` | false | `540` | `60` |
| baseline | `gsm8k_4` | `number` | false | `20` | `100` |
| baseline | `gsm8k_5` | `number` | false | `64` | `80` |
| baseline | `gsm8k_6` | `number` | false | `260` | `160` |
| baseline | `gsm8k_7` | `number` | false | `160` | `100` |
| baseline | `gsm8k_8` | `number` | false | `45` | `1200` |
| baseline | `gsm8k_9` | `number` | false | `460` | `540` |
| baseline | `gsm8k_10` | `number` | false | `366` | `330` |
| baseline | `gsm8k_11` | `number` | false | `694` | `684` |
| baseline | `gsm8k_12` | `number` | true | `13` | `13` |
| baseline | `gsm8k_13` | `number` | false | `18` | `20` |
| baseline | `gsm8k_14` | `number` | false | `60` | `35` |
| baseline | `gsm8k_15` | `number` | false | `125` | `8000` |
| baseline | `gsm8k_16` | `number` | false | `230` | `160` |
| baseline | `gsm8k_17` | `number` | false | `57500` | `104000` |
| baseline | `gsm8k_18` | `number` | false | `7` | `12` |
| baseline | `gsm8k_19` | `number` | true | `6` | `6` |
