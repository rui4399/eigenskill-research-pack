# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 209 / 500 | 0.4180 | 4.8028 | 0.374052 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_11000` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11001` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11002` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11003` | `mcq` | true | `A` | `A. The ex post facto clause.` |
| baseline | `mmlu_11004` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11005` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11007` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11008` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11009` | `mcq` | false | `B` | `D. recover nothing, because the traffic statute was not designed to protect against the type of harm that the owner suff` |
| baseline | `mmlu_11010` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11011` | `mcq` | true | `A` | `A. Yes, because the seller breached the agreement by not following the procedure stated in the purchase agreement.` |
| baseline | `mmlu_11012` | `mcq` | true | `B` | `B. The gift violates the establishment clause.` |
| baseline | `mmlu_11013` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11014` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11015` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11016` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11017` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11018` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11019` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11020` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11021` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11022` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11023` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11024` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11025` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11026` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11027` | `mcq` | true | `A` | `A. Deny the motion and submit the case to the jury with instructions that the custom is relevant but not conclusive on t` |
| baseline | `mmlu_11028` | `mcq` | true | `A` | `A. Reject the instruction, based on ex post facto.` |
| baseline | `mmlu_11029` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11030` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11031` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11032` | `mcq` | true | `A` | `A. The outward signs all indicate that the suspect understood the procedure and gave a voluntary confession despite his ` |
| baseline | `mmlu_11033` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11034` | `mcq` | true | `D` | `D. A or B` |
| baseline | `mmlu_11035` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11036` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11037` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11038` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11039` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11040` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11041` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11042` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11043` | `mcq` | true | `C` | `C. fail, because the purchase by the tenant vitiated any further contractual obligations.` |
| baseline | `mmlu_11044` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11045` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11046` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11047` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11048` | `mcq` | true | `C` | `C. Yes, because it is prior testimony of an unavailable declarant.` |
| baseline | `mmlu_11049` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11050` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11051` | `mcq` | true | `A` | `A. first-degree murder.` |
| baseline | `mmlu_11052` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11053` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11054` | `mcq` | false | `D` | `B. win, because the clerk's conduct was extreme and outrageous.` |
| baseline | `mmlu_11055` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11056` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11057` | `mcq` | true | `D` | `D. The execution of the defendant constitutes cruel and unusual punishment under the Eighth Amendment and cannot be allo` |
| baseline | `mmlu_11058` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11059` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11060` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11061` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11062` | `mcq` | false | `C` | `D. admissible, because they establish a pattern of similar actions.` |
| baseline | `mmlu_11063` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11064` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11065` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11066` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11067` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11068` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11069` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11070` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11071` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11072` | `mcq` | false | `C` | `B. This was an unlawful taking without prior notice and therefore unconstitutional.` |
| baseline | `mmlu_11073` | `mcq` | false | `A` | `D. not recover, because there was no contract between the handyman and the homeowner.` |
| baseline | `mmlu_11074` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11075` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11076` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11077` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11078` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11079` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11080` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11081` | `mcq` | true | `A` | `A. The first purchaser wins because the second purchaser had constructive notice from the title search that someone else` |
| baseline | `mmlu_11082` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11083` | `mcq` | false | `D` | `C. No, because privity of contract does not exist between the woman and the owner of the lumber yard.` |
| baseline | `mmlu_11084` | `mcq` | true | `C` | `C. Yes, because the easement remains valid.` |
| baseline | `mmlu_11085` | `mcq` | true | `A` | `A. Extortion and battery.` |
| baseline | `mmlu_11086` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11087` | `mcq` | true | `D` | `D. The testimony is admissible because habit and routine practice are admissible under the Federal Rules of Evidence.` |
| baseline | `mmlu_11088` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11089` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11090` | `mcq` | true | `D` | `D. The encumbrance would not entitle the rancher to rescind the real estate contract until closing on January 15.` |
| baseline | `mmlu_11091` | `mcq` | false | `C` | `A. sustained the objection, as hearsay not within any recognized exception.` |
| baseline | `mmlu_11092` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11093` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11094` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11095` | `mcq` | true | `B` | `B. The pedestrian must prove by a preponderance of the evidence that the painting company was negligent.` |
| baseline | `mmlu_11096` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11097` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11098` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11099` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11100` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11101` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11102` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11103` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11104` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11105` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11106` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11107` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11108` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11109` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11110` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11111` | `mcq` | false | `D` | `A. the bartender.` |
| baseline | `mmlu_11112` | `mcq` | false | `B` | `D. The friend and the co-worker are tenants in common of the northeast quarter of the farm; and the friend is the owner ` |
| baseline | `mmlu_11113` | `mcq` | true | `D` | `D. no crime.` |
| baseline | `mmlu_11114` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11115` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11116` | `mcq` | false | `D` | `C. invalid, because it is an unauthorized extension of executive power.` |
| baseline | `mmlu_11117` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11118` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11119` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11120` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11121` | `mcq` | false | `D` | `A. The evidence is too prejudicial and must be excluded.` |
| baseline | `mmlu_11122` | `mcq` | true | `B` | `B. Yes, because the defect could have been discovered through the exercise of reasonable care by the bicycle company.` |
| baseline | `mmlu_11123` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11124` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11125` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11126` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11127` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11128` | `mcq` | false | `D` | `C. Yes, because the auto dealer placed a defective car into the stream of commerce.` |
| baseline | `mmlu_11129` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11130` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11131` | `mcq` | true | `D` | `D. Move to strike the separate defense as irrelevant.` |
| baseline | `mmlu_11132` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11133` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11134` | `mcq` | true | `C` | `C. Yes, because in most circumstances an "unclaimed" notification is insufficient to satisfy the demands of due process.` |
| baseline | `mmlu_11135` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11136` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11137` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11138` | `mcq` | false | `C` | `D. Yes, because he succeeded in saving the stockbroker's life.` |
| baseline | `mmlu_11139` | `mcq` | false | `A` | `D. No, because a defendant cannot be retried for attempted commission of a crime that has been ruled unconstitutional by` |
| baseline | `mmlu_11140` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11141` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11142` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11143` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11144` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11145` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11146` | `mcq` | false | `C` | `A. burglary and arson.` |
| baseline | `mmlu_11147` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11148` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11149` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11150` | `mcq` | true | `A` | `A. Yes, because in the law of negligence the defendant takes the plaintiff "as he finds her."` |
| baseline | `mmlu_11151` | `mcq` | true | `C` | `C. The last in time prevails` |
| baseline | `mmlu_11152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11153` | `mcq` | false | `C` | `D. 50% to Joan and the income from the remaining 50% to Joan for life, remainder to the Salvation Army, if Joan files a ` |
| baseline | `mmlu_11154` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11155` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11156` | `mcq` | false | `C` | `D. both the manufacturer and the operator.` |
| baseline | `mmlu_11157` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11158` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11159` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11160` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11161` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11162` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11163` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11164` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11165` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11166` | `mcq` | false | `A` | `D. Yes, she can claim membership in a group of newcomers who are coming and are being treated differently than everyone ` |
| baseline | `mmlu_11167` | `mcq` | false | `B` | `D. not recover, because he was not in privity of contract.` |
| baseline | `mmlu_11168` | `mcq` | false | `A` | `C. No, because the builder waived its right to reject the nonconforming goods by not returning them promptly to the comp` |
| baseline | `mmlu_11169` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11170` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11171` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11172` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11173` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11174` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11175` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11176` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11177` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11178` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11179` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11180` | `mcq` | false | `C` | `A. No interest.` |
| baseline | `mmlu_11181` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11182` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11183` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11184` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11185` | `mcq` | false | `C` | `A. nothing, because the buyer never assented to the assignment.` |
| baseline | `mmlu_11186` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11187` | `mcq` | false | `D` | `A. win, because the player's conduct was extreme and outrageous.` |
| baseline | `mmlu_11188` | `mcq` | true | `C` | `C. The man, because a landowner is entitled to support of his land in its natural condition.` |
| baseline | `mmlu_11189` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11190` | `mcq` | false | `B` | `C. recover nothing, because he had the last clear chance to avoid the collision.` |
| baseline | `mmlu_11191` | `mcq` | false | `D` | `A. Yes, because art works and other physical evidence must be authenticated by their official custodian.` |
| baseline | `mmlu_11192` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11193` | `mcq` | false | `A` | `C. excluded, because the defendant failed to lay a foundation, thus not giving the plaintiff an opportunity to deny or e` |
| baseline | `mmlu_11194` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11195` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11196` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11197` | `mcq` | true | `D` | `D. Proximate or legal causation.` |
| baseline | `mmlu_11198` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11199` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11200` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11201` | `mcq` | true | `D` | `D. not guilty.` |
| baseline | `mmlu_11202` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11203` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11204` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11205` | `mcq` | true | `D` | `D. inadmissible, because the letter was the fruit of an illegal search and seizure.` |
| baseline | `mmlu_11206` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11208` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11209` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11210` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11211` | `mcq` | false | `B` | `A. nothing.` |
| baseline | `mmlu_11212` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11213` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11214` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11215` | `mcq` | false | `D` | `C. the prior mortgage has no legal effect on the investor's rights under the installment land-sale agreement.` |
| baseline | `mmlu_11216` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11217` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11218` | `mcq` | true | `A` | `A. The commerce clause.` |
| baseline | `mmlu_11219` | `mcq` | false | `C` | `B. No, hearsay without an exception.` |
| baseline | `mmlu_11220` | `mcq` | true | `D` | `D. No contract exists.` |
| baseline | `mmlu_11221` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11222` | `mcq` | false | `B` | `D. No, because the court entered final judgment for Plaintiff before the motion to set aside the verdict was filed.` |
| baseline | `mmlu_11223` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11224` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11225` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11226` | `mcq` | false | `C` | `B. shifting executory interest.` |
| baseline | `mmlu_11227` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11228` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11229` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11230` | `mcq` | false | `A` | `C. No, the individual has an absolute constitutional right to be free from intrusion of medications into his system agai` |
| baseline | `mmlu_11231` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11232` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11233` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11234` | `mcq` | true | `D` | `D. The law is unconstitutional because it infringes on fundamental rights of the individual.` |
| baseline | `mmlu_11235` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11236` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11237` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11238` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11239` | `mcq` | false | `B` | `A. hearsay.` |
| baseline | `mmlu_11240` | `mcq` | false | `A` | `D. denied, because the trier of fact may still infer liability for trespass.` |
| baseline | `mmlu_11241` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11242` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11243` | `mcq` | false | `D` | `B. in the co-worker, free and clear of the mortgage.` |
| baseline | `mmlu_11244` | `mcq` | true | `D` | `D. Yes, because there was an agreement to rob the bank and an overt act in furtherance of the agreement.` |
| baseline | `mmlu_11245` | `mcq` | true | `C` | `C. not recover, because the shooting was not a foreseeable consequence of the taxi driver's conduct.` |
| baseline | `mmlu_11246` | `mcq` | false | `B` | `D. Part payment of an unliquidated claim does not constitute sufficient consideration for the discharge of the entire cl` |
| baseline | `mmlu_11247` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11248` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11249` | `mcq` | false | `C` | `D. not prevail, because the second friend consented to participate in the Russian roulette game.` |
| baseline | `mmlu_11250` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11251` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11252` | `mcq` | true | `C` | `C. denied, because the exclusionary rule has not been extended to grand jury hearings.` |
| baseline | `mmlu_11253` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11254` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11255` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11256` | `mcq` | true | `D` | `D. Yes, because the circumstances, including prior practice, showed intent to contract and a meeting of the minds.` |
| baseline | `mmlu_11257` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11258` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11259` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11260` | `mcq` | true | `C` | `C. The treaties and immigration laws of the United States.` |
| baseline | `mmlu_11261` | `mcq` | false | `B` | `D. Yes, because the mother suffered severe emotional distress as a result of viewing the video.` |
| baseline | `mmlu_11262` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11263` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11264` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11265` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11266` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11267` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11268` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11269` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11270` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11271` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11272` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11273` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11274` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11275` | `mcq` | false | `C` | `D. not recover, if the hunter did not intend to shoot the hiker.` |
| baseline | `mmlu_11276` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11277` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11278` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11279` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11280` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11281` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11282` | `mcq` | true | `D` | `D. The subsequent mortgagee, the bank, would prevail as against the prior conveyee (the friend), who failed to record be` |
| baseline | `mmlu_11283` | `mcq` | true | `B` | `B. It may be proved to impeach him as a witness.` |
| baseline | `mmlu_11284` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11285` | `mcq` | true | `C` | `C. Suit dismissed, because it presents a nonjusticiable political question.` |
| baseline | `mmlu_11286` | `mcq` | true | `D` | `D. Yes, because the evidence was sufficient to support the jury's verdict.` |
| baseline | `mmlu_11287` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11288` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11289` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11290` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11291` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11292` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11293` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11294` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11295` | `mcq` | true | `B` | `B. the bank, because the after-acquired property clause in its mortgage is enforceable and takes priority over the frien` |
| baseline | `mmlu_11296` | `mcq` | true | `D` | `D. present evidence of the authenticity of the letter.` |
| baseline | `mmlu_11297` | `mcq` | true | `C` | `C. II and III only.` |
| baseline | `mmlu_11298` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11299` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11300` | `mcq` | true | `D` | `D. not prevail, if the hotel used reasonable care in selecting the lock.` |
| baseline | `mmlu_11301` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11302` | `mcq` | false | `D` | `A. recover, under the "attractive nuisance" doctrine.` |
| baseline | `mmlu_11303` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11304` | `mcq` | true | `A` | `A. The investor.` |
| baseline | `mmlu_11305` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11307` | `mcq` | true | `D` | `D. The doctrine of equitable conversion requires such a result.` |
| baseline | `mmlu_11308` | `mcq` | false | `D` | `C. Yes, because of the doctrine of equitable redemption.` |
| baseline | `mmlu_11309` | `mcq` | false | `A` | `D. no recovery.` |
| baseline | `mmlu_11310` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11311` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11312` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11313` | `mcq` | false | `C` | `B. recover, because she would not have suffered the emotional trauma had it not been for the neighbor's threat to her ch` |
| baseline | `mmlu_11314` | `mcq` | true | `D` | `D. No, criminal battery in this case is a general intent crime and the defense of voluntary intoxication is not availabl` |
| baseline | `mmlu_11315` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11316` | `mcq` | true | `C` | `C. the y-brand and the z-brand stereos.` |
| baseline | `mmlu_11317` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11318` | `mcq` | true | `D` | `D. The man did not intend to commit a crime inside the house.` |
| baseline | `mmlu_11319` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11320` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11321` | `mcq` | false | `B` | `D. No, because the classmate had the girl's implied consent to act in an emergency.` |
| baseline | `mmlu_11322` | `mcq` | false | `C` | `B. The complaint does not allege that the manufacturer's conduct was extreme and outrageous.` |
| baseline | `mmlu_11323` | `mcq` | false | `B` | `C. The woman has a cause of action against both the repair store and the handyman.` |
| baseline | `mmlu_11324` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11325` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11326` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11327` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11328` | `mcq` | true | `C` | `C. Quantum meruit for the reasonable value of his services rendered in installing the 150 fixtures.` |
| baseline | `mmlu_11329` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11330` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11331` | `mcq` | false | `C` | `A. dismiss the action, because the suit involves a political question.` |
| baseline | `mmlu_11332` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11333` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11334` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11335` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11336` | `mcq` | false | `C` | `A. The owner, because the mother's assignment to the nursing home was void as violative of the anti-assignment clause.` |
| baseline | `mmlu_11337` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11338` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11339` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11340` | `mcq` | true | `B` | `B. the statute is an ex post facto law` |
| baseline | `mmlu_11341` | `mcq` | false | `B` | `D. Yes, because the defendant was denied both the right to counsel and the right to a jury trial.` |
| baseline | `mmlu_11342` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11343` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11344` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11345` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11346` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11347` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11348` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11349` | `mcq` | false | `A` | `C. No, because people dealing with an assistant at a convention have a duty to determine whether that person is in fact ` |
| baseline | `mmlu_11350` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11351` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11352` | `mcq` | true | `A` | `A. No, because the contract was voidable due to the woman's apparent incapacity.` |
| baseline | `mmlu_11353` | `mcq` | false | `B` | `D. not admissible.` |
| baseline | `mmlu_11354` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11355` | `mcq` | false | `A` | `C. No, because the man's revocation was effective, since the neighbor had not completed performance.` |
| baseline | `mmlu_11356` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11357` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11358` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11359` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11360` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11361` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11362` | `mcq` | true | `C` | `C. not succeed, because the risk of loss was on the buyer.` |
| baseline | `mmlu_11363` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11364` | `mcq` | false | `C` | `A. $0. 00` |
| baseline | `mmlu_11365` | `mcq` | true | `A` | `A. False pretenses.` |
| baseline | `mmlu_11366` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11367` | `mcq` | false | `D` | `B. No, the evidence was properly seized because the officer had a right to investigate it further once he had properly e` |
| baseline | `mmlu_11368` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11369` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11370` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11371` | `mcq` | false | `C` | `D. win, because mere non-use of an easement does not extinguish it.` |
| baseline | `mmlu_11372` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11373` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11374` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11375` | `mcq` | false | `A` | `D. reckless endangerment.` |
| baseline | `mmlu_11376` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11377` | `mcq` | true | `B` | `B. Yes, because a qualified bank employee must first authenticate them in person or provide a certification in complianc` |
| baseline | `mmlu_11378` | `mcq` | false | `D` | `C. Yes, because the manufacturer's note failed to contain a signature.` |
| baseline | `mmlu_11379` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11380` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11381` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11382` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11383` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11384` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11385` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11386` | `mcq` | false | `C` | `B. recover $27,000.` |
| baseline | `mmlu_11387` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11388` | `mcq` | false | `B` | `D. Yes, because the law is rationally related to a legitimate state interest.` |
| baseline | `mmlu_11389` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11390` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11391` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11392` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11393` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11394` | `mcq` | false | `C` | `A. sustained the objection on the grounds that the former girlfriend's testimony would be inadmissible opinion evidence.` |
| baseline | `mmlu_11395` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11396` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11397` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11398` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11399` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11400` | `mcq` | true | `A` | `A. The contractor, because his signing a contract with the homeowner and completing the work according to the plans and ` |
| baseline | `mmlu_11401` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11402` | `mcq` | false | `B` | `D. $25,000, or the commission equivalent of 5 percent on the sale of the property for $500,000, because all conditions p` |
| baseline | `mmlu_11403` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11404` | `mcq` | false | `A` | `C. The woman.` |
| baseline | `mmlu_11405` | `mcq` | false | `C` | `D. An undivided one-half interest because the 20-year limitation period did not run against her because she was unaware ` |
| baseline | `mmlu_11406` | `mcq` | false | `C` | `A. The contract is enforceable, because a reasonable person in the situation of the seller would have thought that the f` |
| baseline | `mmlu_11407` | `mcq` | true | `A` | `A. Yes, because willfulness clause requires proof of both knowledge of the law and a specific intent to commit the crime` |
| baseline | `mmlu_11408` | `mcq` | false | `C` | `D. Yes, because the client's note and the attorney's performance created an implied-in-fact contract.` |
| baseline | `mmlu_11409` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11410` | `mcq` | false | `A` | `D. win, because the assignment of future rights is enforceable.` |
| baseline | `mmlu_11411` | `mcq` | true | `A` | `A. Larceny.` |
| baseline | `mmlu_11412` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11413` | `mcq` | false | `D` | `C. Yes, and the plaintiff should be allowed the option of reading it into evidence or having the diary received as an ex` |
| baseline | `mmlu_11414` | `mcq` | false | `D` | `A. No, because the potential juror said that he could fairly consider the evidence in the case.` |
| baseline | `mmlu_11415` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11416` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11417` | `mcq` | false | `C` | `B. The federal court should refuse to hear the case because it presents a nonjusticiable political question.  This state` |
| baseline | `mmlu_11418` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11419` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11420` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11421` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11422` | `mcq` | false | `B` | `A. No crime.` |
| baseline | `mmlu_11423` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11424` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11425` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11426` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11427` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11429` | `mcq` | false | `D` | `A. Affirmative covenant(s).` |
| baseline | `mmlu_11430` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11431` | `mcq` | true | `C` | `C. No, because the sign did not explain the danger and only told her that it was not available, and she therefore did no` |
| baseline | `mmlu_11432` | `mcq` | true | `A` | `A. Abuse of discretion.` |
| baseline | `mmlu_11433` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11434` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11435` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11436` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11437` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11438` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11439` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11440` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11441` | `mcq` | true | `A` | `A. Yes, because the renewal premium was placed in the mailbox before the date of expiration, and the notice did not say ` |
| baseline | `mmlu_11442` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11443` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11444` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11445` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11446` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11447` | `mcq` | false | `B` | `D. Yes, because it serves a legitimate government interest in protecting public health.` |
| baseline | `mmlu_11448` | `mcq` | false | `A` | `C. excluded, because it is improper negative evidence.` |
| baseline | `mmlu_11449` | `mcq` | false | `A` | `D. No, because the granddaughter predeceased the widow, title to the apartment building passes to the friend and assista` |
| baseline | `mmlu_11450` | `mcq` | true | `A` | `A. Yes, because the search was unconstitutional due to the officer having no reasonable suspicion that would justify sea` |
| baseline | `mmlu_11451` | `mcq` | true | `A` | `A. Yes, because this was entrapment in that the intent to commit the crime originated with the government.` |
| baseline | `mmlu_11452` | `mcq` | false | `C` | `D. $80,000, because the contractor reasonably relied to his detriment on the electrician's bid in formulating his job es` |
| baseline | `mmlu_11453` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11454` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11455` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11456` | `mcq` | false | `B` | `A. As a cotenant in possession, the best friend retains the profits from his crops and the rents paid by the teacher.` |
| baseline | `mmlu_11457` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11458` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11459` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11460` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11461` | `mcq` | true | `A` | `A. The search was invalid and the evidence must be suppressed because the co-occupant of the premises was present and sp` |
| baseline | `mmlu_11462` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11463` | `mcq` | true | `C` | `C. The equal protection clause of the Fourteenth Amendment.` |
| baseline | `mmlu_11464` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11465` | `mcq` | true | `B` | `B. The case presents a nonjusticiable political question.` |
| baseline | `mmlu_11466` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11467` | `mcq` | true | `B` | `B. The objective intent of the parties.` |
| baseline | `mmlu_11468` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11469` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11470` | `mcq` | false | `B` | `C. Because the contract violates the law and is void, the court will not enforce it.` |
| baseline | `mmlu_11471` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11472` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11473` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11474` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11475` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11476` | `mcq` | false | `A` | `C. No, because there was no contract formed due to the purchaser's lack of assent to the additional terms and conditions` |
| baseline | `mmlu_11477` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11478` | `mcq` | true | `A` | `A. Yes, there was no reasonable suspicion or probable cause for the officer to stop and search her.` |
| baseline | `mmlu_11479` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11480` | `mcq` | false | `A` | `B. Four.` |
| baseline | `mmlu_11481` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11482` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11483` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11484` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11485` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11486` | `mcq` | false | `B` | `C. Yes, because the double jeopardy protection prohibits a second prosecution following a conviction for the same offens` |
| baseline | `mmlu_11487` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11488` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11489` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11490` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11491` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11492` | `mcq` | false | `D` | `C. both larceny and embezzlement.` |
| baseline | `mmlu_11493` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11494` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11495` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11496` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11497` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11498` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11499` | `mcq` | false | `C` | `B` |
