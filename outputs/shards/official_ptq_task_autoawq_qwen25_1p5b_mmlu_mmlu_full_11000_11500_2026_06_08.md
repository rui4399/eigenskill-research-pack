# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 197 / 500 | 0.3940 | 8.5109 | 0.185291 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_11000` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11001` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11002` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11003` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11004` | `mcq` | false | `C` | `D. lose, because she assumed the risk by not making the "patch test."` |
| baseline | `mmlu_11005` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11007` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11008` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11009` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11010` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11011` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11012` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11013` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11014` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11015` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11016` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11017` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11018` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11019` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11020` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11021` | `mcq` | false | `B` | `C. overrule the objection, because the evidence is relevant as to the question of the doctor's negligent hiring.` |
| baseline | `mmlu_11022` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11023` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11024` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11025` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11026` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11027` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11028` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11029` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11030` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11031` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11032` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11033` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11034` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11035` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11036` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11037` | `mcq` | true | `D` | `D. Yes, because the defense has the burden of proving the defense of duress by a preponderance of the evidence.` |
| baseline | `mmlu_11038` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11039` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11040` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11041` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11042` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11043` | `mcq` | true | `C` | `C. fail, because the purchase by the tenant vitiated any further contractual obligations.` |
| baseline | `mmlu_11044` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11045` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11046` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11047` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11048` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11049` | `mcq` | false | `B` | `D. $20,000, which covers the difference between the contract price and the sale price.` |
| baseline | `mmlu_11050` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11051` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11052` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11053` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11054` | `mcq` | false | `D` | `B. win, because the clerk's conduct was extreme and outrageous.` |
| baseline | `mmlu_11055` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11056` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11057` | `mcq` | true | `D` | `D. The execution of the defendant constitutes cruel and unusual punishment under the Eighth Amendment and cannot be allo` |
| baseline | `mmlu_11058` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11059` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11060` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11061` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11062` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11063` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11064` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11065` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11066` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11067` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11068` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11069` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11070` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11071` | `mcq` | false | `A` | `B. The woman, because she had a reasonable basis for fearing that the man would attack her.` |
| baseline | `mmlu_11072` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11073` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11074` | `mcq` | false | `B` | `D. not prevail, because the ordinance is rationally related to a legitimate state interest.` |
| baseline | `mmlu_11075` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11076` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11077` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11078` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11079` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11080` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11081` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11082` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11083` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11084` | `mcq` | true | `C` | `C. Yes, because the easement remains valid.` |
| baseline | `mmlu_11085` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11086` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11087` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11088` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11089` | `mcq` | false | `B` | `C. not recover, because the chef did not know that the egg roll was on the floor.` |
| baseline | `mmlu_11090` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11091` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11092` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11093` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11094` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11095` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11096` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11097` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11098` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11099` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11100` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11101` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11102` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11103` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11104` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11105` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11106` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11107` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11108` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11109` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11110` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11111` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11112` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11113` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11114` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11115` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11116` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11117` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11118` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11119` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11120` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11121` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11122` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11123` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11124` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11125` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11126` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11127` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11128` | `mcq` | false | `D` | `C. Yes, because the auto dealer placed a defective car into the stream of commerce.` |
| baseline | `mmlu_11129` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11130` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11131` | `mcq` | true | `D` | `D. Move to strike the separate defense as irrelevant.` |
| baseline | `mmlu_11132` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11133` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11134` | `mcq` | true | `C` | `C. Yes, because in most circumstances an "unclaimed" notification is insufficient to satisfy the demands of due process.` |
| baseline | `mmlu_11135` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11136` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11137` | `mcq` | true | `C` | `C. not guilty, because the defendant was unconscious.` |
| baseline | `mmlu_11138` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11139` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11140` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11141` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11142` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11143` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11144` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11145` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11146` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11147` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11148` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11149` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11150` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11151` | `mcq` | true | `C` | `C. The last in time prevails` |
| baseline | `mmlu_11152` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11153` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11154` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11155` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11156` | `mcq` | false | `C` | `D. both the manufacturer and the operator.` |
| baseline | `mmlu_11157` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11158` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11159` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11160` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11161` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11162` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11163` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11164` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11165` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11166` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11167` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11168` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11169` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11170` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11171` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11172` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11173` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11174` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11175` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11176` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11177` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11178` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11179` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11180` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11181` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11182` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11183` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11184` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11185` | `mcq` | false | `C` | `A. nothing, because the buyer never assented to the assignment.` |
| baseline | `mmlu_11186` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11187` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11188` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11189` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11190` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11191` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11192` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11193` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11194` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11195` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11196` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11197` | `mcq` | false | `D` | `C. Cause-in-fact.` |
| baseline | `mmlu_11198` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11199` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11200` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11201` | `mcq` | true | `D` | `D. not guilty.` |
| baseline | `mmlu_11202` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11203` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11204` | `mcq` | false | `B` | `D. not prevail, because the passenger assumed the risk by not moving to another seat away from the salesman.` |
| baseline | `mmlu_11205` | `mcq` | true | `D` | `D. inadmissible, because the letter was the fruit of an illegal search and seizure.` |
| baseline | `mmlu_11206` | `mcq` | false | `A` | `C. Yes, because the landscaper could have obtained possession of the truck through legal action rather than by agreeing ` |
| baseline | `mmlu_11207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11208` | `mcq` | true | `C` | `C. $5,000. 00` |
| baseline | `mmlu_11209` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11210` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11211` | `mcq` | false | `B` | `A. nothing.` |
| baseline | `mmlu_11212` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11213` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11214` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11215` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11216` | `mcq` | false | `B` | `C. Yes, because the oral price term is relevant to whether the writing should be reformed.` |
| baseline | `mmlu_11217` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11218` | `mcq` | true | `A` | `A. The commerce clause.` |
| baseline | `mmlu_11219` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11220` | `mcq` | true | `D` | `D. No contract exists.` |
| baseline | `mmlu_11221` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11222` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11223` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11224` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11225` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11226` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11227` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11228` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11229` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11230` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11231` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11232` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11233` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11234` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11235` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11236` | `mcq` | true | `D` | `D. not succeed, because the telephone operator's erroneous identification was protected by a qualified privilege for sta` |
| baseline | `mmlu_11237` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11238` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11239` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11240` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11241` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11242` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11243` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11244` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11245` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11246` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11247` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11248` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11249` | `mcq` | false | `C` | `D. not prevail, because the second friend consented to participate in the Russian roulette game.` |
| baseline | `mmlu_11250` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11251` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11252` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11253` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11254` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11255` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11256` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11257` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11258` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11259` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11260` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11261` | `mcq` | false | `B` | `D. Yes, because the mother suffered severe emotional distress as a result of viewing the video.` |
| baseline | `mmlu_11262` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11263` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11264` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11265` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11266` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11267` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11268` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11269` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11270` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11271` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11272` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11273` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11274` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11275` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11276` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11277` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11278` | `mcq` | false | `A` | `D. not prevail, because the deed of conveyance from the farmer to the investor failed to contain any mention of the righ` |
| baseline | `mmlu_11279` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11280` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11281` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11282` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11283` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11284` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11285` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11286` | `mcq` | true | `D` | `D. Yes, because the evidence was sufficient to support the jury's verdict.` |
| baseline | `mmlu_11287` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11288` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11289` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11290` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11291` | `mcq` | false | `D` | `C. not prevail, because an adverse possessor takes title subject to an equitable lien from the dispossessed owner.` |
| baseline | `mmlu_11292` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11293` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11294` | `mcq` | false | `A` | `C. not prevail, because the contractor negligently installed the plate glass door.` |
| baseline | `mmlu_11295` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11297` | `mcq` | true | `C` | `C. II and III only.` |
| baseline | `mmlu_11298` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11299` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11300` | `mcq` | true | `D` | `D. not prevail, if the hotel used reasonable care in selecting the lock.` |
| baseline | `mmlu_11301` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11302` | `mcq` | false | `D` | `C. not recover, because the boy was a trespasser.` |
| baseline | `mmlu_11303` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11304` | `mcq` | true | `A` | `A. The investor.` |
| baseline | `mmlu_11305` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11307` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11308` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11309` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11310` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11311` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11312` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11313` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11314` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11315` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11316` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11317` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11318` | `mcq` | true | `D` | `D. The man did not intend to commit a crime inside the house.` |
| baseline | `mmlu_11319` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11320` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11321` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11322` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11323` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11324` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11325` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11326` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11327` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11328` | `mcq` | true | `C` | `C. Quantum meruit for the reasonable value of his services rendered in installing the 150 fixtures.` |
| baseline | `mmlu_11329` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11330` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11331` | `mcq` | true | `C` | `C. dismiss the action, because the issues are not ripe.` |
| baseline | `mmlu_11332` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11333` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11334` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11335` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11336` | `mcq` | false | `C` | `A. The owner, because the mother's assignment to the nursing home was void as violative of the anti-assignment clause.` |
| baseline | `mmlu_11337` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11338` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11339` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11340` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11341` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11342` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11343` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11344` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11345` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11346` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11347` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11348` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11349` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11350` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11351` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11352` | `mcq` | false | `A` | `D. Yes, because the woman's offer and the neighbor's acceptance created an enforceable contract.` |
| baseline | `mmlu_11353` | `mcq` | false | `B` | `D. not admissible.` |
| baseline | `mmlu_11354` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11355` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11356` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11357` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11358` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11359` | `mcq` | false | `D` | `C. Yes, because the wife's death without issue would convert the nephew's fee into a reversionary interest.` |
| baseline | `mmlu_11360` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11361` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11362` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11363` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11364` | `mcq` | false | `C` | `A. $0. 00` |
| baseline | `mmlu_11365` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11366` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11367` | `mcq` | true | `D` | `D. Yes, the evidence must be suppressed because the plain view doctrine does not apply where the officer had no probable` |
| baseline | `mmlu_11368` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11369` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11370` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11371` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11372` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11373` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11374` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11375` | `mcq` | false | `A` | `D. reckless endangerment.` |
| baseline | `mmlu_11376` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11377` | `mcq` | true | `B` | `B. Yes, because a qualified bank employee must first authenticate them in person or provide a certification in complianc` |
| baseline | `mmlu_11378` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11379` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11380` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11381` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11382` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11383` | `mcq` | true | `C` | `C. not recover, because the friend assumed the risk by trying to open the dishwasher.` |
| baseline | `mmlu_11384` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11385` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11386` | `mcq` | false | `C` | `B. recover $27,000.` |
| baseline | `mmlu_11387` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11388` | `mcq` | false | `B` | `D. Yes, because the law is rationally related to a legitimate state interest.` |
| baseline | `mmlu_11389` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11390` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11391` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11392` | `mcq` | false | `A` | `D. not granted, because the second statement was volunteered after a knowing Miranda waiver.` |
| baseline | `mmlu_11393` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11394` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11395` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11396` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11397` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11398` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11399` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11400` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11401` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11402` | `mcq` | false | `B` | `D. $25,000, or the commission equivalent of 5 percent on the sale of the property for $500,000, because all conditions p` |
| baseline | `mmlu_11403` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11404` | `mcq` | false | `A` | `C. The woman.` |
| baseline | `mmlu_11405` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11406` | `mcq` | true | `C` | `C. The contract is void, because the father was under guardianship at the time it was made.` |
| baseline | `mmlu_11407` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11408` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11409` | `mcq` | true | `D` | `D. Hearse` |
| baseline | `mmlu_11410` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11411` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11412` | `mcq` | false | `B` | `C. Yes, because a defect in the snowblower caused the homeowner's injury.` |
| baseline | `mmlu_11413` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11414` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11415` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11416` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11417` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11418` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11419` | `mcq` | true | `D` | `D. Yes, as impeachment for prior inconsistency.` |
| baseline | `mmlu_11420` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11421` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11422` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11423` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11424` | `mcq` | false | `B` | `C. not recover, because the nurse's act was a supervening superseding cause.` |
| baseline | `mmlu_11425` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11426` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11427` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11429` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11430` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11431` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11432` | `mcq` | true | `A` | `A. Abuse of discretion.` |
| baseline | `mmlu_11433` | `mcq` | false | `A` | `D. not prevail, because the intern's proper remedy is indemnification, not contribution.` |
| baseline | `mmlu_11434` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11435` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11436` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11437` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11438` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11439` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11440` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11441` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11442` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11443` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11444` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11445` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11446` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11447` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11448` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11449` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11450` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11451` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11452` | `mcq` | false | `C` | `D. $80,000, because the contractor reasonably relied to his detriment on the electrician's bid in formulating his job es` |
| baseline | `mmlu_11453` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11454` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11455` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11456` | `mcq` | false | `B` | `D. The uncle is entitled to no share of any of the monies raised because the uncle's lack of contact with the best frien` |
| baseline | `mmlu_11457` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11458` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11459` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11460` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11461` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11462` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11463` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11464` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11465` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11466` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11467` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11468` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11469` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11470` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11471` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11472` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11473` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11474` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11475` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11476` | `mcq` | false | `A` | `C. No, because there was no contract formed due to the purchaser's lack of assent to the additional terms and conditions` |
| baseline | `mmlu_11477` | `mcq` | false | `B` | `D. not succeed, because the deviation impaired the value of the entire contract.` |
| baseline | `mmlu_11478` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11479` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11480` | `mcq` | false | `A` | `B. Four.` |
| baseline | `mmlu_11481` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11482` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11483` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11484` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11485` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11486` | `mcq` | false | `B` | `C. Yes, because the double jeopardy protection prohibits a second prosecution following a conviction for the same offens` |
| baseline | `mmlu_11487` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11488` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11489` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11490` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11491` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11492` | `mcq` | false | `D` | `C. both larceny and embezzlement.` |
| baseline | `mmlu_11493` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11494` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11495` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11496` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11497` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11498` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11499` | `mcq` | false | `C` | `B` |
