# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 247 / 500 | 0.4940 | 9.0105 | 0.169351 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_12500` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12501` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12502` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12503` | `mcq` | false | `A` | `B. Nonlinear` |
| baseline | `mmlu_12504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12505` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12506` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12507` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12508` | `mcq` | true | `B` | `B. Mediator` |
| baseline | `mmlu_12509` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12510` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12511` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12512` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12513` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12514` | `mcq` | false | `A` | `C. categorization.` |
| baseline | `mmlu_12515` | `mcq` | true | `A` | `A. effect of an IV at diff levels of the other IVs` |
| baseline | `mmlu_12516` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12517` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12518` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12519` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12520` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12521` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12522` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12523` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12524` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12525` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12526` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12527` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12528` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12529` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12530` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12531` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12532` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12533` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12534` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12535` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12536` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12537` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12538` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12539` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12540` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12541` | `mcq` | false | `A` | `C. chronological age` |
| baseline | `mmlu_12542` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12543` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12544` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12545` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12546` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12547` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12548` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12549` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12550` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12551` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12552` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12553` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12554` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12555` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12556` | `mcq` | false | `A` | `B. higher-order conditioning` |
| baseline | `mmlu_12557` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12558` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12559` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12560` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12561` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12562` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12563` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12564` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12565` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12566` | `mcq` | true | `B` | `B. adrenal and pituitary` |
| baseline | `mmlu_12567` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12568` | `mcq` | false | `D` | `A. agree to see Mrs. Wang's daughter in therapy since you've had some experience providing crisis intervention experienc` |
| baseline | `mmlu_12569` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12570` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12571` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12572` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12573` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12574` | `mcq` | false | `C` | `A. non-White research participants` |
| baseline | `mmlu_12575` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12576` | `mcq` | false | `A` | `C. Emotionally cut-off.` |
| baseline | `mmlu_12577` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12578` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12579` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12580` | `mcq` | true | `A` | `A. emic` |
| baseline | `mmlu_12581` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12582` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12583` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12584` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12585` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12586` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12587` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12588` | `mcq` | true | `B` | `B. Obedience` |
| baseline | `mmlu_12589` | `mcq` | false | `C` | `B. Both the parent(s) and the child provide written consent to therapy for the child.` |
| baseline | `mmlu_12590` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12591` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12592` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12593` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12594` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12595` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12596` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12597` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12598` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12599` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12600` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12601` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12602` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12603` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12604` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12605` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12606` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12607` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12608` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12609` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12610` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12611` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12612` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12613` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12614` | `mcq` | true | `A` | `A. making new information meaningful` |
| baseline | `mmlu_12615` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12616` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12617` | `mcq` | true | `A` | `A. authoritative.` |
| baseline | `mmlu_12618` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12619` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12620` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12621` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12622` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12623` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12624` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12625` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12626` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12627` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12628` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12629` | `mcq` | false | `D` | `A. high task-orientation and low relationship orientation` |
| baseline | `mmlu_12630` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12631` | `mcq` | false | `A` | `B. Testify` |
| baseline | `mmlu_12632` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12633` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12634` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12635` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12636` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12637` | `mcq` | false | `C` | `B. internal` |
| baseline | `mmlu_12638` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12639` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12640` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12641` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12642` | `mcq` | false | `C` | `A. during the first few days after starting antidepressant medication` |
| baseline | `mmlu_12643` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12644` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12645` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12646` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12647` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12648` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12649` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12650` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12651` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12652` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12653` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12654` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12655` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12656` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12658` | `mcq` | false | `C` | `D. fatalism` |
| baseline | `mmlu_12659` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12660` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12661` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12662` | `mcq` | true | `A` | `A. blocked potential.` |
| baseline | `mmlu_12663` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12664` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12665` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12666` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12667` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12668` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12669` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12670` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12671` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12672` | `mcq` | false | `A` | `B. advocate.` |
| baseline | `mmlu_12673` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12674` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12675` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12676` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12677` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12678` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12679` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12680` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12681` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12682` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12683` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12684` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12685` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12686` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12687` | `mcq` | true | `B` | `B. Interval` |
| baseline | `mmlu_12688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12689` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12690` | `mcq` | true | `C` | `C. Resistance and immersion` |
| baseline | `mmlu_12691` | `mcq` | true | `C` | `C. Institutional` |
| baseline | `mmlu_12692` | `mcq` | false | `A` | `B. homophobia.` |
| baseline | `mmlu_12693` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12694` | `mcq` | true | `A` | `A. measure of agreement between 2 raters using nominal scales` |
| baseline | `mmlu_12695` | `mcq` | false | `D` | `A. Transtheoretical` |
| baseline | `mmlu_12696` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12697` | `mcq` | true | `B` | `B. Increases` |
| baseline | `mmlu_12698` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12699` | `mcq` | true | `A` | `A. Physiological tolerance and withdrawal.` |
| baseline | `mmlu_12700` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12701` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12702` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12703` | `mcq` | true | `B` | `B. depression` |
| baseline | `mmlu_12704` | `mcq` | true | `B` | `B. Productivity` |
| baseline | `mmlu_12705` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12706` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12707` | `mcq` | false | `C` | `A. Working` |
| baseline | `mmlu_12708` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12709` | `mcq` | true | `A` | `A. sleeping` |
| baseline | `mmlu_12710` | `mcq` | false | `C` | `A. discuss his vacation plans with his current clients ahead of time so that they know he'll be unavailable during that ` |
| baseline | `mmlu_12711` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12712` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12713` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12714` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12715` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12716` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12717` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12718` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12719` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12720` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12721` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12722` | `mcq` | false | `A` | `D. charismatic` |
| baseline | `mmlu_12723` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12724` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12725` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12726` | `mcq` | false | `D` | `B. compensatory` |
| baseline | `mmlu_12727` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12728` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12729` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12730` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12731` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12732` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12733` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12734` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12735` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12736` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12737` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12738` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12739` | `mcq` | false | `C` | `A. ruling out other etiologies through a comprehensive psychodiagnostics workup` |
| baseline | `mmlu_12740` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12741` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12742` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12743` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12744` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12745` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12746` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12747` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12748` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12749` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12750` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12751` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12752` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12753` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12754` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12755` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12756` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12757` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12758` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12759` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12760` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12761` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12762` | `mcq` | true | `B` | `B. Social learning` |
| baseline | `mmlu_12763` | `mcq` | false | `C` | `B. 5 to 7` |
| baseline | `mmlu_12764` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12765` | `mcq` | false | `C` | `A. Young ethnic minority women` |
| baseline | `mmlu_12766` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12767` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12769` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12770` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12771` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12772` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12773` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12774` | `mcq` | false | `C` | `B. Empirically keyed` |
| baseline | `mmlu_12775` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12776` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12777` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12778` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12779` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12780` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12781` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12782` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12783` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12784` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12785` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12786` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12787` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12788` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12789` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12790` | `mcq` | true | `A` | `A. job satisfaction` |
| baseline | `mmlu_12791` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12792` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12793` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12794` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12795` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12796` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12797` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12798` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12799` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12800` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12801` | `mcq` | true | `B` | `B. actor-observer effect` |
| baseline | `mmlu_12802` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12803` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12804` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12805` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12806` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12807` | `mcq` | false | `A` | `D. Consistency` |
| baseline | `mmlu_12808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12809` | `mcq` | false | `D` | `B. suggest that she make an appointment so you can discuss the matter in person.` |
| baseline | `mmlu_12810` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12811` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12812` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12813` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12814` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12815` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12816` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12817` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12818` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12819` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12820` | `mcq` | false | `D` | `A. stimulus control` |
| baseline | `mmlu_12821` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12822` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12823` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12824` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12825` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12826` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12827` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12828` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12829` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12830` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12831` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12832` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12833` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12834` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12835` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12836` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12837` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12838` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12839` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12840` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12841` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12842` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12843` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12844` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12845` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12846` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12847` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12848` | `mcq` | false | `D` | `A. must report the violation to the APA Ethics Committee.` |
| baseline | `mmlu_12849` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12850` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12851` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12852` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12853` | `mcq` | false | `D` | `B. when study has 2 or more DVs` |
| baseline | `mmlu_12854` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12855` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12856` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12857` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12858` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12859` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12860` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12861` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12862` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12863` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12864` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12865` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12866` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12867` | `mcq` | true | `C` | `C. Correlational Research` |
| baseline | `mmlu_12868` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12869` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12870` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12871` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12872` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12873` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12874` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12875` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12876` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12877` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12878` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12879` | `mcq` | false | `C` | `B. math` |
| baseline | `mmlu_12880` | `mcq` | false | `B` | `A. All Verbal subtests` |
| baseline | `mmlu_12881` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12882` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12883` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12884` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12885` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12886` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12887` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12888` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12889` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12890` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12891` | `mcq` | false | `D` | `A. stating conclusions in tentative terms` |
| baseline | `mmlu_12892` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12893` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12894` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12895` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12896` | `mcq` | true | `B` | `B. less than 130` |
| baseline | `mmlu_12897` | `mcq` | true | `D` | `D. Discuss the possible ramifications and legal consequences of terminating therapy without informing his probation offi` |
| baseline | `mmlu_12898` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12899` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12900` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12901` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12902` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12903` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12904` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12905` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12906` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12907` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12908` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12909` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12910` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12911` | `mcq` | false | `B` | `A. talk for longer periods of time.` |
| baseline | `mmlu_12912` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12913` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12914` | `mcq` | false | `C` | `A..stage of career development.` |
| baseline | `mmlu_12915` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12916` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12917` | `mcq` | true | `D` | `D. allow the student to withdraw from the study.` |
| baseline | `mmlu_12918` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12919` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12920` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12921` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12922` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12923` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12924` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12925` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12926` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12927` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12928` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12929` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12930` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12931` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12932` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12933` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12934` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12935` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12936` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12937` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12938` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12939` | `mcq` | false | `C` | `A. content` |
| baseline | `mmlu_12940` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12941` | `mcq` | false | `A` | `B. Conditioning` |
| baseline | `mmlu_12942` | `mcq` | false | `A` | `D. advise the attorney who issued the subpoena that he cannot appear as requested because the client has not given him p` |
| baseline | `mmlu_12943` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12944` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12945` | `mcq` | false | `A` | `B. CS` |
| baseline | `mmlu_12946` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12947` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12948` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12949` | `mcq` | true | `D` | `D. empathy` |
| baseline | `mmlu_12950` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12951` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12952` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12953` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12954` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12955` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12956` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12957` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12958` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12959` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12960` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12961` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12962` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12963` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12964` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12965` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12966` | `mcq` | true | `B` | `B. raise for discussion the possibility of termination and referral to another therapist.` |
| baseline | `mmlu_12967` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12968` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12969` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12970` | `mcq` | true | `A` | `A. when reversal is not possible` |
| baseline | `mmlu_12971` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12972` | `mcq` | true | `D` | `D. not release any information to the mother without appropriate authorization.` |
| baseline | `mmlu_12973` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12974` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12975` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12976` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12977` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12978` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12979` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12980` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12981` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12982` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12983` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12984` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12986` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12987` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12988` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12989` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12990` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12991` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12992` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12993` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12994` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12995` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12996` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12997` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12998` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12999` | `mcq` | false | `A` | `B` |
