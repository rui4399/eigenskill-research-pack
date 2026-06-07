# Chat Task Benchmark

Model: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_public_calib_awq_model`
Tasks: `20`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 5 / 20 | 0.2500 | 4.5607 | 0.342797 |

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
