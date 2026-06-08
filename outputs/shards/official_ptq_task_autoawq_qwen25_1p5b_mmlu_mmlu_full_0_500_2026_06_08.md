# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 271 / 500 | 0.5420 | 10.5848 | 0.144740 |

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
