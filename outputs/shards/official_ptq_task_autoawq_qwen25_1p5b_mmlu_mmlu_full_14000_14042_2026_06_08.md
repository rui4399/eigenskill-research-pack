# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `42`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 36 / 42 | 0.8571 | 12.9006 | 0.158742 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_14000` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_14001` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_14002` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_14003` | `mcq` | true | `B` | `B. 1948` |
| baseline | `mmlu_14004` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14005` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14006` | `mcq` | true | `B` | `B. 1517` |
| baseline | `mmlu_14007` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_14008` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_14009` | `mcq` | true | `D` | `D. Daoism` |
| baseline | `mmlu_14010` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14011` | `mcq` | true | `C` | `C. Heart-mind` |
| baseline | `mmlu_14012` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14013` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_14014` | `mcq` | true | `B` | `B. The Shi'a` |
| baseline | `mmlu_14015` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_14016` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14017` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14018` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_14019` | `mcq` | true | `D` | `D. The Classic of Changes` |
| baseline | `mmlu_14020` | `mcq` | true | `D` | `D. Eleusis` |
| baseline | `mmlu_14021` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14022` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_14023` | `mcq` | true | `B` | `B. Samsara` |
| baseline | `mmlu_14024` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_14025` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_14026` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_14027` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_14028` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14029` | `mcq` | true | `B` | `B. The Crescent` |
| baseline | `mmlu_14030` | `mcq` | true | `C` | `C. Inspiration for personal meditation throughout the day` |
| baseline | `mmlu_14031` | `mcq` | true | `D` | `D. Gemarah` |
| baseline | `mmlu_14032` | `mcq` | true | `A` | `A. A ritual circumciser` |
| baseline | `mmlu_14033` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_14034` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_14035` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_14036` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_14037` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_14038` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_14039` | `mcq` | true | `B` | `B. of the same substance` |
| baseline | `mmlu_14040` | `mcq` | true | `B` | `B. Izanagi` |
| baseline | `mmlu_14041` | `mcq` | true | `A` | `A` |
