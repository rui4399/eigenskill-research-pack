# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `100`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 12 / 100 | 0.1200 | 19.0182 | 0.137708 |

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
| baseline | `gsm8k_20` | `number` | false | `15` | `36` |
| baseline | `gsm8k_21` | `number` | false | `14` | `9` |
| baseline | `gsm8k_22` | `number` | false | `7` | `15` |
| baseline | `gsm8k_23` | `number` | false | `8` | `6` |
| baseline | `gsm8k_24` | `number` | false | `26` | `31.50` |
| baseline | `gsm8k_25` | `number` | false | `2` | `6` |
| baseline | `gsm8k_26` | `number` | false | `243` | `486` |
| baseline | `gsm8k_27` | `number` | false | `16` | `360` |
| baseline | `gsm8k_28` | `number` | false | `25` | `40` |
| baseline | `gsm8k_29` | `number` | false | `104` | `65` |
| baseline | `gsm8k_30` | `number` | false | `109` | `54` |
| baseline | `gsm8k_31` | `number` | false | `80` | `130` |
| baseline | `gsm8k_32` | `number` | true | `35` | `35` |
| baseline | `gsm8k_33` | `number` | false | `70` | `140` |
| baseline | `gsm8k_34` | `number` | false | `23` | `18` |
| baseline | `gsm8k_35` | `number` | false | `9` | `136` |
| baseline | `gsm8k_36` | `number` | false | `75` | `120` |
| baseline | `gsm8k_37` | `number` | false | `2` | `4` |
| baseline | `gsm8k_38` | `number` | false | `10` | `5 mph` |
| baseline | `gsm8k_39` | `number` | false | `18` | `12` |
| baseline | `gsm8k_40` | `number` | true | `8` | `8` |
| baseline | `gsm8k_41` | `number` | false | `200` | `600` |
| baseline | `gsm8k_42` | `number` | true | `26` | `26` |
| baseline | `gsm8k_43` | `number` | false | `48` | `100` |
| baseline | `gsm8k_44` | `number` | false | `20` | `40` |
| baseline | `gsm8k_45` | `number` | false | `104` | `76` |
| baseline | `gsm8k_46` | `number` | false | `163` | `170` |
| baseline | `gsm8k_47` | `number` | false | `800` | `200` |
| baseline | `gsm8k_48` | `number` | false | `8` | `24` |
| baseline | `gsm8k_49` | `number` | false | `30` | `60` |
| baseline | `gsm8k_50` | `number` | false | `294` | `1470` |
| baseline | `gsm8k_51` | `number` | true | `5` | `5` |
| baseline | `gsm8k_52` | `number` | false | `15` | `To determine how many toys Uriah needs to remove, we first calculate the total weight of the comic books he plans to rem` |
| baseline | `gsm8k_53` | `number` | false | `40` | `320` |
| baseline | `gsm8k_54` | `number` | false | `40` | `35` |
| baseline | `gsm8k_55` | `number` | false | `14` | `15` |
| baseline | `gsm8k_56` | `number` | true | `3` | `3` |
| baseline | `gsm8k_57` | `number` | false | `83` | `25` |
| baseline | `gsm8k_58` | `number` | false | `57` | `49.0` |
| baseline | `gsm8k_59` | `number` | false | `187` | `184` |
| baseline | `gsm8k_60` | `number` | false | `17` | `18` |
| baseline | `gsm8k_61` | `number` | false | `1430` | `2100` |
| baseline | `gsm8k_62` | `number` | false | `25000` | `60000` |
| baseline | `gsm8k_63` | `number` | false | `1596` | `210` |
| baseline | `gsm8k_64` | `number` | false | `300` | `360` |
| baseline | `gsm8k_65` | `number` | false | `36` | `120` |
| baseline | `gsm8k_66` | `number` | false | `48` | `120` |
| baseline | `gsm8k_67` | `number` | false | `595` | `680` |
| baseline | `gsm8k_68` | `number` | false | `36` | `15` |
| baseline | `gsm8k_69` | `number` | false | `60` | `40` |
| baseline | `gsm8k_70` | `number` | false | `7425` | `2400` |
| baseline | `gsm8k_71` | `number` | false | `60` | `40` |
| baseline | `gsm8k_72` | `number` | false | `221` | `301` |
| baseline | `gsm8k_73` | `number` | false | `255` | `468` |
| baseline | `gsm8k_74` | `number` | false | `88` | `306` |
| baseline | `gsm8k_75` | `number` | false | `60` | `8` |
| baseline | `gsm8k_76` | `number` | false | `5` | `3` |
| baseline | `gsm8k_77` | `number` | false | `100` | `1600` |
| baseline | `gsm8k_78` | `number` | false | `6` | `10` |
| baseline | `gsm8k_79` | `number` | true | `70` | `70` |
| baseline | `gsm8k_80` | `number` | true | `10` | `10` |
| baseline | `gsm8k_81` | `number` | false | `17` | `45` |
| baseline | `gsm8k_82` | `number` | false | `623` | `137` |
| baseline | `gsm8k_83` | `number` | true | `600` | `600` |
| baseline | `gsm8k_84` | `number` | false | `15` | `30` |
| baseline | `gsm8k_85` | `number` | false | `44` | `160` |
| baseline | `gsm8k_86` | `number` | false | `22` | `19` |
| baseline | `gsm8k_87` | `number` | false | `9360` | `7200` |
| baseline | `gsm8k_88` | `number` | false | `8000` | `20000` |
| baseline | `gsm8k_89` | `number` | false | `24` | `30` |
| baseline | `gsm8k_90` | `number` | false | `225` | `To determine how many pounds of potato salad Ted needs to bring to the picnic, we first calculate the total amount each ` |
| baseline | `gsm8k_91` | `number` | false | `28` | `38` |
| baseline | `gsm8k_92` | `number` | false | `4` | `9` |
| baseline | `gsm8k_93` | `number` | true | `36` | `36` |
| baseline | `gsm8k_94` | `number` | false | `348` | `140` |
| baseline | `gsm8k_95` | `number` | true | `40` | `40` |
| baseline | `gsm8k_96` | `number` | false | `3` | `4` |
| baseline | `gsm8k_97` | `number` | false | `12` | `48` |
| baseline | `gsm8k_98` | `number` | false | `5` | `30` |
| baseline | `gsm8k_99` | `number` | false | `58` | `16` |
