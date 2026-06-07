# Chat Task Benchmark

Model: `outputs/official_gptqmodel_smoke_2026_06_07/qwen25_0p5b_public_calib_gptq_model`
Tasks: `20`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 5 / 20 | 0.2500 | 7.9835 | 0.272888 |

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
