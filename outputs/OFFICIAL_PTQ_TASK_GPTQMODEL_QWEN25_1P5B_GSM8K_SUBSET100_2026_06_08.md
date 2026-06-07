# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `100`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 8 / 100 | 0.0800 | 11.0534 | 0.264654 |

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
| baseline | `gsm8k_20` | `number` | false | `15` | `13` |
| baseline | `gsm8k_21` | `number` | false | `14` | `5` |
| baseline | `gsm8k_22` | `number` | false | `7` | `15` |
| baseline | `gsm8k_23` | `number` | false | `8` | `80` |
| baseline | `gsm8k_24` | `number` | false | `26` | `13.65` |
| baseline | `gsm8k_25` | `number` | false | `2` | `9` |
| baseline | `gsm8k_26` | `number` | false | `243` | `180` |
| baseline | `gsm8k_27` | `number` | false | `16` | `240.` |
| baseline | `gsm8k_28` | `number` | false | `25` | `15 miles` |
| baseline | `gsm8k_29` | `number` | true | `104` | `104` |
| baseline | `gsm8k_30` | `number` | false | `109` | `36` |
| baseline | `gsm8k_31` | `number` | false | `80` | `130` |
| baseline | `gsm8k_32` | `number` | false | `35` | `70` |
| baseline | `gsm8k_33` | `number` | false | `70` | `40` |
| baseline | `gsm8k_34` | `number` | false | `23` | `31` |
| baseline | `gsm8k_35` | `number` | false | `9` | `108` |
| baseline | `gsm8k_36` | `number` | false | `75` | `120` |
| baseline | `gsm8k_37` | `number` | false | `2` | `4` |
| baseline | `gsm8k_38` | `number` | true | `10` | `10` |
| baseline | `gsm8k_39` | `number` | true | `18` | `18` |
| baseline | `gsm8k_40` | `number` | true | `8` | `8` |
| baseline | `gsm8k_41` | `number` | false | `200` | `2000` |
| baseline | `gsm8k_42` | `number` | false | `26` | `13` |
| baseline | `gsm8k_43` | `number` | false | `48` | `400` |
| baseline | `gsm8k_44` | `number` | false | `20` | `400` |
| baseline | `gsm8k_45` | `number` | false | `104` | `168` |
| baseline | `gsm8k_46` | `number` | false | `163` | `167` |
| baseline | `gsm8k_47` | `number` | false | `800` | `1600` |
| baseline | `gsm8k_48` | `number` | false | `8` | `3` |
| baseline | `gsm8k_49` | `number` | false | `30` | `20` |
| baseline | `gsm8k_50` | `number` | false | `294` | `10560` |
| baseline | `gsm8k_51` | `number` | false | `5` | `200` |
| baseline | `gsm8k_52` | `number` | false | `15` | `6` |
| baseline | `gsm8k_53` | `number` | false | `40` | `800` |
| baseline | `gsm8k_54` | `number` | false | `40` | `43` |
| baseline | `gsm8k_55` | `number` | false | `14` | `10` |
| baseline | `gsm8k_56` | `number` | false | `3` | `5` |
| baseline | `gsm8k_57` | `number` | false | `83` | `20` |
| baseline | `gsm8k_58` | `number` | false | `57` | `49.00` |
| baseline | `gsm8k_59` | `number` | false | `187` | `186` |
| baseline | `gsm8k_60` | `number` | false | `17` | `7` |
| baseline | `gsm8k_61` | `number` | false | `1430` | `2300` |
| baseline | `gsm8k_62` | `number` | false | `25000` | `100000` |
| baseline | `gsm8k_63` | `number` | false | `1596` | `2800` |
| baseline | `gsm8k_64` | `number` | false | `300` | `360` |
| baseline | `gsm8k_65` | `number` | false | `36` | `180` |
| baseline | `gsm8k_66` | `number` | false | `48` | `80` |
| baseline | `gsm8k_67` | `number` | false | `595` | `285` |
| baseline | `gsm8k_68` | `number` | false | `36` | `20` |
| baseline | `gsm8k_69` | `number` | false | `60` | `40` |
| baseline | `gsm8k_70` | `number` | false | `7425` | `3250` |
| baseline | `gsm8k_71` | `number` | false | `60` | `140` |
| baseline | `gsm8k_72` | `number` | false | `221` | `150` |
| baseline | `gsm8k_73` | `number` | false | `255` | `$49.74` |
| baseline | `gsm8k_74` | `number` | false | `88` | `356` |
| baseline | `gsm8k_75` | `number` | false | `60` | `8` |
| baseline | `gsm8k_76` | `number` | false | `5` | `60` |
| baseline | `gsm8k_77` | `number` | false | `100` | `200` |
| baseline | `gsm8k_78` | `number` | false | `6` | `9` |
| baseline | `gsm8k_79` | `number` | true | `70` | `70.` |
| baseline | `gsm8k_80` | `number` | false | `10` | `13` |
| baseline | `gsm8k_81` | `number` | false | `17` | `55` |
| baseline | `gsm8k_82` | `number` | false | `623` | `190` |
| baseline | `gsm8k_83` | `number` | false | `600` | `120` |
| baseline | `gsm8k_84` | `number` | false | `15` | `20` |
| baseline | `gsm8k_85` | `number` | false | `44` | `160` |
| baseline | `gsm8k_86` | `number` | false | `22` | `24` |
| baseline | `gsm8k_87` | `number` | false | `9360` | `2760.00` |
| baseline | `gsm8k_88` | `number` | false | `8000` | `40000` |
| baseline | `gsm8k_89` | `number` | false | `24` | `30.00` |
| baseline | `gsm8k_90` | `number` | false | `225` | `200lbs` |
| baseline | `gsm8k_91` | `number` | false | `28` | `25` |
| baseline | `gsm8k_92` | `number` | false | `4` | `8` |
| baseline | `gsm8k_93` | `number` | true | `36` | `36` |
| baseline | `gsm8k_94` | `number` | false | `348` | `120` |
| baseline | `gsm8k_95` | `number` | true | `40` | `40` |
| baseline | `gsm8k_96` | `number` | false | `3` | `4` |
| baseline | `gsm8k_97` | `number` | false | `12` | `8` |
| baseline | `gsm8k_98` | `number` | false | `5` | `10` |
| baseline | `gsm8k_99` | `number` | false | `58` | `9` |
