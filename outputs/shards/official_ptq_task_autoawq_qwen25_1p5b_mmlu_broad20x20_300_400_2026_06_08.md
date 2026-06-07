# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 50 / 100 | 0.5000 | 12.2661 | 0.152823 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_300` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_301` | `mcq` | true | `B` | `B. volume of fluid.` |
| baseline | `mmlu_302` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_303` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_304` | `mcq` | true | `A` | `A. changes` |
| baseline | `mmlu_305` | `mcq` | true | `D` | `D. violet` |
| baseline | `mmlu_306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_307` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_308` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_309` | `mcq` | true | `D` | `D. energy` |
| baseline | `mmlu_310` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_311` | `mcq` | true | `C` | `C. radiation` |
| baseline | `mmlu_312` | `mcq` | false | `B` | `D. Not enough information to say` |
| baseline | `mmlu_313` | `mcq` | true | `A` | `A. increase.` |
| baseline | `mmlu_314` | `mcq` | false | `B` | `D. mg/4` |
| baseline | `mmlu_315` | `mcq` | true | `A` | `A. less.` |
| baseline | `mmlu_316` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_317` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_318` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_319` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_320` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_321` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_322` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_323` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_324` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_325` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_326` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_327` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_328` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_329` | `mcq` | false | `C` | `D. Bigger than 1` |
| baseline | `mmlu_330` | `mcq` | false | `B` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_331` | `mcq` | true | `D` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_332` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_333` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_334` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_335` | `mcq` | true | `A` | `A. (ii) and (iv) only` |
| baseline | `mmlu_336` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_337` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_338` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_339` | `mcq` | false | `B` | `D. 1 and -3` |
| baseline | `mmlu_340` | `mcq` | true | `D` | `D. Both A and C` |
| baseline | `mmlu_341` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_342` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_343` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_344` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_345` | `mcq` | true | `D` | `D. zero.` |
| baseline | `mmlu_346` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_347` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_348` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_349` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_350` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_351` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_352` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_353` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_354` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_355` | `mcq` | false | `C` | `B. 6` |
| baseline | `mmlu_356` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_357` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_358` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_359` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_360` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_361` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_362` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_363` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_364` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_365` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_366` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_367` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_368` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_369` | `mcq` | true | `D` | `D. L ∨ ~L` |
| baseline | `mmlu_370` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_371` | `mcq` | false | `B` | `D. Inconsistent` |
| baseline | `mmlu_372` | `mcq` | true | `D` | `D. ~~F` |
| baseline | `mmlu_373` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_374` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_375` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_376` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_377` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_378` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_379` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_380` | `mcq` | true | `C` | `C. 40%` |
| baseline | `mmlu_381` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_382` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_383` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_384` | `mcq` | false | `C` | `B. by 10 fold` |
| baseline | `mmlu_385` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_386` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_387` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_388` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_389` | `mcq` | false | `B` | `C. 41%` |
| baseline | `mmlu_390` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_391` | `mcq` | false | `B` | `A. 5%` |
| baseline | `mmlu_392` | `mcq` | false | `C` | `D. 18%` |
| baseline | `mmlu_393` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_394` | `mcq` | true | `B` | `B. 56%` |
| baseline | `mmlu_395` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_396` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_397` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_398` | `mcq` | false | `C` | `B. About $8k` |
| baseline | `mmlu_399` | `mcq` | true | `B` | `B.` |
