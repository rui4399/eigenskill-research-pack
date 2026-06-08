# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 325 / 500 | 0.6500 | 4.5088 | 0.353292 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_13000` | `mcq` | true | `B` | `B. degree of continued conflict between the parents after the divorce` |
| baseline | `mmlu_13001` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13002` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13003` | `mcq` | true | `C` | `C. early childhood experiences` |
| baseline | `mmlu_13004` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_13005` | `mcq` | false | `B` | `D. Exposure and Response Prevention` |
| baseline | `mmlu_13006` | `mcq` | true | `B` | `B. Sensitive or critical periods` |
| baseline | `mmlu_13007` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13008` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_13009` | `mcq` | false | `B` | `C. high levels of arousal.` |
| baseline | `mmlu_13010` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13011` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_13012` | `mcq` | false | `B` | `D. All of the above` |
| baseline | `mmlu_13013` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13014` | `mcq` | false | `B` | `A. Social ostracism` |
| baseline | `mmlu_13015` | `mcq` | true | `C` | `C. professional codes and state and provincial laws` |
| baseline | `mmlu_13016` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13017` | `mcq` | false | `A` | `B. life staircase` |
| baseline | `mmlu_13018` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13019` | `mcq` | false | `D` | `B. dissonance` |
| baseline | `mmlu_13020` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13021` | `mcq` | false | `C` | `A. "unethical because it violates the prohibition against “fee splitting”."` |
| baseline | `mmlu_13022` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13023` | `mcq` | false | `B` | `D. therapist` |
| baseline | `mmlu_13024` | `mcq` | true | `A` | `A. time-series` |
| baseline | `mmlu_13025` | `mcq` | false | `B` | `A. small.` |
| baseline | `mmlu_13026` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13027` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13028` | `mcq` | false | `A` | `B.	result	in	prolonged	oscillation` |
| baseline | `mmlu_13029` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13030` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13031` | `mcq` | true | `D` | `D. cohort effect.` |
| baseline | `mmlu_13032` | `mcq` | true | `D` | `D. greater acceptance of eclecticism` |
| baseline | `mmlu_13033` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13034` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13035` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13036` | `mcq` | true | `A` | `A. disorganized/disoriented` |
| baseline | `mmlu_13037` | `mcq` | true | `D` | `D. generalize the results of the study to other individuals, settings, and conditions.` |
| baseline | `mmlu_13038` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13039` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_13040` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_13041` | `mcq` | true | `A` | `A. Transference` |
| baseline | `mmlu_13042` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13043` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13044` | `mcq` | false | `C` | `B. 4 to 6` |
| baseline | `mmlu_13045` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13046` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13047` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13048` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13049` | `mcq` | true | `B` | `B. Media tour` |
| baseline | `mmlu_13050` | `mcq` | true | `B` | `B. Stop all sales of the product throughout the nation and issue a recall for that product.` |
| baseline | `mmlu_13051` | `mcq` | true | `B` | `B. consumer relations` |
| baseline | `mmlu_13052` | `mcq` | true | `B` | `B. 1922` |
| baseline | `mmlu_13053` | `mcq` | false | `C` | `D. Message-oriented` |
| baseline | `mmlu_13054` | `mcq` | true | `B` | `B. to interpret trends for management` |
| baseline | `mmlu_13055` | `mcq` | false | `A` | `B. When people hide their opinions if they do not agree with the majority` |
| baseline | `mmlu_13056` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13057` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13058` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13059` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_13060` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13061` | `mcq` | true | `B` | `B. 1922` |
| baseline | `mmlu_13062` | `mcq` | true | `C` | `C. 2,800` |
| baseline | `mmlu_13063` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_13064` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13065` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13066` | `mcq` | true | `D` | `D. Henry (2006)` |
| baseline | `mmlu_13067` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13068` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13069` | `mcq` | true | `C` | `C. Public affairs` |
| baseline | `mmlu_13070` | `mcq` | true | `B` | `B. Analysis` |
| baseline | `mmlu_13071` | `mcq` | false | `B` | `A. Consider the comprehension level of all of the target audiences.` |
| baseline | `mmlu_13072` | `mcq` | true | `B` | `B. Event` |
| baseline | `mmlu_13073` | `mcq` | false | `D` | `A. Media writing` |
| baseline | `mmlu_13074` | `mcq` | true | `D` | `D. stakeholder analysis` |
| baseline | `mmlu_13075` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13076` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13077` | `mcq` | true | `B` | `B. crisis management` |
| baseline | `mmlu_13078` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13079` | `mcq` | true | `D` | `D. Viral campaigns` |
| baseline | `mmlu_13080` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13081` | `mcq` | false | `C` | `B. 1989` |
| baseline | `mmlu_13082` | `mcq` | false | `B` | `A. Online consumer goods purchases` |
| baseline | `mmlu_13083` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13084` | `mcq` | true | `C` | `C. Open-ended` |
| baseline | `mmlu_13085` | `mcq` | true | `C` | `C. symbol` |
| baseline | `mmlu_13086` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13087` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13088` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13089` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13090` | `mcq` | true | `A` | `A. Inputs` |
| baseline | `mmlu_13091` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13092` | `mcq` | false | `A` | `C. to ensure that the department's events and public relations activities are not neglected` |
| baseline | `mmlu_13093` | `mcq` | false | `C` | `A. Inputs` |
| baseline | `mmlu_13094` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13095` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13096` | `mcq` | true | `A` | `A. The Creel Committee` |
| baseline | `mmlu_13097` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13098` | `mcq` | false | `B` | `A. Shannon and Weaver model` |
| baseline | `mmlu_13099` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13100` | `mcq` | true | `C` | `C. Person-oriented advertising` |
| baseline | `mmlu_13101` | `mcq` | true | `B` | `B. Impact` |
| baseline | `mmlu_13102` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13103` | `mcq` | true | `D` | `D. copyright and trademark law` |
| baseline | `mmlu_13104` | `mcq` | false | `B` | `A. London` |
| baseline | `mmlu_13105` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_13106` | `mcq` | true | `B` | `B. implementation` |
| baseline | `mmlu_13107` | `mcq` | true | `A` | `A. Politics` |
| baseline | `mmlu_13108` | `mcq` | false | `D` | `B. Timeliness` |
| baseline | `mmlu_13109` | `mcq` | true | `B` | `B. Issues management` |
| baseline | `mmlu_13110` | `mcq` | true | `B` | `B. Outputs` |
| baseline | `mmlu_13111` | `mcq` | true | `B` | `B. Localize the news releases for audiences in your geography.` |
| baseline | `mmlu_13112` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13113` | `mcq` | true | `B` | `B. Strategy` |
| baseline | `mmlu_13114` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13115` | `mcq` | true | `A` | `A. workplace violence` |
| baseline | `mmlu_13116` | `mcq` | false | `A` | `D. all of the above` |
| baseline | `mmlu_13117` | `mcq` | false | `A` | `C. Superficial grasp of the client's unique problems` |
| baseline | `mmlu_13118` | `mcq` | true | `D` | `D. 80%` |
| baseline | `mmlu_13119` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13120` | `mcq` | true | `D` | `D. Grunig and Hunt (1984)` |
| baseline | `mmlu_13121` | `mcq` | true | `B` | `B. Media` |
| baseline | `mmlu_13122` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13123` | `mcq` | true | `D` | `D. conducting a pre and post analysis of constituents' opinions` |
| baseline | `mmlu_13124` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13125` | `mcq` | false | `C` | `A. One-quarter` |
| baseline | `mmlu_13126` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13127` | `mcq` | true | `C` | `C. advertising` |
| baseline | `mmlu_13128` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13129` | `mcq` | true | `A` | `A. Securities Act of 1933` |
| baseline | `mmlu_13130` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13131` | `mcq` | false | `C` | `B. 2` |
| baseline | `mmlu_13132` | `mcq` | true | `D` | `D. Twitter` |
| baseline | `mmlu_13133` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13134` | `mcq` | true | `B` | `B. reactive` |
| baseline | `mmlu_13135` | `mcq` | false | `A` | `B. evasion of responsibility` |
| baseline | `mmlu_13136` | `mcq` | true | `D` | `D. planning` |
| baseline | `mmlu_13137` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13138` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13139` | `mcq` | true | `B` | `B. the number who change attitudes and opinions` |
| baseline | `mmlu_13140` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13141` | `mcq` | false | `A` | `C. Business writing` |
| baseline | `mmlu_13142` | `mcq` | false | `C` | `D. Evaluation` |
| baseline | `mmlu_13143` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13144` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13145` | `mcq` | true | `A` | `A. Starbucks` |
| baseline | `mmlu_13146` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13147` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13148` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13149` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13150` | `mcq` | true | `A` | `A and D` |
| baseline | `mmlu_13151` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13152` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13153` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13154` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13155` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_13156` | `mcq` | true | `B` | `B. 1970s` |
| baseline | `mmlu_13157` | `mcq` | true | `A` | `A. Enabling` |
| baseline | `mmlu_13158` | `mcq` | false | `D` | `C. Third parties` |
| baseline | `mmlu_13159` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13160` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13161` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13162` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13163` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13164` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_13165` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13166` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13167` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13168` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13169` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13170` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13171` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13172` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13173` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13174` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13175` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13176` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13177` | `mcq` | true | `C` | `C. The subaltern refers to populations that are marginalized or outside of the hegemonic power structure.` |
| baseline | `mmlu_13178` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13179` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13180` | `mcq` | false | `C` | `A. 1987` |
| baseline | `mmlu_13181` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13182` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13183` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13184` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13185` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13186` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13187` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13188` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13189` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13190` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13191` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13192` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13193` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13194` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13195` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13196` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13197` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13198` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13199` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_13200` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_13201` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13202` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13203` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13204` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13205` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13206` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13207` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13208` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13209` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13210` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13211` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13212` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13213` | `mcq` | true | `D` | `D. All of these.` |
| baseline | `mmlu_13214` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13215` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13216` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13217` | `mcq` | true | `D` | `D. 1991 Gulf War.` |
| baseline | `mmlu_13218` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13219` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13220` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13221` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13222` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13223` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13224` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13225` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13226` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13227` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13228` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13229` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13230` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13231` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13232` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13233` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13234` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13235` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13236` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13237` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13238` | `mcq` | true | `D` | `D. All of these.` |
| baseline | `mmlu_13239` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13240` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13241` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13242` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13243` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13244` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13245` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13246` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13247` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13248` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13249` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13250` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13251` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13252` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13253` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13254` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13255` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13256` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13257` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13258` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13259` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13260` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13261` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13262` | `mcq` | false | `B` | `A. Women did not actively engage in warfare as combatants and so questions of gender or the role of women were not impor` |
| baseline | `mmlu_13263` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13264` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13265` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13266` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13267` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13268` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13269` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13270` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13271` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13272` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_13273` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13274` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13275` | `mcq` | false | `A` | `A/B/C/D` |
| baseline | `mmlu_13276` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13277` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13278` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13279` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13280` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13281` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13282` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13283` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13284` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13285` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13286` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13287` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13288` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13289` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13290` | `mcq` | false | `B` | `A. Digitalised sensitive information` |
| baseline | `mmlu_13291` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13292` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13293` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13294` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13295` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13296` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13297` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13298` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13299` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13300` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13301` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13302` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13303` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13304` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13305` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13306` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13307` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13308` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13309` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13310` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13311` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13312` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13313` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13314` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13316` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13317` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13318` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13319` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13320` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13321` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13322` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13323` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13325` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13326` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13327` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13328` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13329` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13330` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13331` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13332` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13333` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13334` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13335` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13336` | `mcq` | false | `A` | `B. 1990s` |
| baseline | `mmlu_13337` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13338` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13339` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13340` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13341` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13342` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13343` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13344` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13345` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13346` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13347` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13348` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13349` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13350` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13351` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13352` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13353` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13354` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13355` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13356` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13357` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13358` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13359` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13360` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13361` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13362` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13363` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13364` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13365` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13366` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13367` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13368` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13369` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13370` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13371` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13372` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13373` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13374` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13375` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13376` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13378` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13379` | `mcq` | true | `C` | `C. Karl Marx and Friedrich Engels` |
| baseline | `mmlu_13380` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13381` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13382` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13383` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13384` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13385` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13386` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13387` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13388` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13389` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13390` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13391` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13392` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13393` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13394` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13395` | `mcq` | true | `D` | `D. All of these options.` |
| baseline | `mmlu_13396` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13397` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13398` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13399` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13400` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13401` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13402` | `mcq` | false | `A` | `B. The state and state apparatus.` |
| baseline | `mmlu_13403` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13404` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13405` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13406` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13407` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13408` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13409` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13410` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_13411` | `mcq` | true | `B` | `B. seen a temporary aberration from an otherwise 'normal' character` |
| baseline | `mmlu_13412` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13413` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13414` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13415` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13416` | `mcq` | true | `A` | `A. socialization into working class families and communities` |
| baseline | `mmlu_13417` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13418` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13419` | `mcq` | true | `A` | `A. social stratification` |
| baseline | `mmlu_13420` | `mcq` | false | `A` | `B. affective` |
| baseline | `mmlu_13421` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13422` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13423` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13424` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13425` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13426` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13427` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13428` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13429` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13430` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13431` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13432` | `mcq` | true | `A` | `A. active non-work and independence after retirement` |
| baseline | `mmlu_13433` | `mcq` | true | `B` | `B. rational-legal authority` |
| baseline | `mmlu_13434` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13435` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13436` | `mcq` | true | `B` | `B. Social facts` |
| baseline | `mmlu_13437` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13438` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13439` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13440` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13441` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13442` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13443` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13444` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13445` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13446` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13447` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13448` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13449` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13450` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13451` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13452` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13453` | `mcq` | true | `C` | `C. African-Americans who felt excluded from the 'ethnic melting pot' in the USA` |
| baseline | `mmlu_13454` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13455` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13456` | `mcq` | false | `B` | `C. Contagion` |
| baseline | `mmlu_13457` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_13458` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13459` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13460` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13461` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13462` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13463` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13464` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13465` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13466` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13467` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13468` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13469` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13470` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13471` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13472` | `mcq` | true | `A` | `A. response rate bias` |
| baseline | `mmlu_13473` | `mcq` | false | `A` | `B. we create and negotiate our roles through interaction with others` |
| baseline | `mmlu_13474` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13475` | `mcq` | true | `A` | `A. Gentrification` |
| baseline | `mmlu_13476` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13477` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13478` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13479` | `mcq` | true | `A` | `A. community alternatives to imprisonment and institutional care` |
| baseline | `mmlu_13480` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_13481` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13482` | `mcq` | true | `C` | `C. Scapegoating` |
| baseline | `mmlu_13483` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13484` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13485` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13486` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13487` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13488` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13489` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13490` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13491` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13492` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13493` | `mcq` | true | `A` | `A. Functionalism` |
| baseline | `mmlu_13494` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13495` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13496` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13497` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13498` | `mcq` | true | `A` | `A. definitions and indicators can vary, making valid comparisons problematic` |
| baseline | `mmlu_13499` | `mcq` | true | `A` | `A` |
