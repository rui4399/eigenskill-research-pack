# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `4000`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 2145 / 4000 | 0.5363 | 8.8304 | 0.187847 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `2` |
| baseline | `mmlu_2` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `5` |
| baseline | `mmlu_13` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_14` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_16` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_17` | `mcq` | false | `C` | `D. (3,6)` |
| baseline | `mmlu_18` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_19` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_20` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_21` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_22` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_23` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_24` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_25` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_26` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_27` | `mcq` | false | `B` | `D. No.` |
| baseline | `mmlu_28` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_29` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_30` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_31` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_32` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_33` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_35` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_36` | `mcq` | false | `D` | `C. 11` |
| baseline | `mmlu_37` | `mcq` | false | `B` | `D. No.` |
| baseline | `mmlu_38` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_39` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_41` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_42` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_43` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_44` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_45` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_47` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_48` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_49` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_50` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_51` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_52` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_53` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_54` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_55` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_56` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_57` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_58` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_59` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_60` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_61` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_62` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_63` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_64` | `mcq` | false | `B` | `C. infinitely many` |
| baseline | `mmlu_65` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_66` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_67` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_68` | `mcq` | false | `A` | `C. (x-1)(x+1)^3` |
| baseline | `mmlu_69` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_70` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_71` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_72` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_73` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_74` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_75` | `mcq` | false | `B` | `D. False, True` |
| baseline | `mmlu_76` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_77` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_78` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_79` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_80` | `mcq` | false | `B` | `C. True, False` |
| baseline | `mmlu_81` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_82` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_83` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_84` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_85` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_86` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_87` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_88` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_89` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_90` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_91` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_92` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_93` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_94` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_95` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_96` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_97` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_98` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_99` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_100` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_101` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_102` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_103` | `mcq` | false | `C` | `B. Skeletal muscles` |
| baseline | `mmlu_104` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_105` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_106` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_107` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_108` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_109` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_110` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_111` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_112` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_113` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_114` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_115` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_116` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_117` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_118` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_119` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_120` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_121` | `mcq` | false | `C` | `A. deep to its superior border.` |
| baseline | `mmlu_122` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_123` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_124` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_125` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_126` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_127` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_128` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_129` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_130` | `mcq` | true | `C` | `C. Flexion` |
| baseline | `mmlu_131` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_132` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_133` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_134` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_135` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_136` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_137` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_138` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_139` | `mcq` | true | `C` | `C. Liver` |
| baseline | `mmlu_140` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_141` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_142` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_143` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_144` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_145` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_146` | `mcq` | true | `B` | `B. Lower leg` |
| baseline | `mmlu_147` | `mcq` | true | `C` | `C. Erythrocyte` |
| baseline | `mmlu_148` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_149` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_150` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_151` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_153` | `mcq` | false | `B` | `A. caudal` |
| baseline | `mmlu_154` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_155` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_156` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_157` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_158` | `mcq` | true | `D` | `D. Synapse` |
| baseline | `mmlu_159` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_160` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_161` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_162` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_163` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_164` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_165` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_166` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_167` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_168` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_169` | `mcq` | true | `B` | `B. The mental nerve` |
| baseline | `mmlu_170` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_171` | `mcq` | true | `A` | `A. Acetylcholine` |
| baseline | `mmlu_172` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_173` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_174` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_175` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_176` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_177` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_178` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_179` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_180` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_181` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_182` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_183` | `mcq` | true | `B` | `B. Epiglottis` |
| baseline | `mmlu_184` | `mcq` | false | `B` | `A. The roof` |
| baseline | `mmlu_185` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_186` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_187` | `mcq` | false | `C` | `B. muscles of the soft palate.` |
| baseline | `mmlu_188` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_189` | `mcq` | true | `A` | `A. Collagen` |
| baseline | `mmlu_190` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_191` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_193` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_194` | `mcq` | false | `A` | `B. Right lateral pterygoid muscle` |
| baseline | `mmlu_195` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_196` | `mcq` | false | `A` | `C. Fifth Cranial Nerves.` |
| baseline | `mmlu_197` | `mcq` | false | `C` | `A. light pink in color on both sides of the mucogingival junction.` |
| baseline | `mmlu_198` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_199` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_200` | `mcq` | false | `D` | `B. resorb bone and differentiate from periosteal mesenchymal cells.` |
| baseline | `mmlu_201` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_202` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_203` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_204` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_205` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_206` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_207` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_208` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_209` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_210` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_211` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_212` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_213` | `mcq` | true | `A` | `A. Alveoli` |
| baseline | `mmlu_214` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_215` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_216` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_217` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_218` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_219` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_220` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_221` | `mcq` | false | `B` | `A. posterior and medial to medial pterygoid.` |
| baseline | `mmlu_222` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_223` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_224` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_225` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_226` | `mcq` | true | `C` | `C. Olfactory` |
| baseline | `mmlu_227` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_228` | `mcq` | false | `A` | `B. Proteins` |
| baseline | `mmlu_229` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_230` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_231` | `mcq` | true | `D` | `D. Pituitary` |
| baseline | `mmlu_232` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_233` | `mcq` | true | `C` | `C. Urethra` |
| baseline | `mmlu_234` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_235` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_236` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_237` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_238` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_239` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_240` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_241` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_242` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_243` | `mcq` | false | `D` | `B. Hydrogen` |
| baseline | `mmlu_244` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_245` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_246` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_247` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_248` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_249` | `mcq` | true | `B` | `B. Laniakea` |
| baseline | `mmlu_250` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_251` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_252` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_253` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_254` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_255` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_256` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_257` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_258` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_259` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_260` | `mcq` | false | `D` | `A. Callisto` |
| baseline | `mmlu_261` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_262` | `mcq` | true | `D` | `D. Phoenix Mars Lander` |
| baseline | `mmlu_263` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_264` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_265` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_266` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_267` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_268` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_269` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_270` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_271` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_272` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_273` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_274` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_275` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_276` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_277` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_278` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_279` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_280` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_281` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_282` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_283` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_284` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_285` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_286` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_287` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_288` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_289` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_290` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_291` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_292` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_293` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_294` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_295` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_296` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_297` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_298` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_299` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_300` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_301` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_302` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_303` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_304` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_305` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_307` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_308` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_309` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_310` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_311` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_312` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_313` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_314` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_315` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_316` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_317` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_318` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_319` | `mcq` | false | `A` | `B. presence of an atmosphere` |
| baseline | `mmlu_320` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_321` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_322` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_323` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_325` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_326` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_327` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_328` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_329` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_330` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_331` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_332` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_333` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_334` | `mcq` | false | `C` | `B. Cygnus` |
| baseline | `mmlu_335` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_336` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_337` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_338` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_339` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_340` | `mcq` | false | `A` | `B. Helium` |
| baseline | `mmlu_341` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_342` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_343` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_344` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_345` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_346` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_347` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_348` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_349` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_350` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_351` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_352` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_353` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_354` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_355` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_356` | `mcq` | true | `B` | `B. 11` |
| baseline | `mmlu_357` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_358` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_359` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_360` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_361` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_362` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_363` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_364` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_365` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_366` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_367` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_368` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_369` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_370` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_371` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_372` | `mcq` | true | `D` | `D. CO2` |
| baseline | `mmlu_373` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_374` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_375` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_376` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_377` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_378` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_379` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_380` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_381` | `mcq` | true | `B` | `B. Arecibo Telescope` |
| baseline | `mmlu_382` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_383` | `mcq` | false | `D` | `A. Wolf 359` |
| baseline | `mmlu_384` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_385` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_386` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_387` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_388` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_389` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_390` | `mcq` | false | `D` | `C. Work-play balance` |
| baseline | `mmlu_391` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_392` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_393` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_394` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_395` | `mcq` | false | `B` | `C. Political, Interactions, Outcomes` |
| baseline | `mmlu_396` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_397` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_398` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_399` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_401` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_402` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_403` | `mcq` | true | `A` | `A. To make a profit` |
| baseline | `mmlu_404` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_405` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_406` | `mcq` | false | `A` | `D. 1,2,3,4` |
| baseline | `mmlu_407` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_408` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_409` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_410` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_411` | `mcq` | true | `A` | `A. Improve Revenue` |
| baseline | `mmlu_412` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_413` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_414` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_415` | `mcq` | false | `D` | `B. China` |
| baseline | `mmlu_416` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_417` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_418` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_419` | `mcq` | false | `D` | `C. 1,2` |
| baseline | `mmlu_420` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_421` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_422` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_423` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_424` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_425` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_426` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_427` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_428` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_429` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_430` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_431` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_432` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_433` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_434` | `mcq` | true | `A` | `A. Social Contract` |
| baseline | `mmlu_435` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_436` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_437` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_438` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_439` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_440` | `mcq` | true | `C` | `C. Power, Legitimacy, Urgency, Salience` |
| baseline | `mmlu_441` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_442` | `mcq` | true | `C` | `C. 1,2,3` |
| baseline | `mmlu_443` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_444` | `mcq` | true | `A` | `A. Legislation, Sarbanes-Oxley Act` |
| baseline | `mmlu_445` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_446` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_447` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_448` | `mcq` | true | `A` | `A. Globalisation, Cultural, Legal, Accountability` |
| baseline | `mmlu_449` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_450` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_451` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_452` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_453` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_454` | `mcq` | true | `A` | `A. Social responsibility, Collaboration, Process, Frameworks` |
| baseline | `mmlu_455` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_456` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_457` | `mcq` | false | `B` | `C. 1,2,3,4` |
| baseline | `mmlu_458` | `mcq` | false | `B` | `D. 1,2,3,4` |
| baseline | `mmlu_459` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_460` | `mcq` | true | `C` | `C. Postmodern ethics` |
| baseline | `mmlu_461` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_462` | `mcq` | true | `C` | `C. Interest, Uncertain, Speculative, Tangible assets` |
| baseline | `mmlu_463` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_464` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_465` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_466` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_467` | `mcq` | false | `B` | `D. 1,2` |
| baseline | `mmlu_468` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_470` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_471` | `mcq` | true | `C` | `C. 1,2,3` |
| baseline | `mmlu_472` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_473` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_474` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_475` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_476` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_477` | `mcq` | true | `B` | `B. 1,3` |
| baseline | `mmlu_478` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_479` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_480` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_481` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_482` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_483` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_484` | `mcq` | true | `A` | `A. Professional, Organizational, Personal, Organizational` |
| baseline | `mmlu_485` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_486` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_487` | `mcq` | true | `A` | `A. 18 gauge.` |
| baseline | `mmlu_488` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_489` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_490` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_491` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_492` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_493` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_494` | `mcq` | true | `A` | `A. elevating the pH and buffering capacity of the extracellular fluid allowing a faster efflux of hydrogen ions from mus` |
| baseline | `mmlu_495` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_496` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_497` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_498` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_499` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_500` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_501` | `mcq` | true | `B` | `B. actin and myosin.` |
| baseline | `mmlu_502` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_503` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_504` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_505` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_506` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_507` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_508` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_509` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_510` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_511` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_512` | `mcq` | true | `B` | `B. When the catheter is blocked.` |
| baseline | `mmlu_513` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_514` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_515` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_516` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_517` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_518` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_519` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_520` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_522` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_523` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_524` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_526` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_527` | `mcq` | false | `B` | `C. 60-90 bpm.` |
| baseline | `mmlu_528` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_529` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_530` | `mcq` | true | `B` | `B. A pea-sized amount.` |
| baseline | `mmlu_531` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_532` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_533` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_534` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_535` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_536` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_537` | `mcq` | false | `C` | `B. Every 8 hours.` |
| baseline | `mmlu_538` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_539` | `mcq` | false | `C` | `D. 1 mmHg.` |
| baseline | `mmlu_540` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_541` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_542` | `mcq` | false | `D` | `C. 9.3` |
| baseline | `mmlu_543` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_544` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_545` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_546` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_547` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_548` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_549` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_550` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_551` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_552` | `mcq` | false | `D` | `B. 10%` |
| baseline | `mmlu_553` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_554` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_555` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_556` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_557` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_558` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_559` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_560` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_561` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_562` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_563` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_564` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_565` | `mcq` | true | `B` | `B. Insulin` |
| baseline | `mmlu_566` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_567` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_568` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_569` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_570` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_571` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_572` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_573` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_574` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_575` | `mcq` | true | `D` | `D. Call for assistance from a medical practitioner.` |
| baseline | `mmlu_576` | `mcq` | false | `D` | `A. warm.` |
| baseline | `mmlu_577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_578` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_579` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_580` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_581` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_582` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_583` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_584` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_585` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_586` | `mcq` | true | `B` | `B. 1.92` |
| baseline | `mmlu_587` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_588` | `mcq` | true | `C` | `C. Reduced amount of gastric acid.` |
| baseline | `mmlu_589` | `mcq` | true | `B` | `B. Normal saline.` |
| baseline | `mmlu_590` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_591` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_592` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_593` | `mcq` | false | `D` | `B. a recessive allele on the X chromosome.` |
| baseline | `mmlu_594` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_595` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_596` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_597` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_598` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_599` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_600` | `mcq` | false | `A` | `B. 1 mg/L` |
| baseline | `mmlu_601` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_602` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_603` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_604` | `mcq` | true | `C` | `C. Carnosine` |
| baseline | `mmlu_605` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_606` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_607` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_608` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_609` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_610` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_611` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_612` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_613` | `mcq` | true | `A` | `A. deoxyribonucleic acid.` |
| baseline | `mmlu_614` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_615` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_616` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_617` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_618` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_619` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_620` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_621` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_622` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_623` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_624` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_625` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_626` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_627` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_628` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_629` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_630` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_631` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_632` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_633` | `mcq` | true | `B` | `B. Temperature.` |
| baseline | `mmlu_634` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_635` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_636` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_637` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_638` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_639` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_640` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_641` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_642` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_643` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_644` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_645` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_646` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_647` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_648` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_649` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_650` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_651` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_652` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_653` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_654` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_655` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_656` | `mcq` | true | `A` | `A. Thymine` |
| baseline | `mmlu_657` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_658` | `mcq` | false | `C` | `A. Heroin (opiates).` |
| baseline | `mmlu_659` | `mcq` | false | `B` | `C. Understanding others' speech.` |
| baseline | `mmlu_660` | `mcq` | true | `A` | `A. Scaphoid, lunate, triquetral, pisiform, trapezium, trapezoid, capitate, hamate.` |
| baseline | `mmlu_661` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_662` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_663` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_664` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_665` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_666` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_667` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_668` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_669` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_670` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_671` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_672` | `mcq` | true | `D` | `D. 46` |
| baseline | `mmlu_673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_674` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_675` | `mcq` | true | `D` | `D. phosphofructokinase.` |
| baseline | `mmlu_676` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_677` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_678` | `mcq` | true | `A` | `A. yields 8 molecules of acetyl-CoA and some ATP and water.` |
| baseline | `mmlu_679` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_680` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_681` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_682` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_683` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_684` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_685` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_686` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_687` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_688` | `mcq` | true | `C` | `C. cytoplasm.` |
| baseline | `mmlu_689` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_690` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_691` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_692` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_693` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_694` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_695` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_696` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_697` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_698` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_699` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_700` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_701` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_702` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_703` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_704` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_705` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_706` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_707` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_708` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_709` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_710` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_711` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_712` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_713` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_714` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_715` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_716` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_717` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_718` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_719` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_720` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_721` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_722` | `mcq` | false | `A` | `C. frequently falls by 1 - 3 mM.` |
| baseline | `mmlu_723` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_724` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_725` | `mcq` | false | `D` | `B. 500ml.` |
| baseline | `mmlu_726` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_727` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_728` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_729` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_730` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_731` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_732` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_733` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_734` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_735` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_736` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_737` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_738` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_739` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_740` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_741` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_742` | `mcq` | true | `A` | `A. Drugs may be implicated in the causation of gout.` |
| baseline | `mmlu_743` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_744` | `mcq` | true | `B` | `B. The pancreas.` |
| baseline | `mmlu_745` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_746` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_747` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_748` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_749` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_750` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_751` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_752` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_753` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_754` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_755` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_756` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_757` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_758` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_759` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_760` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_761` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_762` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_763` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_764` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_765` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_766` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_767` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_768` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_769` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_770` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_771` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_772` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_773` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_774` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_775` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_776` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_777` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_778` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_779` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_780` | `mcq` | true | `A` | `A. coefficient of relatedness` |
| baseline | `mmlu_781` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_782` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_783` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_784` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_785` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_786` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_787` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_788` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_789` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_790` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_791` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_792` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_793` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_794` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_795` | `mcq` | false | `A` | `C. nodes` |
| baseline | `mmlu_796` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_797` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_798` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_799` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_800` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_801` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_802` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_803` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_804` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_805` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_806` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_807` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_808` | `mcq` | false | `C` | `B. microtubules in the axon to undergo irreversible dissociation` |
| baseline | `mmlu_809` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_810` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_811` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_812` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_813` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_814` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_815` | `mcq` | false | `C` | `B. Two` |
| baseline | `mmlu_816` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_817` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_818` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_819` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_820` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_821` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_822` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_823` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_824` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_825` | `mcq` | false | `A` | `D. 90%` |
| baseline | `mmlu_826` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_827` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_828` | `mcq` | true | `C` | `C. kinetochore` |
| baseline | `mmlu_829` | `mcq` | true | `A` | `A. thigmotropism` |
| baseline | `mmlu_830` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_831` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_832` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_833` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_834` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_835` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_836` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_837` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_838` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_839` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_840` | `mcq` | true | `B` | `B. Palisade mesophyll` |
| baseline | `mmlu_841` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_842` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_843` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_844` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_845` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_846` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_847` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_848` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_849` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_850` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_851` | `mcq` | true | `B` | `B. Colchicine` |
| baseline | `mmlu_852` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_853` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_854` | `mcq` | true | `A` | `A. hydrogen bonding between the peptide backbone atoms` |
| baseline | `mmlu_855` | `mcq` | false | `D` | `C. the nucleosome core` |
| baseline | `mmlu_856` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_857` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_858` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_859` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_860` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_861` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_862` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_863` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_864` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_865` | `mcq` | true | `A` | `A. Nearly all of the enzyme molecules are interacting with acetaldehyde molecules.` |
| baseline | `mmlu_866` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_867` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_868` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_869` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_870` | `mcq` | true | `A` | `A. Producing a heterokaryon` |
| baseline | `mmlu_871` | `mcq` | true | `A` | `A. an increase in genetic homogeneity in the metapopulation` |
| baseline | `mmlu_872` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_873` | `mcq` | true | `B` | `B. Photoperiod` |
| baseline | `mmlu_874` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_875` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_876` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_877` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_878` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_879` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_880` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_881` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_882` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_883` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_884` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_885` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_886` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_887` | `mcq` | false | `A` | `B. population levels of a species are kept at equilibrium through natural regulatory mechanisms.` |
| baseline | `mmlu_888` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_889` | `mcq` | false | `D` | `B. Rain-forest vegetation` |
| baseline | `mmlu_890` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_891` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_892` | `mcq` | true | `A` | `A. Chitin` |
| baseline | `mmlu_893` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_894` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_895` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_896` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_897` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_898` | `mcq` | false | `D` | `B. 3` |
| baseline | `mmlu_899` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_900` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_901` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_902` | `mcq` | false | `A` | `B. Alpha particles` |
| baseline | `mmlu_903` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_904` | `mcq` | true | `C` | `C. 1:6` |
| baseline | `mmlu_905` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_906` | `mcq` | true | `D` | `D. 11.30 ppm` |
| baseline | `mmlu_907` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_908` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_909` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_910` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_911` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_912` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_913` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_914` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_915` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_916` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_917` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_918` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_919` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_920` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_921` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_922` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_923` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_924` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_925` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_926` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_927` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_928` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_929` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_930` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_931` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_932` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_933` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_934` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_935` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_936` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_937` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_938` | `mcq` | false | `B` | `A. NH3` |
| baseline | `mmlu_939` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_940` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_941` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_942` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_943` | `mcq` | true | `B` | `B. 5.18 mT` |
| baseline | `mmlu_944` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_945` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_946` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_947` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_948` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_949` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_950` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_951` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_952` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_953` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_954` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_955` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_956` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_957` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_958` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_959` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_960` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_961` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_962` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_963` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_964` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_965` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_966` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_967` | `mcq` | false | `D` | `A. Electron distribution` |
| baseline | `mmlu_968` | `mcq` | false | `A` | `C. 8` |
| baseline | `mmlu_969` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_970` | `mcq` | true | `B` | `B. Ultraviolet` |
| baseline | `mmlu_971` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_972` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_973` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_974` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_975` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_976` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_977` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_978` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_979` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_980` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_981` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_982` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_983` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_984` | `mcq` | false | `D` | `B. Boiling point` |
| baseline | `mmlu_985` | `mcq` | false | `B` | `C. 11,070 ppm` |
| baseline | `mmlu_986` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_987` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_988` | `mcq` | false | `D` | `B. 9 lines` |
| baseline | `mmlu_989` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_990` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_991` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_992` | `mcq` | false | `C` | `A. K+` |
| baseline | `mmlu_993` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_994` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_995` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_996` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_997` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_998` | `mcq` | true | `B` | `B. 1:3.5` |
| baseline | `mmlu_999` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1000` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1001` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1002` | `mcq` | false | `C` | `D. I and III only` |
| baseline | `mmlu_1003` | `mcq` | false | `B` | `D. I and III` |
| baseline | `mmlu_1004` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1005` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1006` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1007` | `mcq` | false | `A` | `B. n + 1` |
| baseline | `mmlu_1008` | `mcq` | false | `A` | `C. 10` |
| baseline | `mmlu_1009` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1010` | `mcq` | false | `A` | `D. I and II only` |
| baseline | `mmlu_1011` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1012` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1013` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1014` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1015` | `mcq` | true | `D` | `D. II and III only` |
| baseline | `mmlu_1016` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1017` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1018` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1019` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1020` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1021` | `mcq` | true | `D` | `D. I and II` |
| baseline | `mmlu_1022` | `mcq` | true | `C` | `C. Symbol Table` |
| baseline | `mmlu_1023` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1024` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1025` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1026` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1027` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1028` | `mcq` | false | `D` | `B. 999` |
| baseline | `mmlu_1029` | `mcq` | false | `A` | `D. I and III` |
| baseline | `mmlu_1030` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1031` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1032` | `mcq` | true | `C` | `C. Merge sort` |
| baseline | `mmlu_1033` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1034` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1035` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1036` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1037` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1038` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1039` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1040` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1041` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1042` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1043` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1044` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1045` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1046` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1047` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1048` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1049` | `mcq` | true | `C` | `C. Merge sort` |
| baseline | `mmlu_1050` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1051` | `mcq` | true | `C` | `C. 3` |
| baseline | `mmlu_1052` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1053` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1054` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1055` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_1056` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1057` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1058` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1059` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1060` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1061` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1062` | `mcq` | false | `A` | `D. I and II only` |
| baseline | `mmlu_1063` | `mcq` | false | `B` | `C. I and II only` |
| baseline | `mmlu_1064` | `mcq` | false | `B` | `C. 5/3` |
| baseline | `mmlu_1065` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1066` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1067` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1068` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1069` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1070` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1071` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1072` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1073` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1074` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1075` | `mcq` | false | `D` | `C. 38%` |
| baseline | `mmlu_1076` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1077` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1078` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1079` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1080` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1081` | `mcq` | false | `D` | `C. 1/2` |
| baseline | `mmlu_1082` | `mcq` | false | `A` | `D. I and II only` |
| baseline | `mmlu_1083` | `mcq` | false | `B` | `C. I and II only` |
| baseline | `mmlu_1084` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1085` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1086` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1087` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1088` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1089` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1090` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1091` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1092` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1093` | `mcq` | true | `D` | `D. I and III` |
| baseline | `mmlu_1094` | `mcq` | true | `C` | `C. 1.6 microseconds` |
| baseline | `mmlu_1095` | `mcq` | true | `D` | `D. 99.80%` |
| baseline | `mmlu_1096` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1097` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1098` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1099` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1100` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1101` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1102` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1103` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1104` | `mcq` | false | `C` | `D. III only` |
| baseline | `mmlu_1105` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1106` | `mcq` | true | `D` | `D. 45` |
| baseline | `mmlu_1107` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1108` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1109` | `mcq` | false | `B` | `10` |
| baseline | `mmlu_1110` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1111` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_1112` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_1113` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1114` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1115` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1116` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1117` | `mcq` | false | `D` | `C. Four` |
| baseline | `mmlu_1118` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_1119` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1120` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1121` | `mcq` | true | `D` | `D. III only` |
| baseline | `mmlu_1122` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1123` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1125` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1126` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1127` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1128` | `mcq` | true | `B` | `B. For 3, 5, 7, and 11 only` |
| baseline | `mmlu_1129` | `mcq` | false | `C` | `D. 4` |
| baseline | `mmlu_1130` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1131` | `mcq` | false | `D` | `B. (x^2 + y^2 + z^2 + 8)^2 = 36(x^2 + z^2)` |
| baseline | `mmlu_1132` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1133` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1134` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1135` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1136` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1137` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1138` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1139` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1140` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1141` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1142` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1143` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1144` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1145` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1146` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1147` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1148` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1149` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1150` | `mcq` | false | `A` | `C. 8` |
| baseline | `mmlu_1151` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1152` | `mcq` | false | `B` | `5` |
| baseline | `mmlu_1153` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1154` | `mcq` | true | `C` | `C. 4` |
| baseline | `mmlu_1155` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1156` | `mcq` | true | `B` | `B. One` |
| baseline | `mmlu_1157` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1158` | `mcq` | false | `A` | `D. Both (a) and (b).` |
| baseline | `mmlu_1159` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1160` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1161` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1162` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1163` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1164` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1165` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1166` | `mcq` | true | `D` | `D. -16/(3π) cm/min` |
| baseline | `mmlu_1167` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1168` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1169` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_1170` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1171` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1172` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1173` | `mcq` | true | `C` | `C. 0` |
| baseline | `mmlu_1174` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1175` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1176` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1177` | `mcq` | true | `B` | `B. 30` |
| baseline | `mmlu_1178` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_1179` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1180` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1181` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1182` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1183` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1184` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1185` | `mcq` | true | `C` | `C. a^3 = e` |
| baseline | `mmlu_1186` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1187` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1188` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1189` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1190` | `mcq` | false | `D` | `A. 1` |
| baseline | `mmlu_1191` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1192` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1193` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1194` | `mcq` | false | `D` | `C. 28` |
| baseline | `mmlu_1195` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1196` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1197` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1198` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1199` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1200` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1201` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1202` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1203` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1204` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1205` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1206` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1207` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1208` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1209` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1210` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1211` | `mcq` | false | `B` | `D. Not enough information given.` |
| baseline | `mmlu_1212` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1213` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1214` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1215` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1216` | `mcq` | false | `C` | `B. I, II, and III` |
| baseline | `mmlu_1217` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1218` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1219` | `mcq` | true | `A` | `A. Osmosis` |
| baseline | `mmlu_1220` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1221` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1222` | `mcq` | false | `C` | `D. 912 Hz` |
| baseline | `mmlu_1223` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1224` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1225` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1226` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1227` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1228` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1229` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1230` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1231` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1232` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1233` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1234` | `mcq` | false | `D` | `C. Calcium-troponin interaction` |
| baseline | `mmlu_1235` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1236` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1237` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1238` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1239` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1240` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1241` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1242` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1243` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1244` | `mcq` | true | `B` | `B. Maintains alveoli in an open state` |
| baseline | `mmlu_1245` | `mcq` | false | `C` | `D. 156g` |
| baseline | `mmlu_1246` | `mcq` | true | `D` | `D. Replenish fluids with filtered water.` |
| baseline | `mmlu_1247` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1248` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1249` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1250` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1251` | `mcq` | true | `B` | `B. Insulin` |
| baseline | `mmlu_1252` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1253` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1254` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1255` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1256` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1257` | `mcq` | true | `D` | `D. I and IV` |
| baseline | `mmlu_1258` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1259` | `mcq` | false | `C` | `D. I, II, and III` |
| baseline | `mmlu_1260` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1261` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1262` | `mcq` | true | `B` | `B. An 86-year old male mayor who is revered in the community.` |
| baseline | `mmlu_1263` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1264` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1265` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1266` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1267` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1268` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1269` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1270` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1271` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1272` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1273` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1274` | `mcq` | false | `C` | `B. Repolarization` |
| baseline | `mmlu_1275` | `mcq` | true | `A` | `A. yields 8 molecules of acetyl-CoA and some ATP and water.` |
| baseline | `mmlu_1276` | `mcq` | true | `D` | `D. Production of a larger, likely dysfunctional protein` |
| baseline | `mmlu_1277` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1278` | `mcq` | false | `B` | `D. I and III and IV only` |
| baseline | `mmlu_1279` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1280` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1281` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1282` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1283` | `mcq` | true | `A` | `A. deoxyribonucleic acid.` |
| baseline | `mmlu_1284` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1285` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1286` | `mcq` | true | `B` | `B. Phallic` |
| baseline | `mmlu_1287` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1288` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1289` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1290` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1291` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1292` | `mcq` | false | `C` | `D. No effect` |
| baseline | `mmlu_1293` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1294` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1295` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1296` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1298` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1299` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1300` | `mcq` | true | `C` | `C. cytoplasm.` |
| baseline | `mmlu_1301` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1302` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1303` | `mcq` | true | `D` | `D. phosphofructokinase.` |
| baseline | `mmlu_1304` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1305` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1306` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1307` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1308` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1309` | `mcq` | true | `A` | `A. elevating the pH and buffering capacity of the extracellular fluid allowing a faster efflux of hydrogen ions from mus` |
| baseline | `mmlu_1310` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1311` | `mcq` | true | `C` | `C. Carnosine` |
| baseline | `mmlu_1312` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1313` | `mcq` | false | `A` | `C. Microculture` |
| baseline | `mmlu_1314` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1315` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1316` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1317` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1318` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1319` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1320` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1321` | `mcq` | false | `A` | `C. Active transport` |
| baseline | `mmlu_1322` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1323` | `mcq` | true | `C` | `C. I and III only` |
| baseline | `mmlu_1324` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1325` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1326` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1327` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1328` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1329` | `mcq` | false | `A` | `D. I and II` |
| baseline | `mmlu_1330` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1331` | `mcq` | true | `A` | `A. Thymine` |
| baseline | `mmlu_1332` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1333` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1334` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1335` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1336` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1337` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1338` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1339` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1340` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1341` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1342` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1343` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1344` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1345` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1346` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1347` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1348` | `mcq` | true | `A` | `A. ATP.` |
| baseline | `mmlu_1349` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1350` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1351` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1352` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1353` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1354` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1355` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1356` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1357` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1358` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1359` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1360` | `mcq` | false | `D` | `C. 5 m/s` |
| baseline | `mmlu_1361` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1362` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1363` | `mcq` | false | `D` | `B. a recessive allele on the X chromosome.` |
| baseline | `mmlu_1364` | `mcq` | false | `A` | `C. frequently falls by 1 - 3 mM.` |
| baseline | `mmlu_1365` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1366` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1367` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1368` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1369` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1370` | `mcq` | false | `C` | `B. 550 nm` |
| baseline | `mmlu_1371` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1372` | `mcq` | false | `A` | `B. a helium-neon laser` |
| baseline | `mmlu_1373` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1374` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1375` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1376` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1377` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1378` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1379` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1380` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1381` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1382` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1383` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1384` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1385` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1386` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1387` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1388` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1389` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1390` | `mcq` | false | `D` | `C. 6` |
| baseline | `mmlu_1391` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1392` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1393` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1394` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1395` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1396` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1397` | `mcq` | false | `B` | `A. deflected in the +x-direction` |
| baseline | `mmlu_1398` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1399` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1400` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1401` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1402` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1403` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1404` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1405` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1406` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1407` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1408` | `mcq` | false | `D` | `C. 8` |
| baseline | `mmlu_1409` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1410` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1411` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1412` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1413` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1414` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1415` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1416` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1417` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1418` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1419` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1420` | `mcq` | false | `A` | `B. a helium-neon laser` |
| baseline | `mmlu_1421` | `mcq` | true | `A` | `A. real` |
| baseline | `mmlu_1422` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1423` | `mcq` | false | `C` | `B. B is perpendicular to the surface.` |
| baseline | `mmlu_1424` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1425` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1426` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1427` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1428` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1429` | `mcq` | true | `D` | `D. None` |
| baseline | `mmlu_1430` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1431` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1432` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_1433` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1434` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1435` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1436` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1437` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1438` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1439` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1440` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1441` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1442` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1443` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1444` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1445` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1446` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1447` | `mcq` | false | `D` | `C. 4k` |
| baseline | `mmlu_1448` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1449` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1450` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1451` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1452` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1453` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1454` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1455` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1456` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1457` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1459` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1460` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1461` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1462` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1463` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1464` | `mcq` | true | `D` | `D. 19.6 m` |
| baseline | `mmlu_1465` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1466` | `mcq` | false | `C` | `B. 550 nm` |
| baseline | `mmlu_1467` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1468` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1469` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1470` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1471` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1472` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1473` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1474` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1475` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1476` | `mcq` | true | `B` | `B. Buffer-Overrun` |
| baseline | `mmlu_1477` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1478` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1479` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1480` | `mcq` | true | `B` | `B. Authenticated` |
| baseline | `mmlu_1481` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1482` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1483` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1484` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1485` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1486` | `mcq` | true | `B` | `B. Access Point` |
| baseline | `mmlu_1487` | `mcq` | false | `B` | `C. 64` |
| baseline | `mmlu_1488` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1489` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1490` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1491` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1492` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1493` | `mcq` | false | `D` | `B. False, False` |
| baseline | `mmlu_1494` | `mcq` | true | `C` | `C. Key exchange` |
| baseline | `mmlu_1495` | `mcq` | true | `A` | `A. Silk Road` |
| baseline | `mmlu_1496` | `mcq` | true | `C` | `C. Dark web` |
| baseline | `mmlu_1497` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1498` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1499` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1500` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1501` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1502` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1503` | `mcq` | true | `C` | `C. True, False` |
| baseline | `mmlu_1504` | `mcq` | true | `C` | `C. Session layer` |
| baseline | `mmlu_1505` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1506` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1507` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1508` | `mcq` | true | `D` | `D. Network or transport layer` |
| baseline | `mmlu_1509` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1510` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1511` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1512` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1513` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1514` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1515` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1516` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1517` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1518` | `mcq` | false | `C` | `CBF` |
| baseline | `mmlu_1519` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1520` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1521` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1522` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1523` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1524` | `mcq` | true | `B` | `B. 56` |
| baseline | `mmlu_1525` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1526` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1527` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1528` | `mcq` | true | `B` | `B. Application layer` |
| baseline | `mmlu_1529` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1530` | `mcq` | true | `D` | `D. Tor browser` |
| baseline | `mmlu_1531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1532` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1533` | `mcq` | false | `C` | `B. No, there is always a CPA attack on this system.` |
| baseline | `mmlu_1534` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1535` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1536` | `mcq` | false | `C` | `D. False, True` |
| baseline | `mmlu_1537` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1538` | `mcq` | false | `A` | `A/B/C` |
| baseline | `mmlu_1539` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1540` | `mcq` | false | `B` | `A. No, I cannot compute the key.` |
| baseline | `mmlu_1541` | `mcq` | false | `A` | `B. False, False` |
| baseline | `mmlu_1542` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1543` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1544` | `mcq` | true | `A` | `A. Only once` |
| baseline | `mmlu_1545` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1546` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1547` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1548` | `mcq` | true | `C` | `C. Buffer-overflow` |
| baseline | `mmlu_1549` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1550` | `mcq` | true | `C` | `C. Base Transceiver Station` |
| baseline | `mmlu_1551` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1552` | `mcq` | true | `C` | `C. TKIP` |
| baseline | `mmlu_1553` | `mcq` | true | `A` | `A. buffer` |
| baseline | `mmlu_1554` | `mcq` | true | `C` | `C. WPS` |
| baseline | `mmlu_1555` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1556` | `mcq` | true | `A` | `A. WEP` |
| baseline | `mmlu_1557` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1558` | `mcq` | true | `A` | `A. Local variables` |
| baseline | `mmlu_1559` | `mcq` | false | `D` | `B. No, there are no ciphers with perfect secrecy.` |
| baseline | `mmlu_1560` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1561` | `mcq` | true | `C` | `C. Receiver site` |
| baseline | `mmlu_1562` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1563` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1564` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1565` | `mcq` | false | `B` | `C. True, False` |
| baseline | `mmlu_1566` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1567` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1568` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1569` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1570` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1571` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1572` | `mcq` | false | `B` | `D. All of these.` |
| baseline | `mmlu_1573` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1574` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1575` | `mcq` | true | `A` | `A. Changes` |
| baseline | `mmlu_1576` | `mcq` | true | `D` | `D. Violet` |
| baseline | `mmlu_1577` | `mcq` | true | `D` | `D. All of these.` |
| baseline | `mmlu_1578` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1579` | `mcq` | true | `B` | `B. ordered` |
| baseline | `mmlu_1580` | `mcq` | true | `D` | `D. energy` |
| baseline | `mmlu_1581` | `mcq` | true | `B` | `B. opposite` |
| baseline | `mmlu_1582` | `mcq` | true | `C` | `C. radiation` |
| baseline | `mmlu_1583` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1584` | `mcq` | true | `A` | `A. increase.` |
| baseline | `mmlu_1585` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1586` | `mcq` | true | `A` | `A. less.` |
| baseline | `mmlu_1587` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1588` | `mcq` | false | `B` | `D. All of these` |
| baseline | `mmlu_1589` | `mcq` | false | `D` | `A. volume` |
| baseline | `mmlu_1590` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1591` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1592` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1593` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1594` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1595` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1596` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1597` | `mcq` | false | `D` | `B. 2 minutes.` |
| baseline | `mmlu_1598` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1599` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1600` | `mcq` | true | `C` | `C. Both` |
| baseline | `mmlu_1601` | `mcq` | false | `B` | `A. shorter` |
| baseline | `mmlu_1602` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1603` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1604` | `mcq` | false | `D` | `A. equals mass moving at the speed of light squared.` |
| baseline | `mmlu_1605` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1606` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1607` | `mcq` | false | `A` | `B. Decreases` |
| baseline | `mmlu_1608` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1609` | `mcq` | true | `D` | `D. frequency` |
| baseline | `mmlu_1610` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1611` | `mcq` | false | `C` | `D. Need more information.` |
| baseline | `mmlu_1612` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1613` | `mcq` | true | `B` | `B. hot day` |
| baseline | `mmlu_1614` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1615` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1616` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1617` | `mcq` | false | `C` | `B. Less` |
| baseline | `mmlu_1618` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1619` | `mcq` | false | `A` | `C. Both of these` |
| baseline | `mmlu_1620` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1621` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1622` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1623` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1624` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1625` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1626` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1627` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1628` | `mcq` | false | `B` | `C. 8 Hz` |
| baseline | `mmlu_1629` | `mcq` | true | `D` | `D. amplitude` |
| baseline | `mmlu_1630` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1631` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1632` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1633` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1634` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1635` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1636` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1637` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1638` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_1639` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1640` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1641` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1642` | `mcq` | false | `A` | `B. less dense` |
| baseline | `mmlu_1643` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1644` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1645` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1646` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1647` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1648` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1649` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1650` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1651` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1652` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1653` | `mcq` | false | `A` | `D. No think` |
| baseline | `mmlu_1654` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1655` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1656` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1657` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1658` | `mcq` | true | `C` | `C. waves` |
| baseline | `mmlu_1659` | `mcq` | true | `A` | `A. high temperatures` |
| baseline | `mmlu_1660` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1661` | `mcq` | true | `B` | `B. Decreases.` |
| baseline | `mmlu_1662` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1663` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1664` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1665` | `mcq` | false | `C` | `B. violet light.` |
| baseline | `mmlu_1666` | `mcq` | false | `B` | `D. may be greater or less than mg depending on the speed of the ball` |
| baseline | `mmlu_1667` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1668` | `mcq` | true | `A` | `A. lined up with the Sun` |
| baseline | `mmlu_1669` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1670` | `mcq` | true | `A` | `A. lower` |
| baseline | `mmlu_1671` | `mcq` | false | `C` | `D. Violet` |
| baseline | `mmlu_1672` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1673` | `mcq` | false | `D` | `A. Magnesium-22` |
| baseline | `mmlu_1674` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1675` | `mcq` | true | `A` | `A. hydrogen` |
| baseline | `mmlu_1676` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1677` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1678` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1679` | `mcq` | true | `C` | `C. radiation.` |
| baseline | `mmlu_1680` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1681` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1682` | `mcq` | true | `A` | `A.干涉` |
| baseline | `mmlu_1683` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1684` | `mcq` | true | `B` | `B. period` |
| baseline | `mmlu_1685` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1686` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1687` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1689` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1690` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1691` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1692` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1693` | `mcq` | true | `B` | `B. 14 m/s` |
| baseline | `mmlu_1694` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1695` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1696` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1697` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1698` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1699` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1700` | `mcq` | false | `C` | `B. -273°C` |
| baseline | `mmlu_1701` | `mcq` | true | `A` | `A. speed and direction` |
| baseline | `mmlu_1702` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1703` | `mcq` | true | `B` | `B. Decreases` |
| baseline | `mmlu_1704` | `mcq` | true | `C` | `C. blue` |
| baseline | `mmlu_1705` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1706` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1707` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1708` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1709` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1710` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1711` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1712` | `mcq` | false | `C` | `B. decrease` |
| baseline | `mmlu_1713` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1714` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1715` | `mcq` | false | `D` | `C. reflection` |
| baseline | `mmlu_1716` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1717` | `mcq` | false | `B` | `D. Higher than 30°C` |
| baseline | `mmlu_1718` | `mcq` | false | `B` | `A. one-quarter.` |
| baseline | `mmlu_1719` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1720` | `mcq` | true | `D` | `D. More information is needed` |
| baseline | `mmlu_1721` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1722` | `mcq` | true | `A` | `A. also increases.` |
| baseline | `mmlu_1723` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1724` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1725` | `mcq` | true | `B` | `B. Sound` |
| baseline | `mmlu_1726` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1727` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1728` | `mcq` | false | `A` | `B. Decreases.` |
| baseline | `mmlu_1729` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1730` | `mcq` | false | `B` | `C. year` |
| baseline | `mmlu_1731` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1732` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1733` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1734` | `mcq` | true | `B` | `B.干涉` |
| baseline | `mmlu_1735` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1736` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1737` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1738` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1739` | `mcq` | false | `D` | `B. energy` |
| baseline | `mmlu_1740` | `mcq` | true | `C` | `C. Both of these` |
| baseline | `mmlu_1741` | `mcq` | false | `A` | `C. Both` |
| baseline | `mmlu_1742` | `mcq` | true | `B` | `B. 26` |
| baseline | `mmlu_1743` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1744` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1745` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1746` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1747` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1748` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1749` | `mcq` | false | `D` | `B. 500 J` |
| baseline | `mmlu_1750` | `mcq` | true | `D` | `D. 32q.` |
| baseline | `mmlu_1751` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1752` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1753` | `mcq` | true | `B` | `B. frequency` |
| baseline | `mmlu_1754` | `mcq` | true | `B` | `B. Decreases` |
| baseline | `mmlu_1755` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1756` | `mcq` | false | `A` | `C. Both of these` |
| baseline | `mmlu_1757` | `mcq` | false | `A` | `B. minus 1` |
| baseline | `mmlu_1758` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1759` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1760` | `mcq` | true | `A` | `A. shorter in the direction of travel.` |
| baseline | `mmlu_1761` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1762` | `mcq` | false | `A` | `D. Cannot say unless the speed of throw is given.` |
| baseline | `mmlu_1763` | `mcq` | true | `A` | `A. atmosphere` |
| baseline | `mmlu_1764` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1765` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1766` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1767` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1769` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1770` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1771` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1772` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1773` | `mcq` | false | `A` | `B. generates electricity directly` |
| baseline | `mmlu_1774` | `mcq` | false | `B` | `C. Both` |
| baseline | `mmlu_1775` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1776` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1777` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1778` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1779` | `mcq` | true | `B` | `B. twice as much` |
| baseline | `mmlu_1780` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1781` | `mcq` | false | `C` | `D. All of these` |
| baseline | `mmlu_1782` | `mcq` | true | `C` | `C.adioactivity` |
| baseline | `mmlu_1783` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1784` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1785` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1786` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1787` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1788` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1789` | `mcq` | true | `B` | `B._frequency` |
| baseline | `mmlu_1790` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1791` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1792` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1793` | `mcq` | false | `B` | `A. near the rotational axis` |
| baseline | `mmlu_1794` | `mcq` | false | `C` | `A. greatly increases` |
| baseline | `mmlu_1795` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1796` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1797` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1798` | `mcq` | false | `B` | `C. Both` |
| baseline | `mmlu_1799` | `mcq` | false | `B` | `A. compresses with speed.` |
| baseline | `mmlu_1800` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1801` | `mcq` | true | `B` | `B. Decreases.` |
| baseline | `mmlu_1802` | `mcq` | false | `C` | `D. 0.0625 g` |
| baseline | `mmlu_1803` | `mcq` | true | `B` | `B. decreased atmospheric pressure` |
| baseline | `mmlu_1804` | `mcq` | true | `A` | `A. tension.` |
| baseline | `mmlu_1805` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1806` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1807` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1808` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1809` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1810` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1811` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1812` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1813` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1814` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1815` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1816` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1817` | `mcq` | true | `D` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1818` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1819` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1820` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1821` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1822` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1823` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1824` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1825` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1827` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1828` | `mcq` | false | `A` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1829` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1830` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1831` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1832` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1833` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1834` | `mcq` | false | `D` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1835` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1836` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1837` | `mcq` | false | `D` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1838` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1839` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1840` | `mcq` | false | `A` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1841` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1842` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1843` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1844` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1845` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1846` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1847` | `mcq` | false | `B` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1848` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1849` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1850` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1851` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1852` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1853` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1854` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1855` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1856` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1857` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1858` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1859` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1860` | `mcq` | false | `C` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1861` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1862` | `mcq` | true | `D` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1863` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1864` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1865` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1866` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1867` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1868` | `mcq` | false | `C` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1869` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1870` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1871` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1872` | `mcq` | false | `C` | `B. The largest 2` |
| baseline | `mmlu_1873` | `mcq` | false | `A` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1874` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1875` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1876` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1877` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1878` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1879` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1880` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1881` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1882` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1883` | `mcq` | true | `A` | `A. Censored` |
| baseline | `mmlu_1884` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1885` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1886` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1887` | `mcq` | false | `D` | `A. The RSS for the whole sample` |
| baseline | `mmlu_1888` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1889` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1890` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1891` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1892` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1893` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1894` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1895` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1896` | `mcq` | false | `D` | `B. (i) and (iii) only` |
| baseline | `mmlu_1897` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1898` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1899` | `mcq` | true | `C` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1900` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1901` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1902` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1903` | `mcq` | false | `B` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1904` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1905` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1906` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1907` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1908` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1909` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1910` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1911` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1912` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1913` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_1914` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1915` | `mcq` | false | `C` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1916` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1917` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1918` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1919` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1920` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1921` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1922` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1923` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1924` | `mcq` | false | `C` | `D. State box.` |
| baseline | `mmlu_1925` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1926` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1927` | `mcq` | true | `D` | `D. Both A and B` |
| baseline | `mmlu_1928` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1929` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1930` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1931` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1932` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_1933` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1934` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1935` | `mcq` | false | `C` | `B. 6` |
| baseline | `mmlu_1936` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1937` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1938` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1939` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1940` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1941` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1942` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1943` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1944` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1945` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1946` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1947` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1948` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1949` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1950` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1951` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1952` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1953` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1954` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1955` | `mcq` | false | `A` | `C. 50` |
| baseline | `mmlu_1956` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1957` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1958` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1959` | `mcq` | true | `B` | `B. 250 Hz.` |
| baseline | `mmlu_1960` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1961` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1962` | `mcq` | false | `A` | `B. 4` |
| baseline | `mmlu_1963` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1964` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1965` | `mcq` | true | `B` | `B. frequency modulation.` |
| baseline | `mmlu_1966` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1967` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1968` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1969` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1970` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1971` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1972` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1973` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1974` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1975` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1976` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1977` | `mcq` | true | `C` | `C. Amplitude Modulation` |
| baseline | `mmlu_1978` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1979` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1980` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1981` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1982` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1983` | `mcq` | false | `A` | `B. Sulphur.` |
| baseline | `mmlu_1984` | `mcq` | true | `D` | `D. All the above` |
| baseline | `mmlu_1985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1986` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1987` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1988` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1989` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1990` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1991` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1992` | `mcq` | false | `C` | `A. LED` |
| baseline | `mmlu_1993` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1994` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1995` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1996` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1997` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1998` | `mcq` | true | `D` | `D. All of these.` |
| baseline | `mmlu_1999` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2000` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2001` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2002` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2003` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2004` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2005` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2006` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2007` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2008` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2009` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2010` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2011` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2012` | `mcq` | false | `B` | `A. high.` |
| baseline | `mmlu_2013` | `mcq` | false | `A` | `B. upper surface of the conductor.` |
| baseline | `mmlu_2014` | `mcq` | true | `C` | `C. 2` |
| baseline | `mmlu_2015` | `mcq` | false | `D` | `B. Microphone` |
| baseline | `mmlu_2016` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2017` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2018` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2019` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2020` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2021` | `mcq` | true | `B` | `B. clean.` |
| baseline | `mmlu_2022` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2023` | `mcq` | true | `D` | `D. Flux.` |
| baseline | `mmlu_2024` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2025` | `mcq` | false | `D` | `C. RLC circuit.` |
| baseline | `mmlu_2026` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2027` | `mcq` | true | `B` | `B. Analog quantity` |
| baseline | `mmlu_2028` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2029` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2030` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2031` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2032` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2033` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2034` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2035` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2036` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2037` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2038` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2039` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2040` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2041` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2042` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2043` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2044` | `mcq` | true | `B` | `B. non linearly.` |
| baseline | `mmlu_2045` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2046` | `mcq` | true | `B` | `B. 80π coulombs.` |
| baseline | `mmlu_2047` | `mcq` | false | `A` | `B. MSB, Most Significant Bit` |
| baseline | `mmlu_2048` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2049` | `mcq` | false | `B` | `A. 3.33% .` |
| baseline | `mmlu_2050` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2051` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2052` | `mcq` | true | `C` | `C. both A and B.` |
| baseline | `mmlu_2053` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2054` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2055` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2056` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2057` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2058` | `mcq` | false | `A` | `D. No think` |
| baseline | `mmlu_2059` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2060` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2061` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2062` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2063` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2064` | `mcq` | false | `A` | `D. none of above.` |
| baseline | `mmlu_2065` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2066` | `mcq` | true | `C` | `C. 8` |
| baseline | `mmlu_2067` | `mcq` | true | `D` | `D. 5` |
| baseline | `mmlu_2068` | `mcq` | false | `B` | `C. 6` |
| baseline | `mmlu_2069` | `mcq` | true | `B` | `B. 4t = 112; $28` |
| baseline | `mmlu_2070` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2071` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2072` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2073` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2074` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2075` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2076` | `mcq` | false | `D` | `C. 1` |
| baseline | `mmlu_2077` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2078` | `mcq` | true | `A` | `A. 6` |
| baseline | `mmlu_2079` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2080` | `mcq` | true | `B` | `B. 14 minutes` |
| baseline | `mmlu_2081` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2082` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2083` | `mcq` | false | `D` | `C. 50` |
| baseline | `mmlu_2084` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2085` | `mcq` | false | `C` | `A. -12` |
| baseline | `mmlu_2086` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2087` | `mcq` | true | `A` | `A. -7` |
| baseline | `mmlu_2088` | `mcq` | false | `C` | `B. 63` |
| baseline | `mmlu_2089` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2090` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2091` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2092` | `mcq` | false | `D` | `C. 578` |
| baseline | `mmlu_2093` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2094` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2095` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2096` | `mcq` | false | `B` | `C. 16 remainder 5` |
| baseline | `mmlu_2097` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2098` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2099` | `mcq` | false | `D` | `B. 770 parts` |
| baseline | `mmlu_2100` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2101` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2102` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2103` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2104` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_2105` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2106` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2107` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2108` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2109` | `mcq` | false | `D` | `A. 15, 17` |
| baseline | `mmlu_2110` | `mcq` | true | `B` | `B. 12 cans` |
| baseline | `mmlu_2111` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2112` | `mcq` | false | `C` | `B. 11` |
| baseline | `mmlu_2113` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2114` | `mcq` | true | `D` | `D. -45` |
| baseline | `mmlu_2115` | `mcq` | false | `A` | `B. 40 birds` |
| baseline | `mmlu_2116` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2117` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2118` | `mcq` | true | `A` | `A. 120 miles` |
| baseline | `mmlu_2119` | `mcq` | true | `B` | `B. divide both sides by 6` |
| baseline | `mmlu_2120` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2121` | `mcq` | false | `D` | `C. 84 - t = 11; 73°F` |
| baseline | `mmlu_2122` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2123` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2124` | `mcq` | true | `B` | `B. 20` |
| baseline | `mmlu_2125` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2126` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_2127` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2128` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2129` | `mcq` | false | `D` | `A. -4` |
| baseline | `mmlu_2130` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2131` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2132` | `mcq` | false | `A` | `C. 48` |
| baseline | `mmlu_2133` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2134` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2135` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2136` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2137` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2138` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2139` | `mcq` | true | `B` | `B. $6,049` |
| baseline | `mmlu_2140` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2141` | `mcq` | true | `A` | `A. $2.82` |
| baseline | `mmlu_2142` | `mcq` | true | `D` | `D. 5 over 6` |
| baseline | `mmlu_2143` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2144` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2145` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2146` | `mcq` | false | `A` | `C. -1` |
| baseline | `mmlu_2147` | `mcq` | false | `D` | `B. 4` |
| baseline | `mmlu_2148` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2149` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2150` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2151` | `mcq` | false | `A` | `B. 8.9` |
| baseline | `mmlu_2152` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2153` | `mcq` | true | `B` | `B. 66.5 seconds` |
| baseline | `mmlu_2154` | `mcq` | false | `B` | `D. 96` |
| baseline | `mmlu_2155` | `mcq` | true | `C` | `C. 180` |
| baseline | `mmlu_2156` | `mcq` | false | `A` | `C. 4:01` |
| baseline | `mmlu_2157` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2158` | `mcq` | true | `A` | `A. 48` |
| baseline | `mmlu_2159` | `mcq` | false | `C` | `B. 21` |
| baseline | `mmlu_2160` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2161` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2162` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2163` | `mcq` | false | `A` | `C. 2.61` |
| baseline | `mmlu_2164` | `mcq` | false | `C` | `B. 3.6` |
| baseline | `mmlu_2165` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2166` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2167` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2168` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2169` | `mcq` | false | `A` | `B. 2,400` |
| baseline | `mmlu_2170` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2171` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2172` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2173` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2174` | `mcq` | true | `B` | `B. subtract 20 from 180` |
| baseline | `mmlu_2175` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2176` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2177` | `mcq` | false | `B` | `C. 72` |
| baseline | `mmlu_2178` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2179` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2180` | `mcq` | false | `D` | `A. 6` |
| baseline | `mmlu_2181` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2182` | `mcq` | true | `B` | `B. 2.5` |
| baseline | `mmlu_2183` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2184` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2185` | `mcq` | false | `B` | `A. $1.40` |
| baseline | `mmlu_2186` | `mcq` | false | `A` | `C. 1,000` |
| baseline | `mmlu_2187` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2188` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2189` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2190` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2191` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2192` | `mcq` | true | `C` | `C. 9` |
| baseline | `mmlu_2193` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2194` | `mcq` | false | `D` | `C. 19,612` |
| baseline | `mmlu_2195` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2196` | `mcq` | false | `D` | `C. 72 km/h` |
| baseline | `mmlu_2197` | `mcq` | true | `B` | `B. 25 meters` |
| baseline | `mmlu_2198` | `mcq` | true | `C` | `C. 130 minutes` |
| baseline | `mmlu_2199` | `mcq` | false | `C` | `B. 144` |
| baseline | `mmlu_2200` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2201` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2202` | `mcq` | false | `D` | `C. 17` |
| baseline | `mmlu_2203` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2204` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2205` | `mcq` | true | `D` | `D. 120` |
| baseline | `mmlu_2206` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2207` | `mcq` | false | `D` | `B. 3` |
| baseline | `mmlu_2208` | `mcq` | true | `A` | `A. 3:58 p.m.` |
| baseline | `mmlu_2209` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2210` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2211` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2212` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2213` | `mcq` | false | `C` | `B. 17` |
| baseline | `mmlu_2214` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2215` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2216` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2217` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2218` | `mcq` | false | `C` | `B. conducting the survey at all shoe stores` |
| baseline | `mmlu_2219` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2220` | `mcq` | false | `D` | `C. 24 students` |
| baseline | `mmlu_2221` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2222` | `mcq` | false | `A` | `B. 9 stickers` |
| baseline | `mmlu_2223` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2224` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2225` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2226` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2227` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2228` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2229` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2230` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2231` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2232` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2233` | `mcq` | false | `C` | `B. 4 days` |
| baseline | `mmlu_2234` | `mcq` | true | `C` | `C. 18` |
| baseline | `mmlu_2235` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2236` | `mcq` | false | `A` | `B. -7` |
| baseline | `mmlu_2237` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2238` | `mcq` | false | `C` | `D. 79` |
| baseline | `mmlu_2239` | `mcq` | false | `A` | `C. -13` |
| baseline | `mmlu_2240` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2241` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2242` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2243` | `mcq` | false | `B` | `D. 20 over 28` |
| baseline | `mmlu_2244` | `mcq` | true | `A` | `A. -63` |
| baseline | `mmlu_2245` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2246` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2247` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2248` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2249` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2250` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2251` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2252` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2253` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_2254` | `mcq` | true | `B` | `B. 15` |
| baseline | `mmlu_2255` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2256` | `mcq` | true | `B` | `B. -49°C` |
| baseline | `mmlu_2257` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2258` | `mcq` | false | `D` | `B. 27` |
| baseline | `mmlu_2259` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2260` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2261` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2262` | `mcq` | true | `B` | `B. 30/5` |
| baseline | `mmlu_2263` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2264` | `mcq` | true | `D` | `D. -1.1` |
| baseline | `mmlu_2265` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2266` | `mcq` | false | `C` | `B. 77` |
| baseline | `mmlu_2267` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_2268` | `mcq` | true | `B` | `B. 18` |
| baseline | `mmlu_2269` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2270` | `mcq` | false | `D` | `C. 4` |
| baseline | `mmlu_2271` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2272` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2273` | `mcq` | false | `D` | `B. 29` |
| baseline | `mmlu_2274` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2275` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2276` | `mcq` | false | `C` | `B. 12 cm` |
| baseline | `mmlu_2277` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2278` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2279` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2280` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_2281` | `mcq` | true | `B` | `B. $45` |
| baseline | `mmlu_2282` | `mcq` | false | `A` | `B. -7.4` |
| baseline | `mmlu_2283` | `mcq` | true | `B` | `B.ounces` |
| baseline | `mmlu_2284` | `mcq` | false | `C` | `B. $45 loss` |
| baseline | `mmlu_2285` | `mcq` | false | `B` | `C. 39` |
| baseline | `mmlu_2286` | `mcq` | false | `C` | `B. 2 subjects` |
| baseline | `mmlu_2287` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2288` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2289` | `mcq` | false | `C` | `B. 120` |
| baseline | `mmlu_2290` | `mcq` | true | `D` | `D. -36` |
| baseline | `mmlu_2291` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2292` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2293` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2294` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2295` | `mcq` | false | `B` | `C. 7:30 a.m.` |
| baseline | `mmlu_2296` | `mcq` | true | `C` | `C. $0.40` |
| baseline | `mmlu_2297` | `mcq` | false | `D` | `C. 2^3 • 3^2` |
| baseline | `mmlu_2298` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2299` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2300` | `mcq` | false | `D` | `B. 11 in.` |
| baseline | `mmlu_2301` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2302` | `mcq` | true | `A` | `A. 158` |
| baseline | `mmlu_2303` | `mcq` | false | `D` | `B. 1,801 R1` |
| baseline | `mmlu_2304` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2305` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2306` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2307` | `mcq` | true | `C` | `C. 5` |
| baseline | `mmlu_2308` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2309` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2310` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2311` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2312` | `mcq` | false | `A` | `B. 2 over 3` |
| baseline | `mmlu_2313` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2314` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2315` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2316` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2317` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2318` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2319` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2320` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2321` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2322` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2323` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2324` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2325` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2326` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2327` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2328` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2329` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2330` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2331` | `mcq` | false | `B` | `A. -85` |
| baseline | `mmlu_2332` | `mcq` | true | `C` | `C. 314` |
| baseline | `mmlu_2333` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2334` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2335` | `mcq` | true | `B` | `B. 260` |
| baseline | `mmlu_2336` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2337` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2338` | `mcq` | true | `D` | `D. 180` |
| baseline | `mmlu_2339` | `mcq` | true | `B` | `B. $117.30` |
| baseline | `mmlu_2340` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2341` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2342` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2343` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2344` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2345` | `mcq` | true | `C` | `C. 94` |
| baseline | `mmlu_2346` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2347` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2348` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2349` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2350` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2351` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2352` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2353` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2354` | `mcq` | false | `A` | `B. 2,400` |
| baseline | `mmlu_2355` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2356` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2357` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2358` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2359` | `mcq` | false | `D` | `B. 1.281` |
| baseline | `mmlu_2360` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2361` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2362` | `mcq` | true | `C` | `C. 400` |
| baseline | `mmlu_2363` | `mcq` | true | `B` | `B. 13` |
| baseline | `mmlu_2364` | `mcq` | true | `D` | `D. No mode` |
| baseline | `mmlu_2365` | `mcq` | true | `B` | `B. 136` |
| baseline | `mmlu_2366` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2367` | `mcq` | false | `C` | `B. $25.75` |
| baseline | `mmlu_2368` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2369` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2370` | `mcq` | true | `C` | `C. 4 over 9` |
| baseline | `mmlu_2371` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2372` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_2373` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2374` | `mcq` | false | `C` | `B. 495` |
| baseline | `mmlu_2375` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2376` | `mcq` | true | `D` | `D. 189 days` |
| baseline | `mmlu_2377` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2378` | `mcq` | true | `C` | `C. 9` |
| baseline | `mmlu_2379` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2380` | `mcq` | false | `C` | `B. 830` |
| baseline | `mmlu_2381` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2382` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2383` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2384` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2385` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2386` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2387` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2388` | `mcq` | true | `B` | `B. 43.3` |
| baseline | `mmlu_2389` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2390` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2391` | `mcq` | false | `A` | `B. 74.18 m` |
| baseline | `mmlu_2392` | `mcq` | false | `D` | `B. 5-Mar` |
| baseline | `mmlu_2393` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2394` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2395` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2396` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2397` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2398` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2399` | `mcq` | false | `D` | `C. 20` |
| baseline | `mmlu_2400` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2401` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2402` | `mcq` | true | `C` | `C. 2 m` |
| baseline | `mmlu_2403` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2404` | `mcq` | false | `B` | `C. 62` |
| baseline | `mmlu_2405` | `mcq` | false | `C` | `B. $19.88` |
| baseline | `mmlu_2406` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2407` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_2408` | `mcq` | false | `A` | `D. 2-Jan` |
| baseline | `mmlu_2409` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_2410` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2411` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2412` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2413` | `mcq` | false | `A` | `C. 110` |
| baseline | `mmlu_2414` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2415` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2416` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2417` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2418` | `mcq` | true | `C` | `C. 25 bouquets` |
| baseline | `mmlu_2419` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2420` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2421` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2422` | `mcq` | true | `B` | `B. 125` |
| baseline | `mmlu_2423` | `mcq` | true | `C` | `C. 48` |
| baseline | `mmlu_2424` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2425` | `mcq` | true | `C` | `C. 24` |
| baseline | `mmlu_2426` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2427` | `mcq` | false | `B` | `C. 8` |
| baseline | `mmlu_2428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2429` | `mcq` | false | `A` | `D. 1:09` |
| baseline | `mmlu_2430` | `mcq` | false | `C` | `D. 11 over 16` |
| baseline | `mmlu_2431` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2432` | `mcq` | true | `C` | `C. 11` |
| baseline | `mmlu_2433` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2434` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2435` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2436` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2437` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2438` | `mcq` | false | `D` | `C. 120` |
| baseline | `mmlu_2439` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2440` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2441` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2442` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2443` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2444` | `mcq` | false | `A` | `B. Tcd` |
| baseline | `mmlu_2445` | `mcq` | false | `C` | `A. Some large houses are bigger than some apartments.` |
| baseline | `mmlu_2446` | `mcq` | false | `A` | `B. Invalid. Counterexample when G is true and H is false.` |
| baseline | `mmlu_2447` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2448` | `mcq` | false | `D` | `B. Every house is bigger than every apartment.` |
| baseline | `mmlu_2449` | `mcq` | false | `D` | `B. Invalid. Counterexample when K is true and L is false.` |
| baseline | `mmlu_2450` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2451` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2452` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2453` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2454` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2455` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2456` | `mcq` | false | `C` | `B. Invalid. Counterexample when E and F are true and G is false.` |
| baseline | `mmlu_2457` | `mcq` | false | `D` | `B. Invalid. Counterexample when H and I are true and J is false.` |
| baseline | `mmlu_2458` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2459` | `mcq` | true | `D` | `D. None of the above` |
| baseline | `mmlu_2460` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2461` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2462` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2463` | `mcq` | true | `B` | `B. Invalid. Counterexample when P and Q are true and R is false.` |
| baseline | `mmlu_2464` | `mcq` | true | `D` | `D. Mmsi` |
| baseline | `mmlu_2465` | `mcq` | true | `B` | `B. No apartment is bigger than any large house.` |
| baseline | `mmlu_2466` | `mcq` | false | `C` | `B. Invalid. Counterexample when J is true and K and L are false` |
| baseline | `mmlu_2467` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2468` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2470` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2471` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2472` | `mcq` | false | `A` | `B. Invalid. Counterexample when E and G are true and F is false.` |
| baseline | `mmlu_2473` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2474` | `mcq` | false | `A` | `B. Invalid. Counterexample when M is true and O and N are false` |
| baseline | `mmlu_2475` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2476` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2477` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2478` | `mcq` | false | `C` | `B. Invalid. Counterexample when P and Q are true and R and S are false` |
| baseline | `mmlu_2479` | `mcq` | true | `B` | `B. Invalid. Counterexample when T is true and W and U are false` |
| baseline | `mmlu_2480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2481` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2482` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2483` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2484` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2485` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2486` | `mcq` | false | `A` | `B. Contradictory` |
| baseline | `mmlu_2487` | `mcq` | false | `A` | `B. Invalid. Counterexample when T and X are true and U, W, and Z are false.` |
| baseline | `mmlu_2488` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2489` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2490` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2491` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2492` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2493` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2494` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2495` | `mcq` | false | `D` | `A. ~Bje` |
| baseline | `mmlu_2496` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2497` | `mcq` | true | `B` | `B. The Bees win their first game.` |
| baseline | `mmlu_2498` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2499` | `mcq` | true | `B` | `B. Contradictory` |
| baseline | `mmlu_2500` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2501` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2502` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2503` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2505` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2506` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2507` | `mcq` | false | `D` | `A. Sx` |
| baseline | `mmlu_2508` | `mcq` | true | `D` | `D. Iwkj` |
| baseline | `mmlu_2509` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2510` | `mcq` | false | `A` | `B. Invalid. Counterexample when C is true and D is false.` |
| baseline | `mmlu_2511` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2512` | `mcq` | true | `A` | `A. Some cookies have oatmeal. If something's not being a cookie entails that it doesn't have chocolate chips, then this ` |
| baseline | `mmlu_2513` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2514` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2515` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2516` | `mcq` | false | `A` | `B. Invalid. Counterexample when O is true and P is false.` |
| baseline | `mmlu_2517` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2518` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2519` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2520` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2522` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2523` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2524` | `mcq` | false | `A` | `B. Invalid. Counterexample when A is true and B and C are false` |
| baseline | `mmlu_2525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2526` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2527` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2528` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2529` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2530` | `mcq` | false | `D` | `B. Invalid. Counterexample when Y and Z are true and Z is false.` |
| baseline | `mmlu_2531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2532` | `mcq` | false | `A` | `C. Every house is bigger than some apartment.` |
| baseline | `mmlu_2533` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2534` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2535` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2536` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2537` | `mcq` | true | `C` | `C. ~Mmis` |
| baseline | `mmlu_2538` | `mcq` | false | `D` | `B. Invalid. Counterexample when S and U are true and T is false.` |
| baseline | `mmlu_2539` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2540` | `mcq` | false | `D` | `B. Invalid. Counterexample when L, N, O, Q, and R are true and M and P are false` |
| baseline | `mmlu_2541` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2542` | `mcq` | false | `C` | `B. Contradictory` |
| baseline | `mmlu_2543` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2544` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2545` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2546` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2547` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2548` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2549` | `mcq` | true | `D` | `D. Gba` |
| baseline | `mmlu_2550` | `mcq` | true | `A` | `A. ~(∀x)(Lx ⊃ Rx)` |
| baseline | `mmlu_2551` | `mcq` | false | `A` | `B. Invalid. Counterexample when I and H are true and J and K are false` |
| baseline | `mmlu_2552` | `mcq` | false | `D` | `B. Contradictory` |
| baseline | `mmlu_2553` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2554` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2555` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2556` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2557` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2558` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2559` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2560` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2561` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2562` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2563` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2564` | `mcq` | false | `D` | `B. Invalid. Counterexample when L and M are true and K and N are false` |
| baseline | `mmlu_2565` | `mcq` | false | `D` | `B. Invalid. Counterexample when H is true and I and G are false` |
| baseline | `mmlu_2566` | `mcq` | false | `A` | `B. Invalid. Counterexample when M is true and N is false.` |
| baseline | `mmlu_2567` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2568` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2569` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2570` | `mcq` | false | `B` | `A. About $300` |
| baseline | `mmlu_2571` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2572` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2573` | `mcq` | false | `C` | `B. by 10 fold` |
| baseline | `mmlu_2574` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2575` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2576` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2578` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2579` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2580` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2581` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2582` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2583` | `mcq` | true | `B` | `B. 56%` |
| baseline | `mmlu_2584` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2585` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2586` | `mcq` | true | `C` | `C. 82%` |
| baseline | `mmlu_2587` | `mcq` | false | `C` | `A. About $3k` |
| baseline | `mmlu_2588` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2589` | `mcq` | false | `A` | `C. 65%` |
| baseline | `mmlu_2590` | `mcq` | false | `A` | `C. 64%` |
| baseline | `mmlu_2591` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2592` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2593` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2594` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2595` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2596` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2597` | `mcq` | false | `D` | `C. 50%` |
| baseline | `mmlu_2598` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2599` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2600` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2601` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2602` | `mcq` | false | `C` | `B. by 8 fold` |
| baseline | `mmlu_2603` | `mcq` | true | `D` | `D. 19` |
| baseline | `mmlu_2604` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2605` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2606` | `mcq` | false | `B` | `C. 55%` |
| baseline | `mmlu_2607` | `mcq` | false | `D` | `B. by 8 fold` |
| baseline | `mmlu_2608` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2609` | `mcq` | true | `B` | `B. 86%` |
| baseline | `mmlu_2610` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2611` | `mcq` | false | `C` | `A. Brazil` |
| baseline | `mmlu_2612` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2613` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2614` | `mcq` | false | `C` | `B. 14 million` |
| baseline | `mmlu_2615` | `mcq` | false | `A` | `B. 46%` |
| baseline | `mmlu_2616` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2617` | `mcq` | true | `C` | `C. 36%` |
| baseline | `mmlu_2618` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2619` | `mcq` | false | `B` | `C. 6%` |
| baseline | `mmlu_2620` | `mcq` | true | `B` | `B. supported mainly by cross-section, not time-series studies` |
| baseline | `mmlu_2621` | `mcq` | false | `B` | `A. 12 years` |
| baseline | `mmlu_2622` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2623` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2624` | `mcq` | true | `B` | `B. 75%` |
| baseline | `mmlu_2625` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2626` | `mcq` | false | `D` | `B. 25%` |
| baseline | `mmlu_2627` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2628` | `mcq` | false | `B` | `D. 65.20%` |
| baseline | `mmlu_2629` | `mcq` | false | `C` | `B. 30 million` |
| baseline | `mmlu_2630` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2631` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2632` | `mcq` | false | `C` | `B. 58%` |
| baseline | `mmlu_2633` | `mcq` | false | `B` | `D. False, False` |
| baseline | `mmlu_2634` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2635` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2636` | `mcq` | true | `B` | `B. Canada` |
| baseline | `mmlu_2637` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2638` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2639` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2640` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2641` | `mcq` | false | `B` | `A. 1.5 children per woman` |
| baseline | `mmlu_2642` | `mcq` | false | `C` | `B. $1,000` |
| baseline | `mmlu_2643` | `mcq` | false | `C` | `D. 80%` |
| baseline | `mmlu_2644` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2645` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2646` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2647` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2648` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2649` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2650` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2651` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2652` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2653` | `mcq` | false | `A` | `D. False, False` |
| baseline | `mmlu_2654` | `mcq` | false | `B` | `C. -40%` |
| baseline | `mmlu_2655` | `mcq` | false | `C` | `B. 56%` |
| baseline | `mmlu_2656` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2657` | `mcq` | false | `C` | `A. $150,000` |
| baseline | `mmlu_2658` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2659` | `mcq` | false | `D` | `B. Russia` |
| baseline | `mmlu_2660` | `mcq` | true | `A` | `A. India, Congo` |
| baseline | `mmlu_2661` | `mcq` | true | `D` | `D. 86%` |
| baseline | `mmlu_2662` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2663` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2664` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2665` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2666` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2667` | `mcq` | true | `C` | `C. 80%` |
| baseline | `mmlu_2668` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2669` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2670` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2671` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2672` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2674` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2675` | `mcq` | true | `B` | `B. Phagocytes` |
| baseline | `mmlu_2676` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2679` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2680` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2681` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2682` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2683` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2684` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2685` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2686` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2689` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2690` | `mcq` | true | `C` | `C. mutualism` |
| baseline | `mmlu_2691` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2692` | `mcq` | true | `B` | `B. maintaining homeostasis.` |
| baseline | `mmlu_2693` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2694` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2695` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2696` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2697` | `mcq` | true | `C` | `C. Mutations` |
| baseline | `mmlu_2698` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2699` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2700` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2701` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2702` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2703` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2704` | `mcq` | true | `C` | `C. 54%` |
| baseline | `mmlu_2705` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2706` | `mcq` | true | `D` | `D. Mutations contribute the most to genetic variability in a population through natural mutations and other mutagens.` |
| baseline | `mmlu_2707` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2708` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2709` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2710` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2711` | `mcq` | false | `B` | `A. Some mosquitoes experienced a mutation after being exposed to DDT that made them resistant to the insecticide. Then t` |
| baseline | `mmlu_2712` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2713` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2714` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2715` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2716` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2717` | `mcq` | true | `B` | `B. fallopian tube` |
| baseline | `mmlu_2718` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2719` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2720` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2721` | `mcq` | true | `A` | `A. mitochondrial matrix` |
| baseline | `mmlu_2722` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2723` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2724` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2725` | `mcq` | false | `C` | `D. Promoter` |
| baseline | `mmlu_2726` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2727` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2728` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2729` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2730` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2731` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2732` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2733` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2734` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2735` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2736` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2737` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2738` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2739` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2740` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2741` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2742` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2743` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2744` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2745` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2746` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_2747` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2748` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2749` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2750` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2751` | `mcq` | true | `C` | `C. Availability of water.` |
| baseline | `mmlu_2752` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2753` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2754` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2755` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2756` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2757` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2758` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2759` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2760` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2761` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2762` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2763` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2764` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2765` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2766` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2767` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2768` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2769` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2770` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2771` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2772` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2773` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2774` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2775` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2776` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2777` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2778` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2779` | `mcq` | false | `C` | `B. Reproductive isolation was not complete.` |
| baseline | `mmlu_2780` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2781` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2782` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2783` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2784` | `mcq` | false | `B` | `D. 50%` |
| baseline | `mmlu_2785` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2786` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2787` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2788` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2789` | `mcq` | true | `A` | `A. enzymes in the lysosomes` |
| baseline | `mmlu_2790` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2791` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2792` | `mcq` | true | `D` | `D. 25%` |
| baseline | `mmlu_2793` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2794` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2795` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2796` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2797` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2798` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2799` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2800` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2801` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2802` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2803` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2804` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2805` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2806` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2808` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2809` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2810` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2811` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2812` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2813` | `mcq` | true | `A` | `A. Characteristics acquired during an organism's life are generally not passed on through genes.` |
| baseline | `mmlu_2814` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2815` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2816` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2817` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2818` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2819` | `mcq` | true | `B` | `B. The flu virus, which changes its envelope proteins` |
| baseline | `mmlu_2820` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2821` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2822` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2823` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2824` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2825` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2827` | `mcq` | true | `D` | `D. Promoter` |
| baseline | `mmlu_2828` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2829` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2830` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2831` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2832` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2833` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2834` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2835` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2836` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2837` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2838` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2839` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2840` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2841` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2842` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2843` | `mcq` | false | `D` | `A. Lake B is alkaline.` |
| baseline | `mmlu_2844` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2845` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2846` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2847` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2848` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2849` | `mcq` | true | `C` | `C.水` |
| baseline | `mmlu_2850` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2851` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2852` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2853` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2854` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2855` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2856` | `mcq` | true | `A` | `A. Enhancer` |
| baseline | `mmlu_2857` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2858` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2859` | `mcq` | false | `C` | `A. thicker walls, which are impermeable to water` |
| baseline | `mmlu_2860` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2861` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2862` | `mcq` | true | `D` | `D. I and III` |
| baseline | `mmlu_2863` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2864` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2865` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2866` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2867` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2868` | `mcq` | true | `A` | `A. increasing the surface area of the small intestine.` |
| baseline | `mmlu_2869` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2870` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2871` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2872` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2873` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2874` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2875` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2876` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2877` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2878` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2879` | `mcq` | true | `B` | `B. Differences in the timing and expression levels of different genes leads to structural and functional differences.` |
| baseline | `mmlu_2880` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2881` | `mcq` | true | `C` | `C. The frequency of the allele will remain at 0.3 because the population is at Hardy-Weinberg equilibrium.` |
| baseline | `mmlu_2882` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2883` | `mcq` | true | `B` | `B. Minimizing artificial lighting in the area` |
| baseline | `mmlu_2884` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2885` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2886` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2887` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2888` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2889` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2890` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2891` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2892` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2893` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2894` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2895` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2896` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2897` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2898` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2899` | `mcq` | true | `B` | `B. Repressor` |
| baseline | `mmlu_2900` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2901` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2902` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2903` | `mcq` | false | `B` | `A. removing some of reactant A` |
| baseline | `mmlu_2904` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2905` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2906` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2907` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2908` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2909` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2910` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2911` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2912` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2913` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2914` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2915` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2916` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2918` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2919` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2920` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2921` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2922` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2923` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2924` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2925` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2926` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2927` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2928` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2929` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2930` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2931` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2932` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2933` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2934` | `mcq` | true | `B` | `B. Succession` |
| baseline | `mmlu_2935` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2936` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2937` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2938` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2939` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2940` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2941` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2942` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2943` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2944` | `mcq` | true | `A` | `A. H2O` |
| baseline | `mmlu_2945` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2946` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2947` | `mcq` | true | `A` | `A. Prophase I` |
| baseline | `mmlu_2948` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2949` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2950` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2951` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2952` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2953` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2954` | `mcq` | true | `D` | `D. Fungus` |
| baseline | `mmlu_2955` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2956` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2957` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2958` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2959` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2960` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2961` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2962` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2963` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2964` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2965` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2966` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2967` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2968` | `mcq` | true | `D` | `D. Natural selection` |
| baseline | `mmlu_2969` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2970` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2971` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2972` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2973` | `mcq` | false | `B` | `C. Adenine : Guanine` |
| baseline | `mmlu_2974` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2975` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2976` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2977` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2978` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2979` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2980` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2981` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2982` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2983` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2984` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2986` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2987` | `mcq` | false | `C` | `B. Se2-` |
| baseline | `mmlu_2988` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2989` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2990` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2991` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2992` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2993` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2994` | `mcq` | false | `C` | `B. a weak acid` |
| baseline | `mmlu_2995` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2996` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2997` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2998` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2999` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3000` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3001` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3002` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3003` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3004` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3005` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3007` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3008` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3009` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3010` | `mcq` | false | `D` | `B. -3` |
| baseline | `mmlu_3011` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3012` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3013` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3014` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3015` | `mcq` | false | `B` | `D. SF6` |
| baseline | `mmlu_3016` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3017` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3018` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3019` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3020` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3021` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3022` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3023` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3024` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3025` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3026` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3027` | `mcq` | true | `C` | `C. RCOOH` |
| baseline | `mmlu_3028` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3029` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3030` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3031` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3032` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3033` | `mcq` | false | `C` | `A. The 1s peak has the lowest energy.` |
| baseline | `mmlu_3034` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3035` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3036` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3037` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3038` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3039` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3040` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3041` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3042` | `mcq` | true | `D` | `D. 251 torr` |
| baseline | `mmlu_3043` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3044` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3045` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3046` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3047` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3048` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3049` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3050` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3051` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3052` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3053` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3054` | `mcq` | false | `B` | `D. 181°C` |
| baseline | `mmlu_3055` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3056` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3057` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3058` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3059` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3060` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3061` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3062` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3063` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3064` | `mcq` | false | `A` | `D. NO3-` |
| baseline | `mmlu_3065` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3066` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3067` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3068` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3069` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3070` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3071` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3072` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3073` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3074` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3075` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3076` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3077` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3078` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3079` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3080` | `mcq` | true | `D` | `D. Sulfur` |
| baseline | `mmlu_3081` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3082` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3083` | `mcq` | false | `C` | `D. Sulfur` |
| baseline | `mmlu_3084` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3085` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3086` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3087` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3088` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3089` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3090` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3091` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3092` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3094` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3095` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3096` | `mcq` | true | `D` | `D. Making the reaction vessel smaller` |
| baseline | `mmlu_3097` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3098` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3099` | `mcq` | false | `C` | `proton` |
| baseline | `mmlu_3100` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3101` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3102` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3103` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3104` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3105` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3106` | `mcq` | false | `C` | `B. First order` |
| baseline | `mmlu_3107` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3108` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3109` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3110` | `mcq` | false | `D` | `B. HClO` |
| baseline | `mmlu_3111` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3112` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3113` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3114` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3115` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3116` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3117` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3118` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3119` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3120` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3121` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3122` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3123` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3124` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3125` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3126` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3127` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3128` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3129` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3130` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3131` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3132` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3133` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3134` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3135` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3136` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3137` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3138` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3139` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3140` | `mcq` | false | `C` | `A. 1s` |
| baseline | `mmlu_3141` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3142` | `mcq` | true | `C` | `C. Am` |
| baseline | `mmlu_3143` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3144` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3145` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3146` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3147` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3148` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3149` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3150` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3151` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3152` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3153` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3154` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3155` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3156` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3157` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3158` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3159` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3160` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3161` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3162` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3163` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3164` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3165` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3166` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3167` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3168` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3169` | `mcq` | true | `A` | `A. 3.4 × 10^-4 s-1` |
| baseline | `mmlu_3170` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3171` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3172` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3173` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3174` | `mcq` | false | `B` | `D. 7.1 mol` |
| baseline | `mmlu_3175` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3176` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3177` | `mcq` | true | `D` | `D. HBr` |
| baseline | `mmlu_3178` | `mcq` | false | `B` | `A. HNO2` |
| baseline | `mmlu_3179` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3180` | `mcq` | false | `C` | `A. 3+, reduction` |
| baseline | `mmlu_3181` | `mcq` | true | `B` | `B. Rate = k[A]^2` |
| baseline | `mmlu_3182` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_3183` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3184` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3185` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3186` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3187` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3188` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3189` | `mcq` | true | `B` | `B. Only elements that appear in both inputListl and inputList2` |
| baseline | `mmlu_3190` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3191` | `mcq` | false | `B` | `C. Error` |
| baseline | `mmlu_3192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3193` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3194` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3195` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3196` | `mcq` | true | `C` | `C. Lossless compression` |
| baseline | `mmlu_3197` | `mcq` | true | `A` | `A. isupper()` |
| baseline | `mmlu_3198` | `mcq` | true | `D` | `D. (num MOD 2) = 1` |
| baseline | `mmlu_3199` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3200` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3201` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3202` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3203` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3204` | `mcq` | true | `B` | `B. //` |
| baseline | `mmlu_3205` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3206` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3207` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3208` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3209` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3210` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3211` | `mcq` | true | `A` | `A. Yes` |
| baseline | `mmlu_3212` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3213` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3214` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3215` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3216` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3217` | `mcq` | true | `B` | `B. 1` |
| baseline | `mmlu_3218` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3219` | `mcq` | true | `A` | `A. **` |
| baseline | `mmlu_3220` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3221` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3223` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3224` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3225` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3226` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3227` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3228` | `mcq` | false | `C` | `8` |
| baseline | `mmlu_3229` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3230` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3231` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3232` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3233` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3234` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3235` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3236` | `mcq` | true | `D` | `D._heads_counter=2` |
| baseline | `mmlu_3237` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3238` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3239` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3240` | `mcq` | false | `C` | `B. Dictionary/map \| Stack \| Queue` |
| baseline | `mmlu_3241` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3242` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3244` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3245` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3246` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3247` | `mcq` | false | `D` | `A. Error` |
| baseline | `mmlu_3248` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3249` | `mcq` | false | `C` | `D. 4` |
| baseline | `mmlu_3250` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3251` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3252` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3253` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3254` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3255` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3256` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3257` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3258` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3259` | `mcq` | true | `B` | `B. nextAvailableID` |
| baseline | `mmlu_3260` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3261` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3262` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3263` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3264` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3265` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3266` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3267` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3268` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3269` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3270` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3271` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3272` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3273` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3274` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3275` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3276` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3277` | `mcq` | false | `C` | `B. 1 2` |
| baseline | `mmlu_3278` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3279` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3281` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3282` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3283` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3284` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3285` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3286` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3287` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3288` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3289` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3290` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3291` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3292` | `mcq` | true | `D` | `D. Social Darwinism` |
| baseline | `mmlu_3293` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3294` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3295` | `mcq` | false | `B` | `C. Industrialization` |
| baseline | `mmlu_3296` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3298` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3299` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3300` | `mcq` | false | `A` | `B. Financial gain` |
| baseline | `mmlu_3301` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3302` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3303` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3304` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3305` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3306` | `mcq` | true | `D` | `D. Poland` |
| baseline | `mmlu_3307` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3308` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3309` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3310` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3311` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3312` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3313` | `mcq` | false | `D` | `B. he wrote in a language that was understandable to the masses, unlike his predecessors has` |
| baseline | `mmlu_3314` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3315` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3316` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3317` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3318` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3319` | `mcq` | true | `B` | `B. Financial gain` |
| baseline | `mmlu_3320` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3321` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3322` | `mcq` | true | `A` | `A. Jean-Jacques Rousseau because he thought society corrupted noble souls.` |
| baseline | `mmlu_3323` | `mcq` | false | `D` | `A. They are "exiled sons" of the British race.` |
| baseline | `mmlu_3324` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3325` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3326` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3328` | `mcq` | true | `C` | `C. Humanism` |
| baseline | `mmlu_3329` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3330` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3331` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3332` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3333` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3334` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3335` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3336` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3337` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3338` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3339` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3340` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3341` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3342` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3343` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3344` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3345` | `mcq` | false | `C` | `B. New ships like the carrack and caravel` |
| baseline | `mmlu_3346` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3347` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3348` | `mcq` | false | `C` | `B. creating of a secular science to challenge the Church` |
| baseline | `mmlu_3349` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3350` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3351` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3353` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3354` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3355` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3356` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3357` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3358` | `mcq` | false | `D` | `B. He was so concerned with ceremonies and appearances that he did not rule his country well.` |
| baseline | `mmlu_3359` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3360` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3361` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3362` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3363` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3364` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3365` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3366` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3367` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3368` | `mcq` | true | `C` | `C. Increased disillusionment and cynicism` |
| baseline | `mmlu_3369` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3370` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3371` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3372` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3373` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3374` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3375` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3376` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3377` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3378` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3379` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3380` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3381` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3382` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3383` | `mcq` | true | `D` | `D. Anabaptists` |
| baseline | `mmlu_3384` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3385` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3386` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3387` | `mcq` | true | `C` | `C. general rejection of Catholic dogma` |
| baseline | `mmlu_3388` | `mcq` | true | `B` | `B. People could begin to question the Church on a wider scale.` |
| baseline | `mmlu_3389` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3390` | `mcq` | true | `B` | `B. the consent of those members of society` |
| baseline | `mmlu_3391` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3392` | `mcq` | true | `B` | `B. They were subjugated and destroyed.` |
| baseline | `mmlu_3393` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3394` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3395` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3396` | `mcq` | false | `B` | `C. Increased popular participation in politics` |
| baseline | `mmlu_3397` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3398` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3399` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3401` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3402` | `mcq` | true | `A` | `A. They initiated an armed resistance against Western interests in Northern China.` |
| baseline | `mmlu_3403` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3404` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3405` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3406` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3407` | `mcq` | true | `C` | `C. Mercantilism` |
| baseline | `mmlu_3408` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3409` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3410` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3411` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3412` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3413` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3414` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3415` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3416` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3417` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3418` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3419` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3420` | `mcq` | true | `B` | `B. France` |
| baseline | `mmlu_3421` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3422` | `mcq` | false | `A` | `B. Article II` |
| baseline | `mmlu_3423` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3424` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3425` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3426` | `mcq` | true | `B` | `B. Religious` |
| baseline | `mmlu_3427` | `mcq` | true | `B` | `B. successfully harnessed the human resources of the new French Republic` |
| baseline | `mmlu_3428` | `mcq` | false | `C` | `A. The switch from a liberal-dominated to a conservative-dominated Parliament` |
| baseline | `mmlu_3429` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3430` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3431` | `mcq` | true | `C` | `C. Mexico` |
| baseline | `mmlu_3432` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3434` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3435` | `mcq` | true | `D` | `D. Nationalism` |
| baseline | `mmlu_3436` | `mcq` | true | `C` | `C. An increased rate of inflation` |
| baseline | `mmlu_3437` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3438` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3439` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3440` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3441` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3442` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3443` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3444` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3445` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3446` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3447` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3448` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3449` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3450` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3451` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3452` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3453` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3454` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3455` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3456` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3457` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3458` | `mcq` | true | `B` | `B. Replacement level` |
| baseline | `mmlu_3459` | `mcq` | false | `A` | `B. Christianity` |
| baseline | `mmlu_3460` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3461` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3462` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3463` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3464` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3465` | `mcq` | true | `B` | `B. Suburbs` |
| baseline | `mmlu_3466` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3467` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3468` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3470` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3471` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3472` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3473` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3474` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3475` | `mcq` | true | `C` | `C. Natural` |
| baseline | `mmlu_3476` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3477` | `mcq` | false | `A` | `C. Tertiary` |
| baseline | `mmlu_3478` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3479` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3481` | `mcq` | false | `B` | `France` |
| baseline | `mmlu_3482` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3483` | `mcq` | true | `C` | `C. Cambodia.` |
| baseline | `mmlu_3484` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3485` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3486` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3487` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3488` | `mcq` | true | `B` | `B. Acculturation.` |
| baseline | `mmlu_3489` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3490` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3491` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3492` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3493` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3495` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3496` | `mcq` | true | `B` | `B. The Amazon Basin` |
| baseline | `mmlu_3497` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3498` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3499` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3500` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3501` | `mcq` | false | `D` | `B. Italy` |
| baseline | `mmlu_3502` | `mcq` | false | `C` | `A. First` |
| baseline | `mmlu_3503` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3504` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3505` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3506` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3507` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3508` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3509` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3510` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3511` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3512` | `mcq` | true | `C` | `C. Agglomeration.` |
| baseline | `mmlu_3513` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3514` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3515` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3516` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3517` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3518` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3519` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3521` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3522` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3523` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3524` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3525` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3526` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3527` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3528` | `mcq` | true | `B` | `B. The end of the Cold War` |
| baseline | `mmlu_3529` | `mcq` | true | `B` | `B. Air` |
| baseline | `mmlu_3530` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3531` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3532` | `mcq` | true | `C` | `C. Indo-European` |
| baseline | `mmlu_3533` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3534` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3535` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3536` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3537` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3538` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3539` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3540` | `mcq` | true | `C` | `C. Information` |
| baseline | `mmlu_3541` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3542` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3543` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3544` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3545` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3546` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3547` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3548` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3549` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3550` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3551` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3552` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3553` | `mcq` | true | `A` | `A. defend North America and Western Europe against the threat of communism.` |
| baseline | `mmlu_3554` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3555` | `mcq` | false | `C` | `B. Contagious` |
| baseline | `mmlu_3556` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3557` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3558` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3559` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3560` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3561` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3562` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3563` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3564` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3565` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3566` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3567` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3568` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3569` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3570` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3571` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3572` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3573` | `mcq` | true | `D` | `D. Indo-European` |
| baseline | `mmlu_3574` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3575` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3576` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3577` | `mcq` | true | `C` | `C. Chile` |
| baseline | `mmlu_3578` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3579` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3580` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3581` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3582` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3583` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3584` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3585` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3586` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3587` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3588` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3589` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3590` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3591` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3592` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3593` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3594` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3595` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3596` | `mcq` | true | `A` | `A./core, periphery, and semi-periphery./` |
| baseline | `mmlu_3597` | `mcq` | false | `C` | `B. Iraq` |
| baseline | `mmlu_3598` | `mcq` | true | `D` | `D. Spain` |
| baseline | `mmlu_3599` | `mcq` | false | `C` | `B. East Asia` |
| baseline | `mmlu_3600` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3601` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3602` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3603` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3604` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3605` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3606` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3607` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3608` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3609` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3610` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3611` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3612` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3613` | `mcq` | false | `C` | `E.` |
| baseline | `mmlu_3614` | `mcq` | false | `B` | `C. Pesticides` |
| baseline | `mmlu_3615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3616` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3617` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3618` | `mcq` | false | `D` | `B. Land use` |
| baseline | `mmlu_3619` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3620` | `mcq` | false | `C` | `B. Secesion` |
| baseline | `mmlu_3621` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3622` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3623` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3624` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3625` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3626` | `mcq` | true | `C` | `C. China` |
| baseline | `mmlu_3627` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3628` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3629` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3630` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3631` | `mcq` | false | `A` | `B. Asia` |
| baseline | `mmlu_3632` | `mcq` | true | `B` | `B. Christianity` |
| baseline | `mmlu_3633` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3634` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3635` | `mcq` | true | `B` | `B. Transport` |
| baseline | `mmlu_3636` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3637` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3638` | `mcq` | true | `B` | `B. English.` |
| baseline | `mmlu_3639` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3640` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3641` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3642` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3643` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3644` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3645` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3646` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3647` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3648` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3649` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3650` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3651` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3652` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3653` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3654` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3655` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3656` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3657` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3658` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3659` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3660` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3661` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3662` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3663` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3664` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3665` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3666` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3668` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3669` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3670` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3671` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3672` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3673` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3674` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3675` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3676` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3677` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3678` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3679` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3680` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3681` | `mcq` | false | `C` | `B. I and IV only` |
| baseline | `mmlu_3682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3683` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3684` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3685` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3686` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3688` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3689` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3690` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3691` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3692` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3693` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3694` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3695` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3696` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3697` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3698` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3699` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3700` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3701` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3702` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3703` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3704` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3705` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3706` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3707` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3708` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3709` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3710` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3712` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3713` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3714` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3715` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3716` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3717` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3718` | `mcq` | false | `C` | `B. Congress` |
| baseline | `mmlu_3719` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3720` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3721` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3722` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3723` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3724` | `mcq` | true | `A` | `A. judicial activism` |
| baseline | `mmlu_3725` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3726` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3728` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3729` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3730` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3731` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3733` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3734` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3735` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3736` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3737` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3738` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3739` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3740` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3741` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3742` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3743` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3744` | `mcq` | true | `C` | `C. reduce the federal deficit` |
| baseline | `mmlu_3745` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3746` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3747` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3748` | `mcq` | true | `A` | `A. determine both the rules of the House and conditions for legislative process.` |
| baseline | `mmlu_3749` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3750` | `mcq` | false | `C` | `D. II and III only` |
| baseline | `mmlu_3751` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3752` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3753` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3754` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3755` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3756` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3757` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3758` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3759` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3760` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3761` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3762` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3763` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3764` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3765` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3766` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3767` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3769` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3770` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3771` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3772` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3773` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3774` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3775` | `mcq` | true | `A` | `A. will review a lower court decision.` |
| baseline | `mmlu_3776` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3777` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3778` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3779` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3780` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3781` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3782` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3783` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3784` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3785` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3786` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3787` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3788` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3789` | `mcq` | true | `C` | `C. Federal budget entitlements` |
| baseline | `mmlu_3790` | `mcq` | false | `B` | `D. Cabinet` |
| baseline | `mmlu_3791` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3792` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3793` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3794` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3795` | `mcq` | true | `C` | `C. Increasing concentration of ownership in the news media` |
| baseline | `mmlu_3796` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3797` | `mcq` | true | `D` | `D. president` |
| baseline | `mmlu_3798` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3799` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3800` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3801` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3802` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3803` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3804` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3805` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3806` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3807` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3808` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3809` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3810` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3811` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3812` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3813` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3814` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3815` | `mcq` | true | `D` | `D. I, II, and IV only` |
| baseline | `mmlu_3816` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3817` | `mcq` | true | `B` | `B. Ways and Means` |
| baseline | `mmlu_3818` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3819` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3820` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3821` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3822` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3823` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3824` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3825` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3826` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3827` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3828` | `mcq` | true | `D` | `D. John Locke` |
| baseline | `mmlu_3829` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3830` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3831` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3832` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3833` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3834` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3835` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3836` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3837` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3838` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3839` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3840` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3841` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3842` | `mcq` | true | `B` | `B. contractionary monetary policy.` |
| baseline | `mmlu_3843` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3844` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3845` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3846` | `mcq` | true | `D` | `D. Opportunity Cost` |
| baseline | `mmlu_3847` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3848` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3849` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3850` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3851` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3852` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3853` | `mcq` | true | `B` | `B. 30%. Explanation: The reserve ratio can be calculated as follows:  Reserve Ratio = (Excess Reserves / Deposits) * 100` |
| baseline | `mmlu_3854` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3855` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3856` | `mcq` | false | `B` | `D. Expected future inflation.` |
| baseline | `mmlu_3857` | `mcq` | true | `B` | `B. inflation.` |
| baseline | `mmlu_3858` | `mcq` | true | `D` | `D. I II and III are correct.` |
| baseline | `mmlu_3859` | `mcq` | false | `A` | `D. Falls     Falls     No change     No change` |
| baseline | `mmlu_3860` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3861` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3862` | `mcq` | true | `B` | `B. Dollar bills` |
| baseline | `mmlu_3863` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3864` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3865` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3866` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3867` | `mcq` | false | `B` | `A. Decreases            Increases      Decreases` |
| baseline | `mmlu_3868` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3869` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3870` | `mcq` | true | `D` | `D. unexpectedly higher resource prices.` |
| baseline | `mmlu_3871` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3872` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3873` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3874` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3875` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3876` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3877` | `mcq` | false | `C` | `D. $5,000` |
| baseline | `mmlu_3878` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3880` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3881` | `mcq` | false | `D` | `A. increase by $2.9 million.` |
| baseline | `mmlu_3882` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3883` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3884` | `mcq` | true | `B` | `B. 7 14` |
| baseline | `mmlu_3885` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3886` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3887` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3888` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3889` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3890` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3891` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3892` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3893` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3894` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3895` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3896` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3897` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3898` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3899` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3900` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3901` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3902` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3903` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3904` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3905` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3906` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3907` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3908` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3909` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3910` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3911` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3912` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3913` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3914` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3915` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3916` | `mcq` | false | `D` | `A. The productivity of labor in country Z is 33 percent higher than in country X.` |
| baseline | `mmlu_3917` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3918` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3919` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3920` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3921` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3922` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3923` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3924` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3925` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3926` | `mcq` | true | `D` | `D. dumping.` |
| baseline | `mmlu_3927` | `mcq` | false | `C` | `B. $1 million` |
| baseline | `mmlu_3928` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3929` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3930` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3931` | `mcq` | false | `B` | `C. 50 percent.` |
| baseline | `mmlu_3932` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3933` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3934` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3935` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3936` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3937` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3938` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3939` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3940` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3941` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3942` | `mcq` | true | `C` | `C. expansionary monetary policy` |
| baseline | `mmlu_3943` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3944` | `mcq` | false | `B` | `C. variable.` |
| baseline | `mmlu_3945` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3946` | `mcq` | false | `D` | `C. $1.75` |
| baseline | `mmlu_3947` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3948` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3949` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3950` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3951` | `mcq` | true | `D` | `D. I and II` |
| baseline | `mmlu_3952` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3953` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3954` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3955` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3956` | `mcq` | true | `B` | `B. $400 billion` |
| baseline | `mmlu_3957` | `mcq` | true | `B` | `B. Imports.` |
| baseline | `mmlu_3958` | `mcq` | false | `A` | `D. Increased government spending.` |
| baseline | `mmlu_3959` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3960` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3961` | `mcq` | false | `D` | `C. Sell bonds   Decreases   Decreases   Inflation` |
| baseline | `mmlu_3962` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3963` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3964` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3965` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3966` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3967` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3968` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3969` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3970` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3971` | `mcq` | false | `B` | `A. raise the price level and output in the economy.` |
| baseline | `mmlu_3972` | `mcq` | false | `C` | `D. China ($2).` |
| baseline | `mmlu_3973` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3974` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3975` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3976` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3977` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3978` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3979` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3980` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3981` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3982` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3983` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3984` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3985` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3986` | `mcq` | true | `A` | `A. implementing innovative production techniques.` |
| baseline | `mmlu_3987` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3988` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3989` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3990` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3991` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3992` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3993` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3994` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3995` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3996` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3997` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3998` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3999` | `mcq` | true | `B` | `B` |
