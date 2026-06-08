# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 183 / 500 | 0.3660 | 9.9602 | 0.177070 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_10500` | `mcq` | true | `A` | `A. Due care.` |
| baseline | `mmlu_10501` | `mcq` | false | `B` | `D. $3,200` |
| baseline | `mmlu_10502` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10503` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10504` | `mcq` | true | `D` | `D. $60,000 is released.` |
| baseline | `mmlu_10505` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10506` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10507` | `mcq` | true | `C` | `C. Scienter and justifiable reliance.` |
| baseline | `mmlu_10508` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10509` | `mcq` | false | `A` | `C. $8,400` |
| baseline | `mmlu_10510` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10511` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10512` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10513` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10514` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10515` | `mcq` | false | `B` | `A. $4,000 loss.` |
| baseline | `mmlu_10516` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10517` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10518` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10519` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10520` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10521` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10522` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10523` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10524` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10526` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10527` | `mcq` | false | `C` | `D. $50,000 capital loss.` |
| baseline | `mmlu_10528` | `mcq` | true | `C` | `C. $0 $100000 - $150000` |
| baseline | `mmlu_10529` | `mcq` | true | `C` | `C. $375,000` |
| baseline | `mmlu_10530` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10531` | `mcq` | false | `A` | `C. Request the client's management to document the matter in the management representation letter.` |
| baseline | `mmlu_10532` | `mcq` | true | `C` | `C. $150,000` |
| baseline | `mmlu_10533` | `mcq` | true | `A` | `A. Theory of constraints.` |
| baseline | `mmlu_10534` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10535` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10536` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10537` | `mcq` | true | `B` | `B. $25,000` |
| baseline | `mmlu_10538` | `mcq` | false | `A` | `D. $9.60` |
| baseline | `mmlu_10539` | `mcq` | false | `B` | `A. $6000 loss.` |
| baseline | `mmlu_10540` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10541` | `mcq` | false | `C` | `D. 1.5` |
| baseline | `mmlu_10542` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10543` | `mcq` | false | `A` | `C. $26,000` |
| baseline | `mmlu_10544` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10545` | `mcq` | true | `C` | `C. 1200` |
| baseline | `mmlu_10546` | `mcq` | false | `B` | `D. $1,500,000.00` |
| baseline | `mmlu_10547` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10548` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10549` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10550` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10551` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10552` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10553` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10554` | `mcq` | false | `A` | `C. $1,800` |
| baseline | `mmlu_10555` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10556` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10557` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10558` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10559` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10560` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10561` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10562` | `mcq` | true | `C` | `C. $190` |
| baseline | `mmlu_10563` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10564` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10565` | `mcq` | true | `B` | `B. $18.75` |
| baseline | `mmlu_10566` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10567` | `mcq` | true | `A` | `A. Yes Yes` |
| baseline | `mmlu_10568` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10569` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10570` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10571` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10572` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10573` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10574` | `mcq` | true | `C` | `C. $430,000` |
| baseline | `mmlu_10575` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10576` | `mcq` | false | `D` | `C. $5,000` |
| baseline | `mmlu_10577` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10578` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10579` | `mcq` | true | `D` | `D. 13.53 percent.` |
| baseline | `mmlu_10580` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10581` | `mcq` | true | `B` | `B. $27,400` |
| baseline | `mmlu_10582` | `mcq` | false | `D` | `C. -21%` |
| baseline | `mmlu_10583` | `mcq` | false | `D` | `B. $220,000` |
| baseline | `mmlu_10584` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10585` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10586` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10587` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10588` | `mcq` | false | `C` | `B. Increase Decrease` |
| baseline | `mmlu_10589` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10590` | `mcq` | false | `A` | `C. $13,000` |
| baseline | `mmlu_10591` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10592` | `mcq` | true | `C` | `C. 2` |
| baseline | `mmlu_10593` | `mcq` | true | `A` | `A. Identify the types of potential misstatements that could occur.` |
| baseline | `mmlu_10594` | `mcq` | false | `A` | `C. $283,000` |
| baseline | `mmlu_10595` | `mcq` | false | `B` | `D. 6.60%` |
| baseline | `mmlu_10596` | `mcq` | true | `D` | `D. $0 $75000` |
| baseline | `mmlu_10597` | `mcq` | true | `C` | `C. $100` |
| baseline | `mmlu_10598` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10599` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10600` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10601` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10602` | `mcq` | false | `B` | `D. $17,000` |
| baseline | `mmlu_10603` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10604` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10605` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10606` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10607` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10608` | `mcq` | false | `D` | `C. $13,800` |
| baseline | `mmlu_10609` | `mcq` | true | `B` | `B. Yes No` |
| baseline | `mmlu_10610` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10611` | `mcq` | false | `B` | `C. $20,000` |
| baseline | `mmlu_10612` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10613` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10614` | `mcq` | true | `A` | `A. Arrangements regarding fees and billing.` |
| baseline | `mmlu_10615` | `mcq` | true | `A` | `A. Fair value.` |
| baseline | `mmlu_10616` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10617` | `mcq` | true | `B` | `B. 9.6 percent; 13.2 percent` |
| baseline | `mmlu_10618` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10619` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10620` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10621` | `mcq` | true | `D` | `D. $13,000` |
| baseline | `mmlu_10622` | `mcq` | false | `B` | `D. $200,000` |
| baseline | `mmlu_10623` | `mcq` | false | `D` | `B. $25,000` |
| baseline | `mmlu_10624` | `mcq` | false | `A` | `B. Increases Decreases` |
| baseline | `mmlu_10625` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10626` | `mcq` | true | `C` | `C. Rigg Steele and Urco.` |
| baseline | `mmlu_10627` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10628` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10629` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10630` | `mcq` | false | `B` | `D. No Yes` |
| baseline | `mmlu_10631` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10632` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10633` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10634` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10635` | `mcq` | false | `B` | `A. He intended to kill the friend and not the daughter.` |
| baseline | `mmlu_10636` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10637` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10638` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10639` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10640` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10641` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10642` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10643` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10644` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10645` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10646` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10647` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10648` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10649` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10650` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10651` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10652` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10653` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10654` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10655` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10656` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10657` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10658` | `mcq` | false | `C` | `No, because the insurance adjuster did not have a fiduciary relationship requiring him to protect the pedestrian's inter` |
| baseline | `mmlu_10659` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10660` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10661` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10662` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10663` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10664` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10665` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10666` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10667` | `mcq` | false | `A` | `C. $45,000. 00` |
| baseline | `mmlu_10668` | `mcq` | false | `D` | `C. Microhard is entitled to continue their lease because Maximum had actual notice of their prior lease.` |
| baseline | `mmlu_10669` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10670` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10671` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10672` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10673` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10674` | `mcq` | true | `C` | `C. No, the ordinance is void on its face.` |
| baseline | `mmlu_10675` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10676` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10677` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10678` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10679` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10680` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10681` | `mcq` | false | `C` | `B. win, because land is unique, making the legal remedy inadequate.` |
| baseline | `mmlu_10682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10683` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10684` | `mcq` | false | `B` | `No, because the parties stipulated to a verdict from a jury of fewer than six jurors.` |
| baseline | `mmlu_10685` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10686` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10687` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10688` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10689` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10690` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10691` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10692` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10693` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10694` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10695` | `mcq` | false | `C` | `A. Yes, the declaratory relief would interfere with existing state prosecutions and would therefore be disallowed for re` |
| baseline | `mmlu_10696` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10697` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10698` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10699` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10700` | `mcq` | false | `C` | `D. He can be convicted of both larceny and criminal mischief.` |
| baseline | `mmlu_10701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10702` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10703` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10704` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_10705` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_10706` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10707` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10708` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10709` | `mcq` | false | `D` | `C. not guilty, because the commission member did not receive a thing of value, since he would have approved the variance` |
| baseline | `mmlu_10710` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10711` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10712` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10713` | `mcq` | true | `C` | `C. Yes, because his statements to the farmer did not constitute a promise to forgo any cause of action he then had or mi` |
| baseline | `mmlu_10714` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10715` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10716` | `mcq` | true | `B` | `B. No, unless the court finds, in the interests of justice, that the probative value of the conviction, supported by spe` |
| baseline | `mmlu_10717` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10718` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10719` | `mcq` | false | `A` | `D. No, because there was inadequate consideration for the covenant.` |
| baseline | `mmlu_10720` | `mcq` | false | `A` | `B. The investor.` |
| baseline | `mmlu_10721` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10722` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10723` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10724` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10725` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10726` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10727` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10728` | `mcq` | false | `D` | `No, the plaintiff clearly assumed the risk by entering a dangerous loading/unloading area.` |
| baseline | `mmlu_10729` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10730` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10731` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10732` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10733` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10734` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10735` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10736` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10737` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10738` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10739` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10740` | `mcq` | true | `C` | `C. Yes, because it is authorized by a valid treaty of the United States and is not prohibited by any provision of the Co` |
| baseline | `mmlu_10741` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10742` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10743` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10744` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10745` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10746` | `mcq` | false | `A` | `C. No, because owner owes no duty to trespassers except if it acts with willful or wanton disregard.` |
| baseline | `mmlu_10747` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10748` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10749` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10750` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10751` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10752` | `mcq` | true | `D` | `D. No, because the modifying contract was not in writing; it was, therefore, unenforceable under the UCC.` |
| baseline | `mmlu_10753` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10754` | `mcq` | true | `D` | `D. Yes, under the rule of apparent agency.` |
| baseline | `mmlu_10755` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10756` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10757` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10758` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10759` | `mcq` | false | `C` | `A. because the tenant discontinued paying rent following the landowner's death.` |
| baseline | `mmlu_10760` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10761` | `mcq` | true | `A` | `A. No, because even though the wife is a willing witness, the defendant has the right to exclude confidential marital co` |
| baseline | `mmlu_10762` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10763` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10764` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10765` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10766` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10767` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10768` | `mcq` | true | `D` | `D. No, the plaintiff is a citizen of New York and the three members of the LLC are each from a different state, which gi` |
| baseline | `mmlu_10769` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10770` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10771` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10772` | `mcq` | false | `A` | `B. dismiss the suit because the resident lacks standing.` |
| baseline | `mmlu_10773` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10774` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10775` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10776` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10777` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10778` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10779` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10780` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10781` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10782` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10783` | `mcq` | false | `C` | `No, because the facts indicate that he wasn't too intoxicated to form the necessary intent for burglary.` |
| baseline | `mmlu_10784` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10785` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10786` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10787` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10788` | `mcq` | true | `C` | `C. No, a conspiracy would have required that the gun dealer go to the bank with the friend.` |
| baseline | `mmlu_10789` | `mcq` | true | `C` | `C. The seller is entitled to $10,000, because the collector accepted delivery of the coin.` |
| baseline | `mmlu_10790` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10791` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10792` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10793` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10794` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10795` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10796` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10797` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10798` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10799` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10800` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10801` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10802` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10803` | `mcq` | true | `C` | `C. Yes, because her testimony is relevant to the mental state necessary for the commission of the crime.` |
| baseline | `mmlu_10804` | `mcq` | false | `B` | `C. No, because the man received the letter on May 4.` |
| baseline | `mmlu_10805` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10806` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10807` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10808` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10809` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10810` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10811` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10812` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10813` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10814` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10815` | `mcq` | true | `B` | `B. win, because either daughter has the right of re-entry for condition broken.` |
| baseline | `mmlu_10816` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10817` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10818` | `mcq` | false | `B` | `No, because the Eleventh Amendment does not bar actions brought by the United States.` |
| baseline | `mmlu_10819` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10820` | `mcq` | true | `C` | `C. No, because the painter works for the same company as the negligent workers, and he made his statements within the sc` |
| baseline | `mmlu_10821` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10822` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10823` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10824` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10825` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10826` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10827` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10828` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10829` | `mcq` | true | `D` | `D. Yes, because the restriction is binding on the daughter as a successor.` |
| baseline | `mmlu_10830` | `mcq` | true | `C` | `C. Attempted robbery.` |
| baseline | `mmlu_10831` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10832` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10833` | `mcq` | false | `C` | `B. vicarious liability.` |
| baseline | `mmlu_10834` | `mcq` | false | `B` | `No, because there was publication of the recorded conversations.` |
| baseline | `mmlu_10835` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10836` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10837` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10838` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10839` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10840` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10841` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10842` | `mcq` | false | `A` | `C. Yes, because the contractor reasonably relied on the homeowner's contractual promise to pay the full $50,000, and tha` |
| baseline | `mmlu_10843` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10844` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10845` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10846` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10847` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10848` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10849` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10850` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_10851` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10852` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10853` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10854` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10855` | `mcq` | true | `C` | `C. No, legal impossibility is not a defense to the crime of conspiracy.` |
| baseline | `mmlu_10856` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10857` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10858` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10859` | `mcq` | true | `A` | `A. Service as required by State B's rules of civil procedure.` |
| baseline | `mmlu_10860` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10861` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10862` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10863` | `mcq` | true | `C` | `C. No, the court will preclude the entrance of the deficiency judgment because the limitation clause is still enforceabl` |
| baseline | `mmlu_10864` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10865` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10866` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10867` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10868` | `mcq` | true | `A` | `A. violation of procedural due process.` |
| baseline | `mmlu_10869` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10870` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10871` | `mcq` | false | `C` | `No, because it would tend to confuse the jury with too much conflicting evidence.` |
| baseline | `mmlu_10872` | `mcq` | false | `B` | `No, because the jury could have found that the president's conduct was sufficiently reckless to constitute murder.` |
| baseline | `mmlu_10873` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10874` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10875` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10876` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10877` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10878` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10879` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10880` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10881` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10882` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10883` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10884` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10885` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10886` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10887` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10888` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10889` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10890` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10891` | `mcq` | false | `C` | `A. No, because the statement is clearly hearsay with no exception to the hearsay rule being applicable.` |
| baseline | `mmlu_10892` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10893` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10894` | `mcq` | true | `C` | `C. No, because the elevator was under the owner's exclusive control and accidents of this nature do not ordinarily occur` |
| baseline | `mmlu_10895` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10896` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10897` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10898` | `mcq` | false | `D` | `C. Yes, because they were accessions.` |
| baseline | `mmlu_10899` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10900` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10901` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10902` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10903` | `mcq` | false | `C` | `B. $10,000 plus the amount due for 85 percent of the completed work on the town beach house.` |
| baseline | `mmlu_10904` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10905` | `mcq` | false | `C` | `B. Voluntary manslaughter.` |
| baseline | `mmlu_10906` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10907` | `mcq` | false | `B` | `No, because there is no diversity of citizenship between the shop owner and the wholesaler.` |
| baseline | `mmlu_10908` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10909` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10910` | `mcq` | false | `C` | `A. valid, because the city can demonstrate that the school fee is necessary to further a compelling governmental interes` |
| baseline | `mmlu_10911` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10912` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10913` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10914` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10915` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10916` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10917` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10918` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_10919` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10920` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10921` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10922` | `mcq` | false | `B` | `A. negative easement.` |
| baseline | `mmlu_10923` | `mcq` | false | `A` | `D. Yes, a bar against the right to receive proceeds is a favored restriction unless otherwise stated.` |
| baseline | `mmlu_10924` | `mcq` | true | `A` | `A. Yes, his use of a deadly weapon demonstrated the requisite intent to kill.` |
| baseline | `mmlu_10925` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10926` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10927` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10928` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10929` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10930` | `mcq` | true | `A` | `A. Seek a new trial, because the jury instruction affected the protester's substantial rights.` |
| baseline | `mmlu_10931` | `mcq` | false | `C` | `No, because a dismissal with prejudice operates as a judgment on the merits.` |
| baseline | `mmlu_10932` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10933` | `mcq` | false | `A` | `D. No crime.` |
| baseline | `mmlu_10934` | `mcq` | true | `D` | `D. not recover.` |
| baseline | `mmlu_10935` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10936` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10937` | `mcq` | false | `B` | `C. No, because the offer expressly limited the acceptance to the terms of the offer.` |
| baseline | `mmlu_10938` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10939` | `mcq` | false | `D` | `A. Yes, because the scientist was engaged in an abnormally dangerous activity by transporting highly flammable petroleum` |
| baseline | `mmlu_10940` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10941` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10942` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10943` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10944` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10945` | `mcq` | false | `B` | `No, the jury's award is discretionary and inviolate, and it may not be disturbed with respect to personal injury damages` |
| baseline | `mmlu_10946` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10947` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10948` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10949` | `mcq` | false | `B` | `No, because the neighbor was trespassing.` |
| baseline | `mmlu_10950` | `mcq` | false | `B` | `No, because the company did not intend to cause the graduate to suffer severe emotional distress.` |
| baseline | `mmlu_10951` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10952` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10953` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10954` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10955` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10956` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10957` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10958` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10959` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10960` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10961` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10962` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10963` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10964` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10965` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10966` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10967` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10968` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10969` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10970` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10971` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10972` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10973` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10974` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10975` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10976` | `mcq` | false | `B` | `No, because a determination of the sufficiency of the evidence is solely within the jury's province.` |
| baseline | `mmlu_10977` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10978` | `mcq` | false | `C` | `A. No, despite the expert testimony, anticipated profits for a new company are too speculative and are not awarded.` |
| baseline | `mmlu_10979` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10980` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10981` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10982` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10983` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10984` | `mcq` | false | `A` | `No, because there is no evidence that the facility owner and the solvent supplier acted in concert.` |
| baseline | `mmlu_10985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10986` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10987` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10988` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10989` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10990` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10991` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10992` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10993` | `mcq` | true | `A` | `A. No, because the treatise excerpts were not offered during the examination of a qualified expert.` |
| baseline | `mmlu_10994` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10995` | `mcq` | false | `A` | `D. No, because a defamation action cannot be subject to a motion to dismiss ` |
| baseline | `mmlu_10996` | `mcq` | false | `D` | `No, because she had a property right in her license and permits, which were taken without any procedural due process.` |
| baseline | `mmlu_10997` | `mcq` | true | `A` | `A. Yes, because the wording of the instruction could have been viewed by jurors as a mandatory direction to find that th` |
| baseline | `mmlu_10998` | `mcq` | true | `A` | `A. Yes, a business will be liable for known conditions in the building or adjoining parking areas that are a danger to t` |
| baseline | `mmlu_10999` | `mcq` | false | `C` | `D` |
