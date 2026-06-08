# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 202 / 500 | 0.4040 | 8.4533 | 0.185024 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_11500` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11501` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11502` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11503` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11504` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11505` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11506` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11507` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11508` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11509` | `mcq` | true | `D` | `D. not guilty, because the bookcase was a fixture.` |
| baseline | `mmlu_11510` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11511` | `mcq` | false | `D` | `C. Assault and battery.` |
| baseline | `mmlu_11512` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11513` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11514` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11515` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11516` | `mcq` | true | `A` | `A. Nothing.` |
| baseline | `mmlu_11517` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11518` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11519` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11520` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11521` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11522` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11523` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11524` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11525` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11526` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11527` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11528` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11529` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11530` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11531` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11532` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11533` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11534` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11535` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11536` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11537` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11538` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11539` | `mcq` | false | `D` | `B. negligence.` |
| baseline | `mmlu_11540` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11541` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11542` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11543` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11544` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11545` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11546` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11547` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11548` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11549` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11550` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11551` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11552` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11553` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11554` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11555` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11556` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11557` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11558` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11559` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11560` | `mcq` | false | `B` | `C. not prevail, because the conveyance between the investor and the friend did not effectuate a delegation of duties.` |
| baseline | `mmlu_11561` | `mcq` | true | `D` | `D. murder.` |
| baseline | `mmlu_11562` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11563` | `mcq` | false | `D` | `B. Attempted violation of the statute.` |
| baseline | `mmlu_11564` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11565` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11566` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11567` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11568` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11569` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11570` | `mcq` | false | `B` | `D. neither the man nor the woman is guilty of manslaughter.` |
| baseline | `mmlu_11571` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11572` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11573` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11574` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11575` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11576` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11578` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11579` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11580` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11581` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11582` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11583` | `mcq` | true | `C` | `C. Yes, because expert testimony on such issues of causation is relevant and helpful to the jury.` |
| baseline | `mmlu_11584` | `mcq` | false | `B` | `D. denied with respect to both the ski mask and the money.` |
| baseline | `mmlu_11585` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11586` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11587` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11588` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11589` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11590` | `mcq` | false | `B` | `C. denied, because the verdicts do not amount to a reversible error.` |
| baseline | `mmlu_11591` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11592` | `mcq` | true | `C` | `C. as an excited utterance.` |
| baseline | `mmlu_11593` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11594` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11595` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11596` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11597` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11598` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11599` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11600` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11601` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11602` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11603` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11604` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11605` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11606` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11607` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11608` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11609` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11610` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11611` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11612` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11613` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11614` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11615` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11616` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11617` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11618` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11619` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11620` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11621` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11622` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11623` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11624` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11625` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11626` | `mcq` | true | `D` | `D. sustained, because the defendant's statement was the product of a warrantless entry of his home.` |
| baseline | `mmlu_11627` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11628` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11629` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11630` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11631` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11632` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11633` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11634` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11635` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11636` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11637` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11638` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11639` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11640` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11641` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11642` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11643` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11644` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11645` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11646` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11647` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11648` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11649` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11650` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11651` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11652` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11653` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11654` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11655` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11656` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11658` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11659` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11660` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11661` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11662` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11663` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11664` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11665` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11666` | `mcq` | true | `D` | `D. not prevail, because the owner had discontinued protection services from the company when the shooting occurred.` |
| baseline | `mmlu_11667` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11668` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11669` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11670` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11671` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11672` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11673` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11674` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11675` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11676` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11677` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11678` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11679` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11680` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11681` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11682` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11683` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11684` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11685` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11686` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11687` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11688` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11689` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11690` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11691` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11692` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11693` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11694` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11695` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11696` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11697` | `mcq` | false | `A` | `B. dismiss the action as moot.` |
| baseline | `mmlu_11698` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11699` | `mcq` | false | `B` | `D. Yes, because responsible government officials cannot conduct or formulate their decisionmaking processes by means of ` |
| baseline | `mmlu_11700` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11701` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11702` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11703` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11704` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11705` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11706` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11707` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11708` | `mcq` | true | `D` | `D. not recover, because the professor remains liable.` |
| baseline | `mmlu_11709` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11710` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11711` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11712` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11713` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11714` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11715` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11716` | `mcq` | true | `C` | `C. Yes, because the patient has failed to introduce evidence that the first orthopedist's care fell below the profession` |
| baseline | `mmlu_11717` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11718` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11719` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11720` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11721` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11722` | `mcq` | false | `C` | `D. the school district, because the 10-acre tract constituted an equitable servitude.` |
| baseline | `mmlu_11723` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11724` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11725` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11726` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11728` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11729` | `mcq` | true | `B` | `B. not guilty, by reason of necessity.` |
| baseline | `mmlu_11730` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11731` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11733` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11734` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11735` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11736` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11737` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11738` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11739` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11740` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11741` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11742` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11743` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11744` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11745` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11746` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11747` | `mcq` | true | `D` | `D. All three defendants.` |
| baseline | `mmlu_11748` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11749` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11750` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11751` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11752` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11753` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11754` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11755` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11756` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11757` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11758` | `mcq` | true | `A` | `A. The credit union, because the credit union has priority.` |
| baseline | `mmlu_11759` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11760` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11761` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11762` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11763` | `mcq` | false | `C` | `D. Yes, based on the denial of counsel at both stages of the proceeding.` |
| baseline | `mmlu_11764` | `mcq` | false | `C` | `B. $225,000.00` |
| baseline | `mmlu_11765` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11766` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11767` | `mcq` | false | `A` | `C. Specific performance.` |
| baseline | `mmlu_11768` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11769` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11770` | `mcq` | false | `B` | `D. No, because the defendant's withdrawal was effective.` |
| baseline | `mmlu_11771` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11772` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11773` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11775` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11776` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11777` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11778` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11779` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11780` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11781` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11782` | `mcq` | true | `D` | `D. Yes, there was sufficient provocation to justify a jury charge of voluntary manslaughter.` |
| baseline | `mmlu_11783` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11784` | `mcq` | false | `C` | `B. $30,000. 00` |
| baseline | `mmlu_11785` | `mcq` | false | `C` | `B. on November 12, 1981.` |
| baseline | `mmlu_11786` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11787` | `mcq` | false | `B` | `C. lose, because she failed to overcome the presumption.` |
| baseline | `mmlu_11788` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11789` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11790` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11791` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11792` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11793` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11794` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11795` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11796` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11797` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11798` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11799` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11800` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11801` | `mcq` | true | `C` | `C. Yes, the evidence indicates that the sellers made knowingly false representations of material fact to induce the buye` |
| baseline | `mmlu_11802` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11803` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11804` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11805` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11806` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11807` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11809` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11810` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11811` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11812` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11813` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11814` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11815` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11816` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11817` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11818` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11819` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11820` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11821` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11822` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11823` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11824` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11825` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11826` | `mcq` | true | `C` | `C. murder.` |
| baseline | `mmlu_11827` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11828` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11829` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11830` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11831` | `mcq` | true | `B` | `B. 2` |
| baseline | `mmlu_11832` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11833` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11834` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_11835` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11836` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11837` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11838` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11839` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11840` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11841` | `mcq` | true | `D` | `D. not prevail, because the columnist was not involved in the burglary and did not conspire with the apprentice with res` |
| baseline | `mmlu_11842` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11843` | `mcq` | true | `C` | `C. not be held responsible, because the center's consent was effective.` |
| baseline | `mmlu_11844` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_11845` | `mcq` | false | `B` | `C. Both the daughter and the mortgage company have causes of action against the woman.` |
| baseline | `mmlu_11846` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11847` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11848` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11849` | `mcq` | true | `C` | `C. Yes, because the pilot can invoke the privilege of necessity.` |
| baseline | `mmlu_11850` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11851` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11852` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11853` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11854` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11855` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11856` | `mcq` | false | `B` | `D. murder.` |
| baseline | `mmlu_11857` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11858` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11859` | `mcq` | false | `A` | `D. Yes, because the non-assignment provision is not enforceable since public policy favors free assignment and delegatio` |
| baseline | `mmlu_11860` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11861` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11862` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11863` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11864` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11865` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11866` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11867` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11868` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11869` | `mcq` | true | `D` | `D. The manufacturer, because the buyer's negligence in the way he used the shovel was one of the causes of his injury.` |
| baseline | `mmlu_11870` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11871` | `mcq` | false | `D` | `B. win, because the second contract for $75 superseded the original $50 contract.` |
| baseline | `mmlu_11872` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11873` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11874` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11875` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11876` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11877` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11878` | `mcq` | true | `C` | `C. The skier, because the neighbor had already obtained an easement by prescription.` |
| baseline | `mmlu_11879` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11880` | `mcq` | false | `D` | `B. The truck driver recovers $5,000, and the car driver recovers $4,000.` |
| baseline | `mmlu_11881` | `mcq` | true | `D` | `D. None.` |
| baseline | `mmlu_11882` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11883` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11884` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11885` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11886` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_11887` | `mcq` | true | `D` | `D. Yes, because the modification was fair and equitable in view of the unanticipated increase in the price of structural` |
| baseline | `mmlu_11888` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11889` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11890` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11891` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11892` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11893` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11894` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11895` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_11896` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11897` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11898` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11899` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_11900` | `mcq` | false | `C` | `D. not guilty, because she had no legal duty to render assistance.` |
| baseline | `mmlu_11901` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11902` | `mcq` | false | `B` | `C. Yes, because the man indirectly set fire to the friend's cabin.` |
| baseline | `mmlu_11903` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11904` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11905` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11906` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11907` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11908` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11909` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11910` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11911` | `mcq` | true | `A` | `A. $100,000, because that was the contract price.` |
| baseline | `mmlu_11912` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11913` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11914` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_11915` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11916` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11917` | `mcq` | true | `C` | `C. Yes, because the opinion is based on her specialized knowledge, and it will assist the trier of fact in understanding` |
| baseline | `mmlu_11918` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11919` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11920` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11921` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_11922` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11923` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11924` | `mcq` | true | `D` | `D. No crime.` |
| baseline | `mmlu_11925` | `mcq` | false | `B` | `D. The son, because during the past 25 years, the son has exercised the type of occupancy ordinarily considered sufficie` |
| baseline | `mmlu_11926` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11927` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11928` | `mcq` | false | `A` | `B. Only the portion concerning the engineer's reputation is admissible, because where both opinion and reputation eviden` |
| baseline | `mmlu_11929` | `mcq` | false | `B` | `D. The millionaire, because he put the water to a beneficial use prior to the rancher's use and has continuously used th` |
| baseline | `mmlu_11930` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11931` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11932` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11933` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11934` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11935` | `mcq` | true | `A` | `A. The farmer.` |
| baseline | `mmlu_11936` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11937` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11938` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11939` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11940` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11941` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_11942` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11943` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11944` | `mcq` | true | `A` | `A. not guilty.` |
| baseline | `mmlu_11945` | `mcq` | false | `B` | `D. The restaurant owner, because there was no disturbance of peaceful enjoyment of the neighboring property.` |
| baseline | `mmlu_11946` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11947` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11948` | `mcq` | true | `D` | `D. Yes, he is liable because an owner who knows of the dog's dangerous propensities is strictly liable for ensuing damag` |
| baseline | `mmlu_11949` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_11950` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11951` | `mcq` | false | `B` | `C. excluded, because the officer's conduct violated the man's Sixth Amendment right to counsel.` |
| baseline | `mmlu_11952` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11953` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_11954` | `mcq` | false | `D` | `C. Yes, as a prior consistent statement of the defendant.` |
| baseline | `mmlu_11955` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_11956` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11957` | `mcq` | true | `D` | `D. Yes, the elements of false imprisonment are sufficiently established there was an intentional illegal confinement t` |
| baseline | `mmlu_11958` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11959` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11960` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_11961` | `mcq` | false | `B` | `C. not prevail, because the employee was acting outside the scope of the employment relationship at the time of the acci` |
| baseline | `mmlu_11962` | `mcq` | false | `B` | `C. not continuous.` |
| baseline | `mmlu_11963` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11964` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11965` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11966` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11967` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11968` | `mcq` | false | `D` | `B. She does have to produce the MRI scan because a layperson cannot testify to personal observations.` |
| baseline | `mmlu_11969` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11970` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_11971` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11972` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11973` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_11974` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_11975` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_11976` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_11977` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_11978` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_11979` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_11980` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_11981` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_11982` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11983` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11984` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_11985` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_11986` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_11987` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11988` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11989` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_11990` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11991` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11992` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_11993` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_11994` | `mcq` | false | `B` | `A. $20,000 (the $45,000 contract price less the $25,000 the mason could have earned in other employment).` |
| baseline | `mmlu_11995` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_11996` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_11997` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_11998` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_11999` | `mcq` | false | `B` | `C.` |
