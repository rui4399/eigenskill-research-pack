# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `100`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 11 / 100 | 0.1100 | 12.4491 | 0.229782 |

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
| baseline | `gsm8k_20` | `number` | false | `15` | `24` |
| baseline | `gsm8k_21` | `number` | false | `14` | `19` |
| baseline | `gsm8k_22` | `number` | false | `7` | `20` |
| baseline | `gsm8k_23` | `number` | false | `8` | `4` |
| baseline | `gsm8k_24` | `number` | false | `26` | `27.25` |
| baseline | `gsm8k_25` | `number` | false | `2` | `10` |
| baseline | `gsm8k_26` | `number` | false | `243` | `360.0` |
| baseline | `gsm8k_27` | `number` | false | `16` | `120` |
| baseline | `gsm8k_28` | `number` | true | `25` | `25` |
| baseline | `gsm8k_29` | `number` | false | `104` | `100` |
| baseline | `gsm8k_30` | `number` | false | `109` | `100` |
| baseline | `gsm8k_31` | `number` | false | `80` | `100` |
| baseline | `gsm8k_32` | `number` | true | `35` | `35` |
| baseline | `gsm8k_33` | `number` | false | `70` | `140` |
| baseline | `gsm8k_34` | `number` | false | `23` | `26` |
| baseline | `gsm8k_35` | `number` | false | `9` | `130` |
| baseline | `gsm8k_36` | `number` | false | `75` | `120` |
| baseline | `gsm8k_37` | `number` | false | `2` | `10` |
| baseline | `gsm8k_38` | `number` | true | `10` | `10 mph` |
| baseline | `gsm8k_39` | `number` | true | `18` | `18` |
| baseline | `gsm8k_40` | `number` | false | `8` | `28` |
| baseline | `gsm8k_41` | `number` | false | `200` | `1200` |
| baseline | `gsm8k_42` | `number` | false | `26` | `14` |
| baseline | `gsm8k_43` | `number` | false | `48` | `100` |
| baseline | `gsm8k_44` | `number` | false | `20` | `100` |
| baseline | `gsm8k_45` | `number` | false | `104` | `168` |
| baseline | `gsm8k_46` | `number` | false | `163` | `158` |
| baseline | `gsm8k_47` | `number` | false | `800` | `200` |
| baseline | `gsm8k_48` | `number` | false | `8` | `24` |
| baseline | `gsm8k_49` | `number` | false | `30` | `36` |
| baseline | `gsm8k_50` | `number` | false | `294` | `1764` |
| baseline | `gsm8k_51` | `number` | false | `5` | `2` |
| baseline | `gsm8k_52` | `number` | false | `15` | `10` |
| baseline | `gsm8k_53` | `number` | false | `40` | `160` |
| baseline | `gsm8k_54` | `number` | false | `40` | `50` |
| baseline | `gsm8k_55` | `number` | false | `14` | `15` |
| baseline | `gsm8k_56` | `number` | false | `3` | `4` |
| baseline | `gsm8k_57` | `number` | false | `83` | `10` |
| baseline | `gsm8k_58` | `number` | false | `57` | `44.0` |
| baseline | `gsm8k_59` | `number` | false | `187` | `337` |
| baseline | `gsm8k_60` | `number` | false | `17` | `20` |
| baseline | `gsm8k_61` | `number` | false | `1430` | `2600` |
| baseline | `gsm8k_62` | `number` | false | `25000` | `50000` |
| baseline | `gsm8k_63` | `number` | false | `1596` | `1540` |
| baseline | `gsm8k_64` | `number` | false | `300` | `440` |
| baseline | `gsm8k_65` | `number` | false | `36` | `168` |
| baseline | `gsm8k_66` | `number` | false | `48` | `160` |
| baseline | `gsm8k_67` | `number` | false | `595` | `400` |
| baseline | `gsm8k_68` | `number` | false | `36` | `30` |
| baseline | `gsm8k_69` | `number` | false | `60` | `15` |
| baseline | `gsm8k_70` | `number` | false | `7425` | `1050` |
| baseline | `gsm8k_71` | `number` | false | `60` | `140` |
| baseline | `gsm8k_72` | `number` | false | `221` | `101` |
| baseline | `gsm8k_73` | `number` | false | `255` | `150` |
| baseline | `gsm8k_74` | `number` | false | `88` | `605.0` |
| baseline | `gsm8k_75` | `number` | false | `60` | `8` |
| baseline | `gsm8k_76` | `number` | false | `5` | `12` |
| baseline | `gsm8k_77` | `number` | true | `100` | `100` |
| baseline | `gsm8k_78` | `number` | false | `6` | `10` |
| baseline | `gsm8k_79` | `number` | true | `70` | `70` |
| baseline | `gsm8k_80` | `number` | true | `10` | `10` |
| baseline | `gsm8k_81` | `number` | false | `17` | `14` |
| baseline | `gsm8k_82` | `number` | false | `623` | `145` |
| baseline | `gsm8k_83` | `number` | false | `600` | `720` |
| baseline | `gsm8k_84` | `number` | false | `15` | `24` |
| baseline | `gsm8k_85` | `number` | false | `44` | `120` |
| baseline | `gsm8k_86` | `number` | false | `22` | `20` |
| baseline | `gsm8k_87` | `number` | false | `9360` | `660` |
| baseline | `gsm8k_88` | `number` | false | `8000` | `44000` |
| baseline | `gsm8k_89` | `number` | false | `24` | `108` |
| baseline | `gsm8k_90` | `number` | false | `225` | `120` |
| baseline | `gsm8k_91` | `number` | false | `28` | `14` |
| baseline | `gsm8k_92` | `number` | false | `4` | `12` |
| baseline | `gsm8k_93` | `number` | false | `36` | `40` |
| baseline | `gsm8k_94` | `number` | false | `348` | `180` |
| baseline | `gsm8k_95` | `number` | true | `40` | `40` |
| baseline | `gsm8k_96` | `number` | false | `3` | `4` |
| baseline | `gsm8k_97` | `number` | true | `12` | `12` |
| baseline | `gsm8k_98` | `number` | false | `5` | `25` |
| baseline | `gsm8k_99` | `number` | false | `58` | `16` |
