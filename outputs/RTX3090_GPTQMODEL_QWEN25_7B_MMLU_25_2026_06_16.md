# Chat Task Benchmark

Model: `/mnt/e/models/Qwen2.5-7B-Instruct-GPTQ-Int4`
Tasks: `25`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 14 / 25 | 0.5600 | 7.5808 | 0.158950 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_14` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_16` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_17` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_18` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_19` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_20` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_21` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_22` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_23` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_24` | `mcq` | true | `B` | `B` |
