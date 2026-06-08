# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `2500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 1387 / 2500 | 0.5548 | 4.9436 | 0.423534 |

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
