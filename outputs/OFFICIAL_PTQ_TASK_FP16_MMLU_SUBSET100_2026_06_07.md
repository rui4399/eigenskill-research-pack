# Chat Task Benchmark

Model: `Qwen/Qwen2.5-0.5B-Instruct`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 25 / 100 | 0.2500 | 31.0716 | 0.088620 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | false | `B` | `C. 2` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `To find the index of \( \langle p \rangle \) in \( S` |
| baseline | `mmlu_2` | `mcq` | false | `D` | `C. 0,1` |
| baseline | `mmlu_3` | `mcq` | true | `B` | `B. False, False` |
| baseline | `mmlu_4` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_6` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `B. False, False` |
| baseline | `mmlu_8` | `mcq` | false | `B` | `C. 2` |
| baseline | `mmlu_9` | `mcq` | false | `C` | `To find all zeros in the finite field \( \mathbb{Z}_7` |
| baseline | `mmlu_10` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_11` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `D. 11` |
| baseline | `mmlu_13` | `mcq` | false | `C` | `To determine which of the given options is a factorization of the polynomial \(x` |
| baseline | `mmlu_14` | `mcq` | false | `C` | `D. 105` |
| baseline | `mmlu_15` | `mcq` | true | `B` | `B. False, False` |
| baseline | `mmlu_16` | `mcq` | false | `C` | `D. -i` |
| baseline | `mmlu_17` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_18` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_19` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_20` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_21` | `mcq` | true | `A` | `A. 2x^2 + 5` |
| baseline | `mmlu_22` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_23` | `mcq` | false | `D` | `C. group` |
| baseline | `mmlu_24` | `mcq` | false | `B` | `A. True, True` |
| baseline | `mmlu_25` | `mcq` | false | `C` | `A. subgroup` |
| baseline | `mmlu_26` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_27` | `mcq` | false | `B` | `A. Yes, with p=2.` |
| baseline | `mmlu_28` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_29` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_30` | `mcq` | false | `B` | `A. True, True` |
| baseline | `mmlu_31` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_32` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_33` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_34` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_35` | `mcq` | false | `B` | `C. 2` |
| baseline | `mmlu_36` | `mcq` | true | `D` | `D. 22` |
| baseline | `mmlu_37` | `mcq` | false | `B` | `A. Yes, with p=2.` |
| baseline | `mmlu_38` | `mcq` | false | `C` | `D. 4` |
| baseline | `mmlu_39` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `A. 0` |
| baseline | `mmlu_41` | `mcq` | true | `A` | `A. 0` |
| baseline | `mmlu_42` | `mcq` | false | `B` | `A. True, True` |
| baseline | `mmlu_43` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_44` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_45` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `A. True, True` |
| baseline | `mmlu_47` | `mcq` | false | `B` | `D. 3` |
| baseline | `mmlu_48` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_49` | `mcq` | false | `B` | `D. 24` |
| baseline | `mmlu_50` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_51` | `mcq` | false | `B` | `To determine which values of \(c\) make \(Z_3[x]/(` |
| baseline | `mmlu_52` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_53` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_54` | `mcq` | true | `B` | `B. 2` |
| baseline | `mmlu_55` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_56` | `mcq` | false | `D` | `B. False, False` |
| baseline | `mmlu_57` | `mcq` | false | `B` | `D. 4` |
| baseline | `mmlu_58` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_59` | `mcq` | false | `A` | `B. False, False` |
| baseline | `mmlu_60` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_61` | `mcq` | false | `D` | `To determine whether each statement is true or false, let's analyze them one by` |
| baseline | `mmlu_62` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_63` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_64` | `mcq` | false | `B` | `A. 1` |
| baseline | `mmlu_65` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_66` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_67` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_68` | `mcq` | false | `A` | `To determine which of the given options is a factorization of \(x^4` |
| baseline | `mmlu_69` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_70` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_71` | `mcq` | true | `C` | `C. 2` |
| baseline | `mmlu_72` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_73` | `mcq` | false | `B` | `A. 0` |
| baseline | `mmlu_74` | `mcq` | false | `D` | `B. False, False` |
| baseline | `mmlu_75` | `mcq` | false | `B` | `A. True, True` |
| baseline | `mmlu_76` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_77` | `mcq` | true | `A` | `A. 0` |
| baseline | `mmlu_78` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_79` | `mcq` | true | `C` | `C. True, False` |
| baseline | `mmlu_80` | `mcq` | false | `B` | `A. True, True` |
| baseline | `mmlu_81` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_82` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_83` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_84` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_85` | `mcq` | false | `C` | `B. False, False` |
| baseline | `mmlu_86` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_87` | `mcq` | false | `A` | `C. 19` |
| baseline | `mmlu_88` | `mcq` | false | `A` | `D. 6` |
| baseline | `mmlu_89` | `mcq` | false | `C` | `A. True, True` |
| baseline | `mmlu_90` | `mcq` | false | `D` | `A. True, True` |
| baseline | `mmlu_91` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_92` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_93` | `mcq` | false | `A` | `D. 105` |
| baseline | `mmlu_94` | `mcq` | false | `D` | `B. False, False` |
| baseline | `mmlu_95` | `mcq` | true | `C` | `C. True, False` |
| baseline | `mmlu_96` | `mcq` | false | `B` | `C. 0,1` |
| baseline | `mmlu_97` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_98` | `mcq` | false | `C` | `A. 4` |
| baseline | `mmlu_99` | `mcq` | false | `C` | `A. True, True` |
