# Chat Task Benchmark

Model: `Qwen/Qwen2.5-0.5B-Instruct`
Tasks: `100`
Task format: `gsm8k`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 2 / 100 | 0.0200 | 27.7082 | 0.106440 |

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
| baseline | `gsm8k_20` | `number` | false | `15` | `To solve this problem, we need to determine how much water remains after adding the` |
| baseline | `gsm8k_21` | `number` | false | `14` | `4` |
| baseline | `gsm8k_22` | `number` | false | `7` | `14` |
| baseline | `gsm8k_23` | `number` | false | `8` | `30` |
| baseline | `gsm8k_24` | `number` | false | `26` | `$13.50` |
| baseline | `gsm8k_25` | `number` | false | `2` | `To determine how many boxes of pizza Marie ordered, we need to calculate the total` |
| baseline | `gsm8k_26` | `number` | false | `243` | `To determine how much Mishka spent in total on all the clothing items, we` |
| baseline | `gsm8k_27` | `number` | false | `16` | `To determine how much Cynthia will spend on ice cream over 60 days,` |
| baseline | `gsm8k_28` | `number` | false | `25` | `35 miles` |
| baseline | `gsm8k_29` | `number` | false | `104` | `120` |
| baseline | `gsm8k_30` | `number` | false | `109` | `To solve this problem, we need to determine Allen's current age based on the` |
| baseline | `gsm8k_31` | `number` | false | `80` | `140` |
| baseline | `gsm8k_32` | `number` | false | `35` | `70` |
| baseline | `gsm8k_33` | `number` | false | `70` | `To determine how many gold coins Gretchen has, we can set up an equation` |
| baseline | `gsm8k_34` | `number` | false | `23` | `130` |
| baseline | `gsm8k_35` | `number` | false | `9` | `18` |
| baseline | `gsm8k_36` | `number` | false | `75` | `To determine how much Terry spends on yogurt over 30 days, we need` |
| baseline | `gsm8k_37` | `number` | false | `2` | `To determine how many Lego sets John still has, we need to follow these steps` |
| baseline | `gsm8k_38` | `number` | false | `10` | `To determine John's running speed, we need to calculate the total distance he runs` |
| baseline | `gsm8k_39` | `number` | false | `18` | `To determine how many miles Dana can travel in six hours, we need to calculate` |
| baseline | `gsm8k_40` | `number` | false | `8` | `4` |
| baseline | `gsm8k_41` | `number` | false | `200` | `350 feet` |
| baseline | `gsm8k_42` | `number` | false | `26` | `To determine how many pieces of pie were taken by the guests, we need to` |
| baseline | `gsm8k_43` | `number` | false | `48` | `To determine how many grams of chips you can eat while maintaining your daily calorie target` |
| baseline | `gsm8k_44` | `number` | false | `20` | `$40.00` |
| baseline | `gsm8k_45` | `number` | false | `104` | `18` |
| baseline | `gsm8k_46` | `number` | false | `163` | `147` |
| baseline | `gsm8k_47` | `number` | false | `800` | `To determine how much John spent on ties, we need to follow these steps:  ` |
| baseline | `gsm8k_48` | `number` | false | `8` | `10` |
| baseline | `gsm8k_49` | `number` | false | `30` | `20` |
| baseline | `gsm8k_50` | `number` | false | `294` | `To calculate how much Lloyd makes on eggs per week, we need to follow these` |
| baseline | `gsm8k_51` | `number` | false | `5` | `2 hours` |
| baseline | `gsm8k_52` | `number` | false | `15` | `To solve this problem, we first calculate the total weight of the comic books:  ` |
| baseline | `gsm8k_53` | `number` | false | `40` | `To determine how much more revenue the mechanic earned on Friday compared to Thursday, we` |
| baseline | `gsm8k_54` | `number` | false | `40` | `8` |
| baseline | `gsm8k_55` | `number` | false | `14` | `1` |
| baseline | `gsm8k_56` | `number` | false | `3` | `10` |
| baseline | `gsm8k_57` | `number` | false | `83` | `2` |
| baseline | `gsm8k_58` | `number` | false | `57` | `$37.00` |
| baseline | `gsm8k_59` | `number` | false | `187` | `1348` |
| baseline | `gsm8k_60` | `number` | false | `17` | `To determine how many oranges are good in the basket, we need to follow these` |
| baseline | `gsm8k_61` | `number` | false | `1430` | `To determine how much Janet paid for the brooch, we need to follow these` |
| baseline | `gsm8k_62` | `number` | false | `25000` | `100000` |
| baseline | `gsm8k_63` | `number` | false | `1596` | `280` |
| baseline | `gsm8k_64` | `number` | false | `300` | `360` |
| baseline | `gsm8k_65` | `number` | false | `36` | `180` |
| baseline | `gsm8k_66` | `number` | false | `48` | `100` |
| baseline | `gsm8k_67` | `number` | false | `595` | `To determine the total number of gems in the chest, we need to calculate the` |
| baseline | `gsm8k_68` | `number` | false | `36` | `10` |
| baseline | `gsm8k_69` | `number` | false | `60` | `To determine how much money Bailey started with, we need to follow these steps:  ` |
| baseline | `gsm8k_70` | `number` | false | `7425` | `To calculate Judy's weekly earnings, we need to consider her daily earnings from teaching` |
| baseline | `gsm8k_71` | `number` | false | `60` | `15` |
| baseline | `gsm8k_72` | `number` | false | `221` | `159` |
| baseline | `gsm8k_73` | `number` | false | `255` | `To determine how much Shiela will pay each month for 3 months, we` |
| baseline | `gsm8k_74` | `number` | false | `88` | `$30.56` |
| baseline | `gsm8k_75` | `number` | false | `60` | `5` |
| baseline | `gsm8k_76` | `number` | false | `5` | `365 * 1 + 365 * 2 = ` |
| baseline | `gsm8k_77` | `number` | false | `100` | `200` |
| baseline | `gsm8k_78` | `number` | true | `6` | `6` |
| baseline | `gsm8k_79` | `number` | true | `70` | `$70` |
| baseline | `gsm8k_80` | `number` | false | `10` | `36` |
| baseline | `gsm8k_81` | `number` | false | `17` | `7` |
| baseline | `gsm8k_82` | `number` | false | `623` | `370` |
| baseline | `gsm8k_83` | `number` | false | `600` | `140` |
| baseline | `gsm8k_84` | `number` | false | `15` | `10` |
| baseline | `gsm8k_85` | `number` | false | `44` | `150` |
| baseline | `gsm8k_86` | `number` | false | `22` | `To determine how many times the alarm rang in total over the three days, we` |
| baseline | `gsm8k_87` | `number` | false | `9360` | `$72900` |
| baseline | `gsm8k_88` | `number` | false | `8000` | `To determine how many copies Harald sold, we start by defining variables for their` |
| baseline | `gsm8k_89` | `number` | false | `24` | `To determine how much Christina will spend on the gift bags, we need to follow` |
| baseline | `gsm8k_90` | `number` | false | `225` | `To determine how many pounds of potato salad Ted needs to bring, we can follow` |
| baseline | `gsm8k_91` | `number` | false | `28` | `12` |
| baseline | `gsm8k_92` | `number` | false | `4` | `3` |
| baseline | `gsm8k_93` | `number` | false | `36` | `25` |
| baseline | `gsm8k_94` | `number` | false | `348` | `To determine the total number of pets in the neighborhood, we need to follow these` |
| baseline | `gsm8k_95` | `number` | false | `40` | `180` |
| baseline | `gsm8k_96` | `number` | false | `3` | `8` |
| baseline | `gsm8k_97` | `number` | false | `12` | `To determine how many tomatoes Freda used to make her last batch of tomato sauce` |
| baseline | `gsm8k_98` | `number` | false | `5` | `To determine how many cars drove through the traffic jam in the first 15` |
| baseline | `gsm8k_99` | `number` | false | `58` | `36` |
