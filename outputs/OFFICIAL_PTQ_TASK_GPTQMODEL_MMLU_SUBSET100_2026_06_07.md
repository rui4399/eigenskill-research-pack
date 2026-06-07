# Chat Task Benchmark

Model: `outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 22 / 100 | 0.2200 | 10.7656 | 0.202465 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `C. True, False  This question involves understanding concepts related to groups (non` |
| baseline | `mmlu_4` | `mcq` | false | `B` | `A. 2x^2 + 5 D. x^2` |
| baseline | `mmlu_5` | `mcq` | false | `A` | `True, True` |
| baseline | `mmlu_6` | `mcq` | true | `A` | `A. True, True  The statement "Every homomorphic image of a group` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `A. True, True  These statements are true based on their respective definitions and` |
| baseline | `mmlu_8` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10` | `mcq` | false | `C` | `D. False, True  This question involves understanding group properties and their implications for` |
| baseline | `mmlu_11` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_14` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `C. True, False  The statement "R is a splitting field of some` |
| baseline | `mmlu_16` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_17` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_18` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_19` | `mcq` | false | `A` | `D. False, True  The correct answer is D. False, True.` |
| baseline | `mmlu_20` | `mcq` | false | `A` | `D. False, True  The correct answer is D. False, True.` |
| baseline | `mmlu_21` | `mcq` | true | `A` | `A. 2x^2 + 5  The given polynomials are` |
| baseline | `mmlu_22` | `mcq` | false | `D` | `C. True, False  This question involves understanding vector spaces and linear independence.` |
| baseline | `mmlu_23` | `mcq` | false | `D` | `A. semi groups with identity  The set of all nth roots of unity for` |
| baseline | `mmlu_24` | `mcq` | false | `B` | `C. True, False  The correct answer is that statement 1 and statement` |
| baseline | `mmlu_25` | `mcq` | false | `C` | `A. subgroup The set of all n x n non-singular matrices (` |
| baseline | `mmlu_26` | `mcq` | true | `C` | `C. True, False  The correct answer is that statement 1 and statement` |
| baseline | `mmlu_27` | `mcq` | false | `B` | `No.` |
| baseline | `mmlu_28` | `mcq` | false | `D` | `A. True, True  The statement "Statement 1" and "Statement` |
| baseline | `mmlu_29` | `mcq` | true | `A` | `A. True, True  These statements are true based on the definitions provided in` |
| baseline | `mmlu_30` | `mcq` | false | `B` | `A. True, True  These statements are true based on the definitions provided.` |
| baseline | `mmlu_31` | `mcq` | false | `B` | `A. commutative semi group` |
| baseline | `mmlu_32` | `mcq` | false | `A` | `C. True, False  This question involves understanding concepts related to vector spaces and` |
| baseline | `mmlu_33` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `C. True, False  The correct answer is B. False, False.` |
| baseline | `mmlu_35` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_36` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_37` | `mcq` | false | `B` | `No.` |
| baseline | `mmlu_38` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_39` | `mcq` | false | `D` | `A. True, True  These two statements are related to permutations and cycles in` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_41` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_42` | `mcq` | false | `B` | `D. False, True  The correct answer is D. False, True.` |
| baseline | `mmlu_43` | `mcq` | true | `C` | `C. True, False  The correct answer is that statement 1 (Every` |
| baseline | `mmlu_44` | `mcq` | false | `C` | `A. True, True  The statement "the function f must necessarily be inject` |
| baseline | `mmlu_45` | `mcq` | true | `C` | `C. True, False  The correct answer is that statement 1 is false` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `True, True` |
| baseline | `mmlu_47` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_48` | `mcq` | true | `C` | `C. True, False  The correct answer is that statement 1 is false` |
| baseline | `mmlu_49` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_50` | `mcq` | false | `D` | `C. True, False  The correct answer is that statement 1 and statement` |
| baseline | `mmlu_51` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_52` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_53` | `mcq` | false | `C` | `A. True, True  These statements do not match each other, so they` |
| baseline | `mmlu_54` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_55` | `mcq` | false | `A` | `True, False  The statement "Every finitely generated torsion-free ab` |
| baseline | `mmlu_56` | `mcq` | false | `D` | `True, True  The statement "Statement 1 \| 4x - ` |
| baseline | `mmlu_57` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_58` | `mcq` | false | `A` | `True, True` |
| baseline | `mmlu_59` | `mcq` | true | `A` | `A. True, True  These statements are true based on their respective options.` |
| baseline | `mmlu_60` | `mcq` | false | `D` | `A. True, True  These two statements are both true and supported by mathematical` |
| baseline | `mmlu_61` | `mcq` | false | `D` | `False, False  The answer is B. False, True. The first statement` |
| baseline | `mmlu_62` | `mcq` | false | `C` | `A. True, True  These statements are true based on the given information.` |
| baseline | `mmlu_63` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_64` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_65` | `mcq` | false | `C` | `A. True, True  These two statements are both true and related to the` |
| baseline | `mmlu_66` | `mcq` | false | `D` | `A. True, True  These statements are true based on the definitions provided for` |
| baseline | `mmlu_67` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_68` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_69` | `mcq` | false | `A` | `C. True, False  The correct answer is that statement 1 and statement` |
| baseline | `mmlu_70` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_71` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_72` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_73` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_74` | `mcq` | false | `D` | `A. True, True  The statement "If a and b are elements of` |
| baseline | `mmlu_75` | `mcq` | false | `B` | `D. False, True  The correct answer is D. False, True.` |
| baseline | `mmlu_76` | `mcq` | false | `C` | `D. False, True  The statement "Statement 1 \|S_n is` |
| baseline | `mmlu_77` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_78` | `mcq` | true | `D` | `D. False, True  The correct answer is D. False, True.` |
| baseline | `mmlu_79` | `mcq` | true | `C` | `C. True, False  The correct answer is that statement 1 and statement` |
| baseline | `mmlu_80` | `mcq` | false | `B` | `C. True, False  The statement "The external direct product of cyclic groups` |
| baseline | `mmlu_81` | `mcq` | false | `D` | `True, False  The first statement is true because every nontrivial (non` |
| baseline | `mmlu_82` | `mcq` | false | `A` | `C. True, False  The first statement claims that for every positive integer \(` |
| baseline | `mmlu_83` | `mcq` | false | `C` | `D. False, True  The correct answer is D. False, True.` |
| baseline | `mmlu_84` | `mcq` | false | `D` | `A. True, True  The statement "the function g must necessarily be inject` |
| baseline | `mmlu_85` | `mcq` | false | `C` | `A. True, True  The statement "A homomorphism is one to` |
| baseline | `mmlu_86` | `mcq` | false | `A` | `D. False, True  The correct answer is that both statements (A)` |
| baseline | `mmlu_87` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_88` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_89` | `mcq` | true | `C` | `C. True, False  The correct answer is that statement 1 (Every` |
| baseline | `mmlu_90` | `mcq` | false | `D` | `C. True, False  The correct answer is that statement 1 and statement` |
| baseline | `mmlu_91` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_92` | `mcq` | false | `B` | `C  The statement that is true according to the given options is C. The` |
| baseline | `mmlu_93` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_94` | `mcq` | false | `D` | `C. True, False  The first statement claims that if Q is an extension` |
| baseline | `mmlu_95` | `mcq` | false | `C` | `True, True` |
| baseline | `mmlu_96` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_97` | `mcq` | false | `C` | `D. 30  The cyclic subgroup of Z_30 (the` |
| baseline | `mmlu_98` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_99` | `mcq` | true | `C` | `C. True, False  The correct answer is that statement 1 and statement` |
