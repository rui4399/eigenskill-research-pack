# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `6500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 3652 / 6500 | 0.5618 | 8.8778 | 0.187424 |

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
| baseline | `mmlu_4000` | `mcq` | false | `D` | `A. households provide goods to firms in exchange for wage payments.` |
| baseline | `mmlu_4001` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4002` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4003` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4004` | `mcq` | true | `C` | `C. Decreasing   Increasing` |
| baseline | `mmlu_4005` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4006` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4007` | `mcq` | true | `D` | `D. Higher government funding of research on clean energy supplies` |
| baseline | `mmlu_4008` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4009` | `mcq` | true | `D` | `D. 7 years.` |
| baseline | `mmlu_4010` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4011` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4012` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4013` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4014` | `mcq` | true | `B` | `B. Structured unemployment.` |
| baseline | `mmlu_4015` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4016` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4017` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4018` | `mcq` | true | `A` | `A. Increased demand, Appreciating` |
| baseline | `mmlu_4019` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4020` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4021` | `mcq` | false | `D` | `A. Increase, Increase` |
| baseline | `mmlu_4022` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4023` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4024` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4025` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4026` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4027` | `mcq` | false | `D` | `B. Increased demand   Rising   Appreciates` |
| baseline | `mmlu_4028` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4029` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4030` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4031` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4032` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4033` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4034` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4035` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4036` | `mcq` | false | `D` | `C. Decrease in demand Falling` |
| baseline | `mmlu_4037` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4038` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4039` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4040` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4041` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4042` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4043` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4044` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4045` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4046` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4047` | `mcq` | false | `B` | `A. raise the price level and output in the economy.` |
| baseline | `mmlu_4048` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4049` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4050` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4051` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4052` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4053` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4054` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4055` | `mcq` | false | `C` | `B. decreased by 4 percent.` |
| baseline | `mmlu_4056` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4057` | `mcq` | false | `C` | `B. GDP per capita.` |
| baseline | `mmlu_4058` | `mcq` | false | `D` | `C. $625` |
| baseline | `mmlu_4059` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4060` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4061` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4062` | `mcq` | false | `D` | `B. and taxes rise.` |
| baseline | `mmlu_4063` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4064` | `mcq` | false | `D` | `C. Decreases            Decreases      Increases` |
| baseline | `mmlu_4065` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4066` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4067` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4068` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4069` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4070` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4071` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4072` | `mcq` | false | `A` | `B. 1.25` |
| baseline | `mmlu_4073` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4074` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4075` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4076` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4077` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4078` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4079` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4080` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4081` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4082` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4083` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4084` | `mcq` | false | `D` | `B. Decrease     Decrease     Decrease     Increase` |
| baseline | `mmlu_4085` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4086` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4087` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4088` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4089` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4090` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4091` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4092` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4093` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4094` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4095` | `mcq` | false | `D` | `A. Decrease     Increase     Increase` |
| baseline | `mmlu_4096` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4097` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4098` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4099` | `mcq` | true | `D` | `D. Investment tax credits.` |
| baseline | `mmlu_4100` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4101` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4102` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4103` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4104` | `mcq` | false | `C` | `D. 3.3%` |
| baseline | `mmlu_4105` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4106` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4107` | `mcq` | false | `A` | `D. (D) Increased Stayed the same` |
| baseline | `mmlu_4108` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4109` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4110` | `mcq` | true | `D` | `D. Increased Decreased` |
| baseline | `mmlu_4111` | `mcq` | true | `C` | `C. $70` |
| baseline | `mmlu_4112` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4113` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4114` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4115` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4116` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4117` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4118` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4119` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4120` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4121` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4122` | `mcq` | false | `C` | `A/B/C/D` |
| baseline | `mmlu_4123` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4124` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4125` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4126` | `mcq` | true | `B` | `B. $4,500` |
| baseline | `mmlu_4127` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4128` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4129` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4130` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4131` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4132` | `mcq` | true | `B` | `B. $3,000` |
| baseline | `mmlu_4133` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4134` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4135` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4136` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4137` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4138` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4139` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4140` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4141` | `mcq` | true | `D` | `D. both (A) and (C)` |
| baseline | `mmlu_4142` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4143` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4144` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4145` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4146` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4147` | `mcq` | false | `D` | `A. Decrease     Increase     Increase` |
| baseline | `mmlu_4148` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4149` | `mcq` | false | `B` | `Only I is true.` |
| baseline | `mmlu_4150` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4151` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4152` | `mcq` | false | `B` | `D. Greater than $200 but less than $500` |
| baseline | `mmlu_4153` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4154` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4155` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4156` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4157` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4158` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4159` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4160` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4161` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4162` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4163` | `mcq` | false | `D` | `A. Decreases appreciate decreases` |
| baseline | `mmlu_4164` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4165` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4166` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4167` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4168` | `mcq` | false | `C` | `D. $1,900` |
| baseline | `mmlu_4169` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4170` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4171` | `mcq` | false | `A` | `D. I and III` |
| baseline | `mmlu_4172` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4173` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4174` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4175` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4176` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4177` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4178` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4179` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4180` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4181` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4182` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4183` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4184` | `mcq` | true | `A` | `A. deficit recession surplus expansion` |
| baseline | `mmlu_4185` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4186` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4187` | `mcq` | false | `A` | `B. Shifts up, Rises, Falls` |
| baseline | `mmlu_4188` | `mcq` | false | `C` | `D. France has the absolute advantage in cheese.` |
| baseline | `mmlu_4189` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4190` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4191` | `mcq` | true | `D` | `D. I and III.` |
| baseline | `mmlu_4192` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4193` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4194` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4195` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4196` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4197` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4198` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4199` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4200` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4201` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4202` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4203` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4204` | `mcq` | true | `B` | `B. Unit of account` |
| baseline | `mmlu_4205` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4206` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4207` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4208` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4209` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4210` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4211` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4212` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4213` | `mcq` | false | `B` | `A. increase by $200 million.` |
| baseline | `mmlu_4214` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4215` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4216` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4217` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4218` | `mcq` | false | `B` | `C. I and IV only` |
| baseline | `mmlu_4219` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4220` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4221` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4222` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4223` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4224` | `mcq` | false | `D` | `C. incorporates both current year prices and base year prices.` |
| baseline | `mmlu_4225` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4226` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4227` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4228` | `mcq` | false | `D` | `C. (2, 2)` |
| baseline | `mmlu_4229` | `mcq` | false | `C` | `D. 25` |
| baseline | `mmlu_4230` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4231` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4232` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4233` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4234` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4235` | `mcq` | false | `A` | `C. 36` |
| baseline | `mmlu_4236` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4237` | `mcq` | false | `B` | `C. 10` |
| baseline | `mmlu_4238` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4239` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4240` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4241` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4242` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4243` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4244` | `mcq` | true | `A` | `A. 8` |
| baseline | `mmlu_4245` | `mcq` | false | `B` | `C. -1` |
| baseline | `mmlu_4246` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4247` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4248` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4249` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4250` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4251` | `mcq` | false | `B` | `A. 4` |
| baseline | `mmlu_4252` | `mcq` | false | `A` | `C. Wednesday` |
| baseline | `mmlu_4253` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_4254` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4255` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4256` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4257` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4258` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4259` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4260` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4261` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4262` | `mcq` | false | `A` | `C. -6` |
| baseline | `mmlu_4263` | `mcq` | false | `D` | `C. 9` |
| baseline | `mmlu_4264` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4265` | `mcq` | false | `C` | `5.5` |
| baseline | `mmlu_4266` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4267` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4268` | `mcq` | false | `B` | `C. -1` |
| baseline | `mmlu_4269` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4270` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4271` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4272` | `mcq` | false | `C` | `B. 90950` |
| baseline | `mmlu_4273` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4274` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4275` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4276` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4277` | `mcq` | true | `B` | `B. -75` |
| baseline | `mmlu_4278` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4279` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4280` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4281` | `mcq` | false | `C` | `B. 16` |
| baseline | `mmlu_4282` | `mcq` | false | `C` | `B. 1/64` |
| baseline | `mmlu_4283` | `mcq` | false | `A` | `B. \frac{25}{6}` |
| baseline | `mmlu_4284` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4285` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4286` | `mcq` | false | `B` | `D. 12` |
| baseline | `mmlu_4287` | `mcq` | true | `C` | `C. -2` |
| baseline | `mmlu_4288` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4289` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4290` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4291` | `mcq` | false | `D` | `C. 11` |
| baseline | `mmlu_4292` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4293` | `mcq` | true | `B` | `B. -9` |
| baseline | `mmlu_4294` | `mcq` | true | `C` | `C. 5` |
| baseline | `mmlu_4295` | `mcq` | false | `B` | `C. 18` |
| baseline | `mmlu_4296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4297` | `mcq` | false | `A` | `B. 2` |
| baseline | `mmlu_4298` | `mcq` | true | `C` | `C. 625` |
| baseline | `mmlu_4299` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4300` | `mcq` | false | `A` | `C. 27` |
| baseline | `mmlu_4301` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4302` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4303` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4304` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4305` | `mcq` | false | `A` | `C. 11` |
| baseline | `mmlu_4306` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4307` | `mcq` | false | `B` | `January 21st` |
| baseline | `mmlu_4308` | `mcq` | true | `B` | `B. 76` |
| baseline | `mmlu_4309` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4310` | `mcq` | false | `C` | `D. 5` |
| baseline | `mmlu_4311` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4312` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4313` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4314` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4315` | `mcq` | false | `A` | `C. 84` |
| baseline | `mmlu_4316` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4317` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4318` | `mcq` | false | `B` | `C. 38` |
| baseline | `mmlu_4319` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4320` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4321` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4322` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4323` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4324` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4325` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4326` | `mcq` | false | `C` | `B. 27` |
| baseline | `mmlu_4327` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4328` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4329` | `mcq` | false | `D` | `C. 9` |
| baseline | `mmlu_4330` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4331` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4332` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4333` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4334` | `mcq` | false | `B` | `C. 60` |
| baseline | `mmlu_4335` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4336` | `mcq` | true | `C` | `C. 32` |
| baseline | `mmlu_4337` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4338` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4339` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4340` | `mcq` | false | `A` | `C. 90` |
| baseline | `mmlu_4341` | `mcq` | false | `A` | `C. 1` |
| baseline | `mmlu_4342` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4343` | `mcq` | false | `A` | `D. 20` |
| baseline | `mmlu_4344` | `mcq` | false | `C` | `B. 1` |
| baseline | `mmlu_4345` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4346` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4347` | `mcq` | false | `B` | `C. 12` |
| baseline | `mmlu_4348` | `mcq` | false | `B` | `C. 1000` |
| baseline | `mmlu_4349` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4350` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4351` | `mcq` | false | `B` | `C. 2` |
| baseline | `mmlu_4352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4353` | `mcq` | false | `D` | `C. 17` |
| baseline | `mmlu_4354` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4355` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4356` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4357` | `mcq` | false | `B` | `C. 4` |
| baseline | `mmlu_4358` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_4359` | `mcq` | false | `B` | `C. -38` |
| baseline | `mmlu_4360` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4361` | `mcq` | false | `B` | `D. 450` |
| baseline | `mmlu_4362` | `mcq` | false | `B` | `C. $286.00` |
| baseline | `mmlu_4363` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4364` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4365` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4366` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4367` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4368` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4369` | `mcq` | false | `B` | `C. 112` |
| baseline | `mmlu_4370` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4371` | `mcq` | false | `A` | `C. 70` |
| baseline | `mmlu_4372` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4373` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4374` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4375` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4376` | `mcq` | false | `D` | `B. -7` |
| baseline | `mmlu_4377` | `mcq` | false | `D` | `C. 60` |
| baseline | `mmlu_4378` | `mcq` | true | `C` | `C. -1.5` |
| baseline | `mmlu_4379` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4380` | `mcq` | true | `C` | `C. 13` |
| baseline | `mmlu_4381` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4382` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4383` | `mcq` | false | `C` | `A. 6` |
| baseline | `mmlu_4384` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4385` | `mcq` | false | `D` | `3` |
| baseline | `mmlu_4386` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4387` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4388` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4389` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4390` | `mcq` | false | `D` | `B. 120` |
| baseline | `mmlu_4391` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4392` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4393` | `mcq` | false | `D` | `B. 1024` |
| baseline | `mmlu_4394` | `mcq` | true | `B` | `B. 40` |
| baseline | `mmlu_4395` | `mcq` | false | `B` | `C. -50%` |
| baseline | `mmlu_4396` | `mcq` | true | `B` | `B. \frac{15}{2}` |
| baseline | `mmlu_4397` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4398` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4399` | `mcq` | true | `C` | `C. 39` |
| baseline | `mmlu_4400` | `mcq` | false | `B` | `C. 4` |
| baseline | `mmlu_4401` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4402` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4403` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4404` | `mcq` | false | `A` | `C. $22,000` |
| baseline | `mmlu_4405` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4406` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4407` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4408` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4409` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4410` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4411` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4412` | `mcq` | false | `C` | `B. 22140` |
| baseline | `mmlu_4413` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4414` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4415` | `mcq` | true | `C` | `C. 36` |
| baseline | `mmlu_4416` | `mcq` | true | `B` | `B. 55` |
| baseline | `mmlu_4417` | `mcq` | false | `A` | `C. 27` |
| baseline | `mmlu_4418` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4419` | `mcq` | false | `A` | `C. 1` |
| baseline | `mmlu_4420` | `mcq` | false | `B` | `C. 8` |
| baseline | `mmlu_4421` | `mcq` | true | `C` | `C. 10` |
| baseline | `mmlu_4422` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4423` | `mcq` | true | `C` | `C. 3` |
| baseline | `mmlu_4424` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4425` | `mcq` | true | `B` | `B. 2 × 5` |
| baseline | `mmlu_4426` | `mcq` | false | `D` | `C. 4` |
| baseline | `mmlu_4427` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4428` | `mcq` | true | `C` | `C. 10` |
| baseline | `mmlu_4429` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4430` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4431` | `mcq` | true | `B` | `B. -14` |
| baseline | `mmlu_4432` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4433` | `mcq` | false | `D` | `C. 6` |
| baseline | `mmlu_4434` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4435` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4436` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4437` | `mcq` | false | `A` | `8` |
| baseline | `mmlu_4438` | `mcq` | true | `C` | `C. 37 inches` |
| baseline | `mmlu_4439` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4440` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4441` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4442` | `mcq` | false | `D` | `C. 5` |
| baseline | `mmlu_4443` | `mcq` | true | `B` | `B. E` |
| baseline | `mmlu_4444` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4445` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4446` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4447` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4448` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_4449` | `mcq` | false | `B` | `C. 32` |
| baseline | `mmlu_4450` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4451` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4452` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4453` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4454` | `mcq` | false | `A` | `C. 60` |
| baseline | `mmlu_4455` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4456` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4457` | `mcq` | false | `B` | `C. 87` |
| baseline | `mmlu_4458` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4459` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4460` | `mcq` | false | `A` | `B. 276` |
| baseline | `mmlu_4461` | `mcq` | true | `C` | `C. 40` |
| baseline | `mmlu_4462` | `mcq` | false | `D` | `B. 1` |
| baseline | `mmlu_4463` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4464` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4465` | `mcq` | false | `A` | `C. 6` |
| baseline | `mmlu_4466` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4467` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4468` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4469` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4470` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4471` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_4472` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4473` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4474` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4475` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4476` | `mcq` | false | `D` | `C. 4` |
| baseline | `mmlu_4477` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4478` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4479` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4480` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4481` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4482` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4483` | `mcq` | false | `B` | `C. 4` |
| baseline | `mmlu_4484` | `mcq` | false | `D` | `B. -2` |
| baseline | `mmlu_4485` | `mcq` | false | `B` | `C. 49` |
| baseline | `mmlu_4486` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4487` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4488` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4489` | `mcq` | true | `C` | `C. 3` |
| baseline | `mmlu_4490` | `mcq` | false | `A` | `B. 7, 10` |
| baseline | `mmlu_4491` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4492` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4493` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4494` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4495` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4496` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4497` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4498` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4499` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4500` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4501` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4502` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4503` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4505` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4506` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4507` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4508` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4509` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4510` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4512` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4514` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4515` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4516` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4517` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4518` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4519` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4520` | `mcq` | true | `D` | `D. I and III only.` |
| baseline | `mmlu_4521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4522` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4523` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4524` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4525` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4526` | `mcq` | false | `B` | `C. 3` |
| baseline | `mmlu_4527` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4528` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4529` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4530` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4532` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4533` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4534` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4535` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4536` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4537` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4538` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4539` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4540` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4541` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4542` | `mcq` | true | `B` | `B. The volunteer fire department in your community.` |
| baseline | `mmlu_4543` | `mcq` | true | `D` | `D. The International Space Station` |
| baseline | `mmlu_4544` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4545` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4546` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4547` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4548` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4549` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4550` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4551` | `mcq` | true | `B` | `B. Elastic.` |
| baseline | `mmlu_4552` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4553` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4554` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4555` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4556` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4557` | `mcq` | false | `B` | `D. I and III.` |
| baseline | `mmlu_4558` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4559` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4560` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4561` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4562` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4563` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4564` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4565` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4566` | `mcq` | true | `D` | `D. Wage = Marginal revenue product of labor.` |
| baseline | `mmlu_4567` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4568` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4569` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4570` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4571` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4572` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4573` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4574` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4575` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4576` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4577` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4578` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4579` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4580` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4581` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4582` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4583` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4584` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4585` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4586` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4587` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4588` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4589` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4590` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4591` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4592` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4593` | `mcq` | false | `B` | `A. Labor demand` |
| baseline | `mmlu_4594` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4595` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4596` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4597` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4598` | `mcq` | true | `D` | `D. opportunity cost.` |
| baseline | `mmlu_4599` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4600` | `mcq` | false | `D` | `A. Pays less and hires more.` |
| baseline | `mmlu_4601` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4602` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4603` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4604` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4605` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4606` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4607` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4608` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4609` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4610` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4611` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4612` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4613` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4614` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4615` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4616` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4617` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4618` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4619` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4620` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4621` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4622` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4623` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4624` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4625` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4626` | `mcq` | false | `C` | `B. Increased immigration of foreign citizens and their families.` |
| baseline | `mmlu_4627` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4628` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4629` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4630` | `mcq` | true | `B` | `B. Subsidize the firm or its customers.` |
| baseline | `mmlu_4631` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4632` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4634` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4635` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4636` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4637` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4638` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4639` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4640` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4641` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4642` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4643` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4644` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4645` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4646` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4647` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4648` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4649` | `mcq` | false | `A` | `C. Do not produce if the TFC is not covered by revenue.` |
| baseline | `mmlu_4650` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4651` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4652` | `mcq` | true | `C` | `C. Factors of production` |
| baseline | `mmlu_4653` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4654` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4655` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4656` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4657` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4658` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4659` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4660` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4661` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4662` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4663` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4664` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4665` | `mcq` | true | `C` | `C. (P-MC)/P` |
| baseline | `mmlu_4666` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4667` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4668` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4669` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4670` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4671` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4672` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4673` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4674` | `mcq` | true | `D` | `D. I, II, III, and IV` |
| baseline | `mmlu_4675` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4676` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4677` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4678` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4679` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4680` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4681` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4682` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4683` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4684` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4685` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4686` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4688` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4689` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4690` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4691` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4692` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4693` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4694` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4695` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4696` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4697` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4698` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4699` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4700` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4701` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4702` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4703` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4704` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4705` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4706` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4707` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4708` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4709` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4710` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4711` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4712` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4713` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4714` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4715` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4716` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4717` | `mcq` | true | `B` | `B. Increases` |
| baseline | `mmlu_4718` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4719` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4720` | `mcq` | true | `A` | `A. marginal utility is zero` |
| baseline | `mmlu_4721` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4722` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4723` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4724` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4725` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4726` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4728` | `mcq` | true | `C` | `C. Supply public goods using tax dollars.` |
| baseline | `mmlu_4729` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4730` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4731` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4732` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4733` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4734` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4735` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4736` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4737` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4738` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4739` | `mcq` | false | `C` | `D. Less` |
| baseline | `mmlu_4740` | `mcq` | true | `D` | `D. (E) I, II, and III` |
| baseline | `mmlu_4741` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4742` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4743` | `mcq` | false | `C` | `D. 0.1 J` |
| baseline | `mmlu_4744` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4745` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4746` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4747` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4748` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4749` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4750` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4751` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4752` | `mcq` | true | `D` | `D. 1 m` |
| baseline | `mmlu_4753` | `mcq` | false | `C` | `B. 100 cm` |
| baseline | `mmlu_4754` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4755` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4756` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4757` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4758` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4759` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4760` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4761` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4762` | `mcq` | false | `C` | `B. 6 m/s` |
| baseline | `mmlu_4763` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4764` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4765` | `mcq` | false | `D` | `B. Decreases linearly` |
| baseline | `mmlu_4766` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4767` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4768` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4769` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4770` | `mcq` | false | `C` | `D. I & III only` |
| baseline | `mmlu_4771` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4772` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4773` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4774` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4775` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4776` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4777` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4778` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4779` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4780` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4781` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4782` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4783` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4784` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4785` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4786` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4787` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4788` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4789` | `mcq` | false | `D` | `B. Weight` |
| baseline | `mmlu_4790` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4791` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4792` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4793` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4794` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4795` | `mcq` | true | `C` | `C. 16 N` |
| baseline | `mmlu_4796` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4797` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4798` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4799` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4800` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4801` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4802` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4803` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4804` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4805` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4806` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4807` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4809` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4810` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4811` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4812` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4813` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4814` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4815` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4816` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4817` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4818` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4819` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4820` | `mcq` | false | `A` | `D. 400 μN` |
| baseline | `mmlu_4821` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4822` | `mcq` | false | `C` | `D. 60 m` |
| baseline | `mmlu_4823` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4824` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4825` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4826` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4827` | `mcq` | false | `D` | `A. Gamma rays` |
| baseline | `mmlu_4828` | `mcq` | false | `C` | `B. 1.0 m/s` |
| baseline | `mmlu_4829` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4830` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4831` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4832` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4833` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4834` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4835` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4836` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4837` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4838` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4839` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4840` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4841` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4842` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4843` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4844` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4845` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4846` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4847` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4848` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4849` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4850` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4851` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4852` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4853` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4855` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4856` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4857` | `mcq` | false | `C` | `B. 12 m/s^2` |
| baseline | `mmlu_4858` | `mcq` | false | `A` | `D. No.` |
| baseline | `mmlu_4859` | `mcq` | false | `A` | `B. 10.5 s` |
| baseline | `mmlu_4860` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_4861` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4862` | `mcq` | false | `B` | `C. Less than the field found by B.` |
| baseline | `mmlu_4863` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4864` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4865` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4866` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4867` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4868` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4869` | `mcq` | true | `B` | `B. 0.5 A` |
| baseline | `mmlu_4870` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4871` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4872` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4873` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4874` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4875` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4876` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4877` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4878` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4879` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4880` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4881` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4882` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4883` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4884` | `mcq` | false | `D` | `C. (1/5) AU` |
| baseline | `mmlu_4885` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4886` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4887` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4888` | `mcq` | true | `B` | `B. schizophrenia.` |
| baseline | `mmlu_4889` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4890` | `mcq` | true | `A` | `A. measures what it purports to measure.` |
| baseline | `mmlu_4891` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4892` | `mcq` | true | `A` | `A. 0%` |
| baseline | `mmlu_4893` | `mcq` | true | `A` | `A. variance` |
| baseline | `mmlu_4894` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4895` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4896` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4897` | `mcq` | true | `C` | `C. achievement` |
| baseline | `mmlu_4898` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4899` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4900` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4901` | `mcq` | false | `D` | `A. discrimination` |
| baseline | `mmlu_4902` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4903` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4904` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4905` | `mcq` | true | `D` | `D. bitter` |
| baseline | `mmlu_4906` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4907` | `mcq` | true | `B` | `B. a classroom test over a chapter in a textbook` |
| baseline | `mmlu_4908` | `mcq` | true | `B` | `B. suffer from sterility as an adult.` |
| baseline | `mmlu_4909` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4910` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4911` | `mcq` | true | `C` | `C. Hormones released in the womb most significantly influence a person's sexual orientation according to research.` |
| baseline | `mmlu_4912` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4913` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4914` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4915` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4916` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4918` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4919` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4920` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4921` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4922` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4923` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4924` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4925` | `mcq` | true | `C` | `C. Taste` |
| baseline | `mmlu_4926` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4927` | `mcq` | true | `B` | `B. regulating emotion.` |
| baseline | `mmlu_4928` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4929` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4930` | `mcq` | true | `B` | `B. recalling the name of your junior high school shop teacher.` |
| baseline | `mmlu_4931` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4932` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4933` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4934` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4935` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4936` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4937` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4938` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4939` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4940` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4941` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4942` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4943` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4944` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4945` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4946` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4947` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4948` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4949` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4950` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4951` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4952` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4953` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4954` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4955` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4956` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4957` | `mcq` | false | `C` | `A. Duration recording` |
| baseline | `mmlu_4958` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4959` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4960` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4961` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4962` | `mcq` | true | `D` | `D. positive psychology` |
| baseline | `mmlu_4963` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4964` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4965` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4966` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4967` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4968` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4969` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4970` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4971` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4972` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4973` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4974` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4975` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4976` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4977` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4978` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4979` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4980` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4981` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4982` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4983` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4984` | `mcq` | true | `A` | `A. M MPI - 2` |
| baseline | `mmlu_4985` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4986` | `mcq` | true | `D` | `D. Melatonin` |
| baseline | `mmlu_4987` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4988` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4989` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4990` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4991` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4992` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4993` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4994` | `mcq` | true | `B` | `B. behavioral perspective` |
| baseline | `mmlu_4995` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4996` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4997` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4998` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4999` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5000` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5001` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5002` | `mcq` | false | `C` | `A. engage in risky behavior.` |
| baseline | `mmlu_5003` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5004` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5005` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5006` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5007` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5008` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5009` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5010` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5011` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5012` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5013` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5014` | `mcq` | true | `B` | `B. standardized` |
| baseline | `mmlu_5015` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5016` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5017` | `mcq` | true | `C` | `C. Pairing an unconditioned stimulus with a conditioned stimulus.` |
| baseline | `mmlu_5018` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5019` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_5020` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5021` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5022` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5023` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5024` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5025` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5026` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5027` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5028` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5029` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5030` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5031` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5032` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5033` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5034` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5035` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5036` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5037` | `mcq` | true | `A` | `A. expectation` |
| baseline | `mmlu_5038` | `mcq` | true | `B` | `B. sublimation` |
| baseline | `mmlu_5039` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5040` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5041` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5042` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5043` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5044` | `mcq` | true | `D` | `D. hypothalamus` |
| baseline | `mmlu_5045` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5046` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5047` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5048` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5049` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5050` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5051` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5052` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5053` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5054` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5055` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5056` | `mcq` | false | `D` | `A. Bias` |
| baseline | `mmlu_5057` | `mcq` | true | `A` | `A. acquisition trials` |
| baseline | `mmlu_5058` | `mcq` | true | `A` | `A. Schizophrenia` |
| baseline | `mmlu_5059` | `mcq` | false | `C` | `A. hippocampus` |
| baseline | `mmlu_5060` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5061` | `mcq` | true | `A` | `A. amplitude of the wave` |
| baseline | `mmlu_5062` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5063` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5064` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5065` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5066` | `mcq` | true | `A` | `A. talking to a patient` |
| baseline | `mmlu_5067` | `mcq` | true | `B` | `B. acquisition` |
| baseline | `mmlu_5068` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5069` | `mcq` | false | `D` | `A. continuity` |
| baseline | `mmlu_5070` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5071` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5072` | `mcq` | true | `A` | `A. elevate mood and reduce pain` |
| baseline | `mmlu_5073` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5074` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5075` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5076` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5077` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5078` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5079` | `mcq` | false | `D` | `B. generalization.` |
| baseline | `mmlu_5080` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5081` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5082` | `mcq` | true | `C` | `C. unconcious conflicts` |
| baseline | `mmlu_5083` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5084` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5085` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5086` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5087` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5088` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5089` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5090` | `mcq` | true | `C` | `C. unconditional positive regard` |
| baseline | `mmlu_5091` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5092` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5094` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5095` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5096` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5097` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5098` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5099` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5100` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5101` | `mcq` | false | `A` | `D. association areas` |
| baseline | `mmlu_5102` | `mcq` | true | `C` | `C. reinforced` |
| baseline | `mmlu_5103` | `mcq` | false | `A` | `C. sense of time urgency` |
| baseline | `mmlu_5104` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5105` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5106` | `mcq` | true | `B` | `B. white` |
| baseline | `mmlu_5107` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5108` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5109` | `mcq` | false | `D` | `A. discrimination` |
| baseline | `mmlu_5110` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5111` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5112` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5113` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5114` | `mcq` | true | `C` | `C. thalamus` |
| baseline | `mmlu_5115` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5116` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5117` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5118` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5119` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5120` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5121` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5122` | `mcq` | false | `A` | `B. NREM sleep` |
| baseline | `mmlu_5123` | `mcq` | true | `C` | `C. Attribution theory` |
| baseline | `mmlu_5124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5125` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5126` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5127` | `mcq` | false | `C` | `A. black` |
| baseline | `mmlu_5128` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5129` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5130` | `mcq` | false | `A` | `B. simultaneous` |
| baseline | `mmlu_5131` | `mcq` | true | `A` | `A. GAD.` |
| baseline | `mmlu_5132` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5133` | `mcq` | false | `B` | `A. Recognition` |
| baseline | `mmlu_5134` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5135` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5136` | `mcq` | true | `C` | `C. Shaping` |
| baseline | `mmlu_5137` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5138` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5139` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5140` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5141` | `mcq` | true | `A` | `A. Content validity` |
| baseline | `mmlu_5142` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5143` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5144` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5145` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5146` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5147` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5148` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5149` | `mcq` | true | `D` | `D. collective unconscious` |
| baseline | `mmlu_5150` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5151` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5153` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5154` | `mcq` | true | `C` | `C. hypothalamus` |
| baseline | `mmlu_5155` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5156` | `mcq` | true | `B` | `B. chronic pain` |
| baseline | `mmlu_5157` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5158` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5159` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5160` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5161` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5162` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5163` | `mcq` | true | `C` | `C. Compliance strategy` |
| baseline | `mmlu_5164` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5165` | `mcq` | false | `B` | `A. the unconditioned stimulus without the conditioned stimulus` |
| baseline | `mmlu_5166` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5167` | `mcq` | false | `D` | `B. yellow` |
| baseline | `mmlu_5168` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5169` | `mcq` | true | `A` | `A. provide additional opportunities for students to maximize their learning` |
| baseline | `mmlu_5170` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5171` | `mcq` | true | `B` | `B. Visual imagery` |
| baseline | `mmlu_5172` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5173` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5174` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5175` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5176` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5177` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5178` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5179` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5180` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5181` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5182` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5183` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5184` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5185` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5186` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5187` | `mcq` | true | `B` | `B.nemonicdevice` |
| baseline | `mmlu_5188` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5189` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5190` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5191` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5192` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5193` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5194` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5195` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5196` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5197` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5198` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5199` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5200` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5201` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5202` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5203` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5204` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5205` | `mcq` | true | `C` | `C. leading questions` |
| baseline | `mmlu_5206` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5207` | `mcq` | true | `B` | `B. reflex` |
| baseline | `mmlu_5208` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5209` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5210` | `mcq` | true | `B` | `B. recalling the name of your junior high school shop teacher.` |
| baseline | `mmlu_5211` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5212` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5213` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5214` | `mcq` | false | `D` | `C. behaviorist` |
| baseline | `mmlu_5215` | `mcq` | true | `B` | `B. dopamine` |
| baseline | `mmlu_5216` | `mcq` | true | `B` | `B. situational` |
| baseline | `mmlu_5217` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5218` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5219` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5220` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5221` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5222` | `mcq` | true | `D` | `D. flat affect` |
| baseline | `mmlu_5223` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5224` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5225` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5226` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5227` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5228` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5229` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5230` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5231` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5232` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5233` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5234` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5235` | `mcq` | true | `D` | `D. Authoritative` |
| baseline | `mmlu_5236` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5237` | `mcq` | true | `B` | `B. double blind study` |
| baseline | `mmlu_5238` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5239` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5240` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5241` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5242` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5243` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5244` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5245` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5246` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5247` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5248` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5249` | `mcq` | false | `B` | `A. Median` |
| baseline | `mmlu_5250` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5251` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5252` | `mcq` | true | `C` | `C. Homeostasis` |
| baseline | `mmlu_5253` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5254` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5255` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5256` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5257` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5258` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5259` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5260` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5261` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5262` | `mcq` | true | `A` | `A. self-efficacy` |
| baseline | `mmlu_5263` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5264` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5265` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5266` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5267` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5268` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5269` | `mcq` | true | `D` | `D. License` |
| baseline | `mmlu_5270` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5271` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5272` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5273` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5274` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5275` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5276` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5277` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5278` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5279` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5281` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5282` | `mcq` | false | `D` | `C. focusing on the pain.` |
| baseline | `mmlu_5283` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5284` | `mcq` | true | `B` | `B. facial expressions` |
| baseline | `mmlu_5285` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5286` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5287` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5288` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5289` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5290` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5291` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5292` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5293` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5294` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5295` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5296` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5297` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5298` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5299` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5300` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5301` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5302` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5303` | `mcq` | false | `D` | `C. phoneme` |
| baseline | `mmlu_5304` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5305` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5306` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5307` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5308` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5309` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5310` | `mcq` | true | `C` | `C. Hormones released in the womb most significantly influence a person's sexual orientation according to research.` |
| baseline | `mmlu_5311` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5312` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5313` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5314` | `mcq` | true | `A` | `A. acetylcholine` |
| baseline | `mmlu_5315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5316` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5317` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5318` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5319` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5320` | `mcq` | true | `B` | `B. modeling.` |
| baseline | `mmlu_5321` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5322` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5323` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5325` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5326` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5327` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5328` | `mcq` | true | `D` | `D. Diffusion of responsibility` |
| baseline | `mmlu_5329` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5330` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5331` | `mcq` | false | `D` | `A. frequency` |
| baseline | `mmlu_5332` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5333` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5334` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5335` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5336` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5337` | `mcq` | false | `B` | `A. case study` |
| baseline | `mmlu_5338` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5339` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5340` | `mcq` | true | `C` | `C. achievement` |
| baseline | `mmlu_5341` | `mcq` | true | `A` | `A. nomothetic` |
| baseline | `mmlu_5342` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5343` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5344` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5345` | `mcq` | true | `D` | `D. sight` |
| baseline | `mmlu_5346` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5347` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5348` | `mcq` | true | `A` | `A. relative deprivation` |
| baseline | `mmlu_5349` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5350` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5351` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5353` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5354` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5355` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5356` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5357` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5358` | `mcq` | true | `D` | `D. It is important for people to voice dissent.` |
| baseline | `mmlu_5359` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5360` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5361` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5362` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5363` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5364` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5365` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5366` | `mcq` | false | `D` | `A. Experiment` |
| baseline | `mmlu_5367` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5368` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5369` | `mcq` | false | `A` | `B. crystallized intelligence` |
| baseline | `mmlu_5370` | `mcq` | true | `C` | `C. flashbulb memory` |
| baseline | `mmlu_5371` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5372` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5373` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5374` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5376` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5378` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5379` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5380` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5381` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5382` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5383` | `mcq` | false | `D` | `C. 68` |
| baseline | `mmlu_5384` | `mcq` | false | `C` | `A. frequency` |
| baseline | `mmlu_5385` | `mcq` | false | `C` | `B. 3 months` |
| baseline | `mmlu_5386` | `mcq` | false | `B` | `C. Fluid intelligence` |
| baseline | `mmlu_5387` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5388` | `mcq` | true | `B` | `B./optouch` |
| baseline | `mmlu_5389` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5390` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5391` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5392` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5393` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5394` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5395` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5396` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5397` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5398` | `mcq` | true | `A` | `A. Occipital` |
| baseline | `mmlu_5399` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5400` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5401` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5402` | `mcq` | true | `D` | `D. Changes in behavior over time` |
| baseline | `mmlu_5403` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5404` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5405` | `mcq` | true | `C` | `C. industrial/organizational` |
| baseline | `mmlu_5406` | `mcq` | true | `C` | `C. might have been due to chance` |
| baseline | `mmlu_5407` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5408` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5409` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5410` | `mcq` | true | `B` | `B. authoritative` |
| baseline | `mmlu_5411` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5412` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5413` | `mcq` | false | `C` | `A. going to lecture classes` |
| baseline | `mmlu_5414` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5415` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5416` | `mcq` | false | `D` | `C. cold` |
| baseline | `mmlu_5417` | `mcq` | true | `D` | `D. Sociocultural` |
| baseline | `mmlu_5418` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5419` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5420` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5421` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5422` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5423` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5424` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5425` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5426` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5427` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5429` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5430` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5431` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5432` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5433` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5434` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5435` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5436` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5437` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5438` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5439` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5440` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5441` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5442` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5443` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5444` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5445` | `mcq` | false | `C` | `A. increases the interval size by 9%.` |
| baseline | `mmlu_5446` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5447` | `mcq` | true | `D` | `D. I and II` |
| baseline | `mmlu_5448` | `mcq` | false | `B` | `D. III only` |
| baseline | `mmlu_5449` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5450` | `mcq` | true | `D` | `D. 0.0036` |
| baseline | `mmlu_5451` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5452` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5453` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5454` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5455` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5456` | `mcq` | false | `A` | `C. $28,000` |
| baseline | `mmlu_5457` | `mcq` | false | `D` | `B. $23,700` |
| baseline | `mmlu_5458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5459` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5460` | `mcq` | true | `D` | `D. All of the above answers are correct.` |
| baseline | `mmlu_5461` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5462` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5463` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5464` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5465` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5466` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5467` | `mcq` | true | `D` | `D. III only` |
| baseline | `mmlu_5468` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5469` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5470` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5471` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5472` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5473` | `mcq` | false | `D` | `C. 200` |
| baseline | `mmlu_5474` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5475` | `mcq` | false | `A` | `B. Sample survey` |
| baseline | `mmlu_5476` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5477` | `mcq` | false | `B` | `C. Both plans use random samples and so will produce equivalent results.` |
| baseline | `mmlu_5478` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5479` | `mcq` | false | `C` | `A. I and III only` |
| baseline | `mmlu_5480` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5481` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5482` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5483` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5484` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5485` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5486` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5487` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5488` | `mcq` | false | `A` | `D. -0.19` |
| baseline | `mmlu_5489` | `mcq` | true | `D` | `D. z = 2.40` |
| baseline | `mmlu_5490` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5491` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5492` | `mcq` | true | `C` | `C. 86.65; she qualifies.` |
| baseline | `mmlu_5493` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5494` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5495` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5496` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5497` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5498` | `mcq` | false | `B` | `D. 0.60` |
| baseline | `mmlu_5499` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5500` | `mcq` | false | `A` | `D. Any of the above is an acceptable alternative to the given null.` |
| baseline | `mmlu_5501` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5502` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5503` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5504` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5505` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5506` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5507` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5508` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5509` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5510` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5511` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5512` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5513` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5514` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5515` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5516` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5517` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5518` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5519` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5521` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5522` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5523` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5524` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5525` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5526` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5527` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5528` | `mcq` | true | `D` | `D. No, because not every group of 30 employees has the same chance of being selected.` |
| baseline | `mmlu_5529` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5530` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5532` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5533` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5534` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5535` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5536` | `mcq` | false | `C` | `B. A two-sample t-test` |
| baseline | `mmlu_5537` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5538` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5539` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5540` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5541` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5542` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5543` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5544` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5545` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5546` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5547` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5548` | `mcq` | true | `D` | `D. 156` |
| baseline | `mmlu_5549` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5550` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5551` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5552` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5553` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5554` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5555` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5556` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5557` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5558` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5559` | `mcq` | true | `D` | `D. The player will lose about $1.44.` |
| baseline | `mmlu_5560` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5561` | `mcq` | true | `D` | `D. 0.94` |
| baseline | `mmlu_5562` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5563` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5564` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5565` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5566` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5567` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5568` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5569` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5570` | `mcq` | true | `D` | `D. No, because not every sample of the intended size has an equal chance of being selected.` |
| baseline | `mmlu_5571` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5572` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5573` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5574` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5575` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5576` | `mcq` | true | `D` | `D. 0.91` |
| baseline | `mmlu_5577` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5578` | `mcq` | true | `D` | `D. No, because the entire population information was used from both offices. Because no samples were taken, a t-test sho` |
| baseline | `mmlu_5579` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5580` | `mcq` | true | `D` | `D. No, because grade level is a lurking variable which may well be confounded with the variables under consideration.` |
| baseline | `mmlu_5581` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5582` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5583` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5584` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5585` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5586` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5587` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5588` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5589` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5590` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5591` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5592` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5593` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5594` | `mcq` | false | `B` | `C. 0.24` |
| baseline | `mmlu_5595` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5596` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5597` | `mcq` | false | `D` | `C. 0.95` |
| baseline | `mmlu_5598` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5599` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5600` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5601` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5602` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5603` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5604` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5605` | `mcq` | false | `C` | `D. 40` |
| baseline | `mmlu_5606` | `mcq` | true | `B` | `B. The sample mean and sample median are equal.` |
| baseline | `mmlu_5607` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5608` | `mcq` | false | `D` | `B. 0.540` |
| baseline | `mmlu_5609` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5610` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5611` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5612` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5613` | `mcq` | false | `D` | `B. the skewed salary distribution tells us that assumption of normality of the sampled population will not be satisfied.` |
| baseline | `mmlu_5614` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5615` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5616` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5617` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5618` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5619` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5620` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5621` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5622` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5623` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5624` | `mcq` | false | `C` | `B. Use the 88 who did respond, using 120 as the sample size in the analysis.` |
| baseline | `mmlu_5625` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5626` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5627` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5628` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5629` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5630` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5631` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5632` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5633` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5634` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5635` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5636` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5637` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5638` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5639` | `mcq` | false | `A` | `D. I only` |
| baseline | `mmlu_5640` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5641` | `mcq` | false | `C` | `D. 6` |
| baseline | `mmlu_5642` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5643` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5644` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5645` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5646` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5647` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5648` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5649` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5650` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5651` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5652` | `mcq` | true | `B` | `B. Launching the Second New Deal, a series of legislative acts including Social Security` |
| baseline | `mmlu_5653` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5654` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5655` | `mcq` | true | `A` | `A. The Social Gospel` |
| baseline | `mmlu_5656` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5658` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5659` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5660` | `mcq` | false | `A` | `C. all Christians only` |
| baseline | `mmlu_5661` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5662` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5663` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5664` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5665` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5666` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5668` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5669` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5670` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5671` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5672` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5673` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5674` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5675` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5676` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5678` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5679` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5680` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5681` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5683` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5684` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5685` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5686` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5688` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5689` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5690` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5691` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5692` | `mcq` | true | `C` | `C. William M. Tweed` |
| baseline | `mmlu_5693` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5694` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_5695` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5696` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5697` | `mcq` | true | `A` | `A. The care of the mentally ill is a state concern.` |
| baseline | `mmlu_5698` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5699` | `mcq` | true | `D` | `D. Mutually beneficial relations` |
| baseline | `mmlu_5700` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5702` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5703` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5704` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5705` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5706` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5707` | `mcq` | true | `C` | `C. Christopher Columbus was not the first European to have explored North America.` |
| baseline | `mmlu_5708` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5709` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5710` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5712` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5713` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5714` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5715` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5716` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5717` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5718` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5719` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5721` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5722` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5723` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5724` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5725` | `mcq` | true | `D` | `D. New Dealers of the 1930s` |
| baseline | `mmlu_5726` | `mcq` | true | `D` | `D. Ireland` |
| baseline | `mmlu_5727` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5728` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5729` | `mcq` | true | `B` | `B. challenged traditional understandings of women and property embodied in the legal concept of femme covert.` |
| baseline | `mmlu_5730` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5731` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5732` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5733` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5734` | `mcq` | true | `B` | `B. Expanding territories under Spanish control` |
| baseline | `mmlu_5735` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5736` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5737` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5738` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5739` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5740` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5741` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5742` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5743` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5744` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5745` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5746` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5747` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5748` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5749` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5750` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5751` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5752` | `mcq` | true | `D` | `D. Declaration of Independence.` |
| baseline | `mmlu_5753` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5754` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5755` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5756` | `mcq` | true | `A` | `A. Iraqi dictator Saddam Hussein's conquest of Kuwait` |
| baseline | `mmlu_5757` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5758` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5759` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5760` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5761` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5762` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5763` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5764` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5765` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5766` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5767` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5769` | `mcq` | true | `B` | `B. Evangelical Christianity.` |
| baseline | `mmlu_5770` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5771` | `mcq` | true | `C` | `C. powerful nations have a moral duty to govern less developed nations.` |
| baseline | `mmlu_5772` | `mcq` | false | `C` | `B. The Fundamental Orders` |
| baseline | `mmlu_5773` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5775` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5776` | `mcq` | false | `B` | `A. violated the Constitutional injunction against bills of attainder.` |
| baseline | `mmlu_5777` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5778` | `mcq` | true | `C` | `C. Increased economic and political opportunities for women` |
| baseline | `mmlu_5779` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5780` | `mcq` | true | `B` | `B. The Executive Order 9066 interning Japanese Americans` |
| baseline | `mmlu_5781` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5782` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5783` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5784` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5785` | `mcq` | true | `C` | `C. Spanish-American War` |
| baseline | `mmlu_5786` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5787` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5788` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5789` | `mcq` | true | `A` | `A. An opponent of big government in the 1930s` |
| baseline | `mmlu_5790` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5791` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5792` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5793` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5794` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5795` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5796` | `mcq` | true | `B` | `B. immigration quotas` |
| baseline | `mmlu_5797` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5798` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5799` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5800` | `mcq` | false | `B` | `A. Social Darwinism.` |
| baseline | `mmlu_5801` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5802` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5803` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5804` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5805` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5806` | `mcq` | false | `A` | `B. Supportive of the policies of Thomas Jefferson` |
| baseline | `mmlu_5807` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5808` | `mcq` | true | `B` | `B. The growth of corporate power and banking interests inspired rural activists to lobby for political reform.` |
| baseline | `mmlu_5809` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5810` | `mcq` | true | `A` | `A. The rise of the United States to the status of a great power` |
| baseline | `mmlu_5811` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5812` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5813` | `mcq` | false | `C` | `B. masters of their Constitution` |
| baseline | `mmlu_5814` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5815` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5816` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5817` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5818` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5819` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5820` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5821` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5822` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5823` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5824` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5825` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5826` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5827` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5828` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5829` | `mcq` | true | `B` | `B. Equal Rights Amendment.` |
| baseline | `mmlu_5830` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5831` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5832` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5833` | `mcq` | true | `A` | `A. Support for Manifest Destiny` |
| baseline | `mmlu_5834` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5835` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5836` | `mcq` | true | `C` | `C. Quakers` |
| baseline | `mmlu_5837` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5838` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5839` | `mcq` | false | `D` | `B. Respecting Indian territory and sovereignty` |
| baseline | `mmlu_5840` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5841` | `mcq` | true | `A` | `A. Many Southern and Eastern Europeans turned to America for financial gain and political freedom.` |
| baseline | `mmlu_5842` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5843` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5844` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5845` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5846` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5847` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5848` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5849` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5850` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5851` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5852` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5853` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5854` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5855` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5856` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5857` | `mcq` | true | `C` | `C. Cynical, enthusiastic` |
| baseline | `mmlu_5858` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5859` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5860` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5861` | `mcq` | true | `B` | `B. can be viewed as a reaction to the systemic brute force with which the British governed India.` |
| baseline | `mmlu_5862` | `mcq` | true | `B` | `B. He doesn't earn enough on his own.` |
| baseline | `mmlu_5863` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5864` | `mcq` | false | `A` | `C. Sever its responsibility to protect citizens who chose to live in South Africa` |
| baseline | `mmlu_5865` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5866` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5867` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5868` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5869` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5870` | `mcq` | false | `B` | `A. Adroit diplomacy and establishment of client relationships with bordering nomads` |
| baseline | `mmlu_5871` | `mcq` | false | `A` | `B. Expansion of bureaucracy to reinforce dominance` |
| baseline | `mmlu_5872` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5873` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5874` | `mcq` | true | `B` | `B. Nonviolent resistance` |
| baseline | `mmlu_5875` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5876` | `mcq` | false | `B` | `C. Competition with European trade networks` |
| baseline | `mmlu_5877` | `mcq` | false | `A` | `B. The use of religion to justify armed violence.` |
| baseline | `mmlu_5878` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5879` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5880` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5881` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5882` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5883` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5884` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5885` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5886` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5887` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5888` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5889` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5890` | `mcq` | false | `D` | `A. Highlight the extent of the author's property losses` |
| baseline | `mmlu_5891` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5892` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5893` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5894` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5895` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5896` | `mcq` | true | `D` | `D. Socialism` |
| baseline | `mmlu_5897` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5898` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5899` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5900` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5901` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5902` | `mcq` | true | `A` | `A. Russia was excluded from Western European developments (like the Renaissance).` |
| baseline | `mmlu_5903` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5904` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5905` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5906` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5907` | `mcq` | false | `B` | `D. John Wycliffe` |
| baseline | `mmlu_5908` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5909` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5910` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5911` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5912` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5913` | `mcq` | false | `A` | `C. He had lost the blessing of the gods.` |
| baseline | `mmlu_5914` | `mcq` | false | `C` | `A. They required the cultural assimilation of conquered peoples to limit diversity within the empire.` |
| baseline | `mmlu_5915` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5916` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5918` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5919` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5920` | `mcq` | true | `A` | `A. The rise of a literate class of scribes in cities who could record poems.` |
| baseline | `mmlu_5921` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5922` | `mcq` | true | `D` | `D. The New World` |
| baseline | `mmlu_5923` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5924` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5925` | `mcq` | true | `A` | `A. Rulers derived legitimacy for their rule by their sponsorship of religion and chief priests.` |
| baseline | `mmlu_5926` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5927` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5928` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5929` | `mcq` | true | `B` | `B. They study Islamic law faithfully.` |
| baseline | `mmlu_5930` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5931` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5932` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5933` | `mcq` | false | `C` | `B. The independence movements that freed the states of southeast Asia from colonial rule.` |
| baseline | `mmlu_5934` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5935` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5936` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5937` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5938` | `mcq` | true | `A` | `A. Rigid societal gender roles` |
| baseline | `mmlu_5939` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5940` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5941` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5942` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5943` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5944` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5945` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5946` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5947` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5948` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5949` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5950` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5951` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5952` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5953` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5954` | `mcq` | false | `A` | `B. proposed a heavenly existence after death.` |
| baseline | `mmlu_5955` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5956` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5957` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5958` | `mcq` | true | `A` | `A. Laissez-faire` |
| baseline | `mmlu_5959` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5960` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5961` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5962` | `mcq` | false | `B` | `A. Transformation of the social class structure` |
| baseline | `mmlu_5963` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5964` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5965` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5966` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5967` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5968` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5969` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5970` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5971` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5972` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5973` | `mcq` | false | `D` | `A. Pressure on colonial powers by the Soviet Union to retreat from their colonies` |
| baseline | `mmlu_5974` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5975` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5976` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5977` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5978` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5979` | `mcq` | false | `A` | `C. Armed intervention on the part of the Cold War superpowers.` |
| baseline | `mmlu_5980` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5981` | `mcq` | true | `B` | `B. The fight for independence in South America` |
| baseline | `mmlu_5982` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5983` | `mcq` | true | `A` | `A. Policies of religious toleration` |
| baseline | `mmlu_5984` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5985` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5986` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5987` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5988` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5989` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5990` | `mcq` | true | `C` | `C. contact with Muslim trade caravans.` |
| baseline | `mmlu_5991` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5992` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5993` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5994` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5995` | `mcq` | true | `C` | `C. World War II` |
| baseline | `mmlu_5996` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5997` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5998` | `mcq` | false | `C` | `A. All adult men born within the geographic boundaries of the state` |
| baseline | `mmlu_5999` | `mcq` | true | `C` | `C. Decolonization` |
| baseline | `mmlu_6000` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6001` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6002` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6003` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6004` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6005` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6007` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6008` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6009` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6010` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6011` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6012` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6013` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6014` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6015` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6016` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6017` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6018` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6019` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6020` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6021` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6022` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6023` | `mcq` | false | `D` | `B. The importance of ancestor worship.` |
| baseline | `mmlu_6024` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6025` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6026` | `mcq` | true | `C` | `C. Large-scale military losses and resentment of the working classes` |
| baseline | `mmlu_6027` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6028` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6029` | `mcq` | true | `A` | `A. European maritime exploration` |
| baseline | `mmlu_6030` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6031` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6032` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6033` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6034` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6035` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6036` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6037` | `mcq` | true | `D` | `D. Furs` |
| baseline | `mmlu_6038` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6039` | `mcq` | true | `B` | `B. The election of Nelson Mandela` |
| baseline | `mmlu_6040` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6041` | `mcq` | true | `B` | `B. Some elites converted to Islam, but lower classes kept their traditional beliefs.` |
| baseline | `mmlu_6042` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6043` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6044` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6045` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6046` | `mcq` | false | `C` | `A. Gave over his crown to King Ferdinand` |
| baseline | `mmlu_6047` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6048` | `mcq` | false | `D` | `C. Limited economic opportunities` |
| baseline | `mmlu_6049` | `mcq` | false | `B` | `A. The conquest of India by rival Muslim empires` |
| baseline | `mmlu_6050` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6051` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6052` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6053` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6054` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6055` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6056` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6057` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6058` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6059` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6060` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6061` | `mcq` | true | `B` | `B. The adaptation of Western literary forms by non-Western authors.` |
| baseline | `mmlu_6062` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6063` | `mcq` | false | `D` | `A. The Space Race with the United States` |
| baseline | `mmlu_6064` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6065` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6066` | `mcq` | true | `B` | `B. The compass` |
| baseline | `mmlu_6067` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6068` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6069` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6070` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6071` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6072` | `mcq` | true | `A` | `A. European merchants were confined to a few cities designated for foreign trade.` |
| baseline | `mmlu_6073` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6074` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6075` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6076` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6077` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6078` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6079` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6080` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6081` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6082` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6083` | `mcq` | true | `A` | `A. The competing ideologies of the Cold War` |
| baseline | `mmlu_6084` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6085` | `mcq` | true | `C` | `C. Labor unions` |
| baseline | `mmlu_6086` | `mcq` | true | `C` | `C. They had no interest in the products that Great Britain could provide.` |
| baseline | `mmlu_6087` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6088` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6089` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6090` | `mcq` | true | `B` | `B. Eating fish` |
| baseline | `mmlu_6091` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6092` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6094` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6095` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6096` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6097` | `mcq` | true | `A` | `A. Practice regular aerobic exercise` |
| baseline | `mmlu_6098` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6099` | `mcq` | true | `A` | `A. Many pessimists die at a younger age` |
| baseline | `mmlu_6100` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6101` | `mcq` | false | `B` | `C. Hormonal factors such as loss of estrogen.` |
| baseline | `mmlu_6102` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6103` | `mcq` | true | `B` | `B. B6 and B12` |
| baseline | `mmlu_6104` | `mcq` | true | `B` | `B. Identity` |
| baseline | `mmlu_6105` | `mcq` | false | `C` | `B. Social support` |
| baseline | `mmlu_6106` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6107` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6108` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6109` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6110` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6111` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6112` | `mcq` | true | `B` | `B. Neuroticism` |
| baseline | `mmlu_6113` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6114` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6115` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6116` | `mcq` | true | `A` | `A. Men than women` |
| baseline | `mmlu_6117` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6118` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6119` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6120` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6121` | `mcq` | true | `A` | `A. Normal metabolism` |
| baseline | `mmlu_6122` | `mcq` | true | `A` | `A. Ageism` |
| baseline | `mmlu_6123` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6124` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6125` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6126` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6127` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6128` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6129` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6130` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6131` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6132` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6133` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6134` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6135` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6136` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6137` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6138` | `mcq` | true | `A` | `A. Alone` |
| baseline | `mmlu_6139` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6140` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6141` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6142` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6143` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6144` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6145` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6146` | `mcq` | false | `B` | `A. Heart` |
| baseline | `mmlu_6147` | `mcq` | false | `D` | `B. Working` |
| baseline | `mmlu_6148` | `mcq` | false | `C` | `B. Show high satisfaction that steadily declines as the years pass` |
| baseline | `mmlu_6149` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6150` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6151` | `mcq` | true | `C` | `C. Older adults smoke less than younger adults.` |
| baseline | `mmlu_6152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6153` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6154` | `mcq` | false | `B` | `D. They change quite a lot` |
| baseline | `mmlu_6155` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6156` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6157` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6158` | `mcq` | false | `B` | `C. Florida` |
| baseline | `mmlu_6159` | `mcq` | false | `B` | `A. Traits` |
| baseline | `mmlu_6160` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6161` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6163` | `mcq` | false | `A` | `Prevalence` |
| baseline | `mmlu_6164` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6165` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6166` | `mcq` | true | `B` | `B. About 25%` |
| baseline | `mmlu_6167` | `mcq` | true | `B` | `B. Internal` |
| baseline | `mmlu_6168` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6169` | `mcq` | true | `B` | `B. Arthritis` |
| baseline | `mmlu_6170` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6171` | `mcq` | false | `A` | `B. 25%` |
| baseline | `mmlu_6172` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6173` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6174` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6175` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6176` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6177` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6178` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6179` | `mcq` | true | `B` | `B. Education about older adults` |
| baseline | `mmlu_6180` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6181` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6182` | `mcq` | true | `B` | `B. Nicotinic acid is known for lowering LDL (bad) cholesterol levels in the body.` |
| baseline | `mmlu_6183` | `mcq` | false | `B` | `D. Clinical depression` |
| baseline | `mmlu_6184` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6185` | `mcq` | false | `A` | `B. Increase insomnia` |
| baseline | `mmlu_6186` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6187` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6188` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6189` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6190` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6191` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6192` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6193` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6194` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6195` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6196` | `mcq` | true | `C` | `C. Japan` |
| baseline | `mmlu_6197` | `mcq` | true | `C` | `C. Complex` |
| baseline | `mmlu_6198` | `mcq` | true | `B` | `B. Internal` |
| baseline | `mmlu_6199` | `mcq` | false | `A` | `Living will` |
| baseline | `mmlu_6200` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6201` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6202` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6203` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6204` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6205` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6206` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6207` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6208` | `mcq` | true | `B` | `B. MMTI (Minnesota Multiperception Test for Children)` |
| baseline | `mmlu_6209` | `mcq` | false | `B` | `A. Accuracy` |
| baseline | `mmlu_6210` | `mcq` | true | `A` | `A. Japan` |
| baseline | `mmlu_6211` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6212` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6213` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6214` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6215` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6216` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6217` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6218` | `mcq` | false | `A` | `B. Some animals show little or no senescence` |
| baseline | `mmlu_6219` | `mcq` | false | `A` | `C. Changes in hormone levels` |
| baseline | `mmlu_6220` | `mcq` | true | `A` | `A. Stress and loss of social support` |
| baseline | `mmlu_6221` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6223` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6224` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6225` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6226` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6227` | `mcq` | true | `A` | `A. Activities of Daily Living` |
| baseline | `mmlu_6228` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6229` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6230` | `mcq` | true | `A` | `A. Jeanne Calment` |
| baseline | `mmlu_6231` | `mcq` | true | `A` | `A. Fluid pressure in the eye is above normal.` |
| baseline | `mmlu_6232` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6233` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6234` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6235` | `mcq` | false | `A` | `C. Size of our social networks` |
| baseline | `mmlu_6236` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6237` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6238` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6239` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6240` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6241` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6242` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6243` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6244` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6245` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6246` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6247` | `mcq` | true | `A` | `A. Age` |
| baseline | `mmlu_6248` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6249` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6250` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6251` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6252` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6253` | `mcq` | false | `A` | `D. More than 50%` |
| baseline | `mmlu_6254` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6255` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6256` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6257` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6258` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6259` | `mcq` | true | `C` | `C. Ergonomic` |
| baseline | `mmlu_6260` | `mcq` | true | `B` | `B. Medicaid` |
| baseline | `mmlu_6261` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6262` | `mcq` | false | `C` | `A. Ask about their satisfaction with life and offer to help.` |
| baseline | `mmlu_6263` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6264` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6265` | `mcq` | true | `B` | `B. Personal control` |
| baseline | `mmlu_6266` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6267` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6268` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6269` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6270` | `mcq` | true | `B` | `B. Cardiovascular disease` |
| baseline | `mmlu_6271` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6272` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6273` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6274` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6275` | `mcq` | true | `C` | `C. More than 50%` |
| baseline | `mmlu_6276` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6277` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6278` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6279` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6280` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6281` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6282` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6283` | `mcq` | false | `A` | `B. 82` |
| baseline | `mmlu_6284` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6285` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6286` | `mcq` | true | `A` | `A. Height` |
| baseline | `mmlu_6287` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6288` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6289` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6290` | `mcq` | true | `C` | `C. Pretty much stays the same` |
| baseline | `mmlu_6291` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6292` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6293` | `mcq` | true | `B` | `B. SOD` |
| baseline | `mmlu_6294` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6295` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6296` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6297` | `mcq` | false | `D` | `A. Discrimination` |
| baseline | `mmlu_6298` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6299` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6300` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6301` | `mcq` | false | `C` | `B. Is 65` |
| baseline | `mmlu_6302` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6303` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6304` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6305` | `mcq` | false | `D` | `C. Be less productive` |
| baseline | `mmlu_6306` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6307` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6308` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6309` | `mcq` | true | `A` | `A. Social support` |
| baseline | `mmlu_6310` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6311` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6312` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6313` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6314` | `mcq` | false | `A` | `A/B/C/D` |
| baseline | `mmlu_6315` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6316` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6317` | `mcq` | true | `C` | `C. experienced guilt` |
| baseline | `mmlu_6318` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6319` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6320` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6321` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6322` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6323` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6325` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6326` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6327` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6328` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6329` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6330` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6331` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6332` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6333` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6334` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6335` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6336` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6337` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6338` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6339` | `mcq` | true | `C` | `C. Hormones` |
| baseline | `mmlu_6340` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6341` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6342` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6343` | `mcq` | false | `D` | `B. immediately before orgasm` |
| baseline | `mmlu_6344` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6345` | `mcq` | false | `A` | `C. Swedish` |
| baseline | `mmlu_6346` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6347` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6348` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6349` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6350` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6351` | `mcq` | false | `D` | `C. sympathetic` |
| baseline | `mmlu_6352` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6353` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6354` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6355` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6356` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6357` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6358` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6359` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6360` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6361` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6362` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6363` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6364` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6365` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6366` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6367` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6368` | `mcq` | true | `B` | `B. necrophilia` |
| baseline | `mmlu_6369` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6370` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6371` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6372` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6373` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6374` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6376` | `mcq` | false | `B` | `C. 6` |
| baseline | `mmlu_6377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6378` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6379` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6380` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6381` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6382` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6383` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6384` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6385` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6386` | `mcq` | true | `D` | `D. gonorrhea` |
| baseline | `mmlu_6387` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6388` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6389` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6390` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6391` | `mcq` | false | `D` | `C. decreased sperm production` |
| baseline | `mmlu_6392` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6393` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6394` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6395` | `mcq` | false | `B` | `A. woman-on-top` |
| baseline | `mmlu_6396` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6397` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6398` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6399` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6401` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6402` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6403` | `mcq` | true | `B` | `B. reproduction` |
| baseline | `mmlu_6404` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6405` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6406` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6407` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6408` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6409` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6410` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6411` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6412` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6413` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6414` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6415` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6416` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6417` | `mcq` | false | `B` | `C. 15` |
| baseline | `mmlu_6418` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6419` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6420` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6421` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6422` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6423` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6424` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6425` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6426` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6427` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6429` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6430` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_6431` | `mcq` | true | `A` | `A. directly into the bloodstream` |
| baseline | `mmlu_6432` | `mcq` | true | `A` | `A. 1` |
| baseline | `mmlu_6433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6434` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6435` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6436` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6437` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6438` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6439` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6440` | `mcq` | false | `D` | `C. gonorrhea` |
| baseline | `mmlu_6441` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6442` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6443` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6444` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6445` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6446` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6447` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6448` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6449` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6450` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6451` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6452` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6453` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6454` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6455` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6456` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6457` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6459` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6460` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6461` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6462` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6463` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6464` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6465` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6466` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6467` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6468` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6469` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6470` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6471` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6472` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6473` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6474` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6475` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6476` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6477` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6478` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6479` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6480` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6481` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6482` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6483` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6484` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6485` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6486` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6487` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6488` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6489` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6490` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6491` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6492` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6493` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6495` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6496` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6497` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6498` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6499` | `mcq` | true | `B` | `B` |
