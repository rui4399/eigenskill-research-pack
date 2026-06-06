# Chat Task Benchmark

Model: `huihui-qwen35-4b-pmra:latest`
Tasks: `50`
Task format: `gsm8k`
Chat template: `False`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 4 / 50 | 0.0800 | 82.6030 | 0.307866 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `  <think>  </think>  16 - 3 - 4 = 9 9 * 2 = 1` |
| baseline | `gsm8k_1` | `number` | false | `3` | ` /answer  4<\|endoftext\|><think>  </think>  4<\|endoftext\|><end> **Answer:** 4<\|endoftext\|><end` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `  <think>  </think>  262.5<\|endoftext\|>><\|endoftext\|>The house’s new value is $80,0` |
| baseline | `gsm8k_3` | `number` | false | `540` | `  <think> f </think>  180<\|endoftext\|>The final number is 180.<\|endoftext\|>No other text should` |
| baseline | `gsm8k_4` | `number` | true | `20` | `  <think>  </think>  20<\|endoftext\|>> 15 + 25 = 40   > 4` |
| baseline | `gsm8k_5` | `number` | false | `64` | `  <think> fiftynine </think>  fifty-nine<\|endoftext\|></think>  fifty‑nine<\|endoftext\|>Answer with only the` |
| baseline | `gsm8k_6` | `number` | false | `260` | `  <think>  </think>  32<\|endoftext\|>><\|endoftext\|>**32**<\|endoftext\|>><\|endoftext\|>><\|endoftext\|>><\|endoftext` |
| baseline | `gsm8k_7` | `number` | false | `160` | `  <think>  </think>  300<\|endoftext\|>> 200 GB / 2 GB/min` |
| baseline | `gsm8k_8` | `number` | false | `45` | `  <think>  </think>  720<\|endoftext\|><z> **Step‑ 1 – List all the parts` |
| baseline | `gsm8k_9` | `number` | false | `460` | `  <think>  </think>  45 * 12 = 540<\|endoftext\|><\|im_start\|>assistant 540<\|endoftext\|>` |
| baseline | `gsm8k_10` | `number` | false | `366` | `  <think>  </think>  60 + (3 × 60) + (3 × 60 ` |
| baseline | `gsm8k_11` | `number` | false | `694` | `  <think>  </think>  1040<\|endoftext\|>**Step‑by‑step calculation**  \| Item \| Quantity (` |
| baseline | `gsm8k_12` | `number` | false | `13` | `  <think>  </think>  4<\|endoftext\|></think>  4<\|endoftext\|> /<\|endoftext\|><\|endoftext\|><\|endoftext\|>*/ 4<\|end` |
| baseline | `gsm8k_13` | `number` | false | `18` | `  <think>  </think>  7<\|endoftext\|>><\|endoftext\|>**7**<\|endoftext\|>><\|endoftext\|>><\|endoftext\|>><\|endoftext\|` |
| baseline | `gsm8k_14` | `number` | false | `60` | `  <think>  </think>  100<\|endoftext\|>> 20% of 20 = 4 students in contemporary` |
| baseline | `gsm8k_15` | `number` | false | `125` | `  <think>  </think>  To find the profit for each plan, we calculate the increase in value for each item and then` |
| baseline | `gsm8k_16` | `number` | false | `230` | `  <think>  </think>  200<\|endoftext\|>><\|endoftext\|>**200**<\|endoftext\|>><\|endoftext\|>><\|endoftext\|>><\|endofte` |
| baseline | `gsm8k_17` | `number` | false | `57500` | `  <think> f </think>  24000<\|endoftext\|></think>  24000<\|endoftext\|>plr><\|endoftext\|><\|endoftext\|>` |
| baseline | `gsm8k_18` | `number` | false | `7` | `  <think>  </think>  24<\|endoftext\|>conclusion><\|endoftext\|>no_think><\|endoftext\|>/no_think>  24` |
| baseline | `gsm8k_19` | `number` | false | `6` | `  <think>  </think>  4<\|endoftext\|>><\|endoftext\|>Think>   Marissa’s total distance is 12 m` |
| baseline | `gsm8k_20` | `number` | false | `15` | `  <think>  </think>  To find the total amount of water in the remaining 24 liters, we’ll break the` |
| baseline | `gsm8k_21` | `number` | false | `14` | `  <think>  </think>  49<\|endoftext\|>No_think><\|endoftext\|>final answer>49</final answer><\|endoftext\|>final` |
| baseline | `gsm8k_22` | `number` | false | `7` | `  <think>  </think>  20<\|endoftext\|>**Answer:** 20<\|endoftext\|></think>  20<\|endoftext\|>/not_think>` |
| baseline | `gsm8k_23` | `number` | false | `8` | `  <think> f 24 </think>  24<\|endoftext\|></think> 24<\|endoftext\|>think> **A candle melts` |
| baseline | `gsm8k_24` | `number` | true | `26` | `  <think> f 19.50 / 0.75 = 26 </think>  26` |
| baseline | `gsm8k_25` | `number` | false | `2` | `  <think>  </think>  7<\|endoftext\|>><\|endoftext\|>**Step‑1: List the costs of all items**   -` |
| baseline | `gsm8k_26` | `number` | false | `243` | ` /answer  <think>  </think>  $16.50 + $22.50 + $4` |
| baseline | `gsm8k_27` | `number` | false | `16` | `  <think> f 60 * 4 = 240 240 / 15 = ` |
| baseline | `gsm8k_28` | `number` | false | `25` | `  <think>  </think>  40<\|endoftext\|><\|e> 40<\|endoftext\|><\|e> 40 ` |
| baseline | `gsm8k_29` | `number` | false | `104` | `  <think>  </think>  47<\|endoftext\|>**Answer:** 47<\|endoftext\|>Final number: 47<\|endoftext\|></think>  ` |
| baseline | `gsm8k_30` | `number` | false | `109` | `/ <think>  </think>  162 * 11 / (7 + 11) * 1` |
| baseline | `gsm8k_31` | `number` | false | `80` | `  <think>  </think>  45<\|endoftext\|>><\|endoftext\|>Nothink><\|endoftext\|>**Answer:** 45<\|endoftext\|>/no_th` |
| baseline | `gsm8k_32` | `number` | false | `35` | `  <think> f 10 dogs * .5 hours per dog = 5 hours per day 5 hours per day` |
| baseline | `gsm8k_33` | `number` | false | `70` | `/  <think> f 110 - 30 = 80 80 * 110` |
| baseline | `gsm8k_34` | `number` | false | `23` | `  <think>  </think>  42<\|endoftext\|>><\|endoftext\|>**Step‑1:  Raymond’s jewels**   Raymond has` |
| baseline | `gsm8k_35` | `number` | false | `9` | `  <think>  </think>  40<\|endoftext\|>><\|endoftext\|>><\|endoftext\|>> **Answer:** 45<\|endoftext\|>><\|endoftext\|>>` |
| baseline | `gsm8k_36` | `number` | false | `75` | `  <think>  </think>  60<\|endoftext\|>> 2 yogurts per day × 30 days = 60` |
| baseline | `gsm8k_37` | `number` | false | `2` | `  <think>  </think>  13<\|endoftext\|>**Answer:** 8<\|endoftext\|></think>  8<\|endoftext\|>=no<\|endoftext\|>> 8<\|endo` |
| baseline | `gsm8k_38` | `number` | false | `10` | `  <think>  </think>  45<\|endoftext\|>><\|endoftext\|>**Answer:** 45<\|endoftext\|>><\|endoftext\|>><\|endoftext\|>><\|e` |
| baseline | `gsm8k_39` | `number` | false | `18` | `  <think>  </think>  4<\|endoftext\|>><\|endoftext\|>**Answer:** 12<\|endoftext\|>><\|endoftext\|>><\|endoftext\|>> > ` |
| baseline | `gsm8k_40` | `number` | false | `8` | `  <think> f </think>  24<\|endoftext\|></think>  24<\|endoftext\|>/no_think<\|endoftext\|><\|endoftext\|></think>  24<\|` |
| baseline | `gsm8k_41` | `number` | false | `200` | `  <think>  </think>  1200<\|endoftext\|>> 400 ft (without gem) × ` |
| baseline | `gsm8k_42` | `number` | false | `26` | `  <think>  </think>  20<\|endoftext\|><answer>20</answer><\|endoftext\|><answer><\|endoftext\|><answer>` |
| baseline | `gsm8k_43` | `number` | false | `48` | `  <think>  </think>  450<\|endoftext\|>> 250 calories per serving, 5 servings in a ` |
| baseline | `gsm8k_44` | `number` | true | `20` | `  <think>  </think>  40<\|endoftext\|>> 10 candles per pound → 20 candles = 20` |
| baseline | `gsm8k_45` | `number` | true | `104` | `  <think>  </think>  104<\|endoftext\|>**Step‑ **   1. Average time per article` |
| baseline | `gsm8k_46` | `number` | false | `163` | `  <think>  </think>  70<\|endoftext\|>><\|endoftext\|>**70**<\|endoftext\|>><\|endoftext\|>><\|endoftext\|>><\|endoftext` |
| baseline | `gsm8k_47` | `number` | false | `800` | `  <think>  </think>  200<\|endoftext\|>**Answer:** 200<\|endoftext\|><\|endoftext\|>><\|endoftext\|>> 20` |
| baseline | `gsm8k_48` | `number` | false | `8` | ` 12  **Explanation**   The wire is 4 feet long, which equals 4` |
| baseline | `gsm8k_49` | `number` | false | `30` | ` 15 * 8 * 3/4 = 90 Answer: 90<\|endoftext\|>><\|endoftext\|>` |
