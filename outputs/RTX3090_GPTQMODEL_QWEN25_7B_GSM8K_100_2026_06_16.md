# Chat Task Benchmark

Model: `/mnt/e/models/Qwen2.5-7B-Instruct-GPTQ-Int4`
Tasks: `100`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 16 / 100 | 0.1600 | 10.8278 | 0.218625 |

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
| baseline | `gsm8k_25` | `number` | false | `2` | `3` |
| baseline | `gsm8k_26` | `number` | false | `243` | `214.5` |
| baseline | `gsm8k_27` | `number` | false | `16` | `32` |
| baseline | `gsm8k_28` | `number` | false | `25` | `35` |
| baseline | `gsm8k_29` | `number` | false | `104` | `55` |
| baseline | `gsm8k_30` | `number` | false | `109` | `55` |
| baseline | `gsm8k_31` | `number` | false | `80` | `72` |
| baseline | `gsm8k_32` | `number` | true | `35` | `35` |
| baseline | `gsm8k_33` | `number` | true | `70` | `70` |
| baseline | `gsm8k_34` | `number` | false | `23` | `27` |
| baseline | `gsm8k_35` | `number` | false | `9` | `10` |
| baseline | `gsm8k_36` | `number` | false | `75` | `25` |
| baseline | `gsm8k_37` | `number` | false | `2` | `0` |
| baseline | `gsm8k_38` | `number` | false | `10` | `8` |
| baseline | `gsm8k_39` | `number` | false | `18` | `12` |
| baseline | `gsm8k_40` | `number` | true | `8` | `8` |
| baseline | `gsm8k_41` | `number` | false | `200` | `1200` |
| baseline | `gsm8k_42` | `number` | true | `26` | `26` |
| baseline | `gsm8k_43` | `number` | false | `48` | `700` |
| baseline | `gsm8k_44` | `number` | false | `20` | `4` |
| baseline | `gsm8k_45` | `number` | false | `104` | `68` |
| baseline | `gsm8k_46` | `number` | false | `163` | `147` |
| baseline | `gsm8k_47` | `number` | false | `800` | `300` |
| baseline | `gsm8k_48` | `number` | true | `8` | `8` |
| baseline | `gsm8k_49` | `number` | false | `30` | `24` |
| baseline | `gsm8k_50` | `number` | false | `294` | `315` |
| baseline | `gsm8k_51` | `number` | false | `5` | `2` |
| baseline | `gsm8k_52` | `number` | false | `15` | `60` |
| baseline | `gsm8k_53` | `number` | false | `40` | `80` |
| baseline | `gsm8k_54` | `number` | false | `40` | `31` |
| baseline | `gsm8k_55` | `number` | true | `14` | `14` |
| baseline | `gsm8k_56` | `number` | false | `3` | `6` |
| baseline | `gsm8k_57` | `number` | false | `83` | `217` |
| baseline | `gsm8k_58` | `number` | false | `57` | `56` |
| baseline | `gsm8k_59` | `number` | true | `187` | `187` |
| baseline | `gsm8k_60` | `number` | false | `17` | `18` |
| baseline | `gsm8k_61` | `number` | false | `1430` | `1480` |
| baseline | `gsm8k_62` | `number` | false | `25000` | `27500` |
| baseline | `gsm8k_63` | `number` | false | `1596` | `1734` |
| baseline | `gsm8k_64` | `number` | false | `300` | `400` |
| baseline | `gsm8k_65` | `number` | false | `36` | `12` |
| baseline | `gsm8k_66` | `number` | true | `48` | `48` |
| baseline | `gsm8k_67` | `number` | false | `595` | `400` |
| baseline | `gsm8k_68` | `number` | false | `36` | `20` |
| baseline | `gsm8k_69` | `number` | true | `60` | `60` |
| baseline | `gsm8k_70` | `number` | false | `7425` | `3150` |
| baseline | `gsm8k_71` | `number` | true | `60` | `60` |
| baseline | `gsm8k_72` | `number` | false | `221` | `251` |
| baseline | `gsm8k_73` | `number` | false | `255` | `165` |
| baseline | `gsm8k_74` | `number` | false | `88` | `50` |
| baseline | `gsm8k_75` | `number` | false | `60` | `24` |
| baseline | `gsm8k_76` | `number` | false | `5` | `2` |
| baseline | `gsm8k_77` | `number` | false | `100` | `200` |
| baseline | `gsm8k_78` | `number` | false | `6` | `4.5` |
| baseline | `gsm8k_79` | `number` | true | `70` | `70` |
| baseline | `gsm8k_80` | `number` | false | `10` | `15` |
| baseline | `gsm8k_81` | `number` | false | `17` | `29` |
| baseline | `gsm8k_82` | `number` | false | `623` | `502` |
| baseline | `gsm8k_83` | `number` | false | `600` | `400` |
| baseline | `gsm8k_84` | `number` | false | `15` | `13` |
| baseline | `gsm8k_85` | `number` | true | `44` | `44` |
| baseline | `gsm8k_86` | `number` | false | `22` | `14` |
| baseline | `gsm8k_87` | `number` | false | `9360` | `798.6` |
| baseline | `gsm8k_88` | `number` | false | `8000` | `8800` |
| baseline | `gsm8k_89` | `number` | false | `24` | `16` |
| baseline | `gsm8k_90` | `number` | false | `225` | `350` |
| baseline | `gsm8k_91` | `number` | false | `28` | `20` |
| baseline | `gsm8k_92` | `number` | false | `4` | `3` |
| baseline | `gsm8k_93` | `number` | false | `36` | `42` |
| baseline | `gsm8k_94` | `number` | false | `348` | `240` |
| baseline | `gsm8k_95` | `number` | true | `40` | `40` |
| baseline | `gsm8k_96` | `number` | false | `3` | `4` |
| baseline | `gsm8k_97` | `number` | false | `12` | `8` |
| baseline | `gsm8k_98` | `number` | false | `5` | `15` |
| baseline | `gsm8k_99` | `number` | false | `58` | `72` |
