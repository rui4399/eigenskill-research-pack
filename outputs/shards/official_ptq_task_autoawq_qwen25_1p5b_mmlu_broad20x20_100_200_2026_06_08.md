# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 48 / 100 | 0.4800 | 11.7224 | 0.169859 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
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
| baseline | `mmlu_111` | `mcq` | true | `C` | `C` |
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
