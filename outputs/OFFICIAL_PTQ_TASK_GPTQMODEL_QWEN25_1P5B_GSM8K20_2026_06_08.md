# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `20`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 1 / 20 | 0.0500 | 11.1966 | 0.389499 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `48` |
| baseline | `gsm8k_1` | `number` | false | `3` | `6` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `240000` |
| baseline | `gsm8k_3` | `number` | true | `540` | `540` |
| baseline | `gsm8k_4` | `number` | false | `20` | `40` |
| baseline | `gsm8k_5` | `number` | false | `64` | `480` |
| baseline | `gsm8k_6` | `number` | false | `260` | `160` |
| baseline | `gsm8k_7` | `number` | false | `160` | `1600` |
| baseline | `gsm8k_8` | `number` | false | `45` | `150` |
| baseline | `gsm8k_9` | `number` | false | `460` | `550` |
| baseline | `gsm8k_10` | `number` | false | `366` | `150` |
| baseline | `gsm8k_11` | `number` | false | `694` | `412` |
| baseline | `gsm8k_12` | `number` | false | `13` | `6` |
| baseline | `gsm8k_13` | `number` | false | `18` | `10` |
| baseline | `gsm8k_14` | `number` | false | `60` | `15%` |
| baseline | `gsm8k_15` | `number` | false | `125` | `13000` |
| baseline | `gsm8k_16` | `number` | false | `230` | `310` |
| baseline | `gsm8k_17` | `number` | false | `57500` | `64000` |
| baseline | `gsm8k_18` | `number` | false | `7` | `240` |
| baseline | `gsm8k_19` | `number` | false | `6` | `8` |
