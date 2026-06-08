# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `3000`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 1601 / 3000 | 0.5337 | 11.1693 | 0.152503 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | true | `B` | `B. 4` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `A. 8` |
| baseline | `mmlu_2` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4` | `mcq` | false | `B` | `C. 0` |
| baseline | `mmlu_5` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8` | `mcq` | true | `B` | `B. 4` |
| baseline | `mmlu_9` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_14` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_16` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_17` | `mcq` | true | `C` | `C. (1,6)` |
| baseline | `mmlu_18` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_19` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_20` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_21` | `mcq` | false | `A` | `C. 0` |
| baseline | `mmlu_22` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_23` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_24` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_25` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_26` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_27` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_28` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_29` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_30` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_31` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_32` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_33` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_35` | `mcq` | false | `B` | `C. 2` |
| baseline | `mmlu_36` | `mcq` | false | `D` | `A. 0` |
| baseline | `mmlu_37` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_38` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_39` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `A. 0` |
| baseline | `mmlu_41` | `mcq` | false | `A` | `B. 3` |
| baseline | `mmlu_42` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_43` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_44` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_45` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_47` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_48` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_49` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_50` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_51` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_52` | `mcq` | false | `A` | `D. 2` |
| baseline | `mmlu_53` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_54` | `mcq` | false | `B` | `C. 1` |
| baseline | `mmlu_55` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_56` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_57` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_58` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_59` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_60` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_61` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_62` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_63` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_64` | `mcq` | false | `B` | `D. 0` |
| baseline | `mmlu_65` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_66` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_67` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_68` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_69` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_70` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_71` | `mcq` | true | `C` | `C. 2` |
| baseline | `mmlu_72` | `mcq` | false | `D` | `A. 1` |
| baseline | `mmlu_73` | `mcq` | false | `B` | `A. 0` |
| baseline | `mmlu_74` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_75` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_76` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_77` | `mcq` | true | `A` | `A. 0` |
| baseline | `mmlu_78` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_79` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_80` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_81` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_82` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_83` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_84` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_85` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_86` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_87` | `mcq` | true | `A` | `A. -19` |
| baseline | `mmlu_88` | `mcq` | true | `A` | `A. 0` |
| baseline | `mmlu_89` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_90` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_91` | `mcq` | true | `B` | `B. 4Z, 2 + 4Z` |
| baseline | `mmlu_92` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_93` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_94` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_95` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_96` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_97` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_98` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_99` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_100` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_101` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_102` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_103` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_104` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_105` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_106` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_107` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_108` | `mcq` | false | `C` | `B. eight weeks post-fertilization.` |
| baseline | `mmlu_109` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_110` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_111` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_112` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_113` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_114` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_115` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_116` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_117` | `mcq` | true | `D` | `D. Testes` |
| baseline | `mmlu_118` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_119` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_120` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_121` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_122` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_123` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_124` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_125` | `mcq` | true | `C` | `C. Nitrogen` |
| baseline | `mmlu_126` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_127` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_128` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_129` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_130` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_131` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_132` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_133` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_134` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_135` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_136` | `mcq` | true | `D` | `D. Spleen` |
| baseline | `mmlu_137` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_138` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_139` | `mcq` | true | `C` | `C. Liver` |
| baseline | `mmlu_140` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_141` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_142` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_143` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_144` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_145` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_146` | `mcq` | true | `B` | `B. Lower leg` |
| baseline | `mmlu_147` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_148` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_149` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_150` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_151` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_153` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_154` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_155` | `mcq` | false | `D` | `B. Outward` |
| baseline | `mmlu_156` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_157` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_158` | `mcq` | true | `D` | `D. Synapse` |
| baseline | `mmlu_159` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_160` | `mcq` | true | `D` | `D. Pancreas` |
| baseline | `mmlu_161` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_162` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_163` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_164` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_165` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_166` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_167` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_168` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_169` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_170` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_171` | `mcq` | true | `A` | `A. Acetylcholine` |
| baseline | `mmlu_172` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_173` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_174` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_175` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_176` | `mcq` | false | `A` | `B. flaccid paralysis.` |
| baseline | `mmlu_177` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_178` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_179` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_180` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_181` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_182` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_183` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_184` | `mcq` | false | `B` | `A. The roof` |
| baseline | `mmlu_185` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_186` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_187` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_188` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_189` | `mcq` | true | `A` | `A. Collagen` |
| baseline | `mmlu_190` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_191` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_193` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_194` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_195` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_196` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_197` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_198` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_199` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_200` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_201` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_202` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_203` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_204` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_205` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_206` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_207` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_208` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_209` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_210` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_211` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_212` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_213` | `mcq` | true | `A` | `A. Alveoli` |
| baseline | `mmlu_214` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_215` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_216` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_217` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_218` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_219` | `mcq` | true | `D` | `D. The cerebellum` |
| baseline | `mmlu_220` | `mcq` | true | `C` | `C. Ileum` |
| baseline | `mmlu_221` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_222` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_223` | `mcq` | false | `B` | `A. The maxillary bone` |
| baseline | `mmlu_224` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_225` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_226` | `mcq` | true | `C` | `C. Olfactory` |
| baseline | `mmlu_227` | `mcq` | false | `C` | `B. pons` |
| baseline | `mmlu_228` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_229` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_230` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_231` | `mcq` | true | `D` | `D. Pituitary` |
| baseline | `mmlu_232` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_233` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_234` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_235` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_236` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_237` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_238` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_239` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_240` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_241` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_242` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_243` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_244` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_245` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_246` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_247` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_248` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_249` | `mcq` | true | `B` | `B. Laniakea` |
| baseline | `mmlu_250` | `mcq` | true | `C` | `C. Jupiter` |
| baseline | `mmlu_251` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_252` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_253` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_254` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_255` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_256` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_257` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_258` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_259` | `mcq` | true | `C` | `C. 300 Kelvin` |
| baseline | `mmlu_260` | `mcq` | false | `D` | `A. Callisto` |
| baseline | `mmlu_261` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_262` | `mcq` | true | `D` | `D. Phoenix Mars Lander` |
| baseline | `mmlu_263` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_264` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_265` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_266` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_267` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_268` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_269` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_270` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_271` | `mcq` | true | `A` | `A. The path of the Sun in the sky throughout a year.` |
| baseline | `mmlu_272` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_273` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_274` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_275` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_276` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_277` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_278` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_279` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_280` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_281` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_282` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_283` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_284` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_285` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_286` | `mcq` | false | `D` | `A. 4:1` |
| baseline | `mmlu_287` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_288` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_289` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_290` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_291` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_292` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_293` | `mcq` | true | `C` | `C. Higher in the sky` |
| baseline | `mmlu_294` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_295` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_297` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_298` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_299` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_300` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_301` | `mcq` | false | `B` | `A. 100 times brighter` |
| baseline | `mmlu_302` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_303` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_304` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_305` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_307` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_308` | `mcq` | true | `D` | `D. Hawking radiation` |
| baseline | `mmlu_309` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_310` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_311` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_312` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_313` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_314` | `mcq` | true | `C` | `C. 2` |
| baseline | `mmlu_315` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_316` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_317` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_318` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_319` | `mcq` | false | `A` | `B. presence of an atmosphere` |
| baseline | `mmlu_320` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_321` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_322` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_323` | `mcq` | false | `C` | `D. New only` |
| baseline | `mmlu_324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_325` | `mcq` | false | `D` | `B. 2.2x1014kg` |
| baseline | `mmlu_326` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_327` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_328` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_329` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_330` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_331` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_332` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_333` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_334` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_335` | `mcq` | true | `A` | `A. About 6 meters` |
| baseline | `mmlu_336` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_337` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_338` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_339` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_340` | `mcq` | false | `A` | `B. Helium` |
| baseline | `mmlu_341` | `mcq` | false | `B` | `C. Not enough information. It will depend on the inclination of the new orbit.` |
| baseline | `mmlu_342` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_343` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_344` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_345` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_346` | `mcq` | true | `D` | `D. 23.5 degrees` |
| baseline | `mmlu_347` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_348` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_349` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_350` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_351` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_352` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_353` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_354` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_355` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_356` | `mcq` | true | `B` | `B. 11` |
| baseline | `mmlu_357` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_358` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_359` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_360` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_361` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_362` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_363` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_364` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_365` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_366` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_367` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_368` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_369` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_370` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_371` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_372` | `mcq` | true | `D` | `D. CO2` |
| baseline | `mmlu_373` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_374` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_375` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_376` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_377` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_378` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_379` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_380` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_381` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_382` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_383` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_384` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_385` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_386` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_387` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_388` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_389` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_390` | `mcq` | false | `D` | `C. Work-play balance` |
| baseline | `mmlu_391` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_392` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_393` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_394` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_395` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_396` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_397` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_398` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_399` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_400` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_401` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_402` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_403` | `mcq` | true | `A` | `A. To make a profit` |
| baseline | `mmlu_404` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_405` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_406` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_407` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_408` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_409` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_410` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_411` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_412` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_413` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_414` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_415` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_416` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_417` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_418` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_419` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_420` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_421` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_422` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_423` | `mcq` | true | `B` | `B. Green Marketing` |
| baseline | `mmlu_424` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_425` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_426` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_427` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_428` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_429` | `mcq` | true | `A` | `A. Moral imagination` |
| baseline | `mmlu_430` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_431` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_432` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_433` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_434` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_435` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_436` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_437` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_438` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_439` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_440` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_441` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_442` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_443` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_444` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_445` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_446` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_447` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_448` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_449` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_450` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_451` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_452` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_453` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_454` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_455` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_456` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_457` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_458` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_459` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_460` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_461` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_462` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_463` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_464` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_465` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_466` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_467` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_468` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_469` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_470` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_471` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_472` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_473` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_474` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_475` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_476` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_477` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_478` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_479` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_480` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_481` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_482` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_483` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_484` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_485` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_486` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_487` | `mcq` | true | `A` | `A. 18 gauge.` |
| baseline | `mmlu_488` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_489` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_490` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_491` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_492` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_493` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_495` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_496` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_497` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_498` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_499` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_500` | `mcq` | true | `B` | `B. glucose-1-phosphate.` |
| baseline | `mmlu_501` | `mcq` | true | `B` | `B. actin and myosin.` |
| baseline | `mmlu_502` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_503` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_504` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_505` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_506` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_507` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_508` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_509` | `mcq` | true | `A` | `A. 30 minutes.` |
| baseline | `mmlu_510` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_511` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_512` | `mcq` | true | `B` | `B. When the catheter is blocked.` |
| baseline | `mmlu_513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_514` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_515` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_516` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_517` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_518` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_519` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_520` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_521` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_522` | `mcq` | false | `D` | `A. 10-12 breaths per minute.` |
| baseline | `mmlu_523` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_524` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_526` | `mcq` | false | `D` | `A. 400 kJ/min.` |
| baseline | `mmlu_527` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_528` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_529` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_530` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_531` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_532` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_533` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_534` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_535` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_536` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_537` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_538` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_539` | `mcq` | false | `C` | `D. 1 mmHg.` |
| baseline | `mmlu_540` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_541` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_542` | `mcq` | false | `D` | `B. 93` |
| baseline | `mmlu_543` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_544` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_545` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_546` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_547` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_548` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_549` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_550` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_551` | `mcq` | false | `A` | `D. Left ventricular hypertrophy` |
| baseline | `mmlu_552` | `mcq` | false | `D` | `B. 10%` |
| baseline | `mmlu_553` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_554` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_555` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_556` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_557` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_558` | `mcq` | true | `C` | `C. 100/minute.` |
| baseline | `mmlu_559` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_560` | `mcq` | false | `D` | `B. After using their bronchodilator inhaler.` |
| baseline | `mmlu_561` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_562` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_563` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_564` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_565` | `mcq` | true | `B` | `B. Insulin` |
| baseline | `mmlu_566` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_567` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_568` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_569` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_570` | `mcq` | false | `B` | `A. 156` |
| baseline | `mmlu_571` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_572` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_573` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_574` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_575` | `mcq` | true | `D` | `D. Call for assistance from a medical practitioner.` |
| baseline | `mmlu_576` | `mcq` | false | `D` | `A. warm.` |
| baseline | `mmlu_577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_578` | `mcq` | true | `C` | `C. Alzheimer's disease.` |
| baseline | `mmlu_579` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_580` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_581` | `mcq` | true | `C` | `C. 80% or below.` |
| baseline | `mmlu_582` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_583` | `mcq` | false | `D` | `B. 50` |
| baseline | `mmlu_584` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_585` | `mcq` | true | `B` | `B. 2 seconds.` |
| baseline | `mmlu_586` | `mcq` | false | `B` | `A. 0.192` |
| baseline | `mmlu_587` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_588` | `mcq` | true | `C` | `C. Reduced amount of gastric acid.` |
| baseline | `mmlu_589` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_590` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_591` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_592` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_593` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_594` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_595` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_596` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_597` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_598` | `mcq` | true | `C` | `C. 350` |
| baseline | `mmlu_599` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_600` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_601` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_602` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_603` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_604` | `mcq` | true | `C` | `C. Carnosine` |
| baseline | `mmlu_605` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_606` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_607` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_608` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_609` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_610` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_611` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_612` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_613` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_614` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_615` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_616` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_617` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_618` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_619` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_620` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_621` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_622` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_623` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_624` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_625` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_626` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_627` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_628` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_629` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_630` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_631` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_632` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_633` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_634` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_635` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_636` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_637` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_638` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_639` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_640` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_641` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_642` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_643` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_644` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_645` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_646` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_647` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_648` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_649` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_650` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_651` | `mcq` | false | `B` | `A. 10 litres per minute of each other.` |
| baseline | `mmlu_652` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_653` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_654` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_655` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_656` | `mcq` | true | `A` | `A. Thymine` |
| baseline | `mmlu_657` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_658` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_659` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_660` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_661` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_662` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_663` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_664` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_665` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_666` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_667` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_668` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_669` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_670` | `mcq` | false | `D` | `A. 24 hours.` |
| baseline | `mmlu_671` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_672` | `mcq` | true | `D` | `D. 46` |
| baseline | `mmlu_673` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_674` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_675` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_676` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_677` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_678` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_679` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_680` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_681` | `mcq` | false | `D` | `A. about 10 seconds.` |
| baseline | `mmlu_682` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_683` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_684` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_685` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_686` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_687` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_689` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_690` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_691` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_692` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_693` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_694` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_695` | `mcq` | true | `B` | `B. Give drugs regularly with provision for additional 'as required' pain relief for breakthrough pain.` |
| baseline | `mmlu_696` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_697` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_698` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_699` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_700` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_701` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_702` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_703` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_704` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_705` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_706` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_707` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_708` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_709` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_710` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_711` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_712` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_713` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_714` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_715` | `mcq` | true | `A` | `A. Lysozyme.` |
| baseline | `mmlu_716` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_717` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_718` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_719` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_720` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_721` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_722` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_723` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_724` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_725` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_726` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_727` | `mcq` | true | `C` | `C. 300 kJ` |
| baseline | `mmlu_728` | `mcq` | false | `B` | `C. 24 hours.` |
| baseline | `mmlu_729` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_730` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_731` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_732` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_733` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_734` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_735` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_736` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_737` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_738` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_739` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_740` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_741` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_742` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_743` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_744` | `mcq` | true | `B` | `B. The pancreas.` |
| baseline | `mmlu_745` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_746` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_747` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_748` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_749` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_750` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_751` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_752` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_753` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_754` | `mcq` | true | `A` | `A. amnion` |
| baseline | `mmlu_755` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_756` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_757` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_758` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_759` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_760` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_761` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_762` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_763` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_764` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_765` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_766` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_767` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_768` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_769` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_770` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_771` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_772` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_773` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_774` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_775` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_776` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_777` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_778` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_779` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_780` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_781` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_782` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_783` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_784` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_785` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_786` | `mcq` | false | `D` | `C. 5′ GTT AGC 3′` |
| baseline | `mmlu_787` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_788` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_789` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_790` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_791` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_792` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_793` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_794` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_795` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_796` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_797` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_798` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_799` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_800` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_801` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_802` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_803` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_804` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_805` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_806` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_807` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_808` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_809` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_810` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_811` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_812` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_813` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_814` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_815` | `mcq` | false | `C` | `B. Two` |
| baseline | `mmlu_816` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_817` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_818` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_819` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_820` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_821` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_822` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_823` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_824` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_825` | `mcq` | true | `A` | `A. 2%` |
| baseline | `mmlu_826` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_827` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_828` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_829` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_830` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_831` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_832` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_833` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_834` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_835` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_836` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_837` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_838` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_839` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_840` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_841` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_842` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_843` | `mcq` | true | `C` | `C. Microfilaments` |
| baseline | `mmlu_844` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_845` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_846` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_847` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_848` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_849` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_850` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_851` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_852` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_853` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_854` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_855` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_856` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_857` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_858` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_859` | `mcq` | false | `A` | `B. Reduction of NADP+ to NADPH` |
| baseline | `mmlu_860` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_861` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_862` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_863` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_864` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_865` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_866` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_867` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_868` | `mcq` | false | `C` | `A. The amplitude of the action potential` |
| baseline | `mmlu_869` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_870` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_871` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_872` | `mcq` | true | `C` | `C. nucleosome` |
| baseline | `mmlu_873` | `mcq` | true | `B` | `B. Photoperiod` |
| baseline | `mmlu_874` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_875` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_876` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_877` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_878` | `mcq` | true | `D` | `D. endosperm` |
| baseline | `mmlu_879` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_880` | `mcq` | true | `C` | `C. osmosis` |
| baseline | `mmlu_881` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_882` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_883` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_884` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_885` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_886` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_887` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_888` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_889` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_890` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_891` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_892` | `mcq` | true | `A` | `A. Chitin` |
| baseline | `mmlu_893` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_894` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_895` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_896` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_897` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_898` | `mcq` | false | `D` | `A. 2` |
| baseline | `mmlu_899` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_900` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_901` | `mcq` | false | `B` | `C. 5 lines` |
| baseline | `mmlu_902` | `mcq` | false | `A` | `B. Alpha particles` |
| baseline | `mmlu_903` | `mcq` | true | `D` | `D. Unpaired electrons` |
| baseline | `mmlu_904` | `mcq` | false | `C` | `B. 1:3` |
| baseline | `mmlu_905` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_906` | `mcq` | false | `D` | `B. 5.03 ppm` |
| baseline | `mmlu_907` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_908` | `mcq` | true | `A` | `A. 4.6 mT` |
| baseline | `mmlu_909` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_910` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_911` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_912` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_913` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_914` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_915` | `mcq` | false | `B` | `A. 23.56 GHz` |
| baseline | `mmlu_916` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_917` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_918` | `mcq` | false | `D` | `C. 1.0 × 10^−9` |
| baseline | `mmlu_919` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_920` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_921` | `mcq` | false | `A` | `B. 19F` |
| baseline | `mmlu_922` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_923` | `mcq` | false | `D` | `B. 3.98 ppm` |
| baseline | `mmlu_924` | `mcq` | false | `D` | `B. I and II only` |
| baseline | `mmlu_925` | `mcq` | false | `C` | `D. 0.015 M` |
| baseline | `mmlu_926` | `mcq` | false | `B` | `C. Both accurate and precise` |
| baseline | `mmlu_927` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_928` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_929` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_930` | `mcq` | true | `A` | `A. g = 2.002` |
| baseline | `mmlu_931` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_932` | `mcq` | false | `C` | `A. 0.5 T` |
| baseline | `mmlu_933` | `mcq` | false | `B` | `A. 0.0471 Hz` |
| baseline | `mmlu_934` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_935` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_936` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_937` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_938` | `mcq` | true | `B` | `B. NH2⁻` |
| baseline | `mmlu_939` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_940` | `mcq` | false | `D` | `A. Q = 1012` |
| baseline | `mmlu_941` | `mcq` | false | `A` | `C. 91.6 kHz` |
| baseline | `mmlu_942` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_943` | `mcq` | false | `B` | `A. 3.72 mT` |
| baseline | `mmlu_944` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_945` | `mcq` | true | `D` | `D. 9.4 mCi` |
| baseline | `mmlu_946` | `mcq` | false | `C` | `D. 0` |
| baseline | `mmlu_947` | `mcq` | false | `D` | `C. Na2S` |
| baseline | `mmlu_948` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_949` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_950` | `mcq` | false | `C` | `A. 0.95` |
| baseline | `mmlu_951` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_952` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_953` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_954` | `mcq` | true | `A` | `A. 3.74 T` |
| baseline | `mmlu_955` | `mcq` | false | `A` | `D. NaCl` |
| baseline | `mmlu_956` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_957` | `mcq` | true | `D` | `D. 1.71 x 10^-5` |
| baseline | `mmlu_958` | `mcq` | false | `B` | `C. 19F` |
| baseline | `mmlu_959` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_960` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_961` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_962` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_963` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_964` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_965` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_966` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_967` | `mcq` | false | `D` | `B. dipole moment` |
| baseline | `mmlu_968` | `mcq` | false | `A` | `B. 5` |
| baseline | `mmlu_969` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_970` | `mcq` | true | `B` | `B. Ultraviolet` |
| baseline | `mmlu_971` | `mcq` | true | `C` | `C. 4.2 ns` |
| baseline | `mmlu_972` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_973` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_974` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_975` | `mcq` | true | `B` | `B. H3O+ / H2O` |
| baseline | `mmlu_976` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_977` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_978` | `mcq` | false | `D` | `A. 0.721 s` |
| baseline | `mmlu_979` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_980` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_981` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_982` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_983` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_984` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_985` | `mcq` | false | `B` | `C. 11,070 ppm` |
| baseline | `mmlu_986` | `mcq` | true | `A` | `A. 4.19 ms` |
| baseline | `mmlu_987` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_988` | `mcq` | false | `D` | `C. 5 lines` |
| baseline | `mmlu_989` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_990` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_991` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_992` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_993` | `mcq` | false | `C` | `A. 54.91 MHz` |
| baseline | `mmlu_994` | `mcq` | false | `B` | `A. 21` |
| baseline | `mmlu_995` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_996` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_997` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_998` | `mcq` | true | `B` | `B. 1:3.5` |
| baseline | `mmlu_999` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1000` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1001` | `mcq` | false | `C` | `D. M = 6, m = 4` |
| baseline | `mmlu_1002` | `mcq` | false | `C` | `D. I and III only` |
| baseline | `mmlu_1003` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1004` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1005` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1006` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1007` | `mcq` | false | `A` | `B. n + 1` |
| baseline | `mmlu_1008` | `mcq` | true | `A` | `A. 3` |
| baseline | `mmlu_1009` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1010` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1011` | `mcq` | true | `D` | `D. None of the above` |
| baseline | `mmlu_1012` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1013` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1014` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1015` | `mcq` | false | `D` | `C. I and II only` |
| baseline | `mmlu_1016` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1017` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1018` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1019` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1020` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1021` | `mcq` | true | `D` | `D. I and II` |
| baseline | `mmlu_1022` | `mcq` | true | `C` | `C. Symbol Table` |
| baseline | `mmlu_1023` | `mcq` | true | `D` | `D. Quicksort` |
| baseline | `mmlu_1024` | `mcq` | true | `D` | `D. II and III only` |
| baseline | `mmlu_1025` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1026` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1027` | `mcq` | true | `D` | `D. I, II, and IV` |
| baseline | `mmlu_1028` | `mcq` | false | `D` | `B. 999` |
| baseline | `mmlu_1029` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1030` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1031` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1032` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1033` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1034` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1035` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1036` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1037` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1038` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1039` | `mcq` | false | `D` | `A. 1/(n^2)` |
| baseline | `mmlu_1040` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1041` | `mcq` | true | `C` | `C. III only` |
| baseline | `mmlu_1042` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1043` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1044` | `mcq` | false | `A` | `B. 256` |
| baseline | `mmlu_1045` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1046` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1047` | `mcq` | false | `B` | `D. II and III only` |
| baseline | `mmlu_1048` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1049` | `mcq` | true | `C` | `C. Merge sort` |
| baseline | `mmlu_1050` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1051` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1052` | `mcq` | true | `D` | `D. (I, II) and (I, III) only` |
| baseline | `mmlu_1053` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1054` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1055` | `mcq` | false | `D` | `C. III only` |
| baseline | `mmlu_1056` | `mcq` | true | `D` | `D. II and III` |
| baseline | `mmlu_1057` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1058` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1059` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1060` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1061` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1062` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1063` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1064` | `mcq` | false | `B` | `C. 5/3` |
| baseline | `mmlu_1065` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1066` | `mcq` | false | `D` | `C. I and III only` |
| baseline | `mmlu_1067` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1068` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1069` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1070` | `mcq` | true | `D` | `D. II and III only` |
| baseline | `mmlu_1071` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1072` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1073` | `mcq` | false | `B` | `D. 1/w + 1/x < 1/y + 1/z` |
| baseline | `mmlu_1074` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1075` | `mcq` | false | `D` | `C. 38%` |
| baseline | `mmlu_1076` | `mcq` | false | `B` | `A. I only` |
| baseline | `mmlu_1077` | `mcq` | false | `C` | `B. Maximum level of nesting` |
| baseline | `mmlu_1078` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1079` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1080` | `mcq` | false | `D` | `B. O(N log N)` |
| baseline | `mmlu_1081` | `mcq` | false | `D` | `B. 4 / 9` |
| baseline | `mmlu_1082` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1083` | `mcq` | false | `B` | `C. I and II only` |
| baseline | `mmlu_1084` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_1085` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1086` | `mcq` | false | `C` | `B. 256` |
| baseline | `mmlu_1087` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1088` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1089` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1090` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1091` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1092` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1093` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1094` | `mcq` | true | `C` | `C. 1.6 microseconds` |
| baseline | `mmlu_1095` | `mcq` | true | `D` | `D. 99.80%` |
| baseline | `mmlu_1096` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1097` | `mcq` | false | `D` | `B. 1` |
| baseline | `mmlu_1098` | `mcq` | true | `D` | `D. n = 2 and r = 6` |
| baseline | `mmlu_1099` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_1100` | `mcq` | false | `C` | `D. 12/125` |
| baseline | `mmlu_1101` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1102` | `mcq` | false | `C` | `B. 6*sqrt(2)` |
| baseline | `mmlu_1103` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1104` | `mcq` | false | `C` | `D. III only` |
| baseline | `mmlu_1105` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1106` | `mcq` | true | `D` | `D. 45` |
| baseline | `mmlu_1107` | `mcq` | true | `B` | `B. 15/64` |
| baseline | `mmlu_1108` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1109` | `mcq` | false | `B` | `D. 13` |
| baseline | `mmlu_1110` | `mcq` | false | `D` | `C. 0.81` |
| baseline | `mmlu_1111` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_1112` | `mcq` | false | `B` | `A. I only` |
| baseline | `mmlu_1113` | `mcq` | false | `C` | `A. -1/4` |
| baseline | `mmlu_1114` | `mcq` | false | `D` | `C. I and III only` |
| baseline | `mmlu_1115` | `mcq` | true | `A` | `A. 3` |
| baseline | `mmlu_1116` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1117` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_1118` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_1119` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1120` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1121` | `mcq` | true | `D` | `D. III only` |
| baseline | `mmlu_1122` | `mcq` | false | `D` | `A. 9/2 days` |
| baseline | `mmlu_1123` | `mcq` | false | `A` | `C. sqrt(2)` |
| baseline | `mmlu_1124` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1125` | `mcq` | false | `B` | `D. 15` |
| baseline | `mmlu_1126` | `mcq` | false | `C` | `D. S(n) is not true for any n >= n0` |
| baseline | `mmlu_1127` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1128` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1129` | `mcq` | false | `C` | `D. 4` |
| baseline | `mmlu_1130` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_1131` | `mcq` | false | `D` | `B. (x^2 + y^2 + z^2 + 8)^2 = 8 + 36(x^2 + z^2)` |
| baseline | `mmlu_1132` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1133` | `mcq` | true | `A` | `A. 2` |
| baseline | `mmlu_1134` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1135` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1136` | `mcq` | true | `B` | `B. a point` |
| baseline | `mmlu_1137` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1138` | `mcq` | false | `D` | `A. 3` |
| baseline | `mmlu_1139` | `mcq` | true | `A` | `A. II only` |
| baseline | `mmlu_1140` | `mcq` | false | `D` | `C. 5` |
| baseline | `mmlu_1141` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1142` | `mcq` | false | `B` | `A. π/12` |
| baseline | `mmlu_1143` | `mcq` | true | `B` | `B. pi` |
| baseline | `mmlu_1144` | `mcq` | true | `C` | `C. (I) and (IV)` |
| baseline | `mmlu_1145` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1146` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1147` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1148` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1149` | `mcq` | true | `C` | `C. 12*sqrt(3)` |
| baseline | `mmlu_1150` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1151` | `mcq` | true | `D` | `D. \|x + y\| = \|x\| + \|y\|` |
| baseline | `mmlu_1152` | `mcq` | true | `B` | `B. 5` |
| baseline | `mmlu_1153` | `mcq` | false | `D` | `C. 0 and 1 only` |
| baseline | `mmlu_1154` | `mcq` | false | `C` | `B. π` |
| baseline | `mmlu_1155` | `mcq` | true | `A` | `A. 9` |
| baseline | `mmlu_1156` | `mcq` | false | `B` | `A. None` |
| baseline | `mmlu_1157` | `mcq` | false | `A` | `C. 10^(20) - 2^(10)` |
| baseline | `mmlu_1158` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1159` | `mcq` | false | `D` | `C. 1/2` |
| baseline | `mmlu_1160` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1161` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_1162` | `mcq` | false | `C` | `B. -2` |
| baseline | `mmlu_1163` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1164` | `mcq` | true | `A` | `A. π/3` |
| baseline | `mmlu_1165` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1166` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1167` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1168` | `mcq` | false | `D` | `B. f(e^c)` |
| baseline | `mmlu_1169` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_1170` | `mcq` | false | `C` | `A. 1/(2e)` |
| baseline | `mmlu_1171` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1172` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1173` | `mcq` | true | `C` | `C. 0` |
| baseline | `mmlu_1174` | `mcq` | false | `B` | `C. x^2/4` |
| baseline | `mmlu_1175` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1176` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1177` | `mcq` | true | `B` | `B. 30` |
| baseline | `mmlu_1178` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_1179` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1180` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1181` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1182` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1183` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_1184` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1185` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1186` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1187` | `mcq` | false | `C` | `D. I and III only` |
| baseline | `mmlu_1188` | `mcq` | false | `C` | `B. 7/12` |
| baseline | `mmlu_1189` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1190` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1191` | `mcq` | false | `D` | `C. 0 or 1` |
| baseline | `mmlu_1192` | `mcq` | false | `C` | `A. closed` |
| baseline | `mmlu_1193` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1194` | `mcq` | false | `D` | `C. 28` |
| baseline | `mmlu_1195` | `mcq` | false | `A` | `B. (-1, 4)` |
| baseline | `mmlu_1196` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1197` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1198` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1199` | `mcq` | false | `D` | `A. about 10 seconds.` |
| baseline | `mmlu_1200` | `mcq` | true | `A` | `A. 13 m/s^2` |
| baseline | `mmlu_1201` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1202` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1203` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1204` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1205` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1206` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1207` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1208` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1209` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1210` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1211` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1212` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1213` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1214` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1215` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1216` | `mcq` | true | `C` | `C. I and III` |
| baseline | `mmlu_1217` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1218` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1219` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1220` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1221` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1222` | `mcq` | false | `C` | `A. 941 Hz` |
| baseline | `mmlu_1223` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1224` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1225` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1226` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1227` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1228` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1229` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1230` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1231` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1232` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1233` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1234` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1235` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1236` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1237` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1238` | `mcq` | false | `D` | `B. Endometrium, cell division` |
| baseline | `mmlu_1239` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1240` | `mcq` | false | `C` | `D. cannot be determined` |
| baseline | `mmlu_1241` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1242` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1243` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1244` | `mcq` | true | `B` | `B. Maintains alveoli in an open state` |
| baseline | `mmlu_1245` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1246` | `mcq` | true | `D` | `D. Replenish fluids with filtered water.` |
| baseline | `mmlu_1247` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1248` | `mcq` | true | `C` | `C. 300 kJ` |
| baseline | `mmlu_1249` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1250` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1251` | `mcq` | true | `B` | `B. Insulin` |
| baseline | `mmlu_1252` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1253` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1254` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1255` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1256` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1257` | `mcq` | true | `D` | `D. I and IV` |
| baseline | `mmlu_1258` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1259` | `mcq` | false | `C` | `A. I only` |
| baseline | `mmlu_1260` | `mcq` | false | `D` | `A. 400 kJ/min.` |
| baseline | `mmlu_1261` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1262` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1263` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1264` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1265` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1266` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1267` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1268` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1269` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1270` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1271` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1272` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1273` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1274` | `mcq` | true | `C` | `C. Hyperpolarization` |
| baseline | `mmlu_1275` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1276` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1277` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1278` | `mcq` | false | `B` | `D. I and III and IV only` |
| baseline | `mmlu_1279` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1280` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1281` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1282` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1283` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1284` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1285` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1286` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1287` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1288` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1289` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1290` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1291` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1292` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1293` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1294` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_1295` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1298` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1299` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1300` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1301` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1302` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1303` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1304` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1305` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1306` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1307` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1308` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1309` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1310` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1311` | `mcq` | true | `C` | `C. Carnosine` |
| baseline | `mmlu_1312` | `mcq` | true | `B` | `B. Miss` |
| baseline | `mmlu_1313` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1314` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1315` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1316` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1317` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1318` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1319` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1320` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1321` | `mcq` | false | `A` | `C. Active transport` |
| baseline | `mmlu_1322` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1323` | `mcq` | true | `C` | `C. I and III only` |
| baseline | `mmlu_1324` | `mcq` | true | `B` | `B. glucose-1-phosphate.` |
| baseline | `mmlu_1325` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1326` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1327` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1328` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1329` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1330` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1331` | `mcq` | true | `A` | `A. Thymine` |
| baseline | `mmlu_1332` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1333` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1334` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1335` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1336` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1337` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1338` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1339` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1340` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1341` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1342` | `mcq` | true | `B` | `B. 2 seconds.` |
| baseline | `mmlu_1343` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1344` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1345` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1346` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1347` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1348` | `mcq` | true | `A` | `A. ATP.` |
| baseline | `mmlu_1349` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1350` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1351` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1352` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1353` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1354` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1355` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1356` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1357` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1358` | `mcq` | true | `D` | `D. Decreased rate of erectile dysfunction.` |
| baseline | `mmlu_1359` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1360` | `mcq` | false | `D` | `C. 5 m/s` |
| baseline | `mmlu_1361` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1362` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1363` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1364` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1365` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1366` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1367` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1368` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1369` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1370` | `mcq` | false | `C` | `B. 550 nm` |
| baseline | `mmlu_1371` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1372` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1373` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1374` | `mcq` | false | `C` | `B. 1` |
| baseline | `mmlu_1375` | `mcq` | false | `D` | `C. V_0/2` |
| baseline | `mmlu_1376` | `mcq` | false | `A` | `C. 0.67mc^2` |
| baseline | `mmlu_1377` | `mcq` | true | `A` | `A. Planck’s constant` |
| baseline | `mmlu_1378` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1379` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1380` | `mcq` | false | `D` | `A. 0.024 m` |
| baseline | `mmlu_1381` | `mcq` | true | `D` | `D. Hall coefficient` |
| baseline | `mmlu_1382` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1383` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1384` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1385` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1386` | `mcq` | false | `A` | `C. 0.48 mJ` |
| baseline | `mmlu_1387` | `mcq` | false | `B` | `C. 4.2 ns` |
| baseline | `mmlu_1388` | `mcq` | false | `A` | `C. 0.67mc^2` |
| baseline | `mmlu_1389` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1390` | `mcq` | true | `D` | `D. 10` |
| baseline | `mmlu_1391` | `mcq` | false | `B` | `A. 0.25 mm` |
| baseline | `mmlu_1392` | `mcq` | true | `C` | `C. 2 x 10^-5 N` |
| baseline | `mmlu_1393` | `mcq` | true | `B` | `B. Hall coefficient` |
| baseline | `mmlu_1394` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1395` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1396` | `mcq` | false | `B` | `A. 0.50c` |
| baseline | `mmlu_1397` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1398` | `mcq` | false | `D` | `A. 0.04 V` |
| baseline | `mmlu_1399` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1400` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1401` | `mcq` | false | `B` | `A. 414 Hz` |
| baseline | `mmlu_1402` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1403` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1404` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1405` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1406` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1407` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1408` | `mcq` | false | `D` | `B. 4` |
| baseline | `mmlu_1409` | `mcq` | true | `D` | `D. 4 W` |
| baseline | `mmlu_1410` | `mcq` | false | `B` | `C. 1.00016` |
| baseline | `mmlu_1411` | `mcq` | false | `C` | `B. 1 eV` |
| baseline | `mmlu_1412` | `mcq` | false | `B` | `A. 1/4` |
| baseline | `mmlu_1413` | `mcq` | false | `B` | `A. 150 nm` |
| baseline | `mmlu_1414` | `mcq` | false | `B` | `C. 1,100 J` |
| baseline | `mmlu_1415` | `mcq` | false | `C` | `B. 606 Hz` |
| baseline | `mmlu_1416` | `mcq` | false | `D` | `B. 288 m` |
| baseline | `mmlu_1417` | `mcq` | false | `D` | `C. 5/6 c` |
| baseline | `mmlu_1418` | `mcq` | false | `D` | `A. 0.1 GeV/c^2` |
| baseline | `mmlu_1419` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1420` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1421` | `mcq` | true | `A` | `A. real` |
| baseline | `mmlu_1422` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1423` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1424` | `mcq` | false | `D` | `B. 10%` |
| baseline | `mmlu_1425` | `mcq` | false | `C` | `A. 0°` |
| baseline | `mmlu_1426` | `mcq` | true | `D` | `D. Increases by a factor of 81.` |
| baseline | `mmlu_1427` | `mcq` | false | `D` | `A. 0.04 V` |
| baseline | `mmlu_1428` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1429` | `mcq` | true | `D` | `D. None` |
| baseline | `mmlu_1430` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1431` | `mcq` | false | `D` | `C. 262 Hz` |
| baseline | `mmlu_1432` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1433` | `mcq` | true | `A` | `A. L_B = 4L_A` |
| baseline | `mmlu_1434` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1435` | `mcq` | false | `B` | `A. 0.50c` |
| baseline | `mmlu_1436` | `mcq` | false | `A` | `C. 51.8 eV` |
| baseline | `mmlu_1437` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1438` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1439` | `mcq` | false | `D` | `C. 10,000 J` |
| baseline | `mmlu_1440` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1441` | `mcq` | false | `C` | `B. 2 N` |
| baseline | `mmlu_1442` | `mcq` | false | `B` | `A. 0.4c` |
| baseline | `mmlu_1443` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1444` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1445` | `mcq` | false | `C` | `B. 2 N` |
| baseline | `mmlu_1446` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1447` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1448` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1449` | `mcq` | false | `A` | `C. 10 mm` |
| baseline | `mmlu_1450` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1451` | `mcq` | false | `A` | `D. 2` |
| baseline | `mmlu_1452` | `mcq` | false | `D` | `B. 594 Hz` |
| baseline | `mmlu_1453` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1454` | `mcq` | true | `D` | `D. 4mc^2` |
| baseline | `mmlu_1455` | `mcq` | false | `D` | `B. Dye laser` |
| baseline | `mmlu_1456` | `mcq` | false | `D` | `C. 50%` |
| baseline | `mmlu_1457` | `mcq` | false | `D` | `B. 1,750 Hz` |
| baseline | `mmlu_1458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1459` | `mcq` | false | `B` | `A. 1/4` |
| baseline | `mmlu_1460` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1461` | `mcq` | false | `A` | `C. 0.27 J` |
| baseline | `mmlu_1462` | `mcq` | false | `C` | `B. 1 eV` |
| baseline | `mmlu_1463` | `mcq` | false | `C` | `D. 1/sqrt(2)` |
| baseline | `mmlu_1464` | `mcq` | true | `D` | `D. 19.6 m` |
| baseline | `mmlu_1465` | `mcq` | false | `C` | `B. 1/4` |
| baseline | `mmlu_1466` | `mcq` | false | `C` | `B. 550 nm` |
| baseline | `mmlu_1467` | `mcq` | true | `A` | `A. 2.5 * 10^-23 kg` |
| baseline | `mmlu_1468` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1469` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1470` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1471` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1472` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1473` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1474` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1475` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1476` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1477` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1478` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1479` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1480` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1481` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1482` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1483` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1484` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1485` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1486` | `mcq` | true | `B` | `B. Access Point` |
| baseline | `mmlu_1487` | `mcq` | true | `B` | `B. 128` |
| baseline | `mmlu_1488` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1489` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1490` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1491` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1492` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1493` | `mcq` | false | `D` | `C. True, False` |
| baseline | `mmlu_1494` | `mcq` | true | `C` | `C. Key exchange` |
| baseline | `mmlu_1495` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1496` | `mcq` | true | `C` | `C. Dark web` |
| baseline | `mmlu_1497` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1498` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1499` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1500` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1501` | `mcq` | true | `D` | `D. IP Network Browser` |
| baseline | `mmlu_1502` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1503` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1504` | `mcq` | true | `C` | `C. Session layer` |
| baseline | `mmlu_1505` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1506` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1507` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1508` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1509` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1510` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1511` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1512` | `mcq` | true | `B` | `B. 4-way handshake` |
| baseline | `mmlu_1513` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1514` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1515` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1516` | `mcq` | true | `D` | `D. Wireshark` |
| baseline | `mmlu_1517` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1518` | `mcq` | true | `C` | `C. CBF` |
| baseline | `mmlu_1519` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1520` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1521` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1522` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1523` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1524` | `mcq` | false | `B` | `C. 48` |
| baseline | `mmlu_1525` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1526` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1527` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1528` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1529` | `mcq` | false | `B` | `D. Transport Layer Security Protocol` |
| baseline | `mmlu_1530` | `mcq` | true | `D` | `D. Tor browser` |
| baseline | `mmlu_1531` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1532` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1533` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1534` | `mcq` | true | `D` | `D. UNIX` |
| baseline | `mmlu_1535` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1536` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1537` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1538` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1539` | `mcq` | true | `B` | `B. Metasploit` |
| baseline | `mmlu_1540` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1541` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_1542` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1543` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1544` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1545` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1546` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1547` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1548` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1549` | `mcq` | true | `D` | `D. EtterPeak` |
| baseline | `mmlu_1550` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1551` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1552` | `mcq` | false | `C` | `D. AES` |
| baseline | `mmlu_1553` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1554` | `mcq` | true | `C` | `C. WPS` |
| baseline | `mmlu_1555` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1556` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1557` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1558` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1559` | `mcq` | false | `D` | `B. No, there are no ciphers with perfect secrecy` |
| baseline | `mmlu_1560` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1561` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1562` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1563` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1564` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1565` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1566` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1567` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1568` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1569` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1570` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1571` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1572` | `mcq` | true | `B` | `B. volume of fluid.` |
| baseline | `mmlu_1573` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1574` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1575` | `mcq` | true | `A` | `A. changes` |
| baseline | `mmlu_1576` | `mcq` | true | `D` | `D. violet` |
| baseline | `mmlu_1577` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1578` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1579` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1580` | `mcq` | true | `D` | `D. energy` |
| baseline | `mmlu_1581` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1582` | `mcq` | true | `C` | `C. radiation` |
| baseline | `mmlu_1583` | `mcq` | false | `B` | `D. Not enough information to say` |
| baseline | `mmlu_1584` | `mcq` | true | `A` | `A. increase.` |
| baseline | `mmlu_1585` | `mcq` | false | `B` | `D. mg/4` |
| baseline | `mmlu_1586` | `mcq` | true | `A` | `A. less.` |
| baseline | `mmlu_1587` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1588` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1589` | `mcq` | false | `D` | `A. volume` |
| baseline | `mmlu_1590` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1591` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1592` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1593` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1594` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1595` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1596` | `mcq` | false | `A` | `B. doubles` |
| baseline | `mmlu_1597` | `mcq` | false | `D` | `B. 2 minutes.` |
| baseline | `mmlu_1598` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1599` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1600` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1601` | `mcq` | true | `B` | `B. taller` |
| baseline | `mmlu_1602` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1603` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1604` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1605` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1606` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1607` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1608` | `mcq` | true | `C` | `C. 50 km/h` |
| baseline | `mmlu_1609` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1610` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1611` | `mcq` | false | `C` | `A. less.` |
| baseline | `mmlu_1612` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1613` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1614` | `mcq` | false | `C` | `B. twice` |
| baseline | `mmlu_1615` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1616` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1617` | `mcq` | true | `C` | `C. the same` |
| baseline | `mmlu_1618` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1619` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1620` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1621` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1622` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1623` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1624` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1625` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1626` | `mcq` | true | `D` | `D. Not enough information to say` |
| baseline | `mmlu_1627` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1628` | `mcq` | false | `B` | `A. 2 Hz` |
| baseline | `mmlu_1629` | `mcq` | true | `D` | `D. amplitude` |
| baseline | `mmlu_1630` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1631` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1632` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1634` | `mcq` | false | `D` | `B. energy` |
| baseline | `mmlu_1635` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1636` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1637` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1638` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_1639` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1640` | `mcq` | false | `C` | `A. 1/100 as much` |
| baseline | `mmlu_1641` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1642` | `mcq` | false | `A` | `B. less dense` |
| baseline | `mmlu_1643` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1644` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1645` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1646` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1647` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1648` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1649` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1650` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1651` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1652` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1653` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1654` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1655` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1656` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1657` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1658` | `mcq` | true | `C` | `C. waves` |
| baseline | `mmlu_1659` | `mcq` | true | `A` | `A. high temperatures` |
| baseline | `mmlu_1660` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1661` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1662` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1663` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1664` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1665` | `mcq` | false | `C` | `B. violet light.` |
| baseline | `mmlu_1666` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1667` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1668` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1669` | `mcq` | true | `A` | `A. 25 cm` |
| baseline | `mmlu_1670` | `mcq` | true | `A` | `A. lower` |
| baseline | `mmlu_1671` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1672` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1673` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_1674` | `mcq` | false | `B` | `C. more than 20 years.` |
| baseline | `mmlu_1675` | `mcq` | true | `A` | `A. hydrogen` |
| baseline | `mmlu_1676` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1677` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1678` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1679` | `mcq` | true | `C` | `C. radiation.` |
| baseline | `mmlu_1680` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1681` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1682` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1683` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1684` | `mcq` | true | `B` | `B. period` |
| baseline | `mmlu_1685` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1686` | `mcq` | false | `A` | `B. released by the water` |
| baseline | `mmlu_1687` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1689` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1690` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1691` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1692` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1693` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1694` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1695` | `mcq` | true | `B` | `B. Faraday’s law` |
| baseline | `mmlu_1696` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1697` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1698` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1699` | `mcq` | false | `B` | `C. interference.` |
| baseline | `mmlu_1700` | `mcq` | true | `C` | `C. Both are the same` |
| baseline | `mmlu_1701` | `mcq` | true | `A` | `A. speed and direction` |
| baseline | `mmlu_1702` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1703` | `mcq` | true | `B` | `B. decreases` |
| baseline | `mmlu_1704` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1705` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1706` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1707` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1708` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1709` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1710` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1711` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1712` | `mcq` | false | `C` | `B. decrease` |
| baseline | `mmlu_1713` | `mcq` | true | `A` | `A. halve.` |
| baseline | `mmlu_1714` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1715` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1716` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1717` | `mcq` | true | `B` | `B. 22°C` |
| baseline | `mmlu_1718` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1719` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1720` | `mcq` | true | `D` | `D. More information is needed` |
| baseline | `mmlu_1721` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1722` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1723` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1724` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1725` | `mcq` | true | `B` | `B. Sound` |
| baseline | `mmlu_1726` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_1727` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1728` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1729` | `mcq` | false | `C` | `A. cool` |
| baseline | `mmlu_1730` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1731` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1732` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1733` | `mcq` | true | `B` | `B. 500 W` |
| baseline | `mmlu_1734` | `mcq` | true | `B` | `B. interference` |
| baseline | `mmlu_1735` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1736` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1737` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1738` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1739` | `mcq` | false | `D` | `B. energy` |
| baseline | `mmlu_1740` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1741` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1742` | `mcq` | true | `B` | `B. 26` |
| baseline | `mmlu_1743` | `mcq` | true | `B` | `B. reflects red` |
| baseline | `mmlu_1744` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1745` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1746` | `mcq` | false | `A` | `B. 50%` |
| baseline | `mmlu_1747` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1748` | `mcq` | false | `D` | `C. 8 N` |
| baseline | `mmlu_1749` | `mcq` | false | `D` | `B. 500 J` |
| baseline | `mmlu_1750` | `mcq` | false | `D` | `C. 16q.` |
| baseline | `mmlu_1751` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1752` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1753` | `mcq` | true | `B` | `B. frequency` |
| baseline | `mmlu_1754` | `mcq` | false | `B` | `C. remains the same` |
| baseline | `mmlu_1755` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1756` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1757` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1758` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1759` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1760` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1761` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1762` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1763` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1764` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1765` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1766` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1767` | `mcq` | false | `B` | `A. steadily in one direction` |
| baseline | `mmlu_1768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1769` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1770` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1771` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1772` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1773` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1774` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1775` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1776` | `mcq` | false | `D` | `A. current` |
| baseline | `mmlu_1777` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1778` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1779` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1780` | `mcq` | true | `C` | `C. 6.00 m` |
| baseline | `mmlu_1781` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1782` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1783` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1784` | `mcq` | true | `D` | `D. spectrum.` |
| baseline | `mmlu_1785` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1786` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1787` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1788` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1789` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1790` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1791` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1792` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1793` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1794` | `mcq` | true | `C` | `C. decreases` |
| baseline | `mmlu_1795` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1796` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1797` | `mcq` | true | `B` | `B. second law` |
| baseline | `mmlu_1798` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1799` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1800` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1801` | `mcq` | false | `B` | `C. remains largely unchanged.` |
| baseline | `mmlu_1802` | `mcq` | false | `C` | `D. 0.0625 g` |
| baseline | `mmlu_1803` | `mcq` | false | `B` | `A. decreased temperatures` |
| baseline | `mmlu_1804` | `mcq` | true | `A` | `A. tension.` |
| baseline | `mmlu_1805` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1806` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1807` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1808` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1809` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1810` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1811` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1812` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1813` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1814` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_1815` | `mcq` | false | `C` | `D. Bigger than 1` |
| baseline | `mmlu_1816` | `mcq` | false | `B` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1817` | `mcq` | true | `D` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1818` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1819` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1820` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1821` | `mcq` | true | `A` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1822` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1823` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1824` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1825` | `mcq` | false | `B` | `D. 1 and -3` |
| baseline | `mmlu_1826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1827` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1828` | `mcq` | false | `A` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1829` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1830` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1831` | `mcq` | true | `A` | `A. The current value of y` |
| baseline | `mmlu_1832` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1833` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1834` | `mcq` | false | `D` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1835` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1836` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1837` | `mcq` | false | `D` | `B. (i) and (iii) only` |
| baseline | `mmlu_1838` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1839` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1840` | `mcq` | true | `A` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1841` | `mcq` | false | `C` | `A. The roots of the characteristic equation must all lie inside the unit circle` |
| baseline | `mmlu_1842` | `mcq` | false | `B` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1843` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1844` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1845` | `mcq` | false | `D` | `B. Zero` |
| baseline | `mmlu_1846` | `mcq` | false | `C` | `B. (i) and (iii) only` |
| baseline | `mmlu_1847` | `mcq` | false | `B` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1848` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1849` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1850` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1851` | `mcq` | false | `C` | `D. 1.96` |
| baseline | `mmlu_1852` | `mcq` | true | `A` | `A. 77.07` |
| baseline | `mmlu_1853` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1854` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_1855` | `mcq` | false | `A` | `B. (i) and (iii) only` |
| baseline | `mmlu_1856` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1857` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1858` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1859` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1860` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1861` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_1862` | `mcq` | false | `D` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1863` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1864` | `mcq` | true | `C` | `C. Close to minus one` |
| baseline | `mmlu_1865` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1866` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1867` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1868` | `mcq` | true | `C` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1869` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1870` | `mcq` | true | `A` | `A. H0 is rejected` |
| baseline | `mmlu_1871` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1872` | `mcq` | false | `C` | `B. The largest 2` |
| baseline | `mmlu_1873` | `mcq` | true | `A` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1874` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1875` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1876` | `mcq` | false | `A` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1877` | `mcq` | true | `A` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1878` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1879` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1880` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1881` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1882` | `mcq` | true | `A` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1883` | `mcq` | true | `A` | `A. Censored` |
| baseline | `mmlu_1884` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1885` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1886` | `mcq` | true | `D` | `D. 36` |
| baseline | `mmlu_1887` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1888` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1889` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1890` | `mcq` | true | `B` | `B. Unit root process` |
| baseline | `mmlu_1891` | `mcq` | true | `D` | `D. The Breusch-Godfrey test` |
| baseline | `mmlu_1892` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1893` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1894` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1895` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1896` | `mcq` | false | `D` | `B. (i) and (iii) only` |
| baseline | `mmlu_1897` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1898` | `mcq` | false | `C` | `B. (i) and (iii) only` |
| baseline | `mmlu_1899` | `mcq` | false | `C` | `B. (i) and (iii) only` |
| baseline | `mmlu_1900` | `mcq` | false | `C` | `B. (i) and (iii) only` |
| baseline | `mmlu_1901` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1902` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1903` | `mcq` | false | `B` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1904` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1905` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1906` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1907` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1908` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1909` | `mcq` | false | `D` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1910` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1911` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1912` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1913` | `mcq` | false | `B` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1914` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1915` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1916` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1917` | `mcq` | false | `B` | `D. (i), (ii), and (iii)` |
| baseline | `mmlu_1918` | `mcq` | true | `B` | `B. The variables are not cointegrated` |
| baseline | `mmlu_1919` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1920` | `mcq` | true | `D` | `D. Both A and C` |
| baseline | `mmlu_1921` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1922` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1923` | `mcq` | true | `A` | `A. 30° to 150°.` |
| baseline | `mmlu_1924` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1925` | `mcq` | true | `D` | `D. zero.` |
| baseline | `mmlu_1926` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1927` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1928` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1929` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1930` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1931` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1932` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_1933` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1934` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1935` | `mcq` | false | `C` | `B. 6` |
| baseline | `mmlu_1936` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1937` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1938` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1939` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1940` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1941` | `mcq` | true | `B` | `B. 0.15 joule.` |
| baseline | `mmlu_1942` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1943` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1944` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1945` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1946` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1947` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1948` | `mcq` | false | `B` | `A. 0.32.` |
| baseline | `mmlu_1949` | `mcq` | false | `C` | `D. 10` |
| baseline | `mmlu_1950` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1951` | `mcq` | false | `A` | `D. all of the above.` |
| baseline | `mmlu_1952` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1953` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_1954` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1955` | `mcq` | false | `A` | `C. 50` |
| baseline | `mmlu_1956` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1957` | `mcq` | false | `A` | `D. Compensation theorem` |
| baseline | `mmlu_1958` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1959` | `mcq` | true | `B` | `B. 250 Hz.` |
| baseline | `mmlu_1960` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1961` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1962` | `mcq` | false | `A` | `B. 4` |
| baseline | `mmlu_1963` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1964` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1965` | `mcq` | true | `B` | `B. frequency modulation.` |
| baseline | `mmlu_1966` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1967` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1968` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1969` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1970` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1971` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1972` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1973` | `mcq` | true | `D` | `D. Off Switch` |
| baseline | `mmlu_1974` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1975` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1976` | `mcq` | false | `A` | `D. sensitivity.` |
| baseline | `mmlu_1977` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1978` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1979` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1980` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1981` | `mcq` | false | `C` | `D. unchanged.` |
| baseline | `mmlu_1982` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1983` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1984` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1986` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1987` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1988` | `mcq` | false | `C` | `B. edge` |
| baseline | `mmlu_1989` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1990` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1991` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1992` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1993` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1994` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1995` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1996` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1997` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1998` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1999` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2000` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2001` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2002` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2003` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2004` | `mcq` | true | `A` | `A. 160 µF` |
| baseline | `mmlu_2005` | `mcq` | false | `C` | `D. 8R Ω` |
| baseline | `mmlu_2006` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2007` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2008` | `mcq` | true | `C` | `C. high` |
| baseline | `mmlu_2009` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2010` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2011` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_2012` | `mcq` | false | `B` | `A. high.` |
| baseline | `mmlu_2013` | `mcq` | false | `A` | `B. upper surface of the conductor.` |
| baseline | `mmlu_2014` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_2015` | `mcq` | false | `D` | `B. Microphone` |
| baseline | `mmlu_2016` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2017` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2018` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2019` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2020` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2021` | `mcq` | true | `B` | `B. clean.` |
| baseline | `mmlu_2022` | `mcq` | true | `C` | `C. 10 mA.` |
| baseline | `mmlu_2023` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2024` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2025` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2026` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2027` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2028` | `mcq` | false | `C` | `B. 140.` |
| baseline | `mmlu_2029` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2030` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2031` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2032` | `mcq` | true | `B` | `B. Directives` |
| baseline | `mmlu_2033` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2034` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2035` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2036` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2037` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2038` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2039` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2040` | `mcq` | false | `D` | `B. 0.002 A.` |
| baseline | `mmlu_2041` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2042` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2043` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2044` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2045` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2046` | `mcq` | false | `B` | `A. 40π coulombs.` |
| baseline | `mmlu_2047` | `mcq` | false | `A` | `B. MSB, Most Significant Bit` |
| baseline | `mmlu_2048` | `mcq` | false | `B` | `D. none of above.` |
| baseline | `mmlu_2049` | `mcq` | false | `B` | `A. 3.33 %` |
| baseline | `mmlu_2050` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2051` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2052` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2053` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2054` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2055` | `mcq` | false | `C` | `D. Atomic number.` |
| baseline | `mmlu_2056` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2057` | `mcq` | false | `A` | `C. 21.` |
| baseline | `mmlu_2058` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2059` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2060` | `mcq` | true | `C` | `C. Either AC or DC` |
| baseline | `mmlu_2061` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2062` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2063` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2064` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2065` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2066` | `mcq` | true | `C` | `C. 8` |
| baseline | `mmlu_2067` | `mcq` | false | `D` | `B. -5` |
| baseline | `mmlu_2068` | `mcq` | false | `B` | `A. 4` |
| baseline | `mmlu_2069` | `mcq` | true | `B` | `B. 4t = 112; $28` |
| baseline | `mmlu_2070` | `mcq` | false | `C` | `B. 11` |
| baseline | `mmlu_2071` | `mcq` | true | `C` | `C. 12 over 11` |
| baseline | `mmlu_2072` | `mcq` | false | `B` | `D. 12.72` |
| baseline | `mmlu_2073` | `mcq` | true | `D` | `D. 126.26` |
| baseline | `mmlu_2074` | `mcq` | true | `D` | `D. 7.2` |
| baseline | `mmlu_2075` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2076` | `mcq` | false | `D` | `C. 1` |
| baseline | `mmlu_2077` | `mcq` | true | `A` | `A. 8` |
| baseline | `mmlu_2078` | `mcq` | true | `A` | `A. 6` |
| baseline | `mmlu_2079` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2080` | `mcq` | true | `B` | `B. 14 minutes` |
| baseline | `mmlu_2081` | `mcq` | true | `B` | `B. 24` |
| baseline | `mmlu_2082` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2083` | `mcq` | false | `D` | `C. 50` |
| baseline | `mmlu_2084` | `mcq` | false | `A` | `D. 33` |
| baseline | `mmlu_2085` | `mcq` | false | `C` | `A. -12` |
| baseline | `mmlu_2086` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2087` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2088` | `mcq` | true | `C` | `C. 73` |
| baseline | `mmlu_2089` | `mcq` | false | `B` | `C. 3.7` |
| baseline | `mmlu_2090` | `mcq` | false | `A` | `B. 3.2` |
| baseline | `mmlu_2091` | `mcq` | true | `D` | `D. 45.6` |
| baseline | `mmlu_2092` | `mcq` | false | `D` | `A. 508` |
| baseline | `mmlu_2093` | `mcq` | true | `A` | `A. 100 — 5d` |
| baseline | `mmlu_2094` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2095` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2096` | `mcq` | true | `B` | `B. 15 remainder 3` |
| baseline | `mmlu_2097` | `mcq` | false | `A` | `C. 17 over 4` |
| baseline | `mmlu_2098` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2099` | `mcq` | false | `D` | `B. 770 parts` |
| baseline | `mmlu_2100` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2101` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2102` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2103` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2104` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_2105` | `mcq` | false | `B` | `D. 2000 +150x` |
| baseline | `mmlu_2106` | `mcq` | false | `D` | `A. w > 2.3` |
| baseline | `mmlu_2107` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2108` | `mcq` | false | `C` | `A. 156` |
| baseline | `mmlu_2109` | `mcq` | false | `D` | `C. 17, 19` |
| baseline | `mmlu_2110` | `mcq` | true | `B` | `B. 12 cans` |
| baseline | `mmlu_2111` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2112` | `mcq` | false | `C` | `B. 11` |
| baseline | `mmlu_2113` | `mcq` | true | `D` | `D. 840,000` |
| baseline | `mmlu_2114` | `mcq` | true | `D` | `D. -45` |
| baseline | `mmlu_2115` | `mcq` | true | `A` | `A. 21 birds` |
| baseline | `mmlu_2116` | `mcq` | false | `B` | `D. 153` |
| baseline | `mmlu_2117` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2118` | `mcq` | true | `A` | `A. 120 miles` |
| baseline | `mmlu_2119` | `mcq` | true | `B` | `B. divide both sides by 6` |
| baseline | `mmlu_2120` | `mcq` | true | `A` | `A. 7` |
| baseline | `mmlu_2121` | `mcq` | false | `D` | `C. 84 − t = 11; 73°F` |
| baseline | `mmlu_2122` | `mcq` | true | `A` | `A. 72 ÷ 9 = 8` |
| baseline | `mmlu_2123` | `mcq` | false | `D` | `C. 5 boxes` |
| baseline | `mmlu_2124` | `mcq` | true | `B` | `B. 20` |
| baseline | `mmlu_2125` | `mcq` | false | `D` | `A. 6 over 14` |
| baseline | `mmlu_2126` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_2127` | `mcq` | true | `C` | `C. 1,395 push-ups` |
| baseline | `mmlu_2128` | `mcq` | true | `C` | `C. 10 and 12` |
| baseline | `mmlu_2129` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2130` | `mcq` | false | `C` | `B. 236` |
| baseline | `mmlu_2131` | `mcq` | false | `D` | `C. 750 and 1,000` |
| baseline | `mmlu_2132` | `mcq` | true | `A` | `A. 7` |
| baseline | `mmlu_2133` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2134` | `mcq` | false | `D` | `B. 7^2 • 11` |
| baseline | `mmlu_2135` | `mcq` | false | `C` | `B. $28.93` |
| baseline | `mmlu_2136` | `mcq` | false | `A` | `C. 320` |
| baseline | `mmlu_2137` | `mcq` | true | `B` | `B. 0.21 Repeating` |
| baseline | `mmlu_2138` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2139` | `mcq` | true | `B` | `B. $6,049` |
| baseline | `mmlu_2140` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2141` | `mcq` | false | `A` | `B. $2.97` |
| baseline | `mmlu_2142` | `mcq` | true | `D` | `D. 5 over 6` |
| baseline | `mmlu_2143` | `mcq` | false | `D` | `C. 2 over 12` |
| baseline | `mmlu_2144` | `mcq` | true | `A` | `A. 100,000 books` |
| baseline | `mmlu_2145` | `mcq` | false | `B` | `C. 144` |
| baseline | `mmlu_2146` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2147` | `mcq` | false | `D` | `A. 2` |
| baseline | `mmlu_2148` | `mcq` | true | `C` | `C. 24 over 5` |
| baseline | `mmlu_2149` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2150` | `mcq` | false | `D` | `C. 10` |
| baseline | `mmlu_2151` | `mcq` | false | `A` | `B. 8.9` |
| baseline | `mmlu_2152` | `mcq` | false | `C` | `B. 130°` |
| baseline | `mmlu_2153` | `mcq` | true | `B` | `B. 66.5 seconds` |
| baseline | `mmlu_2154` | `mcq` | false | `B` | `A. 18` |
| baseline | `mmlu_2155` | `mcq` | true | `C` | `C. 180` |
| baseline | `mmlu_2156` | `mcq` | true | `A` | `A. 1:04` |
| baseline | `mmlu_2157` | `mcq` | false | `B` | `A. 6` |
| baseline | `mmlu_2158` | `mcq` | true | `A` | `A. 48` |
| baseline | `mmlu_2159` | `mcq` | false | `C` | `A. 7` |
| baseline | `mmlu_2160` | `mcq` | false | `D` | `C. 160 feet 8 inches` |
| baseline | `mmlu_2161` | `mcq` | true | `C` | `C. $5,604` |
| baseline | `mmlu_2162` | `mcq` | true | `A` | `A. 1` |
| baseline | `mmlu_2163` | `mcq` | true | `A` | `A. 0.261` |
| baseline | `mmlu_2164` | `mcq` | false | `C` | `B. 3.6` |
| baseline | `mmlu_2165` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2166` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2167` | `mcq` | true | `B` | `B. 4.5 centimeters` |
| baseline | `mmlu_2168` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2169` | `mcq` | true | `A` | `A. 2,000` |
| baseline | `mmlu_2170` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2171` | `mcq` | true | `C` | `C. 300 seniors` |
| baseline | `mmlu_2172` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2173` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2174` | `mcq` | true | `B` | `B. subtract 20 from 180` |
| baseline | `mmlu_2175` | `mcq` | true | `C` | `C. 30 minutes` |
| baseline | `mmlu_2176` | `mcq` | false | `B` | `D. 231 = 46w` |
| baseline | `mmlu_2177` | `mcq` | true | `B` | `B. 9` |
| baseline | `mmlu_2178` | `mcq` | false | `A` | `D. 1,695` |
| baseline | `mmlu_2179` | `mcq` | false | `A` | `C. 24 hours` |
| baseline | `mmlu_2180` | `mcq` | false | `D` | `A. 6` |
| baseline | `mmlu_2181` | `mcq` | false | `A` | `C. 34.018 L` |
| baseline | `mmlu_2182` | `mcq` | true | `B` | `B. 2.5` |
| baseline | `mmlu_2183` | `mcq` | true | `B` | `B. 1 hour 12 minutes` |
| baseline | `mmlu_2184` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2185` | `mcq` | true | `B` | `B. $14.00` |
| baseline | `mmlu_2186` | `mcq` | false | `A` | `B. 100` |
| baseline | `mmlu_2187` | `mcq` | false | `A` | `C. 7x+8` |
| baseline | `mmlu_2188` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2189` | `mcq` | false | `B` | `A. $4.46` |
| baseline | `mmlu_2190` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2191` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2192` | `mcq` | true | `C` | `C. 9` |
| baseline | `mmlu_2193` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2194` | `mcq` | false | `D` | `C. 19,612` |
| baseline | `mmlu_2195` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2196` | `mcq` | false | `D` | `C. 72 km/h` |
| baseline | `mmlu_2197` | `mcq` | true | `B` | `B. 25 meters` |
| baseline | `mmlu_2198` | `mcq` | true | `C` | `C. 130 minutes` |
| baseline | `mmlu_2199` | `mcq` | false | `C` | `B. 144` |
| baseline | `mmlu_2200` | `mcq` | false | `C` | `A. 64` |
| baseline | `mmlu_2201` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2202` | `mcq` | false | `D` | `A. 9` |
| baseline | `mmlu_2203` | `mcq` | false | `B` | `D. 202.25` |
| baseline | `mmlu_2204` | `mcq` | false | `C` | `A. 22` |
| baseline | `mmlu_2205` | `mcq` | true | `D` | `D. 120` |
| baseline | `mmlu_2206` | `mcq` | false | `C` | `A. 194` |
| baseline | `mmlu_2207` | `mcq` | true | `D` | `D. 9` |
| baseline | `mmlu_2208` | `mcq` | true | `A` | `A. 3:58 p.m.` |
| baseline | `mmlu_2209` | `mcq` | true | `B` | `B. 1 and 1 over 2 ft` |
| baseline | `mmlu_2210` | `mcq` | false | `C` | `B. 60` |
| baseline | `mmlu_2211` | `mcq` | false | `D` | `C. 5:03` |
| baseline | `mmlu_2212` | `mcq` | true | `C` | `C. 20x5=n` |
| baseline | `mmlu_2213` | `mcq` | false | `C` | `B. 17` |
| baseline | `mmlu_2214` | `mcq` | true | `B` | `B. 4(3) + 4(2)` |
| baseline | `mmlu_2215` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2216` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2217` | `mcq` | false | `A` | `B. 258` |
| baseline | `mmlu_2218` | `mcq` | false | `C` | `B. conducting the survey at all shoe stores` |
| baseline | `mmlu_2219` | `mcq` | false | `D` | `C. 665 feet` |
| baseline | `mmlu_2220` | `mcq` | false | `D` | `C. 24 students` |
| baseline | `mmlu_2221` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2222` | `mcq` | true | `A` | `A. 6 stickers` |
| baseline | `mmlu_2223` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2224` | `mcq` | true | `B` | `B. 0.07` |
| baseline | `mmlu_2225` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2226` | `mcq` | true | `D` | `D. 25 × 8` |
| baseline | `mmlu_2227` | `mcq` | true | `D` | `D. 2,144` |
| baseline | `mmlu_2228` | `mcq` | false | `D` | `C. 32.54` |
| baseline | `mmlu_2229` | `mcq` | false | `B` | `A. about 10` |
| baseline | `mmlu_2230` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2231` | `mcq` | false | `A` | `B. 300 and 499` |
| baseline | `mmlu_2232` | `mcq` | false | `D` | `C. {4, 6, 8}` |
| baseline | `mmlu_2233` | `mcq` | false | `C` | `B. 4 days` |
| baseline | `mmlu_2234` | `mcq` | true | `C` | `C. 18` |
| baseline | `mmlu_2235` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2236` | `mcq` | false | `A` | `B. -7` |
| baseline | `mmlu_2237` | `mcq` | true | `C` | `C. 24` |
| baseline | `mmlu_2238` | `mcq` | true | `C` | `C. 77` |
| baseline | `mmlu_2239` | `mcq` | false | `A` | `C. -13` |
| baseline | `mmlu_2240` | `mcq` | true | `C` | `C. 800` |
| baseline | `mmlu_2241` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2242` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2243` | `mcq` | false | `B` | `C. 1 and 5 over 14` |
| baseline | `mmlu_2244` | `mcq` | true | `A` | `A. -63` |
| baseline | `mmlu_2245` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2246` | `mcq` | false | `C` | `A. 3` |
| baseline | `mmlu_2247` | `mcq` | false | `B` | `D. 1,046` |
| baseline | `mmlu_2248` | `mcq` | true | `B` | `B. 6 gallons` |
| baseline | `mmlu_2249` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2250` | `mcq` | false | `D` | `C. 1,060,460 gallons` |
| baseline | `mmlu_2251` | `mcq` | false | `D` | `B. 380` |
| baseline | `mmlu_2252` | `mcq` | true | `B` | `B. 18 = p − 4; 22` |
| baseline | `mmlu_2253` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_2254` | `mcq` | true | `B` | `B. 15` |
| baseline | `mmlu_2255` | `mcq` | false | `D` | `A. 274 square miles per county` |
| baseline | `mmlu_2256` | `mcq` | true | `B` | `B. -49°C` |
| baseline | `mmlu_2257` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2258` | `mcq` | false | `D` | `B. 27` |
| baseline | `mmlu_2259` | `mcq` | false | `C` | `D. 6.3 miles` |
| baseline | `mmlu_2260` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2261` | `mcq` | true | `B` | `B. Between 8 and 11 lb` |
| baseline | `mmlu_2262` | `mcq` | true | `B` | `B. 30/5` |
| baseline | `mmlu_2263` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2264` | `mcq` | true | `D` | `D. -1.1` |
| baseline | `mmlu_2265` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2266` | `mcq` | false | `C` | `D. 79` |
| baseline | `mmlu_2267` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_2268` | `mcq` | true | `B` | `B. 18` |
| baseline | `mmlu_2269` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2270` | `mcq` | false | `D` | `C. 4` |
| baseline | `mmlu_2271` | `mcq` | false | `D` | `A. 12 – 2` |
| baseline | `mmlu_2272` | `mcq` | false | `B` | `A. 3^7` |
| baseline | `mmlu_2273` | `mcq` | false | `D` | `B. 29` |
| baseline | `mmlu_2274` | `mcq` | true | `C` | `C. 32` |
| baseline | `mmlu_2275` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2276` | `mcq` | false | `C` | `B. 12 cm` |
| baseline | `mmlu_2277` | `mcq` | true | `C` | `C. 56` |
| baseline | `mmlu_2278` | `mcq` | false | `B` | `D. 300.59` |
| baseline | `mmlu_2279` | `mcq` | true | `A` | `A. $32.30` |
| baseline | `mmlu_2280` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_2281` | `mcq` | true | `B` | `B. $45` |
| baseline | `mmlu_2282` | `mcq` | false | `A` | `B. −7.4` |
| baseline | `mmlu_2283` | `mcq` | true | `B` | `B. ounces` |
| baseline | `mmlu_2284` | `mcq` | false | `C` | `B. $45 loss` |
| baseline | `mmlu_2285` | `mcq` | false | `B` | `C. 39` |
| baseline | `mmlu_2286` | `mcq` | false | `C` | `A. 4 subjects` |
| baseline | `mmlu_2287` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2288` | `mcq` | true | `A` | `A. 240 ÷ 12` |
| baseline | `mmlu_2289` | `mcq` | true | `C` | `C. 127` |
| baseline | `mmlu_2290` | `mcq` | true | `D` | `D. -36` |
| baseline | `mmlu_2291` | `mcq` | true | `B` | `B. 2.99p + 3.99d` |
| baseline | `mmlu_2292` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2293` | `mcq` | true | `B` | `B. -23` |
| baseline | `mmlu_2294` | `mcq` | false | `A` | `C. 4,800` |
| baseline | `mmlu_2295` | `mcq` | false | `B` | `C. 7:30 a.m.` |
| baseline | `mmlu_2296` | `mcq` | true | `C` | `C. $0.40` |
| baseline | `mmlu_2297` | `mcq` | false | `D` | `C. 2^3 • 3^2` |
| baseline | `mmlu_2298` | `mcq` | true | `B` | `B. 56` |
| baseline | `mmlu_2299` | `mcq` | false | `D` | `C. 11.5` |
| baseline | `mmlu_2300` | `mcq` | false | `D` | `B. 11 in.` |
| baseline | `mmlu_2301` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2302` | `mcq` | true | `A` | `A. 158` |
| baseline | `mmlu_2303` | `mcq` | false | `D` | `B. 1,801 R1` |
| baseline | `mmlu_2304` | `mcq` | false | `D` | `B. 1.70 cm` |
| baseline | `mmlu_2305` | `mcq` | true | `D` | `D. 393 ÷ 3` |
| baseline | `mmlu_2306` | `mcq` | true | `B` | `B. -9` |
| baseline | `mmlu_2307` | `mcq` | true | `C` | `C. 5` |
| baseline | `mmlu_2308` | `mcq` | true | `B` | `B. 12 × 7` |
| baseline | `mmlu_2309` | `mcq` | true | `B` | `B. 100 miles` |
| baseline | `mmlu_2310` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2311` | `mcq` | false | `B` | `D. 32.5 minutes` |
| baseline | `mmlu_2312` | `mcq` | false | `A` | `B. 2 over 3` |
| baseline | `mmlu_2313` | `mcq` | true | `C` | `C. 700 and 900` |
| baseline | `mmlu_2314` | `mcq` | false | `D` | `C. 1 • 11 • 13` |
| baseline | `mmlu_2315` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2316` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2317` | `mcq` | true | `A` | `A. 4(x – 22)` |
| baseline | `mmlu_2318` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2319` | `mcq` | false | `D` | `B. 3 and 3 over 4` |
| baseline | `mmlu_2320` | `mcq` | false | `A` | `B. $99.99` |
| baseline | `mmlu_2321` | `mcq` | false | `B` | `A. 8 ÷ t = 56` |
| baseline | `mmlu_2322` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2323` | `mcq` | true | `B` | `B. 192` |
| baseline | `mmlu_2324` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2325` | `mcq` | true | `C` | `C. 30` |
| baseline | `mmlu_2326` | `mcq` | false | `D` | `C. 8.027` |
| baseline | `mmlu_2327` | `mcq` | false | `C` | `A. 20 words per minute` |
| baseline | `mmlu_2328` | `mcq` | false | `C` | `B. divide 18 by 3` |
| baseline | `mmlu_2329` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2330` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2331` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2332` | `mcq` | true | `C` | `C. 314` |
| baseline | `mmlu_2333` | `mcq` | false | `A` | `C. 24.25` |
| baseline | `mmlu_2334` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2335` | `mcq` | true | `B` | `B. 260` |
| baseline | `mmlu_2336` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2337` | `mcq` | false | `C` | `B. 2 problems per minute` |
| baseline | `mmlu_2338` | `mcq` | true | `D` | `D. 180` |
| baseline | `mmlu_2339` | `mcq` | true | `B` | `B. $117.30` |
| baseline | `mmlu_2340` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2341` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2342` | `mcq` | false | `C` | `A. 599` |
| baseline | `mmlu_2343` | `mcq` | true | `A` | `A. 12 horses` |
| baseline | `mmlu_2344` | `mcq` | true | `C` | `C. $52.80` |
| baseline | `mmlu_2345` | `mcq` | true | `C` | `C. 94` |
| baseline | `mmlu_2346` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2347` | `mcq` | false | `C` | `D. 6960 ft^3` |
| baseline | `mmlu_2348` | `mcq` | false | `B` | `C. 440` |
| baseline | `mmlu_2349` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2350` | `mcq` | true | `D` | `D. 5 out of 15` |
| baseline | `mmlu_2351` | `mcq` | true | `C` | `C. 21.4` |
| baseline | `mmlu_2352` | `mcq` | true | `A` | `A. 7 over 24` |
| baseline | `mmlu_2353` | `mcq` | false | `D` | `A. 30 ft by 53 ft` |
| baseline | `mmlu_2354` | `mcq` | true | `A` | `A. 2,000` |
| baseline | `mmlu_2355` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2356` | `mcq` | false | `A` | `C. 4 and 1 over 20` |
| baseline | `mmlu_2357` | `mcq` | true | `A` | `A. 42 ÷ 7` |
| baseline | `mmlu_2358` | `mcq` | false | `D` | `C. 638` |
| baseline | `mmlu_2359` | `mcq` | false | `D` | `C. 12.81` |
| baseline | `mmlu_2360` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2361` | `mcq` | false | `D` | `C. 8^11` |
| baseline | `mmlu_2362` | `mcq` | true | `C` | `C. 400` |
| baseline | `mmlu_2363` | `mcq` | true | `B` | `B. 13` |
| baseline | `mmlu_2364` | `mcq` | false | `D` | `A. 23` |
| baseline | `mmlu_2365` | `mcq` | true | `B` | `B. 136` |
| baseline | `mmlu_2366` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2367` | `mcq` | true | `C` | `C. $29.25` |
| baseline | `mmlu_2368` | `mcq` | false | `D` | `C. 15` |
| baseline | `mmlu_2369` | `mcq` | false | `A` | `C. $13.50` |
| baseline | `mmlu_2370` | `mcq` | true | `C` | `C. 4 over 9` |
| baseline | `mmlu_2371` | `mcq` | false | `B` | `C. 29,250 yards^2` |
| baseline | `mmlu_2372` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_2373` | `mcq` | false | `B` | `A. $3` |
| baseline | `mmlu_2374` | `mcq` | false | `C` | `B. 495` |
| baseline | `mmlu_2375` | `mcq` | false | `D` | `C. $27.50` |
| baseline | `mmlu_2376` | `mcq` | true | `D` | `D. 189 days` |
| baseline | `mmlu_2377` | `mcq` | true | `D` | `D. 30x + 15y` |
| baseline | `mmlu_2378` | `mcq` | false | `C` | `B. 40` |
| baseline | `mmlu_2379` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2380` | `mcq` | false | `C` | `B. 830` |
| baseline | `mmlu_2381` | `mcq` | true | `D` | `D. 270°` |
| baseline | `mmlu_2382` | `mcq` | false | `D` | `C. 280` |
| baseline | `mmlu_2383` | `mcq` | false | `D` | `C. 64,000 feet` |
| baseline | `mmlu_2384` | `mcq` | true | `A` | `A. 13 over 36` |
| baseline | `mmlu_2385` | `mcq` | false | `A` | `B. 0.0406` |
| baseline | `mmlu_2386` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2387` | `mcq` | false | `D` | `A. dx3=9` |
| baseline | `mmlu_2388` | `mcq` | true | `B` | `B. 43.3` |
| baseline | `mmlu_2389` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2390` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2391` | `mcq` | false | `A` | `B. 74.18 m` |
| baseline | `mmlu_2392` | `mcq` | false | `D` | `A. 7-Mar` |
| baseline | `mmlu_2393` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2394` | `mcq` | false | `A` | `B. 1.0112` |
| baseline | `mmlu_2395` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2396` | `mcq` | true | `D` | `D. 305,610` |
| baseline | `mmlu_2397` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2398` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2399` | `mcq` | false | `D` | `C. 20` |
| baseline | `mmlu_2400` | `mcq` | true | `D` | `D. 30 square feet` |
| baseline | `mmlu_2401` | `mcq` | true | `B` | `B. Quadrant II` |
| baseline | `mmlu_2402` | `mcq` | true | `C` | `C. 2 m` |
| baseline | `mmlu_2403` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2404` | `mcq` | true | `B` | `B. 64` |
| baseline | `mmlu_2405` | `mcq` | false | `C` | `A. $17.88` |
| baseline | `mmlu_2406` | `mcq` | false | `D` | `C. 18m + 12t` |
| baseline | `mmlu_2407` | `mcq` | false | `A` | `B. 6` |
| baseline | `mmlu_2408` | `mcq` | false | `A` | `C. 3-Jan` |
| baseline | `mmlu_2409` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_2410` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2411` | `mcq` | true | `D` | `D. 120/h` |
| baseline | `mmlu_2412` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2413` | `mcq` | false | `A` | `B. 90` |
| baseline | `mmlu_2414` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2415` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2416` | `mcq` | false | `D` | `A. $2.19` |
| baseline | `mmlu_2417` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2418` | `mcq` | false | `C` | `B. 23 bouquets` |
| baseline | `mmlu_2419` | `mcq` | true | `A` | `A. 25 + (25+ m)` |
| baseline | `mmlu_2420` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2421` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2422` | `mcq` | true | `B` | `B. 125` |
| baseline | `mmlu_2423` | `mcq` | true | `C` | `C. 48` |
| baseline | `mmlu_2424` | `mcq` | false | `B` | `A. 632` |
| baseline | `mmlu_2425` | `mcq` | false | `C` | `B. 23` |
| baseline | `mmlu_2426` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2427` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_2428` | `mcq` | true | `D` | `D. 1,176` |
| baseline | `mmlu_2429` | `mcq` | false | `A` | `D. 1:09` |
| baseline | `mmlu_2430` | `mcq` | false | `C` | `A. 21 over 32` |
| baseline | `mmlu_2431` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2432` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2433` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2434` | `mcq` | true | `B` | `B. 3,750` |
| baseline | `mmlu_2435` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2436` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2437` | `mcq` | true | `B` | `B. 309` |
| baseline | `mmlu_2438` | `mcq` | false | `D` | `C. 120` |
| baseline | `mmlu_2439` | `mcq` | false | `A` | `C. 63` |
| baseline | `mmlu_2440` | `mcq` | true | `D` | `D. 99,000` |
| baseline | `mmlu_2441` | `mcq` | true | `C` | `C. 22` |
| baseline | `mmlu_2442` | `mcq` | true | `B` | `B. Divide 25 by 5` |
| baseline | `mmlu_2443` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2444` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2445` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2446` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2447` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2448` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2449` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2450` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2451` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2452` | `mcq` | true | `D` | `D. L ∨ ~L` |
| baseline | `mmlu_2453` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2454` | `mcq` | false | `B` | `D. Inconsistent` |
| baseline | `mmlu_2455` | `mcq` | true | `D` | `D. ~~F` |
| baseline | `mmlu_2456` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2457` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2458` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2459` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2460` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2461` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2462` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2463` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2464` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2465` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2466` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2467` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2468` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2469` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2470` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2471` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2472` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2473` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2474` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2475` | `mcq` | false | `D` | `A. U ⊃ Z` |
| baseline | `mmlu_2476` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2477` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2478` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2479` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2481` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2482` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2483` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2484` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2485` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2486` | `mcq` | false | `A` | `D. Inconsistent` |
| baseline | `mmlu_2487` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2488` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2489` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2490` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2491` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2492` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2493` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2494` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2495` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2496` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2497` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2498` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2499` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2500` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2501` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2502` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2503` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2505` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2506` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2507` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2508` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2509` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2510` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2511` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2512` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2513` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2514` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2515` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2516` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2517` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2518` | `mcq` | true | `D` | `D. (G ∨ H) ⊃ ~I` |
| baseline | `mmlu_2519` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2520` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2522` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2523` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2524` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2526` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2527` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2528` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2529` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2530` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2532` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2533` | `mcq` | false | `D` | `B. Invalid. Counterexample when Q is true and S and R are false` |
| baseline | `mmlu_2534` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2535` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2536` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2537` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2538` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2539` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2540` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2541` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2542` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2543` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2544` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2545` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2546` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2547` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2548` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2549` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2550` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2551` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2552` | `mcq` | true | `D` | `D. Inconsistent` |
| baseline | `mmlu_2553` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2554` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2555` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2556` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2557` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2558` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2559` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2560` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2561` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2562` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2563` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2564` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2565` | `mcq` | false | `D` | `B. Invalid. Counterexample when H is true and I and G are false` |
| baseline | `mmlu_2566` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2567` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2568` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2569` | `mcq` | true | `C` | `C. 40%` |
| baseline | `mmlu_2570` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2571` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2572` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2573` | `mcq` | false | `C` | `B. by 10 fold` |
| baseline | `mmlu_2574` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2575` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2576` | `mcq` | true | `C` | `C. 69%` |
| baseline | `mmlu_2577` | `mcq` | true | `C` | `C. 58%` |
| baseline | `mmlu_2578` | `mcq` | false | `B` | `C. 41%` |
| baseline | `mmlu_2579` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2580` | `mcq` | false | `B` | `A. 5%` |
| baseline | `mmlu_2581` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2582` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2583` | `mcq` | true | `B` | `B. 56%` |
| baseline | `mmlu_2584` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2585` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2586` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2587` | `mcq` | false | `C` | `B. About $8k` |
| baseline | `mmlu_2588` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2589` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2590` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2591` | `mcq` | false | `D` | `C. 55%` |
| baseline | `mmlu_2592` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2593` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2594` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2595` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2596` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2597` | `mcq` | false | `D` | `B. 30%` |
| baseline | `mmlu_2598` | `mcq` | false | `C` | `B. 41%` |
| baseline | `mmlu_2599` | `mcq` | false | `C` | `A. 690 million` |
| baseline | `mmlu_2600` | `mcq` | false | `A` | `B. 29%` |
| baseline | `mmlu_2601` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2602` | `mcq` | false | `C` | `B. by 8 fold` |
| baseline | `mmlu_2603` | `mcq` | true | `D` | `D. 19` |
| baseline | `mmlu_2604` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2605` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2606` | `mcq` | false | `B` | `C. 55%` |
| baseline | `mmlu_2607` | `mcq` | false | `D` | `B. by 8 fold` |
| baseline | `mmlu_2608` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2609` | `mcq` | true | `B` | `B. 86%` |
| baseline | `mmlu_2610` | `mcq` | false | `A` | `D. 86%` |
| baseline | `mmlu_2611` | `mcq` | false | `C` | `B. China` |
| baseline | `mmlu_2612` | `mcq` | false | `A` | `B. 2.4 million` |
| baseline | `mmlu_2613` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2614` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2615` | `mcq` | true | `A` | `A. 26%` |
| baseline | `mmlu_2616` | `mcq` | false | `B` | `C. 65%` |
| baseline | `mmlu_2617` | `mcq` | true | `C` | `C. 36%` |
| baseline | `mmlu_2618` | `mcq` | false | `B` | `A. 43%` |
| baseline | `mmlu_2619` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2620` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2621` | `mcq` | false | `B` | `A. 12 years` |
| baseline | `mmlu_2622` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2623` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2624` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2625` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2626` | `mcq` | false | `D` | `B. 25%` |
| baseline | `mmlu_2627` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2628` | `mcq` | true | `B` | `B. 34.80%` |
| baseline | `mmlu_2629` | `mcq` | false | `C` | `B. 30 million` |
| baseline | `mmlu_2630` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2631` | `mcq` | false | `B` | `A. 10%` |
| baseline | `mmlu_2632` | `mcq` | false | `C` | `B. 58%` |
| baseline | `mmlu_2633` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2634` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2635` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2636` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2637` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2638` | `mcq` | false | `B` | `C. 39%` |
| baseline | `mmlu_2639` | `mcq` | false | `B` | `A. 18%` |
| baseline | `mmlu_2640` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2641` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2642` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2643` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2644` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2645` | `mcq` | true | `C` | `C. 4%` |
| baseline | `mmlu_2646` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2647` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2648` | `mcq` | false | `B` | `A. 15%` |
| baseline | `mmlu_2649` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2650` | `mcq` | false | `C` | `D. over 50` |
| baseline | `mmlu_2651` | `mcq` | false | `A` | `B. 3%` |
| baseline | `mmlu_2652` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2653` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2654` | `mcq` | false | `B` | `C. -40%` |
| baseline | `mmlu_2655` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2656` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2657` | `mcq` | false | `C` | `A. $150,000` |
| baseline | `mmlu_2658` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2659` | `mcq` | false | `D` | `B. Russia` |
| baseline | `mmlu_2660` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2661` | `mcq` | true | `D` | `D. 86%` |
| baseline | `mmlu_2662` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2663` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2664` | `mcq` | false | `B` | `A. 0.70%` |
| baseline | `mmlu_2665` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2666` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2667` | `mcq` | false | `C` | `B. 70%` |
| baseline | `mmlu_2668` | `mcq` | false | `D` | `B. 98%` |
| baseline | `mmlu_2669` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2670` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2671` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2672` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2674` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2675` | `mcq` | true | `B` | `B. Phagocytes` |
| baseline | `mmlu_2676` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2678` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2679` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2680` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2681` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2682` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2683` | `mcq` | false | `D` | `A. The diseases are caused by viruses.` |
| baseline | `mmlu_2684` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2685` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2686` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2689` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2690` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2691` | `mcq` | false | `A` | `B. Their offspring have less genetic variation than the parents.` |
| baseline | `mmlu_2692` | `mcq` | true | `B` | `B. maintaining homeostasis.` |
| baseline | `mmlu_2693` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2694` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2695` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2696` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2697` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2698` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2699` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2700` | `mcq` | true | `B` | `B. parthenogenesis` |
| baseline | `mmlu_2701` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2702` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2703` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2704` | `mcq` | true | `C` | `C. 54%` |
| baseline | `mmlu_2705` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2706` | `mcq` | true | `D` | `D. Mutation` |
| baseline | `mmlu_2707` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2708` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2709` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2710` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2711` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2712` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2713` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2714` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2715` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2716` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2717` | `mcq` | true | `B` | `B. fallopian tube` |
| baseline | `mmlu_2718` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2719` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2720` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2721` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2722` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2723` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2724` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2725` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2726` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2727` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2728` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2729` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2730` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2731` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2732` | `mcq` | false | `C` | `B. Tundra` |
| baseline | `mmlu_2733` | `mcq` | true | `D` | `D. Deciduous forests` |
| baseline | `mmlu_2734` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2735` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2736` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2737` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2738` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2739` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2740` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2741` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2742` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2743` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2744` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2745` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2746` | `mcq` | false | `D` | `A. III only` |
| baseline | `mmlu_2747` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2748` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2749` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2750` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2751` | `mcq` | false | `C` | `A. Amount of sunlight` |
| baseline | `mmlu_2752` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2753` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2754` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2755` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2756` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2757` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2758` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2759` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2760` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2761` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2762` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2763` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2764` | `mcq` | true | `C` | `C. 48` |
| baseline | `mmlu_2765` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2766` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2767` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2768` | `mcq` | true | `B` | `B. Endosymbiotic model` |
| baseline | `mmlu_2769` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2770` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2771` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2772` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2773` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2774` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2775` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2776` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2777` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2778` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2779` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2780` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2781` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2782` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2783` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2784` | `mcq` | false | `B` | `C. 27%` |
| baseline | `mmlu_2785` | `mcq` | true | `B` | `B. the strong cohesion of property of water` |
| baseline | `mmlu_2786` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2787` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2788` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2789` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2790` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2791` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2792` | `mcq` | true | `D` | `D. 25%` |
| baseline | `mmlu_2793` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2794` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2795` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2796` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2797` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2798` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2799` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2800` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2801` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2802` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2803` | `mcq` | false | `B` | `C. H+ would increase in the matrix (inside mitochondrial inner membrane).` |
| baseline | `mmlu_2804` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2805` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2806` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2807` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2808` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2809` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2810` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2811` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2812` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2813` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2814` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2815` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2816` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2817` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2818` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2819` | `mcq` | true | `B` | `B. The flu virus, which changes its envelope proteins` |
| baseline | `mmlu_2820` | `mcq` | true | `A` | `A. 1/2` |
| baseline | `mmlu_2821` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2822` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2823` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2824` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2825` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2827` | `mcq` | true | `D` | `D. Promoter` |
| baseline | `mmlu_2828` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2829` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2830` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2831` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2832` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2833` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2834` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2835` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2836` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2837` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2838` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2839` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2840` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2841` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2842` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2843` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2844` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2845` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2846` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2847` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2848` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2849` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2850` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2851` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2852` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2853` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2855` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2856` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2857` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2858` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2859` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2860` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2861` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2862` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2863` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2864` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2865` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2866` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2867` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2868` | `mcq` | true | `A` | `A. increasing the surface area of the small intestine` |
| baseline | `mmlu_2869` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2870` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2871` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2872` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2873` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2874` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2875` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2876` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2877` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2878` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2879` | `mcq` | true | `B` | `B. Differences in the timing and expression levels of different genes leads to structural and functional differences.` |
| baseline | `mmlu_2880` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2881` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2882` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2883` | `mcq` | true | `B` | `B. Minimizing artificial lighting in the area` |
| baseline | `mmlu_2884` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2885` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2886` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2887` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2888` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2889` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2890` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2891` | `mcq` | false | `D` | `C. placenta` |
| baseline | `mmlu_2892` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2893` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2894` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2895` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2896` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2897` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2898` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2899` | `mcq` | true | `B` | `B. Repressor` |
| baseline | `mmlu_2900` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2901` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2902` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2903` | `mcq` | false | `B` | `C. adding more enzyme K` |
| baseline | `mmlu_2904` | `mcq` | true | `D` | `D. Hot and dry` |
| baseline | `mmlu_2905` | `mcq` | true | `D` | `D. Short loops of Henle to maximize water secretion` |
| baseline | `mmlu_2906` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2907` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2908` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2909` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2910` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2911` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2912` | `mcq` | true | `B` | `B. 32 percent` |
| baseline | `mmlu_2913` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2914` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2915` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2916` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2918` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2919` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2920` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2921` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2922` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2923` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2924` | `mcq` | true | `D` | `D. The streamlined body has a selective advantage in that environment.` |
| baseline | `mmlu_2925` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2926` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2927` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2928` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2929` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2930` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2931` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2932` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2933` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2934` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2935` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2936` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2937` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2938` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2939` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2940` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2941` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2942` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2943` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2944` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2945` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2946` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2947` | `mcq` | true | `A` | `A. Prophase I` |
| baseline | `mmlu_2948` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2949` | `mcq` | true | `C` | `C. Hypothalamus` |
| baseline | `mmlu_2950` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2951` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2952` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2953` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2954` | `mcq` | true | `D` | `D. Fungus` |
| baseline | `mmlu_2955` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2956` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2957` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2958` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2959` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2960` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2961` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2962` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2963` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2964` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2965` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2966` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2967` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2968` | `mcq` | true | `D` | `D. Natural selection` |
| baseline | `mmlu_2969` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2970` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2971` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2972` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2973` | `mcq` | true | `B` | `B. Pyrimidine : Purine` |
| baseline | `mmlu_2974` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2975` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2976` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2977` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2978` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2979` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2980` | `mcq` | true | `A` | `A. 70 pm, 1402 kJ/mol` |
| baseline | `mmlu_2981` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2982` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2983` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2984` | `mcq` | false | `C` | `A. 0.33 atm` |
| baseline | `mmlu_2985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2986` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2987` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2988` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2989` | `mcq` | false | `C` | `A. 0.0641 M` |
| baseline | `mmlu_2990` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2991` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2992` | `mcq` | true | `A` | `A. 3.8 × 10^-3 mol/L` |
| baseline | `mmlu_2993` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2994` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2995` | `mcq` | false | `A` | `B. the value of ΔG° is greater than zero` |
| baseline | `mmlu_2996` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2997` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2998` | `mcq` | false | `D` | `C. 29` |
| baseline | `mmlu_2999` | `mcq` | false | `B` | `C.` |
