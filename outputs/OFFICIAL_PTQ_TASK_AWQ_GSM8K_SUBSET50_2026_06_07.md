# Chat Task Benchmark

Model: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model`
Tasks: `50`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 50 | 0.0000 | 5.0996 | 0.411649 |

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
| baseline | `gsm8k_20` | `number` | false | `15` | `3` |
| baseline | `gsm8k_21` | `number` | false | `14` | `4` |
| baseline | `gsm8k_22` | `number` | false | `7` | `15` |
| baseline | `gsm8k_23` | `number` | false | `8` | `3` |
| baseline | `gsm8k_24` | `number` | false | `26` | `46` |
| baseline | `gsm8k_25` | `number` | false | `2` | `16` |
| baseline | `gsm8k_26` | `number` | false | `243` | `89` |
| baseline | `gsm8k_27` | `number` | false | `16` | `240` |
| baseline | `gsm8k_28` | `number` | false | `25` | `8` |
| baseline | `gsm8k_29` | `number` | false | `104` | `150` |
| baseline | `gsm8k_30` | `number` | false | `109` | `5` |
| baseline | `gsm8k_31` | `number` | false | `80` | `14` |
| baseline | `gsm8k_32` | `number` | false | `35` | `20` |
| baseline | `gsm8k_33` | `number` | false | `70` | `29` |
| baseline | `gsm8k_34` | `number` | false | `23` | `13` |
| baseline | `gsm8k_35` | `number` | false | `9` | `18` |
| baseline | `gsm8k_36` | `number` | false | `75` | `15` |
| baseline | `gsm8k_37` | `number` | false | `2` | `4` |
| baseline | `gsm8k_38` | `number` | false | `10` | `15` |
| baseline | `gsm8k_39` | `number` | false | `18` | `12` |
| baseline | `gsm8k_40` | `number` | false | `8` | `4` |
| baseline | `gsm8k_41` | `number` | false | `200` | `250` |
| baseline | `gsm8k_42` | `number` | false | `26` | `20` |
| baseline | `gsm8k_43` | `number` | false | `48` | `4` |
| baseline | `gsm8k_44` | `number` | false | `20` | `30` |
| baseline | `gsm8k_45` | `number` | false | `104` | `10` |
| baseline | `gsm8k_46` | `number` | false | `163` | `15` |
| baseline | `gsm8k_47` | `number` | false | `800` | `13` |
| baseline | `gsm8k_48` | `number` | false | `8` | `10` |
| baseline | `gsm8k_49` | `number` | false | `30` | `20` |
