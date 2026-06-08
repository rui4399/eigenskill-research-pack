# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `11000`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 6554 / 11000 | 0.5958 | 5.0045 | 0.403427 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `A. 8` |
| baseline | `mmlu_2` | `mcq` | true | `D` | `D. 0,4` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `C. True, False` |
| baseline | `mmlu_8` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11` | `mcq` | false | `C` | `A. symmetric only` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13` | `mcq` | true | `C` | `C. (x + 1)(x − 4)(x − 2)` |
| baseline | `mmlu_14` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_16` | `mcq` | false | `C` | `D. -i` |
| baseline | `mmlu_17` | `mcq` | true | `C` | `C. (1,6)` |
| baseline | `mmlu_18` | `mcq` | false | `D` | `C. identity element does not exist` |
| baseline | `mmlu_19` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_20` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_21` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_22` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_23` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_24` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_25` | `mcq` | false | `C` | `D. infinite, abelian` |
| baseline | `mmlu_26` | `mcq` | true | `C` | `C. True, False` |
| baseline | `mmlu_27` | `mcq` | false | `B` | `D. No.` |
| baseline | `mmlu_28` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_29` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_30` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_31` | `mcq` | true | `B` | `B. abelian group` |
| baseline | `mmlu_32` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_33` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `D. False, True` |
| baseline | `mmlu_35` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_36` | `mcq` | false | `D` | `C. 11` |
| baseline | `mmlu_37` | `mcq` | false | `B` | `A. Yes, with p=2.` |
| baseline | `mmlu_38` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_39` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `A. 0` |
| baseline | `mmlu_41` | `mcq` | false | `A` | `B. 3` |
| baseline | `mmlu_42` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_43` | `mcq` | false | `C` | `D. False, True` |
| baseline | `mmlu_44` | `mcq` | false | `C` | `D. False, True` |
| baseline | `mmlu_45` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_47` | `mcq` | false | `B` | `A. 0` |
| baseline | `mmlu_48` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_49` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_50` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_51` | `mcq` | false | `B` | `A. 0` |
| baseline | `mmlu_52` | `mcq` | false | `A` | `D. 2` |
| baseline | `mmlu_53` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_54` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_55` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_56` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_57` | `mcq` | true | `B` | `B. 2` |
| baseline | `mmlu_58` | `mcq` | false | `A` | `C. True, False` |
| baseline | `mmlu_59` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_60` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_61` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_62` | `mcq` | false | `C` | `D. False, True` |
| baseline | `mmlu_63` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_64` | `mcq` | false | `B` | `A. 1` |
| baseline | `mmlu_65` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_66` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_67` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_68` | `mcq` | false | `A` | `C. (x-1)(x+1)^3` |
| baseline | `mmlu_69` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_70` | `mcq` | false | `D` | `C. a-2` |
| baseline | `mmlu_71` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_72` | `mcq` | false | `D` | `A. 1` |
| baseline | `mmlu_73` | `mcq` | false | `B` | `A. 0` |
| baseline | `mmlu_74` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_75` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_76` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_77` | `mcq` | true | `A` | `A. 0` |
| baseline | `mmlu_78` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_79` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_80` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_81` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_82` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_83` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_84` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_85` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_86` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_87` | `mcq` | true | `A` | `A. -19` |
| baseline | `mmlu_88` | `mcq` | true | `A` | `A. 0` |
| baseline | `mmlu_89` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_90` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_91` | `mcq` | true | `B` | `B. 4Z, 2 + 4Z` |
| baseline | `mmlu_92` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_93` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_94` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_95` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_96` | `mcq` | false | `B` | `C. 0,1` |
| baseline | `mmlu_97` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_98` | `mcq` | false | `C` | `A. 4` |
| baseline | `mmlu_99` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_100` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_101` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_102` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_103` | `mcq` | false | `C` | `B. Skeletal muscles` |
| baseline | `mmlu_104` | `mcq` | true | `B` | `B. Glomerulus` |
| baseline | `mmlu_105` | `mcq` | false | `B` | `D. Breathing will be unaffected.` |
| baseline | `mmlu_106` | `mcq` | false | `A` | `B. Hypochondriac` |
| baseline | `mmlu_107` | `mcq` | true | `B` | `B. Mucous membranes` |
| baseline | `mmlu_108` | `mcq` | false | `C` | `B. eight weeks post-fertilization.` |
| baseline | `mmlu_109` | `mcq` | true | `D` | `D. contraction of contralateral limb musculature.` |
| baseline | `mmlu_110` | `mcq` | true | `D` | `D. hard palate, upper lip, upper central incisor and lower first molar.` |
| baseline | `mmlu_111` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_112` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_113` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_114` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_115` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_116` | `mcq` | true | `B` | `B. External intercostal muscles and diaphragm` |
| baseline | `mmlu_117` | `mcq` | true | `D` | `D. Testes` |
| baseline | `mmlu_118` | `mcq` | false | `D` | `A. Aorta` |
| baseline | `mmlu_119` | `mcq` | true | `C` | `C. Trachea` |
| baseline | `mmlu_120` | `mcq` | true | `C` | `C. In the upper wall of the right atrium` |
| baseline | `mmlu_121` | `mcq` | false | `C` | `A. deep to its superior border.` |
| baseline | `mmlu_122` | `mcq` | false | `B` | `A. left submental lymph node.` |
| baseline | `mmlu_123` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_124` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_125` | `mcq` | true | `C` | `C. Nitrogen` |
| baseline | `mmlu_126` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_127` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_128` | `mcq` | true | `C` | `C. Spleen` |
| baseline | `mmlu_129` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_130` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_131` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_132` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_133` | `mcq` | false | `B` | `D. Prone` |
| baseline | `mmlu_134` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_135` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_136` | `mcq` | true | `D` | `D. Spleen` |
| baseline | `mmlu_137` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_138` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_139` | `mcq` | true | `C` | `C. Liver` |
| baseline | `mmlu_140` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_141` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_142` | `mcq` | true | `B` | `B. Femur` |
| baseline | `mmlu_143` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_144` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_145` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_146` | `mcq` | true | `B` | `B. Lower leg` |
| baseline | `mmlu_147` | `mcq` | true | `C` | `C. Erythrocyte` |
| baseline | `mmlu_148` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_149` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_150` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_151` | `mcq` | false | `D` | `A. The phrenic nerves` |
| baseline | `mmlu_152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_153` | `mcq` | false | `B` | `A. caudal` |
| baseline | `mmlu_154` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_155` | `mcq` | false | `D` | `B. Outward` |
| baseline | `mmlu_156` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_157` | `mcq` | true | `C` | `C. Peristalsis` |
| baseline | `mmlu_158` | `mcq` | true | `D` | `D. Synapse` |
| baseline | `mmlu_159` | `mcq` | false | `D` | `A. Masseter` |
| baseline | `mmlu_160` | `mcq` | true | `D` | `D. Pancreas` |
| baseline | `mmlu_161` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_162` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_163` | `mcq` | true | `C` | `C. Pulmonary arteries` |
| baseline | `mmlu_164` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_165` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_166` | `mcq` | true | `D` | `D. On the anterior side of the neck` |
| baseline | `mmlu_167` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_168` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_169` | `mcq` | false | `B` | `A. The incisive nerve` |
| baseline | `mmlu_170` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_171` | `mcq` | true | `A` | `A. Acetylcholine` |
| baseline | `mmlu_172` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_173` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_174` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_175` | `mcq` | true | `C` | `C. atrophy` |
| baseline | `mmlu_176` | `mcq` | true | `A` | `A. spastic paralysis.` |
| baseline | `mmlu_177` | `mcq` | true | `A` | `A. right lung because the right main bronchus is wider and more vertical than the left.` |
| baseline | `mmlu_178` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_179` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_180` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_181` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_182` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_183` | `mcq` | true | `B` | `B. Epiglottis` |
| baseline | `mmlu_184` | `mcq` | false | `B` | `A. The roof` |
| baseline | `mmlu_185` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_186` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_187` | `mcq` | false | `C` | `B. muscles of the soft palate.` |
| baseline | `mmlu_188` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_189` | `mcq` | true | `A` | `A. Collagen` |
| baseline | `mmlu_190` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_191` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_193` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_194` | `mcq` | false | `A` | `B. Right lateral pterygoid muscle` |
| baseline | `mmlu_195` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_196` | `mcq` | true | `A` | `A. third cranial nerves.` |
| baseline | `mmlu_197` | `mcq` | false | `C` | `A. light pink in color on both sides of the mucogingival junction.` |
| baseline | `mmlu_198` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_199` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_200` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_201` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_202` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_203` | `mcq` | false | `B` | `A. The ribs` |
| baseline | `mmlu_204` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_205` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_206` | `mcq` | true | `C` | `C. Spleen` |
| baseline | `mmlu_207` | `mcq` | false | `D` | `B. synovial membrane and capsule.` |
| baseline | `mmlu_208` | `mcq` | true | `D` | `D. Respiration` |
| baseline | `mmlu_209` | `mcq` | true | `A` | `A. skull bones and dura mater.` |
| baseline | `mmlu_210` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_211` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_212` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_213` | `mcq` | true | `A` | `A. Alveoli` |
| baseline | `mmlu_214` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_215` | `mcq` | true | `B` | `B. Fallopian tube` |
| baseline | `mmlu_216` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_217` | `mcq` | true | `B` | `B. Prostate` |
| baseline | `mmlu_218` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_219` | `mcq` | true | `D` | `D. The cerebellum` |
| baseline | `mmlu_220` | `mcq` | true | `C` | `C. Ileum` |
| baseline | `mmlu_221` | `mcq` | false | `B` | `A. posterior and medial to medial pterygoid.` |
| baseline | `mmlu_222` | `mcq` | true | `C` | `C. Pernicious anemia` |
| baseline | `mmlu_223` | `mcq` | false | `B` | `A. The maxillary bone` |
| baseline | `mmlu_224` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_225` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_226` | `mcq` | true | `C` | `C. Olfactory` |
| baseline | `mmlu_227` | `mcq` | true | `C` | `C. medulla oblongata` |
| baseline | `mmlu_228` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_229` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_230` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_231` | `mcq` | true | `D` | `D. Pituitary` |
| baseline | `mmlu_232` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_233` | `mcq` | true | `C` | `C. Urethra` |
| baseline | `mmlu_234` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_235` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_236` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_237` | `mcq` | true | `C` | `C. Because the atmosphere preferentially scatters short wavelengths.` |
| baseline | `mmlu_238` | `mcq` | true | `C` | `C. You can never prove your theory to be correct only "yet to be proven wrong".` |
| baseline | `mmlu_239` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_240` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_241` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_242` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_243` | `mcq` | false | `D` | `B. Hydrogen` |
| baseline | `mmlu_244` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_245` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_246` | `mcq` | true | `C` | `C. By comparing the maximum altitude of the Sun in two cities at different latitudes at the same time on the same day.` |
| baseline | `mmlu_247` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_248` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_249` | `mcq` | true | `B` | `B. Laniakea` |
| baseline | `mmlu_250` | `mcq` | true | `C` | `C. Jupiter` |
| baseline | `mmlu_251` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_252` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_253` | `mcq` | true | `D` | `D. A and B only` |
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
| baseline | `mmlu_264` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_265` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_266` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_267` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_268` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_269` | `mcq` | true | `C` | `C. The two stars will look like a single point of light.` |
| baseline | `mmlu_270` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_271` | `mcq` | true | `A` | `A. The path of the Sun in the sky throughout a year.` |
| baseline | `mmlu_272` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_273` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_274` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_275` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_276` | `mcq` | true | `D` | `D. Sagittarius A*` |
| baseline | `mmlu_277` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_278` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_279` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_280` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_281` | `mcq` | true | `D` | `D. From radioactive dating of rocks and meteorites.` |
| baseline | `mmlu_282` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_283` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_284` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_285` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_286` | `mcq` | true | `D` | `D. 9:4` |
| baseline | `mmlu_287` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_288` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_289` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_290` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_291` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_292` | `mcq` | true | `D` | `D. There is no solar day Planet X is tidally locked` |
| baseline | `mmlu_293` | `mcq` | false | `C` | `D. Lower in the sky` |
| baseline | `mmlu_294` | `mcq` | true | `D` | `D. Could be any time. The probability of impact is the same next year as it is for any later year.` |
| baseline | `mmlu_295` | `mcq` | false | `D` | `C. They reflect enough of the sun's light to make them brighter than most background stars` |
| baseline | `mmlu_296` | `mcq` | true | `D` | `D. As the cloud shrank its gravitational potential energy was converted to kinetic energy and then into thermal energy.` |
| baseline | `mmlu_297` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_298` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_299` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_300` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_301` | `mcq` | true | `B` | `B. 25 times brighter` |
| baseline | `mmlu_302` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_303` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_304` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_305` | `mcq` | true | `B` | `B. Chicxulub Crater Yucatan Peninsula in Mexico.` |
| baseline | `mmlu_306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_307` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_308` | `mcq` | true | `D` | `D. Hawking radiation` |
| baseline | `mmlu_309` | `mcq` | false | `C` | `A. 1.7 million light years` |
| baseline | `mmlu_310` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_311` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_312` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_313` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_314` | `mcq` | true | `C` | `C. 2` |
| baseline | `mmlu_315` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_316` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_317` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_318` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_319` | `mcq` | false | `A` | `B. presence of an atmosphere` |
| baseline | `mmlu_320` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_321` | `mcq` | true | `C` | `C. black holes.` |
| baseline | `mmlu_322` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_323` | `mcq` | false | `C` | `D. New only` |
| baseline | `mmlu_324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_325` | `mcq` | false | `D` | `B. 2.2x10^14 kg` |
| baseline | `mmlu_326` | `mcq` | true | `B` | `B. Because it's in the southern hemisphere where it is winter now.` |
| baseline | `mmlu_327` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_328` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_329` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_330` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_331` | `mcq` | true | `D` | `D. Phobos and Deimos` |
| baseline | `mmlu_332` | `mcq` | true | `C` | `C. 380 to 740 nm.` |
| baseline | `mmlu_333` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_334` | `mcq` | true | `C` | `C. Cassiopeia` |
| baseline | `mmlu_335` | `mcq` | true | `A` | `A. About 6 meters` |
| baseline | `mmlu_336` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_337` | `mcq` | true | `C` | `C. 29 Earth days` |
| baseline | `mmlu_338` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_339` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_340` | `mcq` | true | `A` | `A. Hydrogen` |
| baseline | `mmlu_341` | `mcq` | false | `B` | `C. Not enough information. It will depend on the inclination of the new orbit.` |
| baseline | `mmlu_342` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_343` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_344` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_345` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_346` | `mcq` | true | `D` | `D. 23.5 degrees` |
| baseline | `mmlu_347` | `mcq` | true | `D` | `D. because the Moon's rotational and orbital periods are equal` |
| baseline | `mmlu_348` | `mcq` | false | `C` | `A. v = sqrt(GM/R)` |
| baseline | `mmlu_349` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_350` | `mcq` | true | `D` | `D. Orion` |
| baseline | `mmlu_351` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_352` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_353` | `mcq` | true | `A` | `A. detecting the gravitational effect of an orbiting planet by looking for the Doppler shifts in the star's spectrum` |
| baseline | `mmlu_354` | `mcq` | false | `D` | `A. 9.3 x 1013 meters` |
| baseline | `mmlu_355` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_356` | `mcq` | true | `B` | `B. 11` |
| baseline | `mmlu_357` | `mcq` | false | `C` | `D. Mars and Earth` |
| baseline | `mmlu_358` | `mcq` | true | `D` | `D. molecules scatter blue light more effectively than red light.` |
| baseline | `mmlu_359` | `mcq` | true | `D` | `D. both a molten metallic core and reasonably fast rotation` |
| baseline | `mmlu_360` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_361` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_362` | `mcq` | true | `C` | `C. 1609` |
| baseline | `mmlu_363` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_364` | `mcq` | true | `C` | `C. You can never prove your theory to be correct only "yet to be proven wrong."` |
| baseline | `mmlu_365` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_366` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_367` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_368` | `mcq` | true | `B` | `B. by contracting changing gravitational potential energy into thermal energy` |
| baseline | `mmlu_369` | `mcq` | false | `D` | `C. Scorpius` |
| baseline | `mmlu_370` | `mcq` | true | `D` | `D. gamma rays X rays ultraviolet visible light infrared radio` |
| baseline | `mmlu_371` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_372` | `mcq` | true | `D` | `D. CO2` |
| baseline | `mmlu_373` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_374` | `mcq` | true | `C` | `C. ν Neutrinos` |
| baseline | `mmlu_375` | `mcq` | true | `A` | `A. 750 million years.` |
| baseline | `mmlu_376` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_377` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_378` | `mcq` | true | `A` | `A. the region around a star where liquid water can potentially exist on planetary surfaces` |
| baseline | `mmlu_379` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_380` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_381` | `mcq` | true | `B` | `B. Arecibo Telescope` |
| baseline | `mmlu_382` | `mcq` | true | `A` | `A. 6000 K` |
| baseline | `mmlu_383` | `mcq` | false | `D` | `A. Wolf 359` |
| baseline | `mmlu_384` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_385` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_386` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_387` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_388` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_389` | `mcq` | true | `D` | `D. Employee duties` |
| baseline | `mmlu_390` | `mcq` | true | `D` | `D. Work-life balance` |
| baseline | `mmlu_391` | `mcq` | true | `B` | `B. Industrial ecosystems` |
| baseline | `mmlu_392` | `mcq` | true | `B` | `B. Power imbalance, Resources, Co-opted` |
| baseline | `mmlu_393` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_394` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_395` | `mcq` | false | `B` | `C. Political, Interactions, Outcomes` |
| baseline | `mmlu_396` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_397` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_398` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_399` | `mcq` | true | `D` | `D. Public services, social, economic and environmental` |
| baseline | `mmlu_400` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_401` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_402` | `mcq` | true | `B` | `B. Healthy and safe working conditions` |
| baseline | `mmlu_403` | `mcq` | true | `A` | `A. To make a profit` |
| baseline | `mmlu_404` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_405` | `mcq` | false | `C` | `B. Consumer control` |
| baseline | `mmlu_406` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_407` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_408` | `mcq` | true | `B` | `B. Cognitive moral development` |
| baseline | `mmlu_409` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_410` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_411` | `mcq` | true | `A` | `A. Increase Revenue` |
| baseline | `mmlu_412` | `mcq` | true | `B` | `B. Social licence to operate` |
| baseline | `mmlu_413` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_414` | `mcq` | true | `C` | `C. Environmental management systems, ISO14001, EMAS` |
| baseline | `mmlu_415` | `mcq` | true | `D` | `D. China, Relationship, Market` |
| baseline | `mmlu_416` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_417` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_418` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_419` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_420` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_421` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_422` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_423` | `mcq` | false | `B` | `A. Eco-strategy` |
| baseline | `mmlu_424` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_425` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_426` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_427` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_428` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_429` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_430` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_431` | `mcq` | false | `B` | `C. Ethical window dressing` |
| baseline | `mmlu_432` | `mcq` | true | `D` | `D. Locus of control` |
| baseline | `mmlu_433` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_434` | `mcq` | true | `A` | `A. Social Contract` |
| baseline | `mmlu_435` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_436` | `mcq` | false | `B` | `D. Economic, Legal, Ethical and Environmental` |
| baseline | `mmlu_437` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_438` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_439` | `mcq` | true | `D` | `D. Consumer vulnerability` |
| baseline | `mmlu_440` | `mcq` | true | `C` | `C. Power, Legitimacy, Urgency, Salience` |
| baseline | `mmlu_441` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_442` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_443` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_444` | `mcq` | true | `A` | `A. Legislation, Sarbanes-Oxley Act` |
| baseline | `mmlu_445` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_446` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_447` | `mcq` | true | `D` | `D. Individual, Situational` |
| baseline | `mmlu_448` | `mcq` | true | `A` | `A. Globalisation, Cultural, Legal, Accountability` |
| baseline | `mmlu_449` | `mcq` | false | `B` | `A. 2,3` |
| baseline | `mmlu_450` | `mcq` | false | `A` | `D. Top, Standardisation, Political, Economic` |
| baseline | `mmlu_451` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_452` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_453` | `mcq` | true | `D` | `D. cannot pay creditors in full after realisation of its assets` |
| baseline | `mmlu_454` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_455` | `mcq` | true | `A` | `A. Social accountability standard, SA 8000` |
| baseline | `mmlu_456` | `mcq` | false | `A` | `C. 1,2,4` |
| baseline | `mmlu_457` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_458` | `mcq` | false | `B` | `A. 1,2,3` |
| baseline | `mmlu_459` | `mcq` | false | `A` | `C. Down, Autonomy, Remuneration, Benefit` |
| baseline | `mmlu_460` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_461` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_462` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_463` | `mcq` | false | `A` | `D. Rationalised, Cost-benefit analysis` |
| baseline | `mmlu_464` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_465` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_466` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_467` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_468` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_469` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_470` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_471` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_472` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_473` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_474` | `mcq` | true | `A` | `A. Supermarket industry` |
| baseline | `mmlu_475` | `mcq` | true | `B` | `B. Fair trade` |
| baseline | `mmlu_476` | `mcq` | false | `B` | `C. Personal attitudes` |
| baseline | `mmlu_477` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_478` | `mcq` | false | `A` | `D. 1,2,3` |
| baseline | `mmlu_479` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_480` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_481` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_482` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_483` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_484` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_485` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_486` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_487` | `mcq` | true | `A` | `A. 18 gauge.` |
| baseline | `mmlu_488` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_489` | `mcq` | true | `A` | `A. Alzheimer's disease.` |
| baseline | `mmlu_490` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_491` | `mcq` | true | `B` | `B. The patient has a colostomy.` |
| baseline | `mmlu_492` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_493` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_494` | `mcq` | true | `A` | `A. elevating the pH and buffering capacity of the extracellular fluid allowing a faster efflux of hydrogen ions from mus` |
| baseline | `mmlu_495` | `mcq` | true | `A` | `A. triplet sequences of nucleotide bases in mRNA or DNA.` |
| baseline | `mmlu_496` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_497` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_498` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_499` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_500` | `mcq` | true | `B` | `B. glucose-1-phosphate.` |
| baseline | `mmlu_501` | `mcq` | true | `B` | `B. actin and myosin.` |
| baseline | `mmlu_502` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_503` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_504` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_505` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_506` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_507` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_508` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_509` | `mcq` | true | `A` | `A. 30 minutes.` |
| baseline | `mmlu_510` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_511` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_512` | `mcq` | true | `B` | `B. When the catheter is blocked.` |
| baseline | `mmlu_513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_514` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_515` | `mcq` | false | `B` | `D. Increases throughout the course of the game as the players become more fatigued.` |
| baseline | `mmlu_516` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_517` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_518` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_519` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_520` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_522` | `mcq` | false | `D` | `A. 10-12 breaths per minute.` |
| baseline | `mmlu_523` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_524` | `mcq` | false | `B` | `A. One gram of glucose` |
| baseline | `mmlu_525` | `mcq` | true | `B` | `B. the components of the electron transport chain.` |
| baseline | `mmlu_526` | `mcq` | false | `D` | `A. 400 kJ/min.` |
| baseline | `mmlu_527` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_528` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_529` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_530` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_531` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_532` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_533` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_534` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_535` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_536` | `mcq` | true | `D` | `D. bound to albumin.` |
| baseline | `mmlu_537` | `mcq` | false | `C` | `A. Every 4 hours.` |
| baseline | `mmlu_538` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_539` | `mcq` | false | `C` | `D. 1 mmHg.` |
| baseline | `mmlu_540` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_541` | `mcq` | true | `D` | `D. 30:02:00` |
| baseline | `mmlu_542` | `mcq` | false | `D` | `A. 930` |
| baseline | `mmlu_543` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_544` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_545` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_546` | `mcq` | true | `B` | `B. 3, 2, 1, 4.` |
| baseline | `mmlu_547` | `mcq` | true | `C` | `C. failure of the ATP supply to match the demand.` |
| baseline | `mmlu_548` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_549` | `mcq` | true | `C` | `C. Leakage of effluent onto peristomal skin.` |
| baseline | `mmlu_550` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_551` | `mcq` | false | `A` | `D. Left ventricular hypertrophy` |
| baseline | `mmlu_552` | `mcq` | false | `D` | `A. 5%` |
| baseline | `mmlu_553` | `mcq` | true | `B` | `B. Reduces pain intensity but also causes sedation.` |
| baseline | `mmlu_554` | `mcq` | true | `D` | `D. Tension headaches is a common cause of headache` |
| baseline | `mmlu_555` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_556` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_557` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_558` | `mcq` | true | `C` | `C. 100/minute.` |
| baseline | `mmlu_559` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_560` | `mcq` | false | `D` | `B. After using their bronchodilator inhaler.` |
| baseline | `mmlu_561` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_562` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_563` | `mcq` | true | `B` | `B. Preload, contractility, and afterload.` |
| baseline | `mmlu_564` | `mcq` | true | `A` | `A. Proximal phalynx, middle phalynx, distal phalynx.` |
| baseline | `mmlu_565` | `mcq` | true | `B` | `B. Insulin` |
| baseline | `mmlu_566` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_567` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_568` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_569` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_570` | `mcq` | false | `B` | `A. 156` |
| baseline | `mmlu_571` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_572` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_573` | `mcq` | true | `A` | `A. each time post-operative observations are undertaken.` |
| baseline | `mmlu_574` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_575` | `mcq` | true | `D` | `D. Call for assistance from a medical practitioner.` |
| baseline | `mmlu_576` | `mcq` | false | `D` | `A. warm.` |
| baseline | `mmlu_577` | `mcq` | true | `C` | `C. physical, psychological, and pharmacological needs followed by regular reassessment.` |
| baseline | `mmlu_578` | `mcq` | true | `C` | `C. Alzheimer's disease.` |
| baseline | `mmlu_579` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_580` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_581` | `mcq` | true | `C` | `C. 80% or below.` |
| baseline | `mmlu_582` | `mcq` | true | `C` | `C. look for chest movements, listen for breath sounds, and feel for exhaled air on your cheek.` |
| baseline | `mmlu_583` | `mcq` | false | `D` | `A. 5` |
| baseline | `mmlu_584` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_585` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_586` | `mcq` | false | `B` | `A. 0.192` |
| baseline | `mmlu_587` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_588` | `mcq` | true | `C` | `C. Reduced amount of gastric acid.` |
| baseline | `mmlu_589` | `mcq` | true | `B` | `B. Normal saline.` |
| baseline | `mmlu_590` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_591` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_592` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_593` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_594` | `mcq` | false | `A` | `C. Coordination in the legs is affected` |
| baseline | `mmlu_595` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_596` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_597` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_598` | `mcq` | true | `C` | `C. 350` |
| baseline | `mmlu_599` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_600` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_601` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_602` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_603` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_604` | `mcq` | true | `C` | `C. Carnosine` |
| baseline | `mmlu_605` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_606` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_607` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_608` | `mcq` | true | `A` | `A. Small, soft toothbrush.` |
| baseline | `mmlu_609` | `mcq` | false | `C` | `B. Ditropan.` |
| baseline | `mmlu_610` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_611` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_612` | `mcq` | true | `D` | `D. More women are now engaged in sport.` |
| baseline | `mmlu_613` | `mcq` | true | `A` | `A. deoxyribonucleic acid.` |
| baseline | `mmlu_614` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_615` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_616` | `mcq` | false | `B` | `A. 6 ATP.` |
| baseline | `mmlu_617` | `mcq` | true | `A` | `A. the nerve stimulus is removed.` |
| baseline | `mmlu_618` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_619` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_620` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_621` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_622` | `mcq` | true | `C` | `C. The general public.` |
| baseline | `mmlu_623` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_624` | `mcq` | true | `C` | `C. Previous tuberculosis of the right upper lobe` |
| baseline | `mmlu_625` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_626` | `mcq` | true | `B` | `B. 0-135 degrees.` |
| baseline | `mmlu_627` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_628` | `mcq` | false | `C` | `D. 4 minutes` |
| baseline | `mmlu_629` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_630` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_631` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_632` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_633` | `mcq` | true | `B` | `B. Temperature.` |
| baseline | `mmlu_634` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_635` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_636` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_637` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_638` | `mcq` | true | `A` | `A. To create an air seal within the trachea and reduce the risk of aspirating saliva or gastric contents.` |
| baseline | `mmlu_639` | `mcq` | true | `A` | `A. Peptide bonds` |
| baseline | `mmlu_640` | `mcq` | false | `D` | `A. Inspect the nail-bed angle from above` |
| baseline | `mmlu_641` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_642` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_643` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_644` | `mcq` | true | `D` | `D. Pupil response.` |
| baseline | `mmlu_645` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_646` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_647` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_648` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_649` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_650` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_651` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_652` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_653` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_654` | `mcq` | true | `D` | `D. Amino acid` |
| baseline | `mmlu_655` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_656` | `mcq` | true | `A` | `A. Thymine` |
| baseline | `mmlu_657` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_658` | `mcq` | true | `C` | `C. Alcohol.` |
| baseline | `mmlu_659` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_660` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_661` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_662` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_663` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_664` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_665` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_666` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_667` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_668` | `mcq` | false | `B` | `D. Remove the catheter and recatheterize.` |
| baseline | `mmlu_669` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_670` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_671` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_672` | `mcq` | true | `D` | `D. 46` |
| baseline | `mmlu_673` | `mcq` | true | `C` | `C. If patient has an artificial heart valve.` |
| baseline | `mmlu_674` | `mcq` | false | `C` | `D. Pressure in the root of the neck reduces the impulse` |
| baseline | `mmlu_675` | `mcq` | true | `D` | `D. phosphofructokinase.` |
| baseline | `mmlu_676` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_677` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_678` | `mcq` | true | `A` | `A. yields 8 molecules of acetyl-CoA and some ATP and water.` |
| baseline | `mmlu_679` | `mcq` | true | `A` | `A. Ammonia, hypoxanthine and uric acid.` |
| baseline | `mmlu_680` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_681` | `mcq` | false | `D` | `C. about 1 minute.` |
| baseline | `mmlu_682` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_683` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_684` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_685` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_686` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_687` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_688` | `mcq` | true | `C` | `C. cytoplasm.` |
| baseline | `mmlu_689` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_690` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_691` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_692` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_693` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_694` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_695` | `mcq` | true | `B` | `B. Give drugs regularly with provision for additional 'as required' pain relief for breakthrough pain.` |
| baseline | `mmlu_696` | `mcq` | true | `A` | `A. Pain resulting from actual or potential tissue damage, which causes the release of chemical mediators that stimulate ` |
| baseline | `mmlu_697` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_698` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_699` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_700` | `mcq` | true | `A` | `A. ensure the emergency team/services are called.` |
| baseline | `mmlu_701` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_702` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_703` | `mcq` | false | `B` | `D. The GP.` |
| baseline | `mmlu_704` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_705` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_706` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_707` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_708` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_709` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_710` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_711` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_712` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_713` | `mcq` | false | `D` | `C. 2CO2 and 12ATP` |
| baseline | `mmlu_714` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_715` | `mcq` | true | `A` | `A. Lysozyme.` |
| baseline | `mmlu_716` | `mcq` | true | `B` | `B. the entire DNA sequence of an organism.` |
| baseline | `mmlu_717` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_718` | `mcq` | false | `D` | `C. Type IIa fibres.` |
| baseline | `mmlu_719` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_720` | `mcq` | true | `B` | `B. phosphocreatine breakdown.` |
| baseline | `mmlu_721` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_722` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_723` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_724` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_725` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_726` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_727` | `mcq` | true | `C` | `C. 300 kJ` |
| baseline | `mmlu_728` | `mcq` | false | `B` | `C. 24 hours.` |
| baseline | `mmlu_729` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_730` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_731` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_732` | `mcq` | true | `A` | `A. Antidiuretic hormone.` |
| baseline | `mmlu_733` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_734` | `mcq` | true | `D` | `D. a lack of oxygen.` |
| baseline | `mmlu_735` | `mcq` | true | `C` | `C. in the nucleus.` |
| baseline | `mmlu_736` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_737` | `mcq` | true | `A` | `A. It works to dilate the airways quickly, allowing better deposition of other medications.` |
| baseline | `mmlu_738` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_739` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_740` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_741` | `mcq` | true | `D` | `D. underestimated the blood pressure.` |
| baseline | `mmlu_742` | `mcq` | true | `A` | `A. Drugs may be implicated in the causation of gout` |
| baseline | `mmlu_743` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_744` | `mcq` | true | `B` | `B. The pancreas.` |
| baseline | `mmlu_745` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_746` | `mcq` | true | `A` | `A. To ensure best lung expansion and accuracy and consistency of readings.` |
| baseline | `mmlu_747` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_748` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_749` | `mcq` | true | `D` | `D. Ventilator-associated pneumonia.` |
| baseline | `mmlu_750` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_751` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_752` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_753` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_754` | `mcq` | true | `A` | `A. amnion` |
| baseline | `mmlu_755` | `mcq` | true | `B` | `B. Inositol triphosphate` |
| baseline | `mmlu_756` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_757` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_758` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_759` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_760` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_761` | `mcq` | true | `C` | `C. Replicate its genetic material and synthesize viral proteins` |
| baseline | `mmlu_762` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_763` | `mcq` | false | `D` | `B. Lysosome` |
| baseline | `mmlu_764` | `mcq` | false | `C` | `A. Both fox and hare populations will decrease.` |
| baseline | `mmlu_765` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_766` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_767` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_768` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_769` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_770` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_771` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_772` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_773` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_774` | `mcq` | true | `B` | `B. analogous structures` |
| baseline | `mmlu_775` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_776` | `mcq` | true | `D` | `D. transposons` |
| baseline | `mmlu_777` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_778` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_779` | `mcq` | true | `C` | `C. clathrin` |
| baseline | `mmlu_780` | `mcq` | true | `A` | `A. coefficient of relatedness` |
| baseline | `mmlu_781` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_782` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_783` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_784` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_785` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_786` | `mcq` | false | `D` | `A. 5′ GCU AAC 3′` |
| baseline | `mmlu_787` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_788` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_789` | `mcq` | true | `A` | `A. Remove ants and measure subsequent leaf damage.` |
| baseline | `mmlu_790` | `mcq` | true | `C` | `C. compound eye` |
| baseline | `mmlu_791` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_792` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_793` | `mcq` | false | `B` | `A. DNA and mRNA` |
| baseline | `mmlu_794` | `mcq` | true | `C` | `C. Increasing the total surface area available for diffusion` |
| baseline | `mmlu_795` | `mcq` | false | `A` | `C. nodes` |
| baseline | `mmlu_796` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_797` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_798` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_799` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_800` | `mcq` | true | `B` | `B. neritic zone` |
| baseline | `mmlu_801` | `mcq` | true | `A` | `A. Thymine dimers` |
| baseline | `mmlu_802` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_803` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_804` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_805` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_806` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_807` | `mcq` | false | `B` | `D. The blastomere with the gray crescent will stop dividing and die before the second cleavage.` |
| baseline | `mmlu_808` | `mcq` | false | `C` | `A. microtubules in the axon to undergo reversible dissociation` |
| baseline | `mmlu_809` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_810` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_811` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_812` | `mcq` | true | `B` | `B. Plasma membrane` |
| baseline | `mmlu_813` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_814` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_815` | `mcq` | false | `C` | `B. Two` |
| baseline | `mmlu_816` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_817` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_818` | `mcq` | true | `D` | `D. endoderm` |
| baseline | `mmlu_819` | `mcq` | false | `B` | `C. Stomatal guard cell` |
| baseline | `mmlu_820` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_821` | `mcq` | false | `B` | `D. More chicks survive the fall from the cliffs than are killed.` |
| baseline | `mmlu_822` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_823` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_824` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_825` | `mcq` | true | `A` | `A. 2%` |
| baseline | `mmlu_826` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_827` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_828` | `mcq` | true | `C` | `C. kinetochore` |
| baseline | `mmlu_829` | `mcq` | true | `A` | `A. thigmotropism` |
| baseline | `mmlu_830` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_831` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_832` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_833` | `mcq` | true | `D` | `D. Electrophoretic mobility shift assay` |
| baseline | `mmlu_834` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_835` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_836` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_837` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_838` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_839` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_840` | `mcq` | true | `B` | `B. Palisade mesophyll` |
| baseline | `mmlu_841` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_842` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_843` | `mcq` | true | `C` | `C. Microfilaments` |
| baseline | `mmlu_844` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_845` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_846` | `mcq` | true | `D` | `D. Tyrosine kinase` |
| baseline | `mmlu_847` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_848` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_849` | `mcq` | true | `D` | `D. reverse transcriptase` |
| baseline | `mmlu_850` | `mcq` | false | `D` | `C. produced by repeated rounds of DNA replication followed by nuclear division` |
| baseline | `mmlu_851` | `mcq` | true | `B` | `B. Colchicine` |
| baseline | `mmlu_852` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_853` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_854` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_855` | `mcq` | false | `D` | `C. the nucleosome core` |
| baseline | `mmlu_856` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_857` | `mcq` | true | `B` | `B. high relative humidity` |
| baseline | `mmlu_858` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_859` | `mcq` | false | `A` | `B. Reduction of NADP+ to NADPH` |
| baseline | `mmlu_860` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_861` | `mcq` | true | `B` | `B. High parental investment` |
| baseline | `mmlu_862` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_863` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_864` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_865` | `mcq` | true | `A` | `A. Nearly all of the enzyme molecules are interacting with acetaldehyde molecules.` |
| baseline | `mmlu_866` | `mcq` | true | `A` | `A. A different polypeptide is produced.` |
| baseline | `mmlu_867` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_868` | `mcq` | false | `C` | `A. The amplitude of the action potential` |
| baseline | `mmlu_869` | `mcq` | true | `C` | `C. The availability of water and warm temperatures in the tropics fosters photosynthesis.` |
| baseline | `mmlu_870` | `mcq` | true | `A` | `A. Producing a heterokaryon` |
| baseline | `mmlu_871` | `mcq` | true | `A` | `A. an increase in genetic homogeneity in the metapopulation` |
| baseline | `mmlu_872` | `mcq` | true | `C` | `C. nucleosome` |
| baseline | `mmlu_873` | `mcq` | true | `B` | `B. Photoperiod` |
| baseline | `mmlu_874` | `mcq` | false | `D` | `A. It increases the concentration of OH-, causing the mitochondria to pump H+ to the intermembrane space.` |
| baseline | `mmlu_875` | `mcq` | true | `A` | `A. Whale` |
| baseline | `mmlu_876` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_877` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_878` | `mcq` | true | `D` | `D. endosperm` |
| baseline | `mmlu_879` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_880` | `mcq` | true | `C` | `C. osmosis` |
| baseline | `mmlu_881` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_882` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_883` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_884` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_885` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_886` | `mcq` | true | `B` | `B. mtDNA is passed from mother to child and is free from recombination that occurs between pairs of chromosomes.` |
| baseline | `mmlu_887` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_888` | `mcq` | false | `A` | `B. independent assortment` |
| baseline | `mmlu_889` | `mcq` | false | `D` | `A. The atmosphere` |
| baseline | `mmlu_890` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_891` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_892` | `mcq` | true | `A` | `A. Chitin` |
| baseline | `mmlu_893` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_894` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_895` | `mcq` | false | `D` | `A. Fibers, phloem parenchyma, companion cell, sieve tube` |
| baseline | `mmlu_896` | `mcq` | true | `D` | `D. r = k` |
| baseline | `mmlu_897` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_898` | `mcq` | false | `D` | `A. 2` |
| baseline | `mmlu_899` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_900` | `mcq` | true | `B` | `B. only for constant pressure processes` |
| baseline | `mmlu_901` | `mcq` | false | `B` | `A. 3 lines` |
| baseline | `mmlu_902` | `mcq` | true | `A` | `A. Neutrons` |
| baseline | `mmlu_903` | `mcq` | true | `D` | `D. Unpaired electrons` |
| baseline | `mmlu_904` | `mcq` | false | `C` | `B. 1:3` |
| baseline | `mmlu_905` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_906` | `mcq` | false | `D` | `A. 3.02 ppm` |
| baseline | `mmlu_907` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_908` | `mcq` | true | `A` | `A. 4.6 mT` |
| baseline | `mmlu_909` | `mcq` | false | `D` | `A. 1:19:36:84:126:126:84:36:19:1` |
| baseline | `mmlu_910` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_911` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_912` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_913` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_914` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_915` | `mcq` | false | `B` | `D. 13.93 MHz` |
| baseline | `mmlu_916` | `mcq` | true | `D` | `D. Arsenic-doped silicon` |
| baseline | `mmlu_917` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_918` | `mcq` | false | `D` | `C. 1.0 × 10^−9` |
| baseline | `mmlu_919` | `mcq` | false | `B` | `D. 2,3-dimethylbutane` |
| baseline | `mmlu_920` | `mcq` | true | `D` | `D. Oxide` |
| baseline | `mmlu_921` | `mcq` | false | `A` | `B. 19F` |
| baseline | `mmlu_922` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_923` | `mcq` | false | `D` | `B. 3.98 ppm` |
| baseline | `mmlu_924` | `mcq` | false | `D` | `B. I and II only` |
| baseline | `mmlu_925` | `mcq` | false | `C` | `D. 0.015 M` |
| baseline | `mmlu_926` | `mcq` | true | `B` | `B. Precise but not accurate` |
| baseline | `mmlu_927` | `mcq` | false | `C` | `A. 500 MHz = 0.185 mT = 0.29842 cm-1` |
| baseline | `mmlu_928` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_929` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_930` | `mcq` | true | `A` | `A. g = 2.002` |
| baseline | `mmlu_931` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_932` | `mcq` | true | `C` | `C. 2.9 T` |
| baseline | `mmlu_933` | `mcq` | false | `B` | `A. 0.0471 Hz` |
| baseline | `mmlu_934` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_935` | `mcq` | false | `A` | `D. CCl4` |
| baseline | `mmlu_936` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_937` | `mcq` | false | `D` | `A. 0.375 mT` |
| baseline | `mmlu_938` | `mcq` | true | `B` | `B. NH2⁻` |
| baseline | `mmlu_939` | `mcq` | false | `A` | `C. nα = ½(nαeq + nβeq) and nβ = ½(nαeq + nβeq)` |
| baseline | `mmlu_940` | `mcq` | false | `D` | `A. Q = 1012` |
| baseline | `mmlu_941` | `mcq` | false | `A` | `C. 91.6 kHz` |
| baseline | `mmlu_942` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_943` | `mcq` | true | `B` | `B. 5.18 mT` |
| baseline | `mmlu_944` | `mcq` | true | `A` | `A. Blackbody radiation curves` |
| baseline | `mmlu_945` | `mcq` | true | `D` | `D. 9.4 mCi` |
| baseline | `mmlu_946` | `mcq` | false | `C` | `D. 0` |
| baseline | `mmlu_947` | `mcq` | false | `D` | `C. Na2S` |
| baseline | `mmlu_948` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_949` | `mcq` | false | `A` | `D. Am` |
| baseline | `mmlu_950` | `mcq` | false | `C` | `A. 0.95` |
| baseline | `mmlu_951` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_952` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_953` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_954` | `mcq` | true | `A` | `A. 3.74 T` |
| baseline | `mmlu_955` | `mcq` | false | `A` | `D. NaCl` |
| baseline | `mmlu_956` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_957` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_958` | `mcq` | false | `B` | `D. 6Li` |
| baseline | `mmlu_959` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_960` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_961` | `mcq` | false | `D` | `C. No information about either position or momentum can be known.` |
| baseline | `mmlu_962` | `mcq` | false | `D` | `C. H(g) + Br(g) → HBr(g)` |
| baseline | `mmlu_963` | `mcq` | false | `C` | `A. 101.1 x 10^7 T-1 s-1` |
| baseline | `mmlu_964` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_965` | `mcq` | false | `D` | `A. 1.5R` |
| baseline | `mmlu_966` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_967` | `mcq` | false | `D` | `B. dipole moment` |
| baseline | `mmlu_968` | `mcq` | false | `A` | `B. 5` |
| baseline | `mmlu_969` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_970` | `mcq` | true | `B` | `B. Ultraviolet` |
| baseline | `mmlu_971` | `mcq` | false | `C` | `A. 420 ns` |
| baseline | `mmlu_972` | `mcq` | true | `A` | `A. Gas chromatographic separation of the air sample on a capillary column followed by electron capture detection` |
| baseline | `mmlu_973` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_974` | `mcq` | true | `A` | `A. It has little effect.` |
| baseline | `mmlu_975` | `mcq` | false | `B` | `D. H+ / Cl−` |
| baseline | `mmlu_976` | `mcq` | false | `B` | `D. Zn2+` |
| baseline | `mmlu_977` | `mcq` | true | `B` | `B. 820` |
| baseline | `mmlu_978` | `mcq` | false | `D` | `A. 0.721 s` |
| baseline | `mmlu_979` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_980` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_981` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_982` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_983` | `mcq` | true | `D` | `D. Potassium hydrogen phthalate` |
| baseline | `mmlu_984` | `mcq` | false | `D` | `B. Boiling point` |
| baseline | `mmlu_985` | `mcq` | false | `B` | `A. 7,530 ppm` |
| baseline | `mmlu_986` | `mcq` | true | `A` | `A. 4.19 ms` |
| baseline | `mmlu_987` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_988` | `mcq` | false | `D` | `A. 3 lines` |
| baseline | `mmlu_989` | `mcq` | true | `A` | `A. Cu, Fe, Co` |
| baseline | `mmlu_990` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_991` | `mcq` | false | `D` | `A. F` |
| baseline | `mmlu_992` | `mcq` | true | `C` | `C. Sc3+` |
| baseline | `mmlu_993` | `mcq` | false | `C` | `A. 54.91 MHz` |
| baseline | `mmlu_994` | `mcq` | false | `B` | `A. 21` |
| baseline | `mmlu_995` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_996` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_997` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_998` | `mcq` | true | `B` | `B. 1:3.5` |
| baseline | `mmlu_999` | `mcq` | true | `A` | `A. C1: (3,3), C2: (4,4), C3: (6,6)` |
| baseline | `mmlu_1000` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1001` | `mcq` | false | `C` | `D. M = 6, m = 4` |
| baseline | `mmlu_1002` | `mcq` | false | `C` | `D. I and III only` |
| baseline | `mmlu_1003` | `mcq` | false | `B` | `C. III only` |
| baseline | `mmlu_1004` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1005` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1006` | `mcq` | false | `D` | `B. III only` |
| baseline | `mmlu_1007` | `mcq` | false | `A` | `B. n + 1` |
| baseline | `mmlu_1008` | `mcq` | true | `A` | `A. 3` |
| baseline | `mmlu_1009` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1010` | `mcq` | false | `A` | `C. III only` |
| baseline | `mmlu_1011` | `mcq` | true | `D` | `D. None of the above` |
| baseline | `mmlu_1012` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1013` | `mcq` | false | `B` | `D. context-free, but not regular` |
| baseline | `mmlu_1014` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1015` | `mcq` | false | `D` | `C. I and II only` |
| baseline | `mmlu_1016` | `mcq` | true | `D` | `D. One-time pad` |
| baseline | `mmlu_1017` | `mcq` | false | `B` | `A. Finding a longest simple cycle in G` |
| baseline | `mmlu_1018` | `mcq` | true | `A` | `A. Routing packets through the network` |
| baseline | `mmlu_1019` | `mcq` | false | `A` | `B. K-1/K` |
| baseline | `mmlu_1020` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1021` | `mcq` | true | `D` | `D. I and II` |
| baseline | `mmlu_1022` | `mcq` | true | `C` | `C. Symbol Table` |
| baseline | `mmlu_1023` | `mcq` | true | `D` | `D. Quicksort` |
| baseline | `mmlu_1024` | `mcq` | true | `D` | `D. II and III only` |
| baseline | `mmlu_1025` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1026` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1027` | `mcq` | true | `D` | `D. I, II, and IV` |
| baseline | `mmlu_1028` | `mcq` | false | `D` | `B. 999` |
| baseline | `mmlu_1029` | `mcq` | false | `A` | `D. I and III` |
| baseline | `mmlu_1030` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1031` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1032` | `mcq` | true | `C` | `C. Merge sort` |
| baseline | `mmlu_1033` | `mcq` | false | `D` | `A. 20 and 10 seconds` |
| baseline | `mmlu_1034` | `mcq` | false | `D` | `C. Two's complement and one's complement only` |
| baseline | `mmlu_1035` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1036` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1037` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1038` | `mcq` | false | `A` | `D. I and III` |
| baseline | `mmlu_1039` | `mcq` | false | `D` | `A. 1/(n^2)` |
| baseline | `mmlu_1040` | `mcq` | true | `D` | `D. I and II` |
| baseline | `mmlu_1041` | `mcq` | true | `C` | `C. III only` |
| baseline | `mmlu_1042` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1043` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1044` | `mcq` | true | `A` | `A. 0` |
| baseline | `mmlu_1045` | `mcq` | false | `D` | `C. I and II only` |
| baseline | `mmlu_1046` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1047` | `mcq` | false | `B` | `D. II and III only` |
| baseline | `mmlu_1048` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1049` | `mcq` | true | `C` | `C. Merge sort` |
| baseline | `mmlu_1050` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1051` | `mcq` | true | `C` | `C. 3` |
| baseline | `mmlu_1052` | `mcq` | true | `D` | `D. (I, II) and (I, III) only` |
| baseline | `mmlu_1053` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1054` | `mcq` | false | `B` | `A. k + 2` |
| baseline | `mmlu_1055` | `mcq` | false | `D` | `C. III only` |
| baseline | `mmlu_1056` | `mcq` | true | `D` | `D. II and III` |
| baseline | `mmlu_1057` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1058` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1059` | `mcq` | true | `A` | `A. Recursive procedures` |
| baseline | `mmlu_1060` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1061` | `mcq` | true | `C` | `C. Θ(n^2)` |
| baseline | `mmlu_1062` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1063` | `mcq` | false | `B` | `C. I and II only` |
| baseline | `mmlu_1064` | `mcq` | false | `B` | `C. 5/3` |
| baseline | `mmlu_1065` | `mcq` | true | `A` | `A. 0x01001234; page mapped with READ/WRITE access` |
| baseline | `mmlu_1066` | `mcq` | false | `D` | `C. I and III only` |
| baseline | `mmlu_1067` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1068` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1069` | `mcq` | true | `C` | `C. 100,000 bytes/ second` |
| baseline | `mmlu_1070` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_1071` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1072` | `mcq` | true | `A` | `A. n^m` |
| baseline | `mmlu_1073` | `mcq` | false | `B` | `D. 1/w + 1/x < 1/y + 1/z` |
| baseline | `mmlu_1074` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1075` | `mcq` | false | `D` | `B. 25%` |
| baseline | `mmlu_1076` | `mcq` | false | `B` | `A. I only` |
| baseline | `mmlu_1077` | `mcq` | false | `C` | `B. Maximum level of nesting` |
| baseline | `mmlu_1078` | `mcq` | true | `D` | `D. II and III` |
| baseline | `mmlu_1079` | `mcq` | true | `A` | `A. Round-robin` |
| baseline | `mmlu_1080` | `mcq` | false | `D` | `B. O(N log N)` |
| baseline | `mmlu_1081` | `mcq` | false | `D` | `C. 1 / 2` |
| baseline | `mmlu_1082` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1083` | `mcq` | false | `B` | `C. I and II only` |
| baseline | `mmlu_1084` | `mcq` | false | `C` | `A. 4` |
| baseline | `mmlu_1085` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1086` | `mcq` | false | `C` | `A. 0` |
| baseline | `mmlu_1087` | `mcq` | false | `C` | `B. 208/5` |
| baseline | `mmlu_1088` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1089` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1090` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1091` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1092` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1093` | `mcq` | true | `D` | `D. I and III` |
| baseline | `mmlu_1094` | `mcq` | true | `C` | `C. 1.6 microseconds` |
| baseline | `mmlu_1095` | `mcq` | true | `D` | `D. 99.80%` |
| baseline | `mmlu_1096` | `mcq` | false | `B` | `A. k = 0 and n = 1` |
| baseline | `mmlu_1097` | `mcq` | false | `D` | `B. 1` |
| baseline | `mmlu_1098` | `mcq` | false | `D` | `B. n = 1 and r = 7` |
| baseline | `mmlu_1099` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_1100` | `mcq` | false | `C` | `A. 2/69` |
| baseline | `mmlu_1101` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1102` | `mcq` | false | `C` | `B. 6*sqrt(2)` |
| baseline | `mmlu_1103` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1104` | `mcq` | false | `C` | `D. III only` |
| baseline | `mmlu_1105` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1106` | `mcq` | true | `D` | `D. 45` |
| baseline | `mmlu_1107` | `mcq` | true | `B` | `B. 15/64` |
| baseline | `mmlu_1108` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1109` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_1110` | `mcq` | false | `D` | `A. 0.64` |
| baseline | `mmlu_1111` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_1112` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_1113` | `mcq` | false | `C` | `A. -1/4` |
| baseline | `mmlu_1114` | `mcq` | false | `D` | `C. I and III only` |
| baseline | `mmlu_1115` | `mcq` | true | `A` | `A. 3` |
| baseline | `mmlu_1116` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1117` | `mcq` | false | `D` | `A. None` |
| baseline | `mmlu_1118` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_1119` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1120` | `mcq` | true | `B` | `B. True, False` |
| baseline | `mmlu_1121` | `mcq` | true | `D` | `D. III only` |
| baseline | `mmlu_1122` | `mcq` | false | `D` | `A. 9/2 days` |
| baseline | `mmlu_1123` | `mcq` | false | `A` | `C. sqrt(2)` |
| baseline | `mmlu_1124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1125` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1126` | `mcq` | false | `C` | `D. S(n) is not true for any n >= n0` |
| baseline | `mmlu_1127` | `mcq` | true | `B` | `B. (3/7, 3/14, 9/14)` |
| baseline | `mmlu_1128` | `mcq` | true | `B` | `B. For 3, 5, 7, and 11 only` |
| baseline | `mmlu_1129` | `mcq` | false | `C` | `D. 4` |
| baseline | `mmlu_1130` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1131` | `mcq` | false | `D` | `B. (x^2 + y^2 + z^2)^2 = 8 + 36(x^2 + z^2)` |
| baseline | `mmlu_1132` | `mcq` | false | `A` | `D. y = x + 1` |
| baseline | `mmlu_1133` | `mcq` | true | `A` | `A. 2` |
| baseline | `mmlu_1134` | `mcq` | false | `A` | `B. True, False` |
| baseline | `mmlu_1135` | `mcq` | true | `C` | `C. 3` |
| baseline | `mmlu_1136` | `mcq` | false | `B` | `A. the entire real axis` |
| baseline | `mmlu_1137` | `mcq` | false | `D` | `B. cyclic` |
| baseline | `mmlu_1138` | `mcq` | false | `D` | `A. 3` |
| baseline | `mmlu_1139` | `mcq` | false | `A` | `C. I and II only` |
| baseline | `mmlu_1140` | `mcq` | false | `D` | `A. 1` |
| baseline | `mmlu_1141` | `mcq` | false | `A` | `B. True, False` |
| baseline | `mmlu_1142` | `mcq` | false | `B` | `C. π/3` |
| baseline | `mmlu_1143` | `mcq` | true | `B` | `B. pi` |
| baseline | `mmlu_1144` | `mcq` | true | `C` | `C. (I) and (IV)` |
| baseline | `mmlu_1145` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_1146` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1147` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1148` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1149` | `mcq` | true | `C` | `C. 12*sqrt(3)` |
| baseline | `mmlu_1150` | `mcq` | false | `A` | `C. 8` |
| baseline | `mmlu_1151` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1152` | `mcq` | false | `B` | `A. 4` |
| baseline | `mmlu_1153` | `mcq` | true | `D` | `D. 0, 1, and 2 only` |
| baseline | `mmlu_1154` | `mcq` | false | `C` | `B. π` |
| baseline | `mmlu_1155` | `mcq` | true | `A` | `A. 9` |
| baseline | `mmlu_1156` | `mcq` | false | `B` | `A. None` |
| baseline | `mmlu_1157` | `mcq` | false | `A` | `C. 10^(20) - 2^(10)` |
| baseline | `mmlu_1158` | `mcq` | false | `A` | `D. Both (a) and (b).` |
| baseline | `mmlu_1159` | `mcq` | false | `D` | `C. 1/2` |
| baseline | `mmlu_1160` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1161` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_1162` | `mcq` | false | `C` | `B. -2` |
| baseline | `mmlu_1163` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1164` | `mcq` | true | `A` | `A. π/3` |
| baseline | `mmlu_1165` | `mcq` | true | `A` | `A. Sunday` |
| baseline | `mmlu_1166` | `mcq` | false | `D` | `C. -8/(3π) cm/min` |
| baseline | `mmlu_1167` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1168` | `mcq` | false | `D` | `A. f(c)` |
| baseline | `mmlu_1169` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_1170` | `mcq` | false | `C` | `A. 1/(2e)` |
| baseline | `mmlu_1171` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1172` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1173` | `mcq` | true | `C` | `C. 0` |
| baseline | `mmlu_1174` | `mcq` | false | `B` | `A. x^2/9` |
| baseline | `mmlu_1175` | `mcq` | true | `B` | `B. True, False` |
| baseline | `mmlu_1176` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1177` | `mcq` | true | `B` | `B. 30` |
| baseline | `mmlu_1178` | `mcq` | false | `B` | `A. 4` |
| baseline | `mmlu_1179` | `mcq` | true | `C` | `C. 35` |
| baseline | `mmlu_1180` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1181` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1182` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1183` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_1184` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1185` | `mcq` | false | `C` | `A. G is abelian` |
| baseline | `mmlu_1186` | `mcq` | false | `B` | `A. -2` |
| baseline | `mmlu_1187` | `mcq` | false | `C` | `D. I and III only` |
| baseline | `mmlu_1188` | `mcq` | false | `C` | `B. 7/12` |
| baseline | `mmlu_1189` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1190` | `mcq` | true | `D` | `D. 32i` |
| baseline | `mmlu_1191` | `mcq` | false | `D` | `C. 0 or 1` |
| baseline | `mmlu_1192` | `mcq` | false | `C` | `A. closed` |
| baseline | `mmlu_1193` | `mcq` | true | `C` | `C. x^2 + y^2 = 9` |
| baseline | `mmlu_1194` | `mcq` | false | `D` | `C. 28` |
| baseline | `mmlu_1195` | `mcq` | true | `A` | `A. (1, 6)` |
| baseline | `mmlu_1196` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1197` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1198` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1199` | `mcq` | false | `D` | `C. about 1 minute.` |
| baseline | `mmlu_1200` | `mcq` | true | `A` | `A. 13 m/s^2` |
| baseline | `mmlu_1201` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1202` | `mcq` | true | `A` | `A. Heart surgery patients who cannot run on treadmills may benefit from sauna use.` |
| baseline | `mmlu_1203` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1204` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1205` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1206` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1207` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1208` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1209` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1210` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1211` | `mcq` | false | `B` | `D. Not enough information given.` |
| baseline | `mmlu_1212` | `mcq` | true | `C` | `C. in the nucleus.` |
| baseline | `mmlu_1213` | `mcq` | true | `B` | `B. Transferase` |
| baseline | `mmlu_1214` | `mcq` | false | `B` | `C. Lower than the pOH` |
| baseline | `mmlu_1215` | `mcq` | true | `B` | `B. the entire DNA sequence of an organism.` |
| baseline | `mmlu_1216` | `mcq` | true | `C` | `C. I and III` |
| baseline | `mmlu_1217` | `mcq` | true | `D` | `D. bound to albumin.` |
| baseline | `mmlu_1218` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_1219` | `mcq` | true | `A` | `A. Osmosis` |
| baseline | `mmlu_1220` | `mcq` | true | `B` | `B. the components of the electron transport chain.` |
| baseline | `mmlu_1221` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1222` | `mcq` | false | `C` | `A. 941 Hz` |
| baseline | `mmlu_1223` | `mcq` | true | `D` | `D. a = g (sin ? – µ cos ?)` |
| baseline | `mmlu_1224` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1225` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1226` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1227` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1228` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1229` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1230` | `mcq` | false | `D` | `B. increasing respiration rate` |
| baseline | `mmlu_1231` | `mcq` | false | `B` | `A. One gram of glucose` |
| baseline | `mmlu_1232` | `mcq` | true | `D` | `D. increased oxygen binding to hemoglobin in the tissues.` |
| baseline | `mmlu_1233` | `mcq` | true | `D` | `D. More women are now engaged in sport.` |
| baseline | `mmlu_1234` | `mcq` | false | `D` | `C. Calcium-troponin interaction` |
| baseline | `mmlu_1235` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1236` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1237` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1238` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1239` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1240` | `mcq` | false | `C` | `D. cannot be determined` |
| baseline | `mmlu_1241` | `mcq` | false | `D` | `C. 2CO2 and 12ATP` |
| baseline | `mmlu_1242` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1243` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1244` | `mcq` | true | `B` | `B. Maintains alveoli in an open state` |
| baseline | `mmlu_1245` | `mcq` | true | `C` | `C. 264g` |
| baseline | `mmlu_1246` | `mcq` | true | `D` | `D. Replenish fluids with filtered water.` |
| baseline | `mmlu_1247` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1248` | `mcq` | true | `C` | `C. 300 kJ` |
| baseline | `mmlu_1249` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1250` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1251` | `mcq` | true | `B` | `B. Insulin` |
| baseline | `mmlu_1252` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1253` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1254` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1255` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1256` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1257` | `mcq` | true | `D` | `D. I and IV` |
| baseline | `mmlu_1258` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1259` | `mcq` | false | `C` | `B. I and II only` |
| baseline | `mmlu_1260` | `mcq` | false | `D` | `A. 400 kJ/min.` |
| baseline | `mmlu_1261` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1262` | `mcq` | true | `B` | `B. An 86-year old male mayor who is revered in the community.` |
| baseline | `mmlu_1263` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1264` | `mcq` | true | `D` | `D. a lack of oxygen.` |
| baseline | `mmlu_1265` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1266` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1267` | `mcq` | false | `C` | `D. 4 minutes` |
| baseline | `mmlu_1268` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1269` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1270` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1271` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1272` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1273` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1274` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1275` | `mcq` | true | `A` | `A. yields 8 molecules of acetyl-CoA and some ATP and water.` |
| baseline | `mmlu_1276` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1277` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1278` | `mcq` | false | `B` | `D. I and III and IV only` |
| baseline | `mmlu_1279` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1280` | `mcq` | true | `A` | `A. the nerve stimulus is removed.` |
| baseline | `mmlu_1281` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1282` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1283` | `mcq` | true | `A` | `A. deoxyribonucleic acid.` |
| baseline | `mmlu_1284` | `mcq` | false | `C` | `B. Narcissistic` |
| baseline | `mmlu_1285` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1286` | `mcq` | false | `B` | `A. Anal` |
| baseline | `mmlu_1287` | `mcq` | true | `A` | `A. Peptide bonds` |
| baseline | `mmlu_1288` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1289` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1290` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1291` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1292` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1293` | `mcq` | false | `A` | `D. He critiques his study methods and tries to find out which led to poor returns.` |
| baseline | `mmlu_1294` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1295` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1298` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1299` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1300` | `mcq` | true | `C` | `C. cytoplasm.` |
| baseline | `mmlu_1301` | `mcq` | true | `A` | `A. Hierarchical` |
| baseline | `mmlu_1302` | `mcq` | true | `A` | `A. Ammonia, hypoxanthine and uric acid.` |
| baseline | `mmlu_1303` | `mcq` | true | `D` | `D. phosphofructokinase.` |
| baseline | `mmlu_1304` | `mcq` | true | `C` | `C. failure of the ATP supply to match the demand.` |
| baseline | `mmlu_1305` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1307` | `mcq` | true | `A` | `A. slightly less than 20L` |
| baseline | `mmlu_1308` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1309` | `mcq` | true | `A` | `A. elevating the pH and buffering capacity of the extracellular fluid allowing a faster efflux of hydrogen ions from mus` |
| baseline | `mmlu_1310` | `mcq` | true | `D` | `D. Transgender, homosexual` |
| baseline | `mmlu_1311` | `mcq` | true | `C` | `C. Carnosine` |
| baseline | `mmlu_1312` | `mcq` | true | `B` | `B. Miss` |
| baseline | `mmlu_1313` | `mcq` | false | `A` | `C. Microculture` |
| baseline | `mmlu_1314` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1315` | `mcq` | true | `A` | `A. triplet sequences of nucleotide bases in mRNA or DNA.` |
| baseline | `mmlu_1316` | `mcq` | false | `B` | `D. Increases throughout the course of the game as the players become more fatigued.` |
| baseline | `mmlu_1317` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1318` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1319` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1320` | `mcq` | true | `B` | `B. phosphocreatine breakdown.` |
| baseline | `mmlu_1321` | `mcq` | false | `A` | `C. Active transport` |
| baseline | `mmlu_1322` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1323` | `mcq` | true | `C` | `C. I and III only` |
| baseline | `mmlu_1324` | `mcq` | true | `B` | `B. glucose-1-phosphate.` |
| baseline | `mmlu_1325` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1326` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1327` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1328` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1329` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1330` | `mcq` | false | `D` | `C. Arginine` |
| baseline | `mmlu_1331` | `mcq` | true | `A` | `A. Thymine` |
| baseline | `mmlu_1332` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1333` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1334` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1335` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1336` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1337` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1338` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1339` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1340` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1341` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1342` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1343` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1344` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1345` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1346` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1347` | `mcq` | false | `D` | `A. I, II, and III` |
| baseline | `mmlu_1348` | `mcq` | true | `A` | `A. ATP.` |
| baseline | `mmlu_1349` | `mcq` | true | `C` | `C. The primary transcripts of many genes can be spliced in various ways to produce different mRNAs, a process known as a` |
| baseline | `mmlu_1350` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1351` | `mcq` | true | `B` | `B. Steroid` |
| baseline | `mmlu_1352` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1353` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1354` | `mcq` | false | `C` | `B. Decrease in histone deacetyltransferase activity` |
| baseline | `mmlu_1355` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1356` | `mcq` | true | `D` | `D. Amino acid` |
| baseline | `mmlu_1357` | `mcq` | true | `C` | `C. 29` |
| baseline | `mmlu_1358` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1359` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1360` | `mcq` | false | `D` | `C. 5 m/s` |
| baseline | `mmlu_1361` | `mcq` | false | `B` | `A. 6 ATP.` |
| baseline | `mmlu_1362` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1363` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1364` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1365` | `mcq` | true | `A` | `A. DNA polymerase I` |
| baseline | `mmlu_1366` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1367` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1368` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1369` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1370` | `mcq` | false | `C` | `A. 500 nm` |
| baseline | `mmlu_1371` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1372` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1373` | `mcq` | true | `B` | `B. The Pauli exclusion principle` |
| baseline | `mmlu_1374` | `mcq` | false | `C` | `A. 1/2` |
| baseline | `mmlu_1375` | `mcq` | false | `D` | `B. V_0/3` |
| baseline | `mmlu_1376` | `mcq` | false | `A` | `C. 0.67mc^2` |
| baseline | `mmlu_1377` | `mcq` | true | `A` | `A. Planck’s constant` |
| baseline | `mmlu_1378` | `mcq` | false | `D` | `B. mc/(2^(1/2))` |
| baseline | `mmlu_1379` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1380` | `mcq` | false | `D` | `B. 0.048 m` |
| baseline | `mmlu_1381` | `mcq` | true | `D` | `D. Hall coefficient` |
| baseline | `mmlu_1382` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1383` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1384` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1385` | `mcq` | true | `B` | `B. The Pauli exclusion principle` |
| baseline | `mmlu_1386` | `mcq` | false | `A` | `C. 0.48 mJ` |
| baseline | `mmlu_1387` | `mcq` | false | `B` | `A. 1.6 ns` |
| baseline | `mmlu_1388` | `mcq` | false | `A` | `C. 0.67mc^2` |
| baseline | `mmlu_1389` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1390` | `mcq` | true | `D` | `D. 10` |
| baseline | `mmlu_1391` | `mcq` | false | `B` | `A. 0.25 mm` |
| baseline | `mmlu_1392` | `mcq` | true | `C` | `C. 2 x 10^-5 N` |
| baseline | `mmlu_1393` | `mcq` | true | `B` | `B. Hall coefficient` |
| baseline | `mmlu_1394` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1395` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1396` | `mcq` | false | `B` | `A. 0.50c` |
| baseline | `mmlu_1397` | `mcq` | false | `B` | `A. deflected in the +x-direction` |
| baseline | `mmlu_1398` | `mcq` | false | `D` | `A. 0.04 V` |
| baseline | `mmlu_1399` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1400` | `mcq` | true | `D` | `D. The orbits would remain unchanged.` |
| baseline | `mmlu_1401` | `mcq` | false | `B` | `A. 414 Hz` |
| baseline | `mmlu_1402` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1403` | `mcq` | false | `D` | `C. (3/2) k T` |
| baseline | `mmlu_1404` | `mcq` | true | `D` | `D. 5,000 s` |
| baseline | `mmlu_1405` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1406` | `mcq` | true | `A` | `A. Electron` |
| baseline | `mmlu_1407` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1408` | `mcq` | false | `D` | `B. 4` |
| baseline | `mmlu_1409` | `mcq` | true | `D` | `D. 4 W` |
| baseline | `mmlu_1410` | `mcq` | true | `B` | `B. 1.00032` |
| baseline | `mmlu_1411` | `mcq` | false | `C` | `B. 1 eV` |
| baseline | `mmlu_1412` | `mcq` | false | `B` | `A. 1/4` |
| baseline | `mmlu_1413` | `mcq` | false | `B` | `C. 300 nm` |
| baseline | `mmlu_1414` | `mcq` | false | `B` | `C. 1,100 J` |
| baseline | `mmlu_1415` | `mcq` | false | `C` | `B. 606 Hz` |
| baseline | `mmlu_1416` | `mcq` | false | `D` | `B. 288 m` |
| baseline | `mmlu_1417` | `mcq` | false | `D` | `C. 5/6 c` |
| baseline | `mmlu_1418` | `mcq` | false | `D` | `A. 0.1 GeV/c^2` |
| baseline | `mmlu_1419` | `mcq` | false | `B` | `D. 10,000` |
| baseline | `mmlu_1420` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1421` | `mcq` | true | `A` | `A. real` |
| baseline | `mmlu_1422` | `mcq` | false | `D` | `A. F_B = 1/4 F_A` |
| baseline | `mmlu_1423` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1424` | `mcq` | false | `D` | `B. 10%` |
| baseline | `mmlu_1425` | `mcq` | true | `C` | `C. 45°` |
| baseline | `mmlu_1426` | `mcq` | true | `D` | `D. Increases by a factor of 81.` |
| baseline | `mmlu_1427` | `mcq` | false | `D` | `A. 0.04 V` |
| baseline | `mmlu_1428` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1429` | `mcq` | true | `D` | `D. None` |
| baseline | `mmlu_1430` | `mcq` | true | `A` | `A. gamma rays` |
| baseline | `mmlu_1431` | `mcq` | false | `D` | `B. 196 Hz` |
| baseline | `mmlu_1432` | `mcq` | true | `D` | `D. 5` |
| baseline | `mmlu_1433` | `mcq` | true | `A` | `A. L_B = 4L_A` |
| baseline | `mmlu_1434` | `mcq` | false | `D` | `C.真空极化` |
| baseline | `mmlu_1435` | `mcq` | false | `B` | `A. 0.50c` |
| baseline | `mmlu_1436` | `mcq` | false | `A` | `C. 51.8 eV` |
| baseline | `mmlu_1437` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1438` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1439` | `mcq` | false | `D` | `C. 10,000 J` |
| baseline | `mmlu_1440` | `mcq` | true | `C` | `C. 0.8c` |
| baseline | `mmlu_1441` | `mcq` | true | `C` | `C. 3 N` |
| baseline | `mmlu_1442` | `mcq` | true | `B` | `B. 0.5c` |
| baseline | `mmlu_1443` | `mcq` | true | `C` | `C. 1,000,000 J` |
| baseline | `mmlu_1444` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1445` | `mcq` | true | `C` | `C. 3 N` |
| baseline | `mmlu_1446` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1447` | `mcq` | true | `D` | `D. 8k` |
| baseline | `mmlu_1448` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1449` | `mcq` | false | `A` | `C. 10 mm` |
| baseline | `mmlu_1450` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1451` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_1452` | `mcq` | false | `D` | `A. 588 Hz` |
| baseline | `mmlu_1453` | `mcq` | false | `A` | `C. decreased by a factor of 81` |
| baseline | `mmlu_1454` | `mcq` | true | `D` | `D. 4mc^2` |
| baseline | `mmlu_1455` | `mcq` | true | `D` | `D. Gas laser` |
| baseline | `mmlu_1456` | `mcq` | false | `D` | `C. 50%` |
| baseline | `mmlu_1457` | `mcq` | false | `D` | `B. 1,750 Hz` |
| baseline | `mmlu_1458` | `mcq` | false | `A` | `C. decreased by a factor of 81` |
| baseline | `mmlu_1459` | `mcq` | false | `B` | `A. 1/4` |
| baseline | `mmlu_1460` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1461` | `mcq` | false | `A` | `C. 0.27 J` |
| baseline | `mmlu_1462` | `mcq` | false | `C` | `B. 1 eV` |
| baseline | `mmlu_1463` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1464` | `mcq` | true | `D` | `D. 19.6 m` |
| baseline | `mmlu_1465` | `mcq` | false | `C` | `B. 1/4` |
| baseline | `mmlu_1466` | `mcq` | false | `C` | `A. 500 nm` |
| baseline | `mmlu_1467` | `mcq` | true | `A` | `A. 2.5 * 10^-23 kg` |
| baseline | `mmlu_1468` | `mcq` | false | `B` | `D. 100 m/s north and 40 m/s down` |
| baseline | `mmlu_1469` | `mcq` | false | `A` | `D. 13.6 eV` |
| baseline | `mmlu_1470` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1471` | `mcq` | true | `C` | `C. Whitebox` |
| baseline | `mmlu_1472` | `mcq` | false | `A` | `D. False, True` |
| baseline | `mmlu_1473` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1474` | `mcq` | true | `A` | `A. Receiver` |
| baseline | `mmlu_1475` | `mcq` | true | `A` | `A. Troya` |
| baseline | `mmlu_1476` | `mcq` | true | `B` | `B. Buffer-overrun` |
| baseline | `mmlu_1477` | `mcq` | true | `A` | `A. all instructions that modify segment state` |
| baseline | `mmlu_1478` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1479` | `mcq` | true | `A` | `A. No string boundary checks in predefined functions` |
| baseline | `mmlu_1480` | `mcq` | true | `B` | `B. Authenticated` |
| baseline | `mmlu_1481` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1482` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1483` | `mcq` | true | `C` | `C. Forward secrecy` |
| baseline | `mmlu_1484` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1485` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1486` | `mcq` | true | `B` | `B. Access Point` |
| baseline | `mmlu_1487` | `mcq` | true | `B` | `B. 128` |
| baseline | `mmlu_1488` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1489` | `mcq` | false | `A` | `D. All of the above` |
| baseline | `mmlu_1490` | `mcq` | true | `D` | `D. Taking care to avoid activities during a penetration test that might attract attention, e.g., by operators or IDS ser` |
| baseline | `mmlu_1491` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1492` | `mcq` | false | `C` | `D. Blinding adds a random amount of time to the decryption due to the multiplication and division by the blinding random` |
| baseline | `mmlu_1493` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_1494` | `mcq` | true | `C` | `C. Key exchange` |
| baseline | `mmlu_1495` | `mcq` | true | `A` | `A. Silk Road` |
| baseline | `mmlu_1496` | `mcq` | true | `C` | `C. Dark web` |
| baseline | `mmlu_1497` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1498` | `mcq` | true | `B` | `B. Sender’s Public key` |
| baseline | `mmlu_1499` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1500` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1501` | `mcq` | true | `D` | `D. IP Network Browser` |
| baseline | `mmlu_1502` | `mcq` | true | `D` | `D. WPA3` |
| baseline | `mmlu_1503` | `mcq` | true | `C` | `C. True, False` |
| baseline | `mmlu_1504` | `mcq` | true | `C` | `C. Session layer` |
| baseline | `mmlu_1505` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_1506` | `mcq` | true | `C` | `C. when a pointer is used to access memory not allocated to it` |
| baseline | `mmlu_1507` | `mcq` | true | `C` | `C. Public-key system` |
| baseline | `mmlu_1508` | `mcq` | true | `D` | `D. Network or transport layer` |
| baseline | `mmlu_1509` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1510` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1511` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1512` | `mcq` | true | `B` | `B. 4-way handshake` |
| baseline | `mmlu_1513` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1514` | `mcq` | true | `D` | `D. SQL queries based on user input` |
| baseline | `mmlu_1515` | `mcq` | false | `A` | `D. False, True` |
| baseline | `mmlu_1516` | `mcq` | true | `D` | `D. Wireshark` |
| baseline | `mmlu_1517` | `mcq` | true | `B` | `B. backdoor` |
| baseline | `mmlu_1518` | `mcq` | false | `C` | `CBF` |
| baseline | `mmlu_1519` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1520` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1521` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1522` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1523` | `mcq` | true | `A` | `A. IM - Trojans` |
| baseline | `mmlu_1524` | `mcq` | false | `B` | `A. 32` |
| baseline | `mmlu_1525` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1526` | `mcq` | false | `B` | `A. Port, network, and services` |
| baseline | `mmlu_1527` | `mcq` | true | `A` | `A. Message Nonrepudiation` |
| baseline | `mmlu_1528` | `mcq` | false | `B` | `D. Network layer` |
| baseline | `mmlu_1529` | `mcq` | false | `B` | `D. Transport Layer Security Protocol` |
| baseline | `mmlu_1530` | `mcq` | true | `D` | `D. Tor browser` |
| baseline | `mmlu_1531` | `mcq` | true | `A` | `A. By overwriting the return address to point to the location of that code` |
| baseline | `mmlu_1532` | `mcq` | false | `A` | `D. Message authentication cipher` |
| baseline | `mmlu_1533` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1534` | `mcq` | true | `D` | `D. UNIX` |
| baseline | `mmlu_1535` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1536` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1537` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1538` | `mcq` | false | `A` | `A, C` |
| baseline | `mmlu_1539` | `mcq` | true | `B` | `B. Metasploit` |
| baseline | `mmlu_1540` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1541` | `mcq` | false | `A` | `D. False, True` |
| baseline | `mmlu_1542` | `mcq` | true | `B` | `B. Message Integrity` |
| baseline | `mmlu_1543` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1544` | `mcq` | true | `A` | `A. Only once` |
| baseline | `mmlu_1545` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1546` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1547` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1548` | `mcq` | true | `C` | `C. Buffer-overflow` |
| baseline | `mmlu_1549` | `mcq` | true | `D` | `D. EtterPeak` |
| baseline | `mmlu_1550` | `mcq` | true | `C` | `C. Base Transceiver Station` |
| baseline | `mmlu_1551` | `mcq` | true | `D` | `D. buffer` |
| baseline | `mmlu_1552` | `mcq` | true | `C` | `C. TKIP` |
| baseline | `mmlu_1553` | `mcq` | true | `A` | `A. buffer` |
| baseline | `mmlu_1554` | `mcq` | true | `C` | `C. WPS` |
| baseline | `mmlu_1555` | `mcq` | false | `C` | `B. Open, half-open, closed` |
| baseline | `mmlu_1556` | `mcq` | true | `A` | `A. WEP` |
| baseline | `mmlu_1557` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1558` | `mcq` | true | `A` | `A. Local variables` |
| baseline | `mmlu_1559` | `mcq` | false | `D` | `B. No, there are no ciphers with perfect secrecy` |
| baseline | `mmlu_1560` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1561` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1562` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1563` | `mcq` | false | `B` | `A. Installing and configuring an Intrusion Detection System (IDS) that can read the IP header.` |
| baseline | `mmlu_1564` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1565` | `mcq` | false | `B` | `C. True, False` |
| baseline | `mmlu_1566` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1567` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1568` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1569` | `mcq` | true | `C` | `C. SMS Trojan` |
| baseline | `mmlu_1570` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1571` | `mcq` | false | `A` | `B. 5 N` |
| baseline | `mmlu_1572` | `mcq` | true | `B` | `B. volume of fluid.` |
| baseline | `mmlu_1573` | `mcq` | true | `B` | `B. passes into the air above` |
| baseline | `mmlu_1574` | `mcq` | false | `B` | `A. always.` |
| baseline | `mmlu_1575` | `mcq` | true | `A` | `A. changes` |
| baseline | `mmlu_1576` | `mcq` | true | `D` | `D. violet` |
| baseline | `mmlu_1577` | `mcq` | true | `D` | `D. All of these.` |
| baseline | `mmlu_1578` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1579` | `mcq` | true | `B` | `B. ordered` |
| baseline | `mmlu_1580` | `mcq` | true | `D` | `D. energy` |
| baseline | `mmlu_1581` | `mcq` | true | `B` | `B. opposite` |
| baseline | `mmlu_1582` | `mcq` | true | `C` | `C. radiation` |
| baseline | `mmlu_1583` | `mcq` | true | `B` | `B. 2 A` |
| baseline | `mmlu_1584` | `mcq` | true | `A` | `A. increase.` |
| baseline | `mmlu_1585` | `mcq` | false | `B` | `D. mg/4` |
| baseline | `mmlu_1586` | `mcq` | true | `A` | `A. less.` |
| baseline | `mmlu_1587` | `mcq` | true | `A` | `A. red.` |
| baseline | `mmlu_1588` | `mcq` | true | `B` | `B. frequency` |
| baseline | `mmlu_1589` | `mcq` | false | `D` | `A. volume` |
| baseline | `mmlu_1590` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1591` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1592` | `mcq` | true | `C` | `C. average translational kinetic energy.` |
| baseline | `mmlu_1593` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1594` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1595` | `mcq` | true | `C` | `C. twice the bend.` |
| baseline | `mmlu_1596` | `mcq` | true | `A` | `A. increases but less than doubles` |
| baseline | `mmlu_1597` | `mcq` | true | `D` | `D. 9 minutes.` |
| baseline | `mmlu_1598` | `mcq` | true | `A` | `A. move at a constant speed in a straight line` |
| baseline | `mmlu_1599` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1600` | `mcq` | false | `C` | `A. evaporation` |
| baseline | `mmlu_1601` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1602` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1603` | `mcq` | false | `C` | `A. increases but less than doubles` |
| baseline | `mmlu_1604` | `mcq` | true | `D` | `D. and mass are closely related.` |
| baseline | `mmlu_1605` | `mcq` | true | `D` | `D. All of these.` |
| baseline | `mmlu_1606` | `mcq` | false | `A` | `B. reduces by 4` |
| baseline | `mmlu_1607` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1608` | `mcq` | true | `C` | `C. 50 km/h` |
| baseline | `mmlu_1609` | `mcq` | true | `D` | `D. frequency` |
| baseline | `mmlu_1610` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1611` | `mcq` | false | `C` | `A. less.` |
| baseline | `mmlu_1612` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1613` | `mcq` | true | `B` | `B. hot day` |
| baseline | `mmlu_1614` | `mcq` | false | `C` | `A. half` |
| baseline | `mmlu_1615` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1616` | `mcq` | true | `A` | `A. hydrogen.` |
| baseline | `mmlu_1617` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1618` | `mcq` | false | `B` | `A. less than 0.8 N` |
| baseline | `mmlu_1619` | `mcq` | true | `A` | `A. along and parallel to the wave` |
| baseline | `mmlu_1620` | `mcq` | false | `A` | `C. Both of these` |
| baseline | `mmlu_1621` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1622` | `mcq` | true | `A` | `A. Inside the nucleus` |
| baseline | `mmlu_1623` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1624` | `mcq` | true | `B` | `B. interference` |
| baseline | `mmlu_1625` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1626` | `mcq` | false | `D` | `B. 2 A` |
| baseline | `mmlu_1627` | `mcq` | true | `C` | `C. Both speed and wavelength` |
| baseline | `mmlu_1628` | `mcq` | false | `B` | `A. 2 Hz` |
| baseline | `mmlu_1629` | `mcq` | true | `D` | `D. amplitude` |
| baseline | `mmlu_1630` | `mcq` | false | `C` | `B. uncharged` |
| baseline | `mmlu_1631` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1632` | `mcq` | true | `C` | `C. thorium-234` |
| baseline | `mmlu_1633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1634` | `mcq` | true | `D` | `D. all of these` |
| baseline | `mmlu_1635` | `mcq` | false | `B` | `D. four times as much` |
| baseline | `mmlu_1636` | `mcq` | false | `C` | `A. breaking the sound barrier` |
| baseline | `mmlu_1637` | `mcq` | false | `B` | `A. becomes slightly radioactive` |
| baseline | `mmlu_1638` | `mcq` | true | `D` | `D. de-excitation.` |
| baseline | `mmlu_1639` | `mcq` | true | `A` | `A. reflected or converted to internal energy in the material.` |
| baseline | `mmlu_1640` | `mcq` | false | `C` | `A. 1/100 as much` |
| baseline | `mmlu_1641` | `mcq` | false | `A` | `C. Both of these` |
| baseline | `mmlu_1642` | `mcq` | false | `A` | `B. less dense` |
| baseline | `mmlu_1643` | `mcq` | false | `C` | `D. All of these.` |
| baseline | `mmlu_1644` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1645` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1646` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1647` | `mcq` | false | `B` | `A. forces` |
| baseline | `mmlu_1648` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1649` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1650` | `mcq` | false | `A` | `C. Both` |
| baseline | `mmlu_1651` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1652` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1653` | `mcq` | true | `A` | `A. 1/10 s` |
| baseline | `mmlu_1654` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1655` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1656` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1657` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1658` | `mcq` | true | `C` | `C. waves` |
| baseline | `mmlu_1659` | `mcq` | true | `A` | `A. high temperatures` |
| baseline | `mmlu_1660` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1661` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1662` | `mcq` | true | `B` | `B. are included in the wire` |
| baseline | `mmlu_1663` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1664` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1665` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1666` | `mcq` | false | `B` | `D. may be greater or less than mg depending on the speed of the ball` |
| baseline | `mmlu_1667` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1668` | `mcq` | false | `A` | `D. lined up during spring` |
| baseline | `mmlu_1669` | `mcq` | true | `A` | `A. 25 cm` |
| baseline | `mmlu_1670` | `mcq` | true | `A` | `A. lower` |
| baseline | `mmlu_1671` | `mcq` | false | `C` | `D. violet` |
| baseline | `mmlu_1672` | `mcq` | true | `B` | `B. 3 A` |
| baseline | `mmlu_1673` | `mcq` | false | `D` | `A. Magnesium-22` |
| baseline | `mmlu_1674` | `mcq` | false | `B` | `C. more than 20 years.` |
| baseline | `mmlu_1675` | `mcq` | true | `A` | `A. hydrogen` |
| baseline | `mmlu_1676` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1677` | `mcq` | false | `D` | `C. three times greater` |
| baseline | `mmlu_1678` | `mcq` | false | `B` | `A. less mass per nucleon` |
| baseline | `mmlu_1679` | `mcq` | true | `C` | `C. radiation.` |
| baseline | `mmlu_1680` | `mcq` | true | `A` | `A. higher order to lower order` |
| baseline | `mmlu_1681` | `mcq` | true | `C` | `C. radioactivity.` |
| baseline | `mmlu_1682` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1683` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1684` | `mcq` | true | `B` | `B. period` |
| baseline | `mmlu_1685` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1686` | `mcq` | false | `A` | `B. released by the water` |
| baseline | `mmlu_1687` | `mcq` | false | `B` | `A. twice as strong` |
| baseline | `mmlu_1688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1689` | `mcq` | false | `B` | `A. produces more tension in the rope than the opponent` |
| baseline | `mmlu_1690` | `mcq` | true | `C` | `C. Gamma` |
| baseline | `mmlu_1691` | `mcq` | true | `B` | `B. fluids` |
| baseline | `mmlu_1692` | `mcq` | false | `D` | `C. 10 V` |
| baseline | `mmlu_1693` | `mcq` | true | `B` | `B. 14 m/s` |
| baseline | `mmlu_1694` | `mcq` | true | `C` | `C. 4 km/h` |
| baseline | `mmlu_1695` | `mcq` | true | `B` | `B. Faraday’s law` |
| baseline | `mmlu_1696` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1697` | `mcq` | false | `C` | `A. gamma radiation.` |
| baseline | `mmlu_1698` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1699` | `mcq` | false | `B` | `C.干涉` |
| baseline | `mmlu_1700` | `mcq` | false | `C` | `A. 0 kelvin` |
| baseline | `mmlu_1701` | `mcq` | true | `A` | `A. speed and direction` |
| baseline | `mmlu_1702` | `mcq` | true | `D` | `D. natural frequency` |
| baseline | `mmlu_1703` | `mcq` | true | `B` | `B. decreases` |
| baseline | `mmlu_1704` | `mcq` | false | `C` | `A. red` |
| baseline | `mmlu_1705` | `mcq` | true | `B` | `B. younger.` |
| baseline | `mmlu_1706` | `mcq` | true | `A` | `A.(horizontal)` |
| baseline | `mmlu_1707` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1708` | `mcq` | false | `B` | `D. Any of these` |
| baseline | `mmlu_1709` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1710` | `mcq` | false | `B` | `A. lunar eclipse.` |
| baseline | `mmlu_1711` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1712` | `mcq` | false | `C` | `B. decrease` |
| baseline | `mmlu_1713` | `mcq` | true | `A` | `A. halve.` |
| baseline | `mmlu_1714` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1715` | `mcq` | true | `D` | `D. scattering` |
| baseline | `mmlu_1716` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1717` | `mcq` | false | `B` | `D. Higher than 30°C` |
| baseline | `mmlu_1718` | `mcq` | false | `B` | `A. one-quarter.` |
| baseline | `mmlu_1719` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1720` | `mcq` | true | `D` | `D. More information is needed` |
| baseline | `mmlu_1721` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1722` | `mcq` | true | `A` | `A. also increases.` |
| baseline | `mmlu_1723` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1724` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1725` | `mcq` | true | `B` | `B. Sound` |
| baseline | `mmlu_1726` | `mcq` | false | `D` | `A. zero` |
| baseline | `mmlu_1727` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1728` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1729` | `mcq` | true | `C` | `C. Both` |
| baseline | `mmlu_1730` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1731` | `mcq` | false | `B` | `C. may be greater or less than mg` |
| baseline | `mmlu_1732` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1733` | `mcq` | true | `B` | `B. 500 W` |
| baseline | `mmlu_1734` | `mcq` | true | `B` | `B.干涉` |
| baseline | `mmlu_1735` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1736` | `mcq` | false | `C` | `B. mass` |
| baseline | `mmlu_1737` | `mcq` | false | `B` | `C. Both of these` |
| baseline | `mmlu_1738` | `mcq` | false | `D` | `C. Both of these.` |
| baseline | `mmlu_1739` | `mcq` | false | `D` | `B. energy` |
| baseline | `mmlu_1740` | `mcq` | true | `C` | `C. Both of these` |
| baseline | `mmlu_1741` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1742` | `mcq` | true | `B` | `B. 26` |
| baseline | `mmlu_1743` | `mcq` | true | `B` | `B. reflects red` |
| baseline | `mmlu_1744` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1745` | `mcq` | false | `A` | `D. white` |
| baseline | `mmlu_1746` | `mcq` | false | `A` | `B. 50%` |
| baseline | `mmlu_1747` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1748` | `mcq` | false | `D` | `C. 8 N` |
| baseline | `mmlu_1749` | `mcq` | false | `D` | `B. 500 J` |
| baseline | `mmlu_1750` | `mcq` | true | `D` | `D. 32q.` |
| baseline | `mmlu_1751` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1752` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1753` | `mcq` | true | `B` | `B. frequency` |
| baseline | `mmlu_1754` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1755` | `mcq` | false | `B` | `A. reduces by 2` |
| baseline | `mmlu_1756` | `mcq` | false | `A` | `C. Both of these` |
| baseline | `mmlu_1757` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1758` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1759` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1760` | `mcq` | true | `A` | `A. shorter in the direction of travel.` |
| baseline | `mmlu_1761` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1762` | `mcq` | false | `A` | `C. less than 9.8 m/s²` |
| baseline | `mmlu_1763` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1764` | `mcq` | true | `D` | `D. ejected neutrons` |
| baseline | `mmlu_1765` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1766` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1767` | `mcq` | false | `B` | `A. steady in one direction` |
| baseline | `mmlu_1768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1769` | `mcq` | true | `B` | `B. 3000 N` |
| baseline | `mmlu_1770` | `mcq` | true | `B` | `B. wavelength` |
| baseline | `mmlu_1771` | `mcq` | false | `B` | `D. All of these` |
| baseline | `mmlu_1772` | `mcq` | true | `B` | `B. second law` |
| baseline | `mmlu_1773` | `mcq` | true | `A` | `A. heated water` |
| baseline | `mmlu_1774` | `mcq` | false | `B` | `A. warm the water` |
| baseline | `mmlu_1775` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1776` | `mcq` | false | `D` | `A. current` |
| baseline | `mmlu_1777` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1778` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1779` | `mcq` | true | `B` | `B. twice as much` |
| baseline | `mmlu_1780` | `mcq` | false | `C` | `B. 24.0 m` |
| baseline | `mmlu_1781` | `mcq` | false | `C` | `D. All of these` |
| baseline | `mmlu_1782` | `mcq` | true | `C` | `C. radioactivity` |
| baseline | `mmlu_1783` | `mcq` | true | `A` | `A. positive` |
| baseline | `mmlu_1784` | `mcq` | true | `D` | `D. spectrum.` |
| baseline | `mmlu_1785` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1786` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1787` | `mcq` | false | `B` | `A. reduces by 1` |
| baseline | `mmlu_1788` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1789` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1790` | `mcq` | false | `D` | `C. All of these.` |
| baseline | `mmlu_1791` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1792` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1793` | `mcq` | false | `B` | `A. near the rotational axis` |
| baseline | `mmlu_1794` | `mcq` | true | `C` | `C. decreases` |
| baseline | `mmlu_1795` | `mcq` | true | `D` | `D. All of these` |
| baseline | `mmlu_1796` | `mcq` | false | `B` | `A. hold particles together` |
| baseline | `mmlu_1797` | `mcq` | true | `B` | `B. second law` |
| baseline | `mmlu_1798` | `mcq` | false | `B` | `A. wavelength` |
| baseline | `mmlu_1799` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1800` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1801` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1802` | `mcq` | true | `C` | `C. 0.125 g` |
| baseline | `mmlu_1803` | `mcq` | false | `B` | `A. decreased temperatures` |
| baseline | `mmlu_1804` | `mcq` | true | `A` | `A. tension.` |
| baseline | `mmlu_1805` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1806` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1807` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1808` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1809` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1810` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1811` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1812` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1813` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1814` | `mcq` | false | `B` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1815` | `mcq` | false | `C` | `D. Bigger than 1` |
| baseline | `mmlu_1816` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_1817` | `mcq` | true | `D` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1818` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1819` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1820` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1821` | `mcq` | false | `A` | `B. (i) and (iii) only` |
| baseline | `mmlu_1822` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1823` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1824` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1825` | `mcq` | false | `B` | `D. 1 and -3` |
| baseline | `mmlu_1826` | `mcq` | true | `B` | `B. The explanatory variable is fixed in repeated samples` |
| baseline | `mmlu_1827` | `mcq` | false | `D` | `C. Residuals appear not to be autocorrelated` |
| baseline | `mmlu_1828` | `mcq` | false | `A` | `D. (i), (ii), (iii), and (iv)` |
| baseline | `mmlu_1829` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_1830` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1831` | `mcq` | true | `A` | `A. The current value of y` |
| baseline | `mmlu_1832` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1833` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1834` | `mcq` | false | `D` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1835` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1836` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1837` | `mcq` | false | `D` | `B. (i) and (iii) only` |
| baseline | `mmlu_1838` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1839` | `mcq` | false | `A` | `C. A model whose dependent variable has recently exhibited a structural change` |
| baseline | `mmlu_1840` | `mcq` | true | `A` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1841` | `mcq` | false | `C` | `A. The roots of the characteristic equation must all lie inside the unit circle` |
| baseline | `mmlu_1842` | `mcq` | false | `B` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1843` | `mcq` | true | `B` | `B. Subtracting the mean of each entity away from each observation on that entity` |
| baseline | `mmlu_1844` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1845` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1846` | `mcq` | true | `C` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1847` | `mcq` | false | `B` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1848` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1849` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1850` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1851` | `mcq` | false | `C` | `D. 1.96` |
| baseline | `mmlu_1852` | `mcq` | true | `A` | `A. 77.07` |
| baseline | `mmlu_1853` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1854` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_1855` | `mcq` | false | `A` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1856` | `mcq` | false | `A` | `C. The disturbance term is assumed to be correlated with x` |
| baseline | `mmlu_1857` | `mcq` | false | `C` | `D. A random walk with drift` |
| baseline | `mmlu_1858` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1859` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1860` | `mcq` | true | `C` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1861` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_1862` | `mcq` | false | `D` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1863` | `mcq` | true | `A` | `A. The variance of the errors is not constant` |
| baseline | `mmlu_1864` | `mcq` | true | `C` | `C. Close to minus one` |
| baseline | `mmlu_1865` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1866` | `mcq` | true | `C` | `C.` |
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
| baseline | `mmlu_1878` | `mcq` | false | `D` | `A. Use a logarithmic functional form instead of a linear one` |
| baseline | `mmlu_1879` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1880` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1881` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1882` | `mcq` | true | `A` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1883` | `mcq` | true | `A` | `A. Censored` |
| baseline | `mmlu_1884` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1885` | `mcq` | true | `B` | `B. T x 1` |
| baseline | `mmlu_1886` | `mcq` | false | `D` | `A. 12` |
| baseline | `mmlu_1887` | `mcq` | false | `D` | `A. The RSS for the whole sample` |
| baseline | `mmlu_1888` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1889` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1890` | `mcq` | true | `B` | `B. Unit root process` |
| baseline | `mmlu_1891` | `mcq` | true | `D` | `D. The Breusch-Godfrey test` |
| baseline | `mmlu_1892` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1893` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1894` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1895` | `mcq` | true | `B` | `B. A multinomial logit` |
| baseline | `mmlu_1896` | `mcq` | false | `D` | `B. (i) and (iii) only` |
| baseline | `mmlu_1897` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1898` | `mcq` | true | `C` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1899` | `mcq` | true | `C` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1900` | `mcq` | true | `C` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1901` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1902` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1903` | `mcq` | false | `B` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1904` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1905` | `mcq` | false | `D` | `A. 0.4` |
| baseline | `mmlu_1906` | `mcq` | false | `B` | `D. (i), (ii), (iii) and (iv)` |
| baseline | `mmlu_1907` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1908` | `mcq` | false | `D` | `A. (-4.79,2.19)` |
| baseline | `mmlu_1909` | `mcq` | false | `D` | `C. (i), (ii), and (iii) only` |
| baseline | `mmlu_1910` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1911` | `mcq` | false | `B` | `D. It is not possible to determine the statistical significance since no standard errors have been given` |
| baseline | `mmlu_1912` | `mcq` | true | `C` | `C. How well the sample regression function fits the data.` |
| baseline | `mmlu_1913` | `mcq` | true | `B` | `B. (i) and (iii) only` |
| baseline | `mmlu_1914` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1915` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1916` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1917` | `mcq` | false | `B` | `D. (i), (ii), and (iii)` |
| baseline | `mmlu_1918` | `mcq` | true | `B` | `B. The variables are not cointegrated` |
| baseline | `mmlu_1919` | `mcq` | false | `C` | `A. (ii) and (iv) only` |
| baseline | `mmlu_1920` | `mcq` | true | `D` | `D. Both A and C` |
| baseline | `mmlu_1921` | `mcq` | true | `D` | `D. It does not load the circuit at all.` |
| baseline | `mmlu_1922` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1923` | `mcq` | true | `A` | `A. 30° to 150°.` |
| baseline | `mmlu_1924` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1925` | `mcq` | true | `D` | `D. zero.` |
| baseline | `mmlu_1926` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1927` | `mcq` | true | `D` | `D. Both A and B` |
| baseline | `mmlu_1928` | `mcq` | true | `A` | `A. 1.5 KV.` |
| baseline | `mmlu_1929` | `mcq` | true | `A` | `A. 1MHz to 500 MHz` |
| baseline | `mmlu_1930` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1931` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_1932` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_1933` | `mcq` | true | `D` | `D. convert AC armature current into DC` |
| baseline | `mmlu_1934` | `mcq` | false | `C` | `D. none of these` |
| baseline | `mmlu_1935` | `mcq` | false | `C` | `B. 6` |
| baseline | `mmlu_1936` | `mcq` | true | `A` | `A. First digit from left to right` |
| baseline | `mmlu_1937` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1938` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1939` | `mcq` | true | `A` | `A. 111.9 ohm` |
| baseline | `mmlu_1940` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1941` | `mcq` | true | `B` | `B. 0.15 joule.` |
| baseline | `mmlu_1942` | `mcq` | false | `B` | `A. protect the insulation.` |
| baseline | `mmlu_1943` | `mcq` | true | `A` | `A. closed winding` |
| baseline | `mmlu_1944` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1945` | `mcq` | true | `D` | `D. 10 KHz to 400 KHz.` |
| baseline | `mmlu_1946` | `mcq` | false | `B` | `C. J = 0, K = 1.` |
| baseline | `mmlu_1947` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1948` | `mcq` | false | `B` | `A. 0.32.` |
| baseline | `mmlu_1949` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1950` | `mcq` | true | `C` | `C. RC.` |
| baseline | `mmlu_1951` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1952` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1953` | `mcq` | true | `C` | `C. 4` |
| baseline | `mmlu_1954` | `mcq` | true | `B` | `B. conducting materials which may be either magnetic or non-magnetic materials.` |
| baseline | `mmlu_1955` | `mcq` | true | `A` | `A. 10` |
| baseline | `mmlu_1956` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1957` | `mcq` | true | `A` | `A. Reciprocity theorem` |
| baseline | `mmlu_1958` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1959` | `mcq` | false | `B` | `A. 500 Hz.` |
| baseline | `mmlu_1960` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_1961` | `mcq` | false | `B` | `A. SRAM` |
| baseline | `mmlu_1962` | `mcq` | false | `A` | `B. 4` |
| baseline | `mmlu_1963` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1964` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1965` | `mcq` | true | `B` | `B. frequency modulation.` |
| baseline | `mmlu_1966` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1967` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1968` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_1969` | `mcq` | true | `C` | `C. 2121.32 A.` |
| baseline | `mmlu_1970` | `mcq` | false | `C` | `D. Registers` |
| baseline | `mmlu_1971` | `mcq` | true | `D` | `D. all of the above.` |
| baseline | `mmlu_1972` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1973` | `mcq` | true | `D` | `D. Off Switch` |
| baseline | `mmlu_1974` | `mcq` | true | `B` | `B. crystal filter.` |
| baseline | `mmlu_1975` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1976` | `mcq` | true | `A` | `A. resolution.` |
| baseline | `mmlu_1977` | `mcq` | true | `C` | `C. Amplitude Modulation` |
| baseline | `mmlu_1978` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_1979` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1980` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1981` | `mcq` | false | `C` | `D. unchanged.` |
| baseline | `mmlu_1982` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1983` | `mcq` | true | `A` | `A. Carbon.` |
| baseline | `mmlu_1984` | `mcq` | true | `D` | `D. All the above` |
| baseline | `mmlu_1985` | `mcq` | true | `C` | `C. Both A and B.` |
| baseline | `mmlu_1986` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1987` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1988` | `mcq` | true | `C` | `C. level` |
| baseline | `mmlu_1989` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1990` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1991` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1992` | `mcq` | false | `C` | `A. LED` |
| baseline | `mmlu_1993` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1994` | `mcq` | false | `B` | `A. Core less furnace.` |
| baseline | `mmlu_1995` | `mcq` | true | `D` | `D. all of above.` |
| baseline | `mmlu_1996` | `mcq` | false | `C` | `A. Resistor` |
| baseline | `mmlu_1997` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1998` | `mcq` | true | `D` | `D. All of these.` |
| baseline | `mmlu_1999` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2000` | `mcq` | false | `A` | `C. 125 MVA` |
| baseline | `mmlu_2001` | `mcq` | true | `B` | `B. jumping from one allowed orbit to another.` |
| baseline | `mmlu_2002` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2003` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_2004` | `mcq` | true | `A` | `A. 160 µF` |
| baseline | `mmlu_2005` | `mcq` | false | `C` | `D. 8R Ω` |
| baseline | `mmlu_2006` | `mcq` | true | `B` | `B. RLC underdamped.` |
| baseline | `mmlu_2007` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2008` | `mcq` | true | `C` | `C. high` |
| baseline | `mmlu_2009` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2010` | `mcq` | true | `D` | `D. all of the above.` |
| baseline | `mmlu_2011` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_2012` | `mcq` | false | `B` | `A. high.` |
| baseline | `mmlu_2013` | `mcq` | true | `A` | `A. lower surface of the conductor.` |
| baseline | `mmlu_2014` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_2015` | `mcq` | false | `D` | `B. Microphone` |
| baseline | `mmlu_2016` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2017` | `mcq` | false | `B` | `C. synchros` |
| baseline | `mmlu_2018` | `mcq` | false | `D` | `C. 10 µF` |
| baseline | `mmlu_2019` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2020` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2021` | `mcq` | true | `B` | `B. clean.` |
| baseline | `mmlu_2022` | `mcq` | false | `C` | `A. 23 mA.` |
| baseline | `mmlu_2023` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2024` | `mcq` | true | `D` | `D. Any one or combinations of the above methods` |
| baseline | `mmlu_2025` | `mcq` | false | `D` | `A. LC circuit.` |
| baseline | `mmlu_2026` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2027` | `mcq` | true | `B` | `B. Analog quantity` |
| baseline | `mmlu_2028` | `mcq` | false | `C` | `B. 140.` |
| baseline | `mmlu_2029` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2030` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2031` | `mcq` | true | `A` | `A. Snubber circuit.` |
| baseline | `mmlu_2032` | `mcq` | true | `B` | `B. Directives` |
| baseline | `mmlu_2033` | `mcq` | false | `D` | `A. 386 kbps - 2 mbps.` |
| baseline | `mmlu_2034` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2035` | `mcq` | true | `C` | `C. 1/C` |
| baseline | `mmlu_2036` | `mcq` | true | `C` | `C. both series and parallel frequencies.` |
| baseline | `mmlu_2037` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2038` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2039` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2040` | `mcq` | false | `D` | `B. 0.002 A.` |
| baseline | `mmlu_2041` | `mcq` | true | `A` | `A. An op-code fetch cycle` |
| baseline | `mmlu_2042` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2043` | `mcq` | true | `D` | `D. Both 2 and 3.` |
| baseline | `mmlu_2044` | `mcq` | true | `B` | `B. non linearly.` |
| baseline | `mmlu_2045` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2046` | `mcq` | false | `B` | `A. 40π coulombs.` |
| baseline | `mmlu_2047` | `mcq` | true | `A` | `A. LSB, Least Significant Bit` |
| baseline | `mmlu_2048` | `mcq` | false | `B` | `D. none of above.` |
| baseline | `mmlu_2049` | `mcq` | false | `B` | `A. 3.33 %` |
| baseline | `mmlu_2050` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2051` | `mcq` | false | `A` | `B. PROM` |
| baseline | `mmlu_2052` | `mcq` | true | `C` | `C. both A and B.` |
| baseline | `mmlu_2053` | `mcq` | true | `D` | `D. both A and B` |
| baseline | `mmlu_2054` | `mcq` | false | `B` | `A. in series.` |
| baseline | `mmlu_2055` | `mcq` | false | `C` | `D..Atomic number.` |
| baseline | `mmlu_2056` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2057` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2058` | `mcq` | false | `A` | `D. None of the above` |
| baseline | `mmlu_2059` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2060` | `mcq` | true | `C` | `C. Either AC or DC` |
| baseline | `mmlu_2061` | `mcq` | false | `C` | `A. 1/3` |
| baseline | `mmlu_2062` | `mcq` | true | `C` | `C. T3 & T4` |
| baseline | `mmlu_2063` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2064` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2065` | `mcq` | false | `C` | `A. p = 4` |
| baseline | `mmlu_2066` | `mcq` | true | `C` | `C. 8` |
| baseline | `mmlu_2067` | `mcq` | true | `D` | `D. 5` |
| baseline | `mmlu_2068` | `mcq` | false | `B` | `C. 6` |
| baseline | `mmlu_2069` | `mcq` | true | `B` | `B. 4t = 112; $28` |
| baseline | `mmlu_2070` | `mcq` | true | `C` | `C. 26` |
| baseline | `mmlu_2071` | `mcq` | true | `C` | `C. 12 over 11` |
| baseline | `mmlu_2072` | `mcq` | false | `B` | `D. 12.72` |
| baseline | `mmlu_2073` | `mcq` | true | `D` | `D. 126.26` |
| baseline | `mmlu_2074` | `mcq` | false | `D` | `A. 0.72` |
| baseline | `mmlu_2075` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2076` | `mcq` | false | `D` | `B. 7` |
| baseline | `mmlu_2077` | `mcq` | true | `A` | `A. 8` |
| baseline | `mmlu_2078` | `mcq` | true | `A` | `A. 6` |
| baseline | `mmlu_2079` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2080` | `mcq` | true | `B` | `B. 14 minutes` |
| baseline | `mmlu_2081` | `mcq` | true | `B` | `B. 24` |
| baseline | `mmlu_2082` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2083` | `mcq` | false | `D` | `C. 50` |
| baseline | `mmlu_2084` | `mcq` | false | `A` | `D. 33` |
| baseline | `mmlu_2085` | `mcq` | false | `C` | `B. 12` |
| baseline | `mmlu_2086` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2087` | `mcq` | true | `A` | `A. -7` |
| baseline | `mmlu_2088` | `mcq` | true | `C` | `C. 73` |
| baseline | `mmlu_2089` | `mcq` | true | `B` | `B. 5.7` |
| baseline | `mmlu_2090` | `mcq` | false | `A` | `B. 3.2` |
| baseline | `mmlu_2091` | `mcq` | true | `D` | `D. 45.6` |
| baseline | `mmlu_2092` | `mcq` | false | `D` | `A. 508` |
| baseline | `mmlu_2093` | `mcq` | true | `A` | `A. 100 — 5d` |
| baseline | `mmlu_2094` | `mcq` | true | `A` | `A. 4t` |
| baseline | `mmlu_2095` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2096` | `mcq` | true | `B` | `B. 15 remainder 3` |
| baseline | `mmlu_2097` | `mcq` | false | `A` | `C. 17 over 4` |
| baseline | `mmlu_2098` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2099` | `mcq` | false | `D` | `B. 770 parts` |
| baseline | `mmlu_2100` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2101` | `mcq` | true | `A` | `A. –7` |
| baseline | `mmlu_2102` | `mcq` | true | `D` | `D. p-3` |
| baseline | `mmlu_2103` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2104` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_2105` | `mcq` | false | `B` | `D. 2000 +150x` |
| baseline | `mmlu_2106` | `mcq` | true | `D` | `D. w < 3.3` |
| baseline | `mmlu_2107` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2108` | `mcq` | false | `C` | `A. 156` |
| baseline | `mmlu_2109` | `mcq` | false | `D` | `B. 15, 19` |
| baseline | `mmlu_2110` | `mcq` | true | `B` | `B. 12 cans` |
| baseline | `mmlu_2111` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2112` | `mcq` | false | `C` | `B. 11` |
| baseline | `mmlu_2113` | `mcq` | true | `D` | `D. 840,000` |
| baseline | `mmlu_2114` | `mcq` | true | `D` | `D. -45` |
| baseline | `mmlu_2115` | `mcq` | true | `A` | `A. 21 birds` |
| baseline | `mmlu_2116` | `mcq` | false | `B` | `D. 153` |
| baseline | `mmlu_2117` | `mcq` | false | `B` | `C` |
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
| baseline | `mmlu_2129` | `mcq` | false | `D` | `A. -4` |
| baseline | `mmlu_2130` | `mcq` | false | `C` | `B. 236` |
| baseline | `mmlu_2131` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2132` | `mcq` | false | `A` | `B. 12` |
| baseline | `mmlu_2133` | `mcq` | false | `C` | `B. 180 and 280` |
| baseline | `mmlu_2134` | `mcq` | false | `D` | `B. 7^2 • 11` |
| baseline | `mmlu_2135` | `mcq` | false | `C` | `B. $28.93` |
| baseline | `mmlu_2136` | `mcq` | false | `A` | `C. 320` |
| baseline | `mmlu_2137` | `mcq` | false | `B` | `A. 0.021 repeating` |
| baseline | `mmlu_2138` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2139` | `mcq` | true | `B` | `B. $6,049` |
| baseline | `mmlu_2140` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2141` | `mcq` | true | `A` | `A. $2.82` |
| baseline | `mmlu_2142` | `mcq` | true | `D` | `D. 5 over 6` |
| baseline | `mmlu_2143` | `mcq` | false | `D` | `C. 2 over 12` |
| baseline | `mmlu_2144` | `mcq` | true | `A` | `A. 100,000 books` |
| baseline | `mmlu_2145` | `mcq` | false | `B` | `C. 144` |
| baseline | `mmlu_2146` | `mcq` | true | `A` | `A. -17` |
| baseline | `mmlu_2147` | `mcq` | false | `D` | `A. 2` |
| baseline | `mmlu_2148` | `mcq` | true | `C` | `C. 24 over 5` |
| baseline | `mmlu_2149` | `mcq` | false | `B` | `D. m = 6e` |
| baseline | `mmlu_2150` | `mcq` | false | `D` | `C. 10` |
| baseline | `mmlu_2151` | `mcq` | true | `A` | `A. 8.1` |
| baseline | `mmlu_2152` | `mcq` | false | `C` | `B. 130°` |
| baseline | `mmlu_2153` | `mcq` | true | `B` | `B. 66.5 seconds` |
| baseline | `mmlu_2154` | `mcq` | false | `B` | `A. 18` |
| baseline | `mmlu_2155` | `mcq` | true | `C` | `C. 180` |
| baseline | `mmlu_2156` | `mcq` | false | `A` | `B. 1:05` |
| baseline | `mmlu_2157` | `mcq` | false | `B` | `A. 6` |
| baseline | `mmlu_2158` | `mcq` | true | `A` | `A. 48` |
| baseline | `mmlu_2159` | `mcq` | false | `C` | `B. 21` |
| baseline | `mmlu_2160` | `mcq` | false | `D` | `B. 154 feet 8 inches` |
| baseline | `mmlu_2161` | `mcq` | false | `C` | `A. $5,434` |
| baseline | `mmlu_2162` | `mcq` | true | `A` | `A. 1` |
| baseline | `mmlu_2163` | `mcq` | true | `A` | `A. 0.261` |
| baseline | `mmlu_2164` | `mcq` | false | `C` | `B. 3.6` |
| baseline | `mmlu_2165` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2166` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2167` | `mcq` | true | `B` | `B. 4.5 centimeters` |
| baseline | `mmlu_2168` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2169` | `mcq` | false | `A` | `B. 2,400` |
| baseline | `mmlu_2170` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2171` | `mcq` | true | `C` | `C. 300 seniors` |
| baseline | `mmlu_2172` | `mcq` | false | `C` | `D. Start with 5. Add 5 each time to get the next number.` |
| baseline | `mmlu_2173` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2174` | `mcq` | true | `B` | `B. subtract 20 from 180` |
| baseline | `mmlu_2175` | `mcq` | false | `C` | `A. 25 minutes` |
| baseline | `mmlu_2176` | `mcq` | false | `B` | `D. 231 = 46w` |
| baseline | `mmlu_2177` | `mcq` | true | `B` | `B. 9` |
| baseline | `mmlu_2178` | `mcq` | false | `A` | `C. 1,493` |
| baseline | `mmlu_2179` | `mcq` | true | `A` | `A. 16 hours` |
| baseline | `mmlu_2180` | `mcq` | false | `D` | `A. 6` |
| baseline | `mmlu_2181` | `mcq` | true | `A` | `A. 34.18 L` |
| baseline | `mmlu_2182` | `mcq` | true | `B` | `B. 2.5` |
| baseline | `mmlu_2183` | `mcq` | false | `B` | `D. 1 hour 44 minutes` |
| baseline | `mmlu_2184` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2185` | `mcq` | false | `B` | `A. $1.40` |
| baseline | `mmlu_2186` | `mcq` | false | `A` | `B. 100` |
| baseline | `mmlu_2187` | `mcq` | true | `A` | `A. 18x+15` |
| baseline | `mmlu_2188` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2189` | `mcq` | false | `B` | `A. $4.46` |
| baseline | `mmlu_2190` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2191` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2192` | `mcq` | false | `C` | `D. 8` |
| baseline | `mmlu_2193` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2194` | `mcq` | false | `D` | `C. 19,612` |
| baseline | `mmlu_2195` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2196` | `mcq` | false | `D` | `A. 82 km/h` |
| baseline | `mmlu_2197` | `mcq` | true | `B` | `B. 25 meters` |
| baseline | `mmlu_2198` | `mcq` | true | `C` | `C. 130 minutes` |
| baseline | `mmlu_2199` | `mcq` | false | `C` | `B. 144` |
| baseline | `mmlu_2200` | `mcq` | false | `C` | `A. 64` |
| baseline | `mmlu_2201` | `mcq` | true | `C` | `C. surveying a group of people standing in line for tickets` |
| baseline | `mmlu_2202` | `mcq` | false | `D` | `A. 9` |
| baseline | `mmlu_2203` | `mcq` | false | `B` | `D. 202.25` |
| baseline | `mmlu_2204` | `mcq` | false | `C` | `A. 22` |
| baseline | `mmlu_2205` | `mcq` | true | `D` | `D. 120` |
| baseline | `mmlu_2206` | `mcq` | false | `C` | `A. 194` |
| baseline | `mmlu_2207` | `mcq` | true | `D` | `D. 9` |
| baseline | `mmlu_2208` | `mcq` | true | `A` | `A. 3:58 p.m.` |
| baseline | `mmlu_2209` | `mcq` | true | `B` | `B. 1 and 1 over 2 ft` |
| baseline | `mmlu_2210` | `mcq` | true | `C` | `C. 120` |
| baseline | `mmlu_2211` | `mcq` | false | `D` | `B. 5:01` |
| baseline | `mmlu_2212` | `mcq` | true | `C` | `C. 20x5=n` |
| baseline | `mmlu_2213` | `mcq` | false | `C` | `B. 17` |
| baseline | `mmlu_2214` | `mcq` | true | `B` | `B. 4(3) + 4(2)` |
| baseline | `mmlu_2215` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2216` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2217` | `mcq` | false | `A` | `B. 258` |
| baseline | `mmlu_2218` | `mcq` | false | `C` | `B. conducting the survey at all shoe stores` |
| baseline | `mmlu_2219` | `mcq` | false | `D` | `C. 665 feet` |
| baseline | `mmlu_2220` | `mcq` | false | `D` | `A. 12 students` |
| baseline | `mmlu_2221` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2222` | `mcq` | true | `A` | `A. 6 stickers` |
| baseline | `mmlu_2223` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2224` | `mcq` | false | `B` | `D. 7` |
| baseline | `mmlu_2225` | `mcq` | true | `A` | `A. 8 over 12` |
| baseline | `mmlu_2226` | `mcq` | true | `D` | `D. 25 × 8` |
| baseline | `mmlu_2227` | `mcq` | true | `D` | `D. 2,144` |
| baseline | `mmlu_2228` | `mcq` | false | `D` | `C. 32.54` |
| baseline | `mmlu_2229` | `mcq` | false | `B` | `A. about 10` |
| baseline | `mmlu_2230` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2231` | `mcq` | true | `A` | `A. 100 and 299` |
| baseline | `mmlu_2232` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2233` | `mcq` | false | `C` | `B. 4 days` |
| baseline | `mmlu_2234` | `mcq` | true | `C` | `C. 18` |
| baseline | `mmlu_2235` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2236` | `mcq` | true | `A` | `A. 7` |
| baseline | `mmlu_2237` | `mcq` | false | `C` | `B. 20` |
| baseline | `mmlu_2238` | `mcq` | true | `C` | `C. 77` |
| baseline | `mmlu_2239` | `mcq` | false | `A` | `D. -62` |
| baseline | `mmlu_2240` | `mcq` | true | `C` | `C. 800` |
| baseline | `mmlu_2241` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2242` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2243` | `mcq` | false | `B` | `D. 20 over 28` |
| baseline | `mmlu_2244` | `mcq` | true | `A` | `A. -63` |
| baseline | `mmlu_2245` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2246` | `mcq` | false | `C` | `D. 3,000` |
| baseline | `mmlu_2247` | `mcq` | false | `B` | `D. 1,046` |
| baseline | `mmlu_2248` | `mcq` | true | `B` | `B. 6 gallons` |
| baseline | `mmlu_2249` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2250` | `mcq` | false | `D` | `A. 860,460 gallons` |
| baseline | `mmlu_2251` | `mcq` | false | `D` | `C. 640` |
| baseline | `mmlu_2252` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2253` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_2254` | `mcq` | true | `B` | `B. 15` |
| baseline | `mmlu_2255` | `mcq` | false | `D` | `A. 274 square miles per county` |
| baseline | `mmlu_2256` | `mcq` | true | `B` | `B. -49°C` |
| baseline | `mmlu_2257` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2258` | `mcq` | false | `D` | `B. 27` |
| baseline | `mmlu_2259` | `mcq` | false | `C` | `D. 6.3 miles` |
| baseline | `mmlu_2260` | `mcq` | true | `B` | `B. 0.0261` |
| baseline | `mmlu_2261` | `mcq` | false | `B` | `A. Between 4 and 7 lb` |
| baseline | `mmlu_2262` | `mcq` | true | `B` | `B. 30/5` |
| baseline | `mmlu_2263` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2264` | `mcq` | true | `D` | `D. -1.1` |
| baseline | `mmlu_2265` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2266` | `mcq` | false | `C` | `B. 77` |
| baseline | `mmlu_2267` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_2268` | `mcq` | true | `B` | `B. 18` |
| baseline | `mmlu_2269` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2270` | `mcq` | false | `D` | `A. 1.6` |
| baseline | `mmlu_2271` | `mcq` | false | `D` | `C. 12 – 2 – 2 – 2` |
| baseline | `mmlu_2272` | `mcq` | true | `B` | `B. 7^3` |
| baseline | `mmlu_2273` | `mcq` | false | `D` | `B. 29` |
| baseline | `mmlu_2274` | `mcq` | true | `C` | `C. 32` |
| baseline | `mmlu_2275` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2276` | `mcq` | false | `C` | `B. 12 cm` |
| baseline | `mmlu_2277` | `mcq` | true | `C` | `C. 56` |
| baseline | `mmlu_2278` | `mcq` | false | `B` | `D. 300.59` |
| baseline | `mmlu_2279` | `mcq` | true | `A` | `A. $32.30` |
| baseline | `mmlu_2280` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_2281` | `mcq` | true | `B` | `B. $45` |
| baseline | `mmlu_2282` | `mcq` | false | `A` | `B. -7.4` |
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
| baseline | `mmlu_2295` | `mcq` | false | `B` | `A. 7:00 a.m.` |
| baseline | `mmlu_2296` | `mcq` | true | `C` | `C. $0.40` |
| baseline | `mmlu_2297` | `mcq` | true | `D` | `D. 2^4 • 3` |
| baseline | `mmlu_2298` | `mcq` | true | `B` | `B. 56` |
| baseline | `mmlu_2299` | `mcq` | false | `D` | `C. 11.5` |
| baseline | `mmlu_2300` | `mcq` | false | `D` | `B. 11 in.` |
| baseline | `mmlu_2301` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2302` | `mcq` | true | `A` | `A. 158` |
| baseline | `mmlu_2303` | `mcq` | false | `D` | `B. 1,801 R1` |
| baseline | `mmlu_2304` | `mcq` | false | `D` | `A. 1.33 cm` |
| baseline | `mmlu_2305` | `mcq` | true | `D` | `D. 393 ÷ 3` |
| baseline | `mmlu_2306` | `mcq` | true | `B` | `B. -9` |
| baseline | `mmlu_2307` | `mcq` | true | `C` | `C. 5` |
| baseline | `mmlu_2308` | `mcq` | true | `B` | `B. 12 × 7` |
| baseline | `mmlu_2309` | `mcq` | false | `B` | `A. 75 miles` |
| baseline | `mmlu_2310` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2311` | `mcq` | false | `B` | `A. 10 minutes` |
| baseline | `mmlu_2312` | `mcq` | true | `A` | `A. 3 over 4` |
| baseline | `mmlu_2313` | `mcq` | false | `C` | `A. 1,300 and 1,500` |
| baseline | `mmlu_2314` | `mcq` | true | `D` | `D. 2 • 2 • 2 • 3 • 11` |
| baseline | `mmlu_2315` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2316` | `mcq` | true | `A` | `A. -93` |
| baseline | `mmlu_2317` | `mcq` | true | `A` | `A. 4(x – 22)` |
| baseline | `mmlu_2318` | `mcq` | false | `B` | `D. 1,122,202` |
| baseline | `mmlu_2319` | `mcq` | false | `D` | `B. 3 and 3 over 4` |
| baseline | `mmlu_2320` | `mcq` | true | `A` | `A. $99.89` |
| baseline | `mmlu_2321` | `mcq` | false | `B` | `D. t ÷ 8 = 56` |
| baseline | `mmlu_2322` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2323` | `mcq` | true | `B` | `B. 192` |
| baseline | `mmlu_2324` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2325` | `mcq` | true | `C` | `C. 30` |
| baseline | `mmlu_2326` | `mcq` | false | `D` | `C. 8.027` |
| baseline | `mmlu_2327` | `mcq` | false | `C` | `A. 20 words per minute` |
| baseline | `mmlu_2328` | `mcq` | false | `C` | `B. divide 18 by 3` |
| baseline | `mmlu_2329` | `mcq` | true | `D` | `D. 6+4 × p = 18` |
| baseline | `mmlu_2330` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2331` | `mcq` | false | `B` | `A. -85` |
| baseline | `mmlu_2332` | `mcq` | true | `C` | `C. 314` |
| baseline | `mmlu_2333` | `mcq` | true | `A` | `A. 22.75` |
| baseline | `mmlu_2334` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2335` | `mcq` | true | `B` | `B. 260` |
| baseline | `mmlu_2336` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2337` | `mcq` | false | `C` | `D. 5 problems per minute` |
| baseline | `mmlu_2338` | `mcq` | true | `D` | `D. 180` |
| baseline | `mmlu_2339` | `mcq` | true | `B` | `B. $117.30` |
| baseline | `mmlu_2340` | `mcq` | true | `A` | `A. 11` |
| baseline | `mmlu_2341` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2342` | `mcq` | false | `C` | `A. 599` |
| baseline | `mmlu_2343` | `mcq` | true | `A` | `A. 12 horses` |
| baseline | `mmlu_2344` | `mcq` | true | `C` | `C. $52.80` |
| baseline | `mmlu_2345` | `mcq` | false | `C` | `B. 42` |
| baseline | `mmlu_2346` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2347` | `mcq` | true | `C` | `C. 3480 ft^3` |
| baseline | `mmlu_2348` | `mcq` | true | `B` | `B. 380` |
| baseline | `mmlu_2349` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2350` | `mcq` | true | `D` | `D. 5 out of 15` |
| baseline | `mmlu_2351` | `mcq` | true | `C` | `C. 21.4` |
| baseline | `mmlu_2352` | `mcq` | true | `A` | `A. 7 over 24` |
| baseline | `mmlu_2353` | `mcq` | false | `D` | `A. 30 ft by 53 ft` |
| baseline | `mmlu_2354` | `mcq` | false | `A` | `B. 2,400` |
| baseline | `mmlu_2355` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2356` | `mcq` | false | `A` | `C. 4 and 1 over 20` |
| baseline | `mmlu_2357` | `mcq` | true | `A` | `A. 42 ÷ 7` |
| baseline | `mmlu_2358` | `mcq` | true | `D` | `D. 642` |
| baseline | `mmlu_2359` | `mcq` | false | `D` | `C. 12.81` |
| baseline | `mmlu_2360` | `mcq` | true | `C` | `C. 178 remainder 2` |
| baseline | `mmlu_2361` | `mcq` | false | `D` | `B. 88^3` |
| baseline | `mmlu_2362` | `mcq` | true | `C` | `C. 400` |
| baseline | `mmlu_2363` | `mcq` | true | `B` | `B. 13` |
| baseline | `mmlu_2364` | `mcq` | true | `D` | `D. No mode` |
| baseline | `mmlu_2365` | `mcq` | true | `B` | `B. 136` |
| baseline | `mmlu_2366` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2367` | `mcq` | false | `C` | `B. $25.75` |
| baseline | `mmlu_2368` | `mcq` | false | `D` | `C. 15` |
| baseline | `mmlu_2369` | `mcq` | false | `A` | `C. $13.50` |
| baseline | `mmlu_2370` | `mcq` | true | `C` | `C. 4 over 9` |
| baseline | `mmlu_2371` | `mcq` | false | `B` | `C. 29,250 yards^2` |
| baseline | `mmlu_2372` | `mcq` | false | `C` | `B. 5` |
| baseline | `mmlu_2373` | `mcq` | false | `B` | `A. $3` |
| baseline | `mmlu_2374` | `mcq` | false | `C` | `B. 495` |
| baseline | `mmlu_2375` | `mcq` | false | `D` | `B. $26.50` |
| baseline | `mmlu_2376` | `mcq` | true | `D` | `D. 189 days` |
| baseline | `mmlu_2377` | `mcq` | true | `D` | `D. 30x + 15y` |
| baseline | `mmlu_2378` | `mcq` | false | `C` | `B. 40` |
| baseline | `mmlu_2379` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2380` | `mcq` | false | `C` | `B. 830` |
| baseline | `mmlu_2381` | `mcq` | true | `D` | `D. 270°` |
| baseline | `mmlu_2382` | `mcq` | true | `D` | `D. 320` |
| baseline | `mmlu_2383` | `mcq` | false | `D` | `C. 64,000 feet` |
| baseline | `mmlu_2384` | `mcq` | true | `A` | `A. 13 over 36` |
| baseline | `mmlu_2385` | `mcq` | true | `A` | `A. 0.406` |
| baseline | `mmlu_2386` | `mcq` | true | `B` | `B. the total number of students in each teacher’s class` |
| baseline | `mmlu_2387` | `mcq` | false | `D` | `A. dx3=9` |
| baseline | `mmlu_2388` | `mcq` | true | `B` | `B. 43.3` |
| baseline | `mmlu_2389` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2390` | `mcq` | true | `B` | `B. Cup` |
| baseline | `mmlu_2391` | `mcq` | false | `A` | `B. 74.18 m` |
| baseline | `mmlu_2392` | `mcq` | false | `D` | `A. 7-Mar` |
| baseline | `mmlu_2393` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2394` | `mcq` | false | `A` | `To solve the equation \( \frac{z}{7.74} = 6.73 \), we need to isolate \( z \). We do this by multiplying both sides of t` |
| baseline | `mmlu_2395` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2396` | `mcq` | true | `D` | `D. 305,610` |
| baseline | `mmlu_2397` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2398` | `mcq` | false | `C` | `B. -14` |
| baseline | `mmlu_2399` | `mcq` | true | `D` | `D. 60` |
| baseline | `mmlu_2400` | `mcq` | true | `D` | `D. 30 square feet` |
| baseline | `mmlu_2401` | `mcq` | false | `B` | `C. Quadrant III` |
| baseline | `mmlu_2402` | `mcq` | true | `C` | `C. 2 m` |
| baseline | `mmlu_2403` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2404` | `mcq` | true | `B` | `B. 64` |
| baseline | `mmlu_2405` | `mcq` | false | `C` | `A. $17.88` |
| baseline | `mmlu_2406` | `mcq` | true | `D` | `D. 81m + 27t` |
| baseline | `mmlu_2407` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_2408` | `mcq` | false | `A` | `C. 3-Jan` |
| baseline | `mmlu_2409` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_2410` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2411` | `mcq` | false | `D` | `B. 120h` |
| baseline | `mmlu_2412` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2413` | `mcq` | false | `A` | `C. 110` |
| baseline | `mmlu_2414` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2415` | `mcq` | false | `B` | `C. C = 16π` |
| baseline | `mmlu_2416` | `mcq` | false | `D` | `A. $2.19` |
| baseline | `mmlu_2417` | `mcq` | false | `B` | `C. 2,329,333` |
| baseline | `mmlu_2418` | `mcq` | false | `C` | `B. 23 bouquets` |
| baseline | `mmlu_2419` | `mcq` | true | `A` | `A. 25 + (25+ m)` |
| baseline | `mmlu_2420` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2421` | `mcq` | false | `A` | `B. 36 - y = 13` |
| baseline | `mmlu_2422` | `mcq` | true | `B` | `B. 125` |
| baseline | `mmlu_2423` | `mcq` | true | `C` | `C. 48` |
| baseline | `mmlu_2424` | `mcq` | false | `B` | `A. 632` |
| baseline | `mmlu_2425` | `mcq` | false | `C` | `B. 23` |
| baseline | `mmlu_2426` | `mcq` | false | `C` | `D. 3 × 24 = b` |
| baseline | `mmlu_2427` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_2428` | `mcq` | true | `D` | `D. 1,176` |
| baseline | `mmlu_2429` | `mcq` | false | `A` | `D. 1:09` |
| baseline | `mmlu_2430` | `mcq` | false | `C` | `A. 21 over 32` |
| baseline | `mmlu_2431` | `mcq` | true | `D` | `D. 3 over 5` |
| baseline | `mmlu_2432` | `mcq` | false | `C` | `B. -11` |
| baseline | `mmlu_2433` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2434` | `mcq` | true | `B` | `B. 3,750` |
| baseline | `mmlu_2435` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2436` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2437` | `mcq` | true | `B` | `B. 309` |
| baseline | `mmlu_2438` | `mcq` | false | `D` | `C. 120` |
| baseline | `mmlu_2439` | `mcq` | true | `A` | `A. 32` |
| baseline | `mmlu_2440` | `mcq` | false | `D` | `A. 44,500` |
| baseline | `mmlu_2441` | `mcq` | true | `C` | `C. 22` |
| baseline | `mmlu_2442` | `mcq` | true | `B` | `B. Divide 25 by 5` |
| baseline | `mmlu_2443` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2444` | `mcq` | true | `A` | `A. Tdc` |
| baseline | `mmlu_2445` | `mcq` | false | `C` | `A. Some large houses are bigger than some apartments.` |
| baseline | `mmlu_2446` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2447` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2448` | `mcq` | true | `D` | `D. Some houses are bigger than every apartment.` |
| baseline | `mmlu_2449` | `mcq` | false | `D` | `B. Invalid. Counterexample when K is true and L is false` |
| baseline | `mmlu_2450` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2451` | `mcq` | false | `D` | `C. H ⊃ ~E` |
| baseline | `mmlu_2452` | `mcq` | true | `D` | `D. L ∨ ~L` |
| baseline | `mmlu_2453` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2454` | `mcq` | false | `B` | `To solve this problem, we need to construct truth tables for both given statements and then compare them to determine th` |
| baseline | `mmlu_2455` | `mcq` | true | `D` | `D. ~~F` |
| baseline | `mmlu_2456` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2457` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2458` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2459` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2460` | `mcq` | true | `D` | `D. (∀x)(Px ⊃ Sxj)` |
| baseline | `mmlu_2461` | `mcq` | true | `B` | `B. Ijwk` |
| baseline | `mmlu_2462` | `mcq` | true | `B` | `B. (∀x)(Ax ⊃ ~Px)` |
| baseline | `mmlu_2463` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2464` | `mcq` | true | `D` | `D. Mmsi` |
| baseline | `mmlu_2465` | `mcq` | true | `B` | `B. No apartment is bigger than any large house.` |
| baseline | `mmlu_2466` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2467` | `mcq` | true | `D` | `D. P ≡ (D • G)` |
| baseline | `mmlu_2468` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2469` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2470` | `mcq` | true | `A` | `A. B ⊃ W` |
| baseline | `mmlu_2471` | `mcq` | true | `A` | `A. Lt ∨ Le` |
| baseline | `mmlu_2472` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2473` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2474` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2475` | `mcq` | false | `D` | `A. U ⊃ Z` |
| baseline | `mmlu_2476` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2477` | `mcq` | false | `D` | `B. fLh` |
| baseline | `mmlu_2478` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2479` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2481` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2482` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2483` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2484` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2485` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2486` | `mcq` | false | `A` | `C. Neither logically equivalent nor contradictory, but consistent` |
| baseline | `mmlu_2487` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2488` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2489` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2490` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2491` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2492` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2493` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2494` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2495` | `mcq` | false | `D` | `A. ~Bje` |
| baseline | `mmlu_2496` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2497` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2498` | `mcq` | true | `B` | `B. (∃x)(Ax • ~Ix)` |
| baseline | `mmlu_2499` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2500` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2501` | `mcq` | true | `B` | `B. Sc ≡ Ej` |
| baseline | `mmlu_2502` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2503` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2504` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2505` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2506` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2507` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2508` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2509` | `mcq` | true | `D` | `D. Fe ⊃ Ss` |
| baseline | `mmlu_2510` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2511` | `mcq` | false | `D` | `B. (∃x)[(Hx • Bx) ⊃ Mx]` |
| baseline | `mmlu_2512` | `mcq` | true | `A` | `A. Some cookies have oatmeal. If something's not being a cookie entails that it doesn't have chocolate chips, then this ` |
| baseline | `mmlu_2513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2514` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2515` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2516` | `mcq` | false | `A` | `B. Invalid. Counterexample when O is true and P is false` |
| baseline | `mmlu_2517` | `mcq` | true | `D` | `D. Bl ⊃ Sk` |
| baseline | `mmlu_2518` | `mcq` | true | `D` | `D. (G ∨ H) ⊃ ~I` |
| baseline | `mmlu_2519` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2520` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2522` | `mcq` | false | `C` | `B. (∃x)(Sx ∨ Wx)` |
| baseline | `mmlu_2523` | `mcq` | false | `D` | `A. (~F ⊃ E) ∨ (C ≡ ~S)` |
| baseline | `mmlu_2524` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2526` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2527` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2528` | `mcq` | true | `B` | `B. (F • L) • ~C` |
| baseline | `mmlu_2529` | `mcq` | true | `C` | `C. (H ∨ ~G) ⊃ J` |
| baseline | `mmlu_2530` | `mcq` | false | `D` | `B. Invalid. Counterexample when X, Y, and Z are true` |
| baseline | `mmlu_2531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2532` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2533` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2534` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2535` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2536` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2537` | `mcq` | true | `C` | `C. ~Mmis` |
| baseline | `mmlu_2538` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2539` | `mcq` | false | `D` | `C. H ∨ ~R` |
| baseline | `mmlu_2540` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2541` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2542` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2543` | `mcq` | false | `D` | `A. (E ≡ F) ∨ ~(C ≡ S)` |
| baseline | `mmlu_2544` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2545` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2546` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2547` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2548` | `mcq` | true | `A` | `A. (∃x)(Fx • Lx)` |
| baseline | `mmlu_2549` | `mcq` | true | `D` | `D. Gba` |
| baseline | `mmlu_2550` | `mcq` | true | `A` | `A. ~(∀x)(Lx ⊃ Rx)` |
| baseline | `mmlu_2551` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2552` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2553` | `mcq` | false | `B` | `A. (∀x)(Sx ⊃ Fx)` |
| baseline | `mmlu_2554` | `mcq` | true | `B` | `B. Lj` |
| baseline | `mmlu_2555` | `mcq` | true | `A` | `A. (∀x)(Sx ⊃ ~Gx)` |
| baseline | `mmlu_2556` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2557` | `mcq` | false | `D` | `A. (E ⊃ F) ∨ (C ≡ ~S)` |
| baseline | `mmlu_2558` | `mcq` | true | `A` | `A. (E ⊃ F) ∨ (S ⊃ C)` |
| baseline | `mmlu_2559` | `mcq` | false | `C` | `B. ~(M • S)` |
| baseline | `mmlu_2560` | `mcq` | true | `C` | `C. (∀x)(Rx ⊃ Ax)` |
| baseline | `mmlu_2561` | `mcq` | true | `C` | `C. U ⊃ (P • ~B)` |
| baseline | `mmlu_2562` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2563` | `mcq` | true | `A` | `A. (F ⊃ ~E) ∨ (C ≡ ~S)` |
| baseline | `mmlu_2564` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2565` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2566` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2567` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2568` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2569` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2570` | `mcq` | false | `B` | `A. About $300` |
| baseline | `mmlu_2571` | `mcq` | false | `C` | `D. 82%` |
| baseline | `mmlu_2572` | `mcq` | true | `A` | `A. China` |
| baseline | `mmlu_2573` | `mcq` | false | `C` | `B. by 10 fold` |
| baseline | `mmlu_2574` | `mcq` | true | `A` | `A. Lower respiratory infections` |
| baseline | `mmlu_2575` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2576` | `mcq` | false | `C` | `D. 89%` |
| baseline | `mmlu_2577` | `mcq` | false | `C` | `A. 18%` |
| baseline | `mmlu_2578` | `mcq` | false | `B` | `D. 56%` |
| baseline | `mmlu_2579` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2580` | `mcq` | false | `B` | `A. 5%` |
| baseline | `mmlu_2581` | `mcq` | false | `C` | `A. 2%` |
| baseline | `mmlu_2582` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2583` | `mcq` | true | `B` | `B. 56%` |
| baseline | `mmlu_2584` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2585` | `mcq` | false | `A` | `D. 79%` |
| baseline | `mmlu_2586` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2587` | `mcq` | false | `C` | `A. About $3k` |
| baseline | `mmlu_2588` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2589` | `mcq` | false | `A` | `D. 85%` |
| baseline | `mmlu_2590` | `mcq` | false | `A` | `D. 84%` |
| baseline | `mmlu_2591` | `mcq` | false | `D` | `A. 25%` |
| baseline | `mmlu_2592` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2593` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2594` | `mcq` | false | `D` | `B. 47%` |
| baseline | `mmlu_2595` | `mcq` | false | `D` | `A. 1%` |
| baseline | `mmlu_2596` | `mcq` | false | `C` | `D. 83%` |
| baseline | `mmlu_2597` | `mcq` | false | `D` | `A. 10%` |
| baseline | `mmlu_2598` | `mcq` | false | `C` | `A. 26%` |
| baseline | `mmlu_2599` | `mcq` | false | `C` | `A. 690 million` |
| baseline | `mmlu_2600` | `mcq` | false | `A` | `B. 29%` |
| baseline | `mmlu_2601` | `mcq` | false | `B` | `D. 91%` |
| baseline | `mmlu_2602` | `mcq` | false | `C` | `B. by 8 fold` |
| baseline | `mmlu_2603` | `mcq` | true | `D` | `D. 19` |
| baseline | `mmlu_2604` | `mcq` | false | `D` | `A. 59%` |
| baseline | `mmlu_2605` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2606` | `mcq` | true | `B` | `B. 35%` |
| baseline | `mmlu_2607` | `mcq` | false | `D` | `B. by 8 fold` |
| baseline | `mmlu_2608` | `mcq` | false | `C` | `B. 51%` |
| baseline | `mmlu_2609` | `mcq` | true | `B` | `B. 86%` |
| baseline | `mmlu_2610` | `mcq` | false | `A` | `D. 86%` |
| baseline | `mmlu_2611` | `mcq` | false | `C` | `D. Iran` |
| baseline | `mmlu_2612` | `mcq` | true | `A` | `A. 1.2 million` |
| baseline | `mmlu_2613` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2614` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2615` | `mcq` | true | `A` | `A. 26%` |
| baseline | `mmlu_2616` | `mcq` | true | `B` | `B. 45%` |
| baseline | `mmlu_2617` | `mcq` | false | `C` | `B. 16%` |
| baseline | `mmlu_2618` | `mcq` | false | `B` | `A. 43%` |
| baseline | `mmlu_2619` | `mcq` | false | `B` | `A. 0.50%` |
| baseline | `mmlu_2620` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2621` | `mcq` | false | `B` | `A. 12 years` |
| baseline | `mmlu_2622` | `mcq` | false | `D` | `A. 0.90%` |
| baseline | `mmlu_2623` | `mcq` | false | `A` | `D. 44%` |
| baseline | `mmlu_2624` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2625` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2626` | `mcq` | false | `D` | `A. 2%` |
| baseline | `mmlu_2627` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2628` | `mcq` | true | `B` | `B. 34.80%` |
| baseline | `mmlu_2629` | `mcq` | false | `C` | `B. 30 million` |
| baseline | `mmlu_2630` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2631` | `mcq` | false | `B` | `A. 10%` |
| baseline | `mmlu_2632` | `mcq` | false | `C` | `A. 38%` |
| baseline | `mmlu_2633` | `mcq` | true | `B` | `B. True, False` |
| baseline | `mmlu_2634` | `mcq` | true | `C` | `C. 26,000` |
| baseline | `mmlu_2635` | `mcq` | true | `A` | `A. 90%` |
| baseline | `mmlu_2636` | `mcq` | false | `B` | `A. Japan` |
| baseline | `mmlu_2637` | `mcq` | true | `C` | `C. 79%` |
| baseline | `mmlu_2638` | `mcq` | true | `B` | `B. 19%` |
| baseline | `mmlu_2639` | `mcq` | false | `B` | `A. 18%` |
| baseline | `mmlu_2640` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_2641` | `mcq` | false | `B` | `A. 1.5 children per woman` |
| baseline | `mmlu_2642` | `mcq` | true | `C` | `C. $10,000` |
| baseline | `mmlu_2643` | `mcq` | false | `C` | `A. 20%` |
| baseline | `mmlu_2644` | `mcq` | false | `B` | `D. 86%` |
| baseline | `mmlu_2645` | `mcq` | false | `C` | `A. 1%` |
| baseline | `mmlu_2646` | `mcq` | true | `A` | `A. US` |
| baseline | `mmlu_2647` | `mcq` | false | `C` | `D. was approximately 3.0% per year` |
| baseline | `mmlu_2648` | `mcq` | false | `B` | `A. 15%` |
| baseline | `mmlu_2649` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2650` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2651` | `mcq` | false | `A` | `B. 3%` |
| baseline | `mmlu_2652` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_2653` | `mcq` | true | `A` | `A. True, True` |
| baseline | `mmlu_2654` | `mcq` | false | `B` | `A. 80%` |
| baseline | `mmlu_2655` | `mcq` | false | `C` | `B. 56%` |
| baseline | `mmlu_2656` | `mcq` | false | `C` | `A. China` |
| baseline | `mmlu_2657` | `mcq` | false | `C` | `A. $150,000` |
| baseline | `mmlu_2658` | `mcq` | false | `B` | `A. 30%` |
| baseline | `mmlu_2659` | `mcq` | false | `D` | `B. Russia` |
| baseline | `mmlu_2660` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_2661` | `mcq` | true | `D` | `D. 86%` |
| baseline | `mmlu_2662` | `mcq` | false | `B` | `D. 71%` |
| baseline | `mmlu_2663` | `mcq` | false | `B` | `C. 6%` |
| baseline | `mmlu_2664` | `mcq` | false | `B` | `A. 0.70%` |
| baseline | `mmlu_2665` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_2666` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2667` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2668` | `mcq` | false | `D` | `A. 79%` |
| baseline | `mmlu_2669` | `mcq` | true | `A` | `A. directional selection.` |
| baseline | `mmlu_2670` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2671` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2672` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2674` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2675` | `mcq` | true | `B` | `B. Phagocytes` |
| baseline | `mmlu_2676` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2678` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2679` | `mcq` | true | `C` | `C. Memory cells` |
| baseline | `mmlu_2680` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2681` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2682` | `mcq` | false | `D` | `A. Water` |
| baseline | `mmlu_2683` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2684` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2685` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2686` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2689` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2690` | `mcq` | true | `C` | `C. mutualism` |
| baseline | `mmlu_2691` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2692` | `mcq` | true | `B` | `B. maintaining homeostasis.` |
| baseline | `mmlu_2693` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2694` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2695` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2696` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2697` | `mcq` | true | `C` | `C. Mutation` |
| baseline | `mmlu_2698` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2699` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2700` | `mcq` | true | `B` | `B. parthenogenesis` |
| baseline | `mmlu_2701` | `mcq` | false | `C` | `D. Bb bb` |
| baseline | `mmlu_2702` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2703` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2704` | `mcq` | true | `C` | `C. 54%` |
| baseline | `mmlu_2705` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2706` | `mcq` | true | `D` | `D. Mutation` |
| baseline | `mmlu_2707` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2708` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2709` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2710` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2711` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2712` | `mcq` | true | `A` | `A. humans and chimpanzees share a relatively recent common ancestor.` |
| baseline | `mmlu_2713` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2714` | `mcq` | true | `C` | `C. Tropical rainforest` |
| baseline | `mmlu_2715` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_2716` | `mcq` | true | `A` | `A. The bonds linking the monomers of starch differ in shape from the bonds linking the monomers of cellulose.` |
| baseline | `mmlu_2717` | `mcq` | true | `B` | `B. fallopian tube` |
| baseline | `mmlu_2718` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_2719` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2720` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2721` | `mcq` | true | `A` | `A. mitochondrial matrix` |
| baseline | `mmlu_2722` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2723` | `mcq` | true | `D` | `D. S` |
| baseline | `mmlu_2724` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2725` | `mcq` | false | `C` | `D. Promoter` |
| baseline | `mmlu_2726` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2727` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2728` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2729` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2730` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2731` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2732` | `mcq` | false | `C` | `B. Tundra` |
| baseline | `mmlu_2733` | `mcq` | true | `D` | `D. Deciduous forests` |
| baseline | `mmlu_2734` | `mcq` | false | `B` | `C. hyperpolarization` |
| baseline | `mmlu_2735` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2736` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2737` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2738` | `mcq` | true | `C` | `C. Genetic drift` |
| baseline | `mmlu_2739` | `mcq` | true | `B` | `B. the reshuffling of alleles in sexual reproduction.` |
| baseline | `mmlu_2740` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2741` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2742` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2743` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2744` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2745` | `mcq` | true | `D` | `D. A and C only` |
| baseline | `mmlu_2746` | `mcq` | false | `D` | `A. III only` |
| baseline | `mmlu_2747` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2748` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2749` | `mcq` | true | `C` | `C. stabilizing selection` |
| baseline | `mmlu_2750` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2751` | `mcq` | false | `C` | `A. Amount of sunlight` |
| baseline | `mmlu_2752` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2753` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2754` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2755` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2756` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2757` | `mcq` | true | `C` | `C. more recently they shared a common ancestor.` |
| baseline | `mmlu_2758` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2759` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2760` | `mcq` | true | `C` | `C. commensalism.` |
| baseline | `mmlu_2761` | `mcq` | true | `C` | `C. pheromones` |
| baseline | `mmlu_2762` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2763` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2764` | `mcq` | true | `C` | `C. 48` |
| baseline | `mmlu_2765` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2766` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2767` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2768` | `mcq` | true | `B` | `B. Endosymbiotic model` |
| baseline | `mmlu_2769` | `mcq` | false | `C` | `B. 5′-G-U-A-3′` |
| baseline | `mmlu_2770` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2771` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2772` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2773` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2774` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2775` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2776` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2777` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2778` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2779` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2780` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2781` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2782` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2783` | `mcq` | false | `B` | `C. Annelida` |
| baseline | `mmlu_2784` | `mcq` | true | `B` | `B. 18%` |
| baseline | `mmlu_2785` | `mcq` | true | `B` | `B. the strong cohesion of property of water` |
| baseline | `mmlu_2786` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2787` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2788` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2789` | `mcq` | true | `A` | `A. enzymes in the lysosomes` |
| baseline | `mmlu_2790` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2791` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2792` | `mcq` | false | `D` | `C. 50%` |
| baseline | `mmlu_2793` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2794` | `mcq` | true | `C` | `C. H+ ions flowing down a gradient across the mitochondrial inner membrane` |
| baseline | `mmlu_2795` | `mcq` | true | `A` | `A. Neutrophils` |
| baseline | `mmlu_2796` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2797` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2798` | `mcq` | true | `A` | `A. Inbreeding and loss of genetic variation threaten a population.` |
| baseline | `mmlu_2799` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2800` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2801` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2802` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2803` | `mcq` | true | `B` | `B. H+ would increase inside the intermembrane space (the compartment between inner and outer membranes).` |
| baseline | `mmlu_2804` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2805` | `mcq` | true | `D` | `D. Cell wall` |
| baseline | `mmlu_2806` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2808` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2809` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2810` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2811` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2812` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2813` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2814` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2815` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2816` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2817` | `mcq` | true | `B` | `B. Breast milk contains maternal antibodies that protect against gastrointestinal pathogens.` |
| baseline | `mmlu_2818` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2819` | `mcq` | true | `B` | `B. The flu virus, which changes its envelope proteins` |
| baseline | `mmlu_2820` | `mcq` | true | `A` | `A. 1/2` |
| baseline | `mmlu_2821` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2822` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2823` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2824` | `mcq` | true | `B` | `B. light, CO2, water` |
| baseline | `mmlu_2825` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2827` | `mcq` | true | `D` | `D. Promoter` |
| baseline | `mmlu_2828` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2829` | `mcq` | true | `D` | `D. habituation.` |
| baseline | `mmlu_2830` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2831` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2832` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2833` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2834` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_2835` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2836` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2837` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2838` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2839` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2840` | `mcq` | true | `A` | `A. H2O diffuses out of the leaf faster than CO2 enters.` |
| baseline | `mmlu_2841` | `mcq` | false | `A` | `C. Translocation events that change gene sequences` |
| baseline | `mmlu_2842` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2843` | `mcq` | false | `D` | `A. Lake B is alkaline.` |
| baseline | `mmlu_2844` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2845` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2846` | `mcq` | true | `A` | `A. thigmotropism` |
| baseline | `mmlu_2847` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2848` | `mcq` | true | `A` | `A. the alignment and separation of chromosomes during mitosis` |
| baseline | `mmlu_2849` | `mcq` | true | `C` | `C. water` |
| baseline | `mmlu_2850` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2851` | `mcq` | true | `C` | `C. A summer influx of nutrients derived from chemical fertilizers that are high in nitrogen and phosphorus` |
| baseline | `mmlu_2852` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2853` | `mcq` | true | `D` | `D. Both A and C` |
| baseline | `mmlu_2854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2855` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2856` | `mcq` | true | `A` | `A. Enhancer` |
| baseline | `mmlu_2857` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2858` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2859` | `mcq` | true | `C` | `C. longer loops of Henle` |
| baseline | `mmlu_2860` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2861` | `mcq` | false | `B` | `A. plasmolyze` |
| baseline | `mmlu_2862` | `mcq` | true | `D` | `D. I and III` |
| baseline | `mmlu_2863` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2864` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2865` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2866` | `mcq` | true | `A` | `A. The surface water cools.` |
| baseline | `mmlu_2867` | `mcq` | true | `A` | `A. Viruses` |
| baseline | `mmlu_2868` | `mcq` | true | `A` | `A. increasing the surface area of the small intestine` |
| baseline | `mmlu_2869` | `mcq` | true | `B` | `B. conjugation.` |
| baseline | `mmlu_2870` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2871` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2872` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2873` | `mcq` | true | `B` | `B. Genetic drift` |
| baseline | `mmlu_2874` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2875` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2876` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2877` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2878` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2879` | `mcq` | true | `B` | `B. Differences in the timing and expression levels of different genes leads to structural and functional differences.` |
| baseline | `mmlu_2880` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2881` | `mcq` | true | `C` | `C. The frequency of the allele will remain at 0.3 because the population is at Hardy-Weinberg equilibrium.` |
| baseline | `mmlu_2882` | `mcq` | true | `B` | `B. These plants have a mutualistic relationship with nitrogen-fixing bacteria.` |
| baseline | `mmlu_2883` | `mcq` | true | `B` | `B. Minimizing artificial lighting in the area` |
| baseline | `mmlu_2884` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2885` | `mcq` | true | `C` | `C. Turner syndrome` |
| baseline | `mmlu_2886` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2887` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2888` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2889` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2890` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2891` | `mcq` | false | `D` | `A. amnion` |
| baseline | `mmlu_2892` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2893` | `mcq` | true | `C` | `C. inserting it into a suitable bacterium in order to produce multiple copies` |
| baseline | `mmlu_2894` | `mcq` | true | `A` | `A. Robert MacArthur and E. O. Wilson` |
| baseline | `mmlu_2895` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2896` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2897` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2898` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2899` | `mcq` | true | `B` | `B. Repressor` |
| baseline | `mmlu_2900` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_2901` | `mcq` | true | `D` | `D. An individual's phenotype` |
| baseline | `mmlu_2902` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_2903` | `mcq` | false | `B` | `C. adding more enzyme K` |
| baseline | `mmlu_2904` | `mcq` | true | `D` | `D. Hot and dry` |
| baseline | `mmlu_2905` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2906` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2907` | `mcq` | true | `C` | `C. Cerebrum` |
| baseline | `mmlu_2908` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2909` | `mcq` | true | `C` | `C. By increasing genetic variation of the bacteria` |
| baseline | `mmlu_2910` | `mcq` | true | `D` | `D. A and B` |
| baseline | `mmlu_2911` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_2912` | `mcq` | true | `B` | `B. 32 percent` |
| baseline | `mmlu_2913` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2914` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2915` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2916` | `mcq` | true | `A` | `A. Random mating` |
| baseline | `mmlu_2917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2918` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_2919` | `mcq` | true | `C` | `C. stabilizing selection` |
| baseline | `mmlu_2920` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2921` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2922` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_2923` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2924` | `mcq` | true | `D` | `D. The streamlined body has a selective advantage in that environment.` |
| baseline | `mmlu_2925` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2926` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2927` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_2928` | `mcq` | true | `D` | `D. Wearing goggles and nitrile-type gloves and keeping all acetone containers closed` |
| baseline | `mmlu_2929` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2930` | `mcq` | true | `A` | `A. 0%` |
| baseline | `mmlu_2931` | `mcq` | true | `A` | `A. Peroxisomes, mitochondria, and ribosomes` |
| baseline | `mmlu_2932` | `mcq` | true | `C` | `C. endergonic reaction.` |
| baseline | `mmlu_2933` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2934` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2935` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2936` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_2937` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2938` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2939` | `mcq` | true | `A` | `A. Lignin provides structural support, allowing plants to grow tall.` |
| baseline | `mmlu_2940` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2941` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2942` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2943` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2944` | `mcq` | true | `A` | `A. H2O` |
| baseline | `mmlu_2945` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_2946` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_2947` | `mcq` | true | `A` | `A. Prophase I` |
| baseline | `mmlu_2948` | `mcq` | true | `D` | `D. frameshift mutation` |
| baseline | `mmlu_2949` | `mcq` | true | `C` | `C. Hypothalamus` |
| baseline | `mmlu_2950` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2951` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_2952` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2953` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2954` | `mcq` | true | `D` | `D. Fungus` |
| baseline | `mmlu_2955` | `mcq` | true | `B` | `B. Secondary succession would begin to occur.` |
| baseline | `mmlu_2956` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2957` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_2958` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2959` | `mcq` | true | `D` | `D. plasmolysis.` |
| baseline | `mmlu_2960` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2961` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2962` | `mcq` | true | `D` | `D. Gastrulation` |
| baseline | `mmlu_2963` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2964` | `mcq` | false | `D` | `A. a higher mean weight compared with their parents` |
| baseline | `mmlu_2965` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2966` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_2967` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2968` | `mcq` | true | `D` | `D. Natural selection` |
| baseline | `mmlu_2969` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_2970` | `mcq` | true | `D` | `D. Coevolution` |
| baseline | `mmlu_2971` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_2972` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2973` | `mcq` | true | `B` | `B. Pyrimidine : Purine` |
| baseline | `mmlu_2974` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2975` | `mcq` | true | `B` | `B. proximal convoluted tubule` |
| baseline | `mmlu_2976` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_2977` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2978` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_2979` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2980` | `mcq` | true | `A` | `A. 70 pm, 1402 kJ/mol` |
| baseline | `mmlu_2981` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_2982` | `mcq` | true | `A` | `A. Ag+(aq) + Br-(aq) → AgBr(s)` |
| baseline | `mmlu_2983` | `mcq` | true | `B` | `B. Sb` |
| baseline | `mmlu_2984` | `mcq` | false | `C` | `A. 0.33 atm` |
| baseline | `mmlu_2985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_2986` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_2987` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_2988` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_2989` | `mcq` | false | `C` | `A. 0.0641 M` |
| baseline | `mmlu_2990` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_2991` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_2992` | `mcq` | true | `A` | `A. 3.8 × 10^-3 mol/L` |
| baseline | `mmlu_2993` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_2994` | `mcq` | true | `C` | `C. a weak base` |
| baseline | `mmlu_2995` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_2996` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_2997` | `mcq` | true | `B` | `B. an intermediate` |
| baseline | `mmlu_2998` | `mcq` | false | `D` | `C. 29` |
| baseline | `mmlu_2999` | `mcq` | false | `B` | `C. this reaction goes to completion` |
| baseline | `mmlu_3000` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3001` | `mcq` | false | `B` | `D. KOH + HClO4` |
| baseline | `mmlu_3002` | `mcq` | false | `B` | `C. CrCl3` |
| baseline | `mmlu_3003` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3004` | `mcq` | true | `B` | `B. bromine` |
| baseline | `mmlu_3005` | `mcq` | true | `D` | `D. CBr4` |
| baseline | `mmlu_3006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3007` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3008` | `mcq` | false | `C` | `A. Measure the ΔS and the ΔG for the reaction, and calculate the ΔH from the Gibbs free energy equation.` |
| baseline | `mmlu_3009` | `mcq` | false | `A` | `C. The point at which the attractive and repulsive forces between the two atoms are equal` |
| baseline | `mmlu_3010` | `mcq` | true | `D` | `D. 7` |
| baseline | `mmlu_3011` | `mcq` | false | `D` | `C. The mass of the displaced water` |
| baseline | `mmlu_3012` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3013` | `mcq` | false | `B` | `A. C2H4O` |
| baseline | `mmlu_3014` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3015` | `mcq` | false | `B` | `D. SF6` |
| baseline | `mmlu_3016` | `mcq` | false | `C` | `A. 30.0 mL` |
| baseline | `mmlu_3017` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3018` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3019` | `mcq` | false | `D` | `B. Chlorine, iodine` |
| baseline | `mmlu_3020` | `mcq` | true | `D` | `D. (A), (B), and (C)` |
| baseline | `mmlu_3021` | `mcq` | false | `C` | `A. H2O and CH3OH` |
| baseline | `mmlu_3022` | `mcq` | true | `C` | `C. the emission spectrum of the elements, particularly hydrogen` |
| baseline | `mmlu_3023` | `mcq` | false | `D` | `C. 2,4-dichlorobenzene` |
| baseline | `mmlu_3024` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3025` | `mcq` | true | `D` | `D. 3 sigma and 1 pi` |
| baseline | `mmlu_3026` | `mcq` | false | `D` | `B. HCN` |
| baseline | `mmlu_3027` | `mcq` | true | `C` | `C. RCOOH` |
| baseline | `mmlu_3028` | `mcq` | true | `A` | `A. 1.00 grams` |
| baseline | `mmlu_3029` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3030` | `mcq` | true | `A` | `A. 8.8 × 10^-11 M` |
| baseline | `mmlu_3031` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3032` | `mcq` | false | `D` | `C. CO32- and NO3-` |
| baseline | `mmlu_3033` | `mcq` | false | `C` | `A. The 1s peak has the lowest energy.` |
| baseline | `mmlu_3034` | `mcq` | false | `B` | `A. magnesium at the anode and bromine at the cathode` |
| baseline | `mmlu_3035` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_3036` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3037` | `mcq` | false | `D` | `A. 6 electrons on the left` |
| baseline | `mmlu_3038` | `mcq` | false | `D` | `B. 8.52` |
| baseline | `mmlu_3039` | `mcq` | false | `A` | `C. 21 neutrons, 19 protons, 19 electrons` |
| baseline | `mmlu_3040` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3041` | `mcq` | true | `A` | `A. 2.0 × 10^-3` |
| baseline | `mmlu_3042` | `mcq` | true | `D` | `D. 251 torr` |
| baseline | `mmlu_3043` | `mcq` | true | `D` | `D. HBrO4` |
| baseline | `mmlu_3044` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3045` | `mcq` | true | `B` | `B. HC2H3O2 and KC2H3O2` |
| baseline | `mmlu_3046` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3047` | `mcq` | true | `D` | `D. When the reaction exhibits no change in pressure at constant volume` |
| baseline | `mmlu_3048` | `mcq` | true | `D` | `D. Mg(s)` |
| baseline | `mmlu_3049` | `mcq` | true | `B` | `B. Increasing the pressure` |
| baseline | `mmlu_3050` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3051` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3052` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3053` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3054` | `mcq` | true | `B` | `B. 527°C` |
| baseline | `mmlu_3055` | `mcq` | true | `B` | `B. free radicals` |
| baseline | `mmlu_3056` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3057` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3058` | `mcq` | false | `C` | `A. HPO42-` |
| baseline | `mmlu_3059` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3060` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3061` | `mcq` | false | `C` | `A. Add 167 mL of the stock solution to the flask, then fill the flask the rest of the way with distilled water while swi` |
| baseline | `mmlu_3062` | `mcq` | true | `B` | `B. An alkane` |
| baseline | `mmlu_3063` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3064` | `mcq` | true | `A` | `A. CO2` |
| baseline | `mmlu_3065` | `mcq` | true | `A` | `A. 1` |
| baseline | `mmlu_3066` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3067` | `mcq` | true | `C` | `C. Decreasing [Fe2+]` |
| baseline | `mmlu_3068` | `mcq` | true | `C` | `C. The endpoint would be before the ideal equivalence point.` |
| baseline | `mmlu_3069` | `mcq` | false | `C` | `D. 2,3-bromochloropentane` |
| baseline | `mmlu_3070` | `mcq` | false | `B` | `A. High temperature and high pressure` |
| baseline | `mmlu_3071` | `mcq` | false | `D` | `C. 24 electrons, 28 protons, 24 neutrons` |
| baseline | `mmlu_3072` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3073` | `mcq` | false | `D` | `A. 2.88 × 10^-6 torr` |
| baseline | `mmlu_3074` | `mcq` | true | `D` | `D. More information is needed to answer this question.` |
| baseline | `mmlu_3075` | `mcq` | false | `D` | `A. q = 0` |
| baseline | `mmlu_3076` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3077` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3078` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3079` | `mcq` | false | `B` | `A. 0.100 mol` |
| baseline | `mmlu_3080` | `mcq` | true | `D` | `D. Sulfur` |
| baseline | `mmlu_3081` | `mcq` | false | `B` | `C. ethanoic acid` |
| baseline | `mmlu_3082` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3083` | `mcq` | false | `C` | `D. Sulfur` |
| baseline | `mmlu_3084` | `mcq` | false | `A` | `B. -9.62 L atm` |
| baseline | `mmlu_3085` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3086` | `mcq` | true | `D` | `D. all of the above are true` |
| baseline | `mmlu_3087` | `mcq` | true | `B` | `B. a covalent or network crystal` |
| baseline | `mmlu_3088` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3089` | `mcq` | false | `B` | `A. 0.496 molar` |
| baseline | `mmlu_3090` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3091` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3092` | `mcq` | true | `C` | `C. The temperature` |
| baseline | `mmlu_3093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3094` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3095` | `mcq` | true | `D` | `D. N2H4(aq)` |
| baseline | `mmlu_3096` | `mcq` | false | `D` | `A. Decreasing the temperature` |
| baseline | `mmlu_3097` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3098` | `mcq` | true | `C` | `C. 0.311` |
| baseline | `mmlu_3099` | `mcq` | false | `C` | `A. proton` |
| baseline | `mmlu_3100` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3101` | `mcq` | false | `D` | `C. Octahedron` |
| baseline | `mmlu_3102` | `mcq` | false | `B` | `C. AlBr3` |
| baseline | `mmlu_3103` | `mcq` | false | `A` | `C. Vapor pressures` |
| baseline | `mmlu_3104` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3105` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3106` | `mcq` | false | `C` | `B. First order` |
| baseline | `mmlu_3107` | `mcq` | false | `B` | `D. it depends on the particular reaction` |
| baseline | `mmlu_3108` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3109` | `mcq` | true | `D` | `D. Triple-distilled water` |
| baseline | `mmlu_3110` | `mcq` | true | `D` | `D. HClO3` |
| baseline | `mmlu_3111` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3112` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3113` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3114` | `mcq` | false | `B` | `D. Dipole-dipole < hydrogen bond < induced dipole` |
| baseline | `mmlu_3115` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3116` | `mcq` | true | `A` | `A. 6.41 × 10^-22 g` |
| baseline | `mmlu_3117` | `mcq` | false | `B` | `D. H2O` |
| baseline | `mmlu_3118` | `mcq` | true | `D` | `D. The existence of isotopes` |
| baseline | `mmlu_3119` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3120` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3121` | `mcq` | true | `B` | `B. [H2SO3] > [HSO3-] > [SO32-]` |
| baseline | `mmlu_3122` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3123` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3124` | `mcq` | false | `C` | `D. H2SO3 < H2SeO3 < HClO < HBrO` |
| baseline | `mmlu_3125` | `mcq` | false | `B` | `A. NO2(g)` |
| baseline | `mmlu_3126` | `mcq` | true | `C` | `C. 0 °C and 760 torr` |
| baseline | `mmlu_3127` | `mcq` | true | `C` | `C. The I2 electron clouds are much more polarizable than the Br2 electron clouds, resulting in much stronger London forc` |
| baseline | `mmlu_3128` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3129` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3130` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3131` | `mcq` | true | `D` | `D. It will increase as the gas molecules will be more dispersed in the larger flask.` |
| baseline | `mmlu_3132` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3133` | `mcq` | true | `A` | `A. 212 g mol-1` |
| baseline | `mmlu_3134` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3135` | `mcq` | false | `B` | `A. [HNO2] > [NO2-]` |
| baseline | `mmlu_3136` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3137` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3138` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3139` | `mcq` | true | `B` | `B. H3PO4 and H2PO4-` |
| baseline | `mmlu_3140` | `mcq` | false | `C` | `A. 1s` |
| baseline | `mmlu_3141` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3142` | `mcq` | true | `C` | `C. Am` |
| baseline | `mmlu_3143` | `mcq` | false | `B` | `A. CCl2F2` |
| baseline | `mmlu_3144` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3145` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3146` | `mcq` | true | `B` | `B. 4.60%` |
| baseline | `mmlu_3147` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3148` | `mcq` | true | `D` | `D. 1 × 10^-5 M` |
| baseline | `mmlu_3149` | `mcq` | false | `C` | `B. 0.00687 mol L-1` |
| baseline | `mmlu_3150` | `mcq` | true | `B` | `B. 8.52` |
| baseline | `mmlu_3151` | `mcq` | true | `C` | `C. The Cl2 electron clouds are much more polarizable than the F2 electron clouds, resulting in much stronger London forc` |
| baseline | `mmlu_3152` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3153` | `mcq` | true | `A` | `A. 53.0 g/mol` |
| baseline | `mmlu_3154` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3155` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3156` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3157` | `mcq` | false | `C` | `A. RbBr only` |
| baseline | `mmlu_3158` | `mcq` | true | `A` | `A. 186 pm, 496 kJ/mol` |
| baseline | `mmlu_3159` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3160` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3161` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3162` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3163` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3164` | `mcq` | true | `B` | `B. 9.26` |
| baseline | `mmlu_3165` | `mcq` | false | `C` | `D. 0.00625 g` |
| baseline | `mmlu_3166` | `mcq` | false | `D` | `A. 8.49 J mol-1 K-1` |
| baseline | `mmlu_3167` | `mcq` | false | `C` | `D. 49.3 g` |
| baseline | `mmlu_3168` | `mcq` | true | `B` | `B. the rate-determining or slow step of the mechanism` |
| baseline | `mmlu_3169` | `mcq` | true | `A` | `A. 3.4 × 10^-4 s-1` |
| baseline | `mmlu_3170` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3171` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3172` | `mcq` | false | `A` | `C. Mg(NO3)2(aq)` |
| baseline | `mmlu_3173` | `mcq` | false | `D` | `B. Increasing the temperature at which the reaction occurs` |
| baseline | `mmlu_3174` | `mcq` | false | `B` | `D. 7.1 mol` |
| baseline | `mmlu_3175` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3176` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3177` | `mcq` | false | `D` | `A. CH3COOH` |
| baseline | `mmlu_3178` | `mcq` | false | `B` | `A. HNO2` |
| baseline | `mmlu_3179` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3180` | `mcq` | false | `C` | `A. 3+, reduction` |
| baseline | `mmlu_3181` | `mcq` | false | `B` | `D. Rate = k[A]^-1` |
| baseline | `mmlu_3182` | `mcq` | true | `C` | `C. 8` |
| baseline | `mmlu_3183` | `mcq` | true | `A` | `A. int(x [,base])` |
| baseline | `mmlu_3184` | `mcq` | true | `A` | `A. The file is broken into packets for transmission. The packets must be reassembled upon receipt.` |
| baseline | `mmlu_3185` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3186` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3187` | `mcq` | false | `C` | `B. 225` |
| baseline | `mmlu_3188` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3189` | `mcq` | true | `B` | `B. Only elements that appear in both inputListl and inputList2` |
| baseline | `mmlu_3190` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3191` | `mcq` | true | `B` | `B. abcd` |
| baseline | `mmlu_3192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3193` | `mcq` | true | `C` | `C. Technology companies can set research and development goals based on anticipated processing speeds.` |
| baseline | `mmlu_3194` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3195` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3196` | `mcq` | true | `C` | `C. Lossless compression` |
| baseline | `mmlu_3197` | `mcq` | true | `A` | `A. isupper()` |
| baseline | `mmlu_3198` | `mcq` | true | `D` | `D. (num MOD 2) = 1` |
| baseline | `mmlu_3199` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3200` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3201` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3202` | `mcq` | false | `C` | `A. The method should be written on the assumption that there is only one value in the array that is larger than the give` |
| baseline | `mmlu_3203` | `mcq` | true | `B` | `B. aab` |
| baseline | `mmlu_3204` | `mcq` | true | `B` | `B. //` |
| baseline | `mmlu_3205` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3206` | `mcq` | false | `D` | `C. I and III only` |
| baseline | `mmlu_3207` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3208` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3209` | `mcq` | true | `D` | `D. num1 < num2 && num1 < num3` |
| baseline | `mmlu_3210` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3211` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3212` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3213` | `mcq` | false | `C` | `D. O(log n)` |
| baseline | `mmlu_3214` | `mcq` | false | `D` | `B. Interchanging line 5 and line 6` |
| baseline | `mmlu_3215` | `mcq` | false | `B` | `A. The ability to distribute information instantaneously` |
| baseline | `mmlu_3216` | `mcq` | true | `C` | `C. The program may have bugs.` |
| baseline | `mmlu_3217` | `mcq` | true | `B` | `B. 1` |
| baseline | `mmlu_3218` | `mcq` | false | `A` | `B. 1001 0111` |
| baseline | `mmlu_3219` | `mcq` | true | `A` | `A. **` |
| baseline | `mmlu_3220` | `mcq` | true | `C` | `C. E7_{16}` |
| baseline | `mmlu_3221` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3223` | `mcq` | true | `C` | `C. [786, 2.23]` |
| baseline | `mmlu_3224` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3225` | `mcq` | true | `A` | `A. 7` |
| baseline | `mmlu_3226` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3227` | `mcq` | true | `B` | `B. 4` |
| baseline | `mmlu_3228` | `mcq` | true | `C` | `C. 24` |
| baseline | `mmlu_3229` | `mcq` | true | `A` | `A. a[i] == max` |
| baseline | `mmlu_3230` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3231` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3232` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3233` | `mcq` | true | `C` | `C.	max(list)` |
| baseline | `mmlu_3234` | `mcq` | true | `A` | `A. O(1)` |
| baseline | `mmlu_3235` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3236` | `mcq` | true | `D` | `D. heads_counter = 2` |
| baseline | `mmlu_3237` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3238` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3239` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3240` | `mcq` | false | `C` | `A. Dictionary/map \| Queue \| Stack` |
| baseline | `mmlu_3241` | `mcq` | true | `A` | `A. 1` |
| baseline | `mmlu_3242` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_3243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3244` | `mcq` | false | `B` | `D. Hexadecimal D, Decimal 11, Binary 1100` |
| baseline | `mmlu_3245` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3246` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3247` | `mcq` | false | `D` | `A. Error` |
| baseline | `mmlu_3248` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3249` | `mcq` | false | `C` | `A. 9` |
| baseline | `mmlu_3250` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3251` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3252` | `mcq` | true | `B` | `B. 3y` |
| baseline | `mmlu_3253` | `mcq` | false | `B` | `A. top-down development` |
| baseline | `mmlu_3254` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3255` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3256` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3257` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3258` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3259` | `mcq` | true | `B` | `B. nextAvailableID` |
| baseline | `mmlu_3260` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3261` | `mcq` | true | `D` | `D. seed([x])` |
| baseline | `mmlu_3262` | `mcq` | true | `A` | `A. ['Hi!', 'Hi!', 'Hi!', 'Hi!']` |
| baseline | `mmlu_3263` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3264` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3265` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3266` | `mcq` | false | `C` | `A. The goal of the attack` |
| baseline | `mmlu_3267` | `mcq` | false | `A` | `B. The Internet Protocol (IP) address of the user's computer` |
| baseline | `mmlu_3268` | `mcq` | true | `B` | `B. An Internet Protocol (IP) address is assigned to the device.` |
| baseline | `mmlu_3269` | `mcq` | true | `A` | `A. a < c` |
| baseline | `mmlu_3270` | `mcq` | true | `C` | `C. {1,2,3,4}` |
| baseline | `mmlu_3271` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3272` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_3273` | `mcq` | false | `C` | `B. (int) (Math.random() * (high - low)) + low;` |
| baseline | `mmlu_3274` | `mcq` | false | `C` | `A. [19,21]` |
| baseline | `mmlu_3275` | `mcq` | true | `D` | `D. During run time` |
| baseline | `mmlu_3276` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3277` | `mcq` | false | `C` | `D. 3 2` |
| baseline | `mmlu_3278` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3279` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3280` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3281` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3282` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3283` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3284` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3285` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3286` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3287` | `mcq` | true | `C` | `C. the sense of continual class struggle` |
| baseline | `mmlu_3288` | `mcq` | true | `C` | `C. the monetary value of goods` |
| baseline | `mmlu_3289` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3290` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3291` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3292` | `mcq` | true | `D` | `D. Social Darwinism` |
| baseline | `mmlu_3293` | `mcq` | false | `C` | `B. Suppress all voices in government other than his own and control all aspects of his citizens' lives.` |
| baseline | `mmlu_3294` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3295` | `mcq` | false | `B` | `C. Industrialization` |
| baseline | `mmlu_3296` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3298` | `mcq` | true | `A` | `A. observation and induction` |
| baseline | `mmlu_3299` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3300` | `mcq` | false | `A` | `B. Financial gain` |
| baseline | `mmlu_3301` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3302` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3303` | `mcq` | true | `A` | `A. The Renaissance` |
| baseline | `mmlu_3304` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3305` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3306` | `mcq` | true | `D` | `D. Poland` |
| baseline | `mmlu_3307` | `mcq` | false | `B` | `C. It had been refined and changed by so many people that it had become unrecognizable to those such as Bacon who had pi` |
| baseline | `mmlu_3308` | `mcq` | true | `D` | `D. Curtailment of citizens' rights` |
| baseline | `mmlu_3309` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3310` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3311` | `mcq` | true | `C` | `C. Rationalism` |
| baseline | `mmlu_3312` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3313` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3314` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3315` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3316` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3317` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3318` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3319` | `mcq` | true | `B` | `B. Financial gain` |
| baseline | `mmlu_3320` | `mcq` | false | `B` | `D. Napoleon's military tactics` |
| baseline | `mmlu_3321` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3322` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3323` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3324` | `mcq` | true | `C` | `C. Adam Smith` |
| baseline | `mmlu_3325` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3326` | `mcq` | true | `D` | `D. it advocated total war` |
| baseline | `mmlu_3327` | `mcq` | false | `D` | `B. Liberals` |
| baseline | `mmlu_3328` | `mcq` | true | `C` | `C. Humanism` |
| baseline | `mmlu_3329` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3330` | `mcq` | true | `C` | `C. Liberalism` |
| baseline | `mmlu_3331` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3332` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3333` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3334` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3335` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3336` | `mcq` | true | `B` | `B. materialism` |
| baseline | `mmlu_3337` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3338` | `mcq` | true | `D` | `D. mass conscription` |
| baseline | `mmlu_3339` | `mcq` | false | `A` | `C. Pietism` |
| baseline | `mmlu_3340` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3341` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3342` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3343` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3344` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3345` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3346` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3347` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3348` | `mcq` | true | `C` | `C. ascertaining the state of the New Philosophy in England and abroad` |
| baseline | `mmlu_3349` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3350` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3351` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3352` | `mcq` | true | `D` | `D. the Earth is not stationary` |
| baseline | `mmlu_3353` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3354` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3355` | `mcq` | false | `C` | `B. Cardinal Mazarin, his regent and foreign policy advisor` |
| baseline | `mmlu_3356` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3357` | `mcq` | true | `B` | `B. Materialism and economic determinism` |
| baseline | `mmlu_3358` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3359` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3360` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3361` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3362` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3363` | `mcq` | false | `B` | `A. Governments did little to address problems of industrialization before 1850.` |
| baseline | `mmlu_3364` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3365` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3366` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_3367` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3368` | `mcq` | true | `C` | `C. Increased disillusionment and cynicism` |
| baseline | `mmlu_3369` | `mcq` | true | `C` | `C. It used information obtained through experimentation to conceptualize the universe.` |
| baseline | `mmlu_3370` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3371` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3372` | `mcq` | true | `C` | `C. The Berlin blockade` |
| baseline | `mmlu_3373` | `mcq` | true | `A` | `A. The social effects of industrialization` |
| baseline | `mmlu_3374` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3376` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3377` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3378` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3379` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3380` | `mcq` | true | `A` | `A. The consolidation of the power of the monarchy` |
| baseline | `mmlu_3381` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3382` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3383` | `mcq` | true | `D` | `D. Anabaptists` |
| baseline | `mmlu_3384` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3385` | `mcq` | true | `C` | `C. constitutionalism` |
| baseline | `mmlu_3386` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3387` | `mcq` | true | `C` | `C. general rejection of Catholic dogma` |
| baseline | `mmlu_3388` | `mcq` | true | `B` | `B. People could begin to question the Church on a wider scale.` |
| baseline | `mmlu_3389` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3390` | `mcq` | true | `B` | `B. the consent of those members of society` |
| baseline | `mmlu_3391` | `mcq` | true | `D` | `D. Darwin` |
| baseline | `mmlu_3392` | `mcq` | true | `B` | `B. They were subjugated and destroyed.` |
| baseline | `mmlu_3393` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3394` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3395` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3396` | `mcq` | false | `B` | `C. Increased popular participation in politics` |
| baseline | `mmlu_3397` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3398` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3399` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3401` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3402` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3403` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3404` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3405` | `mcq` | false | `B` | `D. Challenges to the monopoly on truth held by the Roman Catholic Church on multiple fronts` |
| baseline | `mmlu_3406` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3407` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3408` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3409` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3410` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3411` | `mcq` | true | `B` | `B. Predestination` |
| baseline | `mmlu_3412` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3413` | `mcq` | true | `D` | `D. it tries to exercise absolute power` |
| baseline | `mmlu_3414` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3415` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3416` | `mcq` | true | `B` | `B. They utilized new methods of communicating their ideas, such as salons and inexpensive printed pamphlets.` |
| baseline | `mmlu_3417` | `mcq` | true | `D` | `D. Neoplatonism` |
| baseline | `mmlu_3418` | `mcq` | true | `D` | `D. using cause-and-effect to systematize the understanding of human behavior` |
| baseline | `mmlu_3419` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3420` | `mcq` | true | `B` | `B. France` |
| baseline | `mmlu_3421` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3422` | `mcq` | false | `A` | `B. Article II` |
| baseline | `mmlu_3423` | `mcq` | true | `C` | `C. Economic opportunities were created.` |
| baseline | `mmlu_3424` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3425` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3426` | `mcq` | true | `B` | `B. Religious` |
| baseline | `mmlu_3427` | `mcq` | true | `B` | `B. successfully harnessed the human resources of the new French Republic` |
| baseline | `mmlu_3428` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3429` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3430` | `mcq` | true | `C` | `C. empiricism` |
| baseline | `mmlu_3431` | `mcq` | true | `C` | `C. Mexico` |
| baseline | `mmlu_3432` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3434` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3435` | `mcq` | true | `D` | `D. Nationalism` |
| baseline | `mmlu_3436` | `mcq` | true | `C` | `C. An increased rate of inflation` |
| baseline | `mmlu_3437` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3438` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3439` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3440` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3441` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3442` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3443` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3444` | `mcq` | true | `C` | `C. scientific principles were applied to other cultures as a result of the sudden expansion of European dominance across` |
| baseline | `mmlu_3445` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3446` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3447` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3448` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3449` | `mcq` | true | `C` | `C. distance decay.` |
| baseline | `mmlu_3450` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_3451` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3452` | `mcq` | true | `D` | `D. overcrowding.` |
| baseline | `mmlu_3453` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3454` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3455` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3456` | `mcq` | true | `D` | `D. Access to trade routes` |
| baseline | `mmlu_3457` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3458` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3459` | `mcq` | false | `A` | `B. Christianity` |
| baseline | `mmlu_3460` | `mcq` | true | `D` | `D. hinterland.` |
| baseline | `mmlu_3461` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3462` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3463` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3464` | `mcq` | false | `D` | `A. Highways to airports that link cities` |
| baseline | `mmlu_3465` | `mcq` | true | `B` | `B. Suburbs` |
| baseline | `mmlu_3466` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3467` | `mcq` | true | `C` | `C. supranationalism.` |
| baseline | `mmlu_3468` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3469` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3470` | `mcq` | true | `D` | `D. Sector model` |
| baseline | `mmlu_3471` | `mcq` | true | `B` | `B. theocracy.` |
| baseline | `mmlu_3472` | `mcq` | true | `A` | `A. Christianity` |
| baseline | `mmlu_3473` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3474` | `mcq` | false | `B` | `A. future social spending needs of the population.` |
| baseline | `mmlu_3475` | `mcq` | true | `C` | `C. Natural` |
| baseline | `mmlu_3476` | `mcq` | true | `A` | `A. Primary` |
| baseline | `mmlu_3477` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3478` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3479` | `mcq` | true | `C` | `C. based on comparative advantage.` |
| baseline | `mmlu_3480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3481` | `mcq` | false | `B` | `C. France` |
| baseline | `mmlu_3482` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3483` | `mcq` | true | `C` | `C. Cambodia.` |
| baseline | `mmlu_3484` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3485` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3486` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3487` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3488` | `mcq` | true | `B` | `B. acculturation.` |
| baseline | `mmlu_3489` | `mcq` | true | `B` | `B. A globe` |
| baseline | `mmlu_3490` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3491` | `mcq` | true | `D` | `D. Burgess` |
| baseline | `mmlu_3492` | `mcq` | false | `D` | `C. road map.` |
| baseline | `mmlu_3493` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3494` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3495` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3496` | `mcq` | true | `B` | `B. The Amazon Basin` |
| baseline | `mmlu_3497` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3498` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3499` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3500` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3501` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3502` | `mcq` | false | `C` | `A. First` |
| baseline | `mmlu_3503` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3505` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3506` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3507` | `mcq` | false | `D` | `B. Distance decay` |
| baseline | `mmlu_3508` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3509` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3510` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3511` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3512` | `mcq` | true | `C` | `C. agglomeration.` |
| baseline | `mmlu_3513` | `mcq` | true | `D` | `D. Romance` |
| baseline | `mmlu_3514` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3515` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3516` | `mcq` | true | `C` | `C. heartland theory.` |
| baseline | `mmlu_3517` | `mcq` | true | `B` | `B. Shiite` |
| baseline | `mmlu_3518` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3519` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3521` | `mcq` | true | `C` | `C. Japan` |
| baseline | `mmlu_3522` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3523` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3524` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3525` | `mcq` | false | `A` | `D. push-pull factors.` |
| baseline | `mmlu_3526` | `mcq` | true | `D` | `D. edge city.` |
| baseline | `mmlu_3527` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3528` | `mcq` | true | `B` | `B. The end of the Cold War` |
| baseline | `mmlu_3529` | `mcq` | true | `B` | `B. Air` |
| baseline | `mmlu_3530` | `mcq` | true | `C` | `C. The market area of Winn-Dixie` |
| baseline | `mmlu_3531` | `mcq` | false | `D` | `A. European` |
| baseline | `mmlu_3532` | `mcq` | true | `C` | `C. Indo-European` |
| baseline | `mmlu_3533` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3534` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3535` | `mcq` | true | `C` | `C. Mining copper` |
| baseline | `mmlu_3536` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3537` | `mcq` | true | `C` | `C. Egypt` |
| baseline | `mmlu_3538` | `mcq` | true | `D` | `D. Coal` |
| baseline | `mmlu_3539` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3540` | `mcq` | true | `C` | `C. Information` |
| baseline | `mmlu_3541` | `mcq` | true | `D` | `D. primite city.` |
| baseline | `mmlu_3542` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3543` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3544` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3545` | `mcq` | true | `B` | `B. Origin point` |
| baseline | `mmlu_3546` | `mcq` | true | `C` | `C. latitude.` |
| baseline | `mmlu_3547` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3548` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3549` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3550` | `mcq` | true | `D` | `D. Health care` |
| baseline | `mmlu_3551` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3552` | `mcq` | true | `D` | `D. Latin America` |
| baseline | `mmlu_3553` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3554` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3555` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3556` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3557` | `mcq` | true | `C` | `C. pastorialism.` |
| baseline | `mmlu_3558` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3559` | `mcq` | true | `D` | `D. Green Revolution.` |
| baseline | `mmlu_3560` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3561` | `mcq` | true | `B` | `B. Asia and Latin America` |
| baseline | `mmlu_3562` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3563` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3564` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3565` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3566` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3567` | `mcq` | true | `D` | `D. Mandarin Chinese.` |
| baseline | `mmlu_3568` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3569` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3570` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3571` | `mcq` | true | `B` | `B. Better job and higher wages` |
| baseline | `mmlu_3572` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3573` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3574` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3575` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3576` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3577` | `mcq` | true | `C` | `C. Chile` |
| baseline | `mmlu_3578` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3579` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3580` | `mcq` | false | `B` | `D. The national anthem` |
| baseline | `mmlu_3581` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3582` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3583` | `mcq` | true | `D` | `D. Distance to the nearest city` |
| baseline | `mmlu_3584` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3585` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3586` | `mcq` | true | `D` | `D. 479 Elm Street, Muncie, Indiana` |
| baseline | `mmlu_3587` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3588` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3589` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3590` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3591` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3592` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3593` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3594` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3595` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3596` | `mcq` | true | `A` | `A./core, periphery, and semi-periphery.` |
| baseline | `mmlu_3597` | `mcq` | false | `C` | `B. Iraq` |
| baseline | `mmlu_3598` | `mcq` | true | `D` | `D. Spain` |
| baseline | `mmlu_3599` | `mcq` | true | `C` | `C. Sub-Saharan Africa` |
| baseline | `mmlu_3600` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3601` | `mcq` | true | `B` | `B. the movement of power from the central government to regional governments in the country.` |
| baseline | `mmlu_3602` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3603` | `mcq` | true | `B` | `B. central place theory.` |
| baseline | `mmlu_3604` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3605` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3606` | `mcq` | true | `D` | `D. Containment theory` |
| baseline | `mmlu_3607` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3608` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3609` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3610` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3611` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3612` | `mcq` | false | `C` | `D. Territoriality` |
| baseline | `mmlu_3613` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3614` | `mcq` | false | `B` | `C. Pesticides` |
| baseline | `mmlu_3615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3616` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3617` | `mcq` | true | `D` | `D. dialects.` |
| baseline | `mmlu_3618` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3619` | `mcq` | true | `A` | `A. Canada` |
| baseline | `mmlu_3620` | `mcq` | false | `C` | `B. Secession` |
| baseline | `mmlu_3621` | `mcq` | true | `A` | `A. Internet` |
| baseline | `mmlu_3622` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3623` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3624` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3625` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3626` | `mcq` | true | `C` | `C. China` |
| baseline | `mmlu_3627` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3628` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3629` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3630` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3631` | `mcq` | true | `A` | `A. Africa` |
| baseline | `mmlu_3632` | `mcq` | true | `B` | `B. Christianity` |
| baseline | `mmlu_3633` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3634` | `mcq` | true | `A` | `A. Food production` |
| baseline | `mmlu_3635` | `mcq` | true | `B` | `B. Transport` |
| baseline | `mmlu_3636` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3637` | `mcq` | true | `D` | `D. NATO` |
| baseline | `mmlu_3638` | `mcq` | true | `B` | `B. English.` |
| baseline | `mmlu_3639` | `mcq` | true | `C` | `C. Sunni and Shiite` |
| baseline | `mmlu_3640` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3641` | `mcq` | true | `D` | `D. the United States.` |
| baseline | `mmlu_3642` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3643` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3644` | `mcq` | true | `B` | `B. South America` |
| baseline | `mmlu_3645` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3646` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3647` | `mcq` | true | `B` | `B. The child's family` |
| baseline | `mmlu_3648` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3649` | `mcq` | true | `A` | `A. contribute money to candidates for election` |
| baseline | `mmlu_3650` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3651` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3652` | `mcq` | false | `D` | `A. The amount of coverage the issue receives in the major news media` |
| baseline | `mmlu_3653` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3654` | `mcq` | true | `C` | `C. Judicial review` |
| baseline | `mmlu_3655` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3656` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3658` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3659` | `mcq` | true | `D` | `D. stare decisis` |
| baseline | `mmlu_3660` | `mcq` | true | `D` | `D. Voters aged 18-29` |
| baseline | `mmlu_3661` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3662` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3663` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3664` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3665` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3666` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3667` | `mcq` | true | `D` | `D. Brown v. Board of Education of Topeka` |
| baseline | `mmlu_3668` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3669` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3670` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3671` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3672` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3673` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3674` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3675` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3676` | `mcq` | true | `B` | `B. making it difficult for one faction to gain the power necessary to govern` |
| baseline | `mmlu_3677` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3678` | `mcq` | true | `A` | `A. reflect population shifts indicated by the national census` |
| baseline | `mmlu_3679` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3680` | `mcq` | true | `D` | `D. The two legislative bodies form a conference committee.` |
| baseline | `mmlu_3681` | `mcq` | false | `C` | `B. I and IV only` |
| baseline | `mmlu_3682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3683` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3684` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3685` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3686` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3687` | `mcq` | true | `B` | `B. Checks and balances` |
| baseline | `mmlu_3688` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3689` | `mcq` | false | `B` | `D. Voters increasingly vote based on a party's platform.` |
| baseline | `mmlu_3690` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3691` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3692` | `mcq` | false | `C` | `B. Labor unions` |
| baseline | `mmlu_3693` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3694` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3695` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3696` | `mcq` | true | `D` | `D. End a filibuster and force a vote on a bill in the Senate` |
| baseline | `mmlu_3697` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3698` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3699` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3700` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3701` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3702` | `mcq` | false | `C` | `A. cooperation between the two major political parties` |
| baseline | `mmlu_3703` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3704` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3705` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3706` | `mcq` | true | `B` | `B. The voter's political party affiliation` |
| baseline | `mmlu_3707` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3708` | `mcq` | true | `B` | `B. provide the audience with a candidate's view in a limited amount of time` |
| baseline | `mmlu_3709` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3710` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3712` | `mcq` | true | `B` | `B. To make it easier for citizens to register to vote` |
| baseline | `mmlu_3713` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3714` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3715` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3716` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3717` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3718` | `mcq` | false | `C` | `B. Congress` |
| baseline | `mmlu_3719` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3720` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3721` | `mcq` | true | `D` | `D. Griswold v. Connecticut and Roe v. Wade.` |
| baseline | `mmlu_3722` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3723` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3724` | `mcq` | true | `A` | `A. judicial activism` |
| baseline | `mmlu_3725` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3726` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3728` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3729` | `mcq` | true | `C` | `C. The Bill of Rights implies a right to privacy.` |
| baseline | `mmlu_3730` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3731` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3732` | `mcq` | true | `D` | `D. free speech` |
| baseline | `mmlu_3733` | `mcq` | false | `C` | `A. regulation of interstate commerce` |
| baseline | `mmlu_3734` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3735` | `mcq` | false | `B` | `A. avoid battleground states and focus their campaigns on "safe" states` |
| baseline | `mmlu_3736` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3737` | `mcq` | true | `C` | `C. Southerners` |
| baseline | `mmlu_3738` | `mcq` | true | `D` | `D.	gerrymandering` |
| baseline | `mmlu_3739` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3740` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3741` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3742` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3743` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3744` | `mcq` | true | `C` | `C. reduce the federal deficit` |
| baseline | `mmlu_3745` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3746` | `mcq` | true | `D` | `D. Development of a two-party system` |
| baseline | `mmlu_3747` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3748` | `mcq` | true | `A` | `A. determines both the rules of the House and conditions for legislative process` |
| baseline | `mmlu_3749` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3750` | `mcq` | true | `C` | `C. I and III only` |
| baseline | `mmlu_3751` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3752` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3753` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3754` | `mcq` | false | `D` | `A. The candidate who wins the popular national vote` |
| baseline | `mmlu_3755` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3756` | `mcq` | true | `A` | `A. redrawing congressional district boundaries` |
| baseline | `mmlu_3757` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3758` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3759` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3760` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3761` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3762` | `mcq` | true | `B` | `B. due process clause` |
| baseline | `mmlu_3763` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3764` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3765` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3766` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3767` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3769` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3770` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3771` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3772` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3773` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3774` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3775` | `mcq` | true | `A` | `A. will review a lower court decision` |
| baseline | `mmlu_3776` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3777` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3778` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3779` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3780` | `mcq` | true | `B` | `B. issues a writ of certiorari` |
| baseline | `mmlu_3781` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_3782` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_3783` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3784` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3785` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3786` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3787` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3788` | `mcq` | true | `A` | `A. Plessy v. Ferguson` |
| baseline | `mmlu_3789` | `mcq` | true | `C` | `C. Federal budget entitlements` |
| baseline | `mmlu_3790` | `mcq` | false | `B` | `D. Cabinet` |
| baseline | `mmlu_3791` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3792` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3793` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3794` | `mcq` | true | `D` | `D. The use of racial quotas in public university admissions` |
| baseline | `mmlu_3795` | `mcq` | true | `C` | `C. Increasing concentration of ownership in the news media` |
| baseline | `mmlu_3796` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3797` | `mcq` | true | `D` | `D. president` |
| baseline | `mmlu_3798` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3799` | `mcq` | true | `D` | `D. Fourteenth Amendment` |
| baseline | `mmlu_3800` | `mcq` | true | `B` | `B. delegating the responsibility for electing senators to the state legislatures` |
| baseline | `mmlu_3801` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3802` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3803` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3804` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_3805` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3806` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3807` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3808` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3809` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3810` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3811` | `mcq` | false | `B` | `A. peer pressure` |
| baseline | `mmlu_3812` | `mcq` | true | `A` | `A. First Amendment` |
| baseline | `mmlu_3813` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3814` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3815` | `mcq` | false | `D` | `B. I and III only` |
| baseline | `mmlu_3816` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3817` | `mcq` | true | `B` | `B. Ways and Means` |
| baseline | `mmlu_3818` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3819` | `mcq` | true | `D` | `D. Rules` |
| baseline | `mmlu_3820` | `mcq` | true | `B` | `B. affirmative action programs` |
| baseline | `mmlu_3821` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3822` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3823` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3824` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3825` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3826` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_3827` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3828` | `mcq` | true | `D` | `D. John Locke` |
| baseline | `mmlu_3829` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3830` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3831` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3832` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3833` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3834` | `mcq` | true | `D` | `D. Fourteenth Amendment` |
| baseline | `mmlu_3835` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3836` | `mcq` | true | `B` | `B. The Department of Justice` |
| baseline | `mmlu_3837` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3838` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3839` | `mcq` | false | `D` | `A. II III and IV only` |
| baseline | `mmlu_3840` | `mcq` | false | `D` | `B. Both the price level and real GDP rise.` |
| baseline | `mmlu_3841` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3842` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3843` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3844` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3845` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3846` | `mcq` | true | `D` | `D. opportunity cost` |
| baseline | `mmlu_3847` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3848` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3849` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3850` | `mcq` | false | `D` | `A. 5 percent decrease` |
| baseline | `mmlu_3851` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3852` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3853` | `mcq` | true | `B` | `B. 30%` |
| baseline | `mmlu_3854` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3855` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3856` | `mcq` | false | `B` | `D. expected future inflation.` |
| baseline | `mmlu_3857` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3858` | `mcq` | true | `D` | `D. I II and III are correct.` |
| baseline | `mmlu_3859` | `mcq` | true | `A` | `A. Falls     Falls     No change     Falls` |
| baseline | `mmlu_3860` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3861` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3862` | `mcq` | true | `B` | `B. Dollar bills` |
| baseline | `mmlu_3863` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3864` | `mcq` | true | `D` | `D. II III and IV only` |
| baseline | `mmlu_3865` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3866` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3867` | `mcq` | false | `B` | `A. Decreases            Increases      Decreases` |
| baseline | `mmlu_3868` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3869` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3870` | `mcq` | true | `D` | `D. unexpectedly higher resource prices.` |
| baseline | `mmlu_3871` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3872` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3873` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3874` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3875` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3876` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3877` | `mcq` | false | `C` | `A. $800` |
| baseline | `mmlu_3878` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3880` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3881` | `mcq` | false | `D` | `B. Decrease by $2.9 million.` |
| baseline | `mmlu_3882` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3883` | `mcq` | false | `C` | `A. NDP will be greater than GDP.` |
| baseline | `mmlu_3884` | `mcq` | true | `B` | `B. 7 14` |
| baseline | `mmlu_3885` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3886` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3887` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3888` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3889` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3890` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3891` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3892` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3893` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3894` | `mcq` | false | `D` | `A. Higher taxes     Selling Treasury securities` |
| baseline | `mmlu_3895` | `mcq` | true | `D` | `D. both A and D are correct.` |
| baseline | `mmlu_3896` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_3897` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3898` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3899` | `mcq` | true | `C` | `C. CPI` |
| baseline | `mmlu_3900` | `mcq` | true | `D` | `D. this will increase the demand for the product.` |
| baseline | `mmlu_3901` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3902` | `mcq` | true | `D` | `D. price level and real GDP` |
| baseline | `mmlu_3903` | `mcq` | true | `A` | `A. increase the equilibrium quantity and increase the price.` |
| baseline | `mmlu_3904` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3905` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3906` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3907` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3908` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3909` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3910` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3911` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3912` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3913` | `mcq` | false | `D` | `B. A greatly depreciated currency` |
| baseline | `mmlu_3914` | `mcq` | true | `B` | `B. An increase in labor productivity.` |
| baseline | `mmlu_3915` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3916` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_3917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3918` | `mcq` | false | `C` | `B. in several ways.` |
| baseline | `mmlu_3919` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_3920` | `mcq` | true | `C` | `C. Increases     Increases     Decreases` |
| baseline | `mmlu_3921` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3922` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3923` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_3924` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3925` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_3926` | `mcq` | true | `D` | `D. dumping.` |
| baseline | `mmlu_3927` | `mcq` | false | `C` | `A. $0 million` |
| baseline | `mmlu_3928` | `mcq` | true | `C` | `C. Decreases   Decreases   Increases` |
| baseline | `mmlu_3929` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3930` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_3931` | `mcq` | true | `B` | `B. 5.0 percent.` |
| baseline | `mmlu_3932` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_3933` | `mcq` | true | `C` | `C. this will put upward pressure on the nominal interest rate.` |
| baseline | `mmlu_3934` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3935` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3936` | `mcq` | false | `C` | `B. Changes in the money supply have significant effects.` |
| baseline | `mmlu_3937` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3938` | `mcq` | true | `A` | `A. An increase in the marginal propensity to consume` |
| baseline | `mmlu_3939` | `mcq` | false | `D` | `A. shifted the Phillips curve to the left.` |
| baseline | `mmlu_3940` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3941` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3942` | `mcq` | false | `C` | `D. contractionary monetary policy` |
| baseline | `mmlu_3943` | `mcq` | true | `B` | `B. Structural` |
| baseline | `mmlu_3944` | `mcq` | false | `B` | `C. variable.` |
| baseline | `mmlu_3945` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3946` | `mcq` | false | `D` | `B. $1.25` |
| baseline | `mmlu_3947` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3948` | `mcq` | true | `A` | `A. changes in the price level must be proportional to changes in the money supply.` |
| baseline | `mmlu_3949` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3950` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3951` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_3952` | `mcq` | true | `A` | `A. Decreases it by $9 million` |
| baseline | `mmlu_3953` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_3954` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_3955` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3956` | `mcq` | true | `B` | `B. $400 billion` |
| baseline | `mmlu_3957` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3958` | `mcq` | false | `A` | `D. Increased government spending.` |
| baseline | `mmlu_3959` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3960` | `mcq` | true | `A` | `A. divide nominal GDP by the GDP deflator.` |
| baseline | `mmlu_3961` | `mcq` | false | `D` | `C. Sell bonds     Decreases     Decreases     Inflation` |
| baseline | `mmlu_3962` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3963` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3964` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_3965` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3966` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_3967` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3968` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_3969` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_3970` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_3971` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_3972` | `mcq` | false | `C` | `D. China ($2).` |
| baseline | `mmlu_3973` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3974` | `mcq` | false | `A` | `C. Always horizontal.` |
| baseline | `mmlu_3975` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_3976` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_3977` | `mcq` | true | `D` | `D. Savers` |
| baseline | `mmlu_3978` | `mcq` | false | `D` | `C. Buy government securities risking a recessionary gap` |
| baseline | `mmlu_3979` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3980` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3981` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3982` | `mcq` | true | `D` | `D. The GDP deflator` |
| baseline | `mmlu_3983` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_3984` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_3985` | `mcq` | false | `A` | `D. Country A is less productive than country B.` |
| baseline | `mmlu_3986` | `mcq` | true | `A` | `A. implementing innovative production techniques.` |
| baseline | `mmlu_3987` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_3988` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_3989` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3990` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_3991` | `mcq` | true | `B` | `B. The sale of bonds` |
| baseline | `mmlu_3992` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_3993` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_3994` | `mcq` | false | `D` | `B. has risen 5 percent from the base to the current period.` |
| baseline | `mmlu_3995` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_3996` | `mcq` | true | `A` | `A. the money supply will increase.` |
| baseline | `mmlu_3997` | `mcq` | false | `C` | `A. The supply curve would shift up increasing the equilibrium interest rate.` |
| baseline | `mmlu_3998` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_3999` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4000` | `mcq` | false | `D` | `A. households provide goods to firms in exchange for wage payments.` |
| baseline | `mmlu_4001` | `mcq` | false | `C` | `A. increase imports` |
| baseline | `mmlu_4002` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4003` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4004` | `mcq` | true | `C` | `C. Decreasing     Increasing` |
| baseline | `mmlu_4005` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4006` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4007` | `mcq` | true | `D` | `D. Higher government funding of research on clean energy supplies` |
| baseline | `mmlu_4008` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4009` | `mcq` | false | `D` | `A. 10 years.` |
| baseline | `mmlu_4010` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4011` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4012` | `mcq` | true | `A` | `A. The capital account` |
| baseline | `mmlu_4013` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4014` | `mcq` | true | `B` | `B. Structural unemployment` |
| baseline | `mmlu_4015` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4016` | `mcq` | true | `A` | `A. 10 percent $450 in excess reserves` |
| baseline | `mmlu_4017` | `mcq` | true | `B` | `B. expansionary   4   -3` |
| baseline | `mmlu_4018` | `mcq` | false | `A` | `D. Decreased demand     Depreciating` |
| baseline | `mmlu_4019` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4020` | `mcq` | true | `A` | `A. Nation A has comparative advantage in the production of that good.` |
| baseline | `mmlu_4021` | `mcq` | false | `D` | `A. Increase` |
| baseline | `mmlu_4022` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4023` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4024` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4025` | `mcq` | true | `C` | `C. Medium of exchange` |
| baseline | `mmlu_4026` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4027` | `mcq` | false | `D` | `B. Increased demand   Rising   Appreciates` |
| baseline | `mmlu_4028` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4029` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4030` | `mcq` | true | `D` | `D. Inflation` |
| baseline | `mmlu_4031` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4032` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4033` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4034` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4035` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4036` | `mcq` | false | `D` | `B. Increase in demand   Buying Rising` |
| baseline | `mmlu_4037` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4038` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4039` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4040` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4041` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4042` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4043` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4044` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4045` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4046` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4047` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4048` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4049` | `mcq` | true | `C` | `C. The entire consumption function would shift upward.` |
| baseline | `mmlu_4050` | `mcq` | true | `C` | `C. Increases in the interest rate` |
| baseline | `mmlu_4051` | `mcq` | false | `D` | `C. I and III are correct.` |
| baseline | `mmlu_4052` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4053` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4054` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4055` | `mcq` | false | `C` | `B. decreased by 4 percent.` |
| baseline | `mmlu_4056` | `mcq` | true | `D` | `D. Deposits` |
| baseline | `mmlu_4057` | `mcq` | true | `C` | `C. Real GDP per capita.` |
| baseline | `mmlu_4058` | `mcq` | false | `D` | `A. $400` |
| baseline | `mmlu_4059` | `mcq` | true | `D` | `D. An increase in aggregate supply.` |
| baseline | `mmlu_4060` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4061` | `mcq` | false | `C` | `A. 25% $750 M = ¼` |
| baseline | `mmlu_4062` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4063` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4064` | `mcq` | true | `D` | `D. Decreases   Decreases    Decreases` |
| baseline | `mmlu_4065` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4066` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4067` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4068` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4069` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4070` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4071` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4072` | `mcq` | true | `A` | `A. 125` |
| baseline | `mmlu_4073` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4074` | `mcq` | true | `D` | `D. Lower taxes on personal income` |
| baseline | `mmlu_4075` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4076` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4077` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4078` | `mcq` | true | `D` | `D. Higher consumer prices and a misallocation of resources away from efficient producers` |
| baseline | `mmlu_4079` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4080` | `mcq` | true | `C` | `C. decrease interest rates and risk an inflationary period.` |
| baseline | `mmlu_4081` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4082` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4083` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4084` | `mcq` | false | `D` | `B. Decrease     Decrease     Decrease     Increase` |
| baseline | `mmlu_4085` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4086` | `mcq` | false | `D` | `C. output and population must have increased.` |
| baseline | `mmlu_4087` | `mcq` | true | `D` | `D. not counted in GDP.` |
| baseline | `mmlu_4088` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4089` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4090` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4091` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4092` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4093` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4094` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4095` | `mcq` | true | `D` | `D. Increase     Decrease     Increase` |
| baseline | `mmlu_4096` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4097` | `mcq` | false | `C` | `B. Money supply remains constant the interest rate does not fall and AD does not increase.` |
| baseline | `mmlu_4098` | `mcq` | false | `D` | `A. current-account balance only` |
| baseline | `mmlu_4099` | `mcq` | true | `D` | `D. Investment tax credits.` |
| baseline | `mmlu_4100` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4101` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4102` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4103` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4104` | `mcq` | false | `C` | `B. 5.0 percent.` |
| baseline | `mmlu_4105` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4106` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4107` | `mcq` | false | `A` | `B. (B) Increased     Increased` |
| baseline | `mmlu_4108` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4109` | `mcq` | false | `D` | `C. Real GDP will remain unchanged.` |
| baseline | `mmlu_4110` | `mcq` | true | `D` | `D. Increased     Decreased` |
| baseline | `mmlu_4111` | `mcq` | false | `C` | `B. $1,200` |
| baseline | `mmlu_4112` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4113` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4114` | `mcq` | true | `D` | `D. An increase in government spending` |
| baseline | `mmlu_4115` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4116` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4117` | `mcq` | true | `D` | `D. Saving is equal to zero when consumption equals disposable income.` |
| baseline | `mmlu_4118` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4119` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4120` | `mcq` | true | `B` | `B. A new production technique that lowers costs.` |
| baseline | `mmlu_4121` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4122` | `mcq` | false | `C` | `A/B/C/D` |
| baseline | `mmlu_4123` | `mcq` | true | `B` | `B. determined by supply and demand.` |
| baseline | `mmlu_4124` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4125` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4126` | `mcq` | true | `B` | `B. $4,500` |
| baseline | `mmlu_4127` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4128` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4129` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4130` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4131` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4132` | `mcq` | true | `B` | `B. $3,000` |
| baseline | `mmlu_4133` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4134` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_4135` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4136` | `mcq` | true | `C` | `C. depository institutions decide to hold more excess reserves.` |
| baseline | `mmlu_4137` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4138` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4139` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4140` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4141` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4142` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4143` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4144` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4145` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4146` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4147` | `mcq` | false | `D` | `A. Decrease   Increase   Increase` |
| baseline | `mmlu_4148` | `mcq` | true | `B` | `B. supply shocks` |
| baseline | `mmlu_4149` | `mcq` | false | `B` | `A. Only I is true.` |
| baseline | `mmlu_4150` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4151` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4152` | `mcq` | false | `B` | `D. Greater than $200 but less than $500` |
| baseline | `mmlu_4153` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4154` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4155` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4156` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4157` | `mcq` | true | `A` | `A. Higher disposable income higher consumption higher real GDP lower unemployment` |
| baseline | `mmlu_4158` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4159` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4160` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4161` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4162` | `mcq` | true | `D` | `D. An increase in demand increasing the interest rate.` |
| baseline | `mmlu_4163` | `mcq` | false | `D` | `A. Decreases appreciate decreases` |
| baseline | `mmlu_4164` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4165` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4166` | `mcq` | true | `D` | `D. Frictional` |
| baseline | `mmlu_4167` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4168` | `mcq` | false | `C` | `D. $1,900` |
| baseline | `mmlu_4169` | `mcq` | false | `D` | `C. The equilibrium price level and quantity of output increase.` |
| baseline | `mmlu_4170` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4171` | `mcq` | false | `A` | `D. I and III` |
| baseline | `mmlu_4172` | `mcq` | true | `B` | `B. More investment in capital infrastructure and less consumption of nondurable goods and services` |
| baseline | `mmlu_4173` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4174` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4175` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4176` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4177` | `mcq` | false | `A` | `B. Decrease   Decrease    Increase` |
| baseline | `mmlu_4178` | `mcq` | true | `C` | `C. Buying Treasury securities from commercial banks` |
| baseline | `mmlu_4179` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4180` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4181` | `mcq` | false | `D` | `A. Increases            Increases      Increases` |
| baseline | `mmlu_4182` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4183` | `mcq` | true | `A` | `A. appreciate.` |
| baseline | `mmlu_4184` | `mcq` | true | `A` | `A. deficit recession surplus expansion` |
| baseline | `mmlu_4185` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4186` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4187` | `mcq` | true | `A` | `A. Shifts down     Falls     Rises` |
| baseline | `mmlu_4188` | `mcq` | false | `C` | `D. France has the absolute advantage in cheese.` |
| baseline | `mmlu_4189` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4190` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4191` | `mcq` | true | `D` | `D. I and III.` |
| baseline | `mmlu_4192` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4193` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4194` | `mcq` | false | `A` | `B. this will cause the supply of the product to decrease right now.` |
| baseline | `mmlu_4195` | `mcq` | true | `B` | `B. the checking deposits increase.` |
| baseline | `mmlu_4196` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4197` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4198` | `mcq` | false | `A` | `B. increases decreases deficit` |
| baseline | `mmlu_4199` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4200` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4201` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4202` | `mcq` | false | `B` | `A. budget surpluses and higher discount rates.` |
| baseline | `mmlu_4203` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4204` | `mcq` | true | `B` | `B. Unit of account` |
| baseline | `mmlu_4205` | `mcq` | false | `B` | `A. higher taxes on corporate profits.` |
| baseline | `mmlu_4206` | `mcq` | true | `A` | `A. the aggregate demand curve should be shifted to the right.` |
| baseline | `mmlu_4207` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4208` | `mcq` | true | `B` | `B. Depreciation in the international value of the dollar` |
| baseline | `mmlu_4209` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4210` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4211` | `mcq` | true | `D` | `D. Increasing money spent to pay for government projects` |
| baseline | `mmlu_4212` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4213` | `mcq` | false | `B` | `A. increase by $200 million.` |
| baseline | `mmlu_4214` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4215` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4216` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4217` | `mcq` | true | `B` | `B. increase aggregate demand which will increase real output and increase employment.` |
| baseline | `mmlu_4218` | `mcq` | false | `B` | `C. I and IV only` |
| baseline | `mmlu_4219` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4220` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4221` | `mcq` | false | `D` | `A. Lower interest rates in the United States relative to China` |
| baseline | `mmlu_4222` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4223` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4224` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4225` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4226` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4227` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4228` | `mcq` | false | `D` | `A. (0, – 3)` |
| baseline | `mmlu_4229` | `mcq` | true | `C` | `C. 50` |
| baseline | `mmlu_4230` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4231` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4232` | `mcq` | true | `C` | `C. (-inf, 8)` |
| baseline | `mmlu_4233` | `mcq` | false | `B` | `A. 396` |
| baseline | `mmlu_4234` | `mcq` | false | `C` | `A. 0.16` |
| baseline | `mmlu_4235` | `mcq` | false | `A` | `C. 36` |
| baseline | `mmlu_4236` | `mcq` | false | `C` | `A. \(\frac{125}{648}\)` |
| baseline | `mmlu_4237` | `mcq` | false | `B` | `A. 8` |
| baseline | `mmlu_4238` | `mcq` | false | `D` | `B. 14` |
| baseline | `mmlu_4239` | `mcq` | false | `D` | `C. 2048` |
| baseline | `mmlu_4240` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_4241` | `mcq` | false | `B` | `C. 94.5` |
| baseline | `mmlu_4242` | `mcq` | false | `D` | `B. L <= T <= M <= R` |
| baseline | `mmlu_4243` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4244` | `mcq` | true | `A` | `A. 8` |
| baseline | `mmlu_4245` | `mcq` | false | `B` | `A. -2` |
| baseline | `mmlu_4246` | `mcq` | false | `A` | `C. 0` |
| baseline | `mmlu_4247` | `mcq` | false | `B` | `A. (-∞,-1)∪(1,+∞)` |
| baseline | `mmlu_4248` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4249` | `mcq` | false | `B` | `C. -32` |
| baseline | `mmlu_4250` | `mcq` | false | `D` | `A. 7` |
| baseline | `mmlu_4251` | `mcq` | false | `B` | `A. 4` |
| baseline | `mmlu_4252` | `mcq` | false | `A` | `B. Thursday` |
| baseline | `mmlu_4253` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_4254` | `mcq` | true | `D` | `D. 70` |
| baseline | `mmlu_4255` | `mcq` | false | `C` | `B. 5 min` |
| baseline | `mmlu_4256` | `mcq` | false | `C` | `D. (-inf, -1) U (-1, 4) U (4, inf)` |
| baseline | `mmlu_4257` | `mcq` | true | `D` | `D. 1/e` |
| baseline | `mmlu_4258` | `mcq` | true | `C` | `C. 0` |
| baseline | `mmlu_4259` | `mcq` | false | `A` | `C. 24` |
| baseline | `mmlu_4260` | `mcq` | false | `D` | `C. 840` |
| baseline | `mmlu_4261` | `mcq` | true | `A` | `A. 8788` |
| baseline | `mmlu_4262` | `mcq` | false | `A` | `C. -6` |
| baseline | `mmlu_4263` | `mcq` | false | `D` | `A. 15` |
| baseline | `mmlu_4264` | `mcq` | false | `C` | `B. 4680` |
| baseline | `mmlu_4265` | `mcq` | false | `C` | `A. 4.5` |
| baseline | `mmlu_4266` | `mcq` | true | `A` | `A. 240` |
| baseline | `mmlu_4267` | `mcq` | false | `A` | `B. 5` |
| baseline | `mmlu_4268` | `mcq` | false | `B` | `C. -1` |
| baseline | `mmlu_4269` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4270` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4271` | `mcq` | false | `C` | `A. (6-3x)(6+3x)` |
| baseline | `mmlu_4272` | `mcq` | false | `C` | `B. 90950` |
| baseline | `mmlu_4273` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4274` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4275` | `mcq` | false | `A` | `B. 5` |
| baseline | `mmlu_4276` | `mcq` | false | `D` | `A. 792` |
| baseline | `mmlu_4277` | `mcq` | true | `B` | `B. -75` |
| baseline | `mmlu_4278` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4279` | `mcq` | true | `A` | `A. 100` |
| baseline | `mmlu_4280` | `mcq` | true | `B` | `B. 9` |
| baseline | `mmlu_4281` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4282` | `mcq` | false | `C` | `B. \frac{1}{64}` |
| baseline | `mmlu_4283` | `mcq` | false | `A` | `B. \(\frac{25}{6}\)` |
| baseline | `mmlu_4284` | `mcq` | false | `B` | `C. \(\frac{1}{7}\)` |
| baseline | `mmlu_4285` | `mcq` | false | `B` | `C. 3, 9` |
| baseline | `mmlu_4286` | `mcq` | true | `B` | `B. 120` |
| baseline | `mmlu_4287` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_4288` | `mcq` | true | `D` | `D. 2793` |
| baseline | `mmlu_4289` | `mcq` | true | `B` | `B. 4.875` |
| baseline | `mmlu_4290` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4291` | `mcq` | false | `D` | `B. 2321` |
| baseline | `mmlu_4292` | `mcq` | true | `C` | `C. -128` |
| baseline | `mmlu_4293` | `mcq` | false | `B` | `A. –12` |
| baseline | `mmlu_4294` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_4295` | `mcq` | false | `B` | `C. 18` |
| baseline | `mmlu_4296` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4297` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_4298` | `mcq` | true | `C` | `C. 625` |
| baseline | `mmlu_4299` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4300` | `mcq` | false | `A` | `C. 27` |
| baseline | `mmlu_4301` | `mcq` | false | `C` | `B. 13` |
| baseline | `mmlu_4302` | `mcq` | true | `B` | `B. 1` |
| baseline | `mmlu_4303` | `mcq` | false | `D` | `A. 10240` |
| baseline | `mmlu_4304` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4305` | `mcq` | false | `A` | `C. 11` |
| baseline | `mmlu_4306` | `mcq` | true | `C` | `C. Friday` |
| baseline | `mmlu_4307` | `mcq` | true | `B` | `B. January 21st` |
| baseline | `mmlu_4308` | `mcq` | true | `B` | `B. 76` |
| baseline | `mmlu_4309` | `mcq` | true | `A` | `A. 89` |
| baseline | `mmlu_4310` | `mcq` | false | `C` | `A. 11` |
| baseline | `mmlu_4311` | `mcq` | false | `D` | `A. 6` |
| baseline | `mmlu_4312` | `mcq` | false | `D` | `C. 60` |
| baseline | `mmlu_4313` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4314` | `mcq` | false | `D` | `C. 18` |
| baseline | `mmlu_4315` | `mcq` | false | `A` | `B. 72` |
| baseline | `mmlu_4316` | `mcq` | false | `D` | `C. 32` |
| baseline | `mmlu_4317` | `mcq` | false | `C` | `D. 0` |
| baseline | `mmlu_4318` | `mcq` | false | `B` | `A. 36` |
| baseline | `mmlu_4319` | `mcq` | false | `C` | `A. \(\frac{x-5}{3}\)` |
| baseline | `mmlu_4320` | `mcq` | false | `B` | `A. 1` |
| baseline | `mmlu_4321` | `mcq` | false | `D` | `B. 16` |
| baseline | `mmlu_4322` | `mcq` | false | `A` | `C. \(\frac{7}{12}\)` |
| baseline | `mmlu_4323` | `mcq` | true | `A` | `A. -1/144` |
| baseline | `mmlu_4324` | `mcq` | false | `A` | `C. 0.33` |
| baseline | `mmlu_4325` | `mcq` | true | `B` | `B. 30%` |
| baseline | `mmlu_4326` | `mcq` | false | `C` | `A. 9` |
| baseline | `mmlu_4327` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4328` | `mcq` | true | `B` | `B. x+11` |
| baseline | `mmlu_4329` | `mcq` | false | `D` | `A. 13` |
| baseline | `mmlu_4330` | `mcq` | false | `C` | `D. 54,320` |
| baseline | `mmlu_4331` | `mcq` | true | `D` | `D. 25` |
| baseline | `mmlu_4332` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4333` | `mcq` | true | `A` | `A. 2` |
| baseline | `mmlu_4334` | `mcq` | true | `B` | `B. 31` |
| baseline | `mmlu_4335` | `mcq` | false | `C` | `A. 34` |
| baseline | `mmlu_4336` | `mcq` | false | `C` | `B. 16` |
| baseline | `mmlu_4337` | `mcq` | false | `D` | `B. \(\frac{7}{9}\)` |
| baseline | `mmlu_4338` | `mcq` | false | `C` | `A. 2.62` |
| baseline | `mmlu_4339` | `mcq` | false | `C` | `A. 300` |
| baseline | `mmlu_4340` | `mcq` | false | `A` | `B. 46` |
| baseline | `mmlu_4341` | `mcq` | true | `A` | `A. 12^(1/7)` |
| baseline | `mmlu_4342` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_4343` | `mcq` | true | `A` | `A. 80` |
| baseline | `mmlu_4344` | `mcq` | false | `C` | `B. 1` |
| baseline | `mmlu_4345` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4346` | `mcq` | true | `A` | `A. 288` |
| baseline | `mmlu_4347` | `mcq` | false | `B` | `A. 16` |
| baseline | `mmlu_4348` | `mcq` | false | `B` | `D. 999` |
| baseline | `mmlu_4349` | `mcq` | true | `A` | `A. \(\frac{1}{2}\)` |
| baseline | `mmlu_4350` | `mcq` | false | `D` | `A. 337125` |
| baseline | `mmlu_4351` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_4352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4353` | `mcq` | true | `D` | `D. 20` |
| baseline | `mmlu_4354` | `mcq` | false | `A` | `B. 592,704` |
| baseline | `mmlu_4355` | `mcq` | false | `C` | `B. 0.86` |
| baseline | `mmlu_4356` | `mcq` | true | `C` | `C. 0.547` |
| baseline | `mmlu_4357` | `mcq` | false | `B` | `C. 4` |
| baseline | `mmlu_4358` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_4359` | `mcq` | false | `B` | `C. -38` |
| baseline | `mmlu_4360` | `mcq` | true | `D` | `D. 71` |
| baseline | `mmlu_4361` | `mcq` | true | `B` | `B. 320` |
| baseline | `mmlu_4362` | `mcq` | false | `B` | `A. $227.50` |
| baseline | `mmlu_4363` | `mcq` | false | `B` | `C. 100` |
| baseline | `mmlu_4364` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_4365` | `mcq` | true | `B` | `B. 135` |
| baseline | `mmlu_4366` | `mcq` | true | `B` | `B. 5400` |
| baseline | `mmlu_4367` | `mcq` | true | `D` | `D. 8.6` |
| baseline | `mmlu_4368` | `mcq` | false | `D` | `A. Domain and range remain the same` |
| baseline | `mmlu_4369` | `mcq` | false | `B` | `C. 112` |
| baseline | `mmlu_4370` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4371` | `mcq` | true | `A` | `A. 90` |
| baseline | `mmlu_4372` | `mcq` | true | `D` | `D. 25` |
| baseline | `mmlu_4373` | `mcq` | true | `D` | `D. 104/3` |
| baseline | `mmlu_4374` | `mcq` | false | `A` | `B. 99` |
| baseline | `mmlu_4375` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4376` | `mcq` | false | `D` | `A. -\frac{7}{12}` |
| baseline | `mmlu_4377` | `mcq` | false | `D` | `A. 54` |
| baseline | `mmlu_4378` | `mcq` | true | `C` | `C. -1.5` |
| baseline | `mmlu_4379` | `mcq` | false | `C` | `D. 574` |
| baseline | `mmlu_4380` | `mcq` | false | `C` | `A. 12` |
| baseline | `mmlu_4381` | `mcq` | true | `B` | `B. 298` |
| baseline | `mmlu_4382` | `mcq` | true | `A` | `A. \(\frac{8}{45}\)` |
| baseline | `mmlu_4383` | `mcq` | false | `C` | `B. 8` |
| baseline | `mmlu_4384` | `mcq` | false | `D` | `A. 18` |
| baseline | `mmlu_4385` | `mcq` | false | `D` | `A. 1` |
| baseline | `mmlu_4386` | `mcq` | false | `B` | `A. 38` |
| baseline | `mmlu_4387` | `mcq` | true | `A` | `A. 7` |
| baseline | `mmlu_4388` | `mcq` | false | `A` | `C. \(\frac{10}{3}\)` |
| baseline | `mmlu_4389` | `mcq` | true | `B` | `B. $8,902` |
| baseline | `mmlu_4390` | `mcq` | true | `D` | `D. 3,003` |
| baseline | `mmlu_4391` | `mcq` | false | `C` | `B. 2.931` |
| baseline | `mmlu_4392` | `mcq` | true | `B` | `B. 0` |
| baseline | `mmlu_4393` | `mcq` | false | `D` | `B. 1024` |
| baseline | `mmlu_4394` | `mcq` | true | `B` | `B. 40` |
| baseline | `mmlu_4395` | `mcq` | true | `B` | `B. –33%` |
| baseline | `mmlu_4396` | `mcq` | true | `B` | `B. \(\frac{15}{2}\)` |
| baseline | `mmlu_4397` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4398` | `mcq` | false | `D` | `C. 4-i` |
| baseline | `mmlu_4399` | `mcq` | true | `C` | `C. 39` |
| baseline | `mmlu_4400` | `mcq` | true | `B` | `B. 3` |
| baseline | `mmlu_4401` | `mcq` | false | `C` | `B. $\frac{7}{12}$` |
| baseline | `mmlu_4402` | `mcq` | true | `C` | `C. 20%` |
| baseline | `mmlu_4403` | `mcq` | true | `C` | `C. 3980` |
| baseline | `mmlu_4404` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4405` | `mcq` | false | `D` | `B. \(\frac{17}{66}\)` |
| baseline | `mmlu_4406` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4407` | `mcq` | false | `D` | `B. 32π/3` |
| baseline | `mmlu_4408` | `mcq` | true | `A` | `A. \(\frac{5}{4}\)` |
| baseline | `mmlu_4409` | `mcq` | true | `D` | `D. 2π` |
| baseline | `mmlu_4410` | `mcq` | false | `A` | `B. 34` |
| baseline | `mmlu_4411` | `mcq` | false | `C` | `A. 2` |
| baseline | `mmlu_4412` | `mcq` | false | `C` | `B. 22140` |
| baseline | `mmlu_4413` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4414` | `mcq` | false | `D` | `A. \(\frac{1}{4}\)` |
| baseline | `mmlu_4415` | `mcq` | true | `C` | `C. 36` |
| baseline | `mmlu_4416` | `mcq` | true | `B` | `B. 55` |
| baseline | `mmlu_4417` | `mcq` | true | `A` | `A. 29` |
| baseline | `mmlu_4418` | `mcq` | false | `C` | `A. \(\frac{5}{24}\)` |
| baseline | `mmlu_4419` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_4420` | `mcq` | false | `B` | `A. 3` |
| baseline | `mmlu_4421` | `mcq` | false | `C` | `B. 6` |
| baseline | `mmlu_4422` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4423` | `mcq` | false | `C` | `A. 6` |
| baseline | `mmlu_4424` | `mcq` | true | `D` | `D. p+q-r` |
| baseline | `mmlu_4425` | `mcq` | true | `B` | `B. 2 × 5` |
| baseline | `mmlu_4426` | `mcq` | false | `D` | `B. 6` |
| baseline | `mmlu_4427` | `mcq` | false | `C` | `D. (–3, –2)` |
| baseline | `mmlu_4428` | `mcq` | false | `C` | `B. 20` |
| baseline | `mmlu_4429` | `mcq` | false | `D` | `B. \frac{8}{15}` |
| baseline | `mmlu_4430` | `mcq` | false | `D` | `A. 67` |
| baseline | `mmlu_4431` | `mcq` | true | `B` | `B. -14` |
| baseline | `mmlu_4432` | `mcq` | true | `A` | `A. 50 + 50i` |
| baseline | `mmlu_4433` | `mcq` | false | `D` | `A. 10` |
| baseline | `mmlu_4434` | `mcq` | false | `A` | `C. -40` |
| baseline | `mmlu_4435` | `mcq` | false | `C` | `A. 46/3` |
| baseline | `mmlu_4436` | `mcq` | true | `A` | `A. -4` |
| baseline | `mmlu_4437` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_4438` | `mcq` | false | `C` | `B. 36 inches` |
| baseline | `mmlu_4439` | `mcq` | false | `C` | `A. \(\frac{13}{4}\)` |
| baseline | `mmlu_4440` | `mcq` | false | `C` | `A. 2` |
| baseline | `mmlu_4441` | `mcq` | false | `D` | `A. $\frac{3}{4}$` |
| baseline | `mmlu_4442` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4443` | `mcq` | false | `B` | `C. I` |
| baseline | `mmlu_4444` | `mcq` | false | `D` | `C. 0 ≤ y ≤ 6` |
| baseline | `mmlu_4445` | `mcq` | true | `D` | `D. y – 4 = ln 2(x – 5)` |
| baseline | `mmlu_4446` | `mcq` | true | `A` | `A. \(\frac{1}{2}\)` |
| baseline | `mmlu_4447` | `mcq` | false | `B` | `A. 7` |
| baseline | `mmlu_4448` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_4449` | `mcq` | true | `B` | `B. 400` |
| baseline | `mmlu_4450` | `mcq` | true | `B` | `B. \(\frac{161}{36}\)` |
| baseline | `mmlu_4451` | `mcq` | true | `A` | `A. 112` |
| baseline | `mmlu_4452` | `mcq` | false | `D` | `C. 12` |
| baseline | `mmlu_4453` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4454` | `mcq` | false | `A` | `B. 120` |
| baseline | `mmlu_4455` | `mcq` | false | `B` | `C. 2.427` |
| baseline | `mmlu_4456` | `mcq` | false | `C` | `B. 64` |
| baseline | `mmlu_4457` | `mcq` | false | `B` | `C. 87` |
| baseline | `mmlu_4458` | `mcq` | true | `A` | `A. 165` |
| baseline | `mmlu_4459` | `mcq` | false | `C` | `A. 0 or –1/3` |
| baseline | `mmlu_4460` | `mcq` | false | `A` | `B. 276` |
| baseline | `mmlu_4461` | `mcq` | false | `C` | `A. 28` |
| baseline | `mmlu_4462` | `mcq` | false | `D` | `C. 2` |
| baseline | `mmlu_4463` | `mcq` | false | `C` | `A. 5,760` |
| baseline | `mmlu_4464` | `mcq` | false | `C` | `B. 33` |
| baseline | `mmlu_4465` | `mcq` | false | `A` | `B. 12` |
| baseline | `mmlu_4466` | `mcq` | false | `B` | `A. \(\frac{4\sqrt{3}}{33}\)` |
| baseline | `mmlu_4467` | `mcq` | true | `A` | `A. 1/e` |
| baseline | `mmlu_4468` | `mcq` | false | `A` | `B. \(\frac{27}{128}\)` |
| baseline | `mmlu_4469` | `mcq` | true | `B` | `B. east` |
| baseline | `mmlu_4470` | `mcq` | false | `C` | `A. 15` |
| baseline | `mmlu_4471` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_4472` | `mcq` | false | `C` | `B. (\(\frac{231}{20}\), \(\frac{21}{20}\))` |
| baseline | `mmlu_4473` | `mcq` | false | `C` | `B. θ = 0.39` |
| baseline | `mmlu_4474` | `mcq` | false | `D` | `A. 4.68` |
| baseline | `mmlu_4475` | `mcq` | false | `C` | `A. none` |
| baseline | `mmlu_4476` | `mcq` | false | `D` | `C. 4` |
| baseline | `mmlu_4477` | `mcq` | false | `C` | `A. [-\frac{1}{2}, 0]` |
| baseline | `mmlu_4478` | `mcq` | true | `B` | `B. 2` |
| baseline | `mmlu_4479` | `mcq` | false | `D` | `B. 2049` |
| baseline | `mmlu_4480` | `mcq` | false | `B` | `A. 3` |
| baseline | `mmlu_4481` | `mcq` | false | `B` | `C. 9.2` |
| baseline | `mmlu_4482` | `mcq` | true | `B` | `B. 800,000 + 650 D` |
| baseline | `mmlu_4483` | `mcq` | false | `B` | `C. 4` |
| baseline | `mmlu_4484` | `mcq` | false | `D` | `B. -2` |
| baseline | `mmlu_4485` | `mcq` | true | `B` | `B. 27` |
| baseline | `mmlu_4486` | `mcq` | true | `B` | `B. \frac{1}{12}` |
| baseline | `mmlu_4487` | `mcq` | true | `A` | `A. (0, 9)` |
| baseline | `mmlu_4488` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4489` | `mcq` | false | `C` | `B. 4680` |
| baseline | `mmlu_4490` | `mcq` | true | `A` | `A. 5, 14` |
| baseline | `mmlu_4491` | `mcq` | true | `D` | `D. 1920` |
| baseline | `mmlu_4492` | `mcq` | false | `D` | `C. 3.999` |
| baseline | `mmlu_4493` | `mcq` | false | `C` | `A. 16401` |
| baseline | `mmlu_4494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4495` | `mcq` | false | `B` | `C. 7.98` |
| baseline | `mmlu_4496` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4497` | `mcq` | false | `B` | `A. -80` |
| baseline | `mmlu_4498` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4499` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4500` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4501` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4502` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4503` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4504` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4505` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4506` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4507` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4508` | `mcq` | true | `C` | `C. The size of a McDonald’s kitchen.` |
| baseline | `mmlu_4509` | `mcq` | false | `C` | `A. Price rises, but quantity is ambiguous.` |
| baseline | `mmlu_4510` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4512` | `mcq` | true | `B` | `B. plant and equipment.` |
| baseline | `mmlu_4513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4514` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4515` | `mcq` | true | `D` | `D. Decrease her consumption of chips and increase her consumption of dip until the marginal utility per dollar is equal ` |
| baseline | `mmlu_4516` | `mcq` | true | `B` | `B. Market failure` |
| baseline | `mmlu_4517` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4518` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4519` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4520` | `mcq` | true | `D` | `D. I and III only.` |
| baseline | `mmlu_4521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4522` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4523` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4524` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4525` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4526` | `mcq` | true | `B` | `B. 2` |
| baseline | `mmlu_4527` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4528` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4529` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4530` | `mcq` | true | `D` | `D. Jason should clean 9 pools per day, with economic losses of $10.` |
| baseline | `mmlu_4531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4532` | `mcq` | true | `B` | `B. the total welfare is maximized.` |
| baseline | `mmlu_4533` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4534` | `mcq` | true | `B` | `B. substitution effect.` |
| baseline | `mmlu_4535` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4536` | `mcq` | true | `A` | `A. Decrease price as demand is elastic.` |
| baseline | `mmlu_4537` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4538` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4539` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4540` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4541` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4542` | `mcq` | true | `B` | `B. The volunteer fire department in your community` |
| baseline | `mmlu_4543` | `mcq` | true | `D` | `D. The International Space Station` |
| baseline | `mmlu_4544` | `mcq` | false | `C` | `B. Inferior` |
| baseline | `mmlu_4545` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4546` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4547` | `mcq` | true | `B` | `B. The quantity demanded equals the quantity supplied of good X.` |
| baseline | `mmlu_4548` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4549` | `mcq` | true | `A` | `A. equilibrium quantity rises, but the price change is ambiguous.` |
| baseline | `mmlu_4550` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4551` | `mcq` | true | `B` | `B. elastic.` |
| baseline | `mmlu_4552` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4553` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4554` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4555` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4556` | `mcq` | true | `B` | `B. the marginal benefit equals the marginal cost of the next cookie.` |
| baseline | `mmlu_4557` | `mcq` | true | `B` | `B. I and II.` |
| baseline | `mmlu_4558` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4559` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4560` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4561` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4562` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4563` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4564` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4565` | `mcq` | true | `D` | `D. Average revenue equals marginal revenue.` |
| baseline | `mmlu_4566` | `mcq` | true | `D` | `D. Wage = Marginal revenue product of labor.` |
| baseline | `mmlu_4567` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4568` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4569` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4570` | `mcq` | true | `D` | `D. The firm may earn positive, negative, or normal profits.` |
| baseline | `mmlu_4571` | `mcq` | false | `B` | `D. Technology in the harvesting of coffee beans improves.` |
| baseline | `mmlu_4572` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4573` | `mcq` | false | `D` | `A. Decrease price because demand is elastic` |
| baseline | `mmlu_4574` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4575` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4576` | `mcq` | true | `D` | `D. Air` |
| baseline | `mmlu_4577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4578` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4579` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4580` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4581` | `mcq` | true | `D` | `D. II, III, and V only` |
| baseline | `mmlu_4582` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4583` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4584` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4585` | `mcq` | false | `B` | `A. upward sloping` |
| baseline | `mmlu_4586` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4587` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4588` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4589` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4590` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4591` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4592` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4593` | `mcq` | false | `B` | `A. Labor demand` |
| baseline | `mmlu_4594` | `mcq` | true | `B` | `B. Price rises, but the change in quantity is ambiguous.` |
| baseline | `mmlu_4595` | `mcq` | true | `D` | `D. The price of crude oil, a raw material for gasoline, rises.` |
| baseline | `mmlu_4596` | `mcq` | true | `B` | `B. An increase in the price of tubas` |
| baseline | `mmlu_4597` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4598` | `mcq` | true | `D` | `D. opportunity cost.` |
| baseline | `mmlu_4599` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4600` | `mcq` | true | `D` | `D. pays less and hires fewer` |
| baseline | `mmlu_4601` | `mcq` | false | `A` | `D. The wage would fall, but employment would increase.` |
| baseline | `mmlu_4602` | `mcq` | false | `A` | `B. There would be a shortage created of corn.` |
| baseline | `mmlu_4603` | `mcq` | true | `D` | `D. the minimum of average variable cost` |
| baseline | `mmlu_4604` | `mcq` | false | `C` | `B. of opportunity cost.` |
| baseline | `mmlu_4605` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4606` | `mcq` | true | `A` | `A. The Reds offer discounted parking for all home games.` |
| baseline | `mmlu_4607` | `mcq` | false | `D` | `C. I and III only` |
| baseline | `mmlu_4608` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4609` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4610` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4611` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4612` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4613` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4614` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4615` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4616` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4617` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4618` | `mcq` | true | `C` | `C. total revenue.` |
| baseline | `mmlu_4619` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4620` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4621` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4622` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4623` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4624` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4625` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4626` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4627` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4628` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4629` | `mcq` | true | `A` | `A. Diminishing marginal productivity.` |
| baseline | `mmlu_4630` | `mcq` | true | `B` | `B. Subsidize the firm or its customers.` |
| baseline | `mmlu_4631` | `mcq` | true | `C` | `C. substitutes.` |
| baseline | `mmlu_4632` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4634` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4635` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4636` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4637` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4638` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4639` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4640` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4641` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4642` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4643` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4644` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4645` | `mcq` | true | `C` | `C. Private property.` |
| baseline | `mmlu_4646` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4647` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4648` | `mcq` | true | `D` | `D. the marginal utility from eating the last cookie is zero.` |
| baseline | `mmlu_4649` | `mcq` | false | `A` | `C. Do not produce if the TFC is not covered by revenue.` |
| baseline | `mmlu_4650` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4651` | `mcq` | true | `B` | `B. increasing opportunity cost of time` |
| baseline | `mmlu_4652` | `mcq` | true | `C` | `C. Factors of production` |
| baseline | `mmlu_4653` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4654` | `mcq` | true | `A` | `A. Substitution effects and income effects` |
| baseline | `mmlu_4655` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4656` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4657` | `mcq` | false | `B` | `A. The marginal cost and average variable cost curves will shift upward.` |
| baseline | `mmlu_4658` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4659` | `mcq` | true | `D` | `D. Average total cost = average variable cost plus average fixed cost.` |
| baseline | `mmlu_4660` | `mcq` | true | `C` | `C. significant barriers to entry.` |
| baseline | `mmlu_4661` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4662` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4663` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4664` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4665` | `mcq` | false | `C` | `B. (MC-P)/P` |
| baseline | `mmlu_4666` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4667` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4668` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4669` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4670` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4671` | `mcq` | false | `A` | `B. Demand for automobiles` |
| baseline | `mmlu_4672` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_4673` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4674` | `mcq` | true | `D` | `D. I, II, III, and IV` |
| baseline | `mmlu_4675` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4676` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4678` | `mcq` | true | `C` | `C. Regressive` |
| baseline | `mmlu_4679` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4680` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4681` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4682` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4683` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4684` | `mcq` | true | `B` | `B. She should increase her apple consumption and decrease her orange consumption until the marginal utility per dollar i` |
| baseline | `mmlu_4685` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4686` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4687` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4688` | `mcq` | true | `A` | `A. the marginal social benefit exceeds the marginal social cost.` |
| baseline | `mmlu_4689` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4690` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4691` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4692` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4693` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4694` | `mcq` | true | `C` | `C. the marginal cost curve intersects the demand curve` |
| baseline | `mmlu_4695` | `mcq` | true | `C` | `C. The value placed on the owner's skills in an alternative career` |
| baseline | `mmlu_4696` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4697` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4698` | `mcq` | true | `B` | `B. law of demand` |
| baseline | `mmlu_4699` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4700` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4701` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4702` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4703` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4704` | `mcq` | true | `A` | `A. P = MR = MC = ATC` |
| baseline | `mmlu_4705` | `mcq` | false | `D` | `A. Price rises as firms enter the industry.` |
| baseline | `mmlu_4706` | `mcq` | true | `C` | `C. An increase in printing costs` |
| baseline | `mmlu_4707` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4708` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4709` | `mcq` | true | `D` | `D. a straight diagonal line sloping downward from left to right.` |
| baseline | `mmlu_4710` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4711` | `mcq` | true | `A` | `A. Diminishing Marginal Utility` |
| baseline | `mmlu_4712` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4713` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4714` | `mcq` | true | `D` | `D. A perfectly vertical supply curve.` |
| baseline | `mmlu_4715` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4716` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4717` | `mcq` | true | `B` | `B. Increases` |
| baseline | `mmlu_4718` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4719` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4720` | `mcq` | true | `A` | `A. marginal utility is zero` |
| baseline | `mmlu_4721` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4722` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4723` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4724` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4725` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4726` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4728` | `mcq` | true | `C` | `C. Supply public goods using tax dollars` |
| baseline | `mmlu_4729` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4730` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4731` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4732` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4733` | `mcq` | false | `D` | `C. The ATC curve intersects the MC curve at the minimum point of the MC curve.` |
| baseline | `mmlu_4734` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4735` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4736` | `mcq` | false | `B` | `D. 0.5 C` |
| baseline | `mmlu_4737` | `mcq` | false | `A` | `C. the electric field produced by an infinite plane of charge` |
| baseline | `mmlu_4738` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4739` | `mcq` | false | `C` | `A. Less, because the tension in the string varies directly with the wave speed, which varies inversely with the waveleng` |
| baseline | `mmlu_4740` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_4741` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4742` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4743` | `mcq` | true | `C` | `C. 0.05 J` |
| baseline | `mmlu_4744` | `mcq` | true | `A` | `A. v0^2/(2μg)` |
| baseline | `mmlu_4745` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4746` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4747` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4748` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4749` | `mcq` | false | `B` | `D. 0.03 s` |
| baseline | `mmlu_4750` | `mcq` | false | `B` | `C. 2 N/kg` |
| baseline | `mmlu_4751` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4752` | `mcq` | false | `D` | `A. 1 nm` |
| baseline | `mmlu_4753` | `mcq` | false | `C` | `B. 100 cm` |
| baseline | `mmlu_4754` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4755` | `mcq` | false | `D` | `A. –165 V` |
| baseline | `mmlu_4756` | `mcq` | true | `B` | `B. 300 J out of the system` |
| baseline | `mmlu_4757` | `mcq` | false | `C` | `D. It will remain the same.` |
| baseline | `mmlu_4758` | `mcq` | true | `A` | `A. 5 × 10^15 Hz` |
| baseline | `mmlu_4759` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4760` | `mcq` | false | `D` | `B. 9.0 × 10^4 N/C` |
| baseline | `mmlu_4761` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4762` | `mcq` | false | `C` | `B. 6 m/s` |
| baseline | `mmlu_4763` | `mcq` | false | `C` | `B. 2/3 V` |
| baseline | `mmlu_4764` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4765` | `mcq` | false | `D` | `A. increases linearly` |
| baseline | `mmlu_4766` | `mcq` | true | `A` | `A. 1.41v` |
| baseline | `mmlu_4767` | `mcq` | true | `C` | `C. The net charge has not changed.` |
| baseline | `mmlu_4768` | `mcq` | false | `B` | `D. It would stop rotating on its axis, and it would stop revolving around the Earth.` |
| baseline | `mmlu_4769` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4770` | `mcq` | false | `C` | `D. I & III only` |
| baseline | `mmlu_4771` | `mcq` | false | `C` | `B. LM/T^2` |
| baseline | `mmlu_4772` | `mcq` | false | `C` | `A. 5.0 × 10^6 m/s` |
| baseline | `mmlu_4773` | `mcq` | false | `D` | `A. The force of the elevator cable on the man` |
| baseline | `mmlu_4774` | `mcq` | false | `A` | `B. 150 J of heat was removed from the gas.` |
| baseline | `mmlu_4775` | `mcq` | false | `A` | `C. 1.60 × 10^19` |
| baseline | `mmlu_4776` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4777` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4778` | `mcq` | false | `C` | `D. It would fall to the other side and stop there.` |
| baseline | `mmlu_4779` | `mcq` | false | `D` | `B. It will decrease the amplitude.` |
| baseline | `mmlu_4780` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4781` | `mcq` | false | `B` | `C. 2.0/3` |
| baseline | `mmlu_4782` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4783` | `mcq` | false | `B` | `A. 4d` |
| baseline | `mmlu_4784` | `mcq` | true | `D` | `D. Any 2 of the above values` |
| baseline | `mmlu_4785` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4786` | `mcq` | true | `A` | `A. 2 cm ≤ D ≤ 10 cm` |
| baseline | `mmlu_4787` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4788` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4789` | `mcq` | false | `D` | `B. Weight` |
| baseline | `mmlu_4790` | `mcq` | false | `B` | `C. 2f` |
| baseline | `mmlu_4791` | `mcq` | false | `D` | `B. -5/3 cm` |
| baseline | `mmlu_4792` | `mcq` | false | `C` | `D. -99m` |
| baseline | `mmlu_4793` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4794` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4795` | `mcq` | false | `C` | `A. 1 N` |
| baseline | `mmlu_4796` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4797` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4798` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4799` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4800` | `mcq` | false | `C` | `A. a cubic relationship between C^3 and T` |
| baseline | `mmlu_4801` | `mcq` | false | `D` | `A. 6.4 × 10^-19 C` |
| baseline | `mmlu_4802` | `mcq` | false | `C` | `A. 5.0 × 10^5 m/s` |
| baseline | `mmlu_4803` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4804` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4805` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4806` | `mcq` | false | `D` | `A. Mass, velocity, height, and acceleration` |
| baseline | `mmlu_4807` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4808` | `mcq` | true | `C` | `C. The proton will continue in its straight path at constant velocity.` |
| baseline | `mmlu_4809` | `mcq` | false | `B` | `D. 4v` |
| baseline | `mmlu_4810` | `mcq` | false | `A` | `B. only when the enclosed charge is symmetrically distributed` |
| baseline | `mmlu_4811` | `mcq` | true | `B` | `B. speed and wavelength` |
| baseline | `mmlu_4812` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4813` | `mcq` | false | `B` | `D. half the magnitude and in the opposite direction` |
| baseline | `mmlu_4814` | `mcq` | true | `D` | `D. All reach the base at the same time.` |
| baseline | `mmlu_4815` | `mcq` | false | `A` | `B. 300 m` |
| baseline | `mmlu_4816` | `mcq` | false | `D` | `A. sin–1 (1/g)` |
| baseline | `mmlu_4817` | `mcq` | false | `D` | `B. 41°` |
| baseline | `mmlu_4818` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4819` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4820` | `mcq` | true | `A` | `A. 50 μN` |
| baseline | `mmlu_4821` | `mcq` | false | `A` | `D. Linear momentum` |
| baseline | `mmlu_4822` | `mcq` | false | `C` | `D. 60 m` |
| baseline | `mmlu_4823` | `mcq` | false | `C` | `A. ax = 0; ay < g` |
| baseline | `mmlu_4824` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4825` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4826` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4827` | `mcq` | false | `D` | `A. Gamma rays` |
| baseline | `mmlu_4828` | `mcq` | false | `C` | `B. 1.0 m/s` |
| baseline | `mmlu_4829` | `mcq` | false | `D` | `C. The image gets smaller at first and then bigger in size.` |
| baseline | `mmlu_4830` | `mcq` | false | `D` | `B. 4.9 m/s^2` |
| baseline | `mmlu_4831` | `mcq` | false | `B` | `D. 1600 N` |
| baseline | `mmlu_4832` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4833` | `mcq` | false | `C` | `D. 12.5 J` |
| baseline | `mmlu_4834` | `mcq` | false | `A` | `B. A high voltage battery with resistors arranged in parallel` |
| baseline | `mmlu_4835` | `mcq` | false | `C` | `A. 0.16 N` |
| baseline | `mmlu_4836` | `mcq` | false | `D` | `C. The block, because it does not lose mechanical energy due to friction, but the sphere does` |
| baseline | `mmlu_4837` | `mcq` | false | `C` | `A. Use light of a shorter wavelength.` |
| baseline | `mmlu_4838` | `mcq` | true | `B` | `B. 25 m/s, downward` |
| baseline | `mmlu_4839` | `mcq` | false | `D` | `A. x = –4` |
| baseline | `mmlu_4840` | `mcq` | true | `A` | `A. Clockwise rotation; radius of path = mv/(eB)` |
| baseline | `mmlu_4841` | `mcq` | false | `B` | `C. Decreasing the angle of the string from the horizontal when released` |
| baseline | `mmlu_4842` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4843` | `mcq` | true | `D` | `D. 1.6 m` |
| baseline | `mmlu_4844` | `mcq` | false | `C` | `B. 2 s` |
| baseline | `mmlu_4845` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4846` | `mcq` | false | `B` | `C. 9.8 m/s^2` |
| baseline | `mmlu_4847` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4848` | `mcq` | true | `A` | `A. Static friction` |
| baseline | `mmlu_4849` | `mcq` | false | `D` | `A. zero` |
| baseline | `mmlu_4850` | `mcq` | true | `C` | `C. The electric force, because the outer electrons in the top atomic layer of the table repel the outer electrons in the` |
| baseline | `mmlu_4851` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4852` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4853` | `mcq` | false | `C` | `B. 2h` |
| baseline | `mmlu_4854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4855` | `mcq` | true | `C` | `C. 10^19 N` |
| baseline | `mmlu_4856` | `mcq` | false | `D` | `B. 30%` |
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
| baseline | `mmlu_4874` | `mcq` | false | `D` | `C. It increases linearly for r > R.` |
| baseline | `mmlu_4875` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4876` | `mcq` | true | `C` | `C. Both the length and area` |
| baseline | `mmlu_4877` | `mcq` | false | `B` | `A. An upright, real image about 20 cm in front of her eyes` |
| baseline | `mmlu_4878` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4879` | `mcq` | true | `A` | `A. 4F` |
| baseline | `mmlu_4880` | `mcq` | false | `D` | `B. 9.0 × 10^4 V/m` |
| baseline | `mmlu_4881` | `mcq` | false | `C` | `A. 4:01` |
| baseline | `mmlu_4882` | `mcq` | false | `D` | `B. The wave pulse's width has become greater.` |
| baseline | `mmlu_4883` | `mcq` | false | `D` | `C. Air resistance increases the acceleration of the ball.` |
| baseline | `mmlu_4884` | `mcq` | false | `D` | `A. (1/25) AU` |
| baseline | `mmlu_4885` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4886` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4887` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4888` | `mcq` | true | `B` | `B. schizophrenia.` |
| baseline | `mmlu_4889` | `mcq` | true | `D` | `D. Hierarchy of needs` |
| baseline | `mmlu_4890` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4891` | `mcq` | true | `C` | `C. Schools being held responsible for providing tests that do not discriminate on the basis of race` |
| baseline | `mmlu_4892` | `mcq` | true | `A` | `A. 0%` |
| baseline | `mmlu_4893` | `mcq` | true | `A` | `A. variance` |
| baseline | `mmlu_4894` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4895` | `mcq` | false | `A` | `D. distributed throughout the list` |
| baseline | `mmlu_4896` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4897` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4898` | `mcq` | true | `C` | `C. binocular and monocular cues` |
| baseline | `mmlu_4899` | `mcq` | true | `D` | `D. die` |
| baseline | `mmlu_4900` | `mcq` | true | `B` | `B. standardized` |
| baseline | `mmlu_4901` | `mcq` | true | `D` | `D. generalization` |
| baseline | `mmlu_4902` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4903` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4904` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4905` | `mcq` | true | `D` | `D. bitter` |
| baseline | `mmlu_4906` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4907` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4908` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4909` | `mcq` | false | `C` | `D. Peer comparison` |
| baseline | `mmlu_4910` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4911` | `mcq` | true | `C` | `C. Hormones released in the womb` |
| baseline | `mmlu_4912` | `mcq` | true | `B` | `B. crystallized intelligence` |
| baseline | `mmlu_4913` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4914` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4915` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4916` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4918` | `mcq` | true | `A` | `A. Inferential statistics` |
| baseline | `mmlu_4919` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4920` | `mcq` | true | `D` | `D. systematic desensitization` |
| baseline | `mmlu_4921` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4922` | `mcq` | true | `A` | `A. high self-esteem` |
| baseline | `mmlu_4923` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4924` | `mcq` | true | `B` | `B. Cognitive` |
| baseline | `mmlu_4925` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4926` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4927` | `mcq` | true | `B` | `B. regulating emotion.` |
| baseline | `mmlu_4928` | `mcq` | true | `D` | `D. show that the manipulation of one variable invariably leads to predicted changes in another` |
| baseline | `mmlu_4929` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4930` | `mcq` | true | `B` | `B. recalling the name of your junior high school shop teacher` |
| baseline | `mmlu_4931` | `mcq` | true | `D` | `D. survey` |
| baseline | `mmlu_4932` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4933` | `mcq` | true | `B` | `B. critical periods` |
| baseline | `mmlu_4934` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4935` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4936` | `mcq` | true | `D` | `D. Implementing social skills training to teach Kerry appropriate replacement behaviors for hostile behaviors` |
| baseline | `mmlu_4937` | `mcq` | true | `D` | `D. autism.` |
| baseline | `mmlu_4938` | `mcq` | true | `B` | `B. nausea and food or drink` |
| baseline | `mmlu_4939` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4940` | `mcq` | true | `D` | `D. dissociative` |
| baseline | `mmlu_4941` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4942` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4943` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4944` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4945` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4946` | `mcq` | true | `B` | `B. Correlation-it would be unethical to purposefully expose middle school students to bullying behaviors, so Professor E` |
| baseline | `mmlu_4947` | `mcq` | false | `C` | `B. post-traumatic stress disorder` |
| baseline | `mmlu_4948` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4949` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4950` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4951` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4952` | `mcq` | true | `B` | `B. violet` |
| baseline | `mmlu_4953` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4954` | `mcq` | true | `A` | `A. olfactory receptors` |
| baseline | `mmlu_4955` | `mcq` | true | `B` | `B. nausea and food or drink` |
| baseline | `mmlu_4956` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4957` | `mcq` | false | `C` | `A. Duration recording` |
| baseline | `mmlu_4958` | `mcq` | true | `D` | `D. medulla` |
| baseline | `mmlu_4959` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4960` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4961` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4962` | `mcq` | true | `D` | `D. positive psychology` |
| baseline | `mmlu_4963` | `mcq` | true | `A` | `A. paranoid schizophrenia` |
| baseline | `mmlu_4964` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4965` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4966` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4967` | `mcq` | true | `D` | `D. brain plasticity` |
| baseline | `mmlu_4968` | `mcq` | true | `C` | `C. Triadic` |
| baseline | `mmlu_4969` | `mcq` | true | `D` | `D. humanistic` |
| baseline | `mmlu_4970` | `mcq` | true | `A` | `A. generalization` |
| baseline | `mmlu_4971` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4972` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4973` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4974` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4975` | `mcq` | false | `B` | `A. 9` |
| baseline | `mmlu_4976` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4977` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4978` | `mcq` | true | `B` | `B. long-term potentiation` |
| baseline | `mmlu_4979` | `mcq` | false | `C` | `A. sensation and perception` |
| baseline | `mmlu_4980` | `mcq` | true | `D` | `D. Establishing rapport to better understand the child's perspective on a problem` |
| baseline | `mmlu_4981` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4982` | `mcq` | true | `D` | `D. post-traumatic stress disorder` |
| baseline | `mmlu_4983` | `mcq` | true | `B` | `B. hypothalamus` |
| baseline | `mmlu_4984` | `mcq` | true | `A` | `A. MMPI-2` |
| baseline | `mmlu_4985` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4986` | `mcq` | true | `D` | `D. Melatonin` |
| baseline | `mmlu_4987` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4988` | `mcq` | true | `D` | `D. hearing voices that are not actually there` |
| baseline | `mmlu_4989` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4990` | `mcq` | true | `A` | `A. naturalistic` |
| baseline | `mmlu_4991` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4992` | `mcq` | true | `B` | `B. Preoperational` |
| baseline | `mmlu_4993` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4994` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4995` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4996` | `mcq` | true | `D` | `D. Mania` |
| baseline | `mmlu_4997` | `mcq` | true | `D` | `D. nightmare` |
| baseline | `mmlu_4998` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4999` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5000` | `mcq` | true | `C` | `C. shape constancy` |
| baseline | `mmlu_5001` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5002` | `mcq` | false | `C` | `A. engage in risky behavior.` |
| baseline | `mmlu_5003` | `mcq` | true | `A` | `A. Tip-of-the-Tongue Phenomenon` |
| baseline | `mmlu_5004` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5005` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5006` | `mcq` | true | `D` | `D. language acquisition device` |
| baseline | `mmlu_5007` | `mcq` | true | `C` | `C. Ecological` |
| baseline | `mmlu_5008` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5009` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5010` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5011` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5012` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5013` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5014` | `mcq` | true | `B` | `B. standardized` |
| baseline | `mmlu_5015` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5016` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5017` | `mcq` | true | `C` | `C. Pairing an unconditioned stimulus with a conditioned stimulus` |
| baseline | `mmlu_5018` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5019` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_5020` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5021` | `mcq` | true | `B` | `B. hindbrain and midbrain.` |
| baseline | `mmlu_5022` | `mcq` | true | `D` | `D. linear perspective` |
| baseline | `mmlu_5023` | `mcq` | true | `D` | `D. difference threshold` |
| baseline | `mmlu_5024` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5025` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5026` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5027` | `mcq` | true | `A` | `A. endorphins` |
| baseline | `mmlu_5028` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5029` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5030` | `mcq` | false | `C` | `B. MRI` |
| baseline | `mmlu_5031` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5032` | `mcq` | true | `D` | `D. median` |
| baseline | `mmlu_5033` | `mcq` | true | `D` | `D. morphemes` |
| baseline | `mmlu_5034` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5035` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5036` | `mcq` | false | `D` | `C. variable ratio` |
| baseline | `mmlu_5037` | `mcq` | true | `A` | `A. expectation` |
| baseline | `mmlu_5038` | `mcq` | true | `B` | `B. sublimation` |
| baseline | `mmlu_5039` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5040` | `mcq` | true | `D` | `D. linear perspective` |
| baseline | `mmlu_5041` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5042` | `mcq` | false | `C` | `A.	object permanence` |
| baseline | `mmlu_5043` | `mcq` | true | `D` | `D. Maintenance rehearsal` |
| baseline | `mmlu_5044` | `mcq` | true | `D` | `D. hypothalamus` |
| baseline | `mmlu_5045` | `mcq` | false | `A` | `D. lists 3 and 4 only` |
| baseline | `mmlu_5046` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5047` | `mcq` | true | `C` | `C. balance` |
| baseline | `mmlu_5048` | `mcq` | true | `A` | `A. superordinate goals` |
| baseline | `mmlu_5049` | `mcq` | true | `B` | `B. negative punishment` |
| baseline | `mmlu_5050` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5051` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5052` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5053` | `mcq` | false | `B` | `C. James-Lange theory` |
| baseline | `mmlu_5054` | `mcq` | true | `B` | `B. Preoperational` |
| baseline | `mmlu_5055` | `mcq` | true | `C` | `C. Projection` |
| baseline | `mmlu_5056` | `mcq` | false | `D` | `A. Bias` |
| baseline | `mmlu_5057` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5058` | `mcq` | true | `A` | `A. Schizophrenia` |
| baseline | `mmlu_5059` | `mcq` | true | `C` | `C. hypothalamus` |
| baseline | `mmlu_5060` | `mcq` | true | `C` | `C. shaping.` |
| baseline | `mmlu_5061` | `mcq` | true | `A` | `A. amplitude of the wave` |
| baseline | `mmlu_5062` | `mcq` | true | `C` | `C. pituitary gland` |
| baseline | `mmlu_5063` | `mcq` | true | `D` | `D. psychoanalytic` |
| baseline | `mmlu_5064` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5065` | `mcq` | true | `D` | `D. major depressive disorder.` |
| baseline | `mmlu_5066` | `mcq` | true | `A` | `A. talking to a patient` |
| baseline | `mmlu_5067` | `mcq` | true | `B` | `B. acquisition` |
| baseline | `mmlu_5068` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5069` | `mcq` | true | `D` | `D. proximity` |
| baseline | `mmlu_5070` | `mcq` | true | `D` | `D. in-group bias` |
| baseline | `mmlu_5071` | `mcq` | true | `A` | `A. Selye's general adaptation syndrome` |
| baseline | `mmlu_5072` | `mcq` | true | `A` | `A. elevate mood and reduce pain` |
| baseline | `mmlu_5073` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5074` | `mcq` | false | `B` | `D. Alliance formation` |
| baseline | `mmlu_5075` | `mcq` | true | `B` | `B. satisfying needs from the next step in the hierarchy` |
| baseline | `mmlu_5076` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5077` | `mcq` | false | `C` | `D. sex` |
| baseline | `mmlu_5078` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5079` | `mcq` | false | `D` | `B. generalization.` |
| baseline | `mmlu_5080` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5081` | `mcq` | true | `B` | `B. Cognitive` |
| baseline | `mmlu_5082` | `mcq` | true | `C` | `C. uncon` |
| baseline | `mmlu_5083` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_5084` | `mcq` | true | `A` | `A. traits` |
| baseline | `mmlu_5085` | `mcq` | true | `C` | `C. Broca's area` |
| baseline | `mmlu_5086` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5087` | `mcq` | true | `C` | `C. REM sleep` |
| baseline | `mmlu_5088` | `mcq` | true | `A` | `A. humanistic` |
| baseline | `mmlu_5089` | `mcq` | true | `D` | `D. experiencing a physical problem without a physical cause` |
| baseline | `mmlu_5090` | `mcq` | true | `C` | `C. unconditional positive regard` |
| baseline | `mmlu_5091` | `mcq` | true | `B` | `B. Increase the speed with which messages can be transmitted` |
| baseline | `mmlu_5092` | `mcq` | true | `C` | `C. Inter-rater reliability` |
| baseline | `mmlu_5093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5094` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5095` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5096` | `mcq` | true | `A` | `A. the representativeness heuristic and the availability heuristic` |
| baseline | `mmlu_5097` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5098` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5099` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5100` | `mcq` | true | `D` | `D. denial` |
| baseline | `mmlu_5101` | `mcq` | false | `A` | `D. association areas` |
| baseline | `mmlu_5102` | `mcq` | true | `C` | `C. reinforced` |
| baseline | `mmlu_5103` | `mcq` | false | `A` | `C. sense of time urgency` |
| baseline | `mmlu_5104` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5105` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5106` | `mcq` | true | `B` | `B. white` |
| baseline | `mmlu_5107` | `mcq` | true | `D` | `D. Dopamine` |
| baseline | `mmlu_5108` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5109` | `mcq` | true | `D` | `D. generalization` |
| baseline | `mmlu_5110` | `mcq` | false | `C` | `A. Bob ate a snack.` |
| baseline | `mmlu_5111` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5112` | `mcq` | false | `D` | `C. touch.` |
| baseline | `mmlu_5113` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5114` | `mcq` | true | `C` | `C. thalamus` |
| baseline | `mmlu_5115` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5116` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5117` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5118` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5119` | `mcq` | true | `D` | `D. separation anxiety` |
| baseline | `mmlu_5120` | `mcq` | true | `B` | `B. confirmation bias` |
| baseline | `mmlu_5121` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5122` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5123` | `mcq` | true | `C` | `C. Attribution theory` |
| baseline | `mmlu_5124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5125` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5126` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5127` | `mcq` | false | `C` | `A. black` |
| baseline | `mmlu_5128` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5129` | `mcq` | false | `B` | `D. 1 in 10,000.` |
| baseline | `mmlu_5130` | `mcq` | false | `A` | `B. simultaneous` |
| baseline | `mmlu_5131` | `mcq` | true | `A` | `A. GAD.` |
| baseline | `mmlu_5132` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5133` | `mcq` | false | `B` | `A. recognition` |
| baseline | `mmlu_5134` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5135` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5136` | `mcq` | true | `C` | `C. Shaping` |
| baseline | `mmlu_5137` | `mcq` | true | `C` | `C. closure` |
| baseline | `mmlu_5138` | `mcq` | true | `B` | `B. inferential statistics` |
| baseline | `mmlu_5139` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5140` | `mcq` | true | `D` | `D. more neurons firing more frequently` |
| baseline | `mmlu_5141` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5142` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5143` | `mcq` | true | `D` | `D. risk of psychological harm` |
| baseline | `mmlu_5144` | `mcq` | true | `A` | `A. -1` |
| baseline | `mmlu_5145` | `mcq` | true | `B` | `B. cerebral cortex` |
| baseline | `mmlu_5146` | `mcq` | false | `D` | `B. Variable ratio schedules of reinforcements produce results more quickly.` |
| baseline | `mmlu_5147` | `mcq` | true | `A` | `A. serotonin` |
| baseline | `mmlu_5148` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5149` | `mcq` | true | `D` | `D. collective unconscious` |
| baseline | `mmlu_5150` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5151` | `mcq` | true | `D` | `D. chemotherapy` |
| baseline | `mmlu_5152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5153` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5154` | `mcq` | true | `C` | `C. hypothalamus` |
| baseline | `mmlu_5155` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5156` | `mcq` | false | `B` | `A. alcohol abuse` |
| baseline | `mmlu_5157` | `mcq` | false | `C` | `A. Variable-ratio` |
| baseline | `mmlu_5158` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5159` | `mcq` | true | `D` | `D. Meta-analysis` |
| baseline | `mmlu_5160` | `mcq` | true | `D` | `D. modeling` |
| baseline | `mmlu_5161` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5162` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5163` | `mcq` | true | `C` | `C. compliance strategy` |
| baseline | `mmlu_5164` | `mcq` | true | `D` | `D. rational emotive` |
| baseline | `mmlu_5165` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5166` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5167` | `mcq` | false | `D` | `B. yellow` |
| baseline | `mmlu_5168` | `mcq` | true | `D` | `D. superego` |
| baseline | `mmlu_5169` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5170` | `mcq` | true | `D` | `D. incentive` |
| baseline | `mmlu_5171` | `mcq` | true | `B` | `B. Visual imagery` |
| baseline | `mmlu_5172` | `mcq` | false | `B` | `A. Caring for one's children` |
| baseline | `mmlu_5173` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5174` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5175` | `mcq` | false | `C` | `B. behavior therapy` |
| baseline | `mmlu_5176` | `mcq` | true | `A` | `A. above average` |
| baseline | `mmlu_5177` | `mcq` | true | `B` | `B. selective attention` |
| baseline | `mmlu_5178` | `mcq` | true | `D` | `D.traits, the environment, and behavior` |
| baseline | `mmlu_5179` | `mcq` | true | `D` | `D. prefrontal cortex` |
| baseline | `mmlu_5180` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5181` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5182` | `mcq` | true | `A` | `A. The parasympathetic nervous system resumes control and reverses the sympathetic responses.` |
| baseline | `mmlu_5183` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5184` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5185` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5186` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5187` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5188` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5189` | `mcq` | true | `D` | `D. learning` |
| baseline | `mmlu_5190` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5191` | `mcq` | true | `D` | `D. Hallucinations` |
| baseline | `mmlu_5192` | `mcq` | true | `A` | `A. humanistic` |
| baseline | `mmlu_5193` | `mcq` | true | `C` | `C. Developmental psychologists` |
| baseline | `mmlu_5194` | `mcq` | true | `B` | `B. depressive` |
| baseline | `mmlu_5195` | `mcq` | true | `D` | `D. 60` |
| baseline | `mmlu_5196` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5197` | `mcq` | true | `A` | `A. cognitive dissonance` |
| baseline | `mmlu_5198` | `mcq` | true | `D` | `D. major depressive disorder` |
| baseline | `mmlu_5199` | `mcq` | true | `B` | `B. groupthink` |
| baseline | `mmlu_5200` | `mcq` | true | `D` | `D. attachment` |
| baseline | `mmlu_5201` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5202` | `mcq` | true | `D` | `D. chunking` |
| baseline | `mmlu_5203` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5204` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5205` | `mcq` | true | `C` | `C. leading questions` |
| baseline | `mmlu_5206` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5207` | `mcq` | true | `B` | `B. reflex` |
| baseline | `mmlu_5208` | `mcq` | true | `C` | `C. Catharsis hypothesis` |
| baseline | `mmlu_5209` | `mcq` | false | `A` | `B. Rorschach inkblot test` |
| baseline | `mmlu_5210` | `mcq` | true | `B` | `B. recalling the name of your junior high school shop teacher` |
| baseline | `mmlu_5211` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5212` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5213` | `mcq` | true | `D` | `D. sensory memory` |
| baseline | `mmlu_5214` | `mcq` | true | `D` | `D. trait` |
| baseline | `mmlu_5215` | `mcq` | true | `B` | `B. dopamine` |
| baseline | `mmlu_5216` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5217` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5218` | `mcq` | true | `A` | `A. the color of the paper` |
| baseline | `mmlu_5219` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5220` | `mcq` | true | `C` | `C. set point theory` |
| baseline | `mmlu_5221` | `mcq` | true | `D` | `D. approach-approach` |
| baseline | `mmlu_5222` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5223` | `mcq` | true | `A` | `A. Duty to warn and protect` |
| baseline | `mmlu_5224` | `mcq` | false | `D` | `A. opponent-process theory` |
| baseline | `mmlu_5225` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5226` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5227` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5228` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5229` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5230` | `mcq` | true | `D` | `D. cones` |
| baseline | `mmlu_5231` | `mcq` | false | `D` | `A. the synapse` |
| baseline | `mmlu_5232` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5233` | `mcq` | false | `A` | `D. Love` |
| baseline | `mmlu_5234` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5235` | `mcq` | true | `D` | `D. Authoritative` |
| baseline | `mmlu_5236` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5237` | `mcq` | true | `B` | `B. double blind study` |
| baseline | `mmlu_5238` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5239` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5240` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5241` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5242` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5243` | `mcq` | true | `D` | `D. Difference threshold` |
| baseline | `mmlu_5244` | `mcq` | true | `D` | `D. Systems approach` |
| baseline | `mmlu_5245` | `mcq` | true | `B` | `B. Experiments isolate the effects of independent variables on dependent variables.` |
| baseline | `mmlu_5246` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5247` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5248` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5249` | `mcq` | false | `B` | `A. Median` |
| baseline | `mmlu_5250` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5251` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5252` | `mcq` | true | `C` | `C. Homeostasis` |
| baseline | `mmlu_5253` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5254` | `mcq` | false | `B` | `A. primary` |
| baseline | `mmlu_5255` | `mcq` | true | `B` | `B. "It's the law."` |
| baseline | `mmlu_5256` | `mcq` | true | `D` | `D. agoraphobia` |
| baseline | `mmlu_5257` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5258` | `mcq` | true | `A` | `A. psychoanalysis` |
| baseline | `mmlu_5259` | `mcq` | true | `B` | `B. crystallized intelligence` |
| baseline | `mmlu_5260` | `mcq` | true | `C` | `C. cognitive dissonance` |
| baseline | `mmlu_5261` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5262` | `mcq` | true | `A` | `A. self-efficacy` |
| baseline | `mmlu_5263` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5264` | `mcq` | true | `D` | `D./aptitude	test.` |
| baseline | `mmlu_5265` | `mcq` | true | `B` | `B. four legs and a seat.` |
| baseline | `mmlu_5266` | `mcq` | true | `D` | `D. left temporal` |
| baseline | `mmlu_5267` | `mcq` | true | `B` | `B. semantic memory` |
| baseline | `mmlu_5268` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5269` | `mcq` | true | `D` | `D. License` |
| baseline | `mmlu_5270` | `mcq` | true | `A` | `A. naturalistic observation` |
| baseline | `mmlu_5271` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5272` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5273` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5274` | `mcq` | false | `C` | `A. United States of America` |
| baseline | `mmlu_5275` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5276` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5277` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5278` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5279` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5281` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5282` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5283` | `mcq` | true | `B` | `B. semantic memory` |
| baseline | `mmlu_5284` | `mcq` | true | `B` | `B. facial expressions` |
| baseline | `mmlu_5285` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5286` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5287` | `mcq` | true | `B` | `B. trait` |
| baseline | `mmlu_5288` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5289` | `mcq` | true | `A` | `A. cell body` |
| baseline | `mmlu_5290` | `mcq` | true | `B` | `B. Alzheimer's disease` |
| baseline | `mmlu_5291` | `mcq` | false | `D` | `B. MRI` |
| baseline | `mmlu_5292` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5293` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5294` | `mcq` | true | `B` | `B. a compulsion` |
| baseline | `mmlu_5295` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5296` | `mcq` | true | `D` | `D. thalamus` |
| baseline | `mmlu_5297` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5298` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5299` | `mcq` | true | `D` | `D. group polarization` |
| baseline | `mmlu_5300` | `mcq` | true | `D` | `D. intrinsic motivation` |
| baseline | `mmlu_5301` | `mcq` | true | `B` | `B. external validity` |
| baseline | `mmlu_5302` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5303` | `mcq` | true | `D` | `D. morpheme` |
| baseline | `mmlu_5304` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5305` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5306` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5307` | `mcq` | true | `B` | `B. systematic desensitization` |
| baseline | `mmlu_5308` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5309` | `mcq` | true | `D` | `D. Sensory adaptation` |
| baseline | `mmlu_5310` | `mcq` | true | `C` | `C. Hormones released in the womb` |
| baseline | `mmlu_5311` | `mcq` | false | `D` | `C. id` |
| baseline | `mmlu_5312` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5313` | `mcq` | true | `B` | `B. sympathetic nervous system` |
| baseline | `mmlu_5314` | `mcq` | true | `A` | `A. acetylcholine` |
| baseline | `mmlu_5315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5316` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5317` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5318` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5319` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5320` | `mcq` | true | `B` | `B. modeling.` |
| baseline | `mmlu_5321` | `mcq` | true | `C` | `C. median` |
| baseline | `mmlu_5322` | `mcq` | true | `B` | `B. inductive reasoning` |
| baseline | `mmlu_5323` | `mcq` | true | `A` | `A. the Big Five` |
| baseline | `mmlu_5324` | `mcq` | true | `D` | `D. environments` |
| baseline | `mmlu_5325` | `mcq` | true | `A` | `A. constructing reality out of their own experiences` |
| baseline | `mmlu_5326` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5327` | `mcq` | true | `C` | `C. identify the origin of a sound.` |
| baseline | `mmlu_5328` | `mcq` | true | `D` | `D. Diffusion of responsibility` |
| baseline | `mmlu_5329` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5330` | `mcq` | false | `A` | `D. left cerebral cortex` |
| baseline | `mmlu_5331` | `mcq` | false | `D` | `A. frequency` |
| baseline | `mmlu_5332` | `mcq` | true | `D` | `D. Gender` |
| baseline | `mmlu_5333` | `mcq` | false | `D` | `B. negative reinforcement` |
| baseline | `mmlu_5334` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5335` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5336` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5337` | `mcq` | false | `B` | `A. case study` |
| baseline | `mmlu_5338` | `mcq` | true | `B` | `B. random sampling` |
| baseline | `mmlu_5339` | `mcq` | true | `A` | `A. delay between the CS and the UCS is too long` |
| baseline | `mmlu_5340` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5341` | `mcq` | true | `A` | `A. nomothetic` |
| baseline | `mmlu_5342` | `mcq` | true | `B` | `B. the mind-body problem` |
| baseline | `mmlu_5343` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5344` | `mcq` | true | `D` | `D. Providing acceleration for gifted students, especially within the areas of their interests and skills.` |
| baseline | `mmlu_5345` | `mcq` | true | `D` | `D. sight` |
| baseline | `mmlu_5346` | `mcq` | true | `C` | `C. place` |
| baseline | `mmlu_5347` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5348` | `mcq` | true | `A` | `A. relative deprivation` |
| baseline | `mmlu_5349` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5350` | `mcq` | false | `B` | `A. difference threshold` |
| baseline | `mmlu_5351` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5352` | `mcq` | true | `D` | `D. The retina` |
| baseline | `mmlu_5353` | `mcq` | true | `C` | `C. Broca's area` |
| baseline | `mmlu_5354` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5355` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5356` | `mcq` | true | `B` | `B. psychiatrist` |
| baseline | `mmlu_5357` | `mcq` | true | `D` | `D. reflex` |
| baseline | `mmlu_5358` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5359` | `mcq` | true | `A` | `A. receptor, afferent neuron, interneuron, efferent neuron, effector` |
| baseline | `mmlu_5360` | `mcq` | true | `A` | `A. Jim and Tim will have very similar IQs.` |
| baseline | `mmlu_5361` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5362` | `mcq` | true | `B` | `B. DSM-5` |
| baseline | `mmlu_5363` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5364` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5365` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5366` | `mcq` | true | `D` | `D. correlation` |
| baseline | `mmlu_5367` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5368` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5369` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5370` | `mcq` | true | `C` | `C. flashbulb memory` |
| baseline | `mmlu_5371` | `mcq` | false | `C` | `A. behavioral` |
| baseline | `mmlu_5372` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5373` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5374` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5376` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5378` | `mcq` | true | `D` | `D. Anthropologists` |
| baseline | `mmlu_5379` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5380` | `mcq` | true | `C` | `C. Down syndrome` |
| baseline | `mmlu_5381` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5382` | `mcq` | true | `D` | `D. dissociative disorder` |
| baseline | `mmlu_5383` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5384` | `mcq` | false | `C` | `A. frequency` |
| baseline | `mmlu_5385` | `mcq` | false | `C` | `B. 3 months` |
| baseline | `mmlu_5386` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5387` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5388` | `mcq` | true | `B` | `B. optic chiasm.` |
| baseline | `mmlu_5389` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5390` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5391` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5392` | `mcq` | true | `B` | `B. inferential statistics` |
| baseline | `mmlu_5393` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5394` | `mcq` | true | `D` | `D. Sleep apnea` |
| baseline | `mmlu_5395` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5396` | `mcq` | false | `A` | `D. surface processing` |
| baseline | `mmlu_5397` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5398` | `mcq` | true | `A` | `A. Occipital` |
| baseline | `mmlu_5399` | `mcq` | true | `D` | `D. Causes of all mental disorders` |
| baseline | `mmlu_5400` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5401` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5402` | `mcq` | true | `D` | `D. Changes in behavior over time` |
| baseline | `mmlu_5403` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_5404` | `mcq` | true | `D` | `D. Implementing a class-wide behavior management plan, such as a response-cost raffle.` |
| baseline | `mmlu_5405` | `mcq` | true | `C` | `C. industrial/organizational` |
| baseline | `mmlu_5406` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5407` | `mcq` | false | `D` | `C. it is difficult to convince medical professionals that one has a disorder when one does not.` |
| baseline | `mmlu_5408` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5409` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5410` | `mcq` | true | `B` | `B. authoritative` |
| baseline | `mmlu_5411` | `mcq` | true | `C` | `C. phallic stage.` |
| baseline | `mmlu_5412` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5413` | `mcq` | false | `C` | `A. going to lecture classes` |
| baseline | `mmlu_5414` | `mcq` | true | `D` | `D. deindividuation` |
| baseline | `mmlu_5415` | `mcq` | true | `C` | `C. Wundt set up a laboratory and focused on empirical evidence that could be replicated.` |
| baseline | `mmlu_5416` | `mcq` | false | `D` | `C. cold` |
| baseline | `mmlu_5417` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5418` | `mcq` | true | `C` | `C. influencing patients by controlling the consequences of their actions` |
| baseline | `mmlu_5419` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5420` | `mcq` | false | `D` | `B. behavior therapy` |
| baseline | `mmlu_5421` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5422` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5423` | `mcq` | true | `C` | `C. the local community college and distant community colleges` |
| baseline | `mmlu_5424` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5425` | `mcq` | true | `B` | `B. The neural connections to the primary visual cortex are not fully connected.` |
| baseline | `mmlu_5426` | `mcq` | true | `D` | `D. medulla` |
| baseline | `mmlu_5427` | `mcq` | true | `A` | `A. The self-fulfilling prophecy` |
| baseline | `mmlu_5428` | `mcq` | true | `D` | `D. insight` |
| baseline | `mmlu_5429` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5430` | `mcq` | false | `A` | `B. the "wire" mother versus the "cloth" mother` |
| baseline | `mmlu_5431` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5432` | `mcq` | true | `B` | `B. 2P(t > 1.54) with df = 6` |
| baseline | `mmlu_5433` | `mcq` | true | `C` | `C. 25.3 to 44.7 minutes` |
| baseline | `mmlu_5434` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5435` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5436` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5437` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5438` | `mcq` | true | `D` | `D. The probability of a Type I error would stay the same and the power would increase.` |
| baseline | `mmlu_5439` | `mcq` | true | `D` | `D. The woman, because her height is 1.33 standard deviations above the mean height of all women, whereas the man’s heigh` |
| baseline | `mmlu_5440` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5441` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5442` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5443` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5444` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5445` | `mcq` | false | `C` | `D. decreases the interval size by 57%.` |
| baseline | `mmlu_5446` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5447` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_5448` | `mcq` | false | `B` | `D. III only` |
| baseline | `mmlu_5449` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5450` | `mcq` | false | `D` | `B. 0.0016` |
| baseline | `mmlu_5451` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_5452` | `mcq` | true | `D` | `D. –0.21` |
| baseline | `mmlu_5453` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5454` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5455` | `mcq` | false | `B` | `A. -1` |
| baseline | `mmlu_5456` | `mcq` | true | `A` | `A. $23,000` |
| baseline | `mmlu_5457` | `mcq` | false | `D` | `B. $23,700` |
| baseline | `mmlu_5458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5459` | `mcq` | true | `A` | `A. Her procedure makes use of chance.` |
| baseline | `mmlu_5460` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5461` | `mcq` | false | `D` | `A. 1.345 < t< 1.761` |
| baseline | `mmlu_5462` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5463` | `mcq` | false | `D` | `B. 1.96` |
| baseline | `mmlu_5464` | `mcq` | true | `D` | `D. None of the above are appropriate.` |
| baseline | `mmlu_5465` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5466` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5467` | `mcq` | true | `D` | `D. III only` |
| baseline | `mmlu_5468` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5469` | `mcq` | true | `A` | `A. We are 95 percent confident that the proportion of women interested in shopping on Sundays exceeds the proportion of ` |
| baseline | `mmlu_5470` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5471` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5472` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5473` | `mcq` | false | `D` | `B. 100` |
| baseline | `mmlu_5474` | `mcq` | true | `A` | `A. It is likely that the true proportion of high school students afraid to go to school is between 38% and 48%.` |
| baseline | `mmlu_5475` | `mcq` | false | `A` | `B. Sample survey` |
| baseline | `mmlu_5476` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5477` | `mcq` | false | `B` | `A. Plan I` |
| baseline | `mmlu_5478` | `mcq` | true | `B` | `B. because a sample statistic is used to estimate a population parameter.` |
| baseline | `mmlu_5479` | `mcq` | false | `C` | `A. I and III only` |
| baseline | `mmlu_5480` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5481` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5482` | `mcq` | true | `D` | `D. The population of SAT scores from each group is normally distributed.` |
| baseline | `mmlu_5483` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5484` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5485` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5486` | `mcq` | true | `D` | `D. None of the above can affect the r value.` |
| baseline | `mmlu_5487` | `mcq` | false | `D` | `C. It multiples the interval size by 1.732.` |
| baseline | `mmlu_5488` | `mcq` | true | `A` | `A. 0.19` |
| baseline | `mmlu_5489` | `mcq` | false | `D` | `A. z = 0.04` |
| baseline | `mmlu_5490` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5491` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5492` | `mcq` | true | `C` | `C. 86.65; she qualifies.` |
| baseline | `mmlu_5493` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5494` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_5495` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5496` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5497` | `mcq` | true | `D` | `D. The population of the sales records at each location is normally distributed.` |
| baseline | `mmlu_5498` | `mcq` | true | `B` | `B. 0.40` |
| baseline | `mmlu_5499` | `mcq` | false | `B` | `A. μ = 3.677, σ = 3.561` |
| baseline | `mmlu_5500` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5501` | `mcq` | false | `B` | `C. I and III` |
| baseline | `mmlu_5502` | `mcq` | true | `C` | `C. Use of a confounding variable to control the placebo effect` |
| baseline | `mmlu_5503` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5504` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5505` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5506` | `mcq` | false | `D` | `B. 5.290 pounds` |
| baseline | `mmlu_5507` | `mcq` | true | `B` | `B. The distribution of the sample proportion will be less spread out.` |
| baseline | `mmlu_5508` | `mcq` | false | `D` | `B. 8.0%` |
| baseline | `mmlu_5509` | `mcq` | false | `C` | `B. 67 pounds` |
| baseline | `mmlu_5510` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5512` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5513` | `mcq` | false | `C` | `B. 17.1%` |
| baseline | `mmlu_5514` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5515` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5516` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5517` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5518` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5519` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5521` | `mcq` | false | `C` | `B. An unnecessary stoppage of the production process` |
| baseline | `mmlu_5522` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_5523` | `mcq` | true | `D` | `D. None of the above are true statements.` |
| baseline | `mmlu_5524` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5525` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5526` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5527` | `mcq` | false | `D` | `B. The correlation coefficient is 0.71.` |
| baseline | `mmlu_5528` | `mcq` | true | `D` | `D. No, because not every group of 30 employees has the same chance of being selected.` |
| baseline | `mmlu_5529` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5530` | `mcq` | true | `C` | `C. Selection bias makes this a poorly designed survey.` |
| baseline | `mmlu_5531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5532` | `mcq` | false | `D` | `A. 0.313` |
| baseline | `mmlu_5533` | `mcq` | true | `A` | `A. 6` |
| baseline | `mmlu_5534` | `mcq` | false | `C` | `B. 53 minutes to 281 minutes` |
| baseline | `mmlu_5535` | `mcq` | true | `B` | `B. Her grade will go up by 20.4 points.` |
| baseline | `mmlu_5536` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5537` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5538` | `mcq` | true | `A` | `A. by blocking on exercise intensity` |
| baseline | `mmlu_5539` | `mcq` | false | `C` | `B. 18%` |
| baseline | `mmlu_5540` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5541` | `mcq` | true | `D` | `D. Follow up with those that did not return the survey to encourage them to respond.` |
| baseline | `mmlu_5542` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5543` | `mcq` | true | `A` | `A. 0.235` |
| baseline | `mmlu_5544` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5545` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5546` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5547` | `mcq` | true | `D` | `D. The answer cannot be determined without knowing the size of the jury pool.` |
| baseline | `mmlu_5548` | `mcq` | false | `D` | `B. 144` |
| baseline | `mmlu_5549` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5550` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5551` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5552` | `mcq` | true | `C` | `C. For both companies, the probability that a fuse will last at least 1 hour is 0.159` |
| baseline | `mmlu_5553` | `mcq` | true | `D` | `D. We are 90% confident that the difference in proportions between Toyota and Subaru car owners who are satisfied with t` |
| baseline | `mmlu_5554` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5555` | `mcq` | true | `C` | `C. The number of successes and the number of failures for the two groups are not all large enough.` |
| baseline | `mmlu_5556` | `mcq` | false | `B` | `C. 12 - 2.576(0.3) ounces` |
| baseline | `mmlu_5557` | `mcq` | false | `D` | `A. 66.80%` |
| baseline | `mmlu_5558` | `mcq` | false | `D` | `B. 0.1667` |
| baseline | `mmlu_5559` | `mcq` | true | `D` | `D. The player will lose about $1.44.` |
| baseline | `mmlu_5560` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5561` | `mcq` | false | `D` | `B. 0.34` |
| baseline | `mmlu_5562` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5563` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5564` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5565` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5566` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5567` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5568` | `mcq` | true | `B` | `B. Because tis less extreme than the critical value of t for 17 degrees of freedom, he should not reject the null hypoth` |
| baseline | `mmlu_5569` | `mcq` | true | `B` | `B. All county residents` |
| baseline | `mmlu_5570` | `mcq` | true | `D` | `D. No, because not every sample of the intended size has an equal chance of being selected.` |
| baseline | `mmlu_5571` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5572` | `mcq` | false | `D` | `A. 0.42` |
| baseline | `mmlu_5573` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5574` | `mcq` | false | `C` | `B. Dialysis center: Type I error, towel manufacturer: Type II error` |
| baseline | `mmlu_5575` | `mcq` | false | `A` | `B. Cluster sample, because the population is divided into five clusters—namely, five offices in five different countries` |
| baseline | `mmlu_5576` | `mcq` | false | `D` | `C. 0.8` |
| baseline | `mmlu_5577` | `mcq` | true | `D` | `D. The median of all the salaries.` |
| baseline | `mmlu_5578` | `mcq` | true | `D` | `D. No, because the entire population information was used from both offices. Because no samples were taken, a t-test sho` |
| baseline | `mmlu_5579` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5580` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5581` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5582` | `mcq` | true | `C` | `C. P(t > 2) with 15 degrees of freedom` |
| baseline | `mmlu_5583` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5584` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5585` | `mcq` | false | `C` | `B. μ = 15,100; σ = 6200` |
| baseline | `mmlu_5586` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5587` | `mcq` | false | `D` | `C. 118 points` |
| baseline | `mmlu_5588` | `mcq` | true | `C` | `C. if n is large, no matter what the distribution of the original population.` |
| baseline | `mmlu_5589` | `mcq` | false | `B` | `D. All of the above are valid conclusions.` |
| baseline | `mmlu_5590` | `mcq` | false | `B` | `A. $6,984` |
| baseline | `mmlu_5591` | `mcq` | false | `C` | `A. 8.05` |
| baseline | `mmlu_5592` | `mcq` | true | `D` | `D. An experiment` |
| baseline | `mmlu_5593` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5594` | `mcq` | false | `B` | `A. 0.78` |
| baseline | `mmlu_5595` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5596` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5597` | `mcq` | true | `D` | `D. 0.74` |
| baseline | `mmlu_5598` | `mcq` | true | `D` | `D. Interquartile range` |
| baseline | `mmlu_5599` | `mcq` | false | `C` | `B. reduce confounding.` |
| baseline | `mmlu_5600` | `mcq` | false | `B` | `D. Independent samples comparison of population means` |
| baseline | `mmlu_5601` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5602` | `mcq` | true | `A` | `A. 0.0057` |
| baseline | `mmlu_5603` | `mcq` | true | `C` | `C. Stratified sample` |
| baseline | `mmlu_5604` | `mcq` | false | `D` | `A. 0.07` |
| baseline | `mmlu_5605` | `mcq` | false | `C` | `A. 1536` |
| baseline | `mmlu_5606` | `mcq` | true | `B` | `B. The sample mean and sample median are equal.` |
| baseline | `mmlu_5607` | `mcq` | true | `A` | `A. (3,034, 3,466)` |
| baseline | `mmlu_5608` | `mcq` | false | `D` | `B. 0.540` |
| baseline | `mmlu_5609` | `mcq` | false | `A` | `C. Closing the park when the lead levels are in excess of the allowed limit` |
| baseline | `mmlu_5610` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5611` | `mcq` | false | `C` | `B. 603.8` |
| baseline | `mmlu_5612` | `mcq` | false | `B` | `A. It will remain the same.` |
| baseline | `mmlu_5613` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5614` | `mcq` | false | `B` | `A. 42.2 g` |
| baseline | `mmlu_5615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5616` | `mcq` | true | `D` | `D. There is insufficient information to answer this question.` |
| baseline | `mmlu_5617` | `mcq` | true | `D` | `D. We should be 90% confident that the difference in life expectancies is between 6 and 12 years.` |
| baseline | `mmlu_5618` | `mcq` | true | `B` | `B. 0.4096` |
| baseline | `mmlu_5619` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5620` | `mcq` | false | `C` | `B. 0.0112` |
| baseline | `mmlu_5621` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5622` | `mcq` | true | `C` | `C. Too high, because of undercoverage bias.` |
| baseline | `mmlu_5623` | `mcq` | false | `A` | `B. Standard deviation` |
| baseline | `mmlu_5624` | `mcq` | false | `C` | `A. Use the 88 who did respond, using 88 as the sample size in the analysis.` |
| baseline | `mmlu_5625` | `mcq` | false | `D` | `A. 0.44, 0.5, 0.2` |
| baseline | `mmlu_5626` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5627` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5628` | `mcq` | false | `D` | `A. -0.65` |
| baseline | `mmlu_5629` | `mcq` | false | `D` | `B. 17.8%` |
| baseline | `mmlu_5630` | `mcq` | true | `B` | `B. 0.1446` |
| baseline | `mmlu_5631` | `mcq` | true | `A` | `A. P(A and B) = P(A) · P(B)` |
| baseline | `mmlu_5632` | `mcq` | false | `A` | `B. An experiment, thus making cause and effect a reasonable conclusion` |
| baseline | `mmlu_5633` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5634` | `mcq` | false | `D` | `B. $91` |
| baseline | `mmlu_5635` | `mcq` | true | `D` | `D. 9% of the variability in job satisfaction can be explained by the linear model with self-efficacy as a predictor.` |
| baseline | `mmlu_5636` | `mcq` | true | `D` | `D. There is insufficient information to answer this question.` |
| baseline | `mmlu_5637` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5638` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5639` | `mcq` | false | `A` | `B. I and III only` |
| baseline | `mmlu_5640` | `mcq` | false | `D` | `B. 64` |
| baseline | `mmlu_5641` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_5642` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_5643` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5644` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5645` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5646` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5647` | `mcq` | true | `D` | `D. Influential point` |
| baseline | `mmlu_5648` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5649` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5650` | `mcq` | true | `D` | `D. Reconstruction` |
| baseline | `mmlu_5651` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5652` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5653` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5654` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5655` | `mcq` | true | `A` | `A. The Social Gospel` |
| baseline | `mmlu_5656` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5657` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5658` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5659` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5660` | `mcq` | false | `A` | `C. all Christians only` |
| baseline | `mmlu_5661` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5662` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5663` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5664` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5665` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5666` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5668` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5669` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5670` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5671` | `mcq` | true | `B` | `B. Containment` |
| baseline | `mmlu_5672` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5674` | `mcq` | true | `D` | `D. Improve conditions in urban neighborhoods` |
| baseline | `mmlu_5675` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5676` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5679` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5680` | `mcq` | true | `A` | `A. The Nineteenth Amendment.` |
| baseline | `mmlu_5681` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5682` | `mcq` | true | `C` | `C. Greater rights for unions` |
| baseline | `mmlu_5683` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5684` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5685` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5686` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5688` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5689` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5690` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5691` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5692` | `mcq` | true | `C` | `C. William M. Tweed` |
| baseline | `mmlu_5693` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5694` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5695` | `mcq` | true | `C` | `C. Progressive Liberals` |
| baseline | `mmlu_5696` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5697` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5698` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5699` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5700` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5702` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5703` | `mcq` | true | `C` | `C. still an underdeveloped cultural backwater` |
| baseline | `mmlu_5704` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5705` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5706` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5707` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5708` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5709` | `mcq` | true | `C` | `C. Plessy v. Ferguson` |
| baseline | `mmlu_5710` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5711` | `mcq` | true | `A` | `A. The bombing of Pearl Harbor` |
| baseline | `mmlu_5712` | `mcq` | true | `B` | `B. Government efforts to prevent the publication of the Pentagon Papers in 1971` |
| baseline | `mmlu_5713` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5714` | `mcq` | true | `C` | `C. The USA Patriot Act of 2001` |
| baseline | `mmlu_5715` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5716` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5717` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5718` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5719` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5721` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5722` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5723` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5724` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5725` | `mcq` | true | `D` | `D. New Dealers of the 1930s` |
| baseline | `mmlu_5726` | `mcq` | true | `D` | `D. Ireland` |
| baseline | `mmlu_5727` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5728` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5729` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5730` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5731` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5732` | `mcq` | true | `C` | `C. U.S. involvement in Vietnam and the civil rights movement` |
| baseline | `mmlu_5733` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5734` | `mcq` | true | `B` | `B. Expanding territories under Spanish control` |
| baseline | `mmlu_5735` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5736` | `mcq` | true | `A` | `A. fishing.` |
| baseline | `mmlu_5737` | `mcq` | true | `C` | `C. they were religious Separatists looking for a place to freely practice their faith.` |
| baseline | `mmlu_5738` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5739` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5740` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5741` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5742` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5743` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5744` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5745` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5746` | `mcq` | false | `A` | `C. The Cold War` |
| baseline | `mmlu_5747` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5748` | `mcq` | true | `C` | `C. Manifest Destiny` |
| baseline | `mmlu_5749` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5750` | `mcq` | true | `C` | `C. Insurgence vs. retreat` |
| baseline | `mmlu_5751` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5752` | `mcq` | true | `D` | `D. Declaration of Independence.` |
| baseline | `mmlu_5753` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5754` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5755` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5756` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5758` | `mcq` | true | `C` | `C. Self-government` |
| baseline | `mmlu_5759` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5760` | `mcq` | true | `C` | `C. middle-class college students.` |
| baseline | `mmlu_5761` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5762` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5763` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5764` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5765` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5766` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5767` | `mcq` | true | `A` | `A. James K. Polk` |
| baseline | `mmlu_5768` | `mcq` | true | `D` | `D. the balanced budget mandate` |
| baseline | `mmlu_5769` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5770` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5771` | `mcq` | true | `C` | `C. Powerful nations have a moral duty to govern less developed nations.` |
| baseline | `mmlu_5772` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5773` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5775` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5776` | `mcq` | false | `B` | `A. violated the Constitutional injunction against bills of attainder.` |
| baseline | `mmlu_5777` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5778` | `mcq` | true | `C` | `C. Increased economic and political opportunities for women` |
| baseline | `mmlu_5779` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5780` | `mcq` | true | `B` | `B. Executive Order 9066 interning Japanese Americans` |
| baseline | `mmlu_5781` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5782` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5783` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5784` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5785` | `mcq` | true | `C` | `C. Spanish-American War` |
| baseline | `mmlu_5786` | `mcq` | true | `C` | `C. Republican motherhood` |
| baseline | `mmlu_5787` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5788` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5789` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5790` | `mcq` | false | `D` | `C. an evolving relationship between the federal government and issues of health and poverty.` |
| baseline | `mmlu_5791` | `mcq` | false | `A` | `B. a flourishing economy and a baby boom had led people to desire greater incomes.` |
| baseline | `mmlu_5792` | `mcq` | true | `D` | `D. The Pure Food and Drug Act` |
| baseline | `mmlu_5793` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5794` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5795` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5796` | `mcq` | true | `B` | `B. immigration quotas` |
| baseline | `mmlu_5797` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5798` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5799` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5800` | `mcq` | true | `B` | `B. The Second Great Awakening.` |
| baseline | `mmlu_5801` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5802` | `mcq` | true | `C` | `C. Theodore Roosevelt` |
| baseline | `mmlu_5803` | `mcq` | false | `A` | `D. Eighteenth century scientific racism` |
| baseline | `mmlu_5804` | `mcq` | false | `A` | `C. Plessy v. Ferguson (1896)` |
| baseline | `mmlu_5805` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5806` | `mcq` | false | `A` | `B. Supportive of the policies of Thomas Jefferson` |
| baseline | `mmlu_5807` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5808` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5809` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5810` | `mcq` | true | `A` | `A. The rise of the United States to the status of a great power` |
| baseline | `mmlu_5811` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5812` | `mcq` | true | `D` | `D. farmers, who hoped that a more generous money supply would ease their debt burdens` |
| baseline | `mmlu_5813` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5814` | `mcq` | true | `C` | `C. The Spanish–American War` |
| baseline | `mmlu_5815` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5816` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5817` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5818` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5819` | `mcq` | false | `B` | `A. Puritanism` |
| baseline | `mmlu_5820` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5821` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5822` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5823` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5824` | `mcq` | true | `C` | `C. Taking advantage of divisions among the Indians` |
| baseline | `mmlu_5825` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5826` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5827` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5828` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5829` | `mcq` | true | `B` | `B. Equal Rights Amendment.` |
| baseline | `mmlu_5830` | `mcq` | true | `A` | `A. The New Deal` |
| baseline | `mmlu_5831` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5832` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5833` | `mcq` | true | `A` | `A. Support for Manifest Destiny` |
| baseline | `mmlu_5834` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5835` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5836` | `mcq` | true | `C` | `C. Quakers` |
| baseline | `mmlu_5837` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5838` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5839` | `mcq` | false | `D` | `B. Respecting Indian territory and sovereignty` |
| baseline | `mmlu_5840` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5841` | `mcq` | true | `A` | `A. Many Southern and Eastern Europeans turned to America for financial gain and political freedom.` |
| baseline | `mmlu_5842` | `mcq` | true | `D` | `D. Plessy v. Ferguson (1896).` |
| baseline | `mmlu_5843` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5844` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5845` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5846` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5847` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5848` | `mcq` | true | `D` | `D. the end of the Cold War.` |
| baseline | `mmlu_5849` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5850` | `mcq` | false | `B` | `D. British impressments of American sailors and interference with American trade` |
| baseline | `mmlu_5851` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5852` | `mcq` | true | `A` | `A. The formation of the non-aligned movement` |
| baseline | `mmlu_5853` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5854` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5855` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5856` | `mcq` | true | `D` | `D. Korea remains divided into two nations near the 38th parallel.` |
| baseline | `mmlu_5857` | `mcq` | true | `C` | `C. Cynical, enthusiastic` |
| baseline | `mmlu_5858` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5859` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5860` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5861` | `mcq` | true | `B` | `B. can be viewed as a reaction to the systemic brute force with which the British governed India.` |
| baseline | `mmlu_5862` | `mcq` | true | `B` | `B. He doesn't earn enough on his own.` |
| baseline | `mmlu_5863` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5864` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5865` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5866` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5867` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5868` | `mcq` | true | `A` | `A. Development of socialized programs throughout much of Europe` |
| baseline | `mmlu_5869` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5870` | `mcq` | true | `B` | `B. The ability of the Tang emperor to project military power on the frontier in order to impose his will.` |
| baseline | `mmlu_5871` | `mcq` | true | `A` | `A. Emphasis on trade networks` |
| baseline | `mmlu_5872` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5873` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5874` | `mcq` | true | `B` | `B. Nonviolent resistance` |
| baseline | `mmlu_5875` | `mcq` | true | `C` | `C. The encomienda system` |
| baseline | `mmlu_5876` | `mcq` | false | `B` | `D. The presence of highly developed port cities` |
| baseline | `mmlu_5877` | `mcq` | false | `A` | `B. The use of religion to justify armed violence` |
| baseline | `mmlu_5878` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5879` | `mcq` | true | `D` | `D. The defeat of Indian rebels and the imposition of direct rule by the British government` |
| baseline | `mmlu_5880` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5881` | `mcq` | true | `D` | `D. apartheid.` |
| baseline | `mmlu_5882` | `mcq` | true | `C` | `C. the Enlightenment` |
| baseline | `mmlu_5883` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5884` | `mcq` | true | `B` | `B. The invasion of Anatolia by the Seljuk Turks` |
| baseline | `mmlu_5885` | `mcq` | false | `B` | `A. Rules of royal succession` |
| baseline | `mmlu_5886` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5887` | `mcq` | false | `B` | `D. State-sponsored campaigns of genocide` |
| baseline | `mmlu_5888` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5889` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5890` | `mcq` | false | `D` | `A. Highlight the extent of the author's property losses` |
| baseline | `mmlu_5891` | `mcq` | true | `D` | `D. Overhunting and depletion of furbearing animals` |
| baseline | `mmlu_5892` | `mcq` | true | `C` | `C. Women's power increasingly fell within the private sphere.` |
| baseline | `mmlu_5893` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5894` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5895` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5896` | `mcq` | true | `D` | `D. Socialism` |
| baseline | `mmlu_5897` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5898` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5899` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5900` | `mcq` | true | `C` | `C. They logically decided to develop weapons better suited to their immediate military needs.` |
| baseline | `mmlu_5901` | `mcq` | false | `C` | `D. The country turned inward and closed its ports to all foreigners.` |
| baseline | `mmlu_5902` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5903` | `mcq` | true | `D` | `D. Hardening of anti-immigrant sentiment` |
| baseline | `mmlu_5904` | `mcq` | true | `D` | `D. Persia was brought into the Arabian orbit over the course of the period.` |
| baseline | `mmlu_5905` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5906` | `mcq` | true | `D` | `D. The Crusades` |
| baseline | `mmlu_5907` | `mcq` | false | `B` | `D. John Wycliffe` |
| baseline | `mmlu_5908` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5909` | `mcq` | true | `C` | `C. Pan-Africanism` |
| baseline | `mmlu_5910` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5911` | `mcq` | true | `D` | `D. Unforeseen consequences of British imperialism` |
| baseline | `mmlu_5912` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5913` | `mcq` | false | `A` | `C. He had lost the blessing of the gods.` |
| baseline | `mmlu_5914` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5915` | `mcq` | true | `C` | `C. A state or secular authority` |
| baseline | `mmlu_5916` | `mcq` | false | `A` | `C. The urban middle class` |
| baseline | `mmlu_5917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5918` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5919` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5920` | `mcq` | false | `A` | `D. The rise of a warrior elite whose deeds were worthy of praise and recording` |
| baseline | `mmlu_5921` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5922` | `mcq` | true | `D` | `D. The New World` |
| baseline | `mmlu_5923` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5924` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5925` | `mcq` | true | `A` | `A. Rulers derived legitimacy for their rule by their sponsorship of religion and chief priests.` |
| baseline | `mmlu_5926` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5927` | `mcq` | true | `C` | `C. European participation in East Asian trade patterns` |
| baseline | `mmlu_5928` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5929` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5930` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5931` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5932` | `mcq` | false | `C` | `D. The political nature of the church` |
| baseline | `mmlu_5933` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5934` | `mcq` | true | `A` | `A. Railroad construction` |
| baseline | `mmlu_5935` | `mcq` | false | `D` | `C. The king's lack of interest in the welfare of Native American subjects` |
| baseline | `mmlu_5936` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5937` | `mcq` | true | `A` | `A. Emerging systems of coerced labor` |
| baseline | `mmlu_5938` | `mcq` | true | `A` | `A. Rigid societal gender roles` |
| baseline | `mmlu_5939` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5940` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5941` | `mcq` | true | `B` | `B. Centralized and state-directed campaigns of modernization` |
| baseline | `mmlu_5942` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5943` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5944` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5945` | `mcq` | false | `A` | `C. The Industrial Revolution` |
| baseline | `mmlu_5946` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5947` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5948` | `mcq` | true | `C` | `C. The establishment of the Tokugawa Shogunate` |
| baseline | `mmlu_5949` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5950` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5951` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5952` | `mcq` | true | `C` | `C. A proposal to increase the standing of Africa in the modern world` |
| baseline | `mmlu_5953` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5954` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5955` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5956` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5957` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5958` | `mcq` | true | `A` | `A. Laissez-faire` |
| baseline | `mmlu_5959` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5960` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5961` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5962` | `mcq` | true | `B` | `B. Unfair systems of taxation` |
| baseline | `mmlu_5963` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5964` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5965` | `mcq` | true | `C` | `C. The end justifies the means` |
| baseline | `mmlu_5966` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5967` | `mcq` | true | `A` | `A. Existentialism` |
| baseline | `mmlu_5968` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5969` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5970` | `mcq` | true | `A` | `A. He is found everywhere and contained in everything.` |
| baseline | `mmlu_5971` | `mcq` | true | `C` | `C. The importance of sacrifice to the gods` |
| baseline | `mmlu_5972` | `mcq` | true | `B` | `B. It was a continuation of a preexisting cultural pattern.` |
| baseline | `mmlu_5973` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5974` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5975` | `mcq` | true | `C` | `C. The use of religion to ponder conceptions of the afterlife` |
| baseline | `mmlu_5976` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5977` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5978` | `mcq` | false | `B` | `D. Colonial powers preparing their colonies for independence` |
| baseline | `mmlu_5979` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5980` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5981` | `mcq` | true | `B` | `B. The fight for independence in South America` |
| baseline | `mmlu_5982` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5983` | `mcq` | true | `A` | `A. Policies of religious toleration` |
| baseline | `mmlu_5984` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5985` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5986` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5987` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5988` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5989` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5990` | `mcq` | true | `C` | `C. contact with Muslim trade caravans.` |
| baseline | `mmlu_5991` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5992` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5993` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5994` | `mcq` | false | `B` | `A. The world is too afraid of South Africa to oppose apartheid.` |
| baseline | `mmlu_5995` | `mcq` | true | `C` | `C. World War II` |
| baseline | `mmlu_5996` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5997` | `mcq` | false | `C` | `D. Reform` |
| baseline | `mmlu_5998` | `mcq` | false | `C` | `A. All adult men born within the geographic boundaries of the state` |
| baseline | `mmlu_5999` | `mcq` | true | `C` | `C. Decolonization` |
| baseline | `mmlu_6000` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6001` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6002` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6003` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6004` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6005` | `mcq` | false | `A` | `C. Protestant` |
| baseline | `mmlu_6006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6007` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6008` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6009` | `mcq` | true | `A` | `A. The strain placed on merchant families by long periods of separation` |
| baseline | `mmlu_6010` | `mcq` | true | `C` | `C. U.S. involvement in Panama's independence` |
| baseline | `mmlu_6011` | `mcq` | true | `C` | `C. Ancient leaders were given divine origins to bolster their legitimacy.` |
| baseline | `mmlu_6012` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6013` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6014` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6015` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6016` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6017` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6018` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6019` | `mcq` | true | `D` | `D. French women remained without full political rights until well into the following century.` |
| baseline | `mmlu_6020` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6021` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6022` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6023` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6024` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6025` | `mcq` | false | `B` | `D. The reduced demand for furs among European and Asian elites` |
| baseline | `mmlu_6026` | `mcq` | true | `C` | `C. Large-scale military losses and resentment of the working classes` |
| baseline | `mmlu_6027` | `mcq` | true | `C` | `C. Spanish authorities adapted local forms of labor mobilization for their own purposes.` |
| baseline | `mmlu_6028` | `mcq` | true | `D` | `D. Religious tolerance` |
| baseline | `mmlu_6029` | `mcq` | true | `A` | `A. European maritime exploration` |
| baseline | `mmlu_6030` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6031` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6032` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6033` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6034` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6035` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6036` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6037` | `mcq` | true | `D` | `D. Furs` |
| baseline | `mmlu_6038` | `mcq` | true | `D` | `D. Marxism` |
| baseline | `mmlu_6039` | `mcq` | true | `B` | `B. The election of Nelson Mandela` |
| baseline | `mmlu_6040` | `mcq` | false | `B` | `C. The Spanish wanted to preserve the independence of Native states in the New World as a buffer against Portuguese expa` |
| baseline | `mmlu_6041` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6042` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6043` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6044` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6045` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6046` | `mcq` | false | `C` | `A. Gave over his crown to King Ferdinand` |
| baseline | `mmlu_6047` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6048` | `mcq` | false | `D` | `C. Limited economic opportunities` |
| baseline | `mmlu_6049` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6050` | `mcq` | true | `B` | `B. Robespierre` |
| baseline | `mmlu_6051` | `mcq` | true | `D` | `D. The Industrial Revolution` |
| baseline | `mmlu_6052` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6053` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6054` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6055` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6056` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6057` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6058` | `mcq` | false | `B` | `C. Because these were strongholds of the Holy Roman Empire, the narrator warns the Winter King to stay away.` |
| baseline | `mmlu_6059` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6060` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6061` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6062` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6063` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6064` | `mcq` | false | `A` | `C. Zoroastrianism` |
| baseline | `mmlu_6065` | `mcq` | false | `A` | `C. Persia's location sat astride international trade routes with India.` |
| baseline | `mmlu_6066` | `mcq` | true | `B` | `B. The compass` |
| baseline | `mmlu_6067` | `mcq` | false | `C` | `A. The invention of the machine gun` |
| baseline | `mmlu_6068` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6069` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6070` | `mcq` | true | `D` | `D. The geography of Greece contains many natural harbors that facilitated trade and commerce.` |
| baseline | `mmlu_6071` | `mcq` | true | `C` | `C. A time of intense political conflict among warring Italian city-states and other factions` |
| baseline | `mmlu_6072` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6073` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6074` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6075` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6076` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6077` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6078` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6079` | `mcq` | true | `D` | `D. A response to aggression from outside of Western Europe` |
| baseline | `mmlu_6080` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6081` | `mcq` | true | `B` | `B. The British sought to end what they considered an inhumane practice without endangering their own authority.` |
| baseline | `mmlu_6082` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6083` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6084` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6085` | `mcq` | true | `C` | `C. Labor unions` |
| baseline | `mmlu_6086` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6087` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6088` | `mcq` | true | `C` | `C. The king of Ghana taxed salt and copper imports and exports.` |
| baseline | `mmlu_6089` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6090` | `mcq` | true | `B` | `B. Eating fish` |
| baseline | `mmlu_6091` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6092` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6093` | `mcq` | true | `B` | `B. Sociocultural conditions must always be considered` |
| baseline | `mmlu_6094` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6095` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6096` | `mcq` | true | `D` | `D. Smarthouse` |
| baseline | `mmlu_6097` | `mcq` | true | `A` | `A. Practice regular aerobic exercise` |
| baseline | `mmlu_6098` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6099` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6100` | `mcq` | false | `A` | `C. Avoidance` |
| baseline | `mmlu_6101` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6102` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6103` | `mcq` | true | `B` | `B. B6 and B12` |
| baseline | `mmlu_6104` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6105` | `mcq` | false | `C` | `B. Social support` |
| baseline | `mmlu_6106` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6107` | `mcq` | true | `A` | `A. That place holds many memories` |
| baseline | `mmlu_6108` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6109` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6110` | `mcq` | false | `D` | `C. Levenson` |
| baseline | `mmlu_6111` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6112` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6113` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6114` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6115` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6116` | `mcq` | false | `A` | `B. Women than men` |
| baseline | `mmlu_6117` | `mcq` | true | `B` | `B. Suppression of the immune system` |
| baseline | `mmlu_6118` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6119` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6120` | `mcq` | true | `B` | `B. Perceived as support` |
| baseline | `mmlu_6121` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6122` | `mcq` | true | `A` | `A. Ageism` |
| baseline | `mmlu_6123` | `mcq` | true | `D` | `D. Hospice` |
| baseline | `mmlu_6124` | `mcq` | false | `B` | `A. Very infrequent (less than 15%)` |
| baseline | `mmlu_6125` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6126` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6127` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6128` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6129` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6130` | `mcq` | false | `A` | `B. Shrinkage of the thymus gland` |
| baseline | `mmlu_6131` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6132` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6133` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6134` | `mcq` | false | `B` | `A. Gorilla` |
| baseline | `mmlu_6135` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6136` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6137` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6138` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6139` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6140` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6141` | `mcq` | false | `D` | `B. White` |
| baseline | `mmlu_6142` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6143` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6144` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6145` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6146` | `mcq` | false | `B` | `A. Heart` |
| baseline | `mmlu_6147` | `mcq` | true | `D` | `D. Semantic` |
| baseline | `mmlu_6148` | `mcq` | false | `C` | `D. Show ups and downs throughout the marriage` |
| baseline | `mmlu_6149` | `mcq` | true | `B` | `B. Attempt to explain findings and guide future research` |
| baseline | `mmlu_6150` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6151` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6152` | `mcq` | true | `B` | `B. Participant observer` |
| baseline | `mmlu_6153` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6154` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6155` | `mcq` | true | `C` | `C. Mostly genetic` |
| baseline | `mmlu_6156` | `mcq` | true | `D` | `D. Lower levels of negative emotions` |
| baseline | `mmlu_6157` | `mcq` | true | `D` | `D. Hawaii` |
| baseline | `mmlu_6158` | `mcq` | false | `B` | `C. Florida` |
| baseline | `mmlu_6159` | `mcq` | false | `B` | `A. Traits` |
| baseline | `mmlu_6160` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6161` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6163` | `mcq` | true | `A` | `A. Prevalence` |
| baseline | `mmlu_6164` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6165` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6166` | `mcq` | true | `B` | `B. About 25%` |
| baseline | `mmlu_6167` | `mcq` | true | `B` | `B. Internal` |
| baseline | `mmlu_6168` | `mcq` | true | `A` | `A. Tai chi` |
| baseline | `mmlu_6169` | `mcq` | false | `B` | `A. Hypertension` |
| baseline | `mmlu_6170` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6171` | `mcq` | true | `A` | `A. 10%` |
| baseline | `mmlu_6172` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6173` | `mcq` | false | `B` | `A. Pension` |
| baseline | `mmlu_6174` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6175` | `mcq` | true | `A` | `A. Alzheimer's` |
| baseline | `mmlu_6176` | `mcq` | true | `A` | `A. Longevity` |
| baseline | `mmlu_6177` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6178` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6179` | `mcq` | true | `B` | `B. Education about older adults` |
| baseline | `mmlu_6180` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6181` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6182` | `mcq` | true | `B` | `B. Niacin` |
| baseline | `mmlu_6183` | `mcq` | false | `B` | `D. Clinical depression` |
| baseline | `mmlu_6184` | `mcq` | true | `A` | `A. Quasi-experimental` |
| baseline | `mmlu_6185` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6186` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6187` | `mcq` | false | `B` | `C. Attachment` |
| baseline | `mmlu_6188` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6189` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6190` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6191` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6192` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6193` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_6194` | `mcq` | true | `A` | `A. Osteoblasts` |
| baseline | `mmlu_6195` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6196` | `mcq` | true | `C` | `C. Japan` |
| baseline | `mmlu_6197` | `mcq` | false | `C` | `B. Choice` |
| baseline | `mmlu_6198` | `mcq` | true | `B` | `B. Internal` |
| baseline | `mmlu_6199` | `mcq` | true | `A` | `A. Living will` |
| baseline | `mmlu_6200` | `mcq` | false | `A` | `B. Be able to avoid certain diseases` |
| baseline | `mmlu_6201` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6202` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6203` | `mcq` | true | `B` | `B. Conscientiousness` |
| baseline | `mmlu_6204` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6205` | `mcq` | true | `A` | `A. Have learned to cope with loss` |
| baseline | `mmlu_6206` | `mcq` | true | `C` | `C. Working as a system` |
| baseline | `mmlu_6207` | `mcq` | false | `B` | `C. Jewish` |
| baseline | `mmlu_6208` | `mcq` | true | `B` | `B. MMPI` |
| baseline | `mmlu_6209` | `mcq` | true | `B` | `B. Validity` |
| baseline | `mmlu_6210` | `mcq` | true | `A` | `A. Japan` |
| baseline | `mmlu_6211` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6212` | `mcq` | true | `D` | `D. The Eden Alternative` |
| baseline | `mmlu_6213` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6214` | `mcq` | false | `C` | `A. Positive reappraisal` |
| baseline | `mmlu_6215` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6216` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6217` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6218` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6219` | `mcq` | false | `A` | `C. Changes in hormone levels` |
| baseline | `mmlu_6220` | `mcq` | true | `A` | `A. Stress and loss of social support` |
| baseline | `mmlu_6221` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6223` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6224` | `mcq` | true | `B` | `B. The brain` |
| baseline | `mmlu_6225` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6226` | `mcq` | true | `D` | `D. Older adults drink more herbal tea than do younger adults` |
| baseline | `mmlu_6227` | `mcq` | true | `A` | `A. Activities of Daily Living` |
| baseline | `mmlu_6228` | `mcq` | true | `B` | `B. Korsakoff's` |
| baseline | `mmlu_6229` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6230` | `mcq` | true | `A` | `A. Jeanne Calment` |
| baseline | `mmlu_6231` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6232` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6233` | `mcq` | true | `B` | `B. Is treated like a fellow human being` |
| baseline | `mmlu_6234` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6235` | `mcq` | true | `A` | `A. Perspective` |
| baseline | `mmlu_6236` | `mcq` | false | `A` | `D. Job satisfaction` |
| baseline | `mmlu_6237` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6238` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6239` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6240` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6241` | `mcq` | true | `B` | `B. Daily activities like walking, gesturing, and even fidgeting` |
| baseline | `mmlu_6242` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6243` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6244` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6245` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6246` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6247` | `mcq` | true | `A` | `A. Age` |
| baseline | `mmlu_6248` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6249` | `mcq` | false | `A` | `B. They must fulfill their vows` |
| baseline | `mmlu_6250` | `mcq` | true | `C` | `C. The contents of the message` |
| baseline | `mmlu_6251` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6252` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6253` | `mcq` | false | `A` | `D. More than 50%` |
| baseline | `mmlu_6254` | `mcq` | false | `B` | `C. Kidney problems` |
| baseline | `mmlu_6255` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6256` | `mcq` | false | `A` | `D. Medicaid Directive Information Act` |
| baseline | `mmlu_6257` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6258` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6259` | `mcq` | true | `C` | `C. Ergonomic` |
| baseline | `mmlu_6260` | `mcq` | true | `B` | `B. Medicaid` |
| baseline | `mmlu_6261` | `mcq` | true | `C` | `C. Dementia` |
| baseline | `mmlu_6262` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6263` | `mcq` | false | `B` | `A. 20%` |
| baseline | `mmlu_6264` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6265` | `mcq` | true | `B` | `B. Personal control` |
| baseline | `mmlu_6266` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6267` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6268` | `mcq` | true | `B` | `B. Live to be 100 or older` |
| baseline | `mmlu_6269` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6270` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6271` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6272` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6273` | `mcq` | false | `D` | `C. Smaller inner circles` |
| baseline | `mmlu_6274` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6275` | `mcq` | true | `C` | `C. More than 50%` |
| baseline | `mmlu_6276` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6277` | `mcq` | false | `D` | `A. May be very well rehearsed` |
| baseline | `mmlu_6278` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6279` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6280` | `mcq` | true | `C` | `C. Free radicals and sunlight` |
| baseline | `mmlu_6281` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6282` | `mcq` | true | `B` | `B. Many theories will have to be combined to explain senescence` |
| baseline | `mmlu_6283` | `mcq` | false | `A` | `B. 82` |
| baseline | `mmlu_6284` | `mcq` | true | `B` | `B. Green` |
| baseline | `mmlu_6285` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6286` | `mcq` | true | `A` | `A. Height` |
| baseline | `mmlu_6287` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6288` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6289` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6290` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6291` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6292` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6293` | `mcq` | true | `B` | `B. SOD` |
| baseline | `mmlu_6294` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6295` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6296` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6297` | `mcq` | true | `D` | `D. Intention` |
| baseline | `mmlu_6298` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6299` | `mcq` | true | `B` | `B. Dependent` |
| baseline | `mmlu_6300` | `mcq` | false | `A` | `B. Nurture` |
| baseline | `mmlu_6301` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6302` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6303` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6304` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6305` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6306` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6307` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6308` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6309` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6310` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6311` | `mcq` | false | `B` | `D. Ebbinghaus` |
| baseline | `mmlu_6312` | `mcq` | true | `B` | `B. Mammography` |
| baseline | `mmlu_6313` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_6314` | `mcq` | false | `A` | `A/B/C/D` |
| baseline | `mmlu_6315` | `mcq` | true | `A` | `A. the id` |
| baseline | `mmlu_6316` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6317` | `mcq` | true | `C` | `C. experienced guilt` |
| baseline | `mmlu_6318` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_6319` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6320` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6321` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6322` | `mcq` | true | `C` | `C. between the ages of 3 and 6` |
| baseline | `mmlu_6323` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6324` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_6325` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6326` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_6327` | `mcq` | true | `C` | `C. the cell structure in the hypothalamus of these two groups` |
| baseline | `mmlu_6328` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6329` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6330` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6331` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6332` | `mcq` | true | `A` | `A. Gender identity` |
| baseline | `mmlu_6333` | `mcq` | false | `B` | `C. 7 inches` |
| baseline | `mmlu_6334` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6335` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6336` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6337` | `mcq` | false | `B` | `C. 72 hours` |
| baseline | `mmlu_6338` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6339` | `mcq` | true | `C` | `C. Hormones` |
| baseline | `mmlu_6340` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6341` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6342` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6343` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6344` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6345` | `mcq` | true | `A` | `A. U.S.` |
| baseline | `mmlu_6346` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6347` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6348` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6349` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_6350` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6351` | `mcq` | false | `D` | `C. sympathetic` |
| baseline | `mmlu_6352` | `mcq` | true | `D` | `D. clitoris` |
| baseline | `mmlu_6353` | `mcq` | true | `C` | `C. 14` |
| baseline | `mmlu_6354` | `mcq` | true | `A` | `A. religion and ethics` |
| baseline | `mmlu_6355` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6356` | `mcq` | true | `D` | `D. both A and B` |
| baseline | `mmlu_6357` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6358` | `mcq` | true | `C` | `C. 10 through 20` |
| baseline | `mmlu_6359` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_6360` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6361` | `mcq` | true | `A` | `A. Sterilization` |
| baseline | `mmlu_6362` | `mcq` | false | `C` | `A. natural selection` |
| baseline | `mmlu_6363` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6364` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6365` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6366` | `mcq` | true | `D` | `D. prepuce` |
| baseline | `mmlu_6367` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6368` | `mcq` | true | `B` | `B. necrophilia` |
| baseline | `mmlu_6369` | `mcq` | false | `A` | `D. all of the above` |
| baseline | `mmlu_6370` | `mcq` | true | `D` | `D. both A and C` |
| baseline | `mmlu_6371` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6372` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6373` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6374` | `mcq` | false | `D` | `A. artificial insemination` |
| baseline | `mmlu_6375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6376` | `mcq` | false | `B` | `C. 6` |
| baseline | `mmlu_6377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6378` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6379` | `mcq` | true | `B` | `B. syphilis` |
| baseline | `mmlu_6380` | `mcq` | false | `A` | `D. all of the above` |
| baseline | `mmlu_6381` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6382` | `mcq` | true | `D` | `D. none of the above` |
| baseline | `mmlu_6383` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6384` | `mcq` | true | `B` | `B. blood accumulation in the genitals` |
| baseline | `mmlu_6385` | `mcq` | true | `D` | `D. both A and B` |
| baseline | `mmlu_6386` | `mcq` | true | `D` | `D. gonorrhea` |
| baseline | `mmlu_6387` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6388` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6389` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6390` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6391` | `mcq` | true | `D` | `D. normal orgasm` |
| baseline | `mmlu_6392` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6393` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6394` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6395` | `mcq` | false | `B` | `A. woman-on-top` |
| baseline | `mmlu_6396` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6397` | `mcq` | true | `A` | `A. excitement` |
| baseline | `mmlu_6398` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6399` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6400` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6401` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6402` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6403` | `mcq` | true | `B` | `B. reproduction` |
| baseline | `mmlu_6404` | `mcq` | true | `A` | `A. Behavior modification` |
| baseline | `mmlu_6405` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6406` | `mcq` | true | `B` | `B. Pope Paul VI's` |
| baseline | `mmlu_6407` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6408` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6409` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6410` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6411` | `mcq` | false | `A` | `D. both A and C` |
| baseline | `mmlu_6412` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6413` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6414` | `mcq` | false | `A` | `C. heterosexual` |
| baseline | `mmlu_6415` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6416` | `mcq` | false | `C` | `B. being told by peers` |
| baseline | `mmlu_6417` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_6418` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6419` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6420` | `mcq` | true | `C` | `C. affective, cognitive, and physical` |
| baseline | `mmlu_6421` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6422` | `mcq` | true | `B` | `B. Ectopic pregnancy` |
| baseline | `mmlu_6423` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6424` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6425` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6426` | `mcq` | true | `A` | `A. in the hours immediately following birth` |
| baseline | `mmlu_6427` | `mcq` | false | `D` | `A. egg` |
| baseline | `mmlu_6428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6429` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_6430` | `mcq` | false | `B` | `A. 5` |
| baseline | `mmlu_6431` | `mcq` | true | `A` | `A. directly into the bloodstream` |
| baseline | `mmlu_6432` | `mcq` | true | `A` | `A. 1` |
| baseline | `mmlu_6433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6434` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6435` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6436` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6437` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6438` | `mcq` | true | `C` | `C. urethra` |
| baseline | `mmlu_6439` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6440` | `mcq` | false | `D` | `A. chlamydia` |
| baseline | `mmlu_6441` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6442` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6443` | `mcq` | true | `B` | `B. The flag State` |
| baseline | `mmlu_6444` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6445` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6446` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6447` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6448` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6449` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6450` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6451` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6452` | `mcq` | true | `A` | `A. The UN Human Rights Committee` |
| baseline | `mmlu_6453` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6454` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6455` | `mcq` | true | `C` | `C. No, all States are considered equal as sovereign States (the principle of sovereign equality, enshrined in article 2,` |
| baseline | `mmlu_6456` | `mcq` | false | `B` | `A. Recognition is determinate for the existence of statehood` |
| baseline | `mmlu_6457` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6459` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6460` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6461` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6462` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6463` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6464` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6465` | `mcq` | true | `C` | `C. Treaties, custom and general principles of law` |
| baseline | `mmlu_6466` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6467` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6468` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6469` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6470` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6471` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6472` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6473` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6474` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6475` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6476` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6477` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6478` | `mcq` | true | `D` | `D. GA Resolutions are considered as material source, in the sense that they may enunciate statements of customary law` |
| baseline | `mmlu_6479` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6480` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6481` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6482` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6483` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6484` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6485` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6486` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6487` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6488` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6489` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6490` | `mcq` | true | `D` | `D. The situation is not clear-cut but an act of parliament would most probably be required` |
| baseline | `mmlu_6491` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6492` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6493` | `mcq` | false | `D` | `B. Airey v Ireland (1979)` |
| baseline | `mmlu_6494` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6495` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6496` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6497` | `mcq` | true | `D` | `D. A reporting mechanism and right to individual petition` |
| baseline | `mmlu_6498` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6499` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6500` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6501` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6502` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6503` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6504` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6505` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6506` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6507` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6508` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6509` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6510` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6512` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6513` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6514` | `mcq` | false | `D` | `C. International tribunals share some, but not all, of the jurisdictional principles applicable to national courts` |
| baseline | `mmlu_6515` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6516` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6517` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6518` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6519` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6520` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6521` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6522` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6523` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6524` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6525` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6526` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6527` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6528` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6529` | `mcq` | false | `B` | `A. Recognition of governments is very prevalent in contemporary practice` |
| baseline | `mmlu_6530` | `mcq` | false | `B` | `D. The UDHR is a declaration adopted by several States at an international conference` |
| baseline | `mmlu_6531` | `mcq` | true | `B` | `B. The ECHR applies extraterritorially in circumstances where a member State exercises effective control` |
| baseline | `mmlu_6532` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6533` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6534` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6535` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6536` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6537` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6538` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6539` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6540` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6541` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6542` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6543` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6544` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6545` | `mcq` | false | `C` | `A. Golder v UK (1978)` |
| baseline | `mmlu_6546` | `mcq` | false | `C` | `D.` |
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
| baseline | `mmlu_6558` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6559` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6560` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6561` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6562` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6563` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6564` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6565` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6566` | `mcq` | true | `C` | `C. The international recognition of human rights after World War II` |
| baseline | `mmlu_6567` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6568` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6569` | `mcq` | true | `A` | `A. Law and Economics` |
| baseline | `mmlu_6570` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6571` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6572` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6573` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6574` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6575` | `mcq` | true | `D` | `D. Sociological` |
| baseline | `mmlu_6576` | `mcq` | true | `D` | `D. Reciprocity.` |
| baseline | `mmlu_6577` | `mcq` | true | `C` | `C. That facts about the world or human nature cannot normally ordain what ought to be` |
| baseline | `mmlu_6578` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6579` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6580` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6581` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6582` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6583` | `mcq` | true | `B` | `B. Positive law` |
| baseline | `mmlu_6584` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6585` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6586` | `mcq` | true | `B` | `B. stare decisis` |
| baseline | `mmlu_6587` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6588` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6589` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6590` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6591` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6592` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6593` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6594` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6595` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6596` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6597` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6598` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6599` | `mcq` | true | `B` | `B. Because they are an expression of a capitalist economy and are unnecessary in a socialist society.` |
| baseline | `mmlu_6600` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6601` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6602` | `mcq` | true | `B` | `B. Civil Law.` |
| baseline | `mmlu_6603` | `mcq` | false | `B` | `D. He rejects the idea of equality altogether.` |
| baseline | `mmlu_6604` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6605` | `mcq` | true | `B` | `B. If each person's holdings are just, then the total distribution of holdings is just.` |
| baseline | `mmlu_6606` | `mcq` | true | `B` | `B. Analytical` |
| baseline | `mmlu_6607` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6608` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6609` | `mcq` | true | `C` | `C. Because Aristotle believed that man is a 'social animal'` |
| baseline | `mmlu_6610` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6611` | `mcq` | true | `A` | `A. Command` |
| baseline | `mmlu_6612` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6613` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6614` | `mcq` | true | `A` | `A. Legal fiction` |
| baseline | `mmlu_6615` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6616` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6617` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6618` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6619` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6620` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6621` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6622` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6623` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6624` | `mcq` | true | `A` | `A. Historical` |
| baseline | `mmlu_6625` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6626` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6627` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6628` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6629` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6630` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6631` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6632` | `mcq` | false | `B` | `A. Because of their vagueness.` |
| baseline | `mmlu_6633` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6634` | `mcq` | false | `C` | `B. Salmond` |
| baseline | `mmlu_6635` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6636` | `mcq` | false | `D` | `C. Roman Law` |
| baseline | `mmlu_6637` | `mcq` | true | `B` | `B. void contract` |
| baseline | `mmlu_6638` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6639` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6640` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6641` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6642` | `mcq` | true | `A` | `A. interpret` |
| baseline | `mmlu_6643` | `mcq` | false | `B` | `D. Rousseau` |
| baseline | `mmlu_6644` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6645` | `mcq` | true | `A` | `A. Because it fails to address the actual capabilities people have to benefit from his theory of justice.` |
| baseline | `mmlu_6646` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6647` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6648` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6649` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6650` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6651` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6652` | `mcq` | true | `D` | `D. Austin` |
| baseline | `mmlu_6653` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6654` | `mcq` | true | `B` | `B. Ulpian` |
| baseline | `mmlu_6655` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6656` | `mcq` | true | `B` | `B. federal statutes` |
| baseline | `mmlu_6657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6658` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6659` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6660` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6661` | `mcq` | true | `B` | `B. Extent of responsibility multiplied by actual harm done.` |
| baseline | `mmlu_6662` | `mcq` | true | `D` | `D. Rousseau` |
| baseline | `mmlu_6663` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6664` | `mcq` | true | `B` | `B. Sanction.` |
| baseline | `mmlu_6665` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6666` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6667` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6668` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6669` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6670` | `mcq` | true | `B` | `B. Critical Legal Studies` |
| baseline | `mmlu_6671` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6672` | `mcq` | true | `A` | `A. includes two or more alternatives` |
| baseline | `mmlu_6673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6674` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6675` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6676` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6677` | `mcq` | true | `D` | `D. division` |
| baseline | `mmlu_6678` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6679` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6680` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6681` | `mcq` | true | `B` | `B. Guilt by association` |
| baseline | `mmlu_6682` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6683` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6684` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6685` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6686` | `mcq` | false | `B` | `C. Hypostatization` |
| baseline | `mmlu_6687` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6688` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6689` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6690` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6691` | `mcq` | true | `D` | `D. argument against the person` |
| baseline | `mmlu_6692` | `mcq` | true | `D` | `D. Criticizing the person who makes it` |
| baseline | `mmlu_6693` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6694` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6695` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6696` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6697` | `mcq` | true | `D` | `D. Begging the question` |
| baseline | `mmlu_6698` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6699` | `mcq` | true | `B` | `B. solid slope` |
| baseline | `mmlu_6700` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6701` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6702` | `mcq` | true | `D` | `D. both B and C` |
| baseline | `mmlu_6703` | `mcq` | true | `D` | `D. False dichotomy` |
| baseline | `mmlu_6704` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6705` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6706` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6707` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6708` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6709` | `mcq` | true | `C` | `C. Hypothetical syllogism` |
| baseline | `mmlu_6710` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6712` | `mcq` | true | `D` | `D. Hasty Generalization` |
| baseline | `mmlu_6713` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6714` | `mcq` | false | `B` | `D. Hypostatization` |
| baseline | `mmlu_6715` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6716` | `mcq` | true | `D` | `D. reductio ad absurdum` |
| baseline | `mmlu_6717` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6718` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6719` | `mcq` | false | `A` | `D. False dichotomy` |
| baseline | `mmlu_6720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6721` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6722` | `mcq` | true | `A` | `A. Laudatory personality` |
| baseline | `mmlu_6723` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6724` | `mcq` | true | `D` | `D. False dilemma` |
| baseline | `mmlu_6725` | `mcq` | true | `A` | `A. no valid conclusion can be drawn` |
| baseline | `mmlu_6726` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6728` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6729` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6730` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6731` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6733` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6734` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6735` | `mcq` | true | `C` | `C. Hypostatization` |
| baseline | `mmlu_6736` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6737` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6738` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6739` | `mcq` | true | `C` | `C. False dilemma` |
| baseline | `mmlu_6740` | `mcq` | true | `D` | `D. Style over substance` |
| baseline | `mmlu_6741` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6742` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6743` | `mcq` | false | `B` | `A. no valid conclusion can be drawn` |
| baseline | `mmlu_6744` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6745` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6746` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6747` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6748` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6749` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6750` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6751` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6752` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6753` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6754` | `mcq` | false | `B` | `D. It reaches a truthful conclusion` |
| baseline | `mmlu_6755` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6756` | `mcq` | true | `C` | `C. appeal to anonymous authority` |
| baseline | `mmlu_6757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6758` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6759` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6760` | `mcq` | true | `C` | `C. irrelevant conclusion` |
| baseline | `mmlu_6761` | `mcq` | true | `C` | `C. false criteria` |
| baseline | `mmlu_6762` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6763` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6764` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6765` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6766` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6767` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6768` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6769` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6770` | `mcq` | true | `B` | `B. common person appeal` |
| baseline | `mmlu_6771` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6772` | `mcq` | true | `B` | `B. Equivocation` |
| baseline | `mmlu_6773` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6775` | `mcq` | true | `D` | `D. Loaded language` |
| baseline | `mmlu_6776` | `mcq` | true | `C` | `C. Reprehensible personality` |
| baseline | `mmlu_6777` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6778` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6779` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6780` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6781` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6782` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6783` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6784` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6785` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6786` | `mcq` | false | `A` | `D. both A and B` |
| baseline | `mmlu_6787` | `mcq` | false | `A` | `C. False Dilemma` |
| baseline | `mmlu_6788` | `mcq` | true | `D` | `D. Not sufficiently similar in relevant ways` |
| baseline | `mmlu_6789` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6790` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6791` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6792` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6793` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6794` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6795` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6796` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6797` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6798` | `mcq` | true | `A` | `A. Equivocation` |
| baseline | `mmlu_6799` | `mcq` | false | `B` | `C. Denying the Antecedent` |
| baseline | `mmlu_6800` | `mcq` | true | `B` | `B. appeal to tradition` |
| baseline | `mmlu_6801` | `mcq` | true | `D` | `D. Imperfect analogy` |
| baseline | `mmlu_6802` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6803` | `mcq` | true | `B` | `B. Complex proposition` |
| baseline | `mmlu_6804` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6805` | `mcq` | true | `A` | `A. complex cause` |
| baseline | `mmlu_6806` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6809` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6810` | `mcq` | true | `D` | `D. Argument from Ignorance` |
| baseline | `mmlu_6811` | `mcq` | true | `D` | `D. Argument from authority` |
| baseline | `mmlu_6812` | `mcq` | true | `D` | `D. Equivocation` |
| baseline | `mmlu_6813` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6814` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6815` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6816` | `mcq` | false | `A` | `C. argument by consensus` |
| baseline | `mmlu_6817` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6818` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6819` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6820` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6821` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6822` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6823` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6824` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6825` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6826` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6827` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6828` | `mcq` | false | `C` | `D. suppressed evidence` |
| baseline | `mmlu_6829` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6830` | `mcq` | false | `B` | `D. Hasty Generalization` |
| baseline | `mmlu_6831` | `mcq` | true | `D` | `D. Appeal to the person` |
| baseline | `mmlu_6832` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6833` | `mcq` | true | `A` | `A. Amphiboly` |
| baseline | `mmlu_6834` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6835` | `mcq` | false | `D` | `C. True, False` |
| baseline | `mmlu_6836` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6837` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6838` | `mcq` | false | `D` | `C. 48` |
| baseline | `mmlu_6839` | `mcq` | true | `A` | `A. convolutional networks` |
| baseline | `mmlu_6840` | `mcq` | false | `B` | `D. False, True` |
| baseline | `mmlu_6841` | `mcq` | true | `A` | `A. O(D)` |
| baseline | `mmlu_6842` | `mcq` | false | `B` | `C. True, False` |
| baseline | `mmlu_6843` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_6844` | `mcq` | true | `A` | `A. Lower variance` |
| baseline | `mmlu_6845` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6846` | `mcq` | false | `C` | `B. overfitting` |
| baseline | `mmlu_6847` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6848` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6849` | `mcq` | true | `B` | `B. not pure` |
| baseline | `mmlu_6850` | `mcq` | false | `B` | `D. False, True` |
| baseline | `mmlu_6851` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6852` | `mcq` | true | `A` | `A. The number of hidden nodes` |
| baseline | `mmlu_6853` | `mcq` | true | `A` | `A. The polynomial degree` |
| baseline | `mmlu_6854` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6855` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6856` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6857` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6858` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6859` | `mcq` | true | `B` | `B. Density-based clustering` |
| baseline | `mmlu_6860` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6861` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6862` | `mcq` | false | `C` | `D. dependent on the number of iterations` |
| baseline | `mmlu_6863` | `mcq` | true | `D` | `D. Decrease variance` |
| baseline | `mmlu_6864` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6865` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6866` | `mcq` | false | `C` | `B. 0.473` |
| baseline | `mmlu_6867` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6868` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6869` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6870` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6871` | `mcq` | true | `D` | `D. To avoid overfitting the training set` |
| baseline | `mmlu_6872` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6873` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6874` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6875` | `mcq` | false | `A` | `A, C` |
| baseline | `mmlu_6876` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6877` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6878` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6880` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6881` | `mcq` | false | `D` | `C. 7` |
| baseline | `mmlu_6882` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6883` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6884` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6885` | `mcq` | true | `B` | `B. O(N)` |
| baseline | `mmlu_6886` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6887` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6888` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6889` | `mcq` | true | `A` | `A. Linear hard-margin SVM.` |
| baseline | `mmlu_6890` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_6891` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6892` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6893` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6894` | `mcq` | false | `B` | `A. The use of sampling with replacement as the sampling technique` |
| baseline | `mmlu_6895` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6896` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6897` | `mcq` | false | `C` | `A. 0` |
| baseline | `mmlu_6898` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6899` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6900` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6901` | `mcq` | true | `C` | `C. 0.635` |
| baseline | `mmlu_6902` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6903` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6904` | `mcq` | true | `A` | `A. Expectation Maximization` |
| baseline | `mmlu_6905` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6906` | `mcq` | true | `A` | `A. linear in K` |
| baseline | `mmlu_6907` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6908` | `mcq` | false | `D` | `A. 1/6` |
| baseline | `mmlu_6909` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6910` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6911` | `mcq` | true | `C` | `C. The kernel width` |
| baseline | `mmlu_6912` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6913` | `mcq` | true | `B` | `B. Whether we assume full class covariance matrices or diagonal class covariance matrices` |
| baseline | `mmlu_6914` | `mcq` | false | `D` | `C. True, False` |
| baseline | `mmlu_6915` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6916` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6917` | `mcq` | true | `B` | `B. Unsupervised learning` |
| baseline | `mmlu_6918` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6919` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6920` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6921` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6922` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6923` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6924` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6925` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6926` | `mcq` | false | `B` | `C. both (a) and (b)` |
| baseline | `mmlu_6927` | `mcq` | true | `B` | `B. Maximization` |
| baseline | `mmlu_6928` | `mcq` | true | `B` | `B. Whether we assume full class covariance matrices or diagonal class covariance matrices` |
| baseline | `mmlu_6929` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6930` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6931` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6932` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6933` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6934` | `mcq` | true | `D` | `D. either (a) or (b)` |
| baseline | `mmlu_6935` | `mcq` | false | `B` | `D. All of above` |
| baseline | `mmlu_6936` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6937` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6938` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6939` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6940` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6941` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6942` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6943` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6944` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6945` | `mcq` | true | `A` | `A. 111021` |
| baseline | `mmlu_6946` | `mcq` | true | `C` | `C. True, False` |
| baseline | `mmlu_6947` | `mcq` | true | `B` | `B. Satisficing` |
| baseline | `mmlu_6948` | `mcq` | true | `D` | `D. Heuristics` |
| baseline | `mmlu_6949` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6950` | `mcq` | true | `D` | `D. The level of rivalry` |
| baseline | `mmlu_6951` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6952` | `mcq` | true | `B` | `B. Work schedule design` |
| baseline | `mmlu_6953` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6954` | `mcq` | true | `D` | `D. Legitimate` |
| baseline | `mmlu_6955` | `mcq` | true | `B` | `B. Max Weber` |
| baseline | `mmlu_6956` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6957` | `mcq` | true | `C` | `C. Milton Friedman` |
| baseline | `mmlu_6958` | `mcq` | true | `B` | `B. Elton Mayo` |
| baseline | `mmlu_6959` | `mcq` | false | `A` | `D. Developmental` |
| baseline | `mmlu_6960` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6961` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6962` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6963` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6964` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6965` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6966` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6967` | `mcq` | true | `D` | `D. Agile organisation` |
| baseline | `mmlu_6968` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6969` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6970` | `mcq` | false | `B` | `A. Job design` |
| baseline | `mmlu_6971` | `mcq` | true | `D` | `D. Economic reward` |
| baseline | `mmlu_6972` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6973` | `mcq` | true | `A` | `A. John Stuart Mill` |
| baseline | `mmlu_6974` | `mcq` | true | `A` | `A. Work specialisation` |
| baseline | `mmlu_6975` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6976` | `mcq` | false | `D` | `B. Divisional` |
| baseline | `mmlu_6977` | `mcq` | false | `A` | `D. Service` |
| baseline | `mmlu_6978` | `mcq` | true | `D` | `D. Socialisation` |
| baseline | `mmlu_6979` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6980` | `mcq` | true | `B` | `B. James Dyson` |
| baseline | `mmlu_6981` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6982` | `mcq` | true | `B` | `B. Face-to-face` |
| baseline | `mmlu_6983` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6984` | `mcq` | true | `B` | `B. Introducing private sector business principles into the public sector` |
| baseline | `mmlu_6985` | `mcq` | false | `C` | `B. Jay Barney` |
| baseline | `mmlu_6986` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6987` | `mcq` | true | `B` | `B. A formal process of planning to fill a role that will become vacant` |
| baseline | `mmlu_6988` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6989` | `mcq` | true | `C` | `C. Limited knowledge and uncertainty` |
| baseline | `mmlu_6990` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6991` | `mcq` | true | `A` | `A. Group roles` |
| baseline | `mmlu_6992` | `mcq` | true | `C` | `C. Social audit` |
| baseline | `mmlu_6993` | `mcq` | false | `B` | `A. Task culture` |
| baseline | `mmlu_6994` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6995` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6996` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6997` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6998` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6999` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7000` | `mcq` | false | `D` | `C. Global competition` |
| baseline | `mmlu_7001` | `mcq` | false | `D` | `B. Processes` |
| baseline | `mmlu_7002` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7003` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7004` | `mcq` | true | `D` | `D. Specific, measurable, achievable, rewarded and timely` |
| baseline | `mmlu_7005` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7006` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7007` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7008` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7009` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7010` | `mcq` | true | `B` | `B. Market penetration` |
| baseline | `mmlu_7011` | `mcq` | true | `D` | `D. remotely` |
| baseline | `mmlu_7012` | `mcq` | true | `D` | `D. Assertive and sociable` |
| baseline | `mmlu_7013` | `mcq` | true | `B` | `B. Mission statement` |
| baseline | `mmlu_7014` | `mcq` | true | `B` | `B. Strategy formulation` |
| baseline | `mmlu_7015` | `mcq` | true | `B` | `B. Time and motion studies` |
| baseline | `mmlu_7016` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7017` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7018` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7019` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7020` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7021` | `mcq` | false | `B` | `A. Bottom to top` |
| baseline | `mmlu_7022` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7023` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7024` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7025` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7026` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7027` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7028` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7029` | `mcq` | true | `A` | `A. Long-term` |
| baseline | `mmlu_7030` | `mcq` | false | `B` | `C. Formal` |
| baseline | `mmlu_7031` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7032` | `mcq` | true | `B` | `B. Events` |
| baseline | `mmlu_7033` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7034` | `mcq` | false | `D` | `C. Job characteristics model` |
| baseline | `mmlu_7035` | `mcq` | true | `C` | `C. Adam Smith` |
| baseline | `mmlu_7036` | `mcq` | true | `D` | `D. Productivity` |
| baseline | `mmlu_7037` | `mcq` | false | `C` | `D. planning, organising, controlling, leading` |
| baseline | `mmlu_7038` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7039` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7040` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7041` | `mcq` | true | `C` | `C. Worker empowerment` |
| baseline | `mmlu_7042` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7043` | `mcq` | true | `D` | `D. Strategic business unit` |
| baseline | `mmlu_7044` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7045` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7046` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7047` | `mcq` | true | `D` | `D. Running a business to create social benefits` |
| baseline | `mmlu_7048` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7049` | `mcq` | true | `D` | `D. Company` |
| baseline | `mmlu_7050` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7051` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7052` | `mcq` | false | `C` | `D. After the end of the Second World War.` |
| baseline | `mmlu_7053` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7054` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7055` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7056` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7057` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7058` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7059` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7060` | `mcq` | true | `C` | `C. By grouping together customers with similar needs, it provides a commercially viable method of serving these customer` |
| baseline | `mmlu_7061` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7062` | `mcq` | true | `A` | `A. Winner's curse.` |
| baseline | `mmlu_7063` | `mcq` | true | `B` | `B. Price elasticity.` |
| baseline | `mmlu_7064` | `mcq` | true | `C` | `C. Market exchanges.` |
| baseline | `mmlu_7065` | `mcq` | true | `C` | `C. Permission-based email marketing.` |
| baseline | `mmlu_7066` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7067` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7068` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7069` | `mcq` | true | `B` | `B. Weak theory.` |
| baseline | `mmlu_7070` | `mcq` | true | `C` | `C. Portfolio analysis.` |
| baseline | `mmlu_7071` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7072` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7073` | `mcq` | true | `B` | `B. Public relations.` |
| baseline | `mmlu_7074` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7075` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7076` | `mcq` | false | `A` | `C. Adoption process.` |
| baseline | `mmlu_7077` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7078` | `mcq` | true | `B` | `B. Early adopter.` |
| baseline | `mmlu_7079` | `mcq` | true | `A` | `A. Direct.` |
| baseline | `mmlu_7080` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7081` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7082` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7083` | `mcq` | true | `D` | `D. Brand imagery.` |
| baseline | `mmlu_7084` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7085` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7086` | `mcq` | true | `B` | `B. Research proposal.` |
| baseline | `mmlu_7087` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7088` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7089` | `mcq` | true | `B` | `B. cold canvassing` |
| baseline | `mmlu_7090` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7091` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7092` | `mcq` | true | `B` | `B. Demographics.` |
| baseline | `mmlu_7093` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7094` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7095` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7096` | `mcq` | true | `C` | `C. Relationship marketing.` |
| baseline | `mmlu_7097` | `mcq` | true | `C` | `C. Value.` |
| baseline | `mmlu_7098` | `mcq` | true | `A` | `A. Dialogue.` |
| baseline | `mmlu_7099` | `mcq` | true | `B` | `B. Learning.` |
| baseline | `mmlu_7100` | `mcq` | true | `A` | `A. Price skimming` |
| baseline | `mmlu_7101` | `mcq` | true | `B` | `B. Convenience stores.` |
| baseline | `mmlu_7102` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7103` | `mcq` | true | `D` | `D. Brand personalities.` |
| baseline | `mmlu_7104` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7105` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7106` | `mcq` | true | `B` | `B. Field marketing.` |
| baseline | `mmlu_7107` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7108` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7109` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7110` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7111` | `mcq` | true | `A` | `A. Test markets.` |
| baseline | `mmlu_7112` | `mcq` | true | `A` | `A. Low-contact service.` |
| baseline | `mmlu_7113` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7114` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7115` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7116` | `mcq` | true | `A` | `A. Stratified sample.` |
| baseline | `mmlu_7117` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7118` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7119` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7120` | `mcq` | true | `A` | `A. Test marketing.` |
| baseline | `mmlu_7121` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7122` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7123` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7124` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7125` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7126` | `mcq` | true | `C` | `C. Spam.` |
| baseline | `mmlu_7127` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7128` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7129` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7130` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7131` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7132` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7133` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7134` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7135` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7136` | `mcq` | true | `C` | `C. Price minimizer' purchasing.` |
| baseline | `mmlu_7137` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7138` | `mcq` | true | `D` | `D. Trademark` |
| baseline | `mmlu_7139` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7140` | `mcq` | true | `A` | `A. Internet marketing.` |
| baseline | `mmlu_7141` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7142` | `mcq` | true | `A` | `A. Purchase context.` |
| baseline | `mmlu_7143` | `mcq` | true | `A` | `A. Lead generation.` |
| baseline | `mmlu_7144` | `mcq` | true | `D` | `D. Public relations` |
| baseline | `mmlu_7145` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7146` | `mcq` | false | `B` | `D. Competitor orientation.` |
| baseline | `mmlu_7147` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7148` | `mcq` | true | `B` | `B. Legal environment.` |
| baseline | `mmlu_7149` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7150` | `mcq` | true | `D` | `D. Pay per click (PPC).` |
| baseline | `mmlu_7151` | `mcq` | true | `A` | `A. Distribution.` |
| baseline | `mmlu_7152` | `mcq` | true | `C` | `C. Perceptual maps.` |
| baseline | `mmlu_7153` | `mcq` | true | `C` | `C. $6,860` |
| baseline | `mmlu_7154` | `mcq` | false | `D` | `B. Price assurance.` |
| baseline | `mmlu_7155` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7156` | `mcq` | true | `B` | `B. Decoding.` |
| baseline | `mmlu_7157` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7158` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7159` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7160` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7161` | `mcq` | true | `B` | `B. Product lifecycle.` |
| baseline | `mmlu_7162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7163` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7164` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7165` | `mcq` | false | `B` | `A. Luxury product.` |
| baseline | `mmlu_7166` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7167` | `mcq` | true | `A` | `A. Exhibitions.` |
| baseline | `mmlu_7168` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7169` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7170` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7171` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7172` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7173` | `mcq` | false | `A` | `D. Customer Service (CS).` |
| baseline | `mmlu_7174` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7175` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7176` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7177` | `mcq` | true | `C` | `C. Category-killer stores.` |
| baseline | `mmlu_7178` | `mcq` | true | `A` | `A. Two-step.` |
| baseline | `mmlu_7179` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7180` | `mcq` | true | `B` | `B. The political, economic, social, technological, legal, and ecological environments.` |
| baseline | `mmlu_7181` | `mcq` | true | `B` | `B. The market segment must have measurable purchasing power and size.` |
| baseline | `mmlu_7182` | `mcq` | true | `D` | `D. Promotion.` |
| baseline | `mmlu_7183` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7184` | `mcq` | true | `D` | `D. Threat from government.` |
| baseline | `mmlu_7185` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7186` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7187` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7188` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7189` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7190` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7191` | `mcq` | true | `B` | `B. empathy` |
| baseline | `mmlu_7192` | `mcq` | true | `A` | `A. Encoding.` |
| baseline | `mmlu_7193` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7194` | `mcq` | false | `D` | `C. Public relations.` |
| baseline | `mmlu_7195` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7196` | `mcq` | true | `D` | `D. Service encounters.` |
| baseline | `mmlu_7197` | `mcq` | true | `B` | `B. Place utility.` |
| baseline | `mmlu_7198` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7199` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7200` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7201` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7202` | `mcq` | true | `A` | `A. Self-actualization.` |
| baseline | `mmlu_7203` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7204` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_7205` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7206` | `mcq` | true | `B` | `B. Information utility.` |
| baseline | `mmlu_7207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7208` | `mcq` | true | `B` | `B. Social media.` |
| baseline | `mmlu_7209` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7210` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7211` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7212` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7213` | `mcq` | true | `A` | `A. Face validity.` |
| baseline | `mmlu_7214` | `mcq` | true | `C` | `C. Reliability.` |
| baseline | `mmlu_7215` | `mcq` | false | `D` | `C. Supply chain.` |
| baseline | `mmlu_7216` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7217` | `mcq` | true | `A` | `A. Integrated marketing communications (IMC).` |
| baseline | `mmlu_7218` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7219` | `mcq` | true | `C` | `C. Strategic marketing.` |
| baseline | `mmlu_7220` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7221` | `mcq` | true | `C` | `C. Sponsorship.` |
| baseline | `mmlu_7222` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7223` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7224` | `mcq` | true | `A` | `A. Socio-cultural environment.` |
| baseline | `mmlu_7225` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7226` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_7227` | `mcq` | true | `A` | `A. Brand placement.` |
| baseline | `mmlu_7228` | `mcq` | true | `C` | `C. Digital marketing` |
| baseline | `mmlu_7229` | `mcq` | true | `B` | `B. Search engine optimization.` |
| baseline | `mmlu_7230` | `mcq` | true | `C` | `C. Internet advertising.` |
| baseline | `mmlu_7231` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7232` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7233` | `mcq` | false | `A` | `B. Differentiation.` |
| baseline | `mmlu_7234` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7235` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7236` | `mcq` | true | `A` | `A. perpetual inventory` |
| baseline | `mmlu_7237` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7238` | `mcq` | true | `B` | `B. Long-term; customers and stakeholders.` |
| baseline | `mmlu_7239` | `mcq` | true | `B` | `B. Intensive distribution.` |
| baseline | `mmlu_7240` | `mcq` | true | `C` | `C. Causal research.` |
| baseline | `mmlu_7241` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7242` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7243` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7244` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7245` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7246` | `mcq` | true | `C` | `C. Relationship pricing.` |
| baseline | `mmlu_7247` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7248` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7249` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7250` | `mcq` | true | `B` | `B. Transfer pricing.` |
| baseline | `mmlu_7251` | `mcq` | true | `C` | `C. Pure price bundling.` |
| baseline | `mmlu_7252` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7253` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7254` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7255` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7256` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7257` | `mcq` | true | `C` | `C. Social media marketing (SMM)` |
| baseline | `mmlu_7258` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7259` | `mcq` | true | `C` | `C. Physiological needs.` |
| baseline | `mmlu_7260` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7261` | `mcq` | true | `B` | `B. Secondary research.` |
| baseline | `mmlu_7262` | `mcq` | true | `B` | `B. Mobile.` |
| baseline | `mmlu_7263` | `mcq` | true | `D` | `D. Perishability.` |
| baseline | `mmlu_7264` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7265` | `mcq` | true | `D` | `D. Feedback.` |
| baseline | `mmlu_7266` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7267` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7268` | `mcq` | true | `A` | `A. Direct marketing.` |
| baseline | `mmlu_7269` | `mcq` | true | `A` | `A. Reduced perceived risk.` |
| baseline | `mmlu_7270` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7271` | `mcq` | true | `C` | `C. Full-service agency.` |
| baseline | `mmlu_7272` | `mcq` | true | `D` | `D. positioning` |
| baseline | `mmlu_7273` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7274` | `mcq` | false | `A` | `D. Service satisfaction.` |
| baseline | `mmlu_7275` | `mcq` | true | `B` | `B. Primary research.` |
| baseline | `mmlu_7276` | `mcq` | true | `A` | `A. Direct response advertising.` |
| baseline | `mmlu_7277` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7278` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7279` | `mcq` | false | `C` | `A. Channel conflict.` |
| baseline | `mmlu_7280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7281` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7282` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7283` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7284` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7285` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7286` | `mcq` | true | `A` | `A. 0.01` |
| baseline | `mmlu_7287` | `mcq` | true | `C` | `C. thymine.` |
| baseline | `mmlu_7288` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7289` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7290` | `mcq` | true | `D` | `D. all of these` |
| baseline | `mmlu_7291` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7292` | `mcq` | true | `D` | `D. Almost 100%` |
| baseline | `mmlu_7293` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7294` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7295` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7296` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7298` | `mcq` | true | `D` | `D. 45,X` |
| baseline | `mmlu_7299` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7300` | `mcq` | true | `A` | `A. 1.0/64` |
| baseline | `mmlu_7301` | `mcq` | false | `B` | `A. 10,000–15,000` |
| baseline | `mmlu_7302` | `mcq` | true | `C` | `C. Sister` |
| baseline | `mmlu_7303` | `mcq` | true | `D` | `D. APOE` |
| baseline | `mmlu_7304` | `mcq` | false | `D` | `B. 7` |
| baseline | `mmlu_7305` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7307` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7308` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7309` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7310` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7311` | `mcq` | false | `C` | `D. Pompe disease` |
| baseline | `mmlu_7312` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7313` | `mcq` | false | `D` | `A. 1 in 4` |
| baseline | `mmlu_7314` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7315` | `mcq` | false | `C` | `B. 0.64` |
| baseline | `mmlu_7316` | `mcq` | false | `D` | `B. HMG-CoA reductase` |
| baseline | `mmlu_7317` | `mcq` | false | `B` | `C. codominance` |
| baseline | `mmlu_7318` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7319` | `mcq` | true | `A` | `A. Recessive inheritance has` |
| baseline | `mmlu_7320` | `mcq` | true | `A` | `A. Huntington disease` |
| baseline | `mmlu_7321` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7322` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7323` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7324` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7325` | `mcq` | false | `C` | `A. 1 in 1000` |
| baseline | `mmlu_7326` | `mcq` | true | `C` | `C. Hexosaminidase A` |
| baseline | `mmlu_7327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7328` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7329` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7330` | `mcq` | true | `C` | `C. Developmental plasticity` |
| baseline | `mmlu_7331` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7332` | `mcq` | false | `C` | `B. 1.0/4` |
| baseline | `mmlu_7333` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7334` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7335` | `mcq` | false | `C` | `A. about 2` |
| baseline | `mmlu_7336` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7337` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7338` | `mcq` | true | `A` | `A. bind regions near a eukaryotic gene and allow an RNA polymerase to transcribe a gene` |
| baseline | `mmlu_7339` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7340` | `mcq` | true | `B` | `B. Prophase I.` |
| baseline | `mmlu_7341` | `mcq` | true | `D` | `D. mitochondrial DNA.` |
| baseline | `mmlu_7342` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7343` | `mcq` | false | `B` | `D. 46 pairs` |
| baseline | `mmlu_7344` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7345` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7346` | `mcq` | false | `C` | `B. 0.32` |
| baseline | `mmlu_7347` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7348` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7349` | `mcq` | true | `A` | `A. solving criminal and paternity cases` |
| baseline | `mmlu_7350` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7351` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7352` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7353` | `mcq` | true | `D` | `D. 45,Y` |
| baseline | `mmlu_7354` | `mcq` | true | `B` | `B. BRCA2` |
| baseline | `mmlu_7355` | `mcq` | true | `D` | `D. Succinylcholine` |
| baseline | `mmlu_7356` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7357` | `mcq` | true | `C` | `C. 46` |
| baseline | `mmlu_7358` | `mcq` | false | `B` | `A/B/C/D` |
| baseline | `mmlu_7359` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7360` | `mcq` | true | `C` | `C. Huntington disease` |
| baseline | `mmlu_7361` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7362` | `mcq` | true | `A` | `A. Intron` |
| baseline | `mmlu_7363` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7364` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7365` | `mcq` | true | `D` | `D. Zellweger syndrome` |
| baseline | `mmlu_7366` | `mcq` | true | `B` | `B. hereditary non-polyposis colon cancer (HNPCC).` |
| baseline | `mmlu_7367` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7368` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7369` | `mcq` | true | `B` | `B. phenotype` |
| baseline | `mmlu_7370` | `mcq` | true | `A` | `A. 47,XXX` |
| baseline | `mmlu_7371` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7372` | `mcq` | true | `D` | `D. chimaerism.` |
| baseline | `mmlu_7373` | `mcq` | true | `C` | `C. 1 in 100 to 1 in 200` |
| baseline | `mmlu_7374` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7375` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7376` | `mcq` | true | `B` | `B. neutral or deleterious` |
| baseline | `mmlu_7377` | `mcq` | true | `A` | `A. they allow genetic as opposed to environmental influences on variation in a trait to be estimated` |
| baseline | `mmlu_7378` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7379` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7380` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7381` | `mcq` | false | `D` | `B. less than 1%` |
| baseline | `mmlu_7382` | `mcq` | true | `A` | `A. differences in gene expression which may establish a pattern in the embryo as the cells divide` |
| baseline | `mmlu_7383` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7384` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7385` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7386` | `mcq` | true | `D` | `D. 451 degrees` |
| baseline | `mmlu_7387` | `mcq` | false | `C` | `D. Grape` |
| baseline | `mmlu_7388` | `mcq` | true | `B` | `B. Meriwether and William` |
| baseline | `mmlu_7389` | `mcq` | true | `C` | `C. Guided reading` |
| baseline | `mmlu_7390` | `mcq` | true | `C` | `C. the chicken pox virus` |
| baseline | `mmlu_7391` | `mcq` | true | `A` | `A. Copper` |
| baseline | `mmlu_7392` | `mcq` | true | `A` | `A. sophomore` |
| baseline | `mmlu_7393` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7394` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7395` | `mcq` | false | `B` | `D. Dwight Eisenhower` |
| baseline | `mmlu_7396` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7397` | `mcq` | true | `B` | `B. New plant varieties being patented` |
| baseline | `mmlu_7398` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7399` | `mcq` | false | `B` | `D. Groundhog Day` |
| baseline | `mmlu_7400` | `mcq` | true | `A` | `A. A grayish, milky fluid` |
| baseline | `mmlu_7401` | `mcq` | false | `A` | `B. rabbit` |
| baseline | `mmlu_7402` | `mcq` | true | `A` | `A. Beater` |
| baseline | `mmlu_7403` | `mcq` | true | `A` | `A. Ireland` |
| baseline | `mmlu_7404` | `mcq` | true | `D` | `D. Evaporation from the ocean surface` |
| baseline | `mmlu_7405` | `mcq` | true | `A` | `A. Cannes` |
| baseline | `mmlu_7406` | `mcq` | false | `C` | `A. Yahtzee` |
| baseline | `mmlu_7407` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7408` | `mcq` | true | `D` | `D. Friday the 13th'` |
| baseline | `mmlu_7409` | `mcq` | false | `C` | `A. Miss Jackie` |
| baseline | `mmlu_7410` | `mcq` | true | `C` | `C. bird` |
| baseline | `mmlu_7411` | `mcq` | true | `C` | `C. Stomach` |
| baseline | `mmlu_7412` | `mcq` | false | `D` | `C. Red` |
| baseline | `mmlu_7413` | `mcq` | true | `A` | `A. 0 degrees or below` |
| baseline | `mmlu_7414` | `mcq` | false | `D` | `A. cat` |
| baseline | `mmlu_7415` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7416` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7417` | `mcq` | true | `D` | `D. 6 mol` |
| baseline | `mmlu_7418` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7419` | `mcq` | true | `C` | `C. to make holes` |
| baseline | `mmlu_7420` | `mcq` | true | `C` | `C. Carpals` |
| baseline | `mmlu_7421` | `mcq` | true | `D` | `D. calf` |
| baseline | `mmlu_7422` | `mcq` | true | `B` | `B. Fendi` |
| baseline | `mmlu_7423` | `mcq` | true | `B` | `B. increasing on-task behavior in the classroom` |
| baseline | `mmlu_7424` | `mcq` | true | `C` | `C. Spain` |
| baseline | `mmlu_7425` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7426` | `mcq` | false | `B` | `C. Emptying the gas tank` |
| baseline | `mmlu_7427` | `mcq` | true | `C` | `C. Thrust` |
| baseline | `mmlu_7428` | `mcq` | true | `D` | `D. Jupiter` |
| baseline | `mmlu_7429` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7430` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7431` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7432` | `mcq` | true | `C` | `C. 10,000 liters` |
| baseline | `mmlu_7433` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7434` | `mcq` | true | `B` | `B. work without pay` |
| baseline | `mmlu_7435` | `mcq` | true | `A` | `A. blue whale` |
| baseline | `mmlu_7436` | `mcq` | true | `C` | `C. Sanskrit` |
| baseline | `mmlu_7437` | `mcq` | true | `C` | `C. right` |
| baseline | `mmlu_7438` | `mcq` | false | `B` | `A. quick exposure time` |
| baseline | `mmlu_7439` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7440` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7441` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7442` | `mcq` | true | `B` | `B. flat bread` |
| baseline | `mmlu_7443` | `mcq` | false | `B` | `A. St Augustine Florida` |
| baseline | `mmlu_7444` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7445` | `mcq` | false | `C` | `D. Law` |
| baseline | `mmlu_7446` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7447` | `mcq` | true | `D` | `D. Foreshortening` |
| baseline | `mmlu_7448` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7449` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7450` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7451` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7452` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7453` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7454` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7455` | `mcq` | true | `C` | `C. 10` |
| baseline | `mmlu_7456` | `mcq` | true | `B` | `B. Triangle` |
| baseline | `mmlu_7457` | `mcq` | true | `B` | `B. knife` |
| baseline | `mmlu_7458` | `mcq` | true | `C` | `C. stroll` |
| baseline | `mmlu_7459` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7460` | `mcq` | true | `B` | `B. gamma` |
| baseline | `mmlu_7461` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7462` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7463` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7464` | `mcq` | false | `C` | `A. France` |
| baseline | `mmlu_7465` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7466` | `mcq` | true | `C` | `C. orange` |
| baseline | `mmlu_7467` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7468` | `mcq` | true | `C` | `C. Impasto` |
| baseline | `mmlu_7469` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7470` | `mcq` | true | `C` | `C. Japan` |
| baseline | `mmlu_7471` | `mcq` | true | `D` | `D. rice` |
| baseline | `mmlu_7472` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7473` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7474` | `mcq` | false | `B` | `A. Increased varieties of each crop planted` |
| baseline | `mmlu_7475` | `mcq` | true | `D` | `D. Sherwood Forest` |
| baseline | `mmlu_7476` | `mcq` | true | `B` | `B. four` |
| baseline | `mmlu_7477` | `mcq` | true | `D` | `D. Guatemala` |
| baseline | `mmlu_7478` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7479` | `mcq` | true | `D` | `D. Kouroi` |
| baseline | `mmlu_7480` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7481` | `mcq` | true | `C` | `C. from many one` |
| baseline | `mmlu_7482` | `mcq` | true | `B` | `B. 21-Mar` |
| baseline | `mmlu_7483` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7484` | `mcq` | true | `D` | `D. Jaguar` |
| baseline | `mmlu_7485` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7486` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7487` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7488` | `mcq` | true | `C` | `C. pro wrestling` |
| baseline | `mmlu_7489` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7490` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_7491` | `mcq` | true | `C` | `C. I and II only` |
| baseline | `mmlu_7492` | `mcq` | true | `B` | `B. Martin Luther` |
| baseline | `mmlu_7493` | `mcq` | true | `D` | `D. mercury` |
| baseline | `mmlu_7494` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7495` | `mcq` | false | `A` | `B. underproduce the good relative to the socially optimal level of output` |
| baseline | `mmlu_7496` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7497` | `mcq` | true | `A` | `A. Wendy's` |
| baseline | `mmlu_7498` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7499` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7500` | `mcq` | false | `C` | `A. Brown` |
| baseline | `mmlu_7501` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7502` | `mcq` | true | `D` | `D. Harlem Renaissance` |
| baseline | `mmlu_7503` | `mcq` | false | `B` | `A. Big Slurp` |
| baseline | `mmlu_7504` | `mcq` | true | `A` | `A. Japan` |
| baseline | `mmlu_7505` | `mcq` | true | `D` | `D. Pork` |
| baseline | `mmlu_7506` | `mcq` | true | `B` | `B. Ireland` |
| baseline | `mmlu_7507` | `mcq` | true | `B` | `B. Ivory` |
| baseline | `mmlu_7508` | `mcq` | true | `C` | `C. Liverpool` |
| baseline | `mmlu_7509` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7510` | `mcq` | true | `B` | `B. 100` |
| baseline | `mmlu_7511` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7512` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7513` | `mcq` | true | `D` | `D. North Pole` |
| baseline | `mmlu_7514` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7515` | `mcq` | true | `C` | `C. 50` |
| baseline | `mmlu_7516` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7517` | `mcq` | true | `C` | `C. frog` |
| baseline | `mmlu_7518` | `mcq` | false | `C` | `A. Lower feed efficiency` |
| baseline | `mmlu_7519` | `mcq` | true | `B` | `B. $200,000,000` |
| baseline | `mmlu_7520` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7521` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7522` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7523` | `mcq` | true | `C` | `C. red` |
| baseline | `mmlu_7524` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7525` | `mcq` | true | `C` | `C. 3` |
| baseline | `mmlu_7526` | `mcq` | false | `B` | `A. Joey` |
| baseline | `mmlu_7527` | `mcq` | false | `B` | `A. regressive` |
| baseline | `mmlu_7528` | `mcq` | true | `D` | `D. institutionalism` |
| baseline | `mmlu_7529` | `mcq` | true | `D` | `D. big toe` |
| baseline | `mmlu_7530` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7531` | `mcq` | true | `C` | `C. hemophilia` |
| baseline | `mmlu_7532` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7533` | `mcq` | true | `D` | `D. Reptiles and amphibians` |
| baseline | `mmlu_7534` | `mcq` | true | `D` | `D. Chicken pox` |
| baseline | `mmlu_7535` | `mcq` | false | `B` | `A. piggybank` |
| baseline | `mmlu_7536` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7537` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7538` | `mcq` | true | `B` | `B. a protozoan` |
| baseline | `mmlu_7539` | `mcq` | false | `B` | `C. Jeff Beck` |
| baseline | `mmlu_7540` | `mcq` | true | `B` | `B. talking to the cops` |
| baseline | `mmlu_7541` | `mcq` | true | `B` | `B. St Louis` |
| baseline | `mmlu_7542` | `mcq` | true | `B` | `B. Texas` |
| baseline | `mmlu_7543` | `mcq` | true | `B` | `B. the Gold Glove` |
| baseline | `mmlu_7544` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7545` | `mcq` | true | `D` | `D. Richard Nixon` |
| baseline | `mmlu_7546` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7547` | `mcq` | false | `B` | `A. 1 second` |
| baseline | `mmlu_7548` | `mcq` | true | `D` | `D. the working class` |
| baseline | `mmlu_7549` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7550` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7551` | `mcq` | true | `A` | `A. 6'` |
| baseline | `mmlu_7552` | `mcq` | false | `B` | `A. Rafters` |
| baseline | `mmlu_7553` | `mcq` | true | `A` | `A. China` |
| baseline | `mmlu_7554` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7555` | `mcq` | true | `C` | `C. nine` |
| baseline | `mmlu_7556` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7557` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7558` | `mcq` | true | `A` | `A. 40 years` |
| baseline | `mmlu_7559` | `mcq` | true | `A` | `A. crazy` |
| baseline | `mmlu_7560` | `mcq` | true | `B` | `B. omega` |
| baseline | `mmlu_7561` | `mcq` | true | `C` | `C. Tempo` |
| baseline | `mmlu_7562` | `mcq` | true | `A` | `A. six` |
| baseline | `mmlu_7563` | `mcq` | false | `B` | `D. green bean` |
| baseline | `mmlu_7564` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7565` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7566` | `mcq` | false | `A` | `D. serenade` |
| baseline | `mmlu_7567` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7568` | `mcq` | false | `D` | `B. Lando` |
| baseline | `mmlu_7569` | `mcq` | true | `C` | `C. Ocean floor topography and the shape of the coastline serve to amplify tidal flow at specific localities.` |
| baseline | `mmlu_7570` | `mcq` | true | `C` | `C. Hemlock` |
| baseline | `mmlu_7571` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7572` | `mcq` | true | `C` | `C. the weathering of continental rocks` |
| baseline | `mmlu_7573` | `mcq` | true | `D` | `D. Pinch hitter` |
| baseline | `mmlu_7574` | `mcq` | true | `C` | `C. Argentina` |
| baseline | `mmlu_7575` | `mcq` | false | `C` | `A. 9` |
| baseline | `mmlu_7576` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7577` | `mcq` | false | `B` | `C. GHI` |
| baseline | `mmlu_7578` | `mcq` | false | `D` | `A. The instructional objectives` |
| baseline | `mmlu_7579` | `mcq` | false | `C` | `B. black with white spots` |
| baseline | `mmlu_7580` | `mcq` | true | `D` | `D. Israel` |
| baseline | `mmlu_7581` | `mcq` | true | `B` | `B. Casey Kasem` |
| baseline | `mmlu_7582` | `mcq` | true | `C` | `C. birds` |
| baseline | `mmlu_7583` | `mcq` | false | `B` | `A. Mysterians` |
| baseline | `mmlu_7584` | `mcq` | true | `D` | `D. Hyundai` |
| baseline | `mmlu_7585` | `mcq` | true | `C` | `C. Acceleration` |
| baseline | `mmlu_7586` | `mcq` | true | `A` | `A. Weaving` |
| baseline | `mmlu_7587` | `mcq` | true | `A` | `A. Carbon` |
| baseline | `mmlu_7588` | `mcq` | true | `B` | `B. ichthyologist` |
| baseline | `mmlu_7589` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7590` | `mcq` | false | `A` | `C. ten inches` |
| baseline | `mmlu_7591` | `mcq` | true | `B` | `B. 2` |
| baseline | `mmlu_7592` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7593` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7594` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7595` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7596` | `mcq` | true | `B` | `B. Links` |
| baseline | `mmlu_7597` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7598` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7599` | `mcq` | true | `C` | `C. six years` |
| baseline | `mmlu_7600` | `mcq` | true | `A` | `A. head` |
| baseline | `mmlu_7601` | `mcq` | true | `B` | `B. Counting` |
| baseline | `mmlu_7602` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7603` | `mcq` | true | `C` | `C. Rhea` |
| baseline | `mmlu_7604` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7605` | `mcq` | true | `C` | `C. The Fair Labor Standards Act` |
| baseline | `mmlu_7606` | `mcq` | true | `B` | `B. Chloroplast` |
| baseline | `mmlu_7607` | `mcq` | false | `D` | `A. Dallas` |
| baseline | `mmlu_7608` | `mcq` | true | `C` | `C. Homer` |
| baseline | `mmlu_7609` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7610` | `mcq` | false | `B` | `C. Book pass` |
| baseline | `mmlu_7611` | `mcq` | false | `C` | `B. 6 hours 25 minutes` |
| baseline | `mmlu_7612` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7613` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7614` | `mcq` | true | `D` | `D. San Antonio Spurs` |
| baseline | `mmlu_7615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7616` | `mcq` | true | `B` | `B. 1940s` |
| baseline | `mmlu_7617` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7618` | `mcq` | true | `B` | `B. Portfolio assessment` |
| baseline | `mmlu_7619` | `mcq` | true | `B` | `B. through a human body` |
| baseline | `mmlu_7620` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7621` | `mcq` | true | `A` | `A. Benjamin Franklin` |
| baseline | `mmlu_7622` | `mcq` | false | `B` | `A. shrimp` |
| baseline | `mmlu_7623` | `mcq` | true | `A` | `A. black` |
| baseline | `mmlu_7624` | `mcq` | true | `C` | `C. IRA` |
| baseline | `mmlu_7625` | `mcq` | true | `C` | `C. snowboarding` |
| baseline | `mmlu_7626` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7627` | `mcq` | false | `C` | `A. yellow` |
| baseline | `mmlu_7628` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7629` | `mcq` | true | `A` | `A. 1600` |
| baseline | `mmlu_7630` | `mcq` | true | `B` | `B. CO2 from fossil fuels` |
| baseline | `mmlu_7631` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7632` | `mcq` | true | `D` | `D. Bobby Riggs` |
| baseline | `mmlu_7633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7634` | `mcq` | false | `A` | `D. Dick Dastardly` |
| baseline | `mmlu_7635` | `mcq` | true | `C` | `C. goat` |
| baseline | `mmlu_7636` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7637` | `mcq` | true | `A` | `A. Waltz` |
| baseline | `mmlu_7638` | `mcq` | true | `A` | `A. Ninth` |
| baseline | `mmlu_7639` | `mcq` | true | `B` | `B. Caricature` |
| baseline | `mmlu_7640` | `mcq` | false | `D` | `B. eliminate a shortage in the market` |
| baseline | `mmlu_7641` | `mcq` | true | `D` | `D. Project your voice by relaxing the rib cage and maintaining good posture.` |
| baseline | `mmlu_7642` | `mcq` | true | `D` | `D. Personification` |
| baseline | `mmlu_7643` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7644` | `mcq` | true | `C` | `C. chocolate` |
| baseline | `mmlu_7645` | `mcq` | true | `D` | `D. A grammar guide` |
| baseline | `mmlu_7646` | `mcq` | true | `B` | `B. India` |
| baseline | `mmlu_7647` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7648` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7649` | `mcq` | true | `B` | `B. Saturn` |
| baseline | `mmlu_7650` | `mcq` | false | `B` | `C. Datek Online` |
| baseline | `mmlu_7651` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7652` | `mcq` | true | `A` | `A. 5 cents` |
| baseline | `mmlu_7653` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7654` | `mcq` | true | `A` | `A. Chicken Little` |
| baseline | `mmlu_7655` | `mcq` | false | `A` | `B. kazoo` |
| baseline | `mmlu_7656` | `mcq` | true | `A` | `A. Domain` |
| baseline | `mmlu_7657` | `mcq` | true | `A` | `A. one hour forward` |
| baseline | `mmlu_7658` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7659` | `mcq` | false | `D` | `B. Andrew Jackson` |
| baseline | `mmlu_7660` | `mcq` | false | `D` | `A. The man pays` |
| baseline | `mmlu_7661` | `mcq` | false | `C` | `A. Boston` |
| baseline | `mmlu_7662` | `mcq` | true | `A` | `A. Notre Dame` |
| baseline | `mmlu_7663` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7664` | `mcq` | true | `C` | `C. 1000000` |
| baseline | `mmlu_7665` | `mcq` | false | `B` | `A. simple` |
| baseline | `mmlu_7666` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7667` | `mcq` | true | `A` | `A. Paris` |
| baseline | `mmlu_7668` | `mcq` | true | `B` | `B. Conveyor` |
| baseline | `mmlu_7669` | `mcq` | true | `B` | `B. Primary` |
| baseline | `mmlu_7670` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7671` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7672` | `mcq` | true | `D` | `D. thousand` |
| baseline | `mmlu_7673` | `mcq` | true | `C` | `C. 186000 miles per second` |
| baseline | `mmlu_7674` | `mcq` | true | `D` | `D. King Tut` |
| baseline | `mmlu_7675` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7676` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7677` | `mcq` | true | `A` | `A. 6:00 AM` |
| baseline | `mmlu_7678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7679` | `mcq` | true | `C` | `C. Stonefish` |
| baseline | `mmlu_7680` | `mcq` | true | `A` | `A. centrifugal` |
| baseline | `mmlu_7681` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7682` | `mcq` | true | `B` | `B. meat` |
| baseline | `mmlu_7683` | `mcq` | false | `B` | `C. 18` |
| baseline | `mmlu_7684` | `mcq` | true | `D` | `D. proctologist` |
| baseline | `mmlu_7685` | `mcq` | true | `C` | `C. playing the piano` |
| baseline | `mmlu_7686` | `mcq` | true | `A` | `A. 2` |
| baseline | `mmlu_7687` | `mcq` | true | `D` | `D. France` |
| baseline | `mmlu_7688` | `mcq` | true | `B` | `B. Seven` |
| baseline | `mmlu_7689` | `mcq` | true | `B` | `B. royal flush` |
| baseline | `mmlu_7690` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7691` | `mcq` | true | `A` | `A. Bismarck` |
| baseline | `mmlu_7692` | `mcq` | true | `B` | `B. an increase in government spending` |
| baseline | `mmlu_7693` | `mcq` | true | `C` | `C. II and III only` |
| baseline | `mmlu_7694` | `mcq` | false | `A` | `B. 4*10^12 kg` |
| baseline | `mmlu_7695` | `mcq` | true | `D` | `D. Labrador retriever` |
| baseline | `mmlu_7696` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7697` | `mcq` | true | `B` | `B. in reverse` |
| baseline | `mmlu_7698` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7699` | `mcq` | true | `B` | `B. film production` |
| baseline | `mmlu_7700` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7701` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7702` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7703` | `mcq` | true | `B` | `B. Zulu` |
| baseline | `mmlu_7704` | `mcq` | true | `C` | `C. 88` |
| baseline | `mmlu_7705` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7706` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7707` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7708` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7709` | `mcq` | false | `C` | `A. Atlantis` |
| baseline | `mmlu_7710` | `mcq` | true | `C` | `C. Captain Kangaroo` |
| baseline | `mmlu_7711` | `mcq` | true | `B` | `B. courtroom` |
| baseline | `mmlu_7712` | `mcq` | false | `A` | `B. Sikh` |
| baseline | `mmlu_7713` | `mcq` | false | `A` | `B. Yanni` |
| baseline | `mmlu_7714` | `mcq` | true | `A` | `A. sea horse` |
| baseline | `mmlu_7715` | `mcq` | false | `B` | `D. 320,000` |
| baseline | `mmlu_7716` | `mcq` | false | `A` | `C. Relocation` |
| baseline | `mmlu_7717` | `mcq` | false | `C` | `D. undergo adiabatic cooling` |
| baseline | `mmlu_7718` | `mcq` | true | `B` | `B. Cronus` |
| baseline | `mmlu_7719` | `mcq` | true | `A` | `A. cancer` |
| baseline | `mmlu_7720` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7721` | `mcq` | true | `C` | `C. John Paul I` |
| baseline | `mmlu_7722` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7723` | `mcq` | true | `B` | `B. HTTP` |
| baseline | `mmlu_7724` | `mcq` | true | `B` | `B. Albuquerque` |
| baseline | `mmlu_7725` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7726` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7728` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7729` | `mcq` | true | `C` | `C. 19th` |
| baseline | `mmlu_7730` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7731` | `mcq` | true | `A` | `A. Parka` |
| baseline | `mmlu_7732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7733` | `mcq` | true | `B` | `B. Bloat` |
| baseline | `mmlu_7734` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7735` | `mcq` | true | `A` | `A. gaggle` |
| baseline | `mmlu_7736` | `mcq` | true | `C` | `C. directory assistance` |
| baseline | `mmlu_7737` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7738` | `mcq` | false | `D` | `B. up to 25000` |
| baseline | `mmlu_7739` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7740` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7741` | `mcq` | true | `B` | `B. Determining the objective` |
| baseline | `mmlu_7742` | `mcq` | true | `C` | `C. Little Jimmy Bond` |
| baseline | `mmlu_7743` | `mcq` | false | `D` | `A. Filing applications for building permits and variances` |
| baseline | `mmlu_7744` | `mcq` | false | `B` | `D. four` |
| baseline | `mmlu_7745` | `mcq` | false | `B` | `D. The Iron Sheik` |
| baseline | `mmlu_7746` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7747` | `mcq` | true | `A` | `A. To generate energy` |
| baseline | `mmlu_7748` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7749` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7750` | `mcq` | true | `C` | `C. tangelo` |
| baseline | `mmlu_7751` | `mcq` | false | `B` | `A. Frank and Bill` |
| baseline | `mmlu_7752` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7753` | `mcq` | true | `C` | `C. Wookiee` |
| baseline | `mmlu_7754` | `mcq` | false | `B` | `C. two white doves` |
| baseline | `mmlu_7755` | `mcq` | false | `A` | `C. Giant Sequoia` |
| baseline | `mmlu_7756` | `mcq` | true | `C` | `C. Brush` |
| baseline | `mmlu_7757` | `mcq` | false | `C` | `B. Air Force` |
| baseline | `mmlu_7758` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7759` | `mcq` | true | `C` | `C. Ability to identify the main idea` |
| baseline | `mmlu_7760` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7761` | `mcq` | false | `C` | `A. Two` |
| baseline | `mmlu_7762` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7763` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7764` | `mcq` | true | `B` | `B. the stockholders` |
| baseline | `mmlu_7765` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7766` | `mcq` | true | `C` | `C. Chicago` |
| baseline | `mmlu_7767` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7768` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7769` | `mcq` | true | `D` | `D. Fidelio'` |
| baseline | `mmlu_7770` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7771` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7772` | `mcq` | true | `D` | `D. quickly` |
| baseline | `mmlu_7773` | `mcq` | true | `D` | `D.刹车` |
| baseline | `mmlu_7774` | `mcq` | true | `B` | `B. thistle` |
| baseline | `mmlu_7775` | `mcq` | true | `C` | `C. $1 billion` |
| baseline | `mmlu_7776` | `mcq` | true | `D` | `D. Yogi Bear` |
| baseline | `mmlu_7777` | `mcq` | true | `D` | `D. Nyctophobia` |
| baseline | `mmlu_7778` | `mcq` | true | `B` | `B. Appropriating funds` |
| baseline | `mmlu_7779` | `mcq` | true | `B` | `B. Japan` |
| baseline | `mmlu_7780` | `mcq` | true | `B` | `B. Asia` |
| baseline | `mmlu_7781` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7782` | `mcq` | true | `A` | `A. whooping cough` |
| baseline | `mmlu_7783` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7784` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7785` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7786` | `mcq` | true | `B` | `B. the home team` |
| baseline | `mmlu_7787` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7788` | `mcq` | true | `A` | `A. 11` |
| baseline | `mmlu_7789` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7790` | `mcq` | false | `C` | `A. Pluto` |
| baseline | `mmlu_7791` | `mcq` | false | `A` | `C. Elizabeth Arden` |
| baseline | `mmlu_7792` | `mcq` | true | `B` | `B. German` |
| baseline | `mmlu_7793` | `mcq` | true | `D` | `D. meat` |
| baseline | `mmlu_7794` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7795` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7796` | `mcq` | true | `C` | `C. Funding the construction of the interstate highway system` |
| baseline | `mmlu_7797` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7798` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7799` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7800` | `mcq` | true | `C` | `C. SEC` |
| baseline | `mmlu_7801` | `mcq` | false | `A` | `C. Norm` |
| baseline | `mmlu_7802` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7803` | `mcq` | true | `A` | `A. Solid` |
| baseline | `mmlu_7804` | `mcq` | true | `C` | `C. 4.5 billion years` |
| baseline | `mmlu_7805` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7806` | `mcq` | true | `A` | `A. Grenadine` |
| baseline | `mmlu_7807` | `mcq` | true | `C` | `C. to hold a ship in place` |
| baseline | `mmlu_7808` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7809` | `mcq` | true | `D` | `D. Identifying a student to be Ethan's partner and participate in center time with him` |
| baseline | `mmlu_7810` | `mcq` | true | `A` | `A. declaring bankruptcy` |
| baseline | `mmlu_7811` | `mcq` | true | `C` | `C. ten thousand` |
| baseline | `mmlu_7812` | `mcq` | true | `A` | `A. Identifying attributes of objects` |
| baseline | `mmlu_7813` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7814` | `mcq` | true | `D` | `D. voidable` |
| baseline | `mmlu_7815` | `mcq` | false | `B` | `C. Magellan` |
| baseline | `mmlu_7816` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7817` | `mcq` | true | `B` | `B. Cow` |
| baseline | `mmlu_7818` | `mcq` | true | `A` | `A.	file transfer protocol` |
| baseline | `mmlu_7819` | `mcq` | true | `A` | `A. calligraphy` |
| baseline | `mmlu_7820` | `mcq` | true | `D` | `D. the Trinity` |
| baseline | `mmlu_7821` | `mcq` | true | `B` | `B. 1980` |
| baseline | `mmlu_7822` | `mcq` | true | `A` | `A. heredity` |
| baseline | `mmlu_7823` | `mcq` | true | `B` | `B. Silicon` |
| baseline | `mmlu_7824` | `mcq` | true | `B` | `B. Stephen King` |
| baseline | `mmlu_7825` | `mcq` | true | `D` | `D. Transam` |
| baseline | `mmlu_7826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7827` | `mcq` | true | `D` | `D. Beethoven` |
| baseline | `mmlu_7828` | `mcq` | false | `C` | `A. Chicago` |
| baseline | `mmlu_7829` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7830` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7831` | `mcq` | true | `A` | `A. Gulf of Sidra` |
| baseline | `mmlu_7832` | `mcq` | true | `D` | `D. Old Sparky` |
| baseline | `mmlu_7833` | `mcq` | true | `D` | `D. Spanish` |
| baseline | `mmlu_7834` | `mcq` | true | `A` | `A. Denny's` |
| baseline | `mmlu_7835` | `mcq` | true | `A` | `A. Corundum` |
| baseline | `mmlu_7836` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7837` | `mcq` | true | `B` | `B. identity vs. identity confusion` |
| baseline | `mmlu_7838` | `mcq` | false | `C` | `A. Paradise Lost'` |
| baseline | `mmlu_7839` | `mcq` | true | `B` | `B. pigs in a blanket` |
| baseline | `mmlu_7840` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7841` | `mcq` | true | `A` | `A. print lock` |
| baseline | `mmlu_7842` | `mcq` | true | `C` | `C. Apollos Rivoire` |
| baseline | `mmlu_7843` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7844` | `mcq` | true | `B` | `B. Luigi` |
| baseline | `mmlu_7845` | `mcq` | true | `D` | `D. Paul Anka` |
| baseline | `mmlu_7846` | `mcq` | true | `B` | `B. Mini-Me` |
| baseline | `mmlu_7847` | `mcq` | true | `D` | `D. melting` |
| baseline | `mmlu_7848` | `mcq` | true | `A` | `A. California` |
| baseline | `mmlu_7849` | `mcq` | false | `B` | `C. 30 seconds` |
| baseline | `mmlu_7850` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7851` | `mcq` | true | `A` | `A. Two` |
| baseline | `mmlu_7852` | `mcq` | false | `B` | `D. really big` |
| baseline | `mmlu_7853` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7855` | `mcq` | true | `C` | `C. 0.75` |
| baseline | `mmlu_7856` | `mcq` | false | `A` | `B. Grey Darjeeling` |
| baseline | `mmlu_7857` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7858` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7859` | `mcq` | true | `B` | `B. 74 m.p.h.` |
| baseline | `mmlu_7860` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7861` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7862` | `mcq` | true | `A` | `A. John Constable` |
| baseline | `mmlu_7863` | `mcq` | true | `A` | `A. stop` |
| baseline | `mmlu_7864` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7865` | `mcq` | true | `C` | `C. Water` |
| baseline | `mmlu_7866` | `mcq` | true | `A` | `A. France` |
| baseline | `mmlu_7867` | `mcq` | true | `C` | `C. blue whale` |
| baseline | `mmlu_7868` | `mcq` | true | `C` | `C. dog` |
| baseline | `mmlu_7869` | `mcq` | true | `B` | `B. yellow` |
| baseline | `mmlu_7870` | `mcq` | true | `C` | `C. eye` |
| baseline | `mmlu_7871` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7872` | `mcq` | false | `D` | `B. two` |
| baseline | `mmlu_7873` | `mcq` | true | `A` | `A. Nomadic` |
| baseline | `mmlu_7874` | `mcq` | true | `D` | `D. Dutch` |
| baseline | `mmlu_7875` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7876` | `mcq` | true | `B` | `B. Global division of labor` |
| baseline | `mmlu_7877` | `mcq` | true | `C` | `C. hygrometer` |
| baseline | `mmlu_7878` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7879` | `mcq` | false | `B` | `C. Lancelot` |
| baseline | `mmlu_7880` | `mcq` | true | `D` | `D. Read-Only Memory` |
| baseline | `mmlu_7881` | `mcq` | false | `C` | `D. 21` |
| baseline | `mmlu_7882` | `mcq` | false | `B` | `D. Tisha Campbell` |
| baseline | `mmlu_7883` | `mcq` | false | `A` | `C. 2000` |
| baseline | `mmlu_7884` | `mcq` | true | `B` | `B. euclidean` |
| baseline | `mmlu_7885` | `mcq` | false | `D` | `B. Marginal cost` |
| baseline | `mmlu_7886` | `mcq` | true | `C` | `C. George Orwell's 1984` |
| baseline | `mmlu_7887` | `mcq` | true | `B` | `B. Wellington` |
| baseline | `mmlu_7888` | `mcq` | true | `B` | `B. Hula Hoop` |
| baseline | `mmlu_7889` | `mcq` | false | `C` | `B. May` |
| baseline | `mmlu_7890` | `mcq` | false | `B` | `D. Shemp` |
| baseline | `mmlu_7891` | `mcq` | true | `D` | `D. palette` |
| baseline | `mmlu_7892` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7893` | `mcq` | false | `D` | `B. gold` |
| baseline | `mmlu_7894` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7895` | `mcq` | true | `D` | `D. War of 1812` |
| baseline | `mmlu_7896` | `mcq` | true | `A` | `A. pig` |
| baseline | `mmlu_7897` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7898` | `mcq` | true | `C` | `C. is more willing to take people at face value` |
| baseline | `mmlu_7899` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7900` | `mcq` | true | `D` | `D. Miriam` |
| baseline | `mmlu_7901` | `mcq` | true | `B` | `B. Pennsylvania` |
| baseline | `mmlu_7902` | `mcq` | false | `A` | `D. a goose` |
| baseline | `mmlu_7903` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7904` | `mcq` | false | `C` | `B. 8*10^23` |
| baseline | `mmlu_7905` | `mcq` | true | `A` | `A. Richard Rodgers` |
| baseline | `mmlu_7906` | `mcq` | false | `D` | `A. Sunday` |
| baseline | `mmlu_7907` | `mcq` | true | `C` | `C. Cinco de Mayo` |
| baseline | `mmlu_7908` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7909` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7910` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7911` | `mcq` | true | `D` | `D. Paul Allen` |
| baseline | `mmlu_7912` | `mcq` | true | `A` | `A. Hillary Clinton` |
| baseline | `mmlu_7913` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7914` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7915` | `mcq` | false | `B` | `A. Boat` |
| baseline | `mmlu_7916` | `mcq` | false | `A` | `D. syphilis` |
| baseline | `mmlu_7917` | `mcq` | true | `C` | `C. Uranium` |
| baseline | `mmlu_7918` | `mcq` | true | `A` | `A. Nissan` |
| baseline | `mmlu_7919` | `mcq` | true | `A` | `A. Gamma rays` |
| baseline | `mmlu_7920` | `mcq` | true | `A` | `A. Wood` |
| baseline | `mmlu_7921` | `mcq` | true | `C` | `C. Guard cell` |
| baseline | `mmlu_7922` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7923` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7924` | `mcq` | true | `B` | `B. America Online` |
| baseline | `mmlu_7925` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7926` | `mcq` | true | `C` | `C. The Netherlands` |
| baseline | `mmlu_7927` | `mcq` | true | `A` | `A. Potato` |
| baseline | `mmlu_7928` | `mcq` | false | `C` | `B. four` |
| baseline | `mmlu_7929` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7930` | `mcq` | true | `A` | `A. pink` |
| baseline | `mmlu_7931` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7932` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7933` | `mcq` | true | `C` | `C. Sioux` |
| baseline | `mmlu_7934` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7935` | `mcq` | true | `C` | `C. Price` |
| baseline | `mmlu_7936` | `mcq` | true | `A` | `A. bed sheets` |
| baseline | `mmlu_7937` | `mcq` | false | `C` | `A. Iditarod` |
| baseline | `mmlu_7938` | `mcq` | true | `A` | `A. between; among` |
| baseline | `mmlu_7939` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7940` | `mcq` | true | `B` | `B. kangaroo` |
| baseline | `mmlu_7941` | `mcq` | true | `D` | `D. warp and weft` |
| baseline | `mmlu_7942` | `mcq` | true | `C` | `C. Bones` |
| baseline | `mmlu_7943` | `mcq` | true | `C` | `C. chocolate` |
| baseline | `mmlu_7944` | `mcq` | false | `B` | `A. R chart` |
| baseline | `mmlu_7945` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7946` | `mcq` | true | `D` | `D. .exe` |
| baseline | `mmlu_7947` | `mcq` | true | `C` | `C. anagram` |
| baseline | `mmlu_7948` | `mcq` | true | `B` | `B. mitosis` |
| baseline | `mmlu_7949` | `mcq` | true | `B` | `B. rabies` |
| baseline | `mmlu_7950` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7951` | `mcq` | false | `D` | `B. laundry` |
| baseline | `mmlu_7952` | `mcq` | false | `D` | `A.蔬菜` |
| baseline | `mmlu_7953` | `mcq` | false | `B` | `A. liver` |
| baseline | `mmlu_7954` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7955` | `mcq` | true | `D` | `D. potatoes` |
| baseline | `mmlu_7956` | `mcq` | true | `B` | `B. China` |
| baseline | `mmlu_7957` | `mcq` | true | `D` | `D. IKEA` |
| baseline | `mmlu_7958` | `mcq` | true | `C` | `C. Defining the learning objectives they would like the software to meet` |
| baseline | `mmlu_7959` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7960` | `mcq` | true | `C` | `C. England` |
| baseline | `mmlu_7961` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7962` | `mcq` | true | `D` | `D. reducing immigration quotas sharply, leading to a dramatic decline in immigration` |
| baseline | `mmlu_7963` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7964` | `mcq` | true | `C` | `C. performance art` |
| baseline | `mmlu_7965` | `mcq` | false | `C` | `A. tomato juice` |
| baseline | `mmlu_7966` | `mcq` | true | `A` | `A. Spanish` |
| baseline | `mmlu_7967` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7968` | `mcq` | true | `B` | `B. oil` |
| baseline | `mmlu_7969` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7970` | `mcq` | true | `B` | `B. Creating a chart with the class that shows the many ways students in the class are similar` |
| baseline | `mmlu_7971` | `mcq` | false | `C` | `B. Two` |
| baseline | `mmlu_7972` | `mcq` | true | `D` | `D. Corona` |
| baseline | `mmlu_7973` | `mcq` | true | `C` | `C. 1950s` |
| baseline | `mmlu_7974` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7975` | `mcq` | false | `C` | `A. Canton Ohio` |
| baseline | `mmlu_7976` | `mcq` | false | `C` | `A. Order of business` |
| baseline | `mmlu_7977` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7978` | `mcq` | true | `C` | `C. 16` |
| baseline | `mmlu_7979` | `mcq` | true | `C` | `C. deficient` |
| baseline | `mmlu_7980` | `mcq` | true | `B` | `B. garnet` |
| baseline | `mmlu_7981` | `mcq` | false | `B` | `D. He kills himself` |
| baseline | `mmlu_7982` | `mcq` | false | `B` | `A. United States` |
| baseline | `mmlu_7983` | `mcq` | false | `B` | `A. Monday's child` |
| baseline | `mmlu_7984` | `mcq` | true | `B` | `B. a truck` |
| baseline | `mmlu_7985` | `mcq` | true | `B` | `B. The Daily Planet` |
| baseline | `mmlu_7986` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7987` | `mcq` | false | `A` | `B. 10^-29 %` |
| baseline | `mmlu_7988` | `mcq` | true | `D` | `D. San Francisco` |
| baseline | `mmlu_7989` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7990` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7991` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7992` | `mcq` | true | `B` | `B. Action and movement` |
| baseline | `mmlu_7993` | `mcq` | true | `C` | `C. corned beef` |
| baseline | `mmlu_7994` | `mcq` | true | `D` | `D. 10-K filings with the SEC` |
| baseline | `mmlu_7995` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7996` | `mcq` | true | `A` | `A. Eros` |
| baseline | `mmlu_7997` | `mcq` | false | `B` | `A. Multiplication` |
| baseline | `mmlu_7998` | `mcq` | true | `D` | `D. Sherman` |
| baseline | `mmlu_7999` | `mcq` | false | `B` | `A. marquetry` |
| baseline | `mmlu_8000` | `mcq` | true | `D` | `D. atheist` |
| baseline | `mmlu_8001` | `mcq` | false | `B` | `C. Bugs Bunny` |
| baseline | `mmlu_8002` | `mcq` | true | `B` | `B. chitlins` |
| baseline | `mmlu_8003` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8004` | `mcq` | true | `D` | `D. Financial Industry Regulatory Authority` |
| baseline | `mmlu_8005` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8006` | `mcq` | false | `B` | `D. 42` |
| baseline | `mmlu_8007` | `mcq` | true | `C` | `C. copperhead` |
| baseline | `mmlu_8008` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8009` | `mcq` | true | `A` | `A. red` |
| baseline | `mmlu_8010` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8011` | `mcq` | true | `D` | `D. antihistamines` |
| baseline | `mmlu_8012` | `mcq` | false | `B` | `A. Two` |
| baseline | `mmlu_8013` | `mcq` | true | `B` | `B. rapid eye movement` |
| baseline | `mmlu_8014` | `mcq` | true | `B` | `B. Prince William Sound` |
| baseline | `mmlu_8015` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8016` | `mcq` | true | `A` | `A. Describing and mapping the building types on a plat map` |
| baseline | `mmlu_8017` | `mcq` | true | `A` | `A. in glass-paneled cases` |
| baseline | `mmlu_8018` | `mcq` | true | `B` | `B. a shaker of salt` |
| baseline | `mmlu_8019` | `mcq` | true | `B` | `B. Decreasing the discount rate to member banks` |
| baseline | `mmlu_8020` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8021` | `mcq` | false | `D` | `A. red` |
| baseline | `mmlu_8022` | `mcq` | true | `D` | `D. pumice` |
| baseline | `mmlu_8023` | `mcq` | true | `C` | `C. Ann Landers` |
| baseline | `mmlu_8024` | `mcq` | true | `A` | `A. How the products and services will be priced` |
| baseline | `mmlu_8025` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8026` | `mcq` | true | `B` | `B. 33 1/3 rpm` |
| baseline | `mmlu_8027` | `mcq` | true | `B` | `B. War of 1812` |
| baseline | `mmlu_8028` | `mcq` | true | `D` | `D. Huey Dewey Louie` |
| baseline | `mmlu_8029` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8030` | `mcq` | true | `C` | `C. The site might belong to a nonprofit agency.` |
| baseline | `mmlu_8031` | `mcq` | false | `B` | `A. 11` |
| baseline | `mmlu_8032` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8033` | `mcq` | false | `D` | `C. black and white` |
| baseline | `mmlu_8034` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8035` | `mcq` | true | `B` | `B. Olympus` |
| baseline | `mmlu_8036` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8037` | `mcq` | false | `D` | `B. Jennifer Grey` |
| baseline | `mmlu_8038` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8039` | `mcq` | true | `B` | `B. trepanation` |
| baseline | `mmlu_8040` | `mcq` | false | `B` | `A. Jim Davis` |
| baseline | `mmlu_8041` | `mcq` | false | `B` | `D. guajillo` |
| baseline | `mmlu_8042` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8043` | `mcq` | true | `C` | `C. chocolate` |
| baseline | `mmlu_8044` | `mcq` | true | `B` | `B. ceramic` |
| baseline | `mmlu_8045` | `mcq` | true | `C` | `C. glaucoma` |
| baseline | `mmlu_8046` | `mcq` | true | `C` | `C. scarf` |
| baseline | `mmlu_8047` | `mcq` | true | `C` | `C. Alan Shepard` |
| baseline | `mmlu_8048` | `mcq` | true | `A` | `A. Paul McCartney` |
| baseline | `mmlu_8049` | `mcq` | true | `A` | `A. Outer core` |
| baseline | `mmlu_8050` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8051` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8052` | `mcq` | true | `A` | `A. musical instrument` |
| baseline | `mmlu_8053` | `mcq` | true | `D` | `D. French` |
| baseline | `mmlu_8054` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8055` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8056` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8057` | `mcq` | true | `B` | `B. bogey` |
| baseline | `mmlu_8058` | `mcq` | false | `C` | `B. Farrah Fawcett` |
| baseline | `mmlu_8059` | `mcq` | true | `C` | `C. George Bernard Shaw` |
| baseline | `mmlu_8060` | `mcq` | true | `D` | `D. drag racing` |
| baseline | `mmlu_8061` | `mcq` | true | `C` | `C. MTV` |
| baseline | `mmlu_8062` | `mcq` | false | `B` | `D. Fannie Mae` |
| baseline | `mmlu_8063` | `mcq` | true | `D` | `D. Internet Service Provider` |
| baseline | `mmlu_8064` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8065` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8066` | `mcq` | true | `A` | `A. Bill Viola` |
| baseline | `mmlu_8067` | `mcq` | true | `B` | `B. The sudden demise of the dinosaurs` |
| baseline | `mmlu_8068` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8069` | `mcq` | true | `C` | `C. 3 billion cups per week` |
| baseline | `mmlu_8070` | `mcq` | true | `B` | `B. New York` |
| baseline | `mmlu_8071` | `mcq` | false | `C` | `D. silver` |
| baseline | `mmlu_8072` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8073` | `mcq` | true | `B` | `B. chicken` |
| baseline | `mmlu_8074` | `mcq` | true | `B` | `B. electric current` |
| baseline | `mmlu_8075` | `mcq` | true | `A` | `A. effective depth` |
| baseline | `mmlu_8076` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8077` | `mcq` | true | `A` | `A. visa` |
| baseline | `mmlu_8078` | `mcq` | true | `A` | `A. Ganymede` |
| baseline | `mmlu_8079` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8080` | `mcq` | true | `A` | `A. Perskippity` |
| baseline | `mmlu_8081` | `mcq` | false | `A` | `C. Larrabee` |
| baseline | `mmlu_8082` | `mcq` | true | `B` | `B. trifecta` |
| baseline | `mmlu_8083` | `mcq` | true | `A` | `A. entropy` |
| baseline | `mmlu_8084` | `mcq` | false | `C` | `A. About 0.1%` |
| baseline | `mmlu_8085` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8086` | `mcq` | true | `A` | `A. transpiration` |
| baseline | `mmlu_8087` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8088` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8089` | `mcq` | true | `D` | `D. goalkeeper` |
| baseline | `mmlu_8090` | `mcq` | false | `D` | `A. California` |
| baseline | `mmlu_8091` | `mcq` | true | `C` | `C. magic carpet` |
| baseline | `mmlu_8092` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8093` | `mcq` | true | `C` | `C. hinny` |
| baseline | `mmlu_8094` | `mcq` | true | `A` | `A. Carbon dioxide` |
| baseline | `mmlu_8095` | `mcq` | false | `D` | `C. wabe` |
| baseline | `mmlu_8096` | `mcq` | false | `D` | `A. America` |
| baseline | `mmlu_8097` | `mcq` | true | `D` | `D. Espy` |
| baseline | `mmlu_8098` | `mcq` | true | `C` | `C. School` |
| baseline | `mmlu_8099` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8100` | `mcq` | true | `C` | `C. about 1000 miles per hour` |
| baseline | `mmlu_8101` | `mcq` | false | `D` | `B. Reservoir` |
| baseline | `mmlu_8102` | `mcq` | true | `C` | `C. prevent business behavior that hampers competition` |
| baseline | `mmlu_8103` | `mcq` | true | `B` | `B. 23` |
| baseline | `mmlu_8104` | `mcq` | true | `A` | `A. ENIAC` |
| baseline | `mmlu_8105` | `mcq` | true | `A` | `A. condensation` |
| baseline | `mmlu_8106` | `mcq` | true | `D` | `D. Tensional` |
| baseline | `mmlu_8107` | `mcq` | true | `B` | `B. Greenware` |
| baseline | `mmlu_8108` | `mcq` | true | `B` | `B. 1929` |
| baseline | `mmlu_8109` | `mcq` | true | `A` | `A. England` |
| baseline | `mmlu_8110` | `mcq` | true | `C` | `C. Flora` |
| baseline | `mmlu_8111` | `mcq` | true | `A` | `A. cursing them` |
| baseline | `mmlu_8112` | `mcq` | true | `B` | `B. Seine` |
| baseline | `mmlu_8113` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8114` | `mcq` | false | `A` | `B. The Attractions` |
| baseline | `mmlu_8115` | `mcq` | true | `B` | `B. Riverdale High` |
| baseline | `mmlu_8116` | `mcq` | false | `C` | `D. Chicken pot pie` |
| baseline | `mmlu_8117` | `mcq` | true | `A` | `A. Chicago` |
| baseline | `mmlu_8118` | `mcq` | true | `A` | `A. White balance` |
| baseline | `mmlu_8119` | `mcq` | false | `B` | `C. 40 mph` |
| baseline | `mmlu_8120` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8121` | `mcq` | false | `B` | `C. Pictionary` |
| baseline | `mmlu_8122` | `mcq` | false | `D` | `A. wrestling` |
| baseline | `mmlu_8123` | `mcq` | true | `C` | `C. Mixing vinegar with baking soda` |
| baseline | `mmlu_8124` | `mcq` | true | `A` | `A. Arrangement of soil particles` |
| baseline | `mmlu_8125` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8126` | `mcq` | true | `C` | `C. electric guitar` |
| baseline | `mmlu_8127` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8128` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8129` | `mcq` | true | `C` | `C. Inca` |
| baseline | `mmlu_8130` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8131` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8132` | `mcq` | true | `A` | `A. gingham` |
| baseline | `mmlu_8133` | `mcq` | true | `B` | `B. oui` |
| baseline | `mmlu_8134` | `mcq` | true | `D` | `D. hoot` |
| baseline | `mmlu_8135` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8136` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8137` | `mcq` | true | `D` | `D. Diagnosis` |
| baseline | `mmlu_8138` | `mcq` | true | `C` | `C. Sinn Fein` |
| baseline | `mmlu_8139` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8140` | `mcq` | false | `C` | `B. Correct use of incisors while eating` |
| baseline | `mmlu_8141` | `mcq` | false | `D` | `A. politics` |
| baseline | `mmlu_8142` | `mcq` | false | `D` | `B. Freckles` |
| baseline | `mmlu_8143` | `mcq` | true | `D` | `D. An extruder` |
| baseline | `mmlu_8144` | `mcq` | true | `A` | `A. stationary bicycle` |
| baseline | `mmlu_8145` | `mcq` | false | `C` | `B. Empire State Building` |
| baseline | `mmlu_8146` | `mcq` | false | `C` | `A. baking soda` |
| baseline | `mmlu_8147` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8148` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8149` | `mcq` | true | `C` | `C. The effect the plant will have on the environment` |
| baseline | `mmlu_8150` | `mcq` | true | `C` | `C. New York Yankees` |
| baseline | `mmlu_8151` | `mcq` | true | `A` | `A. Law of Inertia` |
| baseline | `mmlu_8152` | `mcq` | false | `D` | `B. Sheryl Swoopes` |
| baseline | `mmlu_8153` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8154` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8155` | `mcq` | true | `A` | `A. Zaire` |
| baseline | `mmlu_8156` | `mcq` | true | `C` | `C. Land of Enchantment'` |
| baseline | `mmlu_8157` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8158` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8159` | `mcq` | true | `A` | `A. Nautilus` |
| baseline | `mmlu_8160` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8161` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8163` | `mcq` | false | `B` | `D. Jupiter and Saturn` |
| baseline | `mmlu_8164` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8165` | `mcq` | true | `A` | `A. Philadelphia` |
| baseline | `mmlu_8166` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8167` | `mcq` | true | `A` | `A. jus in bello.` |
| baseline | `mmlu_8168` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8169` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8170` | `mcq` | true | `C` | `C. both its quantity and its quality.` |
| baseline | `mmlu_8171` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8172` | `mcq` | true | `C` | `C. somatic cell nuclear transfer` |
| baseline | `mmlu_8173` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8174` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8175` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8176` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8177` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8178` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8179` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8180` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8181` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8182` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8183` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8184` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8185` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8186` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8187` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8188` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8189` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8190` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8191` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8193` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8194` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8195` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8196` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8197` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8198` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8199` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8200` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8201` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8202` | `mcq` | false | `A` | `D. none of the above.` |
| baseline | `mmlu_8203` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8204` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8205` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8206` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8208` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8209` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8210` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8211` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8212` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8213` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8214` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8215` | `mcq` | true | `B` | `B. an actual or hypothetical social agreement of some sort.` |
| baseline | `mmlu_8216` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8217` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8218` | `mcq` | false | `B` | `D. All of the above.` |
| baseline | `mmlu_8219` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8220` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8221` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8222` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8223` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8224` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8225` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8226` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8227` | `mcq` | false | `D` | `A. murder` |
| baseline | `mmlu_8228` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8229` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8230` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8231` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8232` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8233` | `mcq` | false | `B` | `A. just war theory.` |
| baseline | `mmlu_8234` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8235` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8236` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8237` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8238` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8239` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8240` | `mcq` | true | `B` | `B. consequentialist theory` |
| baseline | `mmlu_8241` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8242` | `mcq` | true | `D` | `D. none of the above` |
| baseline | `mmlu_8243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8244` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8245` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8246` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8247` | `mcq` | true | `C` | `C. desirable as a means.` |
| baseline | `mmlu_8248` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8249` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8250` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8251` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8252` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8253` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8254` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_8255` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8256` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8257` | `mcq` | true | `B` | `B. letting die.` |
| baseline | `mmlu_8258` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8259` | `mcq` | false | `B` | `D. all of the above` |
| baseline | `mmlu_8260` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8261` | `mcq` | false | `A` | `B. by eliminating the patient's capacity for self-determination` |
| baseline | `mmlu_8262` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8263` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8264` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8265` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8266` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8267` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8268` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8269` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8270` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8271` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8272` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8273` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8274` | `mcq` | false | `C` | `D. none of the above` |
| baseline | `mmlu_8275` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8276` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8277` | `mcq` | false | `B` | `A. direct moral standing.` |
| baseline | `mmlu_8278` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8279` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8280` | `mcq` | false | `C` | `A. life.` |
| baseline | `mmlu_8281` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8282` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8283` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8284` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8285` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8286` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8287` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8288` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8289` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8290` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8291` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8292` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8293` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8294` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8295` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8297` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8298` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8299` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8300` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8301` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8302` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8303` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8304` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8305` | `mcq` | false | `C` | `D. John Stuart Mill` |
| baseline | `mmlu_8306` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8307` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8308` | `mcq` | false | `C` | `D. virtue.` |
| baseline | `mmlu_8309` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8310` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8311` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8312` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8313` | `mcq` | false | `C` | `D. all of the above` |
| baseline | `mmlu_8314` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8316` | `mcq` | true | `C` | `C. embryonic stage` |
| baseline | `mmlu_8317` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8318` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8319` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8320` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8321` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8322` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8323` | `mcq` | true | `B` | `B. honesty` |
| baseline | `mmlu_8324` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8325` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8326` | `mcq` | true | `A` | `A. causing global warming.` |
| baseline | `mmlu_8327` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8328` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8329` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8330` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8331` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8332` | `mcq` | true | `C` | `C. sentience` |
| baseline | `mmlu_8333` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8334` | `mcq` | true | `B` | `B. "ought."` |
| baseline | `mmlu_8335` | `mcq` | false | `A` | `B. minimize distorted thinking.` |
| baseline | `mmlu_8336` | `mcq` | true | `C` | `C. virtue ethics approach` |
| baseline | `mmlu_8337` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8338` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8339` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8340` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8341` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8342` | `mcq` | false | `C` | `D. all of the above.` |
| baseline | `mmlu_8343` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8344` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8345` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8346` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8347` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8348` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8349` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8350` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8351` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8353` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8354` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_8355` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8356` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8357` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8358` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8359` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8360` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8361` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8362` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8363` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8364` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8365` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8366` | `mcq` | true | `A` | `A. "good is to be done, evil to be avoided."` |
| baseline | `mmlu_8367` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8368` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8369` | `mcq` | true | `C` | `C. it would lead to a "tragedy of the commons."` |
| baseline | `mmlu_8370` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8371` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8372` | `mcq` | false | `C` | `A. "something bad"` |
| baseline | `mmlu_8373` | `mcq` | false | `C` | `B. the pursuit of justice by marking out racism, sexism, and classism.` |
| baseline | `mmlu_8374` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8376` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8377` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8378` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8379` | `mcq` | false | `C` | `D. legislators` |
| baseline | `mmlu_8380` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8381` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8382` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8383` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8384` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8385` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8386` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8387` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8388` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8389` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8390` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8391` | `mcq` | true | `D` | `D. pollution.` |
| baseline | `mmlu_8392` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8393` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8394` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8395` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8396` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8397` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8398` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8399` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8401` | `mcq` | true | `C` | `C. we do not know whether wasteful driving is wrong.` |
| baseline | `mmlu_8402` | `mcq` | true | `B` | `B. Kantianism` |
| baseline | `mmlu_8403` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8404` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8405` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8406` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8407` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8408` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8409` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8410` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8411` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8412` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8413` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8414` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8415` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8416` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8417` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8418` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8419` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8420` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8421` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8422` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8423` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8424` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8425` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8426` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8427` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8428` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8429` | `mcq` | true | `A` | `A. those who value a strong right to privacy` |
| baseline | `mmlu_8430` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8431` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8432` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8433` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8434` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8435` | `mcq` | true | `C` | `C. membership in a legitimate self-governing community.` |
| baseline | `mmlu_8436` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8437` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8438` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8439` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8440` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8441` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8442` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8443` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8444` | `mcq` | false | `B` | `D. A and B are equally good athletes.` |
| baseline | `mmlu_8445` | `mcq` | false | `D` | `C. both causal and expressive harm` |
| baseline | `mmlu_8446` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8447` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8448` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8449` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8450` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8451` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8452` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8453` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8454` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8455` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8456` | `mcq` | true | `C` | `C. consider such speech hate speech.` |
| baseline | `mmlu_8457` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8458` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8459` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8460` | `mcq` | false | `B` | `C. dichotomous thinking` |
| baseline | `mmlu_8461` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8462` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8463` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8464` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8465` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8466` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8467` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8468` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8470` | `mcq` | true | `C` | `C. active/passive euthanasia` |
| baseline | `mmlu_8471` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8472` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8473` | `mcq` | true | `D` | `D. dignity.` |
| baseline | `mmlu_8474` | `mcq` | true | `C` | `C. distributive` |
| baseline | `mmlu_8475` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8476` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8477` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8478` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8479` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8480` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8481` | `mcq` | true | `A` | `A. exclude` |
| baseline | `mmlu_8482` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8483` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8484` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8485` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8486` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8487` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8488` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8489` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8490` | `mcq` | false | `B` | `A. freedom of speech` |
| baseline | `mmlu_8491` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8492` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8493` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8494` | `mcq` | true | `A` | `A. The SCNT individual has genetic material primarily from one person instead of two.` |
| baseline | `mmlu_8495` | `mcq` | false | `C` | `D. all of the above` |
| baseline | `mmlu_8496` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8497` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8498` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8499` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8500` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8501` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8502` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8503` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8504` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8505` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8506` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8507` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8508` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8509` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8510` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8512` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8513` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8514` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8515` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8516` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8517` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8518` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8519` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8520` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8521` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8522` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8523` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8524` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8525` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8526` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8527` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8528` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8529` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8530` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8531` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8532` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8533` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8534` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8535` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8536` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8537` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8538` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8539` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8540` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8541` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8542` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8543` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8544` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8545` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8546` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8547` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8548` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8549` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8550` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8551` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8552` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8553` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8554` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8555` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8556` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8557` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8558` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8559` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8560` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8561` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8562` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8563` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8564` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8565` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8566` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8567` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8568` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8569` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8570` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8571` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8572` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8573` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8574` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8575` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8576` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8577` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8578` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8579` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8580` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8581` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8582` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8583` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8584` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8585` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8586` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8587` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8588` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8589` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8590` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8591` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8592` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8593` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8594` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8595` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8596` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8597` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8598` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8599` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8600` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8601` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8602` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8603` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8604` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8605` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8606` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8607` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8608` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8609` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8610` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8611` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8612` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8613` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8614` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8615` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8616` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8617` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8618` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8619` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8620` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8621` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8622` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8623` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8624` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8625` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8626` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8627` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8628` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8629` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8630` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8631` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8632` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8633` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8634` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8635` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8636` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8637` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8638` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8639` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8640` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8641` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8642` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8643` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8644` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8645` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8646` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8647` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8648` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8649` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8650` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8651` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8652` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8653` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8654` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8655` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8656` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8657` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8658` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8659` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8660` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8661` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8662` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8663` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8664` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8665` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8666` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8667` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8668` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8669` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8670` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8671` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8672` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8673` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8674` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8675` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8676` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8677` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8678` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8679` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8680` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8681` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8682` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8683` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8684` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8685` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8686` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8687` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8688` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8689` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8690` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8691` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8692` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8693` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8694` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8695` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8696` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8697` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8698` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8699` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8700` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8701` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8702` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8703` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8704` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8705` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8706` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8707` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8708` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8709` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8710` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8711` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8712` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8713` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8714` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8715` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8716` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8717` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8718` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8719` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8720` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8721` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8722` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8723` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8724` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8725` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8726` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8727` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8728` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8729` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8730` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8731` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8732` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8733` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8734` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8735` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8736` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8737` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8738` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8739` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8740` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8741` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8742` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8743` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8744` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8745` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8746` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8747` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8748` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8749` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8750` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8751` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8752` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8753` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8754` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8755` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8756` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8757` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8758` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8759` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8760` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8761` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8762` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8763` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8764` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8765` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8766` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8767` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8768` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8769` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8770` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8771` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8772` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8773` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8774` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8775` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8776` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8777` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8778` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8779` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8780` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8781` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8782` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8783` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8784` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8785` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8786` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8787` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8788` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8789` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8790` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8791` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8792` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8793` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8794` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8795` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8796` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8797` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8798` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8799` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8800` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8801` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8802` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8803` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8804` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8805` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8806` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8807` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8808` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8809` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8810` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8811` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8812` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8813` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8814` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8815` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8816` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8817` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8818` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8819` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8820` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8821` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8822` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8823` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8824` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8825` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8826` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8827` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8828` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8829` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8830` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8831` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8832` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8833` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8834` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8835` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8836` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8837` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8838` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8839` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8840` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8841` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8842` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8843` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8844` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8845` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8846` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8847` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8848` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8849` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8850` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8851` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8852` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8853` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8854` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8855` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8856` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8857` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8858` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8859` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8860` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8861` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8862` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8863` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8864` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8865` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8866` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8867` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8868` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8869` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8870` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8871` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8872` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8873` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8874` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8875` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8876` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8877` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8878` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8879` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8880` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8881` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8882` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8883` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8884` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8885` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8886` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8887` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8888` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8889` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8890` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8891` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8892` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8893` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8894` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8895` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8896` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8897` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8898` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8899` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8900` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8901` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8902` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8903` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8904` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8905` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8906` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8907` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8908` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8909` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8910` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8911` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8912` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8913` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8914` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8915` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8916` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8917` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8918` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8919` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8920` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8921` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8922` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8923` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8924` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8925` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8926` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8927` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8928` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8929` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8930` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8931` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8932` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8933` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8934` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8935` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8936` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8937` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8938` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8939` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8940` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8941` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8942` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8943` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8944` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8945` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8946` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8947` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8948` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8949` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8950` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8951` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8952` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8953` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8954` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8955` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8956` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8957` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8958` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8959` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8960` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8961` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8962` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8963` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8964` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8965` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8966` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8967` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8968` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8969` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8970` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8971` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8972` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8973` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8974` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8975` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8976` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8977` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8978` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8979` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8980` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8981` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8982` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8983` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8984` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8985` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8986` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8987` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8988` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8989` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8990` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8991` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8992` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8993` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8994` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8995` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8996` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8997` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8998` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8999` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9000` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9001` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9002` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9003` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9004` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9005` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9006` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9007` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9008` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9009` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9010` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9011` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9012` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9013` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9014` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9015` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9016` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9017` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9018` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9019` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9020` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9021` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9022` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9023` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9024` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9025` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9026` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9027` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9028` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9029` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9030` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9031` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9032` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9033` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9034` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9035` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9036` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9037` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9038` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9039` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9040` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9041` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9042` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9043` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9044` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9045` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9046` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9047` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9048` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9049` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9050` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9051` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9052` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9053` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9054` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9055` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9056` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9057` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9058` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9059` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9060` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9061` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9062` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9063` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9064` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9065` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9066` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9067` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9068` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9069` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9070` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9071` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9072` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9073` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9074` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9075` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9076` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9077` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9078` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9079` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9080` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9081` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9082` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9083` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9084` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9085` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9086` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9087` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9088` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9089` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9090` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9091` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9092` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9093` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9094` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9095` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9096` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9097` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9098` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9099` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9100` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9101` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9102` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9103` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9104` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9105` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9106` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9107` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9108` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9109` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9110` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9111` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9112` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9113` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9114` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9115` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9116` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9117` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9118` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9119` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9120` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9121` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9122` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9123` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9124` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9125` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9126` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9127` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9128` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9129` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9130` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9131` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9132` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9133` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9134` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9135` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9136` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9137` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9138` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9139` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9140` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9141` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9142` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9143` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9144` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9145` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9146` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9147` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9148` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9149` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9150` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9151` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9152` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9153` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9154` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9155` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9156` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9157` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9158` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9159` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9160` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9161` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9162` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9163` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9164` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9165` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9166` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9167` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9168` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9169` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9170` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9171` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9172` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9173` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9174` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9175` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9176` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9177` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9178` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9179` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9180` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9181` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9182` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9183` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9184` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9185` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9186` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9187` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9188` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9189` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9190` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9191` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9192` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9193` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9194` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9195` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9196` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9197` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9198` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9199` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9200` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9201` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9202` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9203` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9204` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9205` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9206` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9207` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9208` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9209` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9210` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9211` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9212` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9213` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9214` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9215` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9216` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9217` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9218` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9219` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9220` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9221` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9222` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9223` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9224` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9225` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9226` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9227` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9228` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9229` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9230` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9231` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9232` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9233` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9234` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9235` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9236` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9237` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9238` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9239` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9240` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9241` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9242` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9243` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9244` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9245` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9246` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9247` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9248` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9249` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9250` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9251` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9252` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9253` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9254` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9255` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9256` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9257` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9258` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9259` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9260` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9261` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9262` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9263` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9264` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9265` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9266` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9267` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9268` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9269` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9270` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9271` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9272` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9273` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9274` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9275` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9276` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9277` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9278` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9279` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9280` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9281` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9282` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9283` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9284` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9285` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9286` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9287` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9288` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9289` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9290` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9291` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9292` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9293` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9294` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9295` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9296` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9297` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9298` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9299` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9300` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9301` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9302` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9303` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9304` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9305` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9306` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9307` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9308` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9309` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9310` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9311` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9312` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9313` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9314` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9315` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9316` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9317` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9318` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9319` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9320` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9321` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9322` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9323` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9324` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9325` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9326` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9327` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9328` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9329` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9330` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9331` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9332` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9333` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9334` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9335` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9336` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9337` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9338` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9339` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9340` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9341` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9342` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9343` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9344` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9345` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9346` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9347` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9348` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9349` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9350` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9351` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9352` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9353` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9354` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9355` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9356` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9357` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9358` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9359` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9360` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9361` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9362` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9363` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9364` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9365` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9366` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9367` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9368` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9369` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9370` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9371` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9372` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9373` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9374` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9375` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9376` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9377` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9378` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9379` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9380` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9381` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9382` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9383` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9384` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_9385` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9386` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9387` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9388` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9389` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9390` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9391` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9392` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9393` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9394` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9395` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9396` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_9397` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9398` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9399` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9400` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9401` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_9402` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9403` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9404` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9405` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9406` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_9407` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9408` | `mcq` | false | `C` | `A. Meat` |
| baseline | `mmlu_9409` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9410` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9411` | `mcq` | true | `A` | `A. Increased energy quantity/density and a more sedentary life-style` |
| baseline | `mmlu_9412` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9413` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_9414` | `mcq` | true | `B` | `B. Oestrogen` |
| baseline | `mmlu_9415` | `mcq` | true | `B` | `B. Vitamin D` |
| baseline | `mmlu_9416` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9417` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9418` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9419` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9420` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9421` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9422` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9423` | `mcq` | true | `B` | `B. Long chain (=20 carbons) saturated and n-3 polyunsaturated fatty acids` |
| baseline | `mmlu_9424` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9425` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9426` | `mcq` | true | `A` | `A. China` |
| baseline | `mmlu_9427` | `mcq` | false | `D` | `A. Happy heart syndrome` |
| baseline | `mmlu_9428` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9429` | `mcq` | false | `A` | `D. Oxygen 18` |
| baseline | `mmlu_9430` | `mcq` | true | `C` | `C. Both of the options given are correct.` |
| baseline | `mmlu_9431` | `mcq` | true | `D` | `D. All of the options given are correct` |
| baseline | `mmlu_9432` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9434` | `mcq` | false | `D` | `A. Liver glycogen` |
| baseline | `mmlu_9435` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9436` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9437` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_9438` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9439` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9440` | `mcq` | true | `C` | `C. Urea` |
| baseline | `mmlu_9441` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9442` | `mcq` | false | `D` | `B. Because the accuracy of some laboratory assays may be compromised in samples from people who are sick.` |
| baseline | `mmlu_9443` | `mcq` | false | `B` | `A. 3%` |
| baseline | `mmlu_9444` | `mcq` | false | `D` | `A. Processed meat` |
| baseline | `mmlu_9445` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9446` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9447` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9448` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9449` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9450` | `mcq` | true | `C` | `C. Salt and salt-preserved foods` |
| baseline | `mmlu_9451` | `mcq` | false | `C` | `A. Alcohol dehydrogenase (ADH)` |
| baseline | `mmlu_9452` | `mcq` | false | `D` | `A. day-to-day basis` |
| baseline | `mmlu_9453` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9454` | `mcq` | true | `B` | `B. 70%-75%` |
| baseline | `mmlu_9455` | `mcq` | true | `A` | `A. Biotin` |
| baseline | `mmlu_9456` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9457` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9458` | `mcq` | false | `C` | `D. All of the above` |
| baseline | `mmlu_9459` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9460` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9461` | `mcq` | false | `B` | `A. Niacin` |
| baseline | `mmlu_9462` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9463` | `mcq` | true | `D` | `D. Benzodizepines (Diazepam, Alprazolam)` |
| baseline | `mmlu_9464` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9465` | `mcq` | true | `D` | `D. Bound to transferrin` |
| baseline | `mmlu_9466` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9467` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9468` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9469` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_9470` | `mcq` | true | `D` | `D. all of the options given are correct` |
| baseline | `mmlu_9471` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9472` | `mcq` | true | `C` | `C. Increased body fat` |
| baseline | `mmlu_9473` | `mcq` | true | `C` | `C. Meat and meat products` |
| baseline | `mmlu_9474` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9475` | `mcq` | true | `A` | `A. Salmonella and Campylobacter` |
| baseline | `mmlu_9476` | `mcq` | true | `A` | `A. 80-90%` |
| baseline | `mmlu_9477` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9478` | `mcq` | true | `B` | `B. ALDH2` |
| baseline | `mmlu_9479` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9480` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9481` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9482` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9483` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9484` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9485` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9486` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9487` | `mcq` | false | `C` | `A. glucose` |
| baseline | `mmlu_9488` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9489` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9490` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9491` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9492` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9493` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9494` | `mcq` | true | `A` | `A. First trimester of pregnancy.` |
| baseline | `mmlu_9495` | `mcq` | true | `C` | `C. Adaptive thermogenesis` |
| baseline | `mmlu_9496` | `mcq` | false | `A` | `C. Lorcaserin` |
| baseline | `mmlu_9497` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9498` | `mcq` | false | `C` | `A. The presence or risk of a clinical deficiency, such as clinical scurvy.` |
| baseline | `mmlu_9499` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9500` | `mcq` | false | `C` | `A. 0.900 g/cm3` |
| baseline | `mmlu_9501` | `mcq` | true | `B` | `B. The group of people that may experience the outcome we want to study.` |
| baseline | `mmlu_9502` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9503` | `mcq` | false | `C` | `D. All of the above` |
| baseline | `mmlu_9504` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9505` | `mcq` | false | `D` | `C. Increasing muscle glycogen use during exercise` |
| baseline | `mmlu_9506` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9507` | `mcq` | false | `B` | `C. Ketone bodies` |
| baseline | `mmlu_9508` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9509` | `mcq` | true | `B` | `B. Selenocysteine` |
| baseline | `mmlu_9510` | `mcq` | true | `D` | `D. Meat and Dairy products` |
| baseline | `mmlu_9511` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9512` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9513` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9514` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9515` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9516` | `mcq` | true | `D` | `D. Both a and c` |
| baseline | `mmlu_9517` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9518` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9519` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9520` | `mcq` | false | `A` | `B. Tryptophan` |
| baseline | `mmlu_9521` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9522` | `mcq` | true | `B` | `B. Dual-energy X-ray absorptiometry` |
| baseline | `mmlu_9523` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9524` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9525` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9526` | `mcq` | true | `D` | `D. 32` |
| baseline | `mmlu_9527` | `mcq` | true | `A` | `A. When intakes exceed established ULs (Upper Levels)` |
| baseline | `mmlu_9528` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9529` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9530` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9531` | `mcq` | true | `A` | `A. potassium` |
| baseline | `mmlu_9532` | `mcq` | false | `C` | `A. 75-95%` |
| baseline | `mmlu_9533` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9534` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9535` | `mcq` | true | `A` | `A. Hemoglobin A1c` |
| baseline | `mmlu_9536` | `mcq` | false | `D` | `A. Brain` |
| baseline | `mmlu_9537` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9538` | `mcq` | true | `B` | `B. They are all derived from plant foods` |
| baseline | `mmlu_9539` | `mcq` | true | `C` | `C. The plasma activity of alkaline phosphatase` |
| baseline | `mmlu_9540` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9541` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9542` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9543` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9544` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9545` | `mcq` | false | `B` | `A. 20%` |
| baseline | `mmlu_9546` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9547` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9548` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9549` | `mcq` | true | `A` | `A. Wernicke-Korsakoff syndrome` |
| baseline | `mmlu_9550` | `mcq` | true | `C` | `C. Cytosine` |
| baseline | `mmlu_9551` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9552` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9553` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9554` | `mcq` | true | `C` | `C. Four-compartment model` |
| baseline | `mmlu_9555` | `mcq` | true | `B` | `B. Cholesterol mainly occurs in the cell walls of mammalian cells` |
| baseline | `mmlu_9556` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9557` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9558` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9559` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9560` | `mcq` | false | `B` | `A. the muscle fibre` |
| baseline | `mmlu_9561` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9562` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9563` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9564` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9565` | `mcq` | true | `C` | `C. acetaldehyde` |
| baseline | `mmlu_9566` | `mcq` | true | `C` | `C. 1 unit of BMI` |
| baseline | `mmlu_9567` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9568` | `mcq` | false | `A` | `B. Chylomicrons and VLDL` |
| baseline | `mmlu_9569` | `mcq` | true | `A` | `A. Folate` |
| baseline | `mmlu_9570` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9571` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9572` | `mcq` | true | `B` | `B. Potassium` |
| baseline | `mmlu_9573` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9574` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9575` | `mcq` | true | `B` | `B. The MUST tool` |
| baseline | `mmlu_9576` | `mcq` | false | `C` | `D. DNA polymerase` |
| baseline | `mmlu_9577` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9578` | `mcq` | true | `B` | `B. The Mediterranean diet` |
| baseline | `mmlu_9579` | `mcq` | true | `A` | `A. DNMT1` |
| baseline | `mmlu_9580` | `mcq` | false | `B` | `A. 11%` |
| baseline | `mmlu_9581` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9582` | `mcq` | false | `B` | `A. 10` |
| baseline | `mmlu_9583` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9584` | `mcq` | true | `D` | `D. vitamin C and thiamin` |
| baseline | `mmlu_9585` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9586` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9587` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9588` | `mcq` | false | `B` | `C. Reduced gluconeogenesis` |
| baseline | `mmlu_9589` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9590` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9591` | `mcq` | true | `D` | `D. All of the options given.` |
| baseline | `mmlu_9592` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9593` | `mcq` | true | `D` | `D. All of the options given are correct` |
| baseline | `mmlu_9594` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9595` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9596` | `mcq` | true | `D` | `D. Iron deficiency` |
| baseline | `mmlu_9597` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9598` | `mcq` | true | `D` | `D. all of the options given are correct` |
| baseline | `mmlu_9599` | `mcq` | true | `D` | `D. All options given are correct` |
| baseline | `mmlu_9600` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9601` | `mcq` | true | `D` | `D. C20 and C22 polyunsaturated fatty acids` |
| baseline | `mmlu_9602` | `mcq` | false | `D` | `C. Aspartate` |
| baseline | `mmlu_9603` | `mcq` | true | `A` | `A. underwater weighing` |
| baseline | `mmlu_9604` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9605` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9606` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9607` | `mcq` | false | `C` | `D. Broccoli` |
| baseline | `mmlu_9608` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9609` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9610` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9611` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9612` | `mcq` | false | `C` | `B. 5.7` |
| baseline | `mmlu_9613` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_9614` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9615` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9616` | `mcq` | true | `D` | `D. BP < 130/80, Trig <150, LDL < 100` |
| baseline | `mmlu_9617` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9618` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9619` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9620` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9621` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9622` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9623` | `mcq` | false | `B` | `A. 30 to 50%` |
| baseline | `mmlu_9624` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9625` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9626` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9627` | `mcq` | true | `C` | `C. <10%` |
| baseline | `mmlu_9628` | `mcq` | true | `D` | `D. All of the options given are correct` |
| baseline | `mmlu_9629` | `mcq` | true | `D` | `D. All of the options given are correct` |
| baseline | `mmlu_9630` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9631` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9632` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9633` | `mcq` | true | `D` | `D. All of the above were among the causes.` |
| baseline | `mmlu_9634` | `mcq` | true | `C` | `C. The daily intake of the substance by humans consuming the food` |
| baseline | `mmlu_9635` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9636` | `mcq` | true | `D` | `D. All of the options listed are correct` |
| baseline | `mmlu_9637` | `mcq` | true | `B` | `B. Children with severe malnutrition or diarrhoea` |
| baseline | `mmlu_9638` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9639` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9640` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9641` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9642` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9643` | `mcq` | true | `D` | `D. Thiamin` |
| baseline | `mmlu_9644` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9645` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9646` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9647` | `mcq` | true | `C` | `C. Weight and height` |
| baseline | `mmlu_9648` | `mcq` | true | `D` | `D. Total urinary nitrogen excretion alone` |
| baseline | `mmlu_9649` | `mcq` | true | `C` | `C. VLDL` |
| baseline | `mmlu_9650` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9651` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9652` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9653` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9654` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9655` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9656` | `mcq` | true | `B` | `B. Dietary fiber` |
| baseline | `mmlu_9657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9658` | `mcq` | true | `B` | `B. Leptin and ghrelin` |
| baseline | `mmlu_9659` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9660` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9661` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9662` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9663` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9664` | `mcq` | true | `C` | `C. High dose ß-carotene supplements` |
| baseline | `mmlu_9665` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9666` | `mcq` | true | `B` | `B. Muscle contains more water than fat` |
| baseline | `mmlu_9667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9668` | `mcq` | false | `D` | `B. Plasma free fatty acids` |
| baseline | `mmlu_9669` | `mcq` | false | `B` | `C. An additional 200 kCal throughout pregnancy` |
| baseline | `mmlu_9670` | `mcq` | true | `C` | `C. The time for blood to clot` |
| baseline | `mmlu_9671` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_9672` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9673` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9674` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9675` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9676` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9677` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9678` | `mcq` | false | `A` | `C. Zinc` |
| baseline | `mmlu_9679` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9680` | `mcq` | true | `D` | `D. Food frequency questionnaire` |
| baseline | `mmlu_9681` | `mcq` | false | `B` | `A. 29` |
| baseline | `mmlu_9682` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9683` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9684` | `mcq` | true | `D` | `D. Folate, vitamins B6 and B12` |
| baseline | `mmlu_9685` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9686` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9687` | `mcq` | true | `A` | `A. N-3 fatty acids` |
| baseline | `mmlu_9688` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9689` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9690` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9691` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9692` | `mcq` | true | `D` | `D. Cohort` |
| baseline | `mmlu_9693` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9694` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9695` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9696` | `mcq` | true | `C` | `C. Chylomicrons` |
| baseline | `mmlu_9697` | `mcq` | true | `A` | `A. Long-term intervention studies that have a large sample size with fracture as an endpoint` |
| baseline | `mmlu_9698` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9699` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9700` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9701` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9702` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9703` | `mcq` | false | `D` | `A. 60 g glucose per hour` |
| baseline | `mmlu_9704` | `mcq` | true | `B` | `B. Muscle glycogen` |
| baseline | `mmlu_9705` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9706` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9707` | `mcq` | true | `A` | `A. Acetaldehyde, acetate, Pyruvate, beta-hydroxybutyrate` |
| baseline | `mmlu_9708` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_9709` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9710` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9711` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9712` | `mcq` | true | `A` | `A. Mutans streptococci` |
| baseline | `mmlu_9713` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9714` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9715` | `mcq` | true | `D` | `D. the soul` |
| baseline | `mmlu_9716` | `mcq` | true | `D` | `D. a good will` |
| baseline | `mmlu_9717` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9718` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9719` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9721` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9722` | `mcq` | true | `A` | `A. knowledge` |
| baseline | `mmlu_9723` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9724` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9725` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9726` | `mcq` | false | `B` | `A. duty.` |
| baseline | `mmlu_9727` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9728` | `mcq` | false | `D` | `A. rational` |
| baseline | `mmlu_9729` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9730` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9731` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9732` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_9733` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9734` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9735` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9736` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9737` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9738` | `mcq` | true | `B` | `B. free and unhindered; servile and subject to hindrance` |
| baseline | `mmlu_9739` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9740` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9741` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9742` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9743` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9744` | `mcq` | true | `A` | `A. expression` |
| baseline | `mmlu_9745` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9746` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9747` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9748` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9749` | `mcq` | true | `B` | `B. the philosophical method` |
| baseline | `mmlu_9750` | `mcq` | false | `B` | `A. determine which one is objectively most pleasurable` |
| baseline | `mmlu_9751` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9752` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9753` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9754` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9755` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9756` | `mcq` | false | `C` | `B. He claims to have offered an account of just such a property.` |
| baseline | `mmlu_9757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9758` | `mcq` | true | `C` | `C. Socrates` |
| baseline | `mmlu_9759` | `mcq` | true | `D` | `D. greater and grander` |
| baseline | `mmlu_9760` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9761` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9762` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9763` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9764` | `mcq` | false | `D` | `C. loving God.` |
| baseline | `mmlu_9765` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9766` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9767` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9768` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9769` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9770` | `mcq` | true | `B` | `B. freedom of the will.` |
| baseline | `mmlu_9771` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9772` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9773` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9775` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9776` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9777` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9778` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9779` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9780` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9781` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9782` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9783` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9784` | `mcq` | true | `D` | `D. arbitrary` |
| baseline | `mmlu_9785` | `mcq` | true | `C` | `C. some good.` |
| baseline | `mmlu_9786` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9787` | `mcq` | false | `B` | `D. all of the above.` |
| baseline | `mmlu_9788` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9789` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9790` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9791` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9792` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9793` | `mcq` | true | `B` | `B. In case individuals, places, or organizations can be harmed through identification or disclosure of personal informat` |
| baseline | `mmlu_9794` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9795` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9796` | `mcq` | false | `B` | `C. both a and b.` |
| baseline | `mmlu_9797` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9798` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9799` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9800` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9801` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9802` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9803` | `mcq` | true | `C` | `C. reflecting on what we really think.` |
| baseline | `mmlu_9804` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9805` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9806` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9808` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9809` | `mcq` | true | `B` | `B. war` |
| baseline | `mmlu_9810` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9811` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9812` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9813` | `mcq` | false | `D` | `A. life.` |
| baseline | `mmlu_9814` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9815` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9816` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9817` | `mcq` | true | `A` | `A. entirely subjective` |
| baseline | `mmlu_9818` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9819` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9820` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9821` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9822` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9823` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9824` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9825` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9826` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9827` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9828` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9829` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9830` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9831` | `mcq` | true | `D` | `D. reductio ad absurdum` |
| baseline | `mmlu_9832` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9833` | `mcq` | false | `B` | `C. God.` |
| baseline | `mmlu_9834` | `mcq` | true | `D` | `D. philosophers and nonphilosophers` |
| baseline | `mmlu_9835` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9836` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9837` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9838` | `mcq` | false | `B` | `A. the external view and the internal view` |
| baseline | `mmlu_9839` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9840` | `mcq` | true | `B` | `B. common` |
| baseline | `mmlu_9841` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9842` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9843` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9844` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9845` | `mcq` | true | `A` | `A. Because to know something that is false is to know no real thing, nothing (i.e., not to know at all).` |
| baseline | `mmlu_9846` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9847` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9848` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9849` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9850` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9851` | `mcq` | true | `B` | `B. God` |
| baseline | `mmlu_9852` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9853` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_9854` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9855` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9856` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9857` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9858` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9859` | `mcq` | true | `D` | `D. no real concept at all.` |
| baseline | `mmlu_9860` | `mcq` | true | `D` | `D. no quality in things themselves` |
| baseline | `mmlu_9861` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9862` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9863` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9864` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9865` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9866` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9867` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9868` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9869` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9870` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9871` | `mcq` | true | `C` | `C. consequentialist` |
| baseline | `mmlu_9872` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9873` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9874` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9875` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9876` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9877` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9878` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9880` | `mcq` | true | `B` | `B. need not be performed before each action, but should always be kept in mind.` |
| baseline | `mmlu_9881` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9882` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9883` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9884` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9885` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9886` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9887` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9888` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9889` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9890` | `mcq` | false | `B` | `A. TRUE` |
| baseline | `mmlu_9891` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9892` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9893` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9894` | `mcq` | true | `A` | `A. pain and pleasure.` |
| baseline | `mmlu_9895` | `mcq` | true | `C` | `C. soul-body dualism` |
| baseline | `mmlu_9896` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9897` | `mcq` | true | `D` | `D. enjoyments` |
| baseline | `mmlu_9898` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9899` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9900` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9901` | `mcq` | true | `A` | `A. easily procured.` |
| baseline | `mmlu_9902` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9903` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9904` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9905` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9906` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9907` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9908` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9909` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9910` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9911` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9912` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9913` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9914` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9915` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9916` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9917` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9918` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9919` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9920` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9921` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9922` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9923` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9924` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9925` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9926` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9927` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9928` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9929` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9930` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9931` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9932` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9933` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9934` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9935` | `mcq` | true | `C` | `C. He became religious.` |
| baseline | `mmlu_9936` | `mcq` | true | `D` | `D. Legalilty` |
| baseline | `mmlu_9937` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9938` | `mcq` | true | `D` | `D. war of every man against every man.` |
| baseline | `mmlu_9939` | `mcq` | true | `C` | `C. representation` |
| baseline | `mmlu_9940` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9941` | `mcq` | true | `C` | `C. exists only in the understanding` |
| baseline | `mmlu_9942` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9943` | `mcq` | true | `C` | `C. serves some important function` |
| baseline | `mmlu_9944` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9945` | `mcq` | true | `B` | `B. man` |
| baseline | `mmlu_9946` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9947` | `mcq` | false | `A` | `D. all of the above.` |
| baseline | `mmlu_9948` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_9949` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9950` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9951` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9952` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_9953` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9954` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9955` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9956` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9957` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9958` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9959` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9960` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9961` | `mcq` | true | `C` | `C. formalism` |
| baseline | `mmlu_9962` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9963` | `mcq` | false | `B` | `C. whether it violates any duties.` |
| baseline | `mmlu_9964` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9965` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9966` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9967` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9968` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9969` | `mcq` | true | `C` | `C. both a and b.` |
| baseline | `mmlu_9970` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9971` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9972` | `mcq` | false | `A` | `B. amoralists.` |
| baseline | `mmlu_9973` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9974` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9975` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_9976` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9977` | `mcq` | true | `A` | `A. cause behavior` |
| baseline | `mmlu_9978` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9979` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9980` | `mcq` | false | `C` | `D. emotion.` |
| baseline | `mmlu_9981` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9982` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9983` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_9984` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9985` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9986` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9987` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9988` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9989` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9990` | `mcq` | true | `D` | `D. all of the above.` |
| baseline | `mmlu_9991` | `mcq` | true | `C` | `C. substance dualism` |
| baseline | `mmlu_9992` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9993` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9994` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9995` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9996` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9997` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9998` | `mcq` | true | `C` | `C. man is nothing else but what he makes of himself` |
| baseline | `mmlu_9999` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10000` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10001` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10002` | `mcq` | false | `C` | `D. whether or not one's maxim can be universalized.` |
| baseline | `mmlu_10003` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10004` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_10005` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10006` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10007` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10008` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10009` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10010` | `mcq` | true | `C` | `C. both a and b.` |
| baseline | `mmlu_10011` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10012` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10013` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10014` | `mcq` | true | `C` | `C. identity theory` |
| baseline | `mmlu_10015` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10016` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10017` | `mcq` | false | `B` | `D. very inefficiently, and are therefore not worth donating to.` |
| baseline | `mmlu_10018` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10019` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10020` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10021` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10022` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_10023` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10024` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_10025` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10026` | `mcq` | false | `A` | `D. all of the above.` |
| baseline | `mmlu_10027` | `mcq` | false | `A` | `D. All of the above` |
| baseline | `mmlu_10028` | `mcq` | false | `A` | `C. parietal art.` |
| baseline | `mmlu_10029` | `mcq` | false | `C` | `B. 500` |
| baseline | `mmlu_10030` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10031` | `mcq` | false | `C` | `B. random scratches and not a meaningful script or written language.` |
| baseline | `mmlu_10032` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10033` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10034` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10035` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10036` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10037` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10038` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10039` | `mcq` | true | `C` | `C. Lapita` |
| baseline | `mmlu_10040` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10041` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10042` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10043` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10044` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10045` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10046` | `mcq` | true | `B` | `B. Denali Complex` |
| baseline | `mmlu_10047` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_10048` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10049` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10050` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10051` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10052` | `mcq` | false | `A` | `B. 12,000 B.P.` |
| baseline | `mmlu_10053` | `mcq` | true | `D` | `D. all of the above.` |
| baseline | `mmlu_10054` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10055` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10056` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10057` | `mcq` | true | `C` | `C. primatology` |
| baseline | `mmlu_10058` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10059` | `mcq` | false | `A` | `D. all of the above` |
| baseline | `mmlu_10060` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10061` | `mcq` | true | `B` | `B. Aztec; Tenochtitlán.` |
| baseline | `mmlu_10062` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10063` | `mcq` | true | `D` | `D. modern Homo sapiens` |
| baseline | `mmlu_10064` | `mcq` | true | `D` | `D. all of the above.` |
| baseline | `mmlu_10065` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10066` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10067` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10068` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10069` | `mcq` | false | `A` | `D. all of the above` |
| baseline | `mmlu_10070` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10071` | `mcq` | false | `B` | `D. both a and c.` |
| baseline | `mmlu_10072` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10073` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10074` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10075` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10076` | `mcq` | true | `B` | `B. potatoes` |
| baseline | `mmlu_10077` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10078` | `mcq` | true | `A` | `A. Potlatch.` |
| baseline | `mmlu_10079` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10080` | `mcq` | true | `C` | `C. Scapulimancy` |
| baseline | `mmlu_10081` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10082` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10083` | `mcq` | true | `C` | `C. Mississippian` |
| baseline | `mmlu_10084` | `mcq` | true | `B` | `B. drought.` |
| baseline | `mmlu_10085` | `mcq` | true | `C` | `C. teosinte` |
| baseline | `mmlu_10086` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10087` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10088` | `mcq` | true | `D` | `D. all the above` |
| baseline | `mmlu_10089` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10090` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10091` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10092` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10093` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10094` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_10095` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10096` | `mcq` | true | `B` | `B. petroglyph.` |
| baseline | `mmlu_10097` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10098` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10099` | `mcq` | false | `B` | `D. all of the above` |
| baseline | `mmlu_10100` | `mcq` | true | `B` | `B. atlatl.` |
| baseline | `mmlu_10101` | `mcq` | true | `B` | `B. artificial selection.` |
| baseline | `mmlu_10102` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10103` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10104` | `mcq` | false | `C` | `A. 3100 B.P.` |
| baseline | `mmlu_10105` | `mcq` | true | `C` | `C. playing ritual ball games` |
| baseline | `mmlu_10106` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10107` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10108` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10109` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10110` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10111` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10112` | `mcq` | false | `C` | `D. All of the above.` |
| baseline | `mmlu_10113` | `mcq` | true | `C` | `C. a change in the environment.` |
| baseline | `mmlu_10114` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10115` | `mcq` | true | `D` | `D. catastrophist.` |
| baseline | `mmlu_10116` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_10117` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10118` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10119` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10120` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_10121` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10122` | `mcq` | false | `A` | `D. all of the above.` |
| baseline | `mmlu_10123` | `mcq` | true | `A` | `A. Mississippian` |
| baseline | `mmlu_10124` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10125` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10126` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10127` | `mcq` | true | `B` | `B. brachiation.` |
| baseline | `mmlu_10128` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10129` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10130` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10131` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10132` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10133` | `mcq` | true | `D` | `D. China.` |
| baseline | `mmlu_10134` | `mcq` | true | `D` | `D. tens of millions` |
| baseline | `mmlu_10135` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10136` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10137` | `mcq` | true | `B` | `B. Mit'a` |
| baseline | `mmlu_10138` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10139` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10140` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10141` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10142` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10143` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10144` | `mcq` | true | `B` | `B. phylogeny.` |
| baseline | `mmlu_10145` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10146` | `mcq` | true | `B` | `B. Acheulean` |
| baseline | `mmlu_10147` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10148` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10149` | `mcq` | false | `A` | `B. A forest fire burned away the dense vegetation that concealed the cemetery.` |
| baseline | `mmlu_10150` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10151` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10152` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10153` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10154` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10155` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10156` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10157` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10158` | `mcq` | true | `B` | `B. Neandertals used caves in Europe where their remains were preserved.` |
| baseline | `mmlu_10159` | `mcq` | true | `B` | `B. "if you've got it, flaunt it."` |
| baseline | `mmlu_10160` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10161` | `mcq` | true | `C` | `C. three-age system` |
| baseline | `mmlu_10162` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10163` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10164` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10165` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10166` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10167` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10168` | `mcq` | true | `A` | `A. Hang-t'u` |
| baseline | `mmlu_10169` | `mcq` | true | `B` | `B. Lacustrine; Pelagic` |
| baseline | `mmlu_10170` | `mcq` | true | `C` | `C. Thule` |
| baseline | `mmlu_10171` | `mcq` | false | `A` | `D. both b and c` |
| baseline | `mmlu_10172` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10173` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10174` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10175` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10176` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10177` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10178` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10179` | `mcq` | true | `D` | `D. all of the above.` |
| baseline | `mmlu_10180` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10181` | `mcq` | false | `D` | `B. about half way through the film` |
| baseline | `mmlu_10182` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10183` | `mcq` | true | `C` | `C. Anasazi` |
| baseline | `mmlu_10184` | `mcq` | false | `C` | `A. 80,000 B.P.` |
| baseline | `mmlu_10185` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10186` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10187` | `mcq` | true | `D` | `D. Both B and C.` |
| baseline | `mmlu_10188` | `mcq` | true | `C` | `C. ceremonial pathways and effigies of spirits and gods.` |
| baseline | `mmlu_10189` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10190` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10191` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10193` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10194` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10195` | `mcq` | true | `C` | `C. Luminescence dating and optically stimulated luminescence` |
| baseline | `mmlu_10196` | `mcq` | false | `C` | `D. both b and c` |
| baseline | `mmlu_10197` | `mcq` | true | `C` | `C. internal; external` |
| baseline | `mmlu_10198` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10199` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10200` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10201` | `mcq` | true | `A` | `A. colder; Pleistocene epoch.` |
| baseline | `mmlu_10202` | `mcq` | false | `D` | `B. stars and comets.` |
| baseline | `mmlu_10203` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10204` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10205` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10206` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10207` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10208` | `mcq` | false | `D` | `A. 10th century.` |
| baseline | `mmlu_10209` | `mcq` | false | `A` | `D. all the above` |
| baseline | `mmlu_10210` | `mcq` | true | `B` | `B. It tested the ability of human beings to adapt.` |
| baseline | `mmlu_10211` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10212` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10213` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10214` | `mcq` | true | `B` | `B. glacials.` |
| baseline | `mmlu_10215` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10216` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10217` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10218` | `mcq` | true | `C` | `C. Thule` |
| baseline | `mmlu_10219` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10220` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10221` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10223` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10224` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10225` | `mcq` | true | `C` | `C. site.` |
| baseline | `mmlu_10226` | `mcq` | true | `B` | `B. terracing` |
| baseline | `mmlu_10227` | `mcq` | true | `C` | `C. increasing awareness and importance of individual identity` |
| baseline | `mmlu_10228` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10229` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10230` | `mcq` | true | `D` | `D. khipu.` |
| baseline | `mmlu_10231` | `mcq` | true | `A` | `A.地中海` |
| baseline | `mmlu_10232` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10233` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10234` | `mcq` | true | `A` | `A. finely crafted large jade disks called bi` |
| baseline | `mmlu_10235` | `mcq` | true | `D` | `D. closed to visitors because of light and moisture damage.` |
| baseline | `mmlu_10236` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10237` | `mcq` | true | `B` | `B. south` |
| baseline | `mmlu_10238` | `mcq` | true | `D` | `D. An 8,000-member life-sized terra cotta army.` |
| baseline | `mmlu_10239` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10240` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10241` | `mcq` | false | `D` | `A. chimpanzees` |
| baseline | `mmlu_10242` | `mcq` | false | `D` | `C. sorghum, emmer, and legumes.` |
| baseline | `mmlu_10243` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10244` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10245` | `mcq` | false | `B` | `C. associations that can be established between artifacts, ecofacts, and bone.` |
| baseline | `mmlu_10246` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_10247` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10248` | `mcq` | true | `D` | `D. Mesopotamia` |
| baseline | `mmlu_10249` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10250` | `mcq` | true | `C` | `C. the foramen magnum` |
| baseline | `mmlu_10251` | `mcq` | false | `C` | `A. 4.5 million; 3.2 million` |
| baseline | `mmlu_10252` | `mcq` | false | `A` | `D. Both a and b.` |
| baseline | `mmlu_10253` | `mcq` | false | `C` | `D. slowly increased brain size and the first stone tools.` |
| baseline | `mmlu_10254` | `mcq` | true | `C` | `C. creationist` |
| baseline | `mmlu_10255` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10256` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10257` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10258` | `mcq` | false | `D` | `B. Africa` |
| baseline | `mmlu_10259` | `mcq` | true | `A` | `A. argon/argon and potassium argon dating` |
| baseline | `mmlu_10260` | `mcq` | true | `C` | `C. both humans and environmental changes.` |
| baseline | `mmlu_10261` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10262` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10263` | `mcq` | true | `A` | `A. Wallace Trench` |
| baseline | `mmlu_10264` | `mcq` | true | `A` | `A. Sheep` |
| baseline | `mmlu_10265` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10266` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10267` | `mcq` | true | `C` | `C. uniformitarianism` |
| baseline | `mmlu_10268` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10269` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10270` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10271` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10272` | `mcq` | false | `C` | `A. steadily improved.` |
| baseline | `mmlu_10273` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10274` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10275` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10276` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10277` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10278` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10279` | `mcq` | true | `C` | `C. 1450 A.D.` |
| baseline | `mmlu_10280` | `mcq` | true | `D` | `D. Sunda; Sahul` |
| baseline | `mmlu_10281` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10282` | `mcq` | true | `D` | `D. all the above` |
| baseline | `mmlu_10283` | `mcq` | false | `C` | `D. all of the above` |
| baseline | `mmlu_10284` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10285` | `mcq` | false | `A` | `D. All of the above.` |
| baseline | `mmlu_10286` | `mcq` | false | `C` | `B. Inca` |
| baseline | `mmlu_10287` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10288` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10289` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10290` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10291` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10292` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10293` | `mcq` | true | `A` | `A. sacrificed adults and occasionally children` |
| baseline | `mmlu_10294` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10295` | `mcq` | true | `D` | `D. foraging` |
| baseline | `mmlu_10296` | `mcq` | false | `C` | `D. all of the above.` |
| baseline | `mmlu_10297` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10298` | `mcq` | true | `A` | `A. forensic anthropologist` |
| baseline | `mmlu_10299` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10300` | `mcq` | true | `A` | `A. Miocene.` |
| baseline | `mmlu_10301` | `mcq` | true | `B` | `B. intelligence` |
| baseline | `mmlu_10302` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10303` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10304` | `mcq` | true | `A` | `A. chimpanzees` |
| baseline | `mmlu_10305` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10306` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10307` | `mcq` | false | `C` | `A. the height and size of its monumental architecture` |
| baseline | `mmlu_10308` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10309` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10310` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10311` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10312` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10313` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10314` | `mcq` | false | `B` | `A. the founding of the Minos dynasty and the invasion of the Mycenaeans` |
| baseline | `mmlu_10315` | `mcq` | true | `D` | `D. Clovis` |
| baseline | `mmlu_10316` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10317` | `mcq` | true | `B` | `B. Australopithecus afarensis` |
| baseline | `mmlu_10318` | `mcq` | true | `D` | `D. cave paintings` |
| baseline | `mmlu_10319` | `mcq` | true | `B` | `B. just after A.D. 1000` |
| baseline | `mmlu_10320` | `mcq` | true | `A` | `A. chiefdom` |
| baseline | `mmlu_10321` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10322` | `mcq` | false | `C` | `B. simple foragers.` |
| baseline | `mmlu_10323` | `mcq` | true | `C` | `C. how societies respond to challenges` |
| baseline | `mmlu_10324` | `mcq` | true | `D` | `D. the Adena` |
| baseline | `mmlu_10325` | `mcq` | true | `A` | `A. the Adena` |
| baseline | `mmlu_10326` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10328` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10329` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10330` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10331` | `mcq` | true | `A` | `A. Europe` |
| baseline | `mmlu_10332` | `mcq` | true | `C` | `C. Intelligence and cultural adaptations.` |
| baseline | `mmlu_10333` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10334` | `mcq` | false | `A` | `B. oppressive social and religious control based on military conquest.` |
| baseline | `mmlu_10335` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10336` | `mcq` | true | `D` | `D. All the above` |
| baseline | `mmlu_10337` | `mcq` | true | `B` | `B. dendrochronology` |
| baseline | `mmlu_10338` | `mcq` | true | `D` | `D. Asia` |
| baseline | `mmlu_10339` | `mcq` | false | `C` | `B. 100,000 years` |
| baseline | `mmlu_10340` | `mcq` | false | `C` | `A. New Guinea` |
| baseline | `mmlu_10341` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10342` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10343` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10344` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10345` | `mcq` | true | `B` | `B. a much colder climate during that time.` |
| baseline | `mmlu_10346` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10347` | `mcq` | false | `B` | `C. 5100 B.P.` |
| baseline | `mmlu_10348` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10349` | `mcq` | true | `A` | `A. 164%` |
| baseline | `mmlu_10350` | `mcq` | true | `B` | `B. No effect Understated` |
| baseline | `mmlu_10351` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10353` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10354` | `mcq` | false | `C` | `B. -$27` |
| baseline | `mmlu_10355` | `mcq` | false | `D` | `B. Understated Overstated` |
| baseline | `mmlu_10356` | `mcq` | false | `D` | `B. $104.29` |
| baseline | `mmlu_10357` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10358` | `mcq` | false | `C` | `B. $132,000` |
| baseline | `mmlu_10359` | `mcq` | false | `D` | `A. $100` |
| baseline | `mmlu_10360` | `mcq` | false | `B` | `A. $0` |
| baseline | `mmlu_10361` | `mcq` | true | `A` | `A. Engagement performance.` |
| baseline | `mmlu_10362` | `mcq` | true | `B` | `B. $22,500` |
| baseline | `mmlu_10363` | `mcq` | false | `C` | `A. $100 billion` |
| baseline | `mmlu_10364` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10365` | `mcq` | false | `C` | `B. $25,000` |
| baseline | `mmlu_10366` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10367` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10368` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10369` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10370` | `mcq` | false | `D` | `A. 600` |
| baseline | `mmlu_10371` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10372` | `mcq` | true | `C` | `C. $830,000` |
| baseline | `mmlu_10373` | `mcq` | false | `D` | `C. A contract was formed on the day Jackson received Sands' acceptance  This answer is based on the understanding that u` |
| baseline | `mmlu_10374` | `mcq` | true | `B` | `B. $1600 $2800` |
| baseline | `mmlu_10375` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10376` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10377` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10378` | `mcq` | true | `C` | `C. $82` |
| baseline | `mmlu_10379` | `mcq` | true | `B` | `B. $492,500` |
| baseline | `mmlu_10380` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10381` | `mcq` | false | `A` | `D. A B and C.` |
| baseline | `mmlu_10382` | `mcq` | true | `A` | `A. Not refer to the change in the auditor’s report.` |
| baseline | `mmlu_10383` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10384` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10385` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10386` | `mcq` | false | `C` | `B. 8.50%` |
| baseline | `mmlu_10387` | `mcq` | false | `D` | `B. 6.25 percent` |
| baseline | `mmlu_10388` | `mcq` | false | `D` | `A. $25000 $25000 $0` |
| baseline | `mmlu_10389` | `mcq` | false | `C` | `B. $5,000` |
| baseline | `mmlu_10390` | `mcq` | true | `D` | `D. $242,000` |
| baseline | `mmlu_10391` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10392` | `mcq` | true | `A` | `A. January.` |
| baseline | `mmlu_10393` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10394` | `mcq` | true | `A` | `A. Zero.` |
| baseline | `mmlu_10395` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10396` | `mcq` | false | `B` | `A. $0` |
| baseline | `mmlu_10397` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10398` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10399` | `mcq` | false | `A` | `B. (2,2),(2,3),(4,2)` |
| baseline | `mmlu_10400` | `mcq` | true | `A` | `A. $2,500` |
| baseline | `mmlu_10401` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10402` | `mcq` | false | `D` | `C. Six months.` |
| baseline | `mmlu_10403` | `mcq` | true | `C` | `C. The procedures to be applied on a particular engagement are a matter of the auditor's professional judgment.` |
| baseline | `mmlu_10404` | `mcq` | true | `D` | `D. Studio did not terminate.` |
| baseline | `mmlu_10405` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10406` | `mcq` | false | `D` | `B. $5,000,000` |
| baseline | `mmlu_10407` | `mcq` | false | `D` | `B. Developing a new fixed asset system to manage the assets and related depreciation` |
| baseline | `mmlu_10408` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10409` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10410` | `mcq` | true | `A` | `A. Make inquiries of management concerning restrictions on the availability of cash balances.` |
| baseline | `mmlu_10411` | `mcq` | false | `D` | `B. $280,000` |
| baseline | `mmlu_10412` | `mcq` | false | `A` | `B. $19,000` |
| baseline | `mmlu_10413` | `mcq` | false | `B` | `A. $0` |
| baseline | `mmlu_10414` | `mcq` | true | `C` | `C. Greater than the initial investment.` |
| baseline | `mmlu_10415` | `mcq` | true | `C` | `C. $14,000` |
| baseline | `mmlu_10416` | `mcq` | false | `C` | `B. $150,000` |
| baseline | `mmlu_10417` | `mcq` | false | `D` | `C. Facts known to the predecessor auditor that might bear on the integrity of management.` |
| baseline | `mmlu_10418` | `mcq` | false | `C` | `A. Current liabilities of $1,000,000; long-term liabilities of $1,050,000` |
| baseline | `mmlu_10419` | `mcq` | false | `B` | `A. 36000` |
| baseline | `mmlu_10420` | `mcq` | false | `C` | `B. $100,276` |
| baseline | `mmlu_10421` | `mcq` | false | `A` | `B. $16,000` |
| baseline | `mmlu_10422` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10423` | `mcq` | true | `B` | `B. $10.00` |
| baseline | `mmlu_10424` | `mcq` | true | `A` | `A. Variable sampling.` |
| baseline | `mmlu_10425` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10426` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10427` | `mcq` | false | `D` | `C. The estimated remaining useful lives of plant assets were revised upward.` |
| baseline | `mmlu_10428` | `mcq` | true | `C` | `C. Depreciation.` |
| baseline | `mmlu_10429` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10430` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10431` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10432` | `mcq` | true | `B` | `B. $2.87` |
| baseline | `mmlu_10433` | `mcq` | true | `C` | `C. $5,333` |
| baseline | `mmlu_10434` | `mcq` | true | `D` | `D. Disclose the departure from GAAP in a separate paragraph of the accountant's report.` |
| baseline | `mmlu_10435` | `mcq` | false | `A` | `C. $62.50` |
| baseline | `mmlu_10436` | `mcq` | false | `C` | `B. $7,000` |
| baseline | `mmlu_10437` | `mcq` | true | `A` | `A. Single.` |
| baseline | `mmlu_10438` | `mcq` | false | `B` | `A. $23.22` |
| baseline | `mmlu_10439` | `mcq` | false | `D` | `A. September 15, year 2.` |
| baseline | `mmlu_10440` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10441` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10442` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10443` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10444` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10445` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10446` | `mcq` | true | `B` | `B. Sunk costs` |
| baseline | `mmlu_10447` | `mcq` | false | `D` | `C. Notes to the financial statements.` |
| baseline | `mmlu_10448` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10449` | `mcq` | true | `A` | `A. Option contract.` |
| baseline | `mmlu_10450` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10451` | `mcq` | true | `C` | `C. $480,000.00` |
| baseline | `mmlu_10452` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10453` | `mcq` | true | `A` | `A. $10,000` |
| baseline | `mmlu_10454` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10455` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10456` | `mcq` | true | `A` | `A. 9.4% and 11.2%` |
| baseline | `mmlu_10457` | `mcq` | true | `B` | `B. $644,000` |
| baseline | `mmlu_10458` | `mcq` | false | `A` | `B. Yes No` |
| baseline | `mmlu_10459` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10460` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10461` | `mcq` | true | `D` | `D. Monitoring.` |
| baseline | `mmlu_10462` | `mcq` | false | `B` | `A. $50` |
| baseline | `mmlu_10463` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10464` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10465` | `mcq` | false | `A` | `B. Yes No` |
| baseline | `mmlu_10466` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10467` | `mcq` | false | `C` | `A. $40,000` |
| baseline | `mmlu_10468` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10469` | `mcq` | true | `D` | `D. Possible effects on the entity’s financial statements.` |
| baseline | `mmlu_10470` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10471` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10472` | `mcq` | false | `C` | `B. $20.18` |
| baseline | `mmlu_10473` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10474` | `mcq` | false | `D` | `B. 6.4` |
| baseline | `mmlu_10475` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10476` | `mcq` | true | `A` | `A. Lower Lower` |
| baseline | `mmlu_10477` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10478` | `mcq` | false | `B` | `C. Three years.` |
| baseline | `mmlu_10479` | `mcq` | true | `A` | `A. Acceptance of a client relationship.` |
| baseline | `mmlu_10480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10481` | `mcq` | false | `C` | `B. $61,250` |
| baseline | `mmlu_10482` | `mcq` | false | `C` | `A. $0` |
| baseline | `mmlu_10483` | `mcq` | false | `D` | `A. $0` |
| baseline | `mmlu_10484` | `mcq` | false | `B` | `A. $0` |
| baseline | `mmlu_10485` | `mcq` | false | `C` | `B. $560,000` |
| baseline | `mmlu_10486` | `mcq` | false | `D` | `A. Strict liability.` |
| baseline | `mmlu_10487` | `mcq` | false | `B` | `A. -$9,500` |
| baseline | `mmlu_10488` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10489` | `mcq` | false | `C` | `D. Tracking warranty expenses over time.` |
| baseline | `mmlu_10490` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10491` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10492` | `mcq` | false | `B` | `A. $520,000` |
| baseline | `mmlu_10493` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10494` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10495` | `mcq` | false | `D` | `A. Disclaim an opinion on the financial statements and advise the board of directors that the financial statements shoul` |
| baseline | `mmlu_10496` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10497` | `mcq` | true | `C` | `C. Benchmarking` |
| baseline | `mmlu_10498` | `mcq` | true | `A` | `A. $12.20` |
| baseline | `mmlu_10499` | `mcq` | false | `A` | `B. $118,500` |
| baseline | `mmlu_10500` | `mcq` | true | `A` | `A. Due care.` |
| baseline | `mmlu_10501` | `mcq` | false | `B` | `A. $533` |
| baseline | `mmlu_10502` | `mcq` | true | `C` | `C. Modified the review report to reflect the fact that the financial statements were presented on another comprehensive ` |
| baseline | `mmlu_10503` | `mcq` | false | `B` | `C. Special revenue Permanent` |
| baseline | `mmlu_10504` | `mcq` | true | `D` | `D. $60,000 is released.` |
| baseline | `mmlu_10505` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10506` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10507` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10508` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10509` | `mcq` | true | `A` | `A. $4,000` |
| baseline | `mmlu_10510` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10511` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10512` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10514` | `mcq` | true | `B` | `B. List of the procedures performed (or reference thereto) and Mill's findings.` |
| baseline | `mmlu_10515` | `mcq` | false | `B` | `A. $4,000 loss.` |
| baseline | `mmlu_10516` | `mcq` | false | `D` | `B. Rose only.` |
| baseline | `mmlu_10517` | `mcq` | false | `D` | `C. $8.26` |
| baseline | `mmlu_10518` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10519` | `mcq` | true | `D` | `D. Receiving reports for items received before year end but not yet recorded.` |
| baseline | `mmlu_10520` | `mcq` | false | `A` | `C. 6.98%` |
| baseline | `mmlu_10521` | `mcq` | false | `B` | `C. $14,000` |
| baseline | `mmlu_10522` | `mcq` | false | `B` | `A. As an increase in accumulated depreciation of $32000.` |
| baseline | `mmlu_10523` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10524` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10526` | `mcq` | false | `D` | `A. 0.24` |
| baseline | `mmlu_10527` | `mcq` | false | `C` | `B. $35,000 capital loss.` |
| baseline | `mmlu_10528` | `mcq` | false | `C` | `Accrue contingent liability Disclose contingent liability` |
| baseline | `mmlu_10529` | `mcq` | true | `C` | `C. $375,000` |
| baseline | `mmlu_10530` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10531` | `mcq` | false | `A` | `D. Explain to the client that the request will most likely cause the auditor to disclaim an opinion.` |
| baseline | `mmlu_10532` | `mcq` | false | `C` | `B. $175,000` |
| baseline | `mmlu_10533` | `mcq` | true | `A` | `A. Theory of constraints.` |
| baseline | `mmlu_10534` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10535` | `mcq` | false | `C` | `A. Stock price will likely decrease.` |
| baseline | `mmlu_10536` | `mcq` | false | `A` | `C. 3.40%` |
| baseline | `mmlu_10537` | `mcq` | true | `B` | `B. $25,000` |
| baseline | `mmlu_10538` | `mcq` | true | `A` | `A. $5.06` |
| baseline | `mmlu_10539` | `mcq` | false | `B` | `D. $6000 gain.` |
| baseline | `mmlu_10540` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10541` | `mcq` | true | `C` | `C. 1.125` |
| baseline | `mmlu_10542` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10543` | `mcq` | false | `A` | `C. $26,000` |
| baseline | `mmlu_10544` | `mcq` | true | `C` | `C. Perform alternative procedures to verify account balances.` |
| baseline | `mmlu_10545` | `mcq` | true | `C` | `C. 1200` |
| baseline | `mmlu_10546` | `mcq` | false | `B` | `A. $3,750,000.00` |
| baseline | `mmlu_10547` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10548` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10549` | `mcq` | false | `D` | `A. 40.00%` |
| baseline | `mmlu_10550` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10551` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10552` | `mcq` | false | `D` | `A. upward sloping` |
| baseline | `mmlu_10553` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10554` | `mcq` | false | `A` | `B. $1,600` |
| baseline | `mmlu_10555` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10556` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10557` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10558` | `mcq` | false | `B` | `C. $7,000` |
| baseline | `mmlu_10559` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10560` | `mcq` | false | `C` | `D. We should use a single metric, like the NPV or the IRR, to have a coherent comparison` |
| baseline | `mmlu_10561` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10562` | `mcq` | false | `C` | `A. $110` |
| baseline | `mmlu_10563` | `mcq` | false | `C` | `A. $2,005,000` |
| baseline | `mmlu_10564` | `mcq` | false | `D` | `A. By recognizing $10,000 in other comprehensive income.` |
| baseline | `mmlu_10565` | `mcq` | true | `B` | `B. $18.75` |
| baseline | `mmlu_10566` | `mcq` | true | `B` | `B. 8%` |
| baseline | `mmlu_10567` | `mcq` | true | `A` | `A. Yes Yes` |
| baseline | `mmlu_10568` | `mcq` | false | `B` | `C. Machinery and equipment used in a business` |
| baseline | `mmlu_10569` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10570` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10571` | `mcq` | true | `D` | `D. Ownership of processed data and costs of data migrations.` |
| baseline | `mmlu_10572` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10573` | `mcq` | false | `A` | `C. Audit the service organization's controls, assess risk, and prepare the audit plan.` |
| baseline | `mmlu_10574` | `mcq` | false | `C` | `B. $320,000` |
| baseline | `mmlu_10575` | `mcq` | true | `B` | `B. Inquiry and other procedures such as observation.` |
| baseline | `mmlu_10576` | `mcq` | false | `D` | `B. $8,250` |
| baseline | `mmlu_10577` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10578` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10579` | `mcq` | true | `D` | `D. 13.53 percent.` |
| baseline | `mmlu_10580` | `mcq` | true | `D` | `D. Expensed as incurred in the current period` |
| baseline | `mmlu_10581` | `mcq` | true | `B` | `B. $27,400` |
| baseline | `mmlu_10582` | `mcq` | false | `D` | `B. 23%` |
| baseline | `mmlu_10583` | `mcq` | false | `D` | `A. $140,000` |
| baseline | `mmlu_10584` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10585` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10586` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10587` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10588` | `mcq` | false | `C` | `B. Increase Decrease` |
| baseline | `mmlu_10589` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10590` | `mcq` | true | `A` | `A. $9,000` |
| baseline | `mmlu_10591` | `mcq` | true | `B` | `B. Inquire about the current status of transactions that were recorded on the basis of preliminary data.` |
| baseline | `mmlu_10592` | `mcq` | true | `C` | `C. 2` |
| baseline | `mmlu_10593` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10594` | `mcq` | false | `A` | `C. $283,000` |
| baseline | `mmlu_10595` | `mcq` | false | `B` | `A. 8.70%` |
| baseline | `mmlu_10596` | `mcq` | false | `D` | `B. $75000 $25000` |
| baseline | `mmlu_10597` | `mcq` | false | `C` | `B. $500` |
| baseline | `mmlu_10598` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10599` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10600` | `mcq` | true | `A` | `A. Resource providers.` |
| baseline | `mmlu_10601` | `mcq` | false | `B` | `A. $26.1 million` |
| baseline | `mmlu_10602` | `mcq` | false | `B` | `D. $17,000` |
| baseline | `mmlu_10603` | `mcq` | false | `B` | `A. Debit prepaid services and credit services expense for $30,000.` |
| baseline | `mmlu_10604` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10605` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10606` | `mcq` | true | `B` | `B. 16.7 percent` |
| baseline | `mmlu_10607` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10608` | `mcq` | false | `D` | `C. $13,800` |
| baseline | `mmlu_10609` | `mcq` | true | `B` | `B. Yes No` |
| baseline | `mmlu_10610` | `mcq` | true | `A` | `A. Notes to the financial statements.` |
| baseline | `mmlu_10611` | `mcq` | false | `B` | `A. $24,000` |
| baseline | `mmlu_10612` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10613` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10614` | `mcq` | true | `A` | `A. Arrangements regarding fees and billing.` |
| baseline | `mmlu_10615` | `mcq` | true | `A` | `A. Fair value.` |
| baseline | `mmlu_10616` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10617` | `mcq` | true | `B` | `B. 9.6 percent; 13.2 percent` |
| baseline | `mmlu_10618` | `mcq` | false | `C` | `B. $161,200` |
| baseline | `mmlu_10619` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10620` | `mcq` | false | `C` | `D. No Net present value is ($8750)` |
| baseline | `mmlu_10621` | `mcq` | false | `D` | `B. $21,000` |
| baseline | `mmlu_10622` | `mcq` | false | `B` | `A. $185,000` |
| baseline | `mmlu_10623` | `mcq` | false | `D` | `B. $25,000` |
| baseline | `mmlu_10624` | `mcq` | false | `A` | `B. Increases Decreases` |
| baseline | `mmlu_10625` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10626` | `mcq` | true | `C` | `C. Rigg Steele and Urco.` |
| baseline | `mmlu_10627` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10628` | `mcq` | false | `C` | `B. Government-wide financial statements.` |
| baseline | `mmlu_10629` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10630` | `mcq` | true | `B` | `B. Yes No` |
| baseline | `mmlu_10631` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10632` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10633` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10634` | `mcq` | true | `C` | `C. The authenticating requirement was necessary to further a compelling state interest.` |
| baseline | `mmlu_10635` | `mcq` | false | `B` | `A. He intended to kill the friend and not the daughter.` |
| baseline | `mmlu_10636` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10637` | `mcq` | false | `B` | `C. invalid, because the executive order is beyond the scope of presidential power absent congressional authorization.` |
| baseline | `mmlu_10638` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10639` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10640` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10641` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10642` | `mcq` | false | `A` | `B. Yes, because the authority to enact laws regulating real estate sales transactions occurring within the boundaries of` |
| baseline | `mmlu_10643` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10644` | `mcq` | true | `B` | `B. The court will require a greater foundation to establish the reliability of the records.` |
| baseline | `mmlu_10645` | `mcq` | true | `D` | `D. The rational basis test, because the regulation need only be related to a legitimate state interest to be valid.` |
| baseline | `mmlu_10646` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10647` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10648` | `mcq` | false | `A` | `B. The man, because the purchaser did not have actual notice of the easement at the time of acquisition.` |
| baseline | `mmlu_10649` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10650` | `mcq` | true | `A` | `A. Remand the entire case.` |
| baseline | `mmlu_10651` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10652` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10653` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10654` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10655` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10656` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10657` | `mcq` | true | `D` | `D. Yes, because the employer's claim shares common questions of law and fact with the clerk's action.` |
| baseline | `mmlu_10658` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10659` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10660` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10661` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10662` | `mcq` | true | `A` | `A. Yes, both the woman and the man can testify because it is an excited utterance exception to the hearsay rule that goe` |
| baseline | `mmlu_10663` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10664` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10665` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10666` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10667` | `mcq` | false | `A` | `B. $55,000. 00` |
| baseline | `mmlu_10668` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10669` | `mcq` | false | `A` | `D. She has a fee simple.` |
| baseline | `mmlu_10670` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10671` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10672` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10673` | `mcq` | true | `B` | `B. Equal protection problem` |
| baseline | `mmlu_10674` | `mcq` | false | `C` | `A. Yes, because the ordinance controls.` |
| baseline | `mmlu_10675` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10676` | `mcq` | false | `D` | `A. admitted, because a doctor is properly qualified as an expert in medical matters.` |
| baseline | `mmlu_10677` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10678` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10679` | `mcq` | false | `C` | `B. recover, under the doctrine of res ipsa loquitur.` |
| baseline | `mmlu_10680` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10681` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10683` | `mcq` | false | `C` | `A. The police were justified, since the rally threatened imminent violence and serious disorder.` |
| baseline | `mmlu_10684` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10685` | `mcq` | true | `B` | `B. Bob Wilson and Ted Lamar are liable jointly.` |
| baseline | `mmlu_10686` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10687` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10688` | `mcq` | false | `B` | `D. unenforceable in all respects.` |
| baseline | `mmlu_10689` | `mcq` | false | `A` | `D. The niece, because she is the residuary legatee.` |
| baseline | `mmlu_10690` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10691` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10692` | `mcq` | true | `A` | `A. Both co-defendants are guilty of felony murder, but neither is guilty of conspiracy to commit murder.` |
| baseline | `mmlu_10693` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10694` | `mcq` | true | `C` | `C. win, because it was highly probable that the friend's extreme and outrageous conduct would cause emotional distress t` |
| baseline | `mmlu_10695` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10696` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10697` | `mcq` | true | `D` | `D. inadmissible, because the owner's statement to the bookkeeper is hearsay not within any exception.` |
| baseline | `mmlu_10698` | `mcq` | false | `B` | `A. Betty // Betty` |
| baseline | `mmlu_10699` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10700` | `mcq` | false | `C` | `D. He can be convicted of both larceny and criminal mischief.` |
| baseline | `mmlu_10701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10702` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10703` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10704` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_10705` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10706` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10707` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10708` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10709` | `mcq` | false | `D` | `C. not guilty, because the commission member did not receive a thing of value, since he would have approved the variance` |
| baseline | `mmlu_10710` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10711` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10712` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10713` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10714` | `mcq` | true | `D` | `D. neither instruct the jury on the matter nor permit the supermarket's attorney to argue the matter.` |
| baseline | `mmlu_10715` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10716` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10717` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10718` | `mcq` | false | `C` | `D. not guilty, because the front door was unlocked.` |
| baseline | `mmlu_10719` | `mcq` | false | `A` | `D. No, because there was inadequate consideration for the covenant.` |
| baseline | `mmlu_10720` | `mcq` | false | `A` | `B. The investor.` |
| baseline | `mmlu_10721` | `mcq` | true | `D` | `D. No, when the medical or scientific information regarding a defect has not yet been discovered, the company will not b` |
| baseline | `mmlu_10722` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10723` | `mcq` | false | `B` | `D. Yes, because the printing company's shipping of the Thanksgiving cards on October 10 constituted a present breach of ` |
| baseline | `mmlu_10724` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10725` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10726` | `mcq` | false | `B` | `C. The enforcement provision of Section 5 of the Fourteenth Amendment.` |
| baseline | `mmlu_10727` | `mcq` | true | `D` | `D. Child Finder Company` |
| baseline | `mmlu_10728` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10729` | `mcq` | false | `A` | `C. The tenant's failure to pay any rent for the last two months was a material breach of contract that discharged the ow` |
| baseline | `mmlu_10730` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10731` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10732` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10733` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10734` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10735` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10736` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10737` | `mcq` | false | `A` | `D. inadmissible, under the Dead Man's Statute.` |
| baseline | `mmlu_10738` | `mcq` | false | `B` | `D. Murder.` |
| baseline | `mmlu_10739` | `mcq` | true | `D` | `D. No, because the defective motor switch was not discoverable by reasonable inspection.` |
| baseline | `mmlu_10740` | `mcq` | true | `C` | `C. Yes, because it is authorized by a valid treaty of the United States and is not prohibited by any provision of the Co` |
| baseline | `mmlu_10741` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10742` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10743` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10744` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10745` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10746` | `mcq` | false | `A` | `C. No, because owner owes no duty to trespassers except if it acts with willful or wanton disregard.` |
| baseline | `mmlu_10747` | `mcq` | false | `B` | `C. He exercised reasonable care under the circumstances.` |
| baseline | `mmlu_10748` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10749` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10750` | `mcq` | false | `C` | `A. The rule in Shelly's case` |
| baseline | `mmlu_10751` | `mcq` | false | `C` | `B. The farmer's failure to survey the 10-acre tract excused him from further obligations under the contract.` |
| baseline | `mmlu_10752` | `mcq` | false | `D` | `B. Yes, because the bakery detrimentally relied on the modification by making the May shipment to the restaurant.` |
| baseline | `mmlu_10753` | `mcq` | true | `C` | `C. That there is a reasonable probability that the trial's outcome would have been different if the attorney had objecte` |
| baseline | `mmlu_10754` | `mcq` | true | `D` | `D. Yes, under the rule of apparent agency.` |
| baseline | `mmlu_10755` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10756` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10757` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10758` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10759` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10760` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10761` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10762` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10763` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10764` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10765` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10766` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10767` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10768` | `mcq` | false | `D` | `A. Yes, there is clearly no diversity in that the construction company LLC and the landscaper corporation were both regi` |
| baseline | `mmlu_10769` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10770` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10771` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10772` | `mcq` | true | `A` | `A. hear the case on its merits.` |
| baseline | `mmlu_10773` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10774` | `mcq` | true | `B` | `B. proper, because it constituted a permissible inference.` |
| baseline | `mmlu_10775` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10776` | `mcq` | false | `B` | `C. excluded, because the newspaper copy does not fit within any established exception to the hearsay rule.` |
| baseline | `mmlu_10777` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10778` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10779` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10780` | `mcq` | true | `D` | `D. The man and the woman are not guilty of either conspiracy or larceny.` |
| baseline | `mmlu_10781` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10782` | `mcq` | false | `B` | `D. U.S constitution, executive agreements, treaties and federal statutes, state law` |
| baseline | `mmlu_10783` | `mcq` | false | `C` | `A. Yes, because he was in fact too intoxicated to form the intent needed to prove burglary.` |
| baseline | `mmlu_10784` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10785` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10786` | `mcq` | false | `D` | `A. equitable servitude.` |
| baseline | `mmlu_10787` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10788` | `mcq` | true | `C` | `C. No, there was no agreement to conspire to rob a bank.` |
| baseline | `mmlu_10789` | `mcq` | false | `C` | `A. The collector is entitled to nominal damages, because the coin was received in a damaged condition.` |
| baseline | `mmlu_10790` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10791` | `mcq` | true | `A` | `A. Murder.` |
| baseline | `mmlu_10792` | `mcq` | false | `D` | `A. The equal protection clause of the Fourteenth Amendment.` |
| baseline | `mmlu_10793` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10794` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10795` | `mcq` | true | `C` | `C. Submit an affidavit from the patient's expert radiologist with findings that contradict the report of the hospital's ` |
| baseline | `mmlu_10796` | `mcq` | true | `A` | `A. The agreement constituted a valid modification of their June 1 contract.` |
| baseline | `mmlu_10797` | `mcq` | false | `C` | `D. denied, because the search was incident to a lawful arrest.` |
| baseline | `mmlu_10798` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10799` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10800` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10801` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10802` | `mcq` | false | `D` | `A. the widow died.` |
| baseline | `mmlu_10803` | `mcq` | true | `C` | `C. Yes, because her testimony is relevant to the mental state necessary for the commission of the crime.` |
| baseline | `mmlu_10804` | `mcq` | false | `B` | `C. No, because the man received the letter on May 4.` |
| baseline | `mmlu_10805` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10806` | `mcq` | false | `D` | `A. Rule in Shelley's Case` |
| baseline | `mmlu_10807` | `mcq` | true | `D` | `D. Yes, because the record does not establish a valid waiver of the right to counsel.` |
| baseline | `mmlu_10808` | `mcq` | false | `C` | `A. sustained the objection, because the blood tests are not conclusive evidence of paternity.` |
| baseline | `mmlu_10809` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10810` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10811` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10812` | `mcq` | false | `A` | `D. not prevail, because the young man was engaged in theft when he was shot.` |
| baseline | `mmlu_10813` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10814` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10815` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10816` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10817` | `mcq` | false | `A` | `D. No, the deed was invalid as to both grantors because partner two stepped outside his scope of authority.` |
| baseline | `mmlu_10818` | `mcq` | false | `B` | `C. Yes, because the Eleventh Amendment bars actions against a state in federal court.` |
| baseline | `mmlu_10819` | `mcq` | false | `A` | `D. not guilty of either solicitation or conspiracy to commit murder.` |
| baseline | `mmlu_10820` | `mcq` | true | `C` | `C. No, because the painter works for the same company as the negligent workers, and he made his statements within the sc` |
| baseline | `mmlu_10821` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10822` | `mcq` | true | `A` | `A. Judgment for the store, because the mill's duties of performance would not be excused.` |
| baseline | `mmlu_10823` | `mcq` | true | `A` | `A. The cousin, based on necessity.` |
| baseline | `mmlu_10824` | `mcq` | true | `A` | `A. The landlord may recover against the tenant for past rent due.` |
| baseline | `mmlu_10825` | `mcq` | false | `D` | `A. Deny both motions and submit the case to the jury based on negligence.` |
| baseline | `mmlu_10826` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10827` | `mcq` | false | `D` | `A. The court should apply the federal common law of negligence.` |
| baseline | `mmlu_10828` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10829` | `mcq` | true | `D` | `D. Yes, because the restriction is binding on the daughter as a successor.` |
| baseline | `mmlu_10830` | `mcq` | false | `C` | `A. No crime.` |
| baseline | `mmlu_10831` | `mcq` | true | `A` | `A. No crime.` |
| baseline | `mmlu_10832` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10833` | `mcq` | false | `C` | `B. vicarious liability.` |
| baseline | `mmlu_10834` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10835` | `mcq` | false | `B` | `A. win, because the friend has a reciprocal right of first refusal.` |
| baseline | `mmlu_10836` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10837` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10838` | `mcq` | true | `D` | `D. not recover, because privity of estate does not exist between the landlord and sublessee.` |
| baseline | `mmlu_10839` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10840` | `mcq` | false | `D` | `A. Felony murder.` |
| baseline | `mmlu_10841` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10842` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10843` | `mcq` | false | `D` | `A. The privileges and immunities clause of the Fourteenth Amendment.` |
| baseline | `mmlu_10844` | `mcq` | false | `C` | `A. Licensee.` |
| baseline | `mmlu_10845` | `mcq` | true | `D` | `D. whether the statement was made during the course of and in furtherance of the conspiracy.` |
| baseline | `mmlu_10846` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10847` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10848` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10849` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10850` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10851` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10852` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10853` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10854` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10855` | `mcq` | true | `C` | `C. No, legal impossibility is not a defense to the crime of conspiracy.` |
| baseline | `mmlu_10856` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10857` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10858` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10859` | `mcq` | true | `A` | `A. Service as required by State B's rules of civil procedure.` |
| baseline | `mmlu_10860` | `mcq` | false | `B` | `C. The debt was already barred by the statute of limitations.` |
| baseline | `mmlu_10861` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10862` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10863` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10864` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10865` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10866` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10867` | `mcq` | false | `D` | `A. both indictments.` |
| baseline | `mmlu_10868` | `mcq` | true | `A` | `A. violation of procedural due process.` |
| baseline | `mmlu_10869` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10870` | `mcq` | true | `D` | `D. $75,000, or the commission equivalent of 5 percent on the sale of the property for $1,500,000, since the consummation` |
| baseline | `mmlu_10871` | `mcq` | true | `C` | `C. Yes, because it is being used to rehabilitate a witness whose credibility was attacked.` |
| baseline | `mmlu_10872` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10873` | `mcq` | false | `A` | `C. tires and bicycles.` |
| baseline | `mmlu_10874` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10875` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10876` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10877` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10878` | `mcq` | false | `A` | `D. denied, because she was sufficiently close or proximate to the crime scene to justify the warrantless search.` |
| baseline | `mmlu_10879` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10880` | `mcq` | false | `A` | `B. Yes, because the tender pet doctrine allows temporary entry to retrieve baby animals.` |
| baseline | `mmlu_10881` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10882` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10883` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10884` | `mcq` | true | `C` | `C. The mobile-home restriction would be enforceable because a common development scheme had been established for the ent` |
| baseline | `mmlu_10885` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10886` | `mcq` | false | `C` | `B. best efforts contract.` |
| baseline | `mmlu_10887` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10888` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10889` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10890` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10891` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10892` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10893` | `mcq` | true | `D` | `D. not prevail, because the husband was acting reasonably in an emergency.` |
| baseline | `mmlu_10894` | `mcq` | true | `C` | `C. No, because the elevator was under the owner's exclusive control and accidents of this nature do not ordinarily occur` |
| baseline | `mmlu_10895` | `mcq` | false | `B` | `A. admissible, under both the marital and spousal privileges.` |
| baseline | `mmlu_10896` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10897` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10898` | `mcq` | false | `D` | `C. Yes, because they were accessions.` |
| baseline | `mmlu_10899` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10900` | `mcq` | false | `A` | `D. The tenant, because the landlord has not shown good cause to terminate the tenancy.` |
| baseline | `mmlu_10901` | `mcq` | false | `C` | `D. The relationship in question is not protected by the right to privacy and is subject to a state's criminal regulation` |
| baseline | `mmlu_10902` | `mcq` | false | `B` | `D. not prevail, because the owner should not be responsible for the intentional acts of the employee.` |
| baseline | `mmlu_10903` | `mcq` | false | `C` | `B. $10,000 plus the amount due for 85 percent of the completed work on the town beach house.` |
| baseline | `mmlu_10904` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10905` | `mcq` | false | `C` | `B. Voluntary manslaughter.` |
| baseline | `mmlu_10906` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10907` | `mcq` | false | `B` | `C. Yes, because there is no diversity of citizenship between the distributor and the wholesaler.` |
| baseline | `mmlu_10908` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10909` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10910` | `mcq` | false | `C` | `B. valid, because the imposition of the school fee is substantially related to a legitimate governmental interest.` |
| baseline | `mmlu_10911` | `mcq` | false | `A` | `D. the friend, the son, the daughter, and any additional children of the sister born within 21 years after the death of ` |
| baseline | `mmlu_10912` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10913` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10914` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10915` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10916` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10917` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10918` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10919` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10920` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10921` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10922` | `mcq` | false | `B` | `A. negative easement.` |
| baseline | `mmlu_10923` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10924` | `mcq` | true | `A` | `A. Yes, his use of a deadly weapon demonstrated the requisite intent to kill.` |
| baseline | `mmlu_10925` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10926` | `mcq` | false | `D` | `A. sustained the objection bc butler's testimony would be violative of hearsay rule.` |
| baseline | `mmlu_10927` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10928` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10929` | `mcq` | false | `A` | `D. unsuccessful, because the man did not intend to shoot the customer.` |
| baseline | `mmlu_10930` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10931` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10932` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10933` | `mcq` | false | `A` | `D. No crime.` |
| baseline | `mmlu_10934` | `mcq` | true | `D` | `D. not recover.` |
| baseline | `mmlu_10935` | `mcq` | false | `C` | `D. not succeed, unless the farmer had constructive notice of the existence of the mortgage.` |
| baseline | `mmlu_10936` | `mcq` | false | `A` | `C. not guilty, because of his intoxication.` |
| baseline | `mmlu_10937` | `mcq` | false | `B` | `C. No, because the offer expressly limited the acceptance to the terms of the offer.` |
| baseline | `mmlu_10938` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10939` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10940` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10941` | `mcq` | false | `A` | `C. Licensee.` |
| baseline | `mmlu_10942` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10943` | `mcq` | true | `C` | `C. A ratified treaty is the supreme law of the land and, therefore, remains effective until superseded by another treaty` |
| baseline | `mmlu_10944` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10945` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10946` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10947` | `mcq` | false | `C` | `D. Yes, as a statement of the friend's state of mind that is not testimonial under the confrontation clause.` |
| baseline | `mmlu_10948` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10949` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10950` | `mcq` | true | `B` | `B. Yes, because the company made no effort to inform the prosecutor that the registration fee had been paid in full.` |
| baseline | `mmlu_10951` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10952` | `mcq` | true | `B` | `B. Because this law burdens interstate commerce by prohibiting all vehicles with window tinting from entering the state,` |
| baseline | `mmlu_10953` | `mcq` | true | `D` | `D. Warranty of merchantability` |
| baseline | `mmlu_10954` | `mcq` | false | `B` | `A. prevail, because the hotel knew that for the past 20 years the husband and wife always stayed in the most luxurious s` |
| baseline | `mmlu_10955` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10956` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10957` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10958` | `mcq` | true | `D` | `D. Yes, the provision is enforceable because it is generally considered to be a reasonable restraint on alienation.` |
| baseline | `mmlu_10959` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10960` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10961` | `mcq` | false | `D` | `C. The speech and debate clause.` |
| baseline | `mmlu_10962` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10963` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10964` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10965` | `mcq` | true | `C` | `C. The statute is necessary to protect the safety and welfare of persons using a state facility, and does not discrimina` |
| baseline | `mmlu_10966` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10967` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10968` | `mcq` | false | `D` | `A. The statute of limitations has run, so Gordon's lawsuit is not timely.` |
| baseline | `mmlu_10969` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10970` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10971` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10972` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10973` | `mcq` | true | `D` | `D. Yes, the construction company has substantially performed the contract.` |
| baseline | `mmlu_10974` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10975` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10976` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10977` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10978` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10979` | `mcq` | false | `C` | `A. Yes, because the sister does not have sufficient experience and knowledge to be able to identify the man's voice and ` |
| baseline | `mmlu_10980` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10981` | `mcq` | true | `D` | `D. The photographer's injury constituted a temporary impracticability of performance, which excused his duty to perform ` |
| baseline | `mmlu_10982` | `mcq` | false | `B` | `C. It would not be excused, because the contract stipulated that no fees would be refundable.` |
| baseline | `mmlu_10983` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10984` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10986` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10987` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10988` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10989` | `mcq` | true | `C` | `C. not guilty, because he honestly believed that she was consenting.` |
| baseline | `mmlu_10990` | `mcq` | true | `D` | `D. The farmer, because he has put the water to a beneficial use prior to the rancher's use and has continuously used the` |
| baseline | `mmlu_10991` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10992` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10993` | `mcq` | false | `A` | `C. Yes, although hearsay, under the learned treatise exception to the hearsay rule.` |
| baseline | `mmlu_10994` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10995` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10996` | `mcq` | true | `D` | `D. No, because she had a property right in her license and permits, which were taken without any procedural due process.` |
| baseline | `mmlu_10997` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10998` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10999` | `mcq` | true | `C` | `C. Larceny and attempted burglary.` |
