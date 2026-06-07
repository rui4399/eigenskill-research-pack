# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `200`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 96 / 200 | 0.4800 | 11.7995 | 0.149837 |

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
| baseline | `mmlu_20` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_21` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_22` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_23` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_24` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_25` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_26` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_27` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_28` | `mcq` | false | `C` | `B. eight weeks post-fertilization.` |
| baseline | `mmlu_29` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_30` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_31` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_32` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_33` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_35` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_36` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_37` | `mcq` | true | `D` | `D. Testes` |
| baseline | `mmlu_38` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_39` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_40` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_41` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_42` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_43` | `mcq` | false | `D` | `C. Work-play balance` |
| baseline | `mmlu_44` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_45` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_46` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_47` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_48` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_49` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_50` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_51` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_52` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_53` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_54` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_55` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_56` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_57` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_58` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_59` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_60` | `mcq` | true | `A` | `A. 18 gauge.` |
| baseline | `mmlu_61` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_62` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_63` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_64` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_65` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_66` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_67` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_68` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_69` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_70` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_71` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_72` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_73` | `mcq` | true | `B` | `B. glucose-1-phosphate.` |
| baseline | `mmlu_74` | `mcq` | true | `B` | `B. actin and myosin.` |
| baseline | `mmlu_75` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_76` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_77` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_78` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_79` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_80` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_81` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_82` | `mcq` | true | `B` | `B. 1:3.5` |
| baseline | `mmlu_83` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_84` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_85` | `mcq` | false | `C` | `D. M = 6, m = 4` |
| baseline | `mmlu_86` | `mcq` | false | `C` | `D. I and III only` |
| baseline | `mmlu_87` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_88` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_89` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_90` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_91` | `mcq` | false | `A` | `B. n + 1` |
| baseline | `mmlu_92` | `mcq` | true | `A` | `A. 3` |
| baseline | `mmlu_93` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_94` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_95` | `mcq` | true | `D` | `D. None of the above` |
| baseline | `mmlu_96` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_97` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_98` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_99` | `mcq` | false | `D` | `C. I and II only` |
| baseline | `mmlu_100` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_101` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_102` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_103` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_104` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_105` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_106` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_107` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_108` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_109` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_110` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_111` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_112` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_113` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_114` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_115` | `mcq` | true | `B` | `B. Access Point` |
| baseline | `mmlu_116` | `mcq` | true | `B` | `B. 128` |
| baseline | `mmlu_117` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_118` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_119` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_120` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_121` | `mcq` | false | `C` | `D. 25` |
| baseline | `mmlu_122` | `mcq` | true | `A` | `A. 392` |
| baseline | `mmlu_123` | `mcq` | false | `B` | `A. \frac{7}{9}` |
| baseline | `mmlu_124` | `mcq` | true | `C` | `C. (-inf, 8)` |
| baseline | `mmlu_125` | `mcq` | false | `B` | `A. 396` |
| baseline | `mmlu_126` | `mcq` | false | `C` | `B. 0.24` |
| baseline | `mmlu_127` | `mcq` | true | `A` | `A. 42` |
| baseline | `mmlu_128` | `mcq` | false | `C` | `A. \frac{125}{648}` |
| baseline | `mmlu_129` | `mcq` | false | `B` | `A. 8` |
| baseline | `mmlu_130` | `mcq` | false | `D` | `B. 14` |
| baseline | `mmlu_131` | `mcq` | false | `D` | `C. 2048` |
| baseline | `mmlu_132` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_133` | `mcq` | false | `B` | `C. 94.5` |
| baseline | `mmlu_134` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_135` | `mcq` | true | `D` | `D. 5+2\sqrt{13}` |
| baseline | `mmlu_136` | `mcq` | true | `A` | `A. 8` |
| baseline | `mmlu_137` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_138` | `mcq` | false | `A` | `C. 0` |
| baseline | `mmlu_139` | `mcq` | false | `B` | `A. (-\infty,-1)\cup (1,\infty)` |
| baseline | `mmlu_140` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_141` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_142` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_143` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_144` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_145` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_146` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_147` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_148` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_149` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_150` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_151` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_152` | `mcq` | false | `A` | `C. all Christians only` |
| baseline | `mmlu_153` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_154` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_155` | `mcq` | true | `C` | `C. The Apollo space program` |
| baseline | `mmlu_156` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_157` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_158` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_159` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_160` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_161` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_162` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_163` | `mcq` | true | `D` | `D. 72` |
| baseline | `mmlu_164` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_165` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_166` | `mcq` | true | `A` | `A. O(D)` |
| baseline | `mmlu_167` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_168` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_169` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_170` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_171` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_172` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_173` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_174` | `mcq` | true | `B` | `B. not pure` |
| baseline | `mmlu_175` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_176` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_177` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_178` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_179` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_180` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_181` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_182` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_183` | `mcq` | true | `C` | `C. The authenticating requirement was necessary to further a compelling state interest.` |
| baseline | `mmlu_184` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_185` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_186` | `mcq` | false | `B` | `C. invalid, because the executive order is beyond the scope of presidential power absent congressional authorization.` |
| baseline | `mmlu_187` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_188` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_189` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_190` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_191` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_192` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_193` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_194` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_195` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_196` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_197` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_198` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_199` | `mcq` | false | `A` | `C.` |
