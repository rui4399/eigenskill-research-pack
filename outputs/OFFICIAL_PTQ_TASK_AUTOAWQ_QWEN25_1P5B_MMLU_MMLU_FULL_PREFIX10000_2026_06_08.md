# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `10000`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 5814 / 10000 | 0.5814 | 11.0766 | 0.155344 |

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
| baseline | `mmlu_3000` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3001` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3002` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3003` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3004` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3005` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3007` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3008` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3009` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3010` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3011` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3012` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3013` | `mcq` | false | `B` | `A. C2H4O` |
| baseline | `mmlu_3014` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3015` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3016` | `mcq` | false | `C` | `A. 30.0 mL` |
| baseline | `mmlu_3017` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3018` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3019` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3020` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3021` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3022` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3023` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3024` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3025` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3026` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3027` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3028` | `mcq` | true | `A` | `A. 1.00 grams` |
| baseline | `mmlu_3029` | `mcq` | false | `B` | `C. 5.4 × 10^-3` |
| baseline | `mmlu_3030` | `mcq` | true | `A` | `A. 8.8 × 10^-11 M` |
| baseline | `mmlu_3031` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3032` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3033` | `mcq` | false | `C` | `A. The 1s peak has the lowest energy.` |
| baseline | `mmlu_3034` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3035` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3036` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3037` | `mcq` | false | `D` | `A. 6 electrons on the left` |
| baseline | `mmlu_3038` | `mcq` | false | `D` | `B. 8.52` |
| baseline | `mmlu_3039` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3040` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3041` | `mcq` | true | `A` | `A. 2.0 × 10^-3` |
| baseline | `mmlu_3042` | `mcq` | true | `D` | `D. 251 torr` |
| baseline | `mmlu_3043` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3044` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3045` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3046` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3047` | `mcq` | false | `D` | `B. When the concentrations are at standard state` |
| baseline | `mmlu_3048` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3049` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3050` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3051` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3052` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3053` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3054` | `mcq` | false | `B` | `A. 454°C` |
| baseline | `mmlu_3055` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3056` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3057` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3058` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3059` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3060` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3061` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3062` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3063` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3064` | `mcq` | false | `A` | `D. NO3-` |
| baseline | `mmlu_3065` | `mcq` | true | `A` | `A. 1` |
| baseline | `mmlu_3066` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3067` | `mcq` | true | `C` | `C. Decreasing [Fe2+]` |
| baseline | `mmlu_3068` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3069` | `mcq` | false | `C` | `D. 2,3-bromochloropentane` |
| baseline | `mmlu_3070` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3071` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3072` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3073` | `mcq` | true | `D` | `D. 1.32 × 10^-5 torr` |
| baseline | `mmlu_3074` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3075` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3076` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3077` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3078` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3079` | `mcq` | false | `B` | `A. 0.100 mol` |
| baseline | `mmlu_3080` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3081` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3082` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3083` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3084` | `mcq` | true | `A` | `A. -3.2 L atm` |
| baseline | `mmlu_3085` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3086` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3087` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3088` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3089` | `mcq` | false | `B` | `A. 0.496 molar` |
| baseline | `mmlu_3090` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3091` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3092` | `mcq` | true | `C` | `C. The temperature` |
| baseline | `mmlu_3093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3094` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3095` | `mcq` | true | `D` | `D. N2H4(aq)` |
| baseline | `mmlu_3096` | `mcq` | false | `D` | `C. Adding a selective catalyst` |
| baseline | `mmlu_3097` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3098` | `mcq` | true | `C` | `C. 0.311` |
| baseline | `mmlu_3099` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3100` | `mcq` | false | `B` | `D. 11` |
| baseline | `mmlu_3101` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3102` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3103` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3104` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3105` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3106` | `mcq` | false | `C` | `B. First order` |
| baseline | `mmlu_3107` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3108` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3109` | `mcq` | true | `D` | `D. triple-distilled water` |
| baseline | `mmlu_3110` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3111` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3112` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3113` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3114` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3115` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3116` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3117` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3118` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3119` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3120` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3121` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3122` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3123` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3124` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3125` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3126` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3127` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3128` | `mcq` | false | `B` | `C. Neon` |
| baseline | `mmlu_3129` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3130` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3131` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3132` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3133` | `mcq` | true | `A` | `A. 212 g mol-1` |
| baseline | `mmlu_3134` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3135` | `mcq` | false | `B` | `A. [HNO2] > [NO2-]` |
| baseline | `mmlu_3136` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3137` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3138` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3139` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3140` | `mcq` | false | `C` | `A. 1s` |
| baseline | `mmlu_3141` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3142` | `mcq` | true | `C` | `C. Am` |
| baseline | `mmlu_3143` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3144` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3145` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3146` | `mcq` | true | `B` | `B. 4.60%` |
| baseline | `mmlu_3147` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3148` | `mcq` | true | `D` | `D. 1 × 10^-5 M` |
| baseline | `mmlu_3149` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3150` | `mcq` | false | `B` | `D. 3.66` |
| baseline | `mmlu_3151` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3152` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3153` | `mcq` | true | `A` | `A. 53.0 g/mol` |
| baseline | `mmlu_3154` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3155` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3156` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3157` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3158` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3159` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3160` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3161` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3162` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3163` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3164` | `mcq` | true | `B` | `B. 9.26` |
| baseline | `mmlu_3165` | `mcq` | false | `C` | `D. 0.00625 g` |
| baseline | `mmlu_3166` | `mcq` | false | `D` | `A. 8.49 J mol-1 K-1` |
| baseline | `mmlu_3167` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3168` | `mcq` | true | `B` | `B. the rate-determining or slow step of the mechanism` |
| baseline | `mmlu_3169` | `mcq` | true | `A` | `A. 3.4 × 10^-4 s-1` |
| baseline | `mmlu_3170` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3171` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3172` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3173` | `mcq` | false | `D` | `B. Increasing the temperature at which the reaction occurs` |
| baseline | `mmlu_3174` | `mcq` | false | `B` | `D. 7.1 mol` |
| baseline | `mmlu_3175` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3176` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3177` | `mcq` | true | `D` | `D. HBr` |
| baseline | `mmlu_3178` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3179` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3180` | `mcq` | false | `C` | `A. 3+, reduction` |
| baseline | `mmlu_3181` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3182` | `mcq` | true | `C` | `C. 8` |
| baseline | `mmlu_3183` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3184` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3185` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3186` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3187` | `mcq` | false | `C` | `B. 225` |
| baseline | `mmlu_3188` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3189` | `mcq` | true | `B` | `B. Only elements that appear in both inputListl and inputList2` |
| baseline | `mmlu_3190` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3191` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3193` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3194` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3195` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3196` | `mcq` | true | `C` | `C. Lossless compression` |
| baseline | `mmlu_3197` | `mcq` | true | `A` | `A. isupper()` |
| baseline | `mmlu_3198` | `mcq` | true | `D` | `D. (num MOD 2) = 1` |
| baseline | `mmlu_3199` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3200` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3201` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3202` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3203` | `mcq` | true | `B` | `B. aab` |
| baseline | `mmlu_3204` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3205` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3206` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3207` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3208` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3209` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3210` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3211` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3212` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3213` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3214` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3215` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3216` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3217` | `mcq` | true | `B` | `B. 1` |
| baseline | `mmlu_3218` | `mcq` | true | `A` | `A. 1001 0100` |
| baseline | `mmlu_3219` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3220` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3221` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3223` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3224` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3225` | `mcq` | true | `A` | `A. 7` |
| baseline | `mmlu_3226` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3227` | `mcq` | false | `B` | `A. 3` |
| baseline | `mmlu_3228` | `mcq` | true | `C` | `C. 24` |
| baseline | `mmlu_3229` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3230` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3231` | `mcq` | false | `C` | `D. O(N)` |
| baseline | `mmlu_3232` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3233` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3234` | `mcq` | false | `A` | `D. O(log n)` |
| baseline | `mmlu_3235` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3236` | `mcq` | true | `D` | `D. heads_counter = 2` |
| baseline | `mmlu_3237` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3238` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3239` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3240` | `mcq` | false | `C` | `D. Stack \| Queue \| Dictionary/map` |
| baseline | `mmlu_3241` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3242` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_3243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3244` | `mcq` | false | `B` | `D. Hexadecimal D, Decimal 11, Binary 1100` |
| baseline | `mmlu_3245` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3246` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3247` | `mcq` | false | `D` | `A. Error` |
| baseline | `mmlu_3248` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3249` | `mcq` | false | `C` | `A. 9` |
| baseline | `mmlu_3250` | `mcq` | true | `D` | `D. 5` |
| baseline | `mmlu_3251` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3252` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3253` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3254` | `mcq` | false | `C` | `D. 8` |
| baseline | `mmlu_3255` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3256` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3257` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3258` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3259` | `mcq` | true | `B` | `B. nextAvailableID` |
| baseline | `mmlu_3260` | `mcq` | false | `A` | `C. 250` |
| baseline | `mmlu_3261` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3262` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3263` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3264` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3265` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3266` | `mcq` | false | `C` | `A. The goal of the attack` |
| baseline | `mmlu_3267` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3268` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3269` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3270` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3271` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3272` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_3273` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3274` | `mcq` | false | `C` | `A. [19,21]` |
| baseline | `mmlu_3275` | `mcq` | true | `D` | `D. During run time` |
| baseline | `mmlu_3276` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3277` | `mcq` | false | `C` | `D. 3 2` |
| baseline | `mmlu_3278` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3279` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3281` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3282` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3283` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3284` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3285` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3286` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3287` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3288` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3289` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3290` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3291` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3292` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3293` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3294` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3295` | `mcq` | false | `B` | `C. Industrialization` |
| baseline | `mmlu_3296` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3298` | `mcq` | true | `A` | `A. observation and induction` |
| baseline | `mmlu_3299` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3300` | `mcq` | false | `A` | `B. Financial gain` |
| baseline | `mmlu_3301` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3302` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3303` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3304` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3305` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3306` | `mcq` | true | `D` | `D. Poland` |
| baseline | `mmlu_3307` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3308` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3309` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3310` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3311` | `mcq` | true | `C` | `C. Rationalism` |
| baseline | `mmlu_3312` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3313` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3314` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3315` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3316` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3317` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3318` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3319` | `mcq` | true | `B` | `B. Financial gain` |
| baseline | `mmlu_3320` | `mcq` | false | `B` | `D. Napoleon's military tactics` |
| baseline | `mmlu_3321` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3322` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3323` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3324` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3325` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3326` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3327` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3328` | `mcq` | true | `C` | `C. Humanism` |
| baseline | `mmlu_3329` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3330` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3331` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3332` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3333` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3334` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3335` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3336` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3337` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3338` | `mcq` | true | `D` | `D. mass conscription` |
| baseline | `mmlu_3339` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3340` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3341` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3342` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3343` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3344` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3345` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3346` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3347` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3348` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3349` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3350` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3351` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3352` | `mcq` | true | `D` | `D. the Earth is not stationary` |
| baseline | `mmlu_3353` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3354` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3355` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3356` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3357` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3358` | `mcq` | false | `D` | `B. He was so concerned with ceremonies and appearances that he did not rule his country well.` |
| baseline | `mmlu_3359` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3360` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3361` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3362` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3363` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3364` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3365` | `mcq` | false | `A` | `D. Utopia` |
| baseline | `mmlu_3366` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3367` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3368` | `mcq` | true | `C` | `C. Increased disillusionment and cynicism` |
| baseline | `mmlu_3369` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3370` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3371` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3372` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3373` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3374` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3376` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3377` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3378` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3379` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3380` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3381` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3382` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3383` | `mcq` | true | `D` | `D. Anabaptists` |
| baseline | `mmlu_3384` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3385` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3386` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3387` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3388` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3389` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3390` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3391` | `mcq` | true | `D` | `D. Darwin` |
| baseline | `mmlu_3392` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3393` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3394` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3395` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3396` | `mcq` | false | `B` | `C. Increased popular participation in politics` |
| baseline | `mmlu_3397` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3398` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3399` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3401` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3402` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3403` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3404` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3405` | `mcq` | false | `B` | `D. Challenges to the monopoly on truth held by the Roman Catholic Church on multiple fronts` |
| baseline | `mmlu_3406` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3407` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3408` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3409` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3410` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3411` | `mcq` | true | `B` | `B. Predestination` |
| baseline | `mmlu_3412` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3413` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3414` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3415` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3416` | `mcq` | true | `B` | `B. They utilized new methods of communicating their ideas, such as salons and inexpensive printed pamphlets.` |
| baseline | `mmlu_3417` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3418` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3419` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3420` | `mcq` | true | `B` | `B. France` |
| baseline | `mmlu_3421` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3422` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3423` | `mcq` | true | `C` | `C. Economic opportunities were created.` |
| baseline | `mmlu_3424` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3425` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3426` | `mcq` | true | `B` | `B. Religious` |
| baseline | `mmlu_3427` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3428` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3429` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3430` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3431` | `mcq` | true | `C` | `C. Mexico` |
| baseline | `mmlu_3432` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3433` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3434` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3435` | `mcq` | true | `D` | `D. Nationalism` |
| baseline | `mmlu_3436` | `mcq` | true | `C` | `C. An increased rate of inflation` |
| baseline | `mmlu_3437` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3438` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3439` | `mcq` | true | `D` | `D. Socioeconomic changes created divisions of labor that led to the development of self-conscious classes.` |
| baseline | `mmlu_3440` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3441` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3442` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3443` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3444` | `mcq` | true | `C` | `C. scientific principles were applied to other cultures as a result of the sudden expansion of European dominance across` |
| baseline | `mmlu_3445` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3446` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3447` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3448` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3449` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3450` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3451` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3452` | `mcq` | true | `D` | `D. overcrowding.` |
| baseline | `mmlu_3453` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3454` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3455` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3456` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3457` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3458` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3459` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3460` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3461` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3462` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3463` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3464` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3465` | `mcq` | true | `B` | `B. Suburbs` |
| baseline | `mmlu_3466` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3467` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3468` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3470` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3471` | `mcq` | true | `B` | `B. theocracy.` |
| baseline | `mmlu_3472` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3473` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3474` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3475` | `mcq` | true | `C` | `C. Natural` |
| baseline | `mmlu_3476` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3477` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3478` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3479` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3481` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3482` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3483` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3484` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3485` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3486` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3487` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3488` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3489` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3490` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3491` | `mcq` | true | `D` | `D. Burgess` |
| baseline | `mmlu_3492` | `mcq` | false | `D` | `C. road map.` |
| baseline | `mmlu_3493` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3494` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3495` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3496` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3497` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3498` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3499` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3500` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3501` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3502` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3503` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3505` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3506` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3507` | `mcq` | false | `D` | `B. Distance decay` |
| baseline | `mmlu_3508` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3509` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3510` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3511` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3512` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3513` | `mcq` | true | `D` | `D. Romance` |
| baseline | `mmlu_3514` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3515` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3516` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3517` | `mcq` | true | `B` | `B. Shiite` |
| baseline | `mmlu_3518` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3519` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3521` | `mcq` | true | `C` | `C. Japan` |
| baseline | `mmlu_3522` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3523` | `mcq` | true | `D` | `D. Strict pollution regulations` |
| baseline | `mmlu_3524` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3525` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3526` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3527` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3528` | `mcq` | true | `B` | `B. The end of the Cold War` |
| baseline | `mmlu_3529` | `mcq` | true | `B` | `B. Air` |
| baseline | `mmlu_3530` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3531` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3532` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3533` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3534` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3535` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3536` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3537` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3538` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3539` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3540` | `mcq` | true | `C` | `C. Information` |
| baseline | `mmlu_3541` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3542` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3543` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3544` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3545` | `mcq` | true | `B` | `B. Origin point` |
| baseline | `mmlu_3546` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3547` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3548` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3549` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3550` | `mcq` | true | `D` | `D. Health care` |
| baseline | `mmlu_3551` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3552` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3553` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3554` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3555` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3556` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3557` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3558` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3559` | `mcq` | true | `D` | `D. Green Revolution.` |
| baseline | `mmlu_3560` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3561` | `mcq` | true | `B` | `B. Asia and Latin America` |
| baseline | `mmlu_3562` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3563` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3564` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3565` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3566` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3567` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3568` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3569` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3570` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3571` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3572` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3573` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3574` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3575` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3576` | `mcq` | true | `D` | `D. Amount of fertilizer produced in the country` |
| baseline | `mmlu_3577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3578` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3579` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3580` | `mcq` | false | `B` | `D. The national anthem` |
| baseline | `mmlu_3581` | `mcq` | true | `B` | `B. destinations for vast numbers of pilgrims` |
| baseline | `mmlu_3582` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3583` | `mcq` | true | `D` | `D. Distance to the nearest city` |
| baseline | `mmlu_3584` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3585` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3586` | `mcq` | false | `D` | `B. Washington` |
| baseline | `mmlu_3587` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3588` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3589` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3590` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3591` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3592` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3593` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3594` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3595` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3596` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3597` | `mcq` | false | `C` | `B. Iraq` |
| baseline | `mmlu_3598` | `mcq` | true | `D` | `D. Spain` |
| baseline | `mmlu_3599` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3600` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3601` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3602` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3603` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3604` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3605` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3606` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3607` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3608` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3609` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3610` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3611` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3612` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3613` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3614` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3616` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3617` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3618` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3619` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3620` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3621` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3622` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3623` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3624` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3625` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3626` | `mcq` | true | `C` | `C. China` |
| baseline | `mmlu_3627` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3628` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3629` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3630` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3631` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3632` | `mcq` | true | `B` | `B. Christianity` |
| baseline | `mmlu_3633` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3634` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3635` | `mcq` | true | `B` | `B. Transport` |
| baseline | `mmlu_3636` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3637` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3638` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3639` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3640` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3641` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3642` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3643` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3644` | `mcq` | true | `B` | `B. South America` |
| baseline | `mmlu_3645` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3646` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3647` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3648` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3649` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3650` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3651` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3652` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3653` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3654` | `mcq` | true | `C` | `C. Judicial review` |
| baseline | `mmlu_3655` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3656` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3658` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3659` | `mcq` | true | `D` | `D. stare decisis` |
| baseline | `mmlu_3660` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3661` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3662` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3663` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3664` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3665` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3666` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3668` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3669` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3670` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3671` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3672` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3673` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3674` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3675` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3676` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3677` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3678` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3679` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3680` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3681` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3683` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3684` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3685` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3686` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3687` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3688` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3689` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3690` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3691` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3692` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3693` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3694` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3695` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3696` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3697` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3698` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3699` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3700` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3701` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3702` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3703` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3704` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3705` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3706` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3707` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3708` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3709` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3710` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3712` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3713` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3714` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3715` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3716` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3717` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3718` | `mcq` | true | `C` | `C. State legislatures` |
| baseline | `mmlu_3719` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3720` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3721` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3722` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3723` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3724` | `mcq` | true | `A` | `A. judicial activism` |
| baseline | `mmlu_3725` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3726` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3728` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3729` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3730` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3731` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3732` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3733` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3734` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3735` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3736` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3737` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3738` | `mcq` | true | `D` | `D. gerrymandering` |
| baseline | `mmlu_3739` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3740` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3741` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3742` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3743` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3744` | `mcq` | true | `C` | `C. reduce the federal deficit` |
| baseline | `mmlu_3745` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3746` | `mcq` | true | `D` | `D. Development of a two-party system` |
| baseline | `mmlu_3747` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3748` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3749` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3750` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3751` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3752` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3753` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3754` | `mcq` | false | `D` | `A. The candidate who wins the popular national vote` |
| baseline | `mmlu_3755` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3756` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3757` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3758` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3759` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3760` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3761` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3762` | `mcq` | true | `B` | `B. due process clause` |
| baseline | `mmlu_3763` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3764` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3765` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3766` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3767` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3769` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3770` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3771` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3772` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3773` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3774` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3775` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3776` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3777` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3778` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3779` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3780` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3781` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3782` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3783` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3784` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3785` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3786` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3787` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3788` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3789` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3790` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3791` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3792` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3793` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3794` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3795` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3796` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3797` | `mcq` | true | `D` | `D. president` |
| baseline | `mmlu_3798` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3799` | `mcq` | true | `D` | `D. Fourteenth Amendment` |
| baseline | `mmlu_3800` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3801` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3802` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3803` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3804` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3805` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3806` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3807` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3808` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3809` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3810` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3811` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3812` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3813` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3814` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3815` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3816` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3817` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3818` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3819` | `mcq` | true | `D` | `D. Rules` |
| baseline | `mmlu_3820` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3821` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3822` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3823` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3824` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3825` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3826` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3827` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3828` | `mcq` | true | `D` | `D. John Locke` |
| baseline | `mmlu_3829` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3830` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3831` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3832` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3833` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3834` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3835` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3836` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3837` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3838` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3839` | `mcq` | false | `D` | `A. II III and IV only` |
| baseline | `mmlu_3840` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3841` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3842` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3843` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3844` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3845` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3846` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3847` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3848` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3849` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3850` | `mcq` | false | `D` | `A. 5 percent decrease` |
| baseline | `mmlu_3851` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3852` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3853` | `mcq` | false | `B` | `A. 70%` |
| baseline | `mmlu_3854` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3855` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3856` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3857` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3858` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3859` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3860` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3861` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3862` | `mcq` | true | `B` | `B. Dollar bills` |
| baseline | `mmlu_3863` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3864` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3865` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3866` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3867` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3868` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3869` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3870` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3871` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3872` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3873` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3874` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3875` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3876` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3877` | `mcq` | true | `C` | `C. $4,000` |
| baseline | `mmlu_3878` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3880` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3881` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3882` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3883` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3884` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3885` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3886` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3887` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3888` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3889` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3890` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3891` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3892` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3893` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3894` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3895` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3896` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3897` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3898` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3899` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3900` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3901` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3902` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3903` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3904` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3905` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3906` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3907` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3908` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3909` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3910` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3911` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3912` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3913` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3914` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3915` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3916` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3917` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3918` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3919` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3920` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3921` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3922` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3923` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3924` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3925` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3926` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3927` | `mcq` | false | `C` | `A. $0 million` |
| baseline | `mmlu_3928` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3929` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3930` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3931` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3932` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3933` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3934` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3935` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3936` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3937` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3938` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3939` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3940` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3941` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3942` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3943` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3944` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3945` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3946` | `mcq` | false | `D` | `B. $1.25` |
| baseline | `mmlu_3947` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3948` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3949` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3950` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3951` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3952` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3953` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3954` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3955` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3956` | `mcq` | true | `B` | `B. $400 billion` |
| baseline | `mmlu_3957` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3958` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3959` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3960` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3961` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3962` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3963` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3964` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3965` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3966` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3967` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3968` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3969` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3970` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3971` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3972` | `mcq` | false | `C` | `D. China ($2).` |
| baseline | `mmlu_3973` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3974` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3975` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3976` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3977` | `mcq` | true | `D` | `D. Savers` |
| baseline | `mmlu_3978` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3979` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3980` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3981` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3982` | `mcq` | true | `D` | `D. The GDP deflator` |
| baseline | `mmlu_3983` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3984` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3985` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3986` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3987` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3988` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3989` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3990` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3991` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3992` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3993` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3994` | `mcq` | false | `D` | `B. has risen 5 percent from the base to the current period.` |
| baseline | `mmlu_3995` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3996` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3997` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3998` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3999` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4000` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4001` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4002` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4003` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4004` | `mcq` | true | `C` | `C. Decreasing     Increasing` |
| baseline | `mmlu_4005` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4006` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4007` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4008` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4009` | `mcq` | false | `D` | `A. 10 years.` |
| baseline | `mmlu_4010` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4011` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4012` | `mcq` | true | `A` | `A. The capital account` |
| baseline | `mmlu_4013` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4014` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4015` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4016` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4017` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4018` | `mcq` | false | `A` | `D. Decreased demand     Depreciating` |
| baseline | `mmlu_4019` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4020` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4021` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4022` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4023` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4024` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4025` | `mcq` | true | `C` | `C. Medium of exchange` |
| baseline | `mmlu_4026` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4027` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4028` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4029` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4030` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4031` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4032` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4033` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4034` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4035` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4036` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4037` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4038` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4039` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4040` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4041` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4042` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4043` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4044` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4045` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4046` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4047` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4048` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4049` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4050` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4051` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4052` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4053` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4054` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4055` | `mcq` | false | `C` | `B. decreased by 4 percent.` |
| baseline | `mmlu_4056` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4057` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4058` | `mcq` | false | `D` | `C. $625` |
| baseline | `mmlu_4059` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4060` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4061` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4062` | `mcq` | false | `D` | `C. rise and taxes fall.` |
| baseline | `mmlu_4063` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4064` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4065` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4066` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4067` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4068` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4069` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4070` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4071` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4072` | `mcq` | false | `A` | `B. 1.25` |
| baseline | `mmlu_4073` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4074` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4075` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4076` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4077` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4078` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4079` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4080` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4081` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4082` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4083` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4084` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4085` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4086` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4087` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4088` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4089` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4090` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4091` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4092` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4093` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4094` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4095` | `mcq` | true | `D` | `D. Increase     Decrease     Increase` |
| baseline | `mmlu_4096` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4097` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4098` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4099` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4100` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4101` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4102` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4103` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4104` | `mcq` | false | `C` | `B. 5.0 percent.` |
| baseline | `mmlu_4105` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4106` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4107` | `mcq` | false | `A` | `D. (D) Increased     Stayed the same` |
| baseline | `mmlu_4108` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4109` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4110` | `mcq` | true | `D` | `D. Increased     Decreased` |
| baseline | `mmlu_4111` | `mcq` | false | `C` | `B. $1,200` |
| baseline | `mmlu_4112` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4113` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4114` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4115` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4116` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4117` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4118` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4119` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4120` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4121` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4122` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4123` | `mcq` | true | `B` | `B. determined by supply and demand.` |
| baseline | `mmlu_4124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4125` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4126` | `mcq` | true | `B` | `B. $4,500` |
| baseline | `mmlu_4127` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4128` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4129` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4130` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4131` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4132` | `mcq` | false | `B` | `D. $1,200` |
| baseline | `mmlu_4133` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4134` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4135` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4136` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4137` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4138` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4139` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4140` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4141` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4142` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4143` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4144` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4145` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4146` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4147` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4148` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4149` | `mcq` | false | `B` | `A. Only I is true.` |
| baseline | `mmlu_4150` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4151` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4152` | `mcq` | true | `B` | `B. $180` |
| baseline | `mmlu_4153` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4154` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4155` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4156` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4157` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4158` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4159` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4160` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4161` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4162` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4163` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4164` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4165` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4166` | `mcq` | true | `D` | `D. Frictional` |
| baseline | `mmlu_4167` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4168` | `mcq` | false | `C` | `D. $1,900` |
| baseline | `mmlu_4169` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4170` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4171` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_4172` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4173` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4174` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4175` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4176` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4177` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4178` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4179` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4180` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4181` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4182` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4183` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4184` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4185` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4186` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4187` | `mcq` | true | `A` | `A. Shifts down     Falls     Rises` |
| baseline | `mmlu_4188` | `mcq` | false | `C` | `D. France has the absolute advantage in cheese.` |
| baseline | `mmlu_4189` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4190` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4191` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4192` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4193` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4194` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4195` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4196` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4197` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4198` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4199` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4200` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4201` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4202` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4203` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4204` | `mcq` | true | `B` | `B. Unit of account` |
| baseline | `mmlu_4205` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4206` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4207` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4208` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4209` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4210` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4211` | `mcq` | true | `D` | `D. Increasing money spent to pay for government projects` |
| baseline | `mmlu_4212` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4213` | `mcq` | false | `B` | `A. increase by $200 million.` |
| baseline | `mmlu_4214` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4215` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4216` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4217` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4218` | `mcq` | false | `B` | `C. I and IV only` |
| baseline | `mmlu_4219` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4220` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4221` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4222` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4223` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4224` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4225` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4226` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4227` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4228` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4229` | `mcq` | false | `C` | `D. 25` |
| baseline | `mmlu_4230` | `mcq` | true | `A` | `A. 392` |
| baseline | `mmlu_4231` | `mcq` | false | `B` | `A. \frac{7}{9}` |
| baseline | `mmlu_4232` | `mcq` | true | `C` | `C. (-inf, 8)` |
| baseline | `mmlu_4233` | `mcq` | false | `B` | `A. 396` |
| baseline | `mmlu_4234` | `mcq` | false | `C` | `B. 0.24` |
| baseline | `mmlu_4235` | `mcq` | true | `A` | `A. 42` |
| baseline | `mmlu_4236` | `mcq` | false | `C` | `A. \frac{125}{648}` |
| baseline | `mmlu_4237` | `mcq` | false | `B` | `A. 8` |
| baseline | `mmlu_4238` | `mcq` | false | `D` | `B. 14` |
| baseline | `mmlu_4239` | `mcq` | false | `D` | `C. 2048` |
| baseline | `mmlu_4240` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_4241` | `mcq` | false | `B` | `C. 94.5` |
| baseline | `mmlu_4242` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4243` | `mcq` | true | `D` | `D. 5+2\sqrt{13}` |
| baseline | `mmlu_4244` | `mcq` | true | `A` | `A. 8` |
| baseline | `mmlu_4245` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4246` | `mcq` | false | `A` | `C. 0` |
| baseline | `mmlu_4247` | `mcq` | false | `B` | `A. (-\infty,-1)\cup (1,\infty)` |
| baseline | `mmlu_4248` | `mcq` | true | `D` | `D. -\frac{x-4}{5}` |
| baseline | `mmlu_4249` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4250` | `mcq` | true | `D` | `D. 8` |
| baseline | `mmlu_4251` | `mcq` | false | `B` | `A. 4` |
| baseline | `mmlu_4252` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4253` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_4254` | `mcq` | true | `D` | `D. 70` |
| baseline | `mmlu_4255` | `mcq` | false | `C` | `B. 5 min` |
| baseline | `mmlu_4256` | `mcq` | false | `C` | `D. (-inf, -1) U (-1, 4) U (4, inf)` |
| baseline | `mmlu_4257` | `mcq` | true | `D` | `D. 1/e` |
| baseline | `mmlu_4258` | `mcq` | true | `C` | `C. 0` |
| baseline | `mmlu_4259` | `mcq` | false | `A` | `D. 12` |
| baseline | `mmlu_4260` | `mcq` | false | `D` | `C. 840` |
| baseline | `mmlu_4261` | `mcq` | true | `A` | `A. 8788` |
| baseline | `mmlu_4262` | `mcq` | true | `A` | `A. -9` |
| baseline | `mmlu_4263` | `mcq` | true | `D` | `D. 17` |
| baseline | `mmlu_4264` | `mcq` | false | `C` | `B. 4680` |
| baseline | `mmlu_4265` | `mcq` | false | `C` | `A. 4.5` |
| baseline | `mmlu_4266` | `mcq` | true | `A` | `A. 240` |
| baseline | `mmlu_4267` | `mcq` | true | `A` | `A. 24` |
| baseline | `mmlu_4268` | `mcq` | true | `B` | `B. -3` |
| baseline | `mmlu_4269` | `mcq` | true | `C` | `C. 10` |
| baseline | `mmlu_4270` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4271` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4272` | `mcq` | false | `C` | `B. 90950` |
| baseline | `mmlu_4273` | `mcq` | true | `D` | `D. \frac{1}{35}` |
| baseline | `mmlu_4274` | `mcq` | false | `D` | `C. 17` |
| baseline | `mmlu_4275` | `mcq` | false | `A` | `B. 5` |
| baseline | `mmlu_4276` | `mcq` | false | `D` | `A. 792` |
| baseline | `mmlu_4277` | `mcq` | true | `B` | `B. -75` |
| baseline | `mmlu_4278` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4279` | `mcq` | true | `A` | `A. 100` |
| baseline | `mmlu_4280` | `mcq` | true | `B` | `B. 9` |
| baseline | `mmlu_4281` | `mcq` | true | `C` | `C. 42` |
| baseline | `mmlu_4282` | `mcq` | false | `C` | `B. \frac{1}{64}` |
| baseline | `mmlu_4283` | `mcq` | false | `A` | `B. \frac{25}{6}` |
| baseline | `mmlu_4284` | `mcq` | false | `B` | `C. \frac{1}{7}` |
| baseline | `mmlu_4285` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4286` | `mcq` | false | `B` | `D. 12` |
| baseline | `mmlu_4287` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_4288` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4289` | `mcq` | true | `B` | `B. 4.875` |
| baseline | `mmlu_4290` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4291` | `mcq` | false | `D` | `A. 211` |
| baseline | `mmlu_4292` | `mcq` | true | `C` | `C. -128` |
| baseline | `mmlu_4293` | `mcq` | false | `B` | `A. –12` |
| baseline | `mmlu_4294` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_4295` | `mcq` | false | `B` | `C. 18` |
| baseline | `mmlu_4296` | `mcq` | true | `D` | `D. \frac{1}{3}` |
| baseline | `mmlu_4297` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_4298` | `mcq` | true | `C` | `C. 625` |
| baseline | `mmlu_4299` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4300` | `mcq` | false | `A` | `C. 27` |
| baseline | `mmlu_4301` | `mcq` | false | `C` | `B. 13` |
| baseline | `mmlu_4302` | `mcq` | false | `B` | `D. 16` |
| baseline | `mmlu_4303` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4304` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4305` | `mcq` | false | `A` | `C. 11` |
| baseline | `mmlu_4306` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4307` | `mcq` | true | `B` | `B. January 21st` |
| baseline | `mmlu_4308` | `mcq` | true | `B` | `B. 76` |
| baseline | `mmlu_4309` | `mcq` | true | `A` | `A. 89` |
| baseline | `mmlu_4310` | `mcq` | false | `C` | `A. 11` |
| baseline | `mmlu_4311` | `mcq` | false | `D` | `A. 6` |
| baseline | `mmlu_4312` | `mcq` | false | `D` | `C. 60` |
| baseline | `mmlu_4313` | `mcq` | true | `B` | `B. 5k` |
| baseline | `mmlu_4314` | `mcq` | true | `D` | `D. 21` |
| baseline | `mmlu_4315` | `mcq` | false | `A` | `B. 72` |
| baseline | `mmlu_4316` | `mcq` | false | `D` | `C. 32` |
| baseline | `mmlu_4317` | `mcq` | false | `C` | `D. 0` |
| baseline | `mmlu_4318` | `mcq` | false | `B` | `A. 36` |
| baseline | `mmlu_4319` | `mcq` | false | `C` | `A. \frac{x-5}{3}` |
| baseline | `mmlu_4320` | `mcq` | true | `B` | `B. -1` |
| baseline | `mmlu_4321` | `mcq` | false | `D` | `B. 16` |
| baseline | `mmlu_4322` | `mcq` | true | `A` | `A. \frac{5}{12}` |
| baseline | `mmlu_4323` | `mcq` | true | `A` | `A. -1/144` |
| baseline | `mmlu_4324` | `mcq` | false | `A` | `C. 0.33` |
| baseline | `mmlu_4325` | `mcq` | true | `B` | `B. 30%` |
| baseline | `mmlu_4326` | `mcq` | false | `C` | `A. 9` |
| baseline | `mmlu_4327` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4328` | `mcq` | false | `B` | `D. 7+2x` |
| baseline | `mmlu_4329` | `mcq` | false | `D` | `A. 13` |
| baseline | `mmlu_4330` | `mcq` | false | `C` | `D. 54,320` |
| baseline | `mmlu_4331` | `mcq` | true | `D` | `D. 25` |
| baseline | `mmlu_4332` | `mcq` | true | `D` | `D. \frac{2500}{52969}` |
| baseline | `mmlu_4333` | `mcq` | true | `A` | `A. 2` |
| baseline | `mmlu_4334` | `mcq` | true | `B` | `B. 31` |
| baseline | `mmlu_4335` | `mcq` | false | `C` | `A. 34` |
| baseline | `mmlu_4336` | `mcq` | false | `C` | `B. 16` |
| baseline | `mmlu_4337` | `mcq` | false | `D` | `B. \frac{7}{9}` |
| baseline | `mmlu_4338` | `mcq` | true | `C` | `C. 3.82` |
| baseline | `mmlu_4339` | `mcq` | false | `C` | `A. 300` |
| baseline | `mmlu_4340` | `mcq` | false | `A` | `B. 46` |
| baseline | `mmlu_4341` | `mcq` | false | `A` | `B. 7^(1/12)` |
| baseline | `mmlu_4342` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_4343` | `mcq` | false | `A` | `D. 20` |
| baseline | `mmlu_4344` | `mcq` | false | `C` | `B. 1` |
| baseline | `mmlu_4345` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4346` | `mcq` | true | `A` | `A. 288` |
| baseline | `mmlu_4347` | `mcq` | false | `B` | `A. 16` |
| baseline | `mmlu_4348` | `mcq` | false | `B` | `C. 1000` |
| baseline | `mmlu_4349` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4350` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4351` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_4352` | `mcq` | true | `D` | `D. \frac{72}{425}` |
| baseline | `mmlu_4353` | `mcq` | true | `D` | `D. 20` |
| baseline | `mmlu_4354` | `mcq` | false | `A` | `D. 614,126` |
| baseline | `mmlu_4355` | `mcq` | true | `C` | `C. 1.18` |
| baseline | `mmlu_4356` | `mcq` | true | `C` | `C. 0.547` |
| baseline | `mmlu_4357` | `mcq` | false | `B` | `C. 4` |
| baseline | `mmlu_4358` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_4359` | `mcq` | false | `B` | `A. 3` |
| baseline | `mmlu_4360` | `mcq` | true | `D` | `D. 71` |
| baseline | `mmlu_4361` | `mcq` | true | `B` | `B. 320` |
| baseline | `mmlu_4362` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4363` | `mcq` | false | `B` | `D. 99` |
| baseline | `mmlu_4364` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_4365` | `mcq` | false | `B` | `C. 45` |
| baseline | `mmlu_4366` | `mcq` | true | `B` | `B. 5400` |
| baseline | `mmlu_4367` | `mcq` | true | `D` | `D. 8.6` |
| baseline | `mmlu_4368` | `mcq` | false | `D` | `A. Domain and range remain the same` |
| baseline | `mmlu_4369` | `mcq` | false | `B` | `C. 112` |
| baseline | `mmlu_4370` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4371` | `mcq` | true | `A` | `A. 90` |
| baseline | `mmlu_4372` | `mcq` | true | `D` | `D. 25` |
| baseline | `mmlu_4373` | `mcq` | false | `D` | `B. 84/3` |
| baseline | `mmlu_4374` | `mcq` | false | `A` | `B. 99` |
| baseline | `mmlu_4375` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4376` | `mcq` | false | `D` | `A. -\frac{7}{12}` |
| baseline | `mmlu_4377` | `mcq` | false | `D` | `B. 59` |
| baseline | `mmlu_4378` | `mcq` | true | `C` | `C. -1.5` |
| baseline | `mmlu_4379` | `mcq` | false | `C` | `D. 574` |
| baseline | `mmlu_4380` | `mcq` | false | `C` | `A. 12` |
| baseline | `mmlu_4381` | `mcq` | true | `B` | `B. 298` |
| baseline | `mmlu_4382` | `mcq` | true | `A` | `A. \frac{8}{45}` |
| baseline | `mmlu_4383` | `mcq` | true | `C` | `C. 9` |
| baseline | `mmlu_4384` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4385` | `mcq` | false | `D` | `A. 1` |
| baseline | `mmlu_4386` | `mcq` | false | `B` | `A. 38` |
| baseline | `mmlu_4387` | `mcq` | true | `A` | `A. 7` |
| baseline | `mmlu_4388` | `mcq` | true | `A` | `A. 1` |
| baseline | `mmlu_4389` | `mcq` | true | `B` | `B. $8,902` |
| baseline | `mmlu_4390` | `mcq` | true | `D` | `D. 3,003` |
| baseline | `mmlu_4391` | `mcq` | true | `C` | `C. 3.743` |
| baseline | `mmlu_4392` | `mcq` | true | `B` | `B. 0` |
| baseline | `mmlu_4393` | `mcq` | false | `D` | `A. 256` |
| baseline | `mmlu_4394` | `mcq` | true | `B` | `B. 40` |
| baseline | `mmlu_4395` | `mcq` | false | `B` | `A. –8%` |
| baseline | `mmlu_4396` | `mcq` | true | `B` | `B. \frac{15}{2}` |
| baseline | `mmlu_4397` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4398` | `mcq` | false | `D` | `C. 4-i` |
| baseline | `mmlu_4399` | `mcq` | true | `C` | `C. 39` |
| baseline | `mmlu_4400` | `mcq` | true | `B` | `B. 3` |
| baseline | `mmlu_4401` | `mcq` | false | `C` | `A. \frac{5}{7}` |
| baseline | `mmlu_4402` | `mcq` | false | `C` | `A. 5%` |
| baseline | `mmlu_4403` | `mcq` | true | `C` | `C. 3980` |
| baseline | `mmlu_4404` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4405` | `mcq` | false | `D` | `B. \frac{17}{66}` |
| baseline | `mmlu_4406` | `mcq` | true | `A` | `A. \frac{485}{486}` |
| baseline | `mmlu_4407` | `mcq` | false | `D` | `B. 32π/3` |
| baseline | `mmlu_4408` | `mcq` | true | `A` | `A. \frac{5}{4}` |
| baseline | `mmlu_4409` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4410` | `mcq` | false | `A` | `C. 40` |
| baseline | `mmlu_4411` | `mcq` | false | `C` | `A. 2` |
| baseline | `mmlu_4412` | `mcq` | false | `C` | `B. 22140` |
| baseline | `mmlu_4413` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4414` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4415` | `mcq` | true | `C` | `C. 36` |
| baseline | `mmlu_4416` | `mcq` | true | `B` | `B. 55` |
| baseline | `mmlu_4417` | `mcq` | false | `A` | `B. 28` |
| baseline | `mmlu_4418` | `mcq` | false | `C` | `A. \frac{5}{24}` |
| baseline | `mmlu_4419` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_4420` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4421` | `mcq` | false | `C` | `B. 6` |
| baseline | `mmlu_4422` | `mcq` | false | `B` | `C. \frac{1}{71}` |
| baseline | `mmlu_4423` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4424` | `mcq` | false | `D` | `C. p-q-r` |
| baseline | `mmlu_4425` | `mcq` | true | `B` | `B. 2 × 5` |
| baseline | `mmlu_4426` | `mcq` | false | `D` | `B. 6` |
| baseline | `mmlu_4427` | `mcq` | true | `C` | `C. (–3, 2)` |
| baseline | `mmlu_4428` | `mcq` | false | `C` | `B. 20` |
| baseline | `mmlu_4429` | `mcq` | true | `D` | `D. \frac{7}{15}` |
| baseline | `mmlu_4430` | `mcq` | false | `D` | `A. 67` |
| baseline | `mmlu_4431` | `mcq` | true | `B` | `B. -14` |
| baseline | `mmlu_4432` | `mcq` | true | `A` | `A. 50 + 50i` |
| baseline | `mmlu_4433` | `mcq` | false | `D` | `A. 10` |
| baseline | `mmlu_4434` | `mcq` | true | `A` | `A. -49` |
| baseline | `mmlu_4435` | `mcq` | false | `C` | `A. 46/3` |
| baseline | `mmlu_4436` | `mcq` | false | `A` | `C. -9` |
| baseline | `mmlu_4437` | `mcq` | false | `A` | `C. 8` |
| baseline | `mmlu_4438` | `mcq` | false | `C` | `B. 36 inches` |
| baseline | `mmlu_4439` | `mcq` | true | `C` | `C. \frac{13}{2}` |
| baseline | `mmlu_4440` | `mcq` | false | `C` | `A. 2` |
| baseline | `mmlu_4441` | `mcq` | false | `D` | `A. \frac{3}{4}` |
| baseline | `mmlu_4442` | `mcq` | false | `D` | `B. 3` |
| baseline | `mmlu_4443` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4444` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4445` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4446` | `mcq` | true | `A` | `A. \frac{1}{2}` |
| baseline | `mmlu_4447` | `mcq` | false | `B` | `C. 12` |
| baseline | `mmlu_4448` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_4449` | `mcq` | true | `B` | `B. 400` |
| baseline | `mmlu_4450` | `mcq` | true | `B` | `B. \frac{161}{36}` |
| baseline | `mmlu_4451` | `mcq` | true | `A` | `A. 112` |
| baseline | `mmlu_4452` | `mcq` | false | `D` | `C. 12` |
| baseline | `mmlu_4453` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4454` | `mcq` | false | `A` | `B. 120` |
| baseline | `mmlu_4455` | `mcq` | false | `B` | `C. 2.427` |
| baseline | `mmlu_4456` | `mcq` | false | `C` | `A. 32` |
| baseline | `mmlu_4457` | `mcq` | false | `B` | `C. 87` |
| baseline | `mmlu_4458` | `mcq` | true | `A` | `A. 165` |
| baseline | `mmlu_4459` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4460` | `mcq` | false | `A` | `B. 276` |
| baseline | `mmlu_4461` | `mcq` | false | `C` | `A. 28` |
| baseline | `mmlu_4462` | `mcq` | false | `D` | `B. 1` |
| baseline | `mmlu_4463` | `mcq` | true | `C` | `C. 2,160` |
| baseline | `mmlu_4464` | `mcq` | false | `C` | `B. 33` |
| baseline | `mmlu_4465` | `mcq` | false | `A` | `B. 12` |
| baseline | `mmlu_4466` | `mcq` | false | `B` | `A. \frac{4\sqrt{3}}{33}` |
| baseline | `mmlu_4467` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4468` | `mcq` | false | `A` | `B. \frac{27}{128}` |
| baseline | `mmlu_4469` | `mcq` | true | `B` | `B. east` |
| baseline | `mmlu_4470` | `mcq` | true | `C` | `C. 17` |
| baseline | `mmlu_4471` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_4472` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4473` | `mcq` | true | `C` | `C. θ=  0.47` |
| baseline | `mmlu_4474` | `mcq` | true | `D` | `D. 12.68` |
| baseline | `mmlu_4475` | `mcq` | false | `C` | `A. none` |
| baseline | `mmlu_4476` | `mcq` | false | `D` | `C. 4` |
| baseline | `mmlu_4477` | `mcq` | false | `C` | `A. [-1/2, 0]` |
| baseline | `mmlu_4478` | `mcq` | false | `B` | `C. 3` |
| baseline | `mmlu_4479` | `mcq` | false | `D` | `B. 2049` |
| baseline | `mmlu_4480` | `mcq` | false | `B` | `A. 3` |
| baseline | `mmlu_4481` | `mcq` | false | `B` | `C. 9.2` |
| baseline | `mmlu_4482` | `mcq` | true | `B` | `B. 800,000 + 650 D` |
| baseline | `mmlu_4483` | `mcq` | false | `B` | `C. 4` |
| baseline | `mmlu_4484` | `mcq` | false | `D` | `B. -2` |
| baseline | `mmlu_4485` | `mcq` | true | `B` | `B. 27` |
| baseline | `mmlu_4486` | `mcq` | true | `B` | `B. \frac{1}{12}` |
| baseline | `mmlu_4487` | `mcq` | true | `A` | `A. (0, 9)` |
| baseline | `mmlu_4488` | `mcq` | false | `D` | `A. 56\sqrt{15}` |
| baseline | `mmlu_4489` | `mcq` | false | `C` | `B. 4680` |
| baseline | `mmlu_4490` | `mcq` | true | `A` | `A. 5, 14` |
| baseline | `mmlu_4491` | `mcq` | false | `D` | `A. 640` |
| baseline | `mmlu_4492` | `mcq` | false | `D` | `C. 3.999` |
| baseline | `mmlu_4493` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4495` | `mcq` | false | `B` | `C. 7.98` |
| baseline | `mmlu_4496` | `mcq` | false | `D` | `B. \frac{1825}{4}` |
| baseline | `mmlu_4497` | `mcq` | false | `B` | `A. -80` |
| baseline | `mmlu_4498` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4499` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4500` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4501` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4502` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4503` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4505` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4506` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4507` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4508` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4509` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4510` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4512` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4514` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4515` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4516` | `mcq` | true | `B` | `B. Market failure` |
| baseline | `mmlu_4517` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4518` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4519` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4520` | `mcq` | true | `D` | `D. I and III only.` |
| baseline | `mmlu_4521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4522` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4523` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4524` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4525` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4526` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4527` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4528` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4529` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4530` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4532` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4533` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4534` | `mcq` | true | `B` | `B. substitution effect.` |
| baseline | `mmlu_4535` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4536` | `mcq` | false | `A` | `C. increase price as demand is elastic.` |
| baseline | `mmlu_4537` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4538` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4539` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4540` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4541` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4542` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4543` | `mcq` | true | `D` | `D. The International Space Station` |
| baseline | `mmlu_4544` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4545` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4546` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4547` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4548` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4549` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4550` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4551` | `mcq` | true | `B` | `B. elastic.` |
| baseline | `mmlu_4552` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4553` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4554` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4555` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4556` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4557` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4558` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4559` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4560` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4561` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4562` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4563` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4564` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4565` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4566` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4567` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4568` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4569` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4570` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4571` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4572` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4573` | `mcq` | false | `D` | `A. decrease price because demand is elastic` |
| baseline | `mmlu_4574` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4575` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4576` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4578` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4579` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4580` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4581` | `mcq` | false | `D` | `A. I, III, and V only` |
| baseline | `mmlu_4582` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4583` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4584` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4585` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4586` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4587` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4588` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4589` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4590` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4591` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4592` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4593` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4594` | `mcq` | true | `B` | `B. Price rises, but the change in quantity is ambiguous.` |
| baseline | `mmlu_4595` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4596` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4597` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4598` | `mcq` | true | `D` | `D. opportunity cost.` |
| baseline | `mmlu_4599` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4600` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4601` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4602` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4603` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4604` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4605` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4606` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4607` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4608` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4609` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4610` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4611` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4612` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4613` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4614` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4615` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4616` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4617` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4618` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4619` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4620` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4621` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4622` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4623` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4624` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4625` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4626` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4627` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4628` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4629` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4630` | `mcq` | true | `B` | `B. Subsidize the firm or its customers.` |
| baseline | `mmlu_4631` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4632` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4634` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4635` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4636` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4637` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4638` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4639` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4640` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4641` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4642` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4643` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4644` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4645` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4646` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4647` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4648` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4649` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4650` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4651` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4652` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4653` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4654` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4655` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4656` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4657` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4658` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4659` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4660` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4661` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4662` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4663` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4664` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4665` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4666` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4667` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4668` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4669` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4670` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4671` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4672` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4673` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4674` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4675` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4676` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4678` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4679` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4680` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4681` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4682` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4683` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4684` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4685` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4686` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4687` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4688` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4689` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4690` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4691` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4692` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4693` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4694` | `mcq` | true | `C` | `C. the marginal cost curve intersects the demand curve` |
| baseline | `mmlu_4695` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4696` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4697` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4698` | `mcq` | true | `B` | `B. law of demand` |
| baseline | `mmlu_4699` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4700` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4701` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4702` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4703` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4704` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4705` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4706` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4707` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4708` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4709` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4710` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4712` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4713` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4714` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4715` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4716` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4717` | `mcq` | true | `B` | `B. Increases` |
| baseline | `mmlu_4718` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4719` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4720` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4721` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4722` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4723` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4724` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4725` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4726` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4727` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4728` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4729` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4730` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4731` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4732` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4733` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4734` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4735` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4736` | `mcq` | false | `B` | `C. 0.02 C` |
| baseline | `mmlu_4737` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4738` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4739` | `mcq` | false | `C` | `A. Less` |
| baseline | `mmlu_4740` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_4741` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4742` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4743` | `mcq` | true | `C` | `C. 0.05 J` |
| baseline | `mmlu_4744` | `mcq` | true | `A` | `A. v0^2/(2μg)` |
| baseline | `mmlu_4745` | `mcq` | false | `B` | `C. 2 s` |
| baseline | `mmlu_4746` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4747` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4748` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4749` | `mcq` | false | `B` | `D. 0.03 s` |
| baseline | `mmlu_4750` | `mcq` | false | `B` | `D. 0.5 N/kg` |
| baseline | `mmlu_4751` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4752` | `mcq` | false | `D` | `A. 1 nm` |
| baseline | `mmlu_4753` | `mcq` | false | `C` | `B. 100 cm` |
| baseline | `mmlu_4754` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4755` | `mcq` | false | `D` | `A. –165 V` |
| baseline | `mmlu_4756` | `mcq` | true | `B` | `B. 300 J out of the system` |
| baseline | `mmlu_4757` | `mcq` | false | `C` | `B. It will quadruple.` |
| baseline | `mmlu_4758` | `mcq` | true | `A` | `A. 5 × 10^15 Hz` |
| baseline | `mmlu_4759` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4760` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4761` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4762` | `mcq` | false | `C` | `B. 6 m/s` |
| baseline | `mmlu_4763` | `mcq` | false | `C` | `A. 1/3 V` |
| baseline | `mmlu_4764` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4765` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4766` | `mcq` | true | `A` | `A. 1.41v` |
| baseline | `mmlu_4767` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4768` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4769` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4770` | `mcq` | false | `C` | `D. I & III only` |
| baseline | `mmlu_4771` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4772` | `mcq` | false | `C` | `A. 5.0 × 10^6 m/s` |
| baseline | `mmlu_4773` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4774` | `mcq` | false | `A` | `B. 150 J of heat was removed from the gas.` |
| baseline | `mmlu_4775` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4776` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4777` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4778` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4779` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4780` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4781` | `mcq` | false | `B` | `C. 2.0/3` |
| baseline | `mmlu_4782` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4783` | `mcq` | false | `B` | `D. 1/2d` |
| baseline | `mmlu_4784` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4785` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4786` | `mcq` | true | `A` | `A. 2 cm ≤ D ≤ 10 cm` |
| baseline | `mmlu_4787` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4788` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4789` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4790` | `mcq` | false | `B` | `C. 2f` |
| baseline | `mmlu_4791` | `mcq` | false | `D` | `A. -3/5 cm` |
| baseline | `mmlu_4792` | `mcq` | false | `C` | `D. -99m` |
| baseline | `mmlu_4793` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4794` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4795` | `mcq` | false | `C` | `A. 1 N` |
| baseline | `mmlu_4796` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4797` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4798` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4799` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4800` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4801` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4802` | `mcq` | false | `C` | `A. 5.0 × 10^5 m/s` |
| baseline | `mmlu_4803` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4804` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4805` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4806` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4807` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4809` | `mcq` | false | `B` | `D. 4v` |
| baseline | `mmlu_4810` | `mcq` | false | `A` | `B. only when the enclosed charge is symmetrically distributed` |
| baseline | `mmlu_4811` | `mcq` | true | `B` | `B. speed and wavelength` |
| baseline | `mmlu_4812` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4813` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4814` | `mcq` | true | `D` | `D. All reach the base at the same time.` |
| baseline | `mmlu_4815` | `mcq` | false | `A` | `B. 300 m` |
| baseline | `mmlu_4816` | `mcq` | false | `D` | `C. 45°` |
| baseline | `mmlu_4817` | `mcq` | false | `D` | `B. 41°` |
| baseline | `mmlu_4818` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4819` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4820` | `mcq` | false | `A` | `C. 200 μN` |
| baseline | `mmlu_4821` | `mcq` | false | `A` | `D. Linear momentum` |
| baseline | `mmlu_4822` | `mcq` | false | `C` | `D. 60 m` |
| baseline | `mmlu_4823` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4824` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4825` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4826` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4827` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4828` | `mcq` | false | `C` | `B. 1.0 m/s` |
| baseline | `mmlu_4829` | `mcq` | false | `D` | `C. The image gets smaller at first and then bigger in size.` |
| baseline | `mmlu_4830` | `mcq` | false | `D` | `A. Zero` |
| baseline | `mmlu_4831` | `mcq` | false | `B` | `A. 200 N` |
| baseline | `mmlu_4832` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4833` | `mcq` | false | `C` | `A. 5.4 × 10–10 J` |
| baseline | `mmlu_4834` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4835` | `mcq` | false | `C` | `A. 0.16 N` |
| baseline | `mmlu_4836` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4837` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4838` | `mcq` | true | `B` | `B. 25 m/s, downward` |
| baseline | `mmlu_4839` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4840` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4841` | `mcq` | false | `B` | `D. Decreasing the mass of the ball` |
| baseline | `mmlu_4842` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4843` | `mcq` | false | `D` | `B. 0.8 m` |
| baseline | `mmlu_4844` | `mcq` | true | `C` | `C. 4 s` |
| baseline | `mmlu_4845` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4846` | `mcq` | false | `B` | `C. 9.8 m/s^2` |
| baseline | `mmlu_4847` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4848` | `mcq` | true | `A` | `A. Static friction` |
| baseline | `mmlu_4849` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4850` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4851` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4852` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4853` | `mcq` | false | `C` | `B. 2h` |
| baseline | `mmlu_4854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4855` | `mcq` | true | `C` | `C. 10^19 N` |
| baseline | `mmlu_4856` | `mcq` | false | `D` | `C. 60%` |
| baseline | `mmlu_4857` | `mcq` | true | `C` | `C. 18 m/s^2` |
| baseline | `mmlu_4858` | `mcq` | false | `A` | `D. No.` |
| baseline | `mmlu_4859` | `mcq` | false | `A` | `B. 10.5 s` |
| baseline | `mmlu_4860` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_4861` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4862` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4863` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4864` | `mcq` | false | `D` | `A. 100 μC` |
| baseline | `mmlu_4865` | `mcq` | false | `B` | `C. 4.5 N` |
| baseline | `mmlu_4866` | `mcq` | true | `D` | `D. a combination of the normal force and the friction force` |
| baseline | `mmlu_4867` | `mcq` | true | `C` | `C. 50 m/s` |
| baseline | `mmlu_4868` | `mcq` | true | `D` | `D. It remains the same.` |
| baseline | `mmlu_4869` | `mcq` | false | `B` | `A. 0.25 A` |
| baseline | `mmlu_4870` | `mcq` | false | `B` | `A. P decreases by a factor of 16.` |
| baseline | `mmlu_4871` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4872` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4873` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4874` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4875` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4876` | `mcq` | true | `C` | `C. Both the length and area` |
| baseline | `mmlu_4877` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4878` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4879` | `mcq` | false | `A` | `D. 1/2 F` |
| baseline | `mmlu_4880` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4881` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4882` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4883` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4884` | `mcq` | false | `D` | `C. (1/5) AU` |
| baseline | `mmlu_4885` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4886` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4887` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4888` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4889` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4890` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4891` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4892` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4893` | `mcq` | true | `A` | `A. variance` |
| baseline | `mmlu_4894` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4895` | `mcq` | false | `A` | `B. in the middle of the list` |
| baseline | `mmlu_4896` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4897` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4898` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4899` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4900` | `mcq` | true | `B` | `B. standardized` |
| baseline | `mmlu_4901` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4902` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4903` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4904` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4905` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4906` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4907` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4908` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4909` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4910` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4911` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4912` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4913` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4914` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4915` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4916` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4918` | `mcq` | true | `A` | `A. Inferential statistics` |
| baseline | `mmlu_4919` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4920` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4921` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4922` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4923` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4924` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4925` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4926` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4927` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4928` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4929` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4930` | `mcq` | true | `B` | `B. remembering how to tie a tie` |
| baseline | `mmlu_4931` | `mcq` | true | `D` | `D. survey` |
| baseline | `mmlu_4932` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4933` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4934` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4935` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4936` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4937` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4938` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4939` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4940` | `mcq` | true | `D` | `D. dissociative` |
| baseline | `mmlu_4941` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4942` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4943` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4944` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4945` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4946` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4947` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4948` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4949` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4950` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4951` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4952` | `mcq` | false | `B` | `C. red` |
| baseline | `mmlu_4953` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4954` | `mcq` | true | `A` | `A. olfactory receptors` |
| baseline | `mmlu_4955` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4956` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4957` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4958` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4959` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4960` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4961` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4962` | `mcq` | true | `D` | `D. positive psychology` |
| baseline | `mmlu_4963` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4964` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4965` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4966` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4967` | `mcq` | true | `D` | `D. brain plasticity` |
| baseline | `mmlu_4968` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4969` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4970` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4971` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4972` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4973` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4974` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4975` | `mcq` | false | `B` | `A. 9` |
| baseline | `mmlu_4976` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4977` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4978` | `mcq` | true | `B` | `B. long-term potentiation` |
| baseline | `mmlu_4979` | `mcq` | false | `C` | `A. sensation and perception` |
| baseline | `mmlu_4980` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4981` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4982` | `mcq` | true | `D` | `D. post-traumatic stress disorder` |
| baseline | `mmlu_4983` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4984` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4985` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4986` | `mcq` | true | `D` | `D. Melatonin` |
| baseline | `mmlu_4987` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4988` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4989` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4990` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4991` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4992` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4993` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4994` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4995` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4996` | `mcq` | true | `D` | `D. Mania` |
| baseline | `mmlu_4997` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4998` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4999` | `mcq` | true | `C` | `C. 90` |
| baseline | `mmlu_5000` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5001` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5002` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5003` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5004` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5005` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5006` | `mcq` | true | `D` | `D. language acquisition device` |
| baseline | `mmlu_5007` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5008` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5009` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5010` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5011` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5012` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5013` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5014` | `mcq` | true | `B` | `B. standardized` |
| baseline | `mmlu_5015` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5016` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5017` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5018` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5019` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5020` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5021` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5022` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5023` | `mcq` | true | `D` | `D. difference threshold` |
| baseline | `mmlu_5024` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5025` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5026` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5027` | `mcq` | true | `A` | `A. endorphins` |
| baseline | `mmlu_5028` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5029` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5030` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5031` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5032` | `mcq` | true | `D` | `D. median` |
| baseline | `mmlu_5033` | `mcq` | true | `D` | `D. morphemes` |
| baseline | `mmlu_5034` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5035` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5036` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5037` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5038` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5039` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5040` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5041` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5042` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5043` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5044` | `mcq` | true | `D` | `D. hypothalamus` |
| baseline | `mmlu_5045` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5046` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5047` | `mcq` | true | `C` | `C. balance` |
| baseline | `mmlu_5048` | `mcq` | true | `A` | `A. superordinate goals` |
| baseline | `mmlu_5049` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5050` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5051` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5052` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5053` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5054` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5055` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5056` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5057` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5058` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5059` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5060` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5061` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5062` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5063` | `mcq` | true | `D` | `D. psychoanalytic` |
| baseline | `mmlu_5064` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5065` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5066` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5067` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5068` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5069` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5070` | `mcq` | true | `D` | `D. in-group bias` |
| baseline | `mmlu_5071` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5072` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5073` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5074` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5075` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5076` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5077` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5078` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5079` | `mcq` | false | `D` | `B. generalization.` |
| baseline | `mmlu_5080` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5081` | `mcq` | true | `B` | `B. Cognitive` |
| baseline | `mmlu_5082` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5083` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5084` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5085` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5086` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5087` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5088` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5089` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5090` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5091` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5092` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5094` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5095` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5096` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5097` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5098` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5099` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5100` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5101` | `mcq` | false | `A` | `D. association areas` |
| baseline | `mmlu_5102` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5103` | `mcq` | false | `A` | `C. sense of time urgency` |
| baseline | `mmlu_5104` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5105` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5106` | `mcq` | true | `B` | `B. white` |
| baseline | `mmlu_5107` | `mcq` | true | `D` | `D. Dopamine` |
| baseline | `mmlu_5108` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5109` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5110` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5111` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5112` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5113` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5114` | `mcq` | true | `C` | `C. thalamus` |
| baseline | `mmlu_5115` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5116` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5117` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5118` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5119` | `mcq` | true | `D` | `D. separation anxiety` |
| baseline | `mmlu_5120` | `mcq` | true | `B` | `B. confirmation bias` |
| baseline | `mmlu_5121` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5122` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5123` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5125` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5126` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5127` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5128` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5129` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5130` | `mcq` | false | `A` | `B. simultaneous` |
| baseline | `mmlu_5131` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5132` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5133` | `mcq` | false | `B` | `A. recognition` |
| baseline | `mmlu_5134` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5135` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5136` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5137` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5138` | `mcq` | true | `B` | `B. inferential statistics` |
| baseline | `mmlu_5139` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5140` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5141` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5142` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5143` | `mcq` | false | `D` | `A. lack of informed consent` |
| baseline | `mmlu_5144` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5145` | `mcq` | true | `B` | `B. cerebral cortex` |
| baseline | `mmlu_5146` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5147` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5148` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5149` | `mcq` | true | `D` | `D. collective unconscious` |
| baseline | `mmlu_5150` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5151` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5152` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5153` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5154` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5155` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5156` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5157` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5158` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5159` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5160` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5161` | `mcq` | true | `D` | `D. superordinate goals` |
| baseline | `mmlu_5162` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5163` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5164` | `mcq` | true | `D` | `D. rational emotive` |
| baseline | `mmlu_5165` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5166` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5167` | `mcq` | false | `D` | `A. green` |
| baseline | `mmlu_5168` | `mcq` | true | `D` | `D. superego` |
| baseline | `mmlu_5169` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5170` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5171` | `mcq` | true | `B` | `B. Visual imagery` |
| baseline | `mmlu_5172` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5173` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5174` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5175` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5176` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5177` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5178` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5179` | `mcq` | true | `D` | `D. prefrontal cortex` |
| baseline | `mmlu_5180` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5181` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5182` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5183` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5184` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5185` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5186` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5187` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5188` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5189` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5190` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5191` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5192` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5193` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5194` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5195` | `mcq` | true | `D` | `D. 60` |
| baseline | `mmlu_5196` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5197` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5198` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5199` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5200` | `mcq` | true | `D` | `D. attachment` |
| baseline | `mmlu_5201` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5202` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5203` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5204` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5205` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5206` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5207` | `mcq` | true | `B` | `B. reflex` |
| baseline | `mmlu_5208` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5209` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5210` | `mcq` | true | `B` | `B. remembering how to tie a tie` |
| baseline | `mmlu_5211` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5212` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5213` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5214` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5215` | `mcq` | true | `B` | `B. dopamine` |
| baseline | `mmlu_5216` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5217` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5218` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5219` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5220` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5221` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5222` | `mcq` | true | `D` | `D. flat affect` |
| baseline | `mmlu_5223` | `mcq` | true | `A` | `A. Duty to warn and protect` |
| baseline | `mmlu_5224` | `mcq` | true | `D` | `D. gate-control theory` |
| baseline | `mmlu_5225` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5226` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5227` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5228` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5229` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5230` | `mcq` | true | `D` | `D. cones` |
| baseline | `mmlu_5231` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5232` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5233` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5234` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5235` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5236` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5237` | `mcq` | true | `B` | `B. double blind study` |
| baseline | `mmlu_5238` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5239` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5240` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5241` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5242` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5243` | `mcq` | true | `D` | `D. Difference threshold` |
| baseline | `mmlu_5244` | `mcq` | true | `D` | `D. Systems approach` |
| baseline | `mmlu_5245` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5246` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5247` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5248` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5249` | `mcq` | false | `B` | `A. Median` |
| baseline | `mmlu_5250` | `mcq` | false | `D` | `B. dishabituation` |
| baseline | `mmlu_5251` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5252` | `mcq` | true | `C` | `C. Homeostasis` |
| baseline | `mmlu_5253` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5254` | `mcq` | true | `B` | `B. secondary` |
| baseline | `mmlu_5255` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5256` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5257` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5258` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5259` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5260` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5261` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5262` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5263` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5264` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5265` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5266` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5267` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5268` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5269` | `mcq` | true | `D` | `D. License` |
| baseline | `mmlu_5270` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5271` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5272` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5273` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5274` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5275` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5276` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5277` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5278` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5279` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5281` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5282` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5283` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5284` | `mcq` | true | `B` | `B. facial expressions` |
| baseline | `mmlu_5285` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5286` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5287` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5288` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5289` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5290` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5291` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5292` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5293` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5294` | `mcq` | true | `B` | `B. a compulsion` |
| baseline | `mmlu_5295` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5296` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5297` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5298` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5299` | `mcq` | true | `D` | `D. group polarization` |
| baseline | `mmlu_5300` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5301` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5302` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5303` | `mcq` | true | `D` | `D. morpheme` |
| baseline | `mmlu_5304` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5305` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5306` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5307` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5308` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5309` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5310` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5311` | `mcq` | true | `D` | `D. superego` |
| baseline | `mmlu_5312` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5313` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5314` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5316` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5317` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5318` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5319` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5320` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5321` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5322` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5323` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5325` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5326` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5327` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5328` | `mcq` | true | `D` | `D. Diffusion of responsibility` |
| baseline | `mmlu_5329` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5330` | `mcq` | false | `A` | `D. left cerebral cortex` |
| baseline | `mmlu_5331` | `mcq` | false | `D` | `A. frequency` |
| baseline | `mmlu_5332` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5333` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5334` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5335` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5336` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5337` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5338` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5339` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5340` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5341` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5342` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5343` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5344` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5345` | `mcq` | true | `D` | `D. sight` |
| baseline | `mmlu_5346` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5347` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5348` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5349` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5350` | `mcq` | false | `B` | `A. difference threshold` |
| baseline | `mmlu_5351` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5352` | `mcq` | true | `D` | `D. The retina` |
| baseline | `mmlu_5353` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5354` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5355` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5356` | `mcq` | true | `B` | `B. psychiatrist` |
| baseline | `mmlu_5357` | `mcq` | true | `D` | `D. reflex` |
| baseline | `mmlu_5358` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5359` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5360` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5361` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5362` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5363` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5364` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5365` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5366` | `mcq` | false | `D` | `A. experiment` |
| baseline | `mmlu_5367` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5368` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5369` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5370` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5371` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5372` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5373` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5374` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5376` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5378` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5379` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5380` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5381` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5382` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5383` | `mcq` | true | `D` | `D. 95` |
| baseline | `mmlu_5384` | `mcq` | true | `C` | `C. amplitude` |
| baseline | `mmlu_5385` | `mcq` | false | `C` | `B. 3 months` |
| baseline | `mmlu_5386` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5387` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5388` | `mcq` | true | `B` | `B. optic chiasm.` |
| baseline | `mmlu_5389` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5390` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5391` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5392` | `mcq` | true | `B` | `B. inferential statistics` |
| baseline | `mmlu_5393` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5394` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5395` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5396` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5397` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5398` | `mcq` | true | `A` | `A. Occipital` |
| baseline | `mmlu_5399` | `mcq` | true | `D` | `D. causes of all mental disorders` |
| baseline | `mmlu_5400` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5401` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5402` | `mcq` | true | `D` | `D. Changes in behavior over time` |
| baseline | `mmlu_5403` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5404` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5405` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5406` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5407` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5408` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5409` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5410` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5411` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5412` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5413` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5414` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5415` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5416` | `mcq` | false | `D` | `C. cold` |
| baseline | `mmlu_5417` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5418` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5419` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5420` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5421` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5422` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5423` | `mcq` | true | `C` | `C. the local community college and distant community colleges` |
| baseline | `mmlu_5424` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5425` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5426` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5427` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5428` | `mcq` | true | `D` | `D. insight` |
| baseline | `mmlu_5429` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5430` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5431` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5432` | `mcq` | false | `B` | `D. 2P(t > 1.54) with df = 7` |
| baseline | `mmlu_5433` | `mcq` | true | `C` | `C. 25.3 to 44.7 minutes` |
| baseline | `mmlu_5434` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5435` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5436` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5437` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5438` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5439` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5440` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5441` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5442` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5443` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5444` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5445` | `mcq` | false | `C` | `D. decreases the interval size by 57%` |
| baseline | `mmlu_5446` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5447` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_5448` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5449` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5450` | `mcq` | false | `D` | `B. 0.0016` |
| baseline | `mmlu_5451` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5452` | `mcq` | true | `D` | `D. –0.21` |
| baseline | `mmlu_5453` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5454` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5455` | `mcq` | false | `B` | `A. -1` |
| baseline | `mmlu_5456` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5457` | `mcq` | false | `D` | `B. $23,700` |
| baseline | `mmlu_5458` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5459` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5460` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5461` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5462` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5463` | `mcq` | false | `D` | `B. 1.96` |
| baseline | `mmlu_5464` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5465` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5466` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5467` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5468` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5469` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5470` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5471` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5472` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5473` | `mcq` | false | `D` | `B. 100` |
| baseline | `mmlu_5474` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5475` | `mcq` | false | `A` | `B. Sample survey` |
| baseline | `mmlu_5476` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5477` | `mcq` | false | `B` | `A. Plan I` |
| baseline | `mmlu_5478` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5479` | `mcq` | false | `C` | `A. I and III only` |
| baseline | `mmlu_5480` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5481` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5482` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5483` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5484` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5485` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5486` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5487` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5488` | `mcq` | true | `A` | `A. 0.19` |
| baseline | `mmlu_5489` | `mcq` | false | `D` | `A. z = 0.04` |
| baseline | `mmlu_5490` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5491` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5492` | `mcq` | true | `C` | `C. 86.65; she qualified.` |
| baseline | `mmlu_5493` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5494` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5495` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5496` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5497` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5498` | `mcq` | true | `B` | `B. 0.40` |
| baseline | `mmlu_5499` | `mcq` | false | `B` | `A. μ = 3.677, σ = 3.561` |
| baseline | `mmlu_5500` | `mcq` | false | `A` | `C. HA: μ1− μ2≠ 0` |
| baseline | `mmlu_5501` | `mcq` | false | `B` | `A. II only` |
| baseline | `mmlu_5502` | `mcq` | true | `C` | `C. Use of a confounding variable to control the placebo effect` |
| baseline | `mmlu_5503` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5504` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5505` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5506` | `mcq` | false | `D` | `C. 4.085 pounds` |
| baseline | `mmlu_5507` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5508` | `mcq` | true | `D` | `D. 90.4%` |
| baseline | `mmlu_5509` | `mcq` | false | `C` | `D. 141 pounds` |
| baseline | `mmlu_5510` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5512` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5513` | `mcq` | true | `C` | `C. 82.9%` |
| baseline | `mmlu_5514` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5515` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5516` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5517` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5518` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5519` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5521` | `mcq` | false | `C` | `B. An unnecessary stoppage of the production process` |
| baseline | `mmlu_5522` | `mcq` | false | `D` | `B. 0.025` |
| baseline | `mmlu_5523` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5524` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5526` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5527` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5528` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5529` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5530` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5532` | `mcq` | false | `D` | `A. 0.313` |
| baseline | `mmlu_5533` | `mcq` | false | `A` | `B. 8` |
| baseline | `mmlu_5534` | `mcq` | true | `C` | `C. 70 minutes to 264 minutes` |
| baseline | `mmlu_5535` | `mcq` | true | `B` | `B. Her grade will go up by 20.4 points.` |
| baseline | `mmlu_5536` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5537` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5538` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5539` | `mcq` | true | `C` | `C. 84%` |
| baseline | `mmlu_5540` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5541` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5542` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5543` | `mcq` | true | `A` | `A. 0.235` |
| baseline | `mmlu_5544` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5545` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5546` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5547` | `mcq` | true | `D` | `D. The answer cannot be determined without knowing the size of the jury pool.` |
| baseline | `mmlu_5548` | `mcq` | false | `D` | `B. 144` |
| baseline | `mmlu_5549` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5550` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5551` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5552` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5553` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5554` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5555` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5556` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5557` | `mcq` | false | `D` | `A. 66.80%` |
| baseline | `mmlu_5558` | `mcq` | false | `D` | `B. 0.1667` |
| baseline | `mmlu_5559` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5560` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5561` | `mcq` | false | `D` | `B. 0.34` |
| baseline | `mmlu_5562` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5563` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5564` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5565` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5566` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5567` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5568` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5569` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5570` | `mcq` | true | `D` | `D. No, because not every sample of the intended size has an equal chance of being selected.` |
| baseline | `mmlu_5571` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5572` | `mcq` | false | `D` | `A. 0.42` |
| baseline | `mmlu_5573` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5574` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5575` | `mcq` | false | `A` | `B. Cluster sample, because the population is divided into five clusters—namely, five offices in five different countries` |
| baseline | `mmlu_5576` | `mcq` | false | `D` | `B. 0.21` |
| baseline | `mmlu_5577` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5578` | `mcq` | true | `D` | `D. No, because the entire population information was used from both offices. Because no samples were taken, a t-test sho` |
| baseline | `mmlu_5579` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5580` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5581` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5582` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5583` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5584` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5585` | `mcq` | true | `C` | `C. μ = 15,300; σ = 6300` |
| baseline | `mmlu_5586` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5587` | `mcq` | false | `D` | `C. 118 points` |
| baseline | `mmlu_5588` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5589` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5590` | `mcq` | false | `B` | `A. $6,984` |
| baseline | `mmlu_5591` | `mcq` | false | `C` | `A. 8.05` |
| baseline | `mmlu_5592` | `mcq` | true | `D` | `D. An experiment` |
| baseline | `mmlu_5593` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5594` | `mcq` | true | `B` | `B. 0.3` |
| baseline | `mmlu_5595` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5596` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5597` | `mcq` | false | `D` | `C. 0.95` |
| baseline | `mmlu_5598` | `mcq` | false | `D` | `B. Standard deviation` |
| baseline | `mmlu_5599` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5600` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5601` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5602` | `mcq` | true | `A` | `A. 0.0057` |
| baseline | `mmlu_5603` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5604` | `mcq` | true | `D` | `D. 0.93` |
| baseline | `mmlu_5605` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5606` | `mcq` | true | `B` | `B. The sample mean and sample median are equal.` |
| baseline | `mmlu_5607` | `mcq` | true | `A` | `A. (3,034, 3,466)` |
| baseline | `mmlu_5608` | `mcq` | false | `D` | `A. 0.460` |
| baseline | `mmlu_5609` | `mcq` | false | `A` | `C. Closing the park when the lead levels are in excess of the allowed limit` |
| baseline | `mmlu_5610` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5611` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5612` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5613` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5614` | `mcq` | true | `B` | `B. 42.3 g` |
| baseline | `mmlu_5615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5616` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5617` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5618` | `mcq` | true | `B` | `B. 0.4096` |
| baseline | `mmlu_5619` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5620` | `mcq` | false | `C` | `B. 0.0112` |
| baseline | `mmlu_5621` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5622` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5623` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5624` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5625` | `mcq` | false | `D` | `A. 0.44, 0.5, 0.2` |
| baseline | `mmlu_5626` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5627` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5628` | `mcq` | true | `D` | `D. 0.65` |
| baseline | `mmlu_5629` | `mcq` | false | `D` | `B. 17.8%` |
| baseline | `mmlu_5630` | `mcq` | true | `B` | `B. 0.1446` |
| baseline | `mmlu_5631` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5632` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5633` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5634` | `mcq` | false | `D` | `B. $91` |
| baseline | `mmlu_5635` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5636` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5637` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5638` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5639` | `mcq` | false | `A` | `D. I only` |
| baseline | `mmlu_5640` | `mcq` | false | `D` | `B. 64` |
| baseline | `mmlu_5641` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_5642` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5643` | `mcq` | true | `D` | `D. The probability of rejecting the null hypothesis if it is, in fact, false.` |
| baseline | `mmlu_5644` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5645` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5646` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5647` | `mcq` | true | `D` | `D. Influential point` |
| baseline | `mmlu_5648` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5649` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5650` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5651` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5652` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5653` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5654` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5655` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5656` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5658` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5659` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5660` | `mcq` | false | `A` | `C. all Christians only` |
| baseline | `mmlu_5661` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5662` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5663` | `mcq` | true | `C` | `C. The Apollo space program` |
| baseline | `mmlu_5664` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5665` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5666` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5668` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5669` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5670` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5671` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5672` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5674` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5675` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5676` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5677` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5678` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5679` | `mcq` | true | `C` | `C. A long tradition of self-rule in the American colonies` |
| baseline | `mmlu_5680` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5681` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5682` | `mcq` | true | `C` | `C. Greater rights for unions` |
| baseline | `mmlu_5683` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5684` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5685` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5686` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5688` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5689` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5690` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5691` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5692` | `mcq` | true | `C` | `C. William M. Tweed` |
| baseline | `mmlu_5693` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5694` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5695` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5696` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5697` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5698` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5699` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5700` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5701` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5702` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5703` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5704` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5705` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5706` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5707` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5708` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5709` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5710` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5712` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5713` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5714` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5715` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5716` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5717` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5718` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5719` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5721` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5722` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5723` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5724` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5725` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5726` | `mcq` | true | `D` | `D. Ireland` |
| baseline | `mmlu_5727` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5728` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5729` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5730` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5731` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5732` | `mcq` | true | `C` | `C. U.S. involvement in Vietnam and the civil rights movement` |
| baseline | `mmlu_5733` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5734` | `mcq` | true | `B` | `B. Expanding territories under Spanish control` |
| baseline | `mmlu_5735` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5736` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5737` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5738` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5739` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5740` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5741` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5742` | `mcq` | true | `C` | `C. an expression of black nationalism.` |
| baseline | `mmlu_5743` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5744` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5745` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5746` | `mcq` | false | `A` | `C. The Cold War` |
| baseline | `mmlu_5747` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5748` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5749` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5750` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5751` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5752` | `mcq` | true | `D` | `D. Declaration of Independence.` |
| baseline | `mmlu_5753` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5754` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5755` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5756` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5758` | `mcq` | true | `C` | `C. Self-government` |
| baseline | `mmlu_5759` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5760` | `mcq` | true | `C` | `C. middle-class college students.` |
| baseline | `mmlu_5761` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5762` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5763` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5764` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5765` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5766` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5767` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5768` | `mcq` | true | `D` | `D. the balanced budget mandate` |
| baseline | `mmlu_5769` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5770` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5771` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5772` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5773` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5774` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5775` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5776` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5777` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5778` | `mcq` | true | `C` | `C. Increased economic and political opportunities for women` |
| baseline | `mmlu_5779` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5780` | `mcq` | true | `B` | `B. Executive Order 9066 interning Japanese Americans` |
| baseline | `mmlu_5781` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5782` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5783` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5784` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5785` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5786` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5787` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5788` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5789` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5790` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5791` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5792` | `mcq` | true | `D` | `D. The Pure Food and Drug Act` |
| baseline | `mmlu_5793` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5794` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5795` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5796` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5797` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5798` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5799` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5800` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5801` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5802` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5803` | `mcq` | false | `A` | `D. Eighteenth century scientific racism` |
| baseline | `mmlu_5804` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5805` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5806` | `mcq` | false | `A` | `B. Supportive of the policies of Thomas Jefferson` |
| baseline | `mmlu_5807` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5808` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5809` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5810` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5811` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5812` | `mcq` | true | `D` | `D. farmers, who hoped that a more generous money supply would ease their debt burdens` |
| baseline | `mmlu_5813` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5814` | `mcq` | true | `C` | `C. The Spanish–American War` |
| baseline | `mmlu_5815` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5816` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5817` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5818` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5819` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5820` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5821` | `mcq` | true | `D` | `D. The creation of an American overseas empire` |
| baseline | `mmlu_5822` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5823` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5824` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5825` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5826` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5827` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5828` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5829` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5830` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5831` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5832` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5833` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5834` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5835` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5836` | `mcq` | true | `C` | `C. Quakers` |
| baseline | `mmlu_5837` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5838` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5839` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5840` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5841` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5842` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5843` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5844` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5845` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5846` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5847` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5848` | `mcq` | true | `D` | `D. the end of the Cold War.` |
| baseline | `mmlu_5849` | `mcq` | false | `B` | `C. Economic recession catalyzed by increased government spending causing "stagflation."` |
| baseline | `mmlu_5850` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5851` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5852` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5853` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5854` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5855` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5856` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5857` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5858` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5859` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5860` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5861` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5862` | `mcq` | true | `B` | `B. He doesn't earn enough on his own.` |
| baseline | `mmlu_5863` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5864` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5865` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5866` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5867` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5868` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5869` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5870` | `mcq` | true | `B` | `B. The ability of the Tang emperor to project military power on the frontier in order to impose his will` |
| baseline | `mmlu_5871` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5872` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5873` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5874` | `mcq` | true | `B` | `B. Nonviolent resistance` |
| baseline | `mmlu_5875` | `mcq` | true | `C` | `C. The encomienda system` |
| baseline | `mmlu_5876` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5877` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5878` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5879` | `mcq` | true | `D` | `D. The defeat of Indian rebels and the imposition of direct rule by the British government` |
| baseline | `mmlu_5880` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5881` | `mcq` | true | `D` | `D. apartheid.` |
| baseline | `mmlu_5882` | `mcq` | true | `C` | `C. the Enlightenment` |
| baseline | `mmlu_5883` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5884` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5885` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5886` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5887` | `mcq` | true | `B` | `B. Killing of civilians during wartime` |
| baseline | `mmlu_5888` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5889` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5890` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5891` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5892` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5893` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5894` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5895` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5896` | `mcq` | false | `D` | `B. Social Darwinism` |
| baseline | `mmlu_5897` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5898` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5899` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5900` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5901` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5902` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5903` | `mcq` | true | `D` | `D. Hardening of anti-immigrant sentiment` |
| baseline | `mmlu_5904` | `mcq` | true | `D` | `D. Persia was brought into the Arabian orbit over the course of the period.` |
| baseline | `mmlu_5905` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5906` | `mcq` | true | `D` | `D. The Crusades` |
| baseline | `mmlu_5907` | `mcq` | false | `B` | `D. John Wycliffe` |
| baseline | `mmlu_5908` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5909` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5910` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5911` | `mcq` | true | `D` | `D. Unforeseen consequences of British imperialism` |
| baseline | `mmlu_5912` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5913` | `mcq` | false | `A` | `C. He had lost the blessing of the gods.` |
| baseline | `mmlu_5914` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5915` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5916` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5917` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5918` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5919` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5920` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5921` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5922` | `mcq` | true | `D` | `D. The New World` |
| baseline | `mmlu_5923` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5924` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5925` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5926` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5927` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5928` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5929` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5930` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5931` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5932` | `mcq` | false | `C` | `D. The political nature of the church` |
| baseline | `mmlu_5933` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5934` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5935` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5936` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5937` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5938` | `mcq` | true | `A` | `A. Rigid societal gender roles` |
| baseline | `mmlu_5939` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5940` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5941` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5942` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5943` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5944` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5945` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5946` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5947` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5948` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5949` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5950` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5951` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5952` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5953` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5954` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5955` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5956` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5957` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5958` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5959` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5960` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5961` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5962` | `mcq` | true | `B` | `B. Unfair systems of taxation` |
| baseline | `mmlu_5963` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5964` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5965` | `mcq` | true | `C` | `C. The end justifies the means` |
| baseline | `mmlu_5966` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5967` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5968` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5969` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5970` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5971` | `mcq` | true | `C` | `C. The importance of sacrifice to the gods` |
| baseline | `mmlu_5972` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5973` | `mcq` | false | `D` | `C. The decolonization process already underway in Africa` |
| baseline | `mmlu_5974` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5975` | `mcq` | true | `C` | `C. The use of religion to ponder conceptions of the afterlife` |
| baseline | `mmlu_5976` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5977` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5978` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5979` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5980` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5981` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5982` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5983` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5984` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5985` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5986` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5987` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5988` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5989` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5990` | `mcq` | true | `C` | `C. contact with Muslim trade caravans.` |
| baseline | `mmlu_5991` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5992` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5993` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5994` | `mcq` | false | `B` | `A. The world is too afraid of South Africa to oppose apartheid.` |
| baseline | `mmlu_5995` | `mcq` | true | `C` | `C. World War II` |
| baseline | `mmlu_5996` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5997` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5998` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5999` | `mcq` | true | `C` | `C. Decolonization` |
| baseline | `mmlu_6000` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6001` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6002` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6003` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6004` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6005` | `mcq` | false | `A` | `C. Protestant` |
| baseline | `mmlu_6006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6007` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6008` | `mcq` | true | `C` | `C. religious regulation of personal behavior in Islamic society.` |
| baseline | `mmlu_6009` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6010` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6011` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6012` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6013` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6014` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6015` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6016` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6017` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6018` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6019` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6020` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6021` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6022` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6023` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6024` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6025` | `mcq` | false | `B` | `C. The general warming of the climate during this time period` |
| baseline | `mmlu_6026` | `mcq` | true | `C` | `C. Large-scale military losses and resentment of the working classes` |
| baseline | `mmlu_6027` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6028` | `mcq` | false | `D` | `C. The game of chess` |
| baseline | `mmlu_6029` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6030` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6031` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6032` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6033` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6034` | `mcq` | true | `C` | `C. Europe's economic domination of China` |
| baseline | `mmlu_6035` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6036` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6037` | `mcq` | true | `D` | `D. Furs` |
| baseline | `mmlu_6038` | `mcq` | true | `D` | `D. Marxism` |
| baseline | `mmlu_6039` | `mcq` | false | `B` | `A. The election of F. W. de Klerk` |
| baseline | `mmlu_6040` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6041` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6042` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6043` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6044` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6045` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6046` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6047` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6048` | `mcq` | false | `D` | `C. Limited economic opportunities` |
| baseline | `mmlu_6049` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6050` | `mcq` | true | `B` | `B. Robespierre` |
| baseline | `mmlu_6051` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6052` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6053` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6054` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6055` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6056` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6057` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6058` | `mcq` | false | `B` | `C. Because these were strongholds of the Holy Roman Empire, the narrator warns the Winter King to stay away.` |
| baseline | `mmlu_6059` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6060` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6061` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6062` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6063` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6064` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6065` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6066` | `mcq` | true | `B` | `B. The compass` |
| baseline | `mmlu_6067` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6068` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6069` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6070` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6071` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6072` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6073` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6074` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6075` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6076` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6077` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6078` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6079` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6080` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6081` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6082` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6083` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6084` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6085` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6086` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6087` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6088` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6089` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6090` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6091` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6092` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6093` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6094` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6095` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6096` | `mcq` | true | `D` | `D. Smarthouse` |
| baseline | `mmlu_6097` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6098` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6099` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6100` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6101` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6102` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6103` | `mcq` | false | `B` | `B6 and B12` |
| baseline | `mmlu_6104` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6105` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6106` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6107` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6108` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6109` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6110` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6111` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6112` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6113` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6114` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6115` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6116` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6117` | `mcq` | true | `B` | `B. Suppression of the immune system` |
| baseline | `mmlu_6118` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6119` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6120` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6121` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6122` | `mcq` | true | `A` | `A. Ageism` |
| baseline | `mmlu_6123` | `mcq` | true | `D` | `D. Hospice` |
| baseline | `mmlu_6124` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6125` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6126` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6127` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6128` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6129` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6130` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6131` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6132` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6133` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6134` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6135` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6136` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6137` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6138` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6139` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6140` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6141` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6142` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6143` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6144` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6145` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6146` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6147` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6148` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6149` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6150` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6151` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6153` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6154` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6155` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6156` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6157` | `mcq` | true | `D` | `D. Hawaii` |
| baseline | `mmlu_6158` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6159` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6160` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6161` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6163` | `mcq` | true | `A` | `A. Prevalence` |
| baseline | `mmlu_6164` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6165` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6166` | `mcq` | true | `B` | `B. About 25%` |
| baseline | `mmlu_6167` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6168` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6169` | `mcq` | true | `B` | `B. Arthritis` |
| baseline | `mmlu_6170` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6171` | `mcq` | false | `A` | `C. 50%` |
| baseline | `mmlu_6172` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6173` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6174` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6175` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6176` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6177` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6178` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6179` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6180` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6181` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6182` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6183` | `mcq` | false | `B` | `D. Clinical depression` |
| baseline | `mmlu_6184` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6185` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6186` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6187` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6188` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6189` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6190` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6191` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6192` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6193` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6194` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6195` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6196` | `mcq` | true | `C` | `C. Japan` |
| baseline | `mmlu_6197` | `mcq` | false | `C` | `B. Choice` |
| baseline | `mmlu_6198` | `mcq` | true | `B` | `B. Internal` |
| baseline | `mmlu_6199` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6200` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6201` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6202` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6203` | `mcq` | true | `B` | `B. Conscientiousness` |
| baseline | `mmlu_6204` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6205` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6206` | `mcq` | true | `C` | `C. Working as a system` |
| baseline | `mmlu_6207` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6208` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6209` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6210` | `mcq` | false | `A` | `B. U. S. A.` |
| baseline | `mmlu_6211` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6212` | `mcq` | true | `D` | `D. The Eden Alternative` |
| baseline | `mmlu_6213` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6214` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6215` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6216` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6217` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6218` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6219` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6220` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6221` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6223` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6224` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6225` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6226` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6227` | `mcq` | true | `A` | `A. Activities of Daily Living` |
| baseline | `mmlu_6228` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6229` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6230` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6231` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6232` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6233` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6234` | `mcq` | true | `B` | `B. Remain in close contact` |
| baseline | `mmlu_6235` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6236` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6237` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6238` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6239` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6240` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6241` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6242` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6243` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6244` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6245` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6246` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6247` | `mcq` | true | `A` | `A. Age` |
| baseline | `mmlu_6248` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6249` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6250` | `mcq` | true | `C` | `C. The contents of the message` |
| baseline | `mmlu_6251` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6252` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6253` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6254` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6255` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6256` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6257` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6258` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6259` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6260` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6261` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6262` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6263` | `mcq` | false | `B` | `C. 50%` |
| baseline | `mmlu_6264` | `mcq` | true | `A` | `A. On foot` |
| baseline | `mmlu_6265` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6266` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6267` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6268` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6269` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6270` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6271` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6272` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6273` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6274` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6275` | `mcq` | true | `C` | `C. More than 50%` |
| baseline | `mmlu_6276` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6277` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6278` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6279` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6280` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6281` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6282` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6283` | `mcq` | false | `A` | `B. 82` |
| baseline | `mmlu_6284` | `mcq` | true | `B` | `B. Green` |
| baseline | `mmlu_6285` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6286` | `mcq` | true | `A` | `A. Height` |
| baseline | `mmlu_6287` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6288` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6289` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6290` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6291` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6292` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6293` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6294` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6295` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6296` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6297` | `mcq` | true | `D` | `D. Intention` |
| baseline | `mmlu_6298` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6299` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6300` | `mcq` | false | `A` | `B. Nurture` |
| baseline | `mmlu_6301` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6302` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6303` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6304` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6305` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6306` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6307` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6308` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6309` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6310` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6311` | `mcq` | false | `B` | `D. Ebbinghaus` |
| baseline | `mmlu_6312` | `mcq` | true | `B` | `B. Mammography` |
| baseline | `mmlu_6313` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6314` | `mcq` | false | `A` | `A, C` |
| baseline | `mmlu_6315` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6316` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6317` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6318` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_6319` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6320` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6321` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6322` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6323` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6325` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6326` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6327` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6328` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6329` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6330` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6331` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6332` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6333` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6334` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6335` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6336` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6337` | `mcq` | false | `B` | `C. 72 hours` |
| baseline | `mmlu_6338` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6339` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6340` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6341` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6342` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6343` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6344` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6345` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6346` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6347` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6348` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6349` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_6350` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6351` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6352` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6353` | `mcq` | true | `C` | `C. 14` |
| baseline | `mmlu_6354` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6355` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6356` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6357` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6358` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6359` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6360` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6361` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6362` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6363` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6364` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6365` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6366` | `mcq` | true | `D` | `D. prepuce` |
| baseline | `mmlu_6367` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6368` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6369` | `mcq` | false | `A` | `D. all of the above` |
| baseline | `mmlu_6370` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6371` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6372` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6373` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6374` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6376` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6378` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6379` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6380` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6381` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6382` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6383` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6384` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6385` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6386` | `mcq` | true | `D` | `D. gonorrhea` |
| baseline | `mmlu_6387` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6388` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6389` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6390` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6391` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6392` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6393` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6394` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6395` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6396` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6397` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6398` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6399` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6400` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6401` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6402` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6403` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6404` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6405` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6406` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6407` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6408` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6409` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6410` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6411` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6412` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6413` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6414` | `mcq` | false | `A` | `C. heterosexual` |
| baseline | `mmlu_6415` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6416` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6417` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_6418` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6419` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6420` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6421` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6422` | `mcq` | true | `B` | `B. Ectopic pregnancy` |
| baseline | `mmlu_6423` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6424` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6425` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6426` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6427` | `mcq` | false | `D` | `A. egg` |
| baseline | `mmlu_6428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6429` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6430` | `mcq` | false | `B` | `A. 5` |
| baseline | `mmlu_6431` | `mcq` | true | `A` | `A. directly into the bloodstream` |
| baseline | `mmlu_6432` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6434` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6435` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6436` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6437` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6438` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6439` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6440` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6441` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6442` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6443` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6444` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6445` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6446` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6447` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6448` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6449` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6450` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6451` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6452` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6453` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6454` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6455` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6456` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6457` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6459` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6460` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6461` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6462` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6463` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6464` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6465` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6466` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6467` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6468` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6469` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6470` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6471` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6472` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6473` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6474` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6475` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6476` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6477` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6478` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6479` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6480` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6481` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6482` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6483` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6484` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6485` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6486` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6487` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6488` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6489` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6490` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6491` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6492` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6493` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6494` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6495` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6496` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6497` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6498` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6499` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6500` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6501` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6502` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6503` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6504` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6505` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6506` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6507` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6508` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6509` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6510` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6512` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6513` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6514` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6515` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6516` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6517` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6518` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6519` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6520` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6521` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6522` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6523` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6524` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6525` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6526` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6527` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6528` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6529` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6530` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6531` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6532` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6533` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6534` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6535` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6536` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6537` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6538` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6539` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6540` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6541` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6542` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6543` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6544` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6545` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6546` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6547` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6548` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6549` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6550` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6551` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6552` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6553` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6554` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6555` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6556` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6557` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6558` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6559` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6560` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6561` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6562` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6563` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6564` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6565` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6566` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6567` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6568` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6569` | `mcq` | true | `A` | `A. Law and Economics` |
| baseline | `mmlu_6570` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6571` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6572` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6573` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6574` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6575` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6576` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6578` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6579` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6580` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6581` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6582` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6583` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6584` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6585` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6586` | `mcq` | true | `B` | `B. stare decisis` |
| baseline | `mmlu_6587` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6588` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6589` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6590` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6591` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6592` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6593` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6594` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6595` | `mcq` | true | `D` | `D. codified` |
| baseline | `mmlu_6596` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6597` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6598` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6599` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6600` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6601` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6602` | `mcq` | true | `B` | `B. Civil Law.` |
| baseline | `mmlu_6603` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6604` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6605` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6606` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6607` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6608` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6609` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6610` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6611` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6612` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6613` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6614` | `mcq` | true | `A` | `A. Legal fiction` |
| baseline | `mmlu_6615` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6616` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6617` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6618` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6619` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6620` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6621` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6622` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6623` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6624` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6625` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6626` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6627` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6628` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6629` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6630` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6631` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6632` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6633` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6634` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6635` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6636` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6637` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6638` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6639` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6640` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6641` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6642` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6643` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6644` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6645` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6646` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6647` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6648` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6649` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6650` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6651` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6652` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6653` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6654` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6655` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6656` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6657` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6658` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6659` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6660` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6661` | `mcq` | true | `B` | `B. Extent of responsibility multiplied by actual harm done.` |
| baseline | `mmlu_6662` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6663` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6664` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6665` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6666` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6667` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6668` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6669` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6670` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6671` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6672` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6674` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6675` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6676` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6677` | `mcq` | true | `D` | `D. division` |
| baseline | `mmlu_6678` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6679` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6680` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6681` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6682` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6683` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6684` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6685` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6686` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6687` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6688` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6689` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6690` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6691` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6692` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6693` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6694` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6695` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6696` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6697` | `mcq` | true | `D` | `D. Begging the question` |
| baseline | `mmlu_6698` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6699` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6700` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6701` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6702` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6703` | `mcq` | true | `D` | `D. False dichotomy` |
| baseline | `mmlu_6704` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6705` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6706` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6707` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6708` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6709` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6710` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6712` | `mcq` | true | `D` | `D. Hasty Generalization` |
| baseline | `mmlu_6713` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6714` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6715` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6716` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6717` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6718` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6719` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6721` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6722` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6723` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6724` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6725` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6726` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6728` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6729` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6730` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6731` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6733` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6734` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6735` | `mcq` | true | `C` | `C. Hypostatization` |
| baseline | `mmlu_6736` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6737` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6738` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6739` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6740` | `mcq` | true | `D` | `D. Style over substance` |
| baseline | `mmlu_6741` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6742` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6743` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6744` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6745` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6746` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6747` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6748` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6749` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6750` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6751` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6752` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6753` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6754` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6755` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6756` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6758` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6759` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6760` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6761` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6762` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6763` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6764` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6765` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6766` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6767` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6768` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6769` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6770` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6771` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6772` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6773` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6775` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6776` | `mcq` | true | `C` | `C. Reprehensible personality` |
| baseline | `mmlu_6777` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6778` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6779` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6780` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6781` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6782` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6783` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6784` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6785` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6786` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6787` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6788` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6789` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6790` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6791` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6792` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6793` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6794` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6795` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6796` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6797` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6798` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6799` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6800` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6801` | `mcq` | true | `D` | `D. Imperfect analogy` |
| baseline | `mmlu_6802` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6803` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6804` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6805` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6806` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6809` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6810` | `mcq` | true | `D` | `D. Argument from Ignorance` |
| baseline | `mmlu_6811` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6812` | `mcq` | true | `D` | `D. Equivocation` |
| baseline | `mmlu_6813` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6814` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6815` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6816` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6817` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6818` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6819` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6820` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6821` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6822` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6823` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6824` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6825` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6826` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6827` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6828` | `mcq` | false | `C` | `D. suppressed evidence` |
| baseline | `mmlu_6829` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6830` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6831` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6832` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6833` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6834` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6835` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6836` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6837` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6838` | `mcq` | true | `D` | `D. 72` |
| baseline | `mmlu_6839` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6840` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6841` | `mcq` | true | `A` | `A. O(D)` |
| baseline | `mmlu_6842` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6843` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_6844` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6845` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6846` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6847` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6848` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6849` | `mcq` | true | `B` | `B. not pure` |
| baseline | `mmlu_6850` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6851` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6852` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6853` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6854` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6855` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6856` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6857` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6858` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6859` | `mcq` | true | `B` | `B. Density-based clustering` |
| baseline | `mmlu_6860` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6861` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6862` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6863` | `mcq` | true | `D` | `D. Decrease variance` |
| baseline | `mmlu_6864` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6865` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6866` | `mcq` | false | `C` | `A. 0.0368` |
| baseline | `mmlu_6867` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6868` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6869` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6870` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6871` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6872` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6873` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6874` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6875` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6876` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6877` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6878` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6879` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6880` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6881` | `mcq` | false | `D` | `C. 7` |
| baseline | `mmlu_6882` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6883` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6884` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6885` | `mcq` | true | `B` | `B. O(N)` |
| baseline | `mmlu_6886` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6887` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6888` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6889` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6890` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6891` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6892` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6893` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6894` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6895` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6896` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6897` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6898` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6899` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6900` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6901` | `mcq` | true | `C` | `C. 0.635` |
| baseline | `mmlu_6902` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6903` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6904` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6905` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6906` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6907` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6908` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6909` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6910` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6911` | `mcq` | true | `C` | `C. The kernel width` |
| baseline | `mmlu_6912` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6913` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6914` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6915` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6916` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6918` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6919` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6920` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6921` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6922` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6923` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6924` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6925` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6926` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6927` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6928` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6929` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6930` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6931` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6932` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6933` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6934` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6935` | `mcq` | false | `B` | `D. All of above` |
| baseline | `mmlu_6936` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6937` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6938` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6939` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6940` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6941` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6942` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6943` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6944` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6945` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6946` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6947` | `mcq` | true | `B` | `B. Satisficing` |
| baseline | `mmlu_6948` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6949` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6950` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6951` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6952` | `mcq` | true | `B` | `B. Work schedule design` |
| baseline | `mmlu_6953` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6954` | `mcq` | true | `D` | `D. Legitimate` |
| baseline | `mmlu_6955` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6956` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6957` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6958` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6959` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6960` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6961` | `mcq` | false | `A` | `D. High level of certainty regarding the environment` |
| baseline | `mmlu_6962` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6963` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6964` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6965` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6966` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6967` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6968` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6969` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6970` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6971` | `mcq` | true | `D` | `D. Economic reward` |
| baseline | `mmlu_6972` | `mcq` | true | `D` | `D. Price-fixing` |
| baseline | `mmlu_6973` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6974` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6975` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6976` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6977` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6978` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6979` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6980` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6981` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6982` | `mcq` | true | `B` | `B. Face-to-face` |
| baseline | `mmlu_6983` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6984` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6985` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6986` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6987` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6988` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6989` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6990` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6991` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6992` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6993` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6994` | `mcq` | true | `D` | `D. Fred Fiedler` |
| baseline | `mmlu_6995` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6996` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6997` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6998` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6999` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7000` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7001` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7002` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7003` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7004` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7005` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7006` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7007` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7008` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7009` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7010` | `mcq` | true | `B` | `B. Market penetration` |
| baseline | `mmlu_7011` | `mcq` | true | `D` | `D. remotely` |
| baseline | `mmlu_7012` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7013` | `mcq` | true | `B` | `B. Mission statement` |
| baseline | `mmlu_7014` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7015` | `mcq` | true | `B` | `B. Time and motion studies` |
| baseline | `mmlu_7016` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7017` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7018` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7019` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7020` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7021` | `mcq` | true | `B` | `B. Top to bottom` |
| baseline | `mmlu_7022` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7023` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7024` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7025` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7026` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7027` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7028` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7029` | `mcq` | true | `A` | `A. Long-term` |
| baseline | `mmlu_7030` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7031` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7032` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7033` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7034` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7035` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7036` | `mcq` | true | `D` | `D. Productivity` |
| baseline | `mmlu_7037` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7038` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7039` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7040` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7041` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7042` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7043` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7044` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7045` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7046` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7047` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7048` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7049` | `mcq` | true | `D` | `D. Company` |
| baseline | `mmlu_7050` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7051` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7052` | `mcq` | false | `C` | `D. After the end of the Second World War.` |
| baseline | `mmlu_7053` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7054` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7055` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7056` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7057` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7058` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7059` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7060` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7061` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7062` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7063` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7064` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7065` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7066` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7067` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7068` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7069` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7070` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7071` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7072` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7073` | `mcq` | true | `B` | `B. Public relations.` |
| baseline | `mmlu_7074` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7075` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7076` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7077` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7078` | `mcq` | true | `B` | `B. Early adopter.` |
| baseline | `mmlu_7079` | `mcq` | true | `A` | `A. Direct` |
| baseline | `mmlu_7080` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7081` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7082` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7083` | `mcq` | true | `D` | `D. Brand imagery.` |
| baseline | `mmlu_7084` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7085` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7086` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7087` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7088` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7089` | `mcq` | true | `B` | `B. cold canvassing` |
| baseline | `mmlu_7090` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7091` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7092` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7093` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7094` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7095` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7096` | `mcq` | true | `C` | `C. Relationship marketing.` |
| baseline | `mmlu_7097` | `mcq` | true | `C` | `C. Value.` |
| baseline | `mmlu_7098` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7099` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7100` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7101` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7102` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7103` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7104` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7105` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7106` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7107` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7108` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7109` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7110` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7111` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7112` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7113` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7114` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7115` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7116` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7117` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7118` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7119` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7120` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7121` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7122` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7123` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7124` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7125` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7126` | `mcq` | true | `C` | `C. Spam.` |
| baseline | `mmlu_7127` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7128` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7129` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7130` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7131` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7132` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7133` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7134` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7135` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7136` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7137` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7138` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7139` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7140` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7141` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7142` | `mcq` | true | `A` | `A. Purchase context.` |
| baseline | `mmlu_7143` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7144` | `mcq` | true | `D` | `D. Public relations` |
| baseline | `mmlu_7145` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7146` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7147` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7148` | `mcq` | true | `B` | `B. Legal environment.` |
| baseline | `mmlu_7149` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7150` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7151` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7152` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7153` | `mcq` | true | `C` | `C. $6,860` |
| baseline | `mmlu_7154` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7155` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7156` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7157` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7158` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7159` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7160` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7161` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7163` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7164` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7165` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7166` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7167` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7168` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7169` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7170` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7171` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7172` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7173` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7174` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7175` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7176` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7177` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7178` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7179` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7180` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7181` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7182` | `mcq` | true | `D` | `D. Promotion.` |
| baseline | `mmlu_7183` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7184` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7185` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7186` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7187` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7188` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7189` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7190` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7191` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7192` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7193` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7194` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7195` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7196` | `mcq` | true | `D` | `D. Service encounters.` |
| baseline | `mmlu_7197` | `mcq` | true | `B` | `B. Place utility.` |
| baseline | `mmlu_7198` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7199` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7200` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7201` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7202` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7203` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7204` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7205` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7206` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7208` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7209` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7210` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7211` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7212` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7213` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7214` | `mcq` | true | `C` | `C. Reliability.` |
| baseline | `mmlu_7215` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7216` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7217` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7218` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7219` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7220` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7221` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7222` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7223` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7224` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7225` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7226` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7227` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7228` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7229` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7230` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7231` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7232` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7233` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7234` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7235` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7236` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7237` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7238` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7239` | `mcq` | true | `B` | `B. Intensive distribution.` |
| baseline | `mmlu_7240` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7241` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7242` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7243` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7244` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7245` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7246` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7247` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7248` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7249` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7250` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7251` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7252` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7253` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7254` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7255` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7256` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7257` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7258` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7259` | `mcq` | true | `C` | `C. Physiological needs.` |
| baseline | `mmlu_7260` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7261` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7262` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7263` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7264` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7265` | `mcq` | true | `D` | `D. Feedback.` |
| baseline | `mmlu_7266` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7267` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7268` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7269` | `mcq` | true | `A` | `A. Reduced perceived risk.` |
| baseline | `mmlu_7270` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7271` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7272` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7273` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7274` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7275` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7276` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7277` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7278` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7279` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7281` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7282` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7283` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7284` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7285` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7286` | `mcq` | false | `A` | `B. 0.001` |
| baseline | `mmlu_7287` | `mcq` | true | `C` | `C. thymine.` |
| baseline | `mmlu_7288` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7289` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7290` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7291` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7292` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7293` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7294` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7295` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7296` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7298` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7299` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7300` | `mcq` | true | `A` | `A. 1.0/64` |
| baseline | `mmlu_7301` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7302` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7303` | `mcq` | true | `D` | `D. APOE` |
| baseline | `mmlu_7304` | `mcq` | false | `D` | `B. 7` |
| baseline | `mmlu_7305` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7306` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7307` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7308` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7309` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7310` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7311` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7312` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7313` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7314` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7315` | `mcq` | false | `C` | `D. 0.32` |
| baseline | `mmlu_7316` | `mcq` | false | `D` | `B. HMG-CoA reductase` |
| baseline | `mmlu_7317` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7318` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7319` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7320` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7321` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7322` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7323` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7324` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7325` | `mcq` | false | `C` | `A. 1 in 1000` |
| baseline | `mmlu_7326` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7328` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7329` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7330` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7331` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7332` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7333` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7334` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7335` | `mcq` | false | `C` | `A. about 2` |
| baseline | `mmlu_7336` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7337` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7338` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7339` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7340` | `mcq` | true | `B` | `B. Prophase I.` |
| baseline | `mmlu_7341` | `mcq` | true | `D` | `D. mitochondrial DNA.` |
| baseline | `mmlu_7342` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7343` | `mcq` | false | `B` | `D. 46 pairs` |
| baseline | `mmlu_7344` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7345` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7346` | `mcq` | false | `C` | `D. 0.02` |
| baseline | `mmlu_7347` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7348` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7349` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7350` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7351` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7352` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7353` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7354` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7355` | `mcq` | true | `D` | `D. Succinylcholine` |
| baseline | `mmlu_7356` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7357` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7358` | `mcq` | false | `B` | `A/B/C/D` |
| baseline | `mmlu_7359` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7360` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7361` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7362` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7363` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7364` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7365` | `mcq` | true | `D` | `D. Zellweger syndrome` |
| baseline | `mmlu_7366` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7367` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7368` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7369` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7370` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7371` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7372` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7373` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7374` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7375` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7376` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7378` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7379` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7380` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7381` | `mcq` | false | `D` | `B. less than 1%` |
| baseline | `mmlu_7382` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7383` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7384` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7385` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7386` | `mcq` | true | `D` | `D. 451 degrees` |
| baseline | `mmlu_7387` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7388` | `mcq` | true | `B` | `B. Meriwether and William` |
| baseline | `mmlu_7389` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7390` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7391` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7392` | `mcq` | true | `A` | `A. sophomore` |
| baseline | `mmlu_7393` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7394` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7395` | `mcq` | false | `B` | `D. Dwight Eisenhower` |
| baseline | `mmlu_7396` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7397` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7398` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7399` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7400` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7401` | `mcq` | false | `A` | `D. monkey` |
| baseline | `mmlu_7402` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7403` | `mcq` | true | `A` | `A. Ireland` |
| baseline | `mmlu_7404` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7405` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7406` | `mcq` | false | `C` | `D. ace` |
| baseline | `mmlu_7407` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7408` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7409` | `mcq` | false | `C` | `A. Miss Jackie` |
| baseline | `mmlu_7410` | `mcq` | true | `C` | `C. bird` |
| baseline | `mmlu_7411` | `mcq` | true | `C` | `C. Stomach` |
| baseline | `mmlu_7412` | `mcq` | false | `D` | `C. Red` |
| baseline | `mmlu_7413` | `mcq` | true | `A` | `A. 0 degrees or below` |
| baseline | `mmlu_7414` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7415` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7416` | `mcq` | true | `C` | `C. Radon` |
| baseline | `mmlu_7417` | `mcq` | false | `D` | `C. 3 mol` |
| baseline | `mmlu_7418` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7419` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7420` | `mcq` | true | `C` | `C. Carpals` |
| baseline | `mmlu_7421` | `mcq` | true | `D` | `D. calf` |
| baseline | `mmlu_7422` | `mcq` | true | `B` | `B. Fendi` |
| baseline | `mmlu_7423` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7424` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7425` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7426` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7427` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7428` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7429` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7430` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7431` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7432` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7433` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7434` | `mcq` | true | `B` | `B. work without pay` |
| baseline | `mmlu_7435` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7436` | `mcq` | true | `C` | `C. Sanskrit` |
| baseline | `mmlu_7437` | `mcq` | true | `C` | `C. right` |
| baseline | `mmlu_7438` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7439` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7440` | `mcq` | true | `C` | `C. Judy` |
| baseline | `mmlu_7441` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7442` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7443` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7444` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7445` | `mcq` | false | `C` | `D. Law` |
| baseline | `mmlu_7446` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7447` | `mcq` | true | `D` | `D. Foreshortening` |
| baseline | `mmlu_7448` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7449` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7450` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7451` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7452` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7453` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7454` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7455` | `mcq` | true | `C` | `C. 10` |
| baseline | `mmlu_7456` | `mcq` | true | `B` | `B. Triangle` |
| baseline | `mmlu_7457` | `mcq` | true | `B` | `B. knife` |
| baseline | `mmlu_7458` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7459` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7460` | `mcq` | false | `B` | `D. theta` |
| baseline | `mmlu_7461` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7462` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7463` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7464` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7465` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7466` | `mcq` | true | `C` | `C. orange` |
| baseline | `mmlu_7467` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7468` | `mcq` | true | `C` | `C. Impasto` |
| baseline | `mmlu_7469` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7470` | `mcq` | true | `C` | `C. Japan` |
| baseline | `mmlu_7471` | `mcq` | true | `D` | `D. rice` |
| baseline | `mmlu_7472` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7473` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7474` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7475` | `mcq` | true | `D` | `D. Sherwood Forest` |
| baseline | `mmlu_7476` | `mcq` | true | `B` | `B. four` |
| baseline | `mmlu_7477` | `mcq` | true | `D` | `D. Guatemala` |
| baseline | `mmlu_7478` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7479` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7480` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7481` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7482` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7483` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7484` | `mcq` | true | `D` | `D. jaguar` |
| baseline | `mmlu_7485` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7486` | `mcq` | true | `B` | `B. Mercury(II) oxide` |
| baseline | `mmlu_7487` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7488` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7489` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7490` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_7491` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7492` | `mcq` | true | `B` | `B. Martin Luther` |
| baseline | `mmlu_7493` | `mcq` | true | `D` | `D. mercury` |
| baseline | `mmlu_7494` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7495` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7496` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7497` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7498` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7499` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7500` | `mcq` | false | `C` | `A. brown` |
| baseline | `mmlu_7501` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7502` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7503` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7504` | `mcq` | true | `A` | `A. Japan` |
| baseline | `mmlu_7505` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7506` | `mcq` | true | `B` | `B. Ireland` |
| baseline | `mmlu_7507` | `mcq` | true | `B` | `B. Ivory` |
| baseline | `mmlu_7508` | `mcq` | true | `C` | `C. Liverpool` |
| baseline | `mmlu_7509` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7510` | `mcq` | true | `B` | `B. 100` |
| baseline | `mmlu_7511` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7512` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7513` | `mcq` | true | `D` | `D. North Pole` |
| baseline | `mmlu_7514` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7515` | `mcq` | true | `C` | `C. 50` |
| baseline | `mmlu_7516` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7517` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7518` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7519` | `mcq` | true | `B` | `B. $200,000,000` |
| baseline | `mmlu_7520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7521` | `mcq` | false | `C` | `B. 2,000,000,000` |
| baseline | `mmlu_7522` | `mcq` | false | `A` | `D. caramel` |
| baseline | `mmlu_7523` | `mcq` | true | `C` | `C. red` |
| baseline | `mmlu_7524` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7525` | `mcq` | false | `C` | `B. 2` |
| baseline | `mmlu_7526` | `mcq` | false | `B` | `A. Joey` |
| baseline | `mmlu_7527` | `mcq` | false | `B` | `A. regressive` |
| baseline | `mmlu_7528` | `mcq` | true | `D` | `D. institutionalism` |
| baseline | `mmlu_7529` | `mcq` | true | `D` | `D. big toe` |
| baseline | `mmlu_7530` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7531` | `mcq` | true | `C` | `C. hemophilia` |
| baseline | `mmlu_7532` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7533` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7534` | `mcq` | true | `D` | `D. Chicken pox` |
| baseline | `mmlu_7535` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7536` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7537` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7538` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7539` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7540` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7541` | `mcq` | true | `B` | `B. St Louis` |
| baseline | `mmlu_7542` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7543` | `mcq` | true | `B` | `B. the Gold Glove` |
| baseline | `mmlu_7544` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7545` | `mcq` | true | `D` | `D. Richard Nixon` |
| baseline | `mmlu_7546` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7547` | `mcq` | false | `B` | `A. 1 seconds` |
| baseline | `mmlu_7548` | `mcq` | true | `D` | `D. the working class` |
| baseline | `mmlu_7549` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7550` | `mcq` | false | `C` | `D. major general` |
| baseline | `mmlu_7551` | `mcq` | true | `A` | `A. 6'` |
| baseline | `mmlu_7552` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7553` | `mcq` | true | `A` | `A. China` |
| baseline | `mmlu_7554` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7555` | `mcq` | true | `C` | `C. nine` |
| baseline | `mmlu_7556` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7557` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7558` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7559` | `mcq` | true | `A` | `A. crazy` |
| baseline | `mmlu_7560` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7561` | `mcq` | true | `C` | `C. Tempo` |
| baseline | `mmlu_7562` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7563` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7564` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7565` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7566` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7567` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7568` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7569` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7570` | `mcq` | true | `C` | `C. Hemlock` |
| baseline | `mmlu_7571` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7572` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7573` | `mcq` | true | `D` | `D. Pinch hitter` |
| baseline | `mmlu_7574` | `mcq` | true | `C` | `C. Argentina` |
| baseline | `mmlu_7575` | `mcq` | true | `C` | `C. 81` |
| baseline | `mmlu_7576` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7577` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7578` | `mcq` | false | `D` | `A. The instructional objectives` |
| baseline | `mmlu_7579` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7580` | `mcq` | true | `D` | `D. Israel` |
| baseline | `mmlu_7581` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7582` | `mcq` | true | `C` | `C. birds` |
| baseline | `mmlu_7583` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7584` | `mcq` | true | `D` | `D. Hyundai` |
| baseline | `mmlu_7585` | `mcq` | true | `C` | `C. Acceleration` |
| baseline | `mmlu_7586` | `mcq` | true | `A` | `A. Weaving` |
| baseline | `mmlu_7587` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7588` | `mcq` | true | `B` | `B. ichthyologist` |
| baseline | `mmlu_7589` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7590` | `mcq` | false | `A` | `C. ten inches` |
| baseline | `mmlu_7591` | `mcq` | false | `B` | `D. 0` |
| baseline | `mmlu_7592` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7593` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7594` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7595` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7596` | `mcq` | true | `B` | `B. Links` |
| baseline | `mmlu_7597` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7598` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7599` | `mcq` | false | `C` | `B. four years` |
| baseline | `mmlu_7600` | `mcq` | true | `A` | `A. head` |
| baseline | `mmlu_7601` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7602` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7603` | `mcq` | true | `C` | `C. Rhea` |
| baseline | `mmlu_7604` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7605` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7606` | `mcq` | true | `B` | `B. Chloroplast` |
| baseline | `mmlu_7607` | `mcq` | false | `D` | `A. Dallas` |
| baseline | `mmlu_7608` | `mcq` | true | `C` | `C. Homer` |
| baseline | `mmlu_7609` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7610` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7611` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7612` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7613` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7614` | `mcq` | true | `D` | `D. San Antonio Spurs` |
| baseline | `mmlu_7615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7616` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7617` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7618` | `mcq` | true | `B` | `B. Portfolio assessment` |
| baseline | `mmlu_7619` | `mcq` | true | `B` | `B. through a human body` |
| baseline | `mmlu_7620` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7621` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7622` | `mcq` | false | `B` | `A. shrimp` |
| baseline | `mmlu_7623` | `mcq` | true | `A` | `A. black` |
| baseline | `mmlu_7624` | `mcq` | true | `C` | `C. IRA` |
| baseline | `mmlu_7625` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7626` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7627` | `mcq` | false | `C` | `A. yellow` |
| baseline | `mmlu_7628` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7629` | `mcq` | true | `A` | `A. 1600` |
| baseline | `mmlu_7630` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7631` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7632` | `mcq` | true | `D` | `D. Bobby Riggs` |
| baseline | `mmlu_7633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7634` | `mcq` | false | `A` | `D. Dick Dastardly` |
| baseline | `mmlu_7635` | `mcq` | true | `C` | `C. goat` |
| baseline | `mmlu_7636` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7637` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7638` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7639` | `mcq` | true | `B` | `B. Caricature` |
| baseline | `mmlu_7640` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7641` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7642` | `mcq` | true | `D` | `D. Personification` |
| baseline | `mmlu_7643` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7644` | `mcq` | true | `C` | `C. chocolate` |
| baseline | `mmlu_7645` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7646` | `mcq` | true | `B` | `B. India` |
| baseline | `mmlu_7647` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7648` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7649` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7650` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7651` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7652` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7653` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7654` | `mcq` | true | `A` | `A. Chicken Little` |
| baseline | `mmlu_7655` | `mcq` | false | `A` | `B. kazoo` |
| baseline | `mmlu_7656` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7657` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7658` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7659` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7660` | `mcq` | false | `D` | `A. The man pays` |
| baseline | `mmlu_7661` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7662` | `mcq` | true | `A` | `A. Notre Dame` |
| baseline | `mmlu_7663` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7664` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7665` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7666` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7667` | `mcq` | true | `A` | `A. Paris` |
| baseline | `mmlu_7668` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7669` | `mcq` | true | `B` | `B. Primary` |
| baseline | `mmlu_7670` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7671` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7672` | `mcq` | true | `D` | `D. thousand` |
| baseline | `mmlu_7673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7674` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7675` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7676` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7677` | `mcq` | false | `A` | `C. 7:00 AM` |
| baseline | `mmlu_7678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7679` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7680` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7681` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7682` | `mcq` | true | `B` | `B. meat` |
| baseline | `mmlu_7683` | `mcq` | false | `B` | `C. 18` |
| baseline | `mmlu_7684` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7685` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7686` | `mcq` | true | `A` | `A. 2` |
| baseline | `mmlu_7687` | `mcq` | true | `D` | `D. France` |
| baseline | `mmlu_7688` | `mcq` | true | `B` | `B. seven` |
| baseline | `mmlu_7689` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7690` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7691` | `mcq` | true | `A` | `A. Bismarck` |
| baseline | `mmlu_7692` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7693` | `mcq` | false | `C` | `A. I only` |
| baseline | `mmlu_7694` | `mcq` | false | `A` | `B. 4*10^12 kg` |
| baseline | `mmlu_7695` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7696` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7697` | `mcq` | true | `B` | `B. in reverse` |
| baseline | `mmlu_7698` | `mcq` | true | `A` | `A. iris` |
| baseline | `mmlu_7699` | `mcq` | true | `B` | `B. film production` |
| baseline | `mmlu_7700` | `mcq` | true | `B` | `B. Louis XIV` |
| baseline | `mmlu_7701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7702` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7703` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7704` | `mcq` | true | `C` | `C. 88` |
| baseline | `mmlu_7705` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7706` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7707` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7708` | `mcq` | true | `B` | `B. nearsighted` |
| baseline | `mmlu_7709` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7710` | `mcq` | true | `C` | `C. Captain Kangaroo` |
| baseline | `mmlu_7711` | `mcq` | true | `B` | `B. courtroom` |
| baseline | `mmlu_7712` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7713` | `mcq` | false | `A` | `B. Yanni` |
| baseline | `mmlu_7714` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7715` | `mcq` | false | `B` | `D. 320,000` |
| baseline | `mmlu_7716` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7717` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7718` | `mcq` | true | `B` | `B. Cronus` |
| baseline | `mmlu_7719` | `mcq` | true | `A` | `A. cancer` |
| baseline | `mmlu_7720` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7721` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7722` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7723` | `mcq` | true | `B` | `B. HTTP` |
| baseline | `mmlu_7724` | `mcq` | true | `B` | `B. Albuquerque` |
| baseline | `mmlu_7725` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7726` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7728` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7729` | `mcq` | true | `C` | `C. 19th` |
| baseline | `mmlu_7730` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7731` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7733` | `mcq` | true | `B` | `B. Bloat` |
| baseline | `mmlu_7734` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7735` | `mcq` | true | `A` | `A. gaggle` |
| baseline | `mmlu_7736` | `mcq` | true | `C` | `C. directory assistance` |
| baseline | `mmlu_7737` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7738` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7739` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7740` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7741` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7742` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7743` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7744` | `mcq` | false | `B` | `D. four` |
| baseline | `mmlu_7745` | `mcq` | false | `B` | `D. The Iron Sheik` |
| baseline | `mmlu_7746` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7747` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7748` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7749` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7750` | `mcq` | true | `C` | `C. tangelo` |
| baseline | `mmlu_7751` | `mcq` | true | `B` | `B. Tom and Dick` |
| baseline | `mmlu_7752` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7753` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7754` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7755` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7756` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7757` | `mcq` | false | `C` | `B. Air Force` |
| baseline | `mmlu_7758` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7759` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7760` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7761` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7762` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7763` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7764` | `mcq` | true | `B` | `B. the stockholders` |
| baseline | `mmlu_7765` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7766` | `mcq` | false | `C` | `D. New York City` |
| baseline | `mmlu_7767` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7768` | `mcq` | true | `D` | `D. Sensation'` |
| baseline | `mmlu_7769` | `mcq` | true | `D` | `D. Fidelio` |
| baseline | `mmlu_7770` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7771` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7772` | `mcq` | true | `D` | `D. quickly` |
| baseline | `mmlu_7773` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7774` | `mcq` | true | `B` | `B. thistle` |
| baseline | `mmlu_7775` | `mcq` | true | `C` | `C. $1 billion` |
| baseline | `mmlu_7776` | `mcq` | true | `D` | `D. Yogi Bear` |
| baseline | `mmlu_7777` | `mcq` | true | `D` | `D. Nyctophobia` |
| baseline | `mmlu_7778` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7779` | `mcq` | true | `B` | `B. Japan` |
| baseline | `mmlu_7780` | `mcq` | true | `B` | `B. Asia` |
| baseline | `mmlu_7781` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7782` | `mcq` | true | `A` | `A. whooping cough` |
| baseline | `mmlu_7783` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7784` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7785` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7786` | `mcq` | true | `B` | `B. the home team` |
| baseline | `mmlu_7787` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7788` | `mcq` | true | `A` | `A. 11` |
| baseline | `mmlu_7789` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7790` | `mcq` | false | `C` | `A. Pluto` |
| baseline | `mmlu_7791` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7792` | `mcq` | true | `B` | `B. German` |
| baseline | `mmlu_7793` | `mcq` | true | `D` | `D. meat` |
| baseline | `mmlu_7794` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7795` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7796` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7797` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7798` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7799` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7800` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7801` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7802` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7803` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7804` | `mcq` | true | `C` | `C. 4.5 billion years` |
| baseline | `mmlu_7805` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7806` | `mcq` | true | `A` | `A. grenadine` |
| baseline | `mmlu_7807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7809` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7810` | `mcq` | true | `A` | `A. declaring bankruptcy` |
| baseline | `mmlu_7811` | `mcq` | true | `C` | `C. ten thousand` |
| baseline | `mmlu_7812` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7813` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7814` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7815` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7816` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7817` | `mcq` | true | `B` | `B. Cow` |
| baseline | `mmlu_7818` | `mcq` | true | `A` | `A. file transfer protocol` |
| baseline | `mmlu_7819` | `mcq` | true | `A` | `A. calligraphy` |
| baseline | `mmlu_7820` | `mcq` | true | `D` | `D. the Trinity` |
| baseline | `mmlu_7821` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7822` | `mcq` | true | `A` | `A. heredity` |
| baseline | `mmlu_7823` | `mcq` | true | `B` | `B. Silicon` |
| baseline | `mmlu_7824` | `mcq` | true | `B` | `B. Stephen King` |
| baseline | `mmlu_7825` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7827` | `mcq` | true | `D` | `D. Beethoven` |
| baseline | `mmlu_7828` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7829` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7830` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7831` | `mcq` | true | `A` | `A. Gulf of Sidra` |
| baseline | `mmlu_7832` | `mcq` | true | `D` | `D. Old Sparky` |
| baseline | `mmlu_7833` | `mcq` | true | `D` | `D. Spanish` |
| baseline | `mmlu_7834` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7835` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7836` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7837` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7838` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7839` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7840` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7841` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7842` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7843` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7844` | `mcq` | true | `B` | `B. Luigi` |
| baseline | `mmlu_7845` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7846` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7847` | `mcq` | true | `D` | `D. melting` |
| baseline | `mmlu_7848` | `mcq` | true | `A` | `A. California` |
| baseline | `mmlu_7849` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7850` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7851` | `mcq` | true | `A` | `A. Two` |
| baseline | `mmlu_7852` | `mcq` | false | `B` | `D. really big` |
| baseline | `mmlu_7853` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7855` | `mcq` | true | `C` | `C. 0.75` |
| baseline | `mmlu_7856` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7857` | `mcq` | true | `B` | `B. indicate the depth of certain readers' feelings about science fiction` |
| baseline | `mmlu_7858` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7859` | `mcq` | true | `B` | `B. 74 m.p.h.` |
| baseline | `mmlu_7860` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7861` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7862` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7863` | `mcq` | true | `A` | `A. stop` |
| baseline | `mmlu_7864` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7865` | `mcq` | true | `C` | `C. Water` |
| baseline | `mmlu_7866` | `mcq` | true | `A` | `A. France` |
| baseline | `mmlu_7867` | `mcq` | false | `C` | `B. sperm whale` |
| baseline | `mmlu_7868` | `mcq` | true | `C` | `C. dog` |
| baseline | `mmlu_7869` | `mcq` | false | `B` | `C. green` |
| baseline | `mmlu_7870` | `mcq` | true | `C` | `C. eye` |
| baseline | `mmlu_7871` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7872` | `mcq` | false | `D` | `B. two` |
| baseline | `mmlu_7873` | `mcq` | true | `A` | `A. Nomadic` |
| baseline | `mmlu_7874` | `mcq` | true | `D` | `D. Dutch` |
| baseline | `mmlu_7875` | `mcq` | true | `D` | `D. shellfish` |
| baseline | `mmlu_7876` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7877` | `mcq` | true | `C` | `C. hygrometer` |
| baseline | `mmlu_7878` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7879` | `mcq` | false | `B` | `C. Lancelot` |
| baseline | `mmlu_7880` | `mcq` | true | `D` | `D. Read-Only Memory` |
| baseline | `mmlu_7881` | `mcq` | false | `C` | `D. 21` |
| baseline | `mmlu_7882` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7883` | `mcq` | false | `A` | `C. 2000` |
| baseline | `mmlu_7884` | `mcq` | true | `B` | `B. euclidean` |
| baseline | `mmlu_7885` | `mcq` | false | `D` | `B. Marginal cost` |
| baseline | `mmlu_7886` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7887` | `mcq` | true | `B` | `B. Wellington` |
| baseline | `mmlu_7888` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7889` | `mcq` | false | `C` | `B. May` |
| baseline | `mmlu_7890` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7891` | `mcq` | true | `D` | `D. palette` |
| baseline | `mmlu_7892` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7893` | `mcq` | true | `D` | `D. silver` |
| baseline | `mmlu_7894` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7895` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7896` | `mcq` | true | `A` | `A. pig` |
| baseline | `mmlu_7897` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7898` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7899` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7900` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7901` | `mcq` | true | `B` | `B. Pennsylvania` |
| baseline | `mmlu_7902` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7903` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7904` | `mcq` | false | `C` | `B. 8*10^23` |
| baseline | `mmlu_7905` | `mcq` | true | `A` | `A. Richard Rodgers` |
| baseline | `mmlu_7906` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7907` | `mcq` | true | `C` | `C. Cinco de Mayo` |
| baseline | `mmlu_7908` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7909` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7910` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7911` | `mcq` | true | `D` | `D. Paul Allen` |
| baseline | `mmlu_7912` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7913` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7914` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7915` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7916` | `mcq` | false | `A` | `D. syphilis` |
| baseline | `mmlu_7917` | `mcq` | true | `C` | `C. Uranium` |
| baseline | `mmlu_7918` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7919` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7920` | `mcq` | true | `A` | `A. Wood` |
| baseline | `mmlu_7921` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7922` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7923` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7924` | `mcq` | true | `B` | `B. America Online` |
| baseline | `mmlu_7925` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7926` | `mcq` | false | `C` | `B. Thailand` |
| baseline | `mmlu_7927` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7928` | `mcq` | true | `C` | `C. five` |
| baseline | `mmlu_7929` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7930` | `mcq` | true | `A` | `A. pink` |
| baseline | `mmlu_7931` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7932` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7933` | `mcq` | true | `C` | `C. Sioux` |
| baseline | `mmlu_7934` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7935` | `mcq` | true | `C` | `C. Price` |
| baseline | `mmlu_7936` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7937` | `mcq` | false | `C` | `D. Super Bowl` |
| baseline | `mmlu_7938` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7939` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7940` | `mcq` | true | `B` | `B. kangaroo` |
| baseline | `mmlu_7941` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7942` | `mcq` | true | `C` | `C. Bones` |
| baseline | `mmlu_7943` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7944` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7945` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7946` | `mcq` | true | `D` | `D. .exe` |
| baseline | `mmlu_7947` | `mcq` | true | `C` | `C. anagram` |
| baseline | `mmlu_7948` | `mcq` | true | `B` | `B. mitosis` |
| baseline | `mmlu_7949` | `mcq` | true | `B` | `B. rabies` |
| baseline | `mmlu_7950` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7951` | `mcq` | false | `D` | `B. laundry` |
| baseline | `mmlu_7952` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7953` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7954` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7955` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7956` | `mcq` | true | `B` | `B. China` |
| baseline | `mmlu_7957` | `mcq` | true | `D` | `D. IKEA` |
| baseline | `mmlu_7958` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7959` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7960` | `mcq` | true | `C` | `C. England` |
| baseline | `mmlu_7961` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7962` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7963` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7964` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7965` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7966` | `mcq` | true | `A` | `A. Spanish` |
| baseline | `mmlu_7967` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7968` | `mcq` | true | `B` | `B. oil` |
| baseline | `mmlu_7969` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7970` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7971` | `mcq` | false | `C` | `B. Two` |
| baseline | `mmlu_7972` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7973` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7974` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7975` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7976` | `mcq` | false | `C` | `A. Order of business` |
| baseline | `mmlu_7977` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7978` | `mcq` | true | `C` | `C. 16` |
| baseline | `mmlu_7979` | `mcq` | true | `C` | `C. deficient` |
| baseline | `mmlu_7980` | `mcq` | true | `B` | `B. garnet` |
| baseline | `mmlu_7981` | `mcq` | false | `B` | `D. He kills himself` |
| baseline | `mmlu_7982` | `mcq` | false | `B` | `A. United States` |
| baseline | `mmlu_7983` | `mcq` | false | `B` | `A. Monday's child` |
| baseline | `mmlu_7984` | `mcq` | true | `B` | `B. a truck` |
| baseline | `mmlu_7985` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7986` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7987` | `mcq` | false | `A` | `B. 10^-29 %` |
| baseline | `mmlu_7988` | `mcq` | true | `D` | `D. San Francisco` |
| baseline | `mmlu_7989` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7990` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7991` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7992` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7993` | `mcq` | true | `C` | `C. corned beef` |
| baseline | `mmlu_7994` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7995` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7996` | `mcq` | true | `A` | `A. Eros` |
| baseline | `mmlu_7997` | `mcq` | false | `B` | `D. Division` |
| baseline | `mmlu_7998` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7999` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8000` | `mcq` | true | `D` | `D. atheist` |
| baseline | `mmlu_8001` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8002` | `mcq` | true | `B` | `B. chitlins` |
| baseline | `mmlu_8003` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8004` | `mcq` | true | `D` | `D. Financial Industry Regulatory Authority` |
| baseline | `mmlu_8005` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8006` | `mcq` | true | `B` | `B. 24` |
| baseline | `mmlu_8007` | `mcq` | true | `C` | `C. copperhead` |
| baseline | `mmlu_8008` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8009` | `mcq` | true | `A` | `A. red` |
| baseline | `mmlu_8010` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8011` | `mcq` | true | `D` | `D. antihistamines` |
| baseline | `mmlu_8012` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8013` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8014` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8015` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8016` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8017` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8018` | `mcq` | true | `B` | `B. a shaker of salt` |
| baseline | `mmlu_8019` | `mcq` | true | `B` | `B. Decreasing the discount rate to member banks` |
| baseline | `mmlu_8020` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8021` | `mcq` | false | `D` | `C. purple` |
| baseline | `mmlu_8022` | `mcq` | true | `D` | `D. pumice` |
| baseline | `mmlu_8023` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8024` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8025` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8026` | `mcq` | true | `B` | `B. 33 1/3 rpm` |
| baseline | `mmlu_8027` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8028` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8029` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8030` | `mcq` | true | `C` | `C. The site might belong to a nonprofit agency.` |
| baseline | `mmlu_8031` | `mcq` | true | `B` | `B. 101` |
| baseline | `mmlu_8032` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8033` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8034` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8035` | `mcq` | true | `B` | `B. Olympus` |
| baseline | `mmlu_8036` | `mcq` | false | `B` | `A. Humpty Dumpty'` |
| baseline | `mmlu_8037` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8038` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8039` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8040` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8041` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8042` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8043` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8044` | `mcq` | true | `B` | `B. ceramic` |
| baseline | `mmlu_8045` | `mcq` | true | `C` | `C. glaucoma` |
| baseline | `mmlu_8046` | `mcq` | true | `C` | `C. scarf` |
| baseline | `mmlu_8047` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8048` | `mcq` | true | `A` | `A. Paul McCartney` |
| baseline | `mmlu_8049` | `mcq` | true | `A` | `A. Outer core` |
| baseline | `mmlu_8050` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8051` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8052` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8053` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8054` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8055` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8056` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8057` | `mcq` | true | `B` | `B. bogey` |
| baseline | `mmlu_8058` | `mcq` | false | `C` | `B. Farrah Fawcett` |
| baseline | `mmlu_8059` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8060` | `mcq` | true | `D` | `D. drag racing` |
| baseline | `mmlu_8061` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8062` | `mcq` | false | `B` | `D. Fannie Mae` |
| baseline | `mmlu_8063` | `mcq` | true | `D` | `D. Internet Service Provider` |
| baseline | `mmlu_8064` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8065` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8066` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8067` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8068` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8069` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8070` | `mcq` | true | `B` | `B. New York` |
| baseline | `mmlu_8071` | `mcq` | false | `C` | `D. silver` |
| baseline | `mmlu_8072` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8073` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8074` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8075` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8076` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8077` | `mcq` | true | `A` | `A. visa` |
| baseline | `mmlu_8078` | `mcq` | false | `A` | `B. The Earth's Moon` |
| baseline | `mmlu_8079` | `mcq` | true | `D` | `D. increased commercial contacts with Indian and Arab merchants` |
| baseline | `mmlu_8080` | `mcq` | false | `A` | `D. Lackawanna` |
| baseline | `mmlu_8081` | `mcq` | false | `A` | `C. Larrabee` |
| baseline | `mmlu_8082` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8083` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8084` | `mcq` | false | `C` | `A. About 0.1%` |
| baseline | `mmlu_8085` | `mcq` | false | `A` | `C. 16.0 grams` |
| baseline | `mmlu_8086` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8087` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8088` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8089` | `mcq` | true | `D` | `D. goalkeeper` |
| baseline | `mmlu_8090` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8091` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8092` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8093` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8094` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8095` | `mcq` | false | `D` | `C. wabe` |
| baseline | `mmlu_8096` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8097` | `mcq` | true | `D` | `D. Espy` |
| baseline | `mmlu_8098` | `mcq` | true | `C` | `C. School` |
| baseline | `mmlu_8099` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8100` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8101` | `mcq` | false | `D` | `B. Reservoir` |
| baseline | `mmlu_8102` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8103` | `mcq` | true | `B` | `B. 23` |
| baseline | `mmlu_8104` | `mcq` | true | `A` | `A. ENIAC` |
| baseline | `mmlu_8105` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8106` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8107` | `mcq` | true | `B` | `B. Greenware` |
| baseline | `mmlu_8108` | `mcq` | true | `B` | `B. 1929` |
| baseline | `mmlu_8109` | `mcq` | true | `A` | `A. England` |
| baseline | `mmlu_8110` | `mcq` | true | `C` | `C. Flora` |
| baseline | `mmlu_8111` | `mcq` | true | `A` | `A. cursing them` |
| baseline | `mmlu_8112` | `mcq` | true | `B` | `B. Seine` |
| baseline | `mmlu_8113` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8114` | `mcq` | false | `A` | `B. The Attractions` |
| baseline | `mmlu_8115` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8116` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8117` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8118` | `mcq` | true | `A` | `A. White balance` |
| baseline | `mmlu_8119` | `mcq` | false | `B` | `C. 40 mph` |
| baseline | `mmlu_8120` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8121` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8122` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8123` | `mcq` | true | `C` | `C. Mixing vinegar with baking soda` |
| baseline | `mmlu_8124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8125` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8126` | `mcq` | true | `C` | `C. electric guitar` |
| baseline | `mmlu_8127` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8128` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8129` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8130` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8131` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8132` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8133` | `mcq` | true | `B` | `B. oui` |
| baseline | `mmlu_8134` | `mcq` | true | `D` | `D. hoot` |
| baseline | `mmlu_8135` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8136` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8137` | `mcq` | true | `D` | `D. Diagnosis` |
| baseline | `mmlu_8138` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8139` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8140` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8141` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8142` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8143` | `mcq` | true | `D` | `D. An extruder` |
| baseline | `mmlu_8144` | `mcq` | true | `A` | `A. stationary bicycle` |
| baseline | `mmlu_8145` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8146` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8147` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8148` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8149` | `mcq` | true | `C` | `C. The effect the plant will have on the environment` |
| baseline | `mmlu_8150` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8151` | `mcq` | true | `A` | `A. Law of Inertia` |
| baseline | `mmlu_8152` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8153` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8154` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8155` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8156` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8157` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8158` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8159` | `mcq` | true | `A` | `A. Nautilus` |
| baseline | `mmlu_8160` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8161` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8163` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8164` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8165` | `mcq` | true | `A` | `A. Philadelphia` |
| baseline | `mmlu_8166` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8167` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8168` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8169` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8170` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8171` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8172` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8173` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8174` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8175` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8176` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8177` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8178` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8179` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8180` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8181` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8182` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8183` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8184` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8185` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8186` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8187` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8188` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8189` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8190` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8191` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8193` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8194` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8195` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8196` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8197` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8198` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8199` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8200` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8201` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8202` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8203` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8204` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8205` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8206` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8208` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8209` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8210` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8211` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8212` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8213` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8214` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8215` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8216` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8217` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8218` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8219` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8220` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8221` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8222` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8223` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8224` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8225` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8226` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8227` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8228` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8229` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8230` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8231` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8232` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8233` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8234` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8235` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8236` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8237` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8238` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8239` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8240` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8241` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8242` | `mcq` | true | `D` | `D. none of the above` |
| baseline | `mmlu_8243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8244` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8245` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8246` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8247` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8248` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8249` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8250` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8251` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8252` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8253` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8254` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8255` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8256` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8257` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8258` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8259` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8260` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8261` | `mcq` | false | `A` | `B. by eliminating the patient's capacity for self-determination` |
| baseline | `mmlu_8262` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8263` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8264` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8265` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8266` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8267` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8268` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8269` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8270` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8271` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8272` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8273` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8274` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8275` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8276` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8277` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8278` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8279` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8280` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8281` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8282` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8283` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8284` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8285` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8286` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8287` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8288` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8289` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8290` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8291` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8292` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8293` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8294` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8295` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8297` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8298` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8299` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8300` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8301` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8302` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8303` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8304` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8305` | `mcq` | false | `C` | `D. John Stuart Mill` |
| baseline | `mmlu_8306` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8307` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8308` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8309` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8310` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8311` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8312` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8313` | `mcq` | false | `C` | `D. all of the above` |
| baseline | `mmlu_8314` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8316` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8317` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8318` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8319` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8320` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8321` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8322` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8323` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8324` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8325` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8326` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8328` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8329` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8330` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8331` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8332` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8333` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8334` | `mcq` | true | `B` | `B. "ought."` |
| baseline | `mmlu_8335` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8336` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8337` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8338` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8339` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8340` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8341` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8342` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8343` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8344` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8345` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8346` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8347` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8348` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8349` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8350` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8351` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8353` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8354` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8355` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8356` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8357` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8358` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8359` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8360` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8361` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8362` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8363` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8364` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8365` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8366` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8367` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8368` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8369` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8370` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8371` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8372` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8373` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8374` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8376` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8377` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8378` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8379` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8380` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8381` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8382` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8383` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8384` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8385` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8386` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8387` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8388` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8389` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8390` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8391` | `mcq` | true | `D` | `D. pollution.` |
| baseline | `mmlu_8392` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8393` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8394` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8395` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8396` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8397` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8398` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8399` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8401` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8402` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8403` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8404` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8405` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8406` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8407` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8408` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8409` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8410` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8411` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8412` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8413` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8414` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8415` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8416` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8417` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8418` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8419` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8420` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8421` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8422` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8423` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8424` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8425` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8426` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8427` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8428` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8429` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8430` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8431` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8432` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8433` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8434` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8435` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8436` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8437` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8438` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8439` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8440` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8441` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8442` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8443` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8444` | `mcq` | false | `B` | `D. A and B are equally good athletes.` |
| baseline | `mmlu_8445` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8446` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8447` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8448` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8449` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8450` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8451` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8452` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8453` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8454` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8455` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8456` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8457` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8458` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8459` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8460` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8461` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8462` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8463` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8464` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8465` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8466` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8467` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8468` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8470` | `mcq` | true | `C` | `C. active/passive euthanasia` |
| baseline | `mmlu_8471` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8472` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8473` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8474` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8475` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8476` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8477` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8478` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8479` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8480` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8481` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8482` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8483` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8484` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8485` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8486` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8487` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8488` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8489` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8490` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8491` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8492` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8493` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8494` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8495` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8496` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8497` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8498` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8499` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8500` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8501` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8502` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8503` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8504` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8505` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8506` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8507` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8508` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8509` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8510` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8512` | `mcq` | true | `B` | `B. actions.` |
| baseline | `mmlu_8513` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8514` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8515` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8516` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8517` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8518` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8519` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8520` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8521` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8522` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8523` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8524` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8525` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8526` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8527` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8528` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8529` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8530` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8531` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8532` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8533` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8534` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8535` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8536` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8537` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8538` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8539` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8540` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8541` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8542` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8543` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8544` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8545` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8546` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8547` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8548` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8549` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8550` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8551` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8552` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8553` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8554` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8555` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8556` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8557` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8558` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8559` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8560` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8561` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8562` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8563` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8564` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8565` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8566` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8567` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8568` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8569` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8570` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8571` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8572` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8573` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8574` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8575` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8576` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8577` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8578` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8579` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8580` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8581` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8582` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8583` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8584` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8585` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8586` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8587` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8588` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8589` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8590` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8591` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8592` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8593` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8594` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8595` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8596` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8597` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8598` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8599` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8600` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8601` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8602` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8603` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8604` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8605` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8606` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8607` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8608` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8609` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8610` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8611` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8612` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8613` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8614` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8615` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8616` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8617` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8618` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8619` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8620` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8621` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8622` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8623` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8624` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8625` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8626` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8627` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8628` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8629` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8630` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8631` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8632` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8633` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8634` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8635` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8636` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8637` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8638` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8639` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8640` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8641` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8642` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8643` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8644` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8645` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8646` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8647` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8648` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8649` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8650` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8651` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8652` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8653` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8654` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8655` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8656` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8657` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8658` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8659` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8660` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8661` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8662` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8663` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8664` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8665` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8666` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8667` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8668` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8669` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8670` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8671` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8672` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8673` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8674` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8675` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8676` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8677` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8678` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8679` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8680` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8681` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8682` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8683` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8684` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8685` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8686` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8687` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8688` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8689` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8690` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8691` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8692` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8693` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8694` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8695` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8696` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8697` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8698` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8699` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8700` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8701` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8702` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8703` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8704` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8705` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8706` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8707` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8708` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8709` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8710` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8711` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8712` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8713` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8714` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8715` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8716` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8717` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8718` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8719` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8720` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8721` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8722` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8723` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8724` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8725` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8726` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8727` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8728` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8729` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8730` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8731` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8732` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8733` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8734` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8735` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8736` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8737` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8738` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8739` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8740` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8741` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8742` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8743` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8744` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8745` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8746` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8747` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8748` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8749` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8750` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8751` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8752` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8753` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8754` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8755` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8756` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8757` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8758` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8759` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8760` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8761` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8762` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8763` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8764` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8765` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8766` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8767` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8768` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8769` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8770` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8771` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8772` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8773` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8774` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8775` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8776` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8777` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8778` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8779` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8780` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8781` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8782` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8783` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8784` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8785` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8786` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8787` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8788` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8789` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8790` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8791` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8792` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8793` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8794` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8795` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8796` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8797` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8798` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8799` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8800` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8801` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8802` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8803` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8804` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8805` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8806` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8807` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8808` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8809` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8810` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8811` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8812` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8813` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8814` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8815` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8816` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8817` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8818` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8819` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8820` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8821` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8822` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8823` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8824` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8825` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8826` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8827` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8828` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8829` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8830` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8831` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8832` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8833` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8834` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8835` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8836` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8837` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8838` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8839` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8840` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8841` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8842` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8843` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8844` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8845` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8846` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8847` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8848` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8849` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8850` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8851` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8852` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8853` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8854` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8855` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8856` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8857` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8858` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8859` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8860` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8861` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8862` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8863` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8864` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8865` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8866` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8867` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8868` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8869` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8870` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8871` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8872` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8873` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8874` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8875` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8876` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8877` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8878` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8879` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8880` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8881` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8882` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8883` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8884` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8885` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8886` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8887` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8888` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8889` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8890` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8891` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8892` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8893` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8894` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8895` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8896` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8897` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8898` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8899` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8900` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8901` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8902` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8903` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8904` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8905` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8906` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8907` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8908` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8909` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8910` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8911` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8912` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8913` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8914` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8915` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8916` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8917` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8918` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8919` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8920` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8921` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8922` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8923` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8924` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8925` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8926` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8927` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8928` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8929` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8930` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8931` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8932` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8933` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8934` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8935` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8936` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8937` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8938` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8939` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8940` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8941` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8942` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8943` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8944` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8945` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8946` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8947` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8948` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8949` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8950` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8951` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8952` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8953` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8954` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8955` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8956` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8957` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8958` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8959` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8960` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8961` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8962` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8963` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8964` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8965` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8966` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8967` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8968` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8969` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8970` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8971` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8972` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8973` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8974` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8975` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8976` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8977` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8978` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8979` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8980` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8981` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8982` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8983` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8984` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8985` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8986` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8987` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8988` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8989` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8990` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8991` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8992` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8993` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8994` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8995` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8996` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8997` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8998` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8999` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9000` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9001` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9002` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9003` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9004` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9005` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9006` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9007` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9008` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9009` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9010` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9011` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9012` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9013` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9014` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9015` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9016` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9017` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9018` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9019` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9020` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9021` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9022` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9023` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9024` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9025` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9026` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9027` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9028` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9029` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9030` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9031` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9032` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9033` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9034` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9035` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9036` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9037` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9038` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9039` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9040` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9041` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9042` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9043` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9044` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9045` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9046` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9047` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9048` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9049` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9050` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9051` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9052` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9053` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9054` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9055` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9056` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9057` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9058` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9059` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9060` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9061` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9062` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9063` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9064` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9065` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9066` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9067` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9068` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9069` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9070` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9071` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9072` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9073` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9074` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9075` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9076` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9077` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9078` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9079` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9080` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9081` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9082` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9083` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9084` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9085` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9086` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9087` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9088` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9089` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9090` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9091` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9092` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9093` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9094` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9095` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9096` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9097` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9098` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9099` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9100` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9101` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9102` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9103` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9104` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9105` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9106` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9107` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9108` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9109` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9110` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9111` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9112` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9113` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9114` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9115` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9116` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9117` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9118` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9119` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9120` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9121` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9122` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9123` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9124` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9125` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9126` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9127` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9128` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9129` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9130` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9131` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9132` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9133` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9134` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9135` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9136` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9137` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9138` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9139` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9140` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9141` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9142` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9143` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9144` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9145` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9146` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9147` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9148` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9149` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9150` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9151` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9152` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9153` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9154` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9155` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9156` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9157` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9158` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9159` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9160` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9161` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9162` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9163` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9164` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9165` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9166` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9167` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9168` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9169` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9170` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9171` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9172` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9173` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9174` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9175` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9176` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9177` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9178` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9179` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9180` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9181` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9182` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9183` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9184` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9185` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9186` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9187` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9188` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9189` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9190` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9191` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9192` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9193` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9194` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9195` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9196` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9197` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9198` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9199` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9200` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9201` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9202` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9203` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9204` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9205` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9206` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9207` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9208` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9209` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9210` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9211` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9212` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9213` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9214` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9215` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9216` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9217` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9218` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9219` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9220` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9221` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9222` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9223` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9224` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9225` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9226` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9227` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9228` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9229` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9230` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9231` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9232` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9233` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9234` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9235` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9236` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9237` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9238` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9239` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9240` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9241` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9242` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9243` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9244` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9245` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9246` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9247` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9248` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9249` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9250` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9251` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9252` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9253` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9254` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9255` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9256` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9257` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9258` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9259` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9260` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9261` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9262` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9263` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9264` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9265` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9266` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9267` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9268` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9269` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9270` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9271` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9272` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9273` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9274` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9275` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9276` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9277` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9278` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9279` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9280` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9281` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9282` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9283` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9284` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9285` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9286` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9287` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9288` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9289` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9290` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9291` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9292` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9293` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9294` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9295` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9296` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9297` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9298` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9299` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9300` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9301` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9302` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9303` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9304` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9305` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9306` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9307` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9308` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9309` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9310` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9311` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9312` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9313` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9314` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9315` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9316` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9317` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9318` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9319` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9320` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9321` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9322` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9323` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9324` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9325` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9326` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9327` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9328` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9329` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9330` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9331` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9332` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9333` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9334` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9335` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9336` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9337` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9338` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9339` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9340` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9341` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9342` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9343` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9344` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9345` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9346` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9347` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9348` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9349` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9350` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9351` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9352` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9353` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9354` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9355` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9356` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9357` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9358` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9359` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9360` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9361` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9362` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9363` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9364` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9365` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9366` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9367` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9368` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9369` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9370` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9371` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9372` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9373` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9374` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9375` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9376` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9377` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9378` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9379` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9380` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9381` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9382` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9383` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9384` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9385` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9386` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9387` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9388` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9389` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9390` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9391` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9392` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9393` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9394` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9395` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9396` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9397` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9398` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9399` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9400` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9401` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9402` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9403` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9404` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9405` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9406` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9407` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9408` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9409` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9410` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9411` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9412` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9413` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9414` | `mcq` | true | `B` | `B. Oestrogen` |
| baseline | `mmlu_9415` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9416` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9417` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9418` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9419` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9420` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9421` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9422` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9423` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9424` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9425` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9426` | `mcq` | true | `A` | `A. China` |
| baseline | `mmlu_9427` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9428` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9429` | `mcq` | true | `A` | `A. Deuterium` |
| baseline | `mmlu_9430` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9431` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9432` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9434` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9435` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9436` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9437` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9438` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9439` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9440` | `mcq` | true | `C` | `C. Urea` |
| baseline | `mmlu_9441` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9442` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9443` | `mcq` | false | `B` | `C. 66%` |
| baseline | `mmlu_9444` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9445` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9446` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9447` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9448` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9449` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9450` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9451` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9452` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9453` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9454` | `mcq` | false | `B` | `A. 45%-50%` |
| baseline | `mmlu_9455` | `mcq` | true | `A` | `A. Biotin` |
| baseline | `mmlu_9456` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9457` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9458` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9459` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9460` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9461` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9462` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9463` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9464` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9465` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9466` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9467` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9468` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9469` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9470` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9471` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9472` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9473` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9474` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9475` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9476` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9477` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9478` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9479` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9480` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9481` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9482` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9483` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9484` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9485` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9486` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9487` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9488` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9489` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9490` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9491` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9492` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9493` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9495` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9496` | `mcq` | false | `A` | `C. Lorcaserin` |
| baseline | `mmlu_9497` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9498` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9499` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9500` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9501` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9502` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9503` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9505` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9506` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9507` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9508` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9509` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9510` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9511` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9512` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9513` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9514` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9515` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9516` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9517` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9518` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9519` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9520` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9521` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9522` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9523` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9524` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9525` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9526` | `mcq` | true | `D` | `D. 32` |
| baseline | `mmlu_9527` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9528` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9529` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9530` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9531` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9532` | `mcq` | true | `C` | `C. > 95%` |
| baseline | `mmlu_9533` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9534` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9535` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9536` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9537` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9538` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9539` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9540` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9541` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9542` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9543` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9544` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9545` | `mcq` | false | `B` | `A. 20%` |
| baseline | `mmlu_9546` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9547` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9548` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9549` | `mcq` | true | `A` | `A. Wernicke-Korsakoff syndrome` |
| baseline | `mmlu_9550` | `mcq` | true | `C` | `C. Cytosine` |
| baseline | `mmlu_9551` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9552` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9553` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9554` | `mcq` | false | `C` | `B. DXA` |
| baseline | `mmlu_9555` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9556` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9557` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9558` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9559` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9560` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9561` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9562` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9563` | `mcq` | true | `D` | `D. Proteins` |
| baseline | `mmlu_9564` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9565` | `mcq` | true | `C` | `C. acetaldehyde` |
| baseline | `mmlu_9566` | `mcq` | true | `C` | `C. 1 unit of BMI` |
| baseline | `mmlu_9567` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9568` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9569` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9570` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9571` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9572` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9573` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9574` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9575` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9576` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9577` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9578` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9579` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9580` | `mcq` | false | `B` | `D. 39%` |
| baseline | `mmlu_9581` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9582` | `mcq` | false | `B` | `D. 4` |
| baseline | `mmlu_9583` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9584` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9585` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9586` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9587` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9588` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9589` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9590` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9591` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9592` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9593` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9594` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9595` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_9596` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9597` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9598` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9599` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9600` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9601` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9602` | `mcq` | false | `D` | `B. Alanine` |
| baseline | `mmlu_9603` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9604` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9605` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9606` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9607` | `mcq` | false | `C` | `D. Broccoli` |
| baseline | `mmlu_9608` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9609` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9610` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9611` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9612` | `mcq` | false | `C` | `B. 5.7` |
| baseline | `mmlu_9613` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9614` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9615` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9616` | `mcq` | true | `D` | `D. BP < 130/80, Trig <150, LDL < 100` |
| baseline | `mmlu_9617` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9618` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9619` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9620` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9621` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9622` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9623` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9624` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9625` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9626` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9627` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9628` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9629` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9630` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9631` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9632` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9633` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9634` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9635` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9636` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9637` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9638` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9639` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9640` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9641` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9642` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9643` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9644` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9645` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9646` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9647` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9648` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_9649` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9650` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9651` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9652` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9653` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9654` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9655` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9656` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9657` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9658` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9659` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9660` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9661` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9662` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9663` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9664` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9665` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9666` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9668` | `mcq` | false | `D` | `B. Plasma free fatty acids` |
| baseline | `mmlu_9669` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9670` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9671` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9672` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9673` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9674` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9675` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9676` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9677` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9678` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9679` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9680` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9681` | `mcq` | true | `B` | `B. 32` |
| baseline | `mmlu_9682` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9683` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9684` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9685` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9686` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9687` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9688` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9689` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9690` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9691` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9692` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9693` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9694` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9695` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9696` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9697` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9698` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9699` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9700` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9701` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9702` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9703` | `mcq` | false | `D` | `A. 60 g glucose per hour` |
| baseline | `mmlu_9704` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9705` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9706` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9707` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9708` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9709` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9710` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9711` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9712` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9713` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9714` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9715` | `mcq` | true | `D` | `D. the soul` |
| baseline | `mmlu_9716` | `mcq` | true | `D` | `D. a good will` |
| baseline | `mmlu_9717` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9718` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9719` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9721` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9722` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9723` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9724` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9725` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9726` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9727` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9728` | `mcq` | false | `D` | `A. rational` |
| baseline | `mmlu_9729` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9730` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9731` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9732` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9733` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9734` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9735` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9736` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9737` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9738` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9739` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9740` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9741` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9742` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9743` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9744` | `mcq` | true | `A` | `A. expression` |
| baseline | `mmlu_9745` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9746` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9747` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9748` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9749` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9750` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9751` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9752` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9753` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9754` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9755` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9756` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9758` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9759` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9760` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9761` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9762` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9763` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9764` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9765` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9766` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9767` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9768` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9769` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9770` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9771` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9772` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9773` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9775` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9776` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9777` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9778` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9779` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9780` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9781` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9782` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9783` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9784` | `mcq` | true | `D` | `D. arbitrary` |
| baseline | `mmlu_9785` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9786` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9787` | `mcq` | false | `B` | `D. all of the above.` |
| baseline | `mmlu_9788` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9789` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9790` | `mcq` | false | `D` | `B. lawful treatment` |
| baseline | `mmlu_9791` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9792` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9793` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9794` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9795` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9796` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9797` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9798` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9799` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9800` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9801` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9802` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9803` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9804` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9805` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9806` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9807` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9808` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9809` | `mcq` | true | `B` | `B. war` |
| baseline | `mmlu_9810` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9811` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9812` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9813` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9814` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9815` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9816` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9817` | `mcq` | true | `A` | `A. entirely subjective` |
| baseline | `mmlu_9818` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9819` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9820` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9821` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9822` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9823` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9824` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9825` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9826` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9827` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9828` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9829` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9830` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9831` | `mcq` | true | `D` | `D. reductio ad absurdum` |
| baseline | `mmlu_9832` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9833` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9834` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9835` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9836` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9837` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9838` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9839` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9840` | `mcq` | true | `B` | `B. common` |
| baseline | `mmlu_9841` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9842` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9843` | `mcq` | true | `C` | `C. impossible` |
| baseline | `mmlu_9844` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9845` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9846` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9847` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9848` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9849` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9850` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9851` | `mcq` | true | `B` | `B. God` |
| baseline | `mmlu_9852` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9853` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9854` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9855` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9856` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9857` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9858` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9859` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9860` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9861` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9862` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9863` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9864` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9865` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9866` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9867` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9868` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9869` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9870` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9871` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9872` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9873` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9874` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9875` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9876` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9877` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9878` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9880` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9881` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9882` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9883` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9884` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9885` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9886` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9887` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9888` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9889` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9890` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9891` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9892` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9893` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9894` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9895` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9896` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9897` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9898` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9899` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9900` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9901` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9902` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9903` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9904` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9905` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9906` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9907` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9908` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9909` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9910` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9911` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9912` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9913` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9914` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9915` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9916` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9917` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9918` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9919` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9920` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9921` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9922` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9923` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9924` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9925` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9926` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9927` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9928` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9929` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9930` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9931` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9932` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9933` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9934` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9935` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9936` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9937` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9938` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9939` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9940` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9941` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9942` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9943` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9944` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9945` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9946` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9947` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9948` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9949` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9950` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9951` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9952` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9953` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9954` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9955` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9956` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9957` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9958` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9959` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9960` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9961` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9962` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9963` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9964` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9965` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9966` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9967` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9968` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9969` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9970` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9971` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9972` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9973` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9974` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9975` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_9976` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9977` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9978` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9979` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9980` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9981` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9982` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9983` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_9984` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9985` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9986` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9987` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9988` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9989` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9990` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9991` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9992` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9993` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9994` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9995` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9996` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9997` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9998` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9999` | `mcq` | false | `A` | `B` |
