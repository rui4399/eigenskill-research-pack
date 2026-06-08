# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 272 / 500 | 0.5440 | 4.7312 | 0.376475 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_12500` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12501` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12502` | `mcq` | true | `C` | `C. showed that the environment influences how a person's behavior is perceived.` |
| baseline | `mmlu_12503` | `mcq` | true | `A` | `A. Linear` |
| baseline | `mmlu_12504` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12505` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12506` | `mcq` | true | `D` | `D. Provide Hermann with appropriate referrals.` |
| baseline | `mmlu_12507` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12508` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12509` | `mcq` | false | `A` | `C. a special diet.` |
| baseline | `mmlu_12510` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12511` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12512` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12513` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12514` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12515` | `mcq` | true | `A` | `A. effect of an IV at different levels of the other IVs` |
| baseline | `mmlu_12516` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12517` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12518` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12519` | `mcq` | true | `A` | `A. Cognitive behavioral therapy` |
| baseline | `mmlu_12520` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12521` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12522` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12523` | `mcq` | true | `D` | `D. Two-Factor Theory` |
| baseline | `mmlu_12524` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12525` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12526` | `mcq` | false | `D` | `A. increase opportunities for contact under pleasant conditions.` |
| baseline | `mmlu_12527` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12528` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12529` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12530` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12531` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12532` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12533` | `mcq` | true | `D` | `D. Norm-referenced tests` |
| baseline | `mmlu_12534` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12535` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12536` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12537` | `mcq` | true | `C` | `C. 12 months` |
| baseline | `mmlu_12538` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_12539` | `mcq` | true | `A` | `A.	number	of	dimensions	necessary` |
| baseline | `mmlu_12540` | `mcq` | true | `C` | `C. substantia nigra.` |
| baseline | `mmlu_12541` | `mcq` | false | `A` | `B. life experience` |
| baseline | `mmlu_12542` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12543` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12544` | `mcq` | false | `C` | `B. 55` |
| baseline | `mmlu_12545` | `mcq` | false | `B` | `A. brain stem` |
| baseline | `mmlu_12546` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12547` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12548` | `mcq` | true | `B` | `B. Untestable and thus, of uncertain scientific value` |
| baseline | `mmlu_12549` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12550` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12551` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12552` | `mcq` | true | `A` | `A. group think` |
| baseline | `mmlu_12553` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12554` | `mcq` | false | `B` | `C. preparation` |
| baseline | `mmlu_12555` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12556` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12557` | `mcq` | true | `D` | `D. content validity` |
| baseline | `mmlu_12558` | `mcq` | true | `A` | `A. stimulus satiation` |
| baseline | `mmlu_12559` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12560` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12561` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_12562` | `mcq` | false | `B` | `A. conﬁdence, competence, and control` |
| baseline | `mmlu_12563` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12564` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12565` | `mcq` | true | `C` | `C. the best interests of the child.` |
| baseline | `mmlu_12566` | `mcq` | true | `B` | `B. adrenal and pituitary` |
| baseline | `mmlu_12567` | `mcq` | true | `B` | `B. different groups divided by age are assessed at the same time` |
| baseline | `mmlu_12568` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12569` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12570` | `mcq` | true | `B` | `B. Leiter–R` |
| baseline | `mmlu_12571` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12572` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12573` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12574` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12575` | `mcq` | false | `C` | `D. alliance` |
| baseline | `mmlu_12576` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12577` | `mcq` | true | `B` | `B. 3-6 years` |
| baseline | `mmlu_12578` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12579` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12580` | `mcq` | true | `A` | `A. emic` |
| baseline | `mmlu_12581` | `mcq` | true | `C` | `C. includes both measured (observed) attributes and latent traits.` |
| baseline | `mmlu_12582` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12583` | `mcq` | true | `B` | `B. Goodness of fit` |
| baseline | `mmlu_12584` | `mcq` | false | `B` | `C. solution-focused` |
| baseline | `mmlu_12585` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12586` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12587` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12588` | `mcq` | true | `B` | `B. Obedience` |
| baseline | `mmlu_12589` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12590` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12591` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12592` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12593` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12594` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12595` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12596` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12597` | `mcq` | true | `B` | `B. adverse impact.` |
| baseline | `mmlu_12598` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12599` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12600` | `mcq` | true | `C` | `C. protecting the public welfare.` |
| baseline | `mmlu_12601` | `mcq` | true | `D` | `D. Object permanence` |
| baseline | `mmlu_12602` | `mcq` | true | `C` | `C. Grand mal` |
| baseline | `mmlu_12603` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12604` | `mcq` | true | `D` | `D. Lack of control and insufficient reward` |
| baseline | `mmlu_12605` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12606` | `mcq` | true | `D` | `D. unethically.` |
| baseline | `mmlu_12607` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12608` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12609` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12610` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12611` | `mcq` | false | `B` | `D. Secure` |
| baseline | `mmlu_12612` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12613` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12614` | `mcq` | true | `A` | `A. making new information meaningful` |
| baseline | `mmlu_12615` | `mcq` | false | `A` | `C. dependent` |
| baseline | `mmlu_12616` | `mcq` | true | `A` | `A. illegal and unethical.` |
| baseline | `mmlu_12617` | `mcq` | true | `A` | `A. authoritative.` |
| baseline | `mmlu_12618` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12619` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12620` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12621` | `mcq` | false | `A` | `B. punishment` |
| baseline | `mmlu_12622` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12623` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12624` | `mcq` | false | `A` | `D. handle the issue within the therapeutic situation and thereby maintain confidentiality` |
| baseline | `mmlu_12625` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12626` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12627` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12628` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12629` | `mcq` | false | `D` | `A. high task-orientation and low relationship orientation` |
| baseline | `mmlu_12630` | `mcq` | false | `C` | `D. phenotype` |
| baseline | `mmlu_12631` | `mcq` | false | `A` | `B. Testify` |
| baseline | `mmlu_12632` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12633` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12634` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12635` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12636` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12637` | `mcq` | false | `C` | `B. internal` |
| baseline | `mmlu_12638` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12639` | `mcq` | false | `D` | `B. concurrent validation` |
| baseline | `mmlu_12640` | `mcq` | true | `B` | `B. legitimate power` |
| baseline | `mmlu_12641` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_12642` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12643` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12644` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12645` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12646` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12647` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12648` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12649` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12650` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12651` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_12652` | `mcq` | false | `C` | `B. Insecure avoidant` |
| baseline | `mmlu_12653` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12654` | `mcq` | false | `D` | `C. job analysis` |
| baseline | `mmlu_12655` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12656` | `mcq` | true | `C` | `C. delusional depression` |
| baseline | `mmlu_12657` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12658` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12659` | `mcq` | false | `C` | `B. when compliance is accompanied by a large reward` |
| baseline | `mmlu_12660` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12661` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12662` | `mcq` | true | `A` | `A. blocked potential.` |
| baseline | `mmlu_12663` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12664` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12665` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12666` | `mcq` | true | `A` | `A. state/provincial regulatory boards` |
| baseline | `mmlu_12667` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12668` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12669` | `mcq` | true | `D` | `D. less than 5 seconds.` |
| baseline | `mmlu_12670` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12671` | `mcq` | true | `D` | `D. increase` |
| baseline | `mmlu_12672` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12673` | `mcq` | true | `B` | `B. acetylcholine` |
| baseline | `mmlu_12674` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12675` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12676` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12677` | `mcq` | false | `B` | `D. The probability of type I and type II errors cannot be computed from the information given.` |
| baseline | `mmlu_12678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12679` | `mcq` | true | `D` | `D. Prader-Willi syndrome` |
| baseline | `mmlu_12680` | `mcq` | true | `C` | `C. Dysprosody` |
| baseline | `mmlu_12681` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_12682` | `mcq` | false | `A` | `D. electric shock` |
| baseline | `mmlu_12683` | `mcq` | true | `B` | `B. age is a bona fide occupational requirement` |
| baseline | `mmlu_12684` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12685` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12686` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12687` | `mcq` | false | `B` | `A. Event` |
| baseline | `mmlu_12688` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12689` | `mcq` | false | `A` | `B. two` |
| baseline | `mmlu_12690` | `mcq` | true | `C` | `C. Resistance and immersion` |
| baseline | `mmlu_12691` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12692` | `mcq` | false | `A` | `B. homophobia.` |
| baseline | `mmlu_12693` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12694` | `mcq` | true | `A` | `A. measure of agreement between 2 raters using nominal scales` |
| baseline | `mmlu_12695` | `mcq` | true | `D` | `D. solution-focused` |
| baseline | `mmlu_12696` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12697` | `mcq` | true | `B` | `B. increases` |
| baseline | `mmlu_12698` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12699` | `mcq` | true | `A` | `A. Physiological tolerance and withdrawal` |
| baseline | `mmlu_12700` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12701` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12702` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12703` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12704` | `mcq` | true | `B` | `B. Productivity` |
| baseline | `mmlu_12705` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12706` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12707` | `mcq` | false | `C` | `A. Working` |
| baseline | `mmlu_12708` | `mcq` | true | `A` | `A. deindividuation.` |
| baseline | `mmlu_12709` | `mcq` | true | `A` | `A. sleeping` |
| baseline | `mmlu_12710` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12711` | `mcq` | true | `D` | `D. The children should not be included in the study` |
| baseline | `mmlu_12712` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12713` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12714` | `mcq` | true | `D` | `D. allow the student to withdraw from the study.` |
| baseline | `mmlu_12715` | `mcq` | false | `B` | `C. longitudinal` |
| baseline | `mmlu_12716` | `mcq` | true | `C` | `C. Choroid plexus` |
| baseline | `mmlu_12717` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12718` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12719` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_12720` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12721` | `mcq` | true | `B` | `B. the effects of one variable are contingent on the level of the second variable.` |
| baseline | `mmlu_12722` | `mcq` | false | `A` | `D. charismatic` |
| baseline | `mmlu_12723` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12724` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12725` | `mcq` | false | `B` | `D. as close to the point of reinforcements possible` |
| baseline | `mmlu_12726` | `mcq` | false | `D` | `C. disjunctive` |
| baseline | `mmlu_12727` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12728` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12729` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12730` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12731` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12732` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12733` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12734` | `mcq` | true | `C` | `C. Sexual selection and parental investment` |
| baseline | `mmlu_12735` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12736` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12737` | `mcq` | true | `C` | `C. demand characteristics` |
| baseline | `mmlu_12738` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12739` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12740` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12741` | `mcq` | true | `A` | `A. perceptions of his/her own contribution/reward ratio and the ratio of his/her partner.` |
| baseline | `mmlu_12742` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12743` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12744` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12745` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12746` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12747` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12748` | `mcq` | false | `B` | `D. as long as no other information about the treatment is given to the supervisor.` |
| baseline | `mmlu_12749` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12750` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12751` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12752` | `mcq` | false | `C` | `B. Send the records as requested` |
| baseline | `mmlu_12753` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12754` | `mcq` | true | `B` | `B. must appear at the deposition as requested.` |
| baseline | `mmlu_12755` | `mcq` | false | `C` | `A. overjustification hypothesis` |
| baseline | `mmlu_12756` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12757` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12758` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12759` | `mcq` | true | `D` | `D. symptom` |
| baseline | `mmlu_12760` | `mcq` | false | `D` | `C. "the message is within his “latitude of acceptance."""` |
| baseline | `mmlu_12761` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12762` | `mcq` | true | `B` | `B. Social learning` |
| baseline | `mmlu_12763` | `mcq` | false | `C` | `B. 5 to 7` |
| baseline | `mmlu_12764` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12765` | `mcq` | false | `C` | `A. Young ethnic minority women` |
| baseline | `mmlu_12766` | `mcq` | true | `B` | `B. the predictor has an inverse relationship with the criterion.` |
| baseline | `mmlu_12767` | `mcq` | true | `A` | `A. Point-biserial` |
| baseline | `mmlu_12768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12769` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12770` | `mcq` | false | `C` | `B. use of control or comparison groups` |
| baseline | `mmlu_12771` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12772` | `mcq` | false | `A` | `D. Pain` |
| baseline | `mmlu_12773` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12774` | `mcq` | false | `C` | `D. Multiple-choice` |
| baseline | `mmlu_12775` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12776` | `mcq` | true | `B` | `B. superordinate goals` |
| baseline | `mmlu_12777` | `mcq` | true | `A` | `A. mesosystem` |
| baseline | `mmlu_12778` | `mcq` | true | `B` | `B. interpretations of the data and limiting circumstances involving the test administration` |
| baseline | `mmlu_12779` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12780` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12781` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12782` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12783` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12784` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12785` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12786` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12787` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12788` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12789` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12790` | `mcq` | true | `A` | `A. job satisfaction` |
| baseline | `mmlu_12791` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12792` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12793` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12794` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12795` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12796` | `mcq` | true | `C` | `C. parietal cortex` |
| baseline | `mmlu_12797` | `mcq` | true | `D` | `D. learning and memory` |
| baseline | `mmlu_12798` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12799` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12800` | `mcq` | false | `C` | `D. adults who are mentally retarded.` |
| baseline | `mmlu_12801` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12802` | `mcq` | true | `D` | `D. listed as an author` |
| baseline | `mmlu_12803` | `mcq` | false | `C` | `D. Throughout the life span` |
| baseline | `mmlu_12804` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12805` | `mcq` | false | `C` | `D. Secure` |
| baseline | `mmlu_12806` | `mcq` | false | `C` | `D. Interpersonal therapy` |
| baseline | `mmlu_12807` | `mcq` | false | `A` | `D. Consistency` |
| baseline | `mmlu_12808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12809` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12810` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12811` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12812` | `mcq` | true | `B` | `B. They can lead to dependence` |
| baseline | `mmlu_12813` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12814` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12815` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12816` | `mcq` | false | `B` | `D. Household Responsibilities` |
| baseline | `mmlu_12817` | `mcq` | true | `C` | `C. scripts` |
| baseline | `mmlu_12818` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12819` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12820` | `mcq` | false | `D` | `A. stimulus control` |
| baseline | `mmlu_12821` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12822` | `mcq` | false | `C` | `B. 0.15` |
| baseline | `mmlu_12823` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12824` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12825` | `mcq` | false | `B` | `C. treat this as an instance of resistance` |
| baseline | `mmlu_12826` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12827` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12828` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12829` | `mcq` | true | `C` | `C. how temperamental style and the environment work together to determine later development` |
| baseline | `mmlu_12830` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12831` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12832` | `mcq` | false | `D` | `B. An objective personality inventory` |
| baseline | `mmlu_12833` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12834` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12835` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12836` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12837` | `mcq` | false | `A` | `D. productivity` |
| baseline | `mmlu_12838` | `mcq` | false | `C` | `B. allows the therapist to control the client's behavior` |
| baseline | `mmlu_12839` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12840` | `mcq` | true | `B` | `B. equally effective` |
| baseline | `mmlu_12841` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12842` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12843` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12844` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12845` | `mcq` | true | `C` | `C. increasing nonproductive motor activity` |
| baseline | `mmlu_12846` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12847` | `mcq` | true | `A` | `A. It compares to means from unrelated samples` |
| baseline | `mmlu_12848` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12849` | `mcq` | true | `B` | `B. integrate the various aspects of the self.` |
| baseline | `mmlu_12850` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12851` | `mcq` | false | `D` | `C. Addison's disease` |
| baseline | `mmlu_12852` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12853` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12855` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12856` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12857` | `mcq` | true | `A` | `A. airline pilot` |
| baseline | `mmlu_12858` | `mcq` | true | `C` | `C. confirm his negative self-evaluations.` |
| baseline | `mmlu_12859` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12860` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12861` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_12862` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12863` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_12864` | `mcq` | true | `D` | `D. Results` |
| baseline | `mmlu_12865` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12866` | `mcq` | true | `B` | `B. thalamus` |
| baseline | `mmlu_12867` | `mcq` | true | `C` | `C. Correlational Research` |
| baseline | `mmlu_12868` | `mcq` | true | `B` | `B. Binet–Simon Scale` |
| baseline | `mmlu_12869` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12870` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12871` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12872` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12873` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12874` | `mcq` | false | `C` | `A. Clerical` |
| baseline | `mmlu_12875` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12876` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12877` | `mcq` | true | `B` | `B. Developmental trajectory` |
| baseline | `mmlu_12878` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12879` | `mcq` | false | `C` | `A. English` |
| baseline | `mmlu_12880` | `mcq` | false | `B` | `A. All Verbal subtests` |
| baseline | `mmlu_12881` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12882` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12883` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_12884` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12885` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12886` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12887` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_12888` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12889` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12890` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12891` | `mcq` | true | `D` | `D. acknowledging the limits of their data or conclusions` |
| baseline | `mmlu_12892` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12893` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12894` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12895` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12896` | `mcq` | false | `B` | `C. 130` |
| baseline | `mmlu_12897` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12898` | `mcq` | true | `B` | `B. Cognitive Assessment System` |
| baseline | `mmlu_12899` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12900` | `mcq` | true | `C` | `C. cervical` |
| baseline | `mmlu_12901` | `mcq` | false | `D` | `C. decrease in vocabulary` |
| baseline | `mmlu_12902` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12903` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12904` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_12905` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12906` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12907` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_12908` | `mcq` | false | `C` | `D. Lying` |
| baseline | `mmlu_12909` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12910` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12911` | `mcq` | false | `B` | `A. talk for longer periods of time.` |
| baseline | `mmlu_12912` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12913` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12914` | `mcq` | true | `C` | `C. Skills and willingness to assume responsibility.` |
| baseline | `mmlu_12915` | `mcq` | true | `B` | `B. the client.` |
| baseline | `mmlu_12916` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12917` | `mcq` | true | `D` | `D. allow the student to withdraw from the study.` |
| baseline | `mmlu_12918` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12919` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12920` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12921` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12922` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12923` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_12924` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12925` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12926` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12927` | `mcq` | false | `C` | `A. 7` |
| baseline | `mmlu_12928` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12929` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_12930` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12931` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12932` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12933` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_12934` | `mcq` | false | `B` | `C. median` |
| baseline | `mmlu_12935` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12936` | `mcq` | false | `B` | `A. Self-regulating psyche, the unconscious, family, therapist–patient relationship` |
| baseline | `mmlu_12937` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12938` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12939` | `mcq` | false | `C` | `A. content` |
| baseline | `mmlu_12940` | `mcq` | true | `C` | `C. see the clients and obtain supervision or consultation by telephone.` |
| baseline | `mmlu_12941` | `mcq` | false | `A` | `B. Conditioning` |
| baseline | `mmlu_12942` | `mcq` | false | `A` | `D. advise the attorney who issued the subpoena that he cannot appear as requested because the client has not given him p` |
| baseline | `mmlu_12943` | `mcq` | true | `D` | `D. using professional judgment to select from among the tests or combinations of tests, depending upon the goals of the ` |
| baseline | `mmlu_12944` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12945` | `mcq` | false | `A` | `B. CS` |
| baseline | `mmlu_12946` | `mcq` | true | `B` | `B. The private sector` |
| baseline | `mmlu_12947` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_12948` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12949` | `mcq` | true | `D` | `D. empathy` |
| baseline | `mmlu_12950` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12951` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_12952` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_12953` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12954` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_12955` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12956` | `mcq` | false | `B` | `A. Striate cortex` |
| baseline | `mmlu_12957` | `mcq` | true | `B` | `B. Apraxia` |
| baseline | `mmlu_12958` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_12959` | `mcq` | false | `C` | `A. Cocaine` |
| baseline | `mmlu_12960` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12961` | `mcq` | false | `B` | `A. Causality, generalizability` |
| baseline | `mmlu_12962` | `mcq` | true | `C` | `C. stability` |
| baseline | `mmlu_12963` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12964` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_12965` | `mcq` | true | `D` | `D. Initiative vs. Guilt.` |
| baseline | `mmlu_12966` | `mcq` | true | `B` | `B. raise for discussion the possibility of termination and referral to another therapist.` |
| baseline | `mmlu_12967` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12968` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12969` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12970` | `mcq` | true | `A` | `A. when reversal is not possible` |
| baseline | `mmlu_12971` | `mcq` | true | `C` | `C.	display genuine interest in the client by asking about his/her family and work or school.` |
| baseline | `mmlu_12972` | `mcq` | true | `D` | `D. not release any information to the mother without appropriate authorization.` |
| baseline | `mmlu_12973` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12974` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12975` | `mcq` | false | `B` | `C. brain stem` |
| baseline | `mmlu_12976` | `mcq` | true | `D` | `D. close and conflictual.` |
| baseline | `mmlu_12977` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_12978` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_12979` | `mcq` | true | `A` | `A. decrease the anonymity of individuals in the community` |
| baseline | `mmlu_12980` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_12981` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_12982` | `mcq` | true | `B` | `B. the client.` |
| baseline | `mmlu_12983` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_12984` | `mcq` | true | `B` | `B. redesign the job to provide a challenge and a sense of accomplishment` |
| baseline | `mmlu_12985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12986` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12987` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12988` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_12989` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_12990` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_12991` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_12992` | `mcq` | false | `D` | `B. severity of symptoms` |
| baseline | `mmlu_12993` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12994` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_12995` | `mcq` | false | `C` | `A. reintegration` |
| baseline | `mmlu_12996` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_12997` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_12998` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_12999` | `mcq` | false | `A` | `B` |
