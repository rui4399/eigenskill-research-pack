# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 192 / 500 | 0.3840 | 9.8724 | 0.187318 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_11000` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11001` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11002` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11003` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11004` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11005` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11006` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11007` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11008` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11009` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11010` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11011` | `mcq` | true | `A` | `A. Yes, because the seller breached the agreement by not following the procedure stated in the purchase agreement.` |
| baseline | `mmlu_11012` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11013` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11014` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11015` | `mcq` | false | `D` | `A. No, because the state procedure for protecting the woman's money until a judgment is entered is a fair one that compo` |
| baseline | `mmlu_11016` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11017` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11018` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11019` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11020` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11021` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11022` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11023` | `mcq` | true | `C` | `C. Yes, because the man and the woman were acting in concert in a dangerous activity.` |
| baseline | `mmlu_11024` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11025` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11026` | `mcq` | false | `A` | `C. No, because the paving requirement had to be placed in the deed to the married couple and it was not.` |
| baseline | `mmlu_11027` | `mcq` | true | `A` | `A. Deny the motion and submit the case to the jury with instructions that the custom is relevant but not conclusive on t` |
| baseline | `mmlu_11028` | `mcq` | false | `A` | `Reject the instruction, based on ex post facto.` |
| baseline | `mmlu_11029` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11030` | `mcq` | true | `C` | `C. not liable, because there was no assumption of the mortgage.` |
| baseline | `mmlu_11031` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11032` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11033` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11034` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11035` | `mcq` | false | `A` | `No, because the contractor breached his duty of good faith and fair dealing by supplying unsatisfactory materials.` |
| baseline | `mmlu_11036` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11037` | `mcq` | true | `D` | `D. Yes, because the defense has the burden of proving the defense of duress by a preponderance of the evidence.` |
| baseline | `mmlu_11038` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11039` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11040` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11041` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11042` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11043` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11044` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11045` | `mcq` | false | `A` | `No, because neither party objected to the findings.` |
| baseline | `mmlu_11046` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11047` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11048` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11049` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11050` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11051` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11052` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11053` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11054` | `mcq` | false | `D` | `B. win, because the clerk's conduct was extreme and outrageous.` |
| baseline | `mmlu_11055` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11056` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11057` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11058` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11059` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11060` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11061` | `mcq` | true | `A` | `A. No, because exigent circumstances justified the officers' entry.` |
| baseline | `mmlu_11062` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11063` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11064` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11065` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11066` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11067` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11068` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11069` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11070` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11071` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11072` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11073` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11074` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11075` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11076` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11077` | `mcq` | false | `C` | `No, because the stockbroker waived her claim for improper service of process by asserting it in her answer.` |
| baseline | `mmlu_11078` | `mcq` | false | `C` | `No, because the nonconformity does not materially alter the value of the posters to the sporting goods shop.` |
| baseline | `mmlu_11079` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11080` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11081` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11082` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11083` | `mcq` | false | `D` | `A. Yes, because by operation of law the woman is an equitable assignee of the builder's claim against the owner of the l` |
| baseline | `mmlu_11084` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11085` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11086` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11087` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11088` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11089` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11090` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11091` | `mcq` | false | `C` | `A. sustain the objection, as hearsay not within any recognized exception.` |
| baseline | `mmlu_11092` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11093` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11094` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11095` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11096` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11097` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11098` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11099` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11100` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11101` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11102` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11103` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11104` | `mcq` | true | `A` | `A. No, because the expansion is a disproportionate increase in product that exceeds contractual estimates and cannot be ` |
| baseline | `mmlu_11105` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11106` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11107` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11108` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11109` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11110` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11111` | `mcq` | false | `D` | `A. the bartender.` |
| baseline | `mmlu_11112` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11113` | `mcq` | true | `D` | `D. no crime.` |
| baseline | `mmlu_11114` | `mcq` | false | `B` | `C. No, because the coach's October 11 statement effectuated a waiver of any condition of timely delivery.` |
| baseline | `mmlu_11115` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11116` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11117` | `mcq` | false | `B` | `No, because the elevator stalled due to a manufacturing defect.` |
| baseline | `mmlu_11118` | `mcq` | false | `A` | `No, the court will order the adult child to resume paying on the mortgage and to obtain a loan to pay it off within a re` |
| baseline | `mmlu_11119` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11120` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11121` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11122` | `mcq` | true | `B` | `B. Yes, because the defect could have been discovered through the exercise of reasonable care by the bicycle company.` |
| baseline | `mmlu_11123` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11124` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11125` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11126` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11127` | `mcq` | false | `B` | `No, because an at-will employee has the right to terminate an employment contract.` |
| baseline | `mmlu_11128` | `mcq` | false | `D` | `C. Yes, because the auto dealer placed a defective car into the stream of commerce.` |
| baseline | `mmlu_11129` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11130` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11131` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11132` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11133` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11134` | `mcq` | true | `C` | `C. Yes, because in most circumstances an "unclaimed" notification is insufficient to satisfy the demands of due process.` |
| baseline | `mmlu_11135` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11136` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11137` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11138` | `mcq` | false | `C` | `No, because the stockbroker did not intend to harm anyone other than himself.` |
| baseline | `mmlu_11139` | `mcq` | true | `A` | `A. Yes, because he possessed the requisite intent.` |
| baseline | `mmlu_11140` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11141` | `mcq` | false | `B` | `A. attempted larceny.` |
| baseline | `mmlu_11142` | `mcq` | false | `C` | `No, because either the plaintiff or the defendant may block disclosure of statements made during such meetings.` |
| baseline | `mmlu_11143` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11144` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11145` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11146` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11147` | `mcq` | false | `A` | `No, because the appellate court lacks jurisdiction over the appeal.` |
| baseline | `mmlu_11148` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11149` | `mcq` | false | `C` | `No, because the three siblings took the farm as tenants in common rather than as joint tenants with right of survivorshi` |
| baseline | `mmlu_11150` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11151` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11152` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11153` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11154` | `mcq` | false | `D` | `No, because families with children are already living in units with balconies.` |
| baseline | `mmlu_11155` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11156` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11157` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11158` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11159` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11160` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11161` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11162` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11163` | `mcq` | true | `A` | `A. No, the parol evidence rule does not apply to preclude the testimony in cases such as this one where the testimony wo` |
| baseline | `mmlu_11164` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11165` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11166` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11167` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11168` | `mcq` | false | `A` | `C. No, because the builder waived its right to reject the nonconforming goods by not returning them promptly to the comp` |
| baseline | `mmlu_11169` | `mcq` | false | `A` | `No, because the entrepreneur waived the right to challenge subject-matter jurisdiction by not raising the issue initiall` |
| baseline | `mmlu_11170` | `mcq` | false | `B` | `A. No, because the prosecution seeks to punish the publication of lawfully obtained, truthful information about a matter` |
| baseline | `mmlu_11171` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11172` | `mcq` | true | `C` | `C. Yes, judicial fact-finding that increases the maximum sentence over what the jury's verdict allows is unconstitutiona` |
| baseline | `mmlu_11173` | `mcq` | true | `C` | `C. Yes, because Congress can determine that the transportation of stolen boats affects interstate commerce.` |
| baseline | `mmlu_11174` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11175` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11176` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11177` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11178` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11179` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11180` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11181` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11182` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11183` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11184` | `mcq` | true | `A` | `A. No, because the officers discovered the cocaine during a lawful protective sweep of the house looking for the man's a` |
| baseline | `mmlu_11185` | `mcq` | true | `C` | `C. the contract price of$10,000.` |
| baseline | `mmlu_11186` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11187` | `mcq` | false | `D` | `A. win, because the player's conduct was extreme and outrageous.` |
| baseline | `mmlu_11188` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11189` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11190` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11191` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11192` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11193` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11194` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11195` | `mcq` | false | `B` | `Conviction affirmed, because the modern trend of the law is to recognize criminal liability without mens rea or specific` |
| baseline | `mmlu_11196` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11197` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11198` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11199` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11200` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11201` | `mcq` | true | `D` | `D. not guilty.` |
| baseline | `mmlu_11202` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11203` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11204` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11205` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11206` | `mcq` | false | `A` | `No, because the landscaper could have obtained possession of the truck through legal action rather than by agreeing to t` |
| baseline | `mmlu_11207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11208` | `mcq` | false | `C` | `D. $4,000. 00` |
| baseline | `mmlu_11209` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11210` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11211` | `mcq` | true | `B` | `B. $10,000.00` |
| baseline | `mmlu_11212` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11213` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11214` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11215` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11216` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11217` | `mcq` | true | `A` | `A. No, it will preclude the lessee from making such drastic changes without the investor's consent.` |
| baseline | `mmlu_11218` | `mcq` | false | `A` | `B. The equal protection clause of the Fourteenth Amendment.` |
| baseline | `mmlu_11219` | `mcq` | false | `C` | `B. No, hearsay without an exception.` |
| baseline | `mmlu_11220` | `mcq` | true | `D` | `D. No contract exists.` |
| baseline | `mmlu_11221` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11222` | `mcq` | false | `B` | `No, because the court entered final judgment for Plaintiff before the motion to set aside the verdict was filed.` |
| baseline | `mmlu_11223` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11224` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11225` | `mcq` | true | `C` | `C. No, because the common law doctrine of negligence per se does not abrogate the defendant's right to apportion fault u` |
| baseline | `mmlu_11226` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11227` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11228` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11229` | `mcq` | false | `C` | `A. succeed, because his apprehension of the murderer created a contract implied in law.` |
| baseline | `mmlu_11230` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11231` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11232` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11233` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11234` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11235` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11236` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11237` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11238` | `mcq` | false | `B` | `D. Yes, she would be charged with negligent homicide because it was foreseeable that if she fell asleep for even just a ` |
| baseline | `mmlu_11239` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11240` | `mcq` | false | `A` | `denied, because the trier of fact may still infer liability for trespass.` |
| baseline | `mmlu_11241` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11242` | `mcq` | false | `A` | `C. Yes, because the host has the privilege of host immunity.` |
| baseline | `mmlu_11243` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11244` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11245` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11246` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11247` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11248` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11249` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11250` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11251` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11252` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11253` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11254` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11255` | `mcq` | true | `A` | `A. No, because the friend is not a named insured on the title insurance policy.` |
| baseline | `mmlu_11256` | `mcq` | true | `D` | `D. Yes, because the circumstances, including prior practice, showed intent to contract and a meeting of the minds.` |
| baseline | `mmlu_11257` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11258` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11259` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11260` | `mcq` | false | `C` | `B. The necessity for the enactment of this particular statute.` |
| baseline | `mmlu_11261` | `mcq` | false | `B` | `No, because a person has no right to privacy after their death.` |
| baseline | `mmlu_11262` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11263` | `mcq` | false | `B` | `A. not prevail, because the president was acting to protect a legitimate public interest.` |
| baseline | `mmlu_11264` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11265` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11266` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11267` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11268` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11269` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11270` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11271` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11272` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11273` | `mcq` | true | `A` | `A. No, because it is hearsay not within any exception.` |
| baseline | `mmlu_11274` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11275` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11276` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11277` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11278` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11279` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11280` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11281` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11282` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11283` | `mcq` | true | `B` | `B. It may be used to impeach him as a witness.` |
| baseline | `mmlu_11284` | `mcq` | false | `B` | `No, because the oral agreement is inconsistent with the terms of the written contract.` |
| baseline | `mmlu_11285` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11286` | `mcq` | true | `D` | `D. Yes, because the evidence was sufficient to support the jury's verdict.` |
| baseline | `mmlu_11287` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11288` | `mcq` | true | `B` | `B. Yes, because it retrospectively increases the punishment over what was in effect when the offense was committed.` |
| baseline | `mmlu_11289` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11290` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11291` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11292` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11293` | `mcq` | true | `C` | `C. not guilty, because the defendant did not intend to kill the woman.` |
| baseline | `mmlu_11294` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11295` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11297` | `mcq` | false | `C` | `D. I, II, and III.` |
| baseline | `mmlu_11298` | `mcq` | true | `A` | `A. granted, because the statement is hearsay not within any recognized exception.` |
| baseline | `mmlu_11299` | `mcq` | true | `A` | `A. No, the circumstances indicate that he understood that he could stop the questioning and get a lawyer but he did not ` |
| baseline | `mmlu_11300` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11301` | `mcq` | true | `C` | `C. a voidable promise as violative of the statute of frauds.` |
| baseline | `mmlu_11302` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11303` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11304` | `mcq` | false | `A` | `B. The landscaper.` |
| baseline | `mmlu_11305` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11306` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11307` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11308` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11309` | `mcq` | false | `A` | `D. no recovery.` |
| baseline | `mmlu_11310` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11311` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11312` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11313` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11314` | `mcq` | true | `D` | `D. No, criminal battery in this case is a general intent crime and the defense of voluntary intoxication is not availabl` |
| baseline | `mmlu_11315` | `mcq` | true | `C` | `C. No, the mother's deed was a nullity because the entireties estate can only be broken with the consent of both parties` |
| baseline | `mmlu_11316` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11317` | `mcq` | false | `A` | `No, because the act of purchasing the fish and taking it to the seller's facility with the criminal intent to color it i` |
| baseline | `mmlu_11318` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11319` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11320` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11321` | `mcq` | true | `B` | `B. No, unless the classmate acted unreasonably when she pushed the girl off the sled.` |
| baseline | `mmlu_11322` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11323` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11324` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11325` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11326` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11327` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11328` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11329` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11330` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11331` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11332` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11333` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11334` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11335` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11336` | `mcq` | false | `C` | `A. The owner, because the mother's assignment to the nursing home was void as violative of the anti-assignment clause.` |
| baseline | `mmlu_11337` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11338` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11339` | `mcq` | false | `C` | `D. Yes, because they owned the property due to paying the taxes on it.` |
| baseline | `mmlu_11340` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11341` | `mcq` | false | `B` | `D. Yes, because the defendant was denied both the right to counsel and the right to a jury trial.` |
| baseline | `mmlu_11342` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11343` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11344` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11345` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11346` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11347` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11348` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11349` | `mcq` | true | `A` | `A. Yes, because the furnishing of the indicia of authority to act to the employee was sufficient proof to bind the princ` |
| baseline | `mmlu_11350` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11351` | `mcq` | true | `A` | `A. No, because this is likely a strict liability law that does not provide for defenses based on mental state.` |
| baseline | `mmlu_11352` | `mcq` | false | `A` | `D. Yes, because the woman's offer and the neighbor's acceptance created an enforceable contract.` |
| baseline | `mmlu_11353` | `mcq` | false | `B` | `D. not admissible.` |
| baseline | `mmlu_11354` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11355` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11356` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11357` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11358` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11359` | `mcq` | false | `D` | `No, because the nature of the nephew's estate would not be altered by the wife's death.` |
| baseline | `mmlu_11360` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11361` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11362` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11363` | `mcq` | false | `A` | `No, because the booster's promise was made to the coach rather than to the university and, therefore, was not a charitab` |
| baseline | `mmlu_11364` | `mcq` | false | `C` | `D. $110,000. 00` |
| baseline | `mmlu_11365` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11366` | `mcq` | true | `B` | `B. by certiorari.` |
| baseline | `mmlu_11367` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11368` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11369` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11370` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11371` | `mcq` | false | `C` | `D. win, because mere non-use of an easement does not extinguish it.` |
| baseline | `mmlu_11372` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11373` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11374` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11375` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11376` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11377` | `mcq` | true | `B` | `B. Yes, because a qualified bank employee must first authenticate them in person or provide a certification in complianc` |
| baseline | `mmlu_11378` | `mcq` | false | `D` | `C. Yes, because the manufacturer's note failed to contain a signature.` |
| baseline | `mmlu_11379` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11380` | `mcq` | false | `D` | `No, because contributory negligence is not a defense to strict liability in a products liability case.` |
| baseline | `mmlu_11381` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11382` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11383` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11384` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11385` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11386` | `mcq` | false | `C` | `D. recover $15,000.` |
| baseline | `mmlu_11387` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11388` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11389` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11390` | `mcq` | false | `D` | `No, because a first-party negligent entrustment claim is generally allowed when the entrustor knows that he is loaning t` |
| baseline | `mmlu_11391` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11392` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11393` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11394` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11395` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11396` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11397` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11398` | `mcq` | true | `C` | `C. No, because a party always has a right to rescind a contract where the value of the product or services does not live` |
| baseline | `mmlu_11399` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11400` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11401` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11402` | `mcq` | false | `B` | `D. $25,000, or the commission equivalent of 5 percent on the sale of the property for $500,000, because all conditions p` |
| baseline | `mmlu_11403` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11404` | `mcq` | false | `A` | `C. The woman.` |
| baseline | `mmlu_11405` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11406` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11407` | `mcq` | true | `A` | `A. Yes, because willfulness clause requires proof of both knowledge of the law and a specific intent to commit the crime` |
| baseline | `mmlu_11408` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11409` | `mcq` | true | `D` | `D. Hearsay` |
| baseline | `mmlu_11410` | `mcq` | false | `A` | `D. win, because the assignment of future rights is enforceable.` |
| baseline | `mmlu_11411` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11412` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11413` | `mcq` | false | `D` | `C. Yes, and the plaintiff should be allowed the option of reading it into evidence or having the diary received as an ex` |
| baseline | `mmlu_11414` | `mcq` | false | `D` | `No, because the potential juror is presumed to be biased because of his relationship to the company.` |
| baseline | `mmlu_11415` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11416` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11417` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11418` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11419` | `mcq` | true | `D` | `D. Yes, as impeachment for prior inconsistency.` |
| baseline | `mmlu_11420` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11421` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11422` | `mcq` | false | `B` | `A. No crime.` |
| baseline | `mmlu_11423` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11424` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11425` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11426` | `mcq` | true | `B` | `B. Felony murder.` |
| baseline | `mmlu_11427` | `mcq` | false | `A` | `B. Yes, the fact that a person sees that action is needed for another's aid or protection does impose a legal duty to ac` |
| baseline | `mmlu_11428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11429` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11430` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11431` | `mcq` | true | `C` | `C. No, because the sign did not explain the danger and only told her that it was not available, and she therefore did no` |
| baseline | `mmlu_11432` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11433` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11434` | `mcq` | false | `D` | `B. $25,000. 00` |
| baseline | `mmlu_11435` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11436` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11437` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11438` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11439` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11440` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11441` | `mcq` | true | `A` | `A. Yes, because the renewal premium was placed in the mailbox before the date of expiration, and the notice did not say ` |
| baseline | `mmlu_11442` | `mcq` | false | `B` | `No, because whether the man's behavior was unduly risky is a question of fact for the jury to resolve.` |
| baseline | `mmlu_11443` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11444` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11445` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11446` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11447` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11448` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11449` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11450` | `mcq` | false | `A` | `C. No, the stop and the search were within the normal bounds of propriety for a speeding stop.` |
| baseline | `mmlu_11451` | `mcq` | true | `A` | `A. Yes, because this was entrapment in that the intent to commit the crime originated with the government.` |
| baseline | `mmlu_11452` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11453` | `mcq` | true | `B` | `B. No, because the designer did not have sufficiently clear notice that she must accept the licensing terms prior to dow` |
| baseline | `mmlu_11454` | `mcq` | true | `A` | `A. No, because the accumulation of factors all added up to reasonable suspicion for a stop and articulable suspicion for` |
| baseline | `mmlu_11455` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11456` | `mcq` | true | `B` | `B. As a cotenant in possession, the best friend retains the profits from his crops, and the uncle is entitled to a share` |
| baseline | `mmlu_11457` | `mcq` | false | `C` | `A. No, because it is impermissible character evidence.` |
| baseline | `mmlu_11458` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11459` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11460` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11461` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11462` | `mcq` | false | `B` | `D. No, because the sports fan cannot offer proof as to which of the men struck the sports fan over the head with the bot` |
| baseline | `mmlu_11463` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11464` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11465` | `mcq` | true | `B` | `B. The case presents a nonjusticiable political question.` |
| baseline | `mmlu_11466` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11467` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11468` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11469` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11470` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11471` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11472` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11473` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11474` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11475` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11476` | `mcq` | false | `A` | `C. No, because there is no evidence suggesting that the additional terms and conditions were incorporated into the origi` |
| baseline | `mmlu_11477` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11478` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11479` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11480` | `mcq` | false | `A` | `B. Four.` |
| baseline | `mmlu_11481` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11482` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11483` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11484` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11485` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11486` | `mcq` | false | `B` | `No, because the double jeopardy protection only prohibits a second prosecution following an acquittal for the same offen` |
| baseline | `mmlu_11487` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11488` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11489` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11490` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11491` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11492` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11493` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11494` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11495` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11496` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11497` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11498` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11499` | `mcq` | false | `C` | `B` |
