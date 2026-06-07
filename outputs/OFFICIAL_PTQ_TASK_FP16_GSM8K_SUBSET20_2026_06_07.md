# Chat Task Benchmark

Model: `Qwen/Qwen2.5-0.5B-Instruct`
Tasks: `20`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 0 / 20 | 0.0000 | 29.5206 | 0.157866 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `gsm8k_0` | `number` | false | `18` | `To determine how much Janet makes every day at the farmers' market, we need` |
| baseline | `gsm8k_1` | `number` | false | `3` | `4` |
| baseline | `gsm8k_2` | `number` | false | `70000` | `$35,000` |
| baseline | `gsm8k_3` | `number` | false | `540` | `1800` |
| baseline | `gsm8k_4` | `number` | false | `20` | `30` |
| baseline | `gsm8k_5` | `number` | false | `64` | `To determine how much Kylar needs to pay for 16 glasses,` |
| baseline | `gsm8k_6` | `number` | false | `260` | `160` |
| baseline | `gsm8k_7` | `number` | false | `160` | `To determine the total time required for Carla to complete the download, we need to` |
| baseline | `gsm8k_8` | `number` | false | `45` | `To determine how far John is from home at the end of the 4 hours` |
| baseline | `gsm8k_9` | `number` | false | `460` | `To calculate Eliza's earnings for the week, we need to consider both her` |
| baseline | `gsm8k_10` | `number` | false | `366` | `To determine the total number of downloads for the program over the three months, we` |
| baseline | `gsm8k_11` | `number` | false | `694` | `To determine the total cost of Toula's purchases, we need to calculate the` |
| baseline | `gsm8k_12` | `number` | false | `13` | `24` |
| baseline | `gsm8k_13` | `number` | false | `18` | `To determine how many vacuum cleaners Melanie started with, we need to work backwards from` |
| baseline | `gsm8k_14` | `number` | false | `60` | `10%` |
| baseline | `gsm8k_15` | `number` | false | `125` | `To determine the best option for the merchant, we need to calculate the expected value` |
| baseline | `gsm8k_16` | `number` | false | `230` | `The distance covered by each train in the two days is 200 miles` |
| baseline | `gsm8k_17` | `number` | false | `57500` | `$49500` |
| baseline | `gsm8k_18` | `number` | false | `7` | `120` |
| baseline | `gsm8k_19` | `number` | false | `6` | `To determine Marissa's required walking speed for the remaining distance of the trail,` |
