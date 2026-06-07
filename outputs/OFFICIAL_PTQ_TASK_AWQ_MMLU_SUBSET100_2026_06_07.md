# Chat Task Benchmark

Model: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 23 / 100 | 0.2300 | 4.8842 | 0.326504 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2` | `mcq` | false | `D` | `Option A` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_6` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9` | `mcq` | false | `C` | `Option A` |
| baseline | `mmlu_10` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_11` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_14` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `A. True, True` |
| baseline | `mmlu_16` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_17` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_18` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_19` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_20` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_21` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_22` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_23` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_24` | `mcq` | false | `B` | `A. True, True` |
| baseline | `mmlu_25` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_26` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_27` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_28` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_29` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_30` | `mcq` | false | `B` | `A. True, True` |
| baseline | `mmlu_31` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_32` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_33` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_34` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_35` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_36` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_37` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_38` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_39` | `mcq` | false | `D` | `A. True, False` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_41` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_42` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_43` | `mcq` | false | `C` | `A. True, False` |
| baseline | `mmlu_44` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_45` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_47` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_48` | `mcq` | false | `C` | `A. True, False` |
| baseline | `mmlu_49` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_50` | `mcq` | false | `D` | `A. True, False` |
| baseline | `mmlu_51` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_52` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_53` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_54` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_55` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_56` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_57` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_58` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_59` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_60` | `mcq` | false | `D` | `A. True, False` |
| baseline | `mmlu_61` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_62` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_63` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_64` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_65` | `mcq` | false | `C` | `A. True, False` |
| baseline | `mmlu_66` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_67` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_68` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_69` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_70` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_71` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_72` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_73` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_74` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_75` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_76` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_77` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_78` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_79` | `mcq` | false | `C` | `A. True, False` |
| baseline | `mmlu_80` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_81` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_82` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_83` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_84` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_85` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_86` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_87` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_88` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_89` | `mcq` | false | `C` | `A. True, False` |
| baseline | `mmlu_90` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_91` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_92` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_93` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_94` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_95` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_96` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_97` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_98` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_99` | `mcq` | false | `C` | `A. True, False` |
