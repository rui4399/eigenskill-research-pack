# Chat Task Benchmark

Model: `outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model`
Tasks: `50`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 13 / 50 | 0.2600 | 11.1024 | 0.205163 |

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
