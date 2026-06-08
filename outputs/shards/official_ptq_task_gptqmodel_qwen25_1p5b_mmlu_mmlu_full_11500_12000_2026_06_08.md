# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 186 / 500 | 0.3720 | 10.0391 | 0.178200 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_11500` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11501` | `mcq` | false | `D` | `A. No, the entry was authorized by exigent circumstances and the gun was in plain view.` |
| baseline | `mmlu_11502` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11503` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11504` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11505` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11506` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11507` | `mcq` | true | `B` | `B. No, because the act of purchasing supplies specifically for the homeowner's job was an effective acceptance and a con` |
| baseline | `mmlu_11508` | `mcq` | false | `A` | `B. Yes, because a customer voluntarily assumes the foreseeable risk that fish will contain metal fish hooks.` |
| baseline | `mmlu_11509` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11510` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11511` | `mcq` | false | `D` | `C. Assault and battery.` |
| baseline | `mmlu_11512` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11513` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11514` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11515` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11516` | `mcq` | true | `A` | `A. Nothing.` |
| baseline | `mmlu_11517` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11518` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11519` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11520` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11521` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11522` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11523` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11524` | `mcq` | true | `C` | `C. Yes, because a life-without-parole sentence is not permissible for a juvenile defendant convicted of a nonviolent off` |
| baseline | `mmlu_11525` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11526` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11527` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11528` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11529` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11530` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11531` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11532` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11533` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11534` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11535` | `mcq` | false | `A` | `B. Yes, because the activity was outrageous and shocking.` |
| baseline | `mmlu_11536` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11537` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11538` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11539` | `mcq` | false | `D` | `B. negligence.` |
| baseline | `mmlu_11540` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11541` | `mcq` | false | `C` | `A. No, because they are hearsay not within any exception.` |
| baseline | `mmlu_11542` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11543` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11544` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11545` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11546` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11547` | `mcq` | false | `B` | `None, because the co-worker acquired title to the whole of the property by right of survivorship.` |
| baseline | `mmlu_11548` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11549` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11550` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11551` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11552` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11553` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11554` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11555` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11556` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11557` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11558` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11559` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11560` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11561` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11562` | `mcq` | false | `B` | `No, because the homeowner had no practical way of controlling where the material went and he acted without malice or ill` |
| baseline | `mmlu_11563` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11564` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11565` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11566` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11567` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11568` | `mcq` | false | `C` | `A. He did not intend to use the gun for an unlawful purpose.` |
| baseline | `mmlu_11569` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11570` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11571` | `mcq` | true | `A` | `A. No, because the city's failure to perform has frustrated the purpose of the liquidated damages clause, making liquida` |
| baseline | `mmlu_11572` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11573` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11574` | `mcq` | true | `D` | `D. No, because it is hearsay within hearsay, and there are no hearsay exceptions that apply.` |
| baseline | `mmlu_11575` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11576` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11577` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11578` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11579` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11580` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11581` | `mcq` | false | `C` | `No, because the law reasonably conserves the state's limited resources.` |
| baseline | `mmlu_11582` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11583` | `mcq` | false | `C` | `No, because the expert has used a reliable method for reaching his conclusion.` |
| baseline | `mmlu_11584` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11585` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11586` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11587` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11588` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11589` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11590` | `mcq` | false | `B` | `denied` |
| baseline | `mmlu_11591` | `mcq` | false | `A` | `D. Yes, because the bank's loan modification was material.` |
| baseline | `mmlu_11592` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11593` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11594` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11595` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11596` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11597` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11598` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11599` | `mcq` | false | `D` | `A. granted, because the housekeeper's testimony is hearsay not within any recognized exception.` |
| baseline | `mmlu_11600` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11601` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11602` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11603` | `mcq` | false | `C` | `A. The equal protection clause of the Fourteenth Amendment.` |
| baseline | `mmlu_11604` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11605` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11606` | `mcq` | false | `C` | `denied, because the husband left the briefcase in the kitchen in plain view.` |
| baseline | `mmlu_11607` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11608` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11609` | `mcq` | false | `A` | `D. No crime.` |
| baseline | `mmlu_11610` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11611` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11612` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11613` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11614` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11615` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11616` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11617` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11618` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11619` | `mcq` | true | `B` | `B. it is necessary to further a compelling state interest.` |
| baseline | `mmlu_11620` | `mcq` | false | `B` | `A. only if the manufacturer had been a party to the former proceeding.` |
| baseline | `mmlu_11621` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11622` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11623` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11624` | `mcq` | true | `C` | `C. issue an injunction against the neighbor unless it can be shown that the neighbor's use did not unreasonably interfer` |
| baseline | `mmlu_11625` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11626` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11627` | `mcq` | false | `B` | `D. No, because the customer was not justified in relying on the woman's offer.` |
| baseline | `mmlu_11628` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11629` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11630` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11631` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11632` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11633` | `mcq` | false | `C` | `A. win, because his deed antedated the woman's deed.` |
| baseline | `mmlu_11634` | `mcq` | true | `C` | `C. No, because such "sexual predisposition" evidence is generally prohibited by the rules of evidence except under narro` |
| baseline | `mmlu_11635` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11636` | `mcq` | false | `B` | `C. Yes, because surplus government property is not subject to the limitations imposed by the establishment clause as inc` |
| baseline | `mmlu_11637` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11638` | `mcq` | false | `C` | `A. No, because the woman did not make any subsequent affirmative misrepresentations about her financial condition.` |
| baseline | `mmlu_11639` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11640` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11641` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11642` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11643` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11644` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11645` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11646` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11647` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11648` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11649` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11650` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11651` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11652` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11653` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11654` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11655` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11656` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11657` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11658` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11659` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11660` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11661` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11662` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11663` | `mcq` | true | `D` | `D. Yes, it is unconstitutional because it presents an undue burden on a woman's right to obtain an abortion.` |
| baseline | `mmlu_11664` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11665` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11666` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11667` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11668` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11669` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11670` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11671` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11672` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11673` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11674` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11675` | `mcq` | false | `D` | `No, because of the doctrine of alternative liability.` |
| baseline | `mmlu_11676` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11677` | `mcq` | true | `B` | `B. No, because the officer had reasonable suspicion to believe that there might be criminal activity afoot.` |
| baseline | `mmlu_11678` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11679` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11680` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11681` | `mcq` | true | `A` | `A. Yes, because the dishwasher was defective.` |
| baseline | `mmlu_11682` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11683` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11684` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11685` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11686` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11687` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11688` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11689` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11690` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11691` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11692` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11693` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11694` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11695` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11696` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11697` | `mcq` | false | `A` | `B. dismiss the action as moot.` |
| baseline | `mmlu_11698` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11699` | `mcq` | false | `B` | `C. Yes, because the action of the city violated the equal protection clause of the Fourteenth Amendment.` |
| baseline | `mmlu_11700` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11701` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11702` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11703` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11704` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11705` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11706` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11707` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11708` | `mcq` | true | `D` | `D. not recover, because the professor remains liable.` |
| baseline | `mmlu_11709` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11710` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11711` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11712` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11713` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11714` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11715` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11716` | `mcq` | true | `C` | `C. Yes, because the patient has failed to introduce evidence that the first orthopedist's care fell below the profession` |
| baseline | `mmlu_11717` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11718` | `mcq` | true | `B` | `B. Yes, there were sufficient facts for the former employee to establish the basic elements of the malicious prosecution` |
| baseline | `mmlu_11719` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11720` | `mcq` | false | `A` | `B. constituted an impermissible conflict of interest.` |
| baseline | `mmlu_11721` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11722` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11723` | `mcq` | false | `D` | `No, because the loan agreement was a condition precedent to the existence of the contract.` |
| baseline | `mmlu_11724` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11725` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11726` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11728` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11729` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11730` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11731` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11733` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11734` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11735` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11736` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11737` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11738` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11739` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11740` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11741` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11742` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11743` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11744` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11745` | `mcq` | true | `B` | `B. No, the testimony was admissible because several factors militated in favor of the expert's opinion being reliable, a` |
| baseline | `mmlu_11746` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11747` | `mcq` | true | `D` | `D. All three defendants.` |
| baseline | `mmlu_11748` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11749` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11750` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11751` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11752` | `mcq` | true | `D` | `D. an undivided one-third interest in the land.` |
| baseline | `mmlu_11753` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11754` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11755` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11756` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11757` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11758` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11759` | `mcq` | false | `B` | `C. No, because the cause of death is an issue to be decided by the jury.` |
| baseline | `mmlu_11760` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11761` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11762` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11763` | `mcq` | false | `C` | `D. Yes, based on the denial of counsel at both stages of the proceeding.` |
| baseline | `mmlu_11764` | `mcq` | false | `C` | `D. $232,000.00` |
| baseline | `mmlu_11765` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11766` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11767` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11768` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11769` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11770` | `mcq` | false | `B` | `D. No, because the defendant's withdrawal was effective.` |
| baseline | `mmlu_11771` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11772` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11773` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11774` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11775` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11776` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11777` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11778` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11779` | `mcq` | false | `D` | `No, because the closing occurred after the listing period had expired.` |
| baseline | `mmlu_11780` | `mcq` | false | `B` | `No, the testimony was admissible because it tended to show a pattern of "transferred intent" that proved the defendant's` |
| baseline | `mmlu_11781` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11782` | `mcq` | true | `D` | `D. Yes, there was sufficient provocation to justify a jury charge of voluntary manslaughter.` |
| baseline | `mmlu_11783` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11784` | `mcq` | false | `C` | `D. $100,000. 00` |
| baseline | `mmlu_11785` | `mcq` | false | `C` | `B. on November 12, 1981.` |
| baseline | `mmlu_11786` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11787` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11788` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11789` | `mcq` | true | `A` | `A. No, because the janitor's statement is a hearsay not within any exception.` |
| baseline | `mmlu_11790` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11791` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11792` | `mcq` | false | `B` | `No, because the intervention of third parties is unpredictable and not within the foreseeability of the hospital. Theref` |
| baseline | `mmlu_11793` | `mcq` | false | `B` | `No, because the government has a right to have its designated representative remain in the courtroom through-out the tri` |
| baseline | `mmlu_11794` | `mcq` | false | `A` | `No, because the Sheriff, as a part of the executive branch himself, is not legally qualified to bring a claim against th` |
| baseline | `mmlu_11795` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11796` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11797` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11798` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11799` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11800` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11801` | `mcq` | true | `C` | `C. Yes, the evidence indicates that the sellers made knowingly false representations of material fact to induce the buye` |
| baseline | `mmlu_11802` | `mcq` | false | `C` | `No, because the parties cannot proceed in federal court since there is no diversity of citizenship.` |
| baseline | `mmlu_11803` | `mcq` | false | `A` | `B. Interstate travel` |
| baseline | `mmlu_11804` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11805` | `mcq` | false | `A` | `C. H holds herself out as an expert in the goods sold to Roberta.` |
| baseline | `mmlu_11806` | `mcq` | false | `B` | `C. Yes, so long as a reasonable person in the friend's position would have considered the letter as referring to the 198` |
| baseline | `mmlu_11807` | `mcq` | false | `C` | `No, because the note and mortgage did not contain a due-on-sale clause.` |
| baseline | `mmlu_11808` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11809` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11810` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11811` | `mcq` | false | `D` | `No, because the company was engaged in an abnormally dangerous activity.` |
| baseline | `mmlu_11812` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11813` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11814` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11815` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11816` | `mcq` | false | `B` | `No, because a jury could find the hospital liable for negligence based on res ipsa loquitur.` |
| baseline | `mmlu_11817` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11818` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11819` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11820` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11821` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11822` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11823` | `mcq` | false | `A` | `No, because a business owner has a constitutional right to present and admit character evidence.` |
| baseline | `mmlu_11824` | `mcq` | false | `A` | `C. No, it will not dismiss because the circumstances show that all of the elements of defamation are all present.` |
| baseline | `mmlu_11825` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11826` | `mcq` | true | `C` | `C. murder.` |
| baseline | `mmlu_11827` | `mcq` | false | `A` | `D. Nothing, because the driver was contributorily negligent for parking his car so that part of it stuck out into the st` |
| baseline | `mmlu_11828` | `mcq` | false | `A` | `C. No, because the driver has properly alleged a joint enterprise situation where the passenger is liable for her share ` |
| baseline | `mmlu_11829` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11830` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11831` | `mcq` | false | `B` | `D. None.` |
| baseline | `mmlu_11832` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11833` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11834` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11835` | `mcq` | true | `D` | `D. No, because the SPCA acted under the authority of the state statute and cooperated with state authorities to perform ` |
| baseline | `mmlu_11836` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11837` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11838` | `mcq` | false | `C` | `A. No, because the customer's conduct was privileged as a defense of others.` |
| baseline | `mmlu_11839` | `mcq` | false | `C` | `No, because the corporation was not granted use-and-derivative-use immunity.` |
| baseline | `mmlu_11840` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11841` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11842` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11843` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11844` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11845` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11846` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11847` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11848` | `mcq` | false | `D` | `No, because the officers had probable cause to arrest the woman based on the store owner's complaint and honest belief t` |
| baseline | `mmlu_11849` | `mcq` | true | `C` | `C. Yes, because the pilot can invoke the privilege of necessity.` |
| baseline | `mmlu_11850` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11851` | `mcq` | false | `A` | `B. not guilty, because the killing constituted justifiable homicide.` |
| baseline | `mmlu_11852` | `mcq` | false | `B` | `D. Yes, because a dwelling owner can always use deadly force to protect his property and person from an illegal trespass` |
| baseline | `mmlu_11853` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11854` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11855` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11856` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11857` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11858` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11859` | `mcq` | false | `A` | `No, because the non-assignment provision is not enforceable since public policy favors free assignment and delegation.` |
| baseline | `mmlu_11860` | `mcq` | false | `B` | `No, because under the Sixth Amendment, a defendant has the right to a fair trial.` |
| baseline | `mmlu_11861` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11862` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11863` | `mcq` | false | `D` | `B. The man and his brother are guilty of conspiracy but not attempted murder.` |
| baseline | `mmlu_11864` | `mcq` | false | `B` | `C. No, her consent implied that the doctor could perform any other procedures that were necessary.` |
| baseline | `mmlu_11865` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11866` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11867` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11868` | `mcq` | false | `B` | `A. No, because the notice of removal was not timely filed.` |
| baseline | `mmlu_11869` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11870` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11871` | `mcq` | false | `D` | `B. win, because the second contract for $75 superseded the original $50 contract.` |
| baseline | `mmlu_11872` | `mcq` | true | `A` | `A. Dismiss the suit as moot.` |
| baseline | `mmlu_11873` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11874` | `mcq` | true | `B` | `B. recklessness in lending his car to his classmate.` |
| baseline | `mmlu_11875` | `mcq` | true | `A` | `A. denied, because the Rule would not be triggered, thus creating only a life estate in the nephew.` |
| baseline | `mmlu_11876` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11877` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11878` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11879` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11880` | `mcq` | false | `D` | `B. The truck driver recovers $5,000, and the car driver recovers $3,000.` |
| baseline | `mmlu_11881` | `mcq` | false | `D` | `B. The man and the woman.` |
| baseline | `mmlu_11882` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11883` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11884` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11885` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11886` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11887` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11888` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11889` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11890` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11891` | `mcq` | false | `C` | `No, the law will enforce the "benefit of the bargain" rule.` |
| baseline | `mmlu_11892` | `mcq` | false | `D` | `B. Yes, the newspaper is allowed to make mistakes as long as there is no malice, and the case must be dismissed as a mat` |
| baseline | `mmlu_11893` | `mcq` | false | `A` | `No, because the neighbor was an invitee for the purpose of retrieving the shovel.` |
| baseline | `mmlu_11894` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11895` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11896` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11897` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11898` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11899` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11900` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11901` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11902` | `mcq` | false | `B` | `C. Yes, because the injury to the friend and to his cabin was the natural result of the man's actions.` |
| baseline | `mmlu_11903` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11904` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11905` | `mcq` | false | `C` | `No, because the towing company assumed the risk by the manager's failure to examine the distance himself.` |
| baseline | `mmlu_11906` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11907` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11908` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11909` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11910` | `mcq` | false | `A` | `D. No, because such disclosure constitutes an implied representation that is testimonial in character and, thus, violate` |
| baseline | `mmlu_11911` | `mcq` | true | `A` | `A. $100,000, because that was the contract price.` |
| baseline | `mmlu_11912` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11913` | `mcq` | true | `A` | `A. No. While what the president did wasn't a good idea, the Constitution expressly grants the President an unqualified p` |
| baseline | `mmlu_11914` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11915` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11916` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11917` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11918` | `mcq` | false | `C` | `No, because even taking the facts in the light most favorable to the non-moving party under Rule 56, it is nonetheless c` |
| baseline | `mmlu_11919` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11920` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11921` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11922` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11923` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11924` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11925` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11926` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11927` | `mcq` | false | `B` | `A. No, because the defendant failed to object after the judge gave the instructions to the jury.` |
| baseline | `mmlu_11928` | `mcq` | false | `A` | `B. Only the portion concerning the witness's opinion of the engineer's character, because the witness's reporting of the` |
| baseline | `mmlu_11929` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11930` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11931` | `mcq` | false | `C` | `No, because he received erroneous legal advice.` |
| baseline | `mmlu_11932` | `mcq` | false | `B` | `A. Nothing.` |
| baseline | `mmlu_11933` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11934` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11935` | `mcq` | false | `A` | `B. The sister.` |
| baseline | `mmlu_11936` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11937` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11938` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11939` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11940` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11941` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11942` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11943` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11944` | `mcq` | true | `A` | `A. not guilty.` |
| baseline | `mmlu_11945` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11946` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11947` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11948` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11949` | `mcq` | false | `D` | `C. No, unless they use the rationally related to a legitimate state interest standard.` |
| baseline | `mmlu_11950` | `mcq` | true | `B` | `B. The tenant is liable under such a covenant for all defects, including the damage to the wall.` |
| baseline | `mmlu_11951` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11952` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11953` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11954` | `mcq` | true | `D` | `D. Yes, as a statement by the defendant of his then-existing state of mind.` |
| baseline | `mmlu_11955` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11956` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11957` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11958` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11959` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11960` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11961` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11962` | `mcq` | false | `B` | `D. not open and notorious.` |
| baseline | `mmlu_11963` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11964` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11965` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11966` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11967` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11968` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11969` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11970` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11971` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11972` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11973` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11974` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11975` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11976` | `mcq` | false | `D` | `A. No, because such evidence would vary an unambiguous term of the contract.` |
| baseline | `mmlu_11977` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11978` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11979` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11980` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11981` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11982` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11983` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11984` | `mcq` | false | `B` | `A. succeed, because a life tenant must account for permissive waste to the reversioner or remainderman.` |
| baseline | `mmlu_11985` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11986` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11987` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11988` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11989` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11990` | `mcq` | true | `A` | `A. No, his belief that she consented in advance was unreasonable and impermissible.` |
| baseline | `mmlu_11991` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11992` | `mcq` | true | `C` | `C. Yes, because the supplier is liable for all damages flowing directly from its breach.` |
| baseline | `mmlu_11993` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11994` | `mcq` | false | `B` | `A. $20,000 (the $45,000 contract price less the $25,000 the mason could have earned in other employment).` |
| baseline | `mmlu_11995` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11996` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11997` | `mcq` | true | `A` | `A. No, the school exercised its appropriate function of trying to restrict the use of vulgarity and offensive discourse ` |
| baseline | `mmlu_11998` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11999` | `mcq` | true | `B` | `B.` |
