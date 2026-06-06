# Chat Task Benchmark

Model: `huihui_ai/qwen2.5-abliterate:7b-instruct`
Tasks: `50`
Task format: `mmlu`
Chat template: `False`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 28 / 50 | 0.5600 | 23.3929 | 0.871185 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_14` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_16` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_17` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_18` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_19` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_20` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_21` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_22` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_23` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_24` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_25` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_26` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_27` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_28` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_29` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_30` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_31` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_32` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_33` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_35` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_36` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_37` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_38` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_39` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_41` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_42` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_43` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_44` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_45` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_47` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_48` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_49` | `mcq` | true | `B` | `B` |
