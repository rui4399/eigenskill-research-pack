# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `100`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 48 / 100 | 0.4800 | 4.9205 | 0.434441 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
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
