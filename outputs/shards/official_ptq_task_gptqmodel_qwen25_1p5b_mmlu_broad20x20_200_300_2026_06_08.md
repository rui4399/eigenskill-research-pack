# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 58 / 100 | 0.5800 | 8.8386 | 0.202222 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_200` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_201` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_202` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_203` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_204` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_205` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_206` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_207` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_208` | `mcq` | false | `D` | `B. Hydrogen` |
| baseline | `mmlu_209` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_210` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_211` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_212` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_213` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_214` | `mcq` | true | `B` | `B. Laniakea` |
| baseline | `mmlu_215` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_216` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_217` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_218` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_219` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_220` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_221` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_222` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_223` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_224` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_225` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_226` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_227` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_228` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_229` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_230` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_231` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_232` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_233` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_234` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_235` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_236` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_237` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_238` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_239` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_240` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_241` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_242` | `mcq` | false | `D` | `B. 3` |
| baseline | `mmlu_243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_244` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_245` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_246` | `mcq` | false | `A` | `B. Alpha particles` |
| baseline | `mmlu_247` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_248` | `mcq` | true | `C` | `C. 1:6` |
| baseline | `mmlu_249` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_250` | `mcq` | true | `D` | `D. 11.30 ppm` |
| baseline | `mmlu_251` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_252` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_253` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_254` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_255` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_256` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_257` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_258` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_259` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_260` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_261` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_262` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_263` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_264` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_265` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_266` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_267` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_268` | `mcq` | false | `C` | `D. III only` |
| baseline | `mmlu_269` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_270` | `mcq` | true | `D` | `D. 45` |
| baseline | `mmlu_271` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_272` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_273` | `mcq` | false | `B` | `10` |
| baseline | `mmlu_274` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_275` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_276` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_277` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_278` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_279` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_280` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_281` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_282` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_283` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_284` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_285` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_286` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_287` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_288` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_289` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_290` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_291` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_292` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_293` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_294` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_295` | `mcq` | false | `B` | `D. Not enough information given.` |
| baseline | `mmlu_296` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_297` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_298` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_299` | `mcq` | true | `B` | `B.` |
