# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 46 / 100 | 0.4600 | 9.7430 | 0.213166 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_300` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_301` | `mcq` | false | `B` | `D. All of these.` |
| baseline | `mmlu_302` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_303` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_304` | `mcq` | true | `A` | `A. Changes` |
| baseline | `mmlu_305` | `mcq` | true | `D` | `D. Violet` |
| baseline | `mmlu_306` | `mcq` | true | `D` | `D. All of these.` |
| baseline | `mmlu_307` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_308` | `mcq` | true | `B` | `B. ordered` |
| baseline | `mmlu_309` | `mcq` | true | `D` | `D. energy` |
| baseline | `mmlu_310` | `mcq` | true | `B` | `B. opposite` |
| baseline | `mmlu_311` | `mcq` | true | `C` | `C. radiation` |
| baseline | `mmlu_312` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_313` | `mcq` | true | `A` | `A. increase.` |
| baseline | `mmlu_314` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_315` | `mcq` | true | `A` | `A. less.` |
| baseline | `mmlu_316` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_317` | `mcq` | false | `B` | `D. All of these` |
| baseline | `mmlu_318` | `mcq` | false | `D` | `A. volume` |
| baseline | `mmlu_319` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_320` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_321` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_322` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_323` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_324` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_325` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_326` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_327` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_328` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_329` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_330` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_331` | `mcq` | true | `D` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_332` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_333` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_334` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_335` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_336` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_337` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_338` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_339` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_340` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_341` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_342` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_343` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_344` | `mcq` | false | `C` | `D. State box.` |
| baseline | `mmlu_345` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_346` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_347` | `mcq` | true | `D` | `D. Both A and B` |
| baseline | `mmlu_348` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_349` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_350` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_351` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_352` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_353` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_354` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_355` | `mcq` | false | `C` | `B. 6` |
| baseline | `mmlu_356` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_357` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_358` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_359` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_360` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_361` | `mcq` | false | `A` | `B. Tcd` |
| baseline | `mmlu_362` | `mcq` | false | `C` | `A. Some large houses are bigger than some apartments.` |
| baseline | `mmlu_363` | `mcq` | false | `A` | `B. Invalid. Counterexample when G is true and H is false.` |
| baseline | `mmlu_364` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_365` | `mcq` | false | `D` | `B. Every house is bigger than every apartment.` |
| baseline | `mmlu_366` | `mcq` | false | `D` | `B. Invalid. Counterexample when K is true and L is false.` |
| baseline | `mmlu_367` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_368` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_369` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_370` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_371` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_372` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_373` | `mcq` | false | `C` | `B. Invalid. Counterexample when E and F are true and G is false.` |
| baseline | `mmlu_374` | `mcq` | false | `D` | `B. Invalid. Counterexample when H and I are true and J is false.` |
| baseline | `mmlu_375` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_376` | `mcq` | true | `D` | `D. None of the above` |
| baseline | `mmlu_377` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_378` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_379` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_380` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_381` | `mcq` | false | `B` | `A. About $300` |
| baseline | `mmlu_382` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_383` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_384` | `mcq` | false | `C` | `B. by 10 fold` |
| baseline | `mmlu_385` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_386` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_387` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_388` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_389` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_390` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_391` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_392` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_393` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_394` | `mcq` | true | `B` | `B. 56%` |
| baseline | `mmlu_395` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_396` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_397` | `mcq` | true | `C` | `C. 82%` |
| baseline | `mmlu_398` | `mcq` | false | `C` | `A. About $3k` |
| baseline | `mmlu_399` | `mcq` | true | `B` | `B` |
