# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 297 / 500 | 0.5940 | 5.1598 | 0.387930 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_12000` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12001` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12002` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12003` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12004` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12005` | `mcq` | false | `A` | `C. No, because the city did not discriminate against anyone's waste, if it was in the city limits the state from where t` |
| baseline | `mmlu_12006` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12007` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12008` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12009` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12010` | `mcq` | true | `B` | `B. The Federal Rules of Evidence allow the admission of hearsay statements that were made for the purpose of medical dia` |
| baseline | `mmlu_12011` | `mcq` | true | `C` | `C. both the heroin and the marijuana.` |
| baseline | `mmlu_12012` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12013` | `mcq` | false | `A` | `D. recover $35,000.` |
| baseline | `mmlu_12014` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12015` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12016` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12017` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12018` | `mcq` | false | `A` | `C. No, unless the tenant paid or tendered to the landlord the one-dollar consideration.` |
| baseline | `mmlu_12019` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12020` | `mcq` | false | `A` | `C. not guilty, because she returned the bracelet to the display tray.` |
| baseline | `mmlu_12021` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12022` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12023` | `mcq` | true | `C` | `C. penalty and forfeiture clause.` |
| baseline | `mmlu_12024` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12025` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12026` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12027` | `mcq` | false | `A` | `D. not proper, because character cannot be proved by generalities.` |
| baseline | `mmlu_12028` | `mcq` | true | `D` | `D. Yes, because the program knowingly made false factual representations that the customer relied on.` |
| baseline | `mmlu_12029` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12030` | `mcq` | false | `B` | `D. deny relief, because a pre-primary election is not within the scope of federal election control.` |
| baseline | `mmlu_12031` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12032` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12033` | `mcq` | true | `A` | `A. The evidence is admissible, to show that the written agreement did not become a contract.` |
| baseline | `mmlu_12034` | `mcq` | true | `D` | `D. Although the business owner may continue to use the right-of-way, the office workers would be enjoined from making su` |
| baseline | `mmlu_12035` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12036` | `mcq` | false | `C` | `D. No, because the holder of an easement is not entitled to compensation when the servient tenement is extinguished by c` |
| baseline | `mmlu_12037` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12038` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12039` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12040` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12041` | `mcq` | true | `C` | `C. Yes, because the fumigation company can be held strictly liable for its activity.` |
| baseline | `mmlu_12042` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12043` | `mcq` | false | `B` | `D. not recover, because the friend was only joking.` |
| baseline | `mmlu_12044` | `mcq` | true | `A` | `A. Yes, under the due process clause no compelling state interest justifies denying same-sex couples the fundamental rig` |
| baseline | `mmlu_12045` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12046` | `mcq` | true | `A` | `A. Murder.` |
| baseline | `mmlu_12047` | `mcq` | false | `C` | `A. prevail, because the graduate's conduct was extreme and outrageous.` |
| baseline | `mmlu_12048` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12049` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12050` | `mcq` | true | `D` | `D. lose, because the washing machine was defective and unreasonably dangerous.` |
| baseline | `mmlu_12051` | `mcq` | true | `D` | `D. The contract is enforceable with reasonable price being fixed at time of delivery.` |
| baseline | `mmlu_12052` | `mcq` | true | `A` | `A. The referendum procedure as a basic instrument of the democratic process does not violate the due process clause of t` |
| baseline | `mmlu_12053` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12054` | `mcq` | false | `C` | `A. The student's suspension deprived him of liberty and property without due process, as guaranteed by the Fourteenth Am` |
| baseline | `mmlu_12055` | `mcq` | false | `A` | `D. No sentence, because the defendant was denied the right to counsel.` |
| baseline | `mmlu_12056` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12057` | `mcq` | true | `C` | `C. not prevail, because the accountant could not reasonably have been expected to discover the defect.` |
| baseline | `mmlu_12058` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12059` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12060` | `mcq` | false | `C` | `A. admissible as an admission.` |
| baseline | `mmlu_12061` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12062` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12063` | `mcq` | false | `A` | `B. win, because the statutory period for adverse possession does not run against a remainder-man until his interest beco` |
| baseline | `mmlu_12064` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12065` | `mcq` | true | `D` | `D. No, because when the first cousin died the second cousin became the sole owner due to the right of survivorship, as p` |
| baseline | `mmlu_12066` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12067` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12068` | `mcq` | false | `C` | `A. Yes, because a revocation of an offer requires explicit words of rejection in order to be enforced.` |
| baseline | `mmlu_12069` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12070` | `mcq` | true | `A` | `A. Yes, because the dealer withheld material information intentionally and knowingly misrepresented the condition of the` |
| baseline | `mmlu_12071` | `mcq` | true | `A` | `A. Yes, because this is an objectionable question based on pure speculation.` |
| baseline | `mmlu_12072` | `mcq` | false | `D` | `B. Yes, as a statement against the interests of the other defendants.` |
| baseline | `mmlu_12073` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12074` | `mcq` | false | `B` | `D. $10,000, the proportion of the pedestrian's damages caused by her own negligence, less the $10,000 in hospital expens` |
| baseline | `mmlu_12075` | `mcq` | true | `D` | `D. There is no remedy.` |
| baseline | `mmlu_12076` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12077` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12078` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12079` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12080` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12081` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12082` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12083` | `mcq` | true | `C` | `C. he did not have the requisite intent at the time of the breaking and entering.` |
| baseline | `mmlu_12084` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12085` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12086` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12087` | `mcq` | true | `A` | `A. Yes, because the purchaser did not make a timely application and lost the protection of the contingency clause.` |
| baseline | `mmlu_12088` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12089` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12090` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12091` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12092` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12093` | `mcq` | false | `C` | `D. not guilty, because she effectively withdrew from the criminal endeavor.` |
| baseline | `mmlu_12094` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12095` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12096` | `mcq` | false | `B` | `C. Yes, because the written instrument appears to be a complete integration of the parties' agreement.` |
| baseline | `mmlu_12097` | `mcq` | false | `D` | `A. No.` |
| baseline | `mmlu_12098` | `mcq` | true | `B` | `B. Murder and voluntary manslaughter.` |
| baseline | `mmlu_12099` | `mcq` | false | `B` | `D. The father, because the First Amendment does not include protection for vicious verbal assaults such as this.` |
| baseline | `mmlu_12100` | `mcq` | false | `D` | `A. Negligence and battery.` |
| baseline | `mmlu_12101` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12102` | `mcq` | true | `C` | `C. the daughter and the doctor as tenants in common, subject to the professor's life estate.` |
| baseline | `mmlu_12103` | `mcq` | false | `C` | `B. Not having been recorded, the condition cannot be enforced against the son.` |
| baseline | `mmlu_12104` | `mcq` | true | `C` | `C. not guilty, because the defendant did not make any threat of force.` |
| baseline | `mmlu_12105` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12106` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12107` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12108` | `mcq` | false | `C` | `B. he returned the jacket after discovering his mistake.` |
| baseline | `mmlu_12109` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12110` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12111` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12112` | `mcq` | false | `D` | `A. The First Amendment prohibits government interference with freedom of the press.` |
| baseline | `mmlu_12113` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12114` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12115` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12116` | `mcq` | true | `C` | `C. not prevail, unless the driver was driving negligently when the accident occurred.` |
| baseline | `mmlu_12117` | `mcq` | true | `C` | `C. No, because the collector made no false representations of fact.` |
| baseline | `mmlu_12118` | `mcq` | true | `D` | `D. Wait a reasonable time not to exceed 30 days; if adequate assurances are not received, cancel the contract, cover imm` |
| baseline | `mmlu_12119` | `mcq` | false | `A` | `C. The federal officer was way outside his scope of authority and he clearly cannot make an arrest outside of the confin` |
| baseline | `mmlu_12120` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12121` | `mcq` | true | `D` | `D. Yes, because federal law governs transfers of venue, and it would be more convenient for the witnesses and parties to` |
| baseline | `mmlu_12122` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12123` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12124` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12125` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12126` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12127` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12128` | `mcq` | true | `C` | `C. not guilty, because the defendant did not intend to cause physical injury to the senior partner.` |
| baseline | `mmlu_12129` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12130` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12131` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12132` | `mcq` | false | `B` | `C. denied, because the verdicts do not amount to a reversible error.` |
| baseline | `mmlu_12133` | `mcq` | true | `B` | `B. Because the charge constitutes a lien, there is no personal obligation on the landscaper's part.` |
| baseline | `mmlu_12134` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12135` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12136` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12137` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12138` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12139` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12140` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12141` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12142` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12143` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12144` | `mcq` | false | `A` | `D. Yes, because due process precludes requiring a criminal defendant to bear the burden on an issue that would make an a` |
| baseline | `mmlu_12145` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12146` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12147` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12148` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12149` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12150` | `mcq` | true | `C` | `C. No, there was no police misconduct or overreaching, and as a result the confession is voluntary.` |
| baseline | `mmlu_12151` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12152` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12153` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12154` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12155` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12156` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12157` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12158` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12159` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12160` | `mcq` | true | `B` | `B. He has been unjustly enriched and he owes her restitution under a quasi-contractual legal theory.` |
| baseline | `mmlu_12161` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12162` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12163` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12164` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12165` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12166` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12167` | `mcq` | false | `B` | `A. The findings are clinically and statistically significant` |
| baseline | `mmlu_12168` | `mcq` | false | `C` | `B. Cor pulmonale` |
| baseline | `mmlu_12169` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12170` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12171` | `mcq` | true | `B` | `B. Assess for suicidal ideation` |
| baseline | `mmlu_12172` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12173` | `mcq` | false | `D` | `A. Inferior deep cervical` |
| baseline | `mmlu_12174` | `mcq` | true | `B` | `B. Na+ –Cl− symport inhibitor` |
| baseline | `mmlu_12175` | `mcq` | true | `D` | `D. Determination of serum digoxin level` |
| baseline | `mmlu_12176` | `mcq` | true | `D` | `D. Erythromycin` |
| baseline | `mmlu_12177` | `mcq` | false | `D` | `B. Frontal sinus` |
| baseline | `mmlu_12178` | `mcq` | true | `D` | `D. supraspinatus` |
| baseline | `mmlu_12179` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12180` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12181` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12182` | `mcq` | true | `B` | `B. Polymerase chain reaction` |
| baseline | `mmlu_12183` | `mcq` | false | `D` | `C. Intubation` |
| baseline | `mmlu_12184` | `mcq` | true | `C` | `C. Escherichia coli` |
| baseline | `mmlu_12185` | `mcq` | false | `D` | `C. Pelvic ultrasonography` |
| baseline | `mmlu_12186` | `mcq` | true | `D` | `D. Endometrial biopsy` |
| baseline | `mmlu_12187` | `mcq` | true | `A` | `A. Adopt` |
| baseline | `mmlu_12188` | `mcq` | true | `B` | `B. CT scan of the head` |
| baseline | `mmlu_12189` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12190` | `mcq` | false | `A` | `D. Postnasal drip syndrome` |
| baseline | `mmlu_12191` | `mcq` | false | `D` | `C. Stromelysin` |
| baseline | `mmlu_12192` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12193` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12194` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12195` | `mcq` | true | `B` | `B. Explain that the patient does not need the MRI and that it is not appropriate to misrepresent her examination finding` |
| baseline | `mmlu_12196` | `mcq` | false | `B` | `A. Intramural (pre-prostatic)` |
| baseline | `mmlu_12197` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12198` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12199` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12200` | `mcq` | true | `D` | `D. Non-small cell lung carcinoma` |
| baseline | `mmlu_12201` | `mcq` | true | `A` | `A. Ductography` |
| baseline | `mmlu_12202` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12203` | `mcq` | true | `C` | `C. Glycogenolysis in the liver` |
| baseline | `mmlu_12204` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12205` | `mcq` | true | `C` | `C. Sertoli-Leydig tumor` |
| baseline | `mmlu_12206` | `mcq` | true | `B` | `B. aortic stenosis` |
| baseline | `mmlu_12207` | `mcq` | true | `A` | `A. Amputation` |
| baseline | `mmlu_12208` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12209` | `mcq` | false | `D` | `B. Increased hydrostatic pressure` |
| baseline | `mmlu_12210` | `mcq` | true | `D` | `D. Influenza virus vaccine` |
| baseline | `mmlu_12211` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12212` | `mcq` | false | `D` | `A. Decreased filtration coefficient (Kf)` |
| baseline | `mmlu_12213` | `mcq` | false | `C` | `D. Formation of antibodies to RhD` |
| baseline | `mmlu_12214` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12215` | `mcq` | false | `D` | `A. Digoxin` |
| baseline | `mmlu_12216` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12217` | `mcq` | false | `C` | `D. Randomized clinical trial` |
| baseline | `mmlu_12218` | `mcq` | false | `D` | `C. Metoprolol` |
| baseline | `mmlu_12219` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12220` | `mcq` | true | `C` | `C. Relieve the physician of duty and alert the hospital's patient safety officer` |
| baseline | `mmlu_12221` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12222` | `mcq` | true | `D` | `D. Vancomycin` |
| baseline | `mmlu_12223` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12224` | `mcq` | true | `C` | `C. Herniorrhaphy should be scheduled at the earliest convenient time` |
| baseline | `mmlu_12225` | `mcq` | true | `B` | `B. Adjusting her medication regimen` |
| baseline | `mmlu_12226` | `mcq` | false | `B` | `C. Hypothyroidism` |
| baseline | `mmlu_12227` | `mcq` | true | `D` | `D. Trinucleotide repeat expansion` |
| baseline | `mmlu_12228` | `mcq` | false | `C` | `A. Arterial blood gas analysis` |
| baseline | `mmlu_12229` | `mcq` | true | `B` | `B. P2 louder than A2` |
| baseline | `mmlu_12230` | `mcq` | true | `A` | `A. Amniotic fluid embolism` |
| baseline | `mmlu_12231` | `mcq` | false | `C` | `B. Bronchoscopy` |
| baseline | `mmlu_12232` | `mcq` | true | `D` | `D. Preterm labor and delivery` |
| baseline | `mmlu_12233` | `mcq` | true | `D` | `D. Tumor necrosis factor α` |
| baseline | `mmlu_12234` | `mcq` | true | `B` | `B. fibromyalgia` |
| baseline | `mmlu_12235` | `mcq` | true | `D` | `D. Pericardiocentesis` |
| baseline | `mmlu_12236` | `mcq` | true | `B` | `B. anterior rami of T6-T10` |
| baseline | `mmlu_12237` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12238` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12239` | `mcq` | false | `D` | `C. Remove the patient from the ventilator and ventilate him with a bag-valve mask` |
| baseline | `mmlu_12240` | `mcq` | true | `A` | `A. Diffuse interstitial fibrosis` |
| baseline | `mmlu_12241` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12242` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12243` | `mcq` | false | `D` | `B. Number of men with test results greater than 5 ng/mL and a normal biopsy specimen` |
| baseline | `mmlu_12244` | `mcq` | true | `D` | `D. Splitting` |
| baseline | `mmlu_12245` | `mcq` | true | `D` | `D. Paroxetine` |
| baseline | `mmlu_12246` | `mcq` | true | `B` | `B. Decreased macrophage activity` |
| baseline | `mmlu_12247` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12248` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12249` | `mcq` | true | `A` | `A. Antigenic variation` |
| baseline | `mmlu_12250` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12251` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12252` | `mcq` | true | `D` | `D. Herpes zoster` |
| baseline | `mmlu_12253` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12254` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12255` | `mcq` | true | `B` | `B. Mucosal edema` |
| baseline | `mmlu_12256` | `mcq` | false | `D` | `C. 40%` |
| baseline | `mmlu_12257` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12258` | `mcq` | true | `D` | `D. Increased serum bradykinin concentrations` |
| baseline | `mmlu_12259` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12260` | `mcq` | false | `D` | `B. Doppler ultrasonography of the left lower extremity` |
| baseline | `mmlu_12261` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12262` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12263` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12264` | `mcq` | true | `C` | `C. Polysomnography` |
| baseline | `mmlu_12265` | `mcq` | true | `B` | `B. Aortic dissection` |
| baseline | `mmlu_12266` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12267` | `mcq` | true | `C` | `C. Optic nerve` |
| baseline | `mmlu_12268` | `mcq` | true | `D` | `D. Intramuscular ceftriaxone and oral doxycycline` |
| baseline | `mmlu_12269` | `mcq` | false | `C` | `A. Lesser peritoneal cavity` |
| baseline | `mmlu_12270` | `mcq` | true | `C` | `C. Smoking cessation program` |
| baseline | `mmlu_12271` | `mcq` | true | `D` | `D. Stage of disease` |
| baseline | `mmlu_12272` | `mcq` | true | `B` | `B. diffuse enlargement of the rectus muscles` |
| baseline | `mmlu_12273` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12274` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12275` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12276` | `mcq` | true | `C` | `C. Polymyositis` |
| baseline | `mmlu_12277` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12278` | `mcq` | true | `A` | `A. Frequent turning` |
| baseline | `mmlu_12279` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12280` | `mcq` | false | `D` | `C. complete blood count` |
| baseline | `mmlu_12281` | `mcq` | false | `B` | `C. Deviation of the tongue to the left side` |
| baseline | `mmlu_12282` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12283` | `mcq` | true | `C` | `C. Branch of the thyrocervical trunk` |
| baseline | `mmlu_12284` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12285` | `mcq` | false | `C` | `B. Seek a court order to appoint a legal guardian` |
| baseline | `mmlu_12286` | `mcq` | true | `A` | `A. Adenovirus` |
| baseline | `mmlu_12287` | `mcq` | false | `C` | `B. Begin intravenous vasopressin therapy` |
| baseline | `mmlu_12288` | `mcq` | true | `D` | `D. PCP (phencyclidine)` |
| baseline | `mmlu_12289` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12290` | `mcq` | true | `D` | `D. No treatment is needed at this time` |
| baseline | `mmlu_12291` | `mcq` | true | `D` | `D. Third-degree atrioventricular block` |
| baseline | `mmlu_12292` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12293` | `mcq` | false | `A` | `C. Generalized anxiety disorder` |
| baseline | `mmlu_12294` | `mcq` | false | `D` | `B. Order MRI of the lumbosacral spine` |
| baseline | `mmlu_12295` | `mcq` | false | `D` | `A. Color, caliber, and frequency of bowel movements` |
| baseline | `mmlu_12296` | `mcq` | true | `A` | `A. Adhere to the patient's wishes and discuss home-care options` |
| baseline | `mmlu_12297` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12298` | `mcq` | false | `D` | `B. administer tocolytic therapy` |
| baseline | `mmlu_12299` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_12300` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12301` | `mcq` | true | `D` | `D. Neck stiffness` |
| baseline | `mmlu_12302` | `mcq` | true | `A` | `A. Acting out` |
| baseline | `mmlu_12303` | `mcq` | true | `D` | `D. Cryotherapy` |
| baseline | `mmlu_12304` | `mcq` | true | `C` | `C. Hypovolemic` |
| baseline | `mmlu_12305` | `mcq` | true | `B` | `B. Influenza` |
| baseline | `mmlu_12306` | `mcq` | false | `A` | `D. Serine kinase` |
| baseline | `mmlu_12307` | `mcq` | false | `D` | `B. feeding through a nasogastric feeding tube` |
| baseline | `mmlu_12308` | `mcq` | true | `D` | `D. Measurement of serum insulin and C-peptide concentrations` |
| baseline | `mmlu_12309` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12310` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12311` | `mcq` | false | `B` | `A. high velocity, low amplitude` |
| baseline | `mmlu_12312` | `mcq` | true | `C` | `C. Filgrastim` |
| baseline | `mmlu_12313` | `mcq` | true | `D` | `D. Microscopic examination of the stool` |
| baseline | `mmlu_12314` | `mcq` | false | `D` | `C. His wife` |
| baseline | `mmlu_12315` | `mcq` | true | `D` | `D. Normal development` |
| baseline | `mmlu_12316` | `mcq` | false | `B` | `D. MRI of the spine` |
| baseline | `mmlu_12317` | `mcq` | false | `A` | `C. Laparoscopy` |
| baseline | `mmlu_12318` | `mcq` | true | `D` | `D. Systemic sclerosis (scleroderma)` |
| baseline | `mmlu_12319` | `mcq` | true | `B` | `B. Fine-needle aspiration of the nodule` |
| baseline | `mmlu_12320` | `mcq` | false | `D` | `A. allergy to eggs` |
| baseline | `mmlu_12321` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12322` | `mcq` | false | `B` | `A. Chance of a type I error` |
| baseline | `mmlu_12323` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12324` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12325` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12326` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12328` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12329` | `mcq` | false | `D` | `C. Myocardium` |
| baseline | `mmlu_12330` | `mcq` | false | `D` | `B. Dermis` |
| baseline | `mmlu_12331` | `mcq` | true | `D` | `D. surgical repair` |
| baseline | `mmlu_12332` | `mcq` | false | `D` | `B. Double-stranded nucleic acid genome` |
| baseline | `mmlu_12333` | `mcq` | true | `D` | `D. Metabolism` |
| baseline | `mmlu_12334` | `mcq` | false | `B` | `D. M` |
| baseline | `mmlu_12335` | `mcq` | true | `B` | `B. Cholinesterase inhibitor` |
| baseline | `mmlu_12336` | `mcq` | true | `C` | `C. Pulmonary hypoplasia` |
| baseline | `mmlu_12337` | `mcq` | false | `C` | `A. 0%` |
| baseline | `mmlu_12338` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12339` | `mcq` | false | `B` | `A. Skeletal survey` |
| baseline | `mmlu_12340` | `mcq` | true | `A` | `A. Abdominal ultrasonography of the right upper quadrant` |
| baseline | `mmlu_12341` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12342` | `mcq` | true | `D` | `D. pilonidal abscess` |
| baseline | `mmlu_12343` | `mcq` | false | `B` | `A. Admit the patient to the hospital` |
| baseline | `mmlu_12344` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12345` | `mcq` | true | `D` | `D. Laparotomy` |
| baseline | `mmlu_12346` | `mcq` | true | `D` | `D. Polycystic ovarian syndrome` |
| baseline | `mmlu_12347` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12348` | `mcq` | true | `B` | `B. BK virus` |
| baseline | `mmlu_12349` | `mcq` | false | `D` | `A. Internal iliac` |
| baseline | `mmlu_12350` | `mcq` | true | `C` | `C. Minimize ascertainment bias` |
| baseline | `mmlu_12351` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12352` | `mcq` | false | `B` | `D. Metronidazole` |
| baseline | `mmlu_12353` | `mcq` | true | `D` | `D. Vascular dementia` |
| baseline | `mmlu_12354` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12355` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12356` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12357` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12358` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12359` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12360` | `mcq` | true | `D` | `D. surgical evaluation` |
| baseline | `mmlu_12361` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12362` | `mcq` | true | `A` | `A. Decreasing myocardial contractility` |
| baseline | `mmlu_12363` | `mcq` | true | `D` | `D. Order a transthoracic echocardiography` |
| baseline | `mmlu_12364` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12365` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12366` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12367` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12368` | `mcq` | true | `D` | `D. Arthrocentesis` |
| baseline | `mmlu_12369` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12370` | `mcq` | true | `C` | `C. contact child protective services` |
| baseline | `mmlu_12371` | `mcq` | false | `D` | `C. Begin amphotericin therapy` |
| baseline | `mmlu_12372` | `mcq` | false | `D` | `A. Pulse pressure` |
| baseline | `mmlu_12373` | `mcq` | true | `D` | `D. Left tube thoracostomy` |
| baseline | `mmlu_12374` | `mcq` | true | `D` | `D. Mitral stenosis complicated by atrial fibrillation` |
| baseline | `mmlu_12375` | `mcq` | true | `D` | `D. Subarachnoid hemorrhage` |
| baseline | `mmlu_12376` | `mcq` | true | `B` | `B. It is a polymorphism` |
| baseline | `mmlu_12377` | `mcq` | true | `D` | `D. Somatic symptom disorder` |
| baseline | `mmlu_12378` | `mcq` | true | `D` | `D. Refer the patient to a child psychiatrist` |
| baseline | `mmlu_12379` | `mcq` | true | `A` | `A. Karyotype from peripheral leukocytes` |
| baseline | `mmlu_12380` | `mcq` | true | `D` | `D. The patient is at no increased risk` |
| baseline | `mmlu_12381` | `mcq` | true | `D` | `D. referral for an upper endoscopy with biopsy` |
| baseline | `mmlu_12382` | `mcq` | true | `D` | `D. Increased peripheral vascular resistance` |
| baseline | `mmlu_12383` | `mcq` | true | `A` | `A. Amygdala` |
| baseline | `mmlu_12384` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12385` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12386` | `mcq` | false | `D` | `C. Proteasomal degradation` |
| baseline | `mmlu_12387` | `mcq` | true | `D` | `D. Clindamycin` |
| baseline | `mmlu_12388` | `mcq` | true | `D` | `D. Meniere's disease` |
| baseline | `mmlu_12389` | `mcq` | false | `A` | `B. Intravenous methylprednisolone therapy` |
| baseline | `mmlu_12390` | `mcq` | true | `D` | `D. vanillylmandelic acid` |
| baseline | `mmlu_12391` | `mcq` | false | `B` | `C. Foramen rotundum` |
| baseline | `mmlu_12392` | `mcq` | true | `C` | `C. Nystatin` |
| baseline | `mmlu_12393` | `mcq` | false | `A` | `D. Supraspinatus` |
| baseline | `mmlu_12394` | `mcq` | true | `D` | `D. Bone marrow aspiration` |
| baseline | `mmlu_12395` | `mcq` | false | `D` | `A. Administer the meningococcal vaccine` |
| baseline | `mmlu_12396` | `mcq` | true | `B` | `B. Increased intensity of the murmur with deep inspiration` |
| baseline | `mmlu_12397` | `mcq` | true | `D` | `D. Initiation of a daily corticosteroid inhaler` |
| baseline | `mmlu_12398` | `mcq` | true | `C` | `C. Administer intravenous fluids` |
| baseline | `mmlu_12399` | `mcq` | true | `A` | `A. Avoids the concern for reversion to virulence` |
| baseline | `mmlu_12400` | `mcq` | false | `A` | `D. Transfer to a burn center` |
| baseline | `mmlu_12401` | `mcq` | true | `C` | `C. Bipolar disorder` |
| baseline | `mmlu_12402` | `mcq` | true | `D` | `D. Echocardiography` |
| baseline | `mmlu_12403` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12404` | `mcq` | false | `D` | `A. Epigastric artery` |
| baseline | `mmlu_12405` | `mcq` | false | `D` | `B. The patient is a CFTR obligate carrier` |
| baseline | `mmlu_12406` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12407` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12408` | `mcq` | true | `D` | `D. Subcutaneous enoxaparin` |
| baseline | `mmlu_12409` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12410` | `mcq` | false | `D` | `A. Attempt to identify the father's physician and work with that physician to obtain chromosome studies on the father` |
| baseline | `mmlu_12411` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12412` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12413` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12414` | `mcq` | false | `A` | `B. Await contact with the caregiver before proceeding with management` |
| baseline | `mmlu_12415` | `mcq` | true | `A` | `A. Reassure the patient that her chance of becoming addicted to narcotics is minuscule` |
| baseline | `mmlu_12416` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12417` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12418` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12419` | `mcq` | true | `D` | `D. Incision and drainage` |
| baseline | `mmlu_12420` | `mcq` | true | `C` | `C. Lubiprostone` |
| baseline | `mmlu_12421` | `mcq` | false | `D` | `C. Refer her to an allergist` |
| baseline | `mmlu_12422` | `mcq` | false | `D` | `B. Parasympathetic nervous system` |
| baseline | `mmlu_12423` | `mcq` | false | `A` | `C. Middle ear effusion` |
| baseline | `mmlu_12424` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12425` | `mcq` | true | `D` | `D. Carrying self-injectable epinephrine` |
| baseline | `mmlu_12426` | `mcq` | false | `D` | `B. Barbiturates` |
| baseline | `mmlu_12427` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12428` | `mcq` | true | `D` | `D. Sexual activity` |
| baseline | `mmlu_12429` | `mcq` | true | `C` | `C. Ultrasonography` |
| baseline | `mmlu_12430` | `mcq` | true | `B` | `B. Cyclin-dependent kinases` |
| baseline | `mmlu_12431` | `mcq` | true | `C` | `C. Calcium pyrophosphate` |
| baseline | `mmlu_12432` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12433` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12434` | `mcq` | false | `D` | `B. Ferrous sulfate therapy` |
| baseline | `mmlu_12435` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12436` | `mcq` | false | `B` | `A. Increases cAMP concentration` |
| baseline | `mmlu_12437` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12438` | `mcq` | true | `C` | `C. "Little scientists"` |
| baseline | `mmlu_12439` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12440` | `mcq` | true | `B` | `B. A teratogen` |
| baseline | `mmlu_12441` | `mcq` | true | `A` | `A. needs analysis.` |
| baseline | `mmlu_12442` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12443` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12444` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12445` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12446` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12447` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12448` | `mcq` | true | `D` | `D. production of speech` |
| baseline | `mmlu_12449` | `mcq` | true | `D` | `D. the parents' childrearing behaviors` |
| baseline | `mmlu_12450` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12451` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12452` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12453` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12454` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12455` | `mcq` | false | `B` | `D. Dr. Y and Dr. Z should be listed as co-authors.` |
| baseline | `mmlu_12456` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12457` | `mcq` | true | `B` | `B. Referral out` |
| baseline | `mmlu_12458` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12459` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12460` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12461` | `mcq` | false | `A` | `B. Brief Reactive Psychosis` |
| baseline | `mmlu_12462` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12463` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12464` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12465` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12466` | `mcq` | false | `B` | `C. conjunctive` |
| baseline | `mmlu_12467` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12468` | `mcq` | true | `C` | `C. Provide the data to an appropriately qualified psychologist as indicated on the release form` |
| baseline | `mmlu_12469` | `mcq` | false | `D` | `C. adverse impact` |
| baseline | `mmlu_12470` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_12471` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12472` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12473` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12474` | `mcq` | true | `B` | `B. seek professional consultation and consider temporarily suspending his practice.` |
| baseline | `mmlu_12475` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12476` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12477` | `mcq` | false | `B` | `C. Aphasia` |
| baseline | `mmlu_12478` | `mcq` | false | `D` | `B. the quality of the parent-child relationships prior to the divorce.` |
| baseline | `mmlu_12479` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12481` | `mcq` | true | `A` | `A. more challenging` |
| baseline | `mmlu_12482` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12483` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12484` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12485` | `mcq` | false | `D` | `A. Report it to the APA Ethics Committee` |
| baseline | `mmlu_12486` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12487` | `mcq` | true | `B` | `B. at specific times, because then the medication will not be given in response to pain` |
| baseline | `mmlu_12488` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12489` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12490` | `mcq` | true | `C` | `C. Relatively malleable` |
| baseline | `mmlu_12491` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12492` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12493` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12494` | `mcq` | true | `D` | `D. Functional abilities` |
| baseline | `mmlu_12495` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12496` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12497` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12498` | `mcq` | true | `A` | `A. unfreezing, changing, and refreezing` |
| baseline | `mmlu_12499` | `mcq` | false | `B` | `A.` |
