# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `400`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 214 / 400 | 0.5350 | 5.2316 | 0.407572 |

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
| baseline | `mmlu_20` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_21` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_22` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_23` | `mcq` | false | `C` | `B. Skeletal muscles` |
| baseline | `mmlu_24` | `mcq` | true | `B` | `B. Glomerulus` |
| baseline | `mmlu_25` | `mcq` | false | `B` | `D. Breathing will be unaffected.` |
| baseline | `mmlu_26` | `mcq` | false | `A` | `B. Hypochondriac` |
| baseline | `mmlu_27` | `mcq` | true | `B` | `B. Mucous membranes` |
| baseline | `mmlu_28` | `mcq` | false | `C` | `B. eight weeks post-fertilization.` |
| baseline | `mmlu_29` | `mcq` | true | `D` | `D. contraction of contralateral limb musculature.` |
| baseline | `mmlu_30` | `mcq` | true | `D` | `D. hard palate, upper lip, upper central incisor and lower first molar.` |
| baseline | `mmlu_31` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_32` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_33` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_35` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_36` | `mcq` | true | `B` | `B. External intercostal muscles and diaphragm` |
| baseline | `mmlu_37` | `mcq` | true | `D` | `D. Testes` |
| baseline | `mmlu_38` | `mcq` | false | `D` | `A. Aorta` |
| baseline | `mmlu_39` | `mcq` | true | `C` | `C. Trachea` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_41` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_42` | `mcq` | true | `D` | `D. Employee duties` |
| baseline | `mmlu_43` | `mcq` | true | `D` | `D. Work-life balance` |
| baseline | `mmlu_44` | `mcq` | true | `B` | `B. Industrial ecosystems` |
| baseline | `mmlu_45` | `mcq` | true | `B` | `B. Power imbalance, Resources, Co-opted` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_47` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_48` | `mcq` | false | `B` | `C. Political, Interactions, Outcomes` |
| baseline | `mmlu_49` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_50` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_51` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_52` | `mcq` | true | `D` | `D. Public services, social, economic and environmental` |
| baseline | `mmlu_53` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_54` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_55` | `mcq` | true | `B` | `B. Healthy and safe working conditions` |
| baseline | `mmlu_56` | `mcq` | true | `A` | `A. To make a profit` |
| baseline | `mmlu_57` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_58` | `mcq` | false | `C` | `B. Consumer control` |
| baseline | `mmlu_59` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_60` | `mcq` | true | `A` | `A. 18 gauge.` |
| baseline | `mmlu_61` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_62` | `mcq` | true | `A` | `A. Alzheimer's disease.` |
| baseline | `mmlu_63` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_64` | `mcq` | true | `B` | `B. The patient has a colostomy.` |
| baseline | `mmlu_65` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_66` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_67` | `mcq` | true | `A` | `A. elevating the pH and buffering capacity of the extracellular fluid allowing a faster efflux of hydrogen ions from mus` |
| baseline | `mmlu_68` | `mcq` | true | `A` | `A. triplet sequences of nucleotide bases in mRNA or DNA.` |
| baseline | `mmlu_69` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_70` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_71` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_72` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_73` | `mcq` | true | `B` | `B. glucose-1-phosphate.` |
| baseline | `mmlu_74` | `mcq` | true | `B` | `B. actin and myosin.` |
| baseline | `mmlu_75` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_76` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_77` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_78` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_79` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_80` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_81` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_82` | `mcq` | true | `B` | `B. 1:3.5` |
| baseline | `mmlu_83` | `mcq` | true | `A` | `A. C1: (3,3), C2: (4,4), C3: (6,6)` |
| baseline | `mmlu_84` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_85` | `mcq` | false | `C` | `D. M = 6, m = 4` |
| baseline | `mmlu_86` | `mcq` | false | `C` | `D. I and III only` |
| baseline | `mmlu_87` | `mcq` | false | `B` | `C. III only` |
| baseline | `mmlu_88` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_89` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_90` | `mcq` | false | `D` | `B. III only` |
| baseline | `mmlu_91` | `mcq` | false | `A` | `B. n + 1` |
| baseline | `mmlu_92` | `mcq` | true | `A` | `A. 3` |
| baseline | `mmlu_93` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_94` | `mcq` | false | `A` | `C. III only` |
| baseline | `mmlu_95` | `mcq` | true | `D` | `D. None of the above` |
| baseline | `mmlu_96` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_97` | `mcq` | false | `B` | `D. context-free, but not regular` |
| baseline | `mmlu_98` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_99` | `mcq` | false | `D` | `C. I and II only` |
| baseline | `mmlu_100` | `mcq` | true | `C` | `C. Whitebox` |
| baseline | `mmlu_101` | `mcq` | false | `A` | `D. False, True` |
| baseline | `mmlu_102` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_103` | `mcq` | true | `A` | `A. Receiver` |
| baseline | `mmlu_104` | `mcq` | true | `A` | `A. Troya` |
| baseline | `mmlu_105` | `mcq` | true | `B` | `B. Buffer-overrun` |
| baseline | `mmlu_106` | `mcq` | true | `A` | `A. all instructions that modify segment state` |
| baseline | `mmlu_107` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_108` | `mcq` | true | `A` | `A. No string boundary checks in predefined functions` |
| baseline | `mmlu_109` | `mcq` | true | `B` | `B. Authenticated` |
| baseline | `mmlu_110` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_111` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_112` | `mcq` | true | `C` | `C. Forward secrecy` |
| baseline | `mmlu_113` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_114` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_115` | `mcq` | true | `B` | `B. Access Point` |
| baseline | `mmlu_116` | `mcq` | true | `B` | `B. 128` |
| baseline | `mmlu_117` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_118` | `mcq` | false | `A` | `D. All of the above` |
| baseline | `mmlu_119` | `mcq` | true | `D` | `D. Taking care to avoid activities during a penetration test that might attract attention, e.g., by operators or IDS ser` |
| baseline | `mmlu_120` | `mcq` | false | `D` | `A. (0, – 3)` |
| baseline | `mmlu_121` | `mcq` | true | `C` | `C. 50` |
| baseline | `mmlu_122` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_123` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_124` | `mcq` | true | `C` | `C. (-inf, 8)` |
| baseline | `mmlu_125` | `mcq` | false | `B` | `A. 396` |
| baseline | `mmlu_126` | `mcq` | false | `C` | `A. 0.16` |
| baseline | `mmlu_127` | `mcq` | false | `A` | `C. 36` |
| baseline | `mmlu_128` | `mcq` | false | `C` | `A. \(\frac{125}{648}\)` |
| baseline | `mmlu_129` | `mcq` | false | `B` | `A. 8` |
| baseline | `mmlu_130` | `mcq` | false | `D` | `B. 14` |
| baseline | `mmlu_131` | `mcq` | false | `D` | `C. 2048` |
| baseline | `mmlu_132` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_133` | `mcq` | false | `B` | `C. 94.5` |
| baseline | `mmlu_134` | `mcq` | false | `D` | `B. L <= T <= M <= R` |
| baseline | `mmlu_135` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_136` | `mcq` | true | `A` | `A. 8` |
| baseline | `mmlu_137` | `mcq` | false | `B` | `A. -2` |
| baseline | `mmlu_138` | `mcq` | false | `A` | `C. 0` |
| baseline | `mmlu_139` | `mcq` | false | `B` | `A. (-∞,-1)∪(1,+∞)` |
| baseline | `mmlu_140` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_141` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_142` | `mcq` | true | `D` | `D. Reconstruction` |
| baseline | `mmlu_143` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_144` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_145` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_146` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_147` | `mcq` | true | `A` | `A. The Social Gospel` |
| baseline | `mmlu_148` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_149` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_150` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_151` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_152` | `mcq` | false | `A` | `C. all Christians only` |
| baseline | `mmlu_153` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_154` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_155` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_156` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_157` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_158` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_159` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_160` | `mcq` | false | `D` | `C. True, False` |
| baseline | `mmlu_161` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_162` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_163` | `mcq` | false | `D` | `C. 48` |
| baseline | `mmlu_164` | `mcq` | true | `A` | `A. convolutional networks` |
| baseline | `mmlu_165` | `mcq` | false | `B` | `D. False, True` |
| baseline | `mmlu_166` | `mcq` | true | `A` | `A. O(D)` |
| baseline | `mmlu_167` | `mcq` | false | `B` | `C. True, False` |
| baseline | `mmlu_168` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_169` | `mcq` | true | `A` | `A. Lower variance` |
| baseline | `mmlu_170` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_171` | `mcq` | false | `C` | `B. overfitting` |
| baseline | `mmlu_172` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_173` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_174` | `mcq` | true | `B` | `B. not pure` |
| baseline | `mmlu_175` | `mcq` | false | `B` | `D. False, True` |
| baseline | `mmlu_176` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_177` | `mcq` | true | `A` | `A. The number of hidden nodes` |
| baseline | `mmlu_178` | `mcq` | true | `A` | `A. The polynomial degree` |
| baseline | `mmlu_179` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_180` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_181` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_182` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_183` | `mcq` | true | `C` | `C. The authenticating requirement was necessary to further a compelling state interest.` |
| baseline | `mmlu_184` | `mcq` | false | `B` | `A. He intended to kill the friend and not the daughter.` |
| baseline | `mmlu_185` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_186` | `mcq` | false | `B` | `C. invalid, because the executive order is beyond the scope of presidential power absent congressional authorization.` |
| baseline | `mmlu_187` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_188` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_189` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_190` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_191` | `mcq` | false | `A` | `B. Yes, because the authority to enact laws regulating real estate sales transactions occurring within the boundaries of` |
| baseline | `mmlu_192` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_193` | `mcq` | true | `B` | `B. The court will require a greater foundation to establish the reliability of the records.` |
| baseline | `mmlu_194` | `mcq` | true | `D` | `D. The rational basis test, because the regulation need only be related to a legitimate state interest to be valid.` |
| baseline | `mmlu_195` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_196` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_197` | `mcq` | false | `A` | `B. The man, because the purchaser did not have actual notice of the easement at the time of acquisition.` |
| baseline | `mmlu_198` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_199` | `mcq` | true | `A` | `A. Remand the entire case.` |
| baseline | `mmlu_200` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_201` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_202` | `mcq` | true | `C` | `C. Because the atmosphere preferentially scatters short wavelengths.` |
| baseline | `mmlu_203` | `mcq` | true | `C` | `C. You can never prove your theory to be correct only "yet to be proven wrong".` |
| baseline | `mmlu_204` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_205` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_206` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_207` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_208` | `mcq` | false | `D` | `B. Hydrogen` |
| baseline | `mmlu_209` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_210` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_211` | `mcq` | true | `C` | `C. By comparing the maximum altitude of the Sun in two cities at different latitudes at the same time on the same day.` |
| baseline | `mmlu_212` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_213` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_214` | `mcq` | true | `B` | `B. Laniakea` |
| baseline | `mmlu_215` | `mcq` | true | `C` | `C. Jupiter` |
| baseline | `mmlu_216` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_217` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_218` | `mcq` | true | `D` | `D. A and B only` |
| baseline | `mmlu_219` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_220` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_221` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_222` | `mcq` | true | `A` | `A. amnion` |
| baseline | `mmlu_223` | `mcq` | true | `B` | `B. Inositol triphosphate` |
| baseline | `mmlu_224` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_225` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_226` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_227` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_228` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_229` | `mcq` | true | `C` | `C. Replicate its genetic material and synthesize viral proteins` |
| baseline | `mmlu_230` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_231` | `mcq` | false | `D` | `B. Lysosome` |
| baseline | `mmlu_232` | `mcq` | false | `C` | `A. Both fox and hare populations will decrease.` |
| baseline | `mmlu_233` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_234` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_235` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_236` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_237` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_238` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_239` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_240` | `mcq` | true | `D` | `D. r = k` |
| baseline | `mmlu_241` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_242` | `mcq` | false | `D` | `A. 2` |
| baseline | `mmlu_243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_244` | `mcq` | true | `B` | `B. only for constant pressure processes` |
| baseline | `mmlu_245` | `mcq` | false | `B` | `A. 3 lines` |
| baseline | `mmlu_246` | `mcq` | true | `A` | `A. Neutrons` |
| baseline | `mmlu_247` | `mcq` | true | `D` | `D. Unpaired electrons` |
| baseline | `mmlu_248` | `mcq` | false | `C` | `B. 1:3` |
| baseline | `mmlu_249` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_250` | `mcq` | false | `D` | `A. 3.02 ppm` |
| baseline | `mmlu_251` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_252` | `mcq` | true | `A` | `A. 4.6 mT` |
| baseline | `mmlu_253` | `mcq` | false | `D` | `A. 1:19:36:84:126:126:84:36:19:1` |
| baseline | `mmlu_254` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_255` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_256` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_257` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_258` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_259` | `mcq` | false | `B` | `D. 13.93 MHz` |
| baseline | `mmlu_260` | `mcq` | false | `B` | `A. k = 0 and n = 1` |
| baseline | `mmlu_261` | `mcq` | false | `D` | `B. 1` |
| baseline | `mmlu_262` | `mcq` | false | `D` | `B. n = 1 and r = 7` |
| baseline | `mmlu_263` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_264` | `mcq` | false | `C` | `A. 2/69` |
| baseline | `mmlu_265` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_266` | `mcq` | false | `C` | `B. 6*sqrt(2)` |
| baseline | `mmlu_267` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_268` | `mcq` | false | `C` | `D. III only` |
| baseline | `mmlu_269` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_270` | `mcq` | true | `D` | `D. 45` |
| baseline | `mmlu_271` | `mcq` | true | `B` | `B. 15/64` |
| baseline | `mmlu_272` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_273` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_274` | `mcq` | false | `D` | `A. 0.64` |
| baseline | `mmlu_275` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_276` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_277` | `mcq` | false | `C` | `A. -1/4` |
| baseline | `mmlu_278` | `mcq` | false | `D` | `C. I and III only` |
| baseline | `mmlu_279` | `mcq` | true | `A` | `A. 3` |
| baseline | `mmlu_280` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_281` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_282` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_283` | `mcq` | false | `D` | `C. about 1 minute.` |
| baseline | `mmlu_284` | `mcq` | true | `A` | `A. 13 m/s^2` |
| baseline | `mmlu_285` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_286` | `mcq` | true | `A` | `A. Heart surgery patients who cannot run on treadmills may benefit from sauna use.` |
| baseline | `mmlu_287` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_288` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_289` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_290` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_291` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_292` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_293` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_294` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_295` | `mcq` | false | `B` | `D. Not enough information given.` |
| baseline | `mmlu_296` | `mcq` | true | `C` | `C. in the nucleus.` |
| baseline | `mmlu_297` | `mcq` | true | `B` | `B. Transferase` |
| baseline | `mmlu_298` | `mcq` | false | `B` | `C. Lower than the pOH` |
| baseline | `mmlu_299` | `mcq` | true | `B` | `B. the entire DNA sequence of an organism.` |
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
