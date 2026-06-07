# Chat Task Benchmark

Model: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model`
Tasks: `100`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 1 / 100 | 0.0100 | 5.1528 | 0.385639 |

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
| baseline | `gsm8k_50` | `number` | false | `294` | `1408` |
| baseline | `gsm8k_51` | `number` | false | `5` | `2` |
| baseline | `gsm8k_52` | `number` | false | `15` | `8` |
| baseline | `gsm8k_53` | `number` | false | `40` | `5` |
| baseline | `gsm8k_54` | `number` | false | `40` | `8` |
| baseline | `gsm8k_55` | `number` | false | `14` | `1` |
| baseline | `gsm8k_56` | `number` | false | `3` | `10` |
| baseline | `gsm8k_57` | `number` | false | `83` | `2` |
| baseline | `gsm8k_58` | `number` | false | `57` | `16.5` |
| baseline | `gsm8k_59` | `number` | false | `187` | `1420` |
| baseline | `gsm8k_60` | `number` | false | `17` | `4` |
| baseline | `gsm8k_61` | `number` | false | `1430` | `240` |
| baseline | `gsm8k_62` | `number` | false | `25000` | `10` |
| baseline | `gsm8k_63` | `number` | false | `1596` | `280` |
| baseline | `gsm8k_64` | `number` | false | `300` | `5` |
| baseline | `gsm8k_65` | `number` | false | `36` | `18` |
| baseline | `gsm8k_66` | `number` | false | `48` | `10` |
| baseline | `gsm8k_67` | `number` | false | `595` | `20` |
| baseline | `gsm8k_68` | `number` | false | `36` | `12` |
| baseline | `gsm8k_69` | `number` | false | `60` | `240` |
| baseline | `gsm8k_70` | `number` | false | `7425` | `2250` |
| baseline | `gsm8k_71` | `number` | false | `60` | `4` |
| baseline | `gsm8k_72` | `number` | false | `221` | `158` |
| baseline | `gsm8k_73` | `number` | false | `255` | `45  Final answer: 45.` |
| baseline | `gsm8k_74` | `number` | false | `88` | `5.00` |
| baseline | `gsm8k_75` | `number` | false | `60` | `5` |
| baseline | `gsm8k_76` | `number` | true | `5` | `5` |
| baseline | `gsm8k_77` | `number` | false | `100` | `25` |
| baseline | `gsm8k_78` | `number` | false | `6` | `4` |
| baseline | `gsm8k_79` | `number` | false | `70` | `24` |
| baseline | `gsm8k_80` | `number` | false | `10` | `3` |
| baseline | `gsm8k_81` | `number` | false | `17` | `5` |
| baseline | `gsm8k_82` | `number` | false | `623` | `360` |
| baseline | `gsm8k_83` | `number` | false | `600` | `100` |
| baseline | `gsm8k_84` | `number` | false | `15` | `10` |
| baseline | `gsm8k_85` | `number` | false | `44` | `15` |
| baseline | `gsm8k_86` | `number` | false | `22` | `10` |
| baseline | `gsm8k_87` | `number` | false | `9360` | `3` |
| baseline | `gsm8k_88` | `number` | false | `8000` | `22` |
| baseline | `gsm8k_89` | `number` | false | `24` | `3` |
| baseline | `gsm8k_90` | `number` | false | `225` | `40` |
| baseline | `gsm8k_91` | `number` | false | `28` | `5` |
| baseline | `gsm8k_92` | `number` | false | `4` | `3` |
| baseline | `gsm8k_93` | `number` | false | `36` | `2` |
| baseline | `gsm8k_94` | `number` | false | `348` | `142` |
| baseline | `gsm8k_95` | `number` | false | `40` | `198` |
| baseline | `gsm8k_96` | `number` | false | `3` | `5` |
| baseline | `gsm8k_97` | `number` | false | `12` | `4` |
| baseline | `gsm8k_98` | `number` | false | `5` | `4` |
| baseline | `gsm8k_99` | `number` | false | `58` | `56` |
