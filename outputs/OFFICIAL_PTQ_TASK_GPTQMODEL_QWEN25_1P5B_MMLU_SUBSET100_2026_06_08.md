# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 25 / 100 | 0.2500 | 10.2403 | 0.207707 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `2` |
| baseline | `mmlu_2` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `5` |
| baseline | `mmlu_13` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_16` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_17` | `mcq` | false | `C` | `D. (3,6)` |
| baseline | `mmlu_18` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_19` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_20` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_21` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_22` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_23` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_24` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_25` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_26` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_27` | `mcq` | false | `B` | `D. No.` |
| baseline | `mmlu_28` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_29` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_30` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_31` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_32` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_33` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_35` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_36` | `mcq` | false | `D` | `C. 11` |
| baseline | `mmlu_37` | `mcq` | false | `B` | `D. No.` |
| baseline | `mmlu_38` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_39` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_41` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_42` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_43` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_44` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_45` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_47` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_48` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_49` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_50` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_51` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_52` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_53` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_54` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_55` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_56` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_57` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_58` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_59` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_60` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_61` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_62` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_63` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_64` | `mcq` | false | `B` | `C. infinitely many` |
| baseline | `mmlu_65` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_66` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_67` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_68` | `mcq` | false | `A` | `C. (x-1)(x+1)^3` |
| baseline | `mmlu_69` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_70` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_71` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_72` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_73` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_74` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_75` | `mcq` | false | `B` | `D. False, True` |
| baseline | `mmlu_76` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_77` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_78` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_79` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_80` | `mcq` | false | `B` | `C. True, False` |
| baseline | `mmlu_81` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_82` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_83` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_84` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_85` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_86` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_87` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_88` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_89` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_90` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_91` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_92` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_93` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_94` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_95` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_96` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_97` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_98` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_99` | `mcq` | false | `C` | `D.` |
