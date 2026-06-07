# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 52 / 100 | 0.5200 | 5.3513 | 0.403825 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_300` | `mcq` | false | `A` | `B. 5 N` |
| baseline | `mmlu_301` | `mcq` | true | `B` | `B. volume of fluid.` |
| baseline | `mmlu_302` | `mcq` | true | `B` | `B. passes into the air above` |
| baseline | `mmlu_303` | `mcq` | false | `B` | `A. always.` |
| baseline | `mmlu_304` | `mcq` | true | `A` | `A. changes` |
| baseline | `mmlu_305` | `mcq` | true | `D` | `D. violet` |
| baseline | `mmlu_306` | `mcq` | true | `D` | `D. All of these.` |
| baseline | `mmlu_307` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_308` | `mcq` | true | `B` | `B. ordered` |
| baseline | `mmlu_309` | `mcq` | true | `D` | `D. energy` |
| baseline | `mmlu_310` | `mcq` | true | `B` | `B. opposite` |
| baseline | `mmlu_311` | `mcq` | true | `C` | `C. radiation` |
| baseline | `mmlu_312` | `mcq` | true | `B` | `B. 2 A` |
| baseline | `mmlu_313` | `mcq` | true | `A` | `A. increase.` |
| baseline | `mmlu_314` | `mcq` | false | `B` | `D. mg/4` |
| baseline | `mmlu_315` | `mcq` | true | `A` | `A. less.` |
| baseline | `mmlu_316` | `mcq` | true | `A` | `A. red.` |
| baseline | `mmlu_317` | `mcq` | true | `B` | `B. frequency` |
| baseline | `mmlu_318` | `mcq` | false | `D` | `A. volume` |
| baseline | `mmlu_319` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_320` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_321` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_322` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_323` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_324` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_325` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_326` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_327` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_328` | `mcq` | false | `B` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_329` | `mcq` | false | `C` | `D. Bigger than 1` |
| baseline | `mmlu_330` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_331` | `mcq` | true | `D` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_332` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_333` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_334` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_335` | `mcq` | false | `A` | `B. (i) and (iii) only` |
| baseline | `mmlu_336` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_337` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_338` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_339` | `mcq` | false | `B` | `D. 1 and -3` |
| baseline | `mmlu_340` | `mcq` | true | `D` | `D. Both A and C` |
| baseline | `mmlu_341` | `mcq` | true | `D` | `D. It does not load the circuit at all.` |
| baseline | `mmlu_342` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_343` | `mcq` | true | `A` | `A. 30° to 150°.` |
| baseline | `mmlu_344` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_345` | `mcq` | true | `D` | `D. zero.` |
| baseline | `mmlu_346` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_347` | `mcq` | true | `D` | `D. Both A and B` |
| baseline | `mmlu_348` | `mcq` | true | `A` | `A. 1.5 KV.` |
| baseline | `mmlu_349` | `mcq` | true | `A` | `A. 1MHz to 500 MHz` |
| baseline | `mmlu_350` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_351` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_352` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_353` | `mcq` | true | `D` | `D. convert AC armature current into DC` |
| baseline | `mmlu_354` | `mcq` | false | `C` | `D. none of these` |
| baseline | `mmlu_355` | `mcq` | false | `C` | `B. 6` |
| baseline | `mmlu_356` | `mcq` | true | `A` | `A. First digit from left to right` |
| baseline | `mmlu_357` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_358` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_359` | `mcq` | true | `A` | `A. 111.9 ohm` |
| baseline | `mmlu_360` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_361` | `mcq` | true | `A` | `A. Tdc` |
| baseline | `mmlu_362` | `mcq` | false | `C` | `A. Some large houses are bigger than some apartments.` |
| baseline | `mmlu_363` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_364` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_365` | `mcq` | true | `D` | `D. Some houses are bigger than every apartment.` |
| baseline | `mmlu_366` | `mcq` | false | `D` | `B. Invalid. Counterexample when K is true and L is false` |
| baseline | `mmlu_367` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_368` | `mcq` | false | `D` | `C. H ⊃ ~E` |
| baseline | `mmlu_369` | `mcq` | true | `D` | `D. L ∨ ~L` |
| baseline | `mmlu_370` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_371` | `mcq` | false | `B` | `To solve this problem, we need to construct truth tables for both given statements and then compare them to determine th` |
| baseline | `mmlu_372` | `mcq` | true | `D` | `D. ~~F` |
| baseline | `mmlu_373` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_374` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_375` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_376` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_377` | `mcq` | true | `D` | `D. (∀x)(Px ⊃ Sxj)` |
| baseline | `mmlu_378` | `mcq` | true | `B` | `B. Ijwk` |
| baseline | `mmlu_379` | `mcq` | true | `B` | `B. (∀x)(Ax ⊃ ~Px)` |
| baseline | `mmlu_380` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_381` | `mcq` | false | `B` | `A. About $300` |
| baseline | `mmlu_382` | `mcq` | false | `C` | `D. 82%` |
| baseline | `mmlu_383` | `mcq` | true | `A` | `A. China` |
| baseline | `mmlu_384` | `mcq` | false | `C` | `B. by 10 fold` |
| baseline | `mmlu_385` | `mcq` | true | `A` | `A. Lower respiratory infections` |
| baseline | `mmlu_386` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_387` | `mcq` | false | `C` | `D. 89%` |
| baseline | `mmlu_388` | `mcq` | false | `C` | `A. 18%` |
| baseline | `mmlu_389` | `mcq` | false | `B` | `D. 56%` |
| baseline | `mmlu_390` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_391` | `mcq` | false | `B` | `A. 5%` |
| baseline | `mmlu_392` | `mcq` | false | `C` | `A. 2%` |
| baseline | `mmlu_393` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_394` | `mcq` | true | `B` | `B. 56%` |
| baseline | `mmlu_395` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_396` | `mcq` | false | `A` | `D. 79%` |
| baseline | `mmlu_397` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_398` | `mcq` | false | `C` | `A. About $3k` |
| baseline | `mmlu_399` | `mcq` | true | `B` | `B` |
