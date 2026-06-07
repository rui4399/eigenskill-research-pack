# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 54 / 100 | 0.5400 | 11.1998 | 0.154689 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | true | `B` | `B. 4` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `A. 8` |
| baseline | `mmlu_2` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4` | `mcq` | false | `B` | `C. 0` |
| baseline | `mmlu_5` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8` | `mcq` | true | `B` | `B. 4` |
| baseline | `mmlu_9` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_14` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_16` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_17` | `mcq` | true | `C` | `C. (1,6)` |
| baseline | `mmlu_18` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_19` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_20` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_21` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_22` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_23` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_24` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_25` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_26` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_27` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_28` | `mcq` | false | `C` | `B. eight weeks post-fertilization.` |
| baseline | `mmlu_29` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_30` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_31` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_32` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_33` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_35` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_36` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_37` | `mcq` | true | `D` | `D. Testes` |
| baseline | `mmlu_38` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_39` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_40` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_41` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_42` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_43` | `mcq` | false | `D` | `C. Work-play balance` |
| baseline | `mmlu_44` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_45` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_46` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_47` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_48` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_49` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_50` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_51` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_52` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_53` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_54` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_55` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_56` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_57` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_58` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_59` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_60` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_61` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_62` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_63` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_64` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_65` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_66` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_67` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_68` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_69` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_70` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_71` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_72` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_73` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_74` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_75` | `mcq` | true | `B` | `B. Access Point` |
| baseline | `mmlu_76` | `mcq` | true | `B` | `B. 128` |
| baseline | `mmlu_77` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_78` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_79` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_80` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_81` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_82` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_83` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_84` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_85` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_86` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_87` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_88` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_89` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_90` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_91` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_92` | `mcq` | false | `A` | `C. all Christians only` |
| baseline | `mmlu_93` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_94` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_95` | `mcq` | true | `C` | `C. The Apollo space program` |
| baseline | `mmlu_96` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_97` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_98` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_99` | `mcq` | true | `D` | `D` |
