# Chat Task Benchmark

Model: `huihui-qwen35-4b-pmra:latest`
Tasks: `50`
Task format: `mmlu`
Chat template: `False`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 50 | 0.0000 | 83.4536 | 0.488652 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_0` | `mcq` | false | `B` | `  <think>  </think>  C<\|endoftext\|>>` |
| baseline | `mmlu_1` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_2` | `mcq` | false | `D` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_3` | `mcq` | false | `B` | `  <think>one Answer with only the` |
| baseline | `mmlu_4` | `mcq` | false | `B` | `  <think>  </think>  C<\|endoftext\|>>` |
| baseline | `mmlu_5` | `mcq` | false | `A` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_6` | `mcq` | false | `A` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_7` | `mcq` | false | `D` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_8` | `mcq` | false | `B` | `  <think>  </think>  C<\|endoftext\|>>` |
| baseline | `mmlu_9` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_10` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_11` | `mcq` | false | `C` | `/  <think>  </think>  C<\|endoftext\|>` |
| baseline | `mmlu_12` | `mcq` | false | `A` | `/  <think>  </think>  C<\|endoftext\|>` |
| baseline | `mmlu_13` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_14` | `mcq` | false | `C` | `/  <think>  </think>  D<\|endoftext\|>` |
| baseline | `mmlu_15` | `mcq` | false | `B` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_16` | `mcq` | false | `C` | `/Answer:  D<\|endoftext\|>Simple and` |
| baseline | `mmlu_17` | `mcq` | false | `C` | `/  <think>  </think>  D<\|endoftext\|>` |
| baseline | `mmlu_18` | `mcq` | false | `D` | `/zero has no inverse  <think>  ` |
| baseline | `mmlu_19` | `mcq` | false | `A` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_20` | `mcq` | false | `A` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_21` | `mcq` | false | `A` | `/  <think>  </think>  C<\|endoftext\|>` |
| baseline | `mmlu_22` | `mcq` | false | `D` | `_token>  <think>  </think>  D` |
| baseline | `mmlu_23` | `mcq` | false | `D` | `  <think>  </think>  D<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_24` | `mcq` | false | `B` | `  <think>one. Answer with only` |
| baseline | `mmlu_25` | `mcq` | false | `C` | `/  <think>  </think>  C<\|endoftext\|>` |
| baseline | `mmlu_26` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_27` | `mcq` | false | `B` | `  <think>  </think>  D<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_28` | `mcq` | false | `D` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_29` | `mcq` | false | `A` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_30` | `mcq` | false | `B` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_31` | `mcq` | false | `B` | `  <think>  </think>  B<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_32` | `mcq` | false | `A` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_33` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_34` | `mcq` | false | `A` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_35` | `mcq` | false | `B` | `  <think>  </think>  B<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_36` | `mcq` | false | `D` | `/  <think>  </think>  D<\|endoftext\|>` |
| baseline | `mmlu_37` | `mcq` | false | `B` | `  <think>  </think>  D. No` |
| baseline | `mmlu_38` | `mcq` | false | `C` | `  <think>  </think>  B<\|endoftext\|>no` |
| baseline | `mmlu_39` | `mcq` | false | `D` | `  <think>  </think>  D<\|endoftext\|><` |
| baseline | `mmlu_40` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_41` | `mcq` | false | `A` | `/  <think>  </think>  C<\|endoftext\|>` |
| baseline | `mmlu_42` | `mcq` | false | `B` | `  <think>one C </think>  ` |
| baseline | `mmlu_43` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><` |
| baseline | `mmlu_44` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_45` | `mcq` | false | `C` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_46` | `mcq` | false | `B` | `  <think>  </think>  C<\|endoftext\|><\|endoftext\|>` |
| baseline | `mmlu_47` | `mcq` | false | `B` | `/  <think>  </think>  C<\|endoftext\|>` |
| baseline | `mmlu_48` | `mcq` | false | `C` | `  <think>one D<\|endoftext\|>> ` |
| baseline | `mmlu_49` | `mcq` | false | `B` | `/  <think>  </think>  C<\|endoftext\|>` |
