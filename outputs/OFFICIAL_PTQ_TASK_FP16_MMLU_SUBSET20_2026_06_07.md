# Chat Task Benchmark

Model: `Qwen/Qwen2.5-0.5B-Instruct`
Tasks: `20`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 5 / 20 | 0.2500 | 31.4878 | 0.134118 |

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
