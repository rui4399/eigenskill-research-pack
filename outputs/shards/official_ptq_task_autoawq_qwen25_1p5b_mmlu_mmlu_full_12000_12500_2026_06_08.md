# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 280 / 500 | 0.5600 | 9.7487 | 0.150583 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_12000` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12001` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12002` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12003` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12004` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12005` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12006` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12007` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12008` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12009` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12010` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12011` | `mcq` | true | `C` | `C. both the heroin and the marijuana.` |
| baseline | `mmlu_12012` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12013` | `mcq` | false | `A` | `C. recover $55,000.` |
| baseline | `mmlu_12014` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12015` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12016` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12017` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12018` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12019` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12020` | `mcq` | false | `A` | `C. not guilty, because she returned the bracelet to the display tray.` |
| baseline | `mmlu_12021` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12022` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12023` | `mcq` | true | `C` | `C. penalty and forfeiture clause.` |
| baseline | `mmlu_12024` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12025` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12026` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12027` | `mcq` | false | `A` | `D. not proper, because character cannot be proved by generalities.` |
| baseline | `mmlu_12028` | `mcq` | true | `D` | `D. Yes, because the program knowingly made false factual representations that the customer relied on.` |
| baseline | `mmlu_12029` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12030` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12031` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12032` | `mcq` | false | `C` | `D. Yes, because the State A federal court lacked personal jurisdiction over the plumber as a State B citizen.` |
| baseline | `mmlu_12033` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12034` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12035` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12036` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12037` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12038` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12039` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12040` | `mcq` | false | `D` | `C. not succeed, because the resident's remarks were a matter of personal opinion rather than statements of fact.` |
| baseline | `mmlu_12041` | `mcq` | true | `C` | `C. Yes, because the fumigation company can be held strictly liable for its activity.` |
| baseline | `mmlu_12042` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12043` | `mcq` | false | `B` | `D. not recover, because the friend was only joking.` |
| baseline | `mmlu_12044` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12045` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12046` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12047` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12048` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12049` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12050` | `mcq` | true | `D` | `D. lose, because the washing machine was defective and unreasonably dangerous.` |
| baseline | `mmlu_12051` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12052` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12053` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12054` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12055` | `mcq` | false | `A` | `D. No sentence, because the defendant was denied the right to counsel.` |
| baseline | `mmlu_12056` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12057` | `mcq` | true | `C` | `C. not prevail, because the accountant could not reasonably have been expected to discover the defect.` |
| baseline | `mmlu_12058` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_12059` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12060` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12061` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12062` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12063` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12064` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12065` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12066` | `mcq` | true | `C` | `C. deny relief, because the picketing ordinancewas unconstitutional on its face.` |
| baseline | `mmlu_12067` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12068` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12069` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12070` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_12071` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12072` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12073` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12074` | `mcq` | false | `B` | `D. $10,000, the proportion of the pedestrian's damages caused by her own negligence, less the $10,000 in hospital expens` |
| baseline | `mmlu_12075` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12076` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12077` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12078` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12079` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12080` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12081` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12082` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12083` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12084` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12085` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12086` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12087` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12088` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12089` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12090` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12091` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12092` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12093` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12094` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12095` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12096` | `mcq` | false | `B` | `C. Yes, because the written instrument appears to be a complete integration of the parties' agreement.` |
| baseline | `mmlu_12097` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12098` | `mcq` | true | `B` | `B. Murder and voluntary manslaughter.` |
| baseline | `mmlu_12099` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12100` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12101` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12102` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12103` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12104` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12105` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12106` | `mcq` | false | `B` | `D. excluded, because her testimony is impermissible evidence of character to show defendant's plaintiff's conduct on a p` |
| baseline | `mmlu_12107` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12108` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12109` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12110` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12111` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12112` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12113` | `mcq` | false | `A` | `C. State law, because the judgment is being asserted in a state court.` |
| baseline | `mmlu_12114` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12115` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12116` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12117` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12118` | `mcq` | true | `D` | `D. Wait a reasonable time not to exceed 30 days; if adequate assurances are not received, cancel the contract, cover imm` |
| baseline | `mmlu_12119` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12120` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12121` | `mcq` | true | `D` | `D. Yes, because federal law governs transfers of venue, and it would be more convenient for the witnesses and parties to` |
| baseline | `mmlu_12122` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12123` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12124` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12125` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12126` | `mcq` | true | `D` | `D. not recover, because the gang member was unaware that the woman was watching.` |
| baseline | `mmlu_12127` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12128` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12129` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12130` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12131` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12132` | `mcq` | false | `B` | `C. denied, because the verdicts do not amount to a reversible error.` |
| baseline | `mmlu_12133` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12134` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12135` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12136` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12137` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12138` | `mcq` | true | `C` | `C. Yes, because the manufacturer sold a product with a dangerous defect.` |
| baseline | `mmlu_12139` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12140` | `mcq` | true | `C` | `C. not prevail, unless he is able to prove malice on the defendant's part.` |
| baseline | `mmlu_12141` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12142` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12143` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12144` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12145` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12146` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12147` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12148` | `mcq` | true | `C` | `C. The court's negligence instruction was plain error that affected the worker's substantial rights.` |
| baseline | `mmlu_12149` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12150` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12151` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12152` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12153` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12154` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12155` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12156` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12157` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12158` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12159` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12160` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12161` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12162` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12163` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12164` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12165` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12166` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12167` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12168` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12169` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12170` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12171` | `mcq` | true | `B` | `B. Assess for suicidal ideation` |
| baseline | `mmlu_12172` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12173` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12174` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12175` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12176` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12177` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12178` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12179` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12180` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12181` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12182` | `mcq` | true | `B` | `B. Polymerase chain reaction` |
| baseline | `mmlu_12183` | `mcq` | false | `D` | `C. Intubation` |
| baseline | `mmlu_12184` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12185` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12186` | `mcq` | true | `D` | `D. Endometrial biopsy` |
| baseline | `mmlu_12187` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12188` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12189` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12190` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12191` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12192` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12193` | `mcq` | false | `B` | `C. Order a test for HIV antibody` |
| baseline | `mmlu_12194` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12195` | `mcq` | true | `B` | `B. Explain that the patient does not need the MRI and that it is not appropriate to misrepresent her examination finding` |
| baseline | `mmlu_12196` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12197` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12198` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12199` | `mcq` | false | `B` | `C. Place a percutaneous endoscopic gastrostomy (PEG) tube` |
| baseline | `mmlu_12200` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12201` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12202` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12203` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12204` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12205` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12206` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12207` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12208` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12209` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12210` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12211` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12212` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12213` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12214` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12215` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12216` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12217` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12218` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12219` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12220` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12221` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12222` | `mcq` | true | `D` | `D. Vancomycin` |
| baseline | `mmlu_12223` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12224` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12225` | `mcq` | true | `B` | `B. Adjusting her medication regimen` |
| baseline | `mmlu_12226` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12227` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12228` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12229` | `mcq` | false | `B` | `D. Presence of an S3` |
| baseline | `mmlu_12230` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12231` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12232` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12233` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12234` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12235` | `mcq` | true | `D` | `D. Pericardiocentesis` |
| baseline | `mmlu_12236` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12237` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12238` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12239` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12240` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12241` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12242` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12243` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12244` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12245` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12246` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12247` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12248` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12249` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12250` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12251` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12252` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12253` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12254` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12255` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12256` | `mcq` | true | `D` | `D. 90%` |
| baseline | `mmlu_12257` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12258` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12259` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12260` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12261` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12262` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12263` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12264` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12265` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12266` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12267` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12268` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12269` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12270` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12271` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12272` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12273` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12274` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12275` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12276` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12277` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12278` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12279` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12280` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12281` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12282` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12283` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12284` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12285` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12286` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12287` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12288` | `mcq` | true | `D` | `D. PCP (phencyclidine)` |
| baseline | `mmlu_12289` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12290` | `mcq` | true | `D` | `D. No treatment is needed at this time` |
| baseline | `mmlu_12291` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12292` | `mcq` | true | `D` | `D. He cannot date her because she was once his psychiatric patient.` |
| baseline | `mmlu_12293` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12294` | `mcq` | false | `D` | `B. Order MRI of the lumbosacral spine` |
| baseline | `mmlu_12295` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12296` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12297` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12298` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12299` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12300` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12301` | `mcq` | true | `D` | `D. Neck stiffness` |
| baseline | `mmlu_12302` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12303` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12304` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12305` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12306` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12307` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12308` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12309` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12310` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12311` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12312` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12313` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12314` | `mcq` | false | `D` | `C. His wife` |
| baseline | `mmlu_12315` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12316` | `mcq` | false | `B` | `D. MRI of the spine` |
| baseline | `mmlu_12317` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12318` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12319` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12320` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12321` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12322` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12323` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12324` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12325` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12326` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12327` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12328` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12329` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12330` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12331` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12332` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12333` | `mcq` | true | `D` | `D. Metabolism` |
| baseline | `mmlu_12334` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12335` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12336` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12337` | `mcq` | false | `C` | `A. 0%` |
| baseline | `mmlu_12338` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12339` | `mcq` | true | `B` | `B. Echocardiography` |
| baseline | `mmlu_12340` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12341` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12342` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12343` | `mcq` | false | `B` | `A. Admit the patient to the hospital` |
| baseline | `mmlu_12344` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12345` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12346` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12347` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12348` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12349` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12350` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12351` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12352` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12353` | `mcq` | true | `D` | `D. Vascular dementia` |
| baseline | `mmlu_12354` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12355` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12356` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12357` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12358` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12359` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12360` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12361` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12362` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12363` | `mcq` | true | `D` | `D. Order a transthoracic echocardiography` |
| baseline | `mmlu_12364` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12365` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12366` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12367` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12368` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12369` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12370` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12371` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12372` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12373` | `mcq` | true | `D` | `D. Left tube thoracostomy` |
| baseline | `mmlu_12374` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12375` | `mcq` | true | `D` | `D. Subarachnoid hemorrhage` |
| baseline | `mmlu_12376` | `mcq` | true | `B` | `B. It is a polymorphism` |
| baseline | `mmlu_12377` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12378` | `mcq` | true | `D` | `D. Refer the patient to a child psychiatrist` |
| baseline | `mmlu_12379` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12380` | `mcq` | true | `D` | `D. The patient is at no increased risk` |
| baseline | `mmlu_12381` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12382` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12383` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12384` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12385` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_12386` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12387` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12388` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12389` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12390` | `mcq` | true | `D` | `D. vanillylmandelic acid` |
| baseline | `mmlu_12391` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12392` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12393` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12394` | `mcq` | false | `D` | `B. CT scan of the chest` |
| baseline | `mmlu_12395` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12396` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12397` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12398` | `mcq` | true | `C` | `C. Administer intravenous fluids` |
| baseline | `mmlu_12399` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12400` | `mcq` | false | `A` | `B. Psychiatric consultation` |
| baseline | `mmlu_12401` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12402` | `mcq` | true | `D` | `D. Echocardiography` |
| baseline | `mmlu_12403` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12404` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12405` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12406` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12407` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12408` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12409` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12410` | `mcq` | true | `D` | `D. Help the mother deal with her anger and educate her regarding the potential benefit to her son and others if the fath` |
| baseline | `mmlu_12411` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12412` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12413` | `mcq` | false | `D` | `B. Epinephrine` |
| baseline | `mmlu_12414` | `mcq` | false | `A` | `B. Await contact with the caregiver before proceeding with management` |
| baseline | `mmlu_12415` | `mcq` | false | `A` | `B. Maintain the morphine, but periodically administer intravenous naloxone` |
| baseline | `mmlu_12416` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12417` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12418` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12419` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12420` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12421` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12422` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12423` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12424` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12425` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12426` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12427` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12428` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12429` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12430` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12431` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12432` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12433` | `mcq` | true | `B` | `B. Alcohol withdrawal` |
| baseline | `mmlu_12434` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12435` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12436` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12437` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12438` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12439` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12440` | `mcq` | true | `B` | `B. A teratogen` |
| baseline | `mmlu_12441` | `mcq` | true | `A` | `A. needs analysis.` |
| baseline | `mmlu_12442` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12443` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12444` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12445` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12446` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12447` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12448` | `mcq` | true | `D` | `D. production of speech` |
| baseline | `mmlu_12449` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12450` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12451` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12452` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12453` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12454` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12455` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12456` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12457` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12458` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12459` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12460` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12461` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12462` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12463` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12464` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12465` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12466` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12467` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12468` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12469` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12470` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_12471` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12472` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12473` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12474` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12475` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12476` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12477` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12478` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12479` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12481` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12482` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12483` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12484` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12485` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12486` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12487` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12488` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12489` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12490` | `mcq` | true | `C` | `C. Relatively malleable` |
| baseline | `mmlu_12491` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12492` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12493` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12494` | `mcq` | true | `D` | `D. Functional abilities` |
| baseline | `mmlu_12495` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12496` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12497` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12498` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12499` | `mcq` | true | `B` | `B` |
