# Chat Task Benchmark

Model: `huihui_ai/qwen2.5-abliterate:7b-instruct`
Tasks: `50`
Task format: `gsm8k`
Chat template: `False`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 11 / 50 | 0.2200 | 18.6902 | 0.762850 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `9` |
| baseline | `gsm8k_1` | `number` | true | `3` | `3` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `120000` |
| baseline | `gsm8k_3` | `number` | false | `540` | `1080` |
| baseline | `gsm8k_4` | `number` | false | `20` | `10` |
| baseline | `gsm8k_5` | `number` | false | `64` | `44` |
| baseline | `gsm8k_6` | `number` | false | `260` | `300` |
| baseline | `gsm8k_7` | `number` | false | `160` | `30` |
| baseline | `gsm8k_8` | `number` | false | `45` | `20 miles` |
| baseline | `gsm8k_9` | `number` | false | `460` | `44` |
| baseline | `gsm8k_10` | `number` | false | `366` | `108` |
| baseline | `gsm8k_11` | `number` | false | `694` | `128` |
| baseline | `gsm8k_12` | `number` | false | `13` | `6` |
| baseline | `gsm8k_13` | `number` | false | `18` | `12` |
| baseline | `gsm8k_14` | `number` | false | `60` | `55` |
| baseline | `gsm8k_15` | `number` | false | `125` | `130` |
| baseline | `gsm8k_16` | `number` | true | `230` | `230` |
| baseline | `gsm8k_17` | `number` | false | `57500` | `4750` |
| baseline | `gsm8k_18` | `number` | true | `7` | `7` |
| baseline | `gsm8k_19` | `number` | false | `6` | `3` |
| baseline | `gsm8k_20` | `number` | false | `15` | `16` |
| baseline | `gsm8k_21` | `number` | false | `14` | `9` |
| baseline | `gsm8k_22` | `number` | false | `7` | `5` |
| baseline | `gsm8k_23` | `number` | true | `8` | `8` |
| baseline | `gsm8k_24` | `number` | false | `26` | `25.33` |
| baseline | `gsm8k_25` | `number` | false | `2` | `3` |
| baseline | `gsm8k_26` | `number` | false | `243` | `157.5` |
| baseline | `gsm8k_27` | `number` | true | `16` | `16` |
| baseline | `gsm8k_28` | `number` | true | `25` | `25` |
| baseline | `gsm8k_29` | `number` | false | `104` | `44` |
| baseline | `gsm8k_30` | `number` | false | `109` | `22` |
| baseline | `gsm8k_31` | `number` | false | `80` | `75` |
| baseline | `gsm8k_32` | `number` | true | `35` | `35` |
| baseline | `gsm8k_33` | `number` | true | `70` | `70` |
| baseline | `gsm8k_34` | `number` | false | `23` | `22` |
| baseline | `gsm8k_35` | `number` | false | `9` | `5.5` |
| baseline | `gsm8k_36` | `number` | false | `75` | `25` |
| baseline | `gsm8k_37` | `number` | false | `2` | `0` |
| baseline | `gsm8k_38` | `number` | true | `10` | `10` |
| baseline | `gsm8k_39` | `number` | false | `18` | `2.0` |
| baseline | `gsm8k_40` | `number` | true | `8` | `8` |
| baseline | `gsm8k_41` | `number` | false | `200` | `700` |
| baseline | `gsm8k_42` | `number` | false | `26` | `32` |
| baseline | `gsm8k_43` | `number` | false | `48` | `200` |
| baseline | `gsm8k_44` | `number` | false | `20` | `4` |
| baseline | `gsm8k_45` | `number` | false | `104` | `24` |
| baseline | `gsm8k_46` | `number` | false | `163` | `103` |
| baseline | `gsm8k_47` | `number` | false | `800` | `140` |
| baseline | `gsm8k_48` | `number` | true | `8` | `8` |
| baseline | `gsm8k_49` | `number` | false | `30` | `9` |
