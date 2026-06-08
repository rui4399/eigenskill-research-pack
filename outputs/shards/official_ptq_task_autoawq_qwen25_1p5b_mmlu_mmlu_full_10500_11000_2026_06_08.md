# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 193 / 500 | 0.3860 | 9.9300 | 0.166629 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_10500` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10501` | `mcq` | false | `B` | `A. $533` |
| baseline | `mmlu_10502` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10503` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10504` | `mcq` | true | `D` | `D. $60,000 is released.` |
| baseline | `mmlu_10505` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10506` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10507` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10508` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10509` | `mcq` | true | `A` | `A. $4,000` |
| baseline | `mmlu_10510` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10511` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10512` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10514` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10515` | `mcq` | false | `B` | `A. $4,000 loss.` |
| baseline | `mmlu_10516` | `mcq` | false | `D` | `B. Rose only.` |
| baseline | `mmlu_10517` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10518` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10519` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10520` | `mcq` | false | `A` | `C. 6.98%` |
| baseline | `mmlu_10521` | `mcq` | false | `B` | `C. $14,000` |
| baseline | `mmlu_10522` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10523` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10524` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10525` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10526` | `mcq` | false | `D` | `A. 0.24` |
| baseline | `mmlu_10527` | `mcq` | false | `C` | `B. $35,000 capital loss.` |
| baseline | `mmlu_10528` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10529` | `mcq` | true | `C` | `C. $375,000` |
| baseline | `mmlu_10530` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10531` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10532` | `mcq` | true | `C` | `C. $150,000` |
| baseline | `mmlu_10533` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10534` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10535` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10536` | `mcq` | false | `A` | `C. 3.40%` |
| baseline | `mmlu_10537` | `mcq` | true | `B` | `B. $25,000` |
| baseline | `mmlu_10538` | `mcq` | false | `A` | `B. $6.11` |
| baseline | `mmlu_10539` | `mcq` | false | `B` | `D. $6000 gain.` |
| baseline | `mmlu_10540` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10541` | `mcq` | true | `C` | `C. 1.125` |
| baseline | `mmlu_10542` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10543` | `mcq` | false | `A` | `C. $26,000` |
| baseline | `mmlu_10544` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10545` | `mcq` | true | `C` | `C. 1200` |
| baseline | `mmlu_10546` | `mcq` | false | `B` | `A. $3,750,000.00` |
| baseline | `mmlu_10547` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10548` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10549` | `mcq` | false | `D` | `C. 4.00%` |
| baseline | `mmlu_10550` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10551` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10552` | `mcq` | true | `D` | `D. downward sloping` |
| baseline | `mmlu_10553` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10554` | `mcq` | false | `A` | `B. $1,600` |
| baseline | `mmlu_10555` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10556` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10557` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10558` | `mcq` | false | `B` | `C. $7,000` |
| baseline | `mmlu_10559` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10560` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10561` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10562` | `mcq` | true | `C` | `C. $190` |
| baseline | `mmlu_10563` | `mcq` | false | `C` | `A. $2,005,000` |
| baseline | `mmlu_10564` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10565` | `mcq` | true | `B` | `B. $18.75` |
| baseline | `mmlu_10566` | `mcq` | true | `B` | `B. 8%` |
| baseline | `mmlu_10567` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10568` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10569` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10570` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10571` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10572` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10573` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10574` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10575` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10576` | `mcq` | false | `D` | `B. $8,250` |
| baseline | `mmlu_10577` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10578` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10579` | `mcq` | false | `D` | `C. 26.5 percent.` |
| baseline | `mmlu_10580` | `mcq` | true | `D` | `D. Expensed as incurred in the current period` |
| baseline | `mmlu_10581` | `mcq` | true | `B` | `B. $27,400` |
| baseline | `mmlu_10582` | `mcq` | false | `D` | `B. 23%` |
| baseline | `mmlu_10583` | `mcq` | false | `D` | `A. $140,000` |
| baseline | `mmlu_10584` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10585` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10586` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10587` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10588` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10589` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10590` | `mcq` | true | `A` | `A. $9,000` |
| baseline | `mmlu_10591` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10592` | `mcq` | false | `C` | `B. 1.5` |
| baseline | `mmlu_10593` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10594` | `mcq` | false | `A` | `C. $283,000` |
| baseline | `mmlu_10595` | `mcq` | false | `B` | `D. 6.60%` |
| baseline | `mmlu_10596` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10597` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10598` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10599` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10600` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10601` | `mcq` | false | `B` | `A. $26.1 million` |
| baseline | `mmlu_10602` | `mcq` | false | `B` | `D. $17,000` |
| baseline | `mmlu_10603` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10604` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10605` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10606` | `mcq` | true | `B` | `B. 16.7 percent` |
| baseline | `mmlu_10607` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10608` | `mcq` | false | `D` | `C. $13,800` |
| baseline | `mmlu_10609` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10610` | `mcq` | true | `A` | `A. Notes to the financial statements.` |
| baseline | `mmlu_10611` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10612` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10613` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10614` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10615` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10616` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10617` | `mcq` | true | `B` | `B. 9.6 percent; 13.2 percent` |
| baseline | `mmlu_10618` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10619` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10620` | `mcq` | true | `C` | `C. No Net present value is ($750)` |
| baseline | `mmlu_10621` | `mcq` | false | `D` | `A. $27,000` |
| baseline | `mmlu_10622` | `mcq` | false | `B` | `A. $185,000` |
| baseline | `mmlu_10623` | `mcq` | false | `D` | `B. $25,000` |
| baseline | `mmlu_10624` | `mcq` | false | `A` | `B. Increases Decreases` |
| baseline | `mmlu_10625` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10626` | `mcq` | true | `C` | `C. Rigg Steele and Urco.` |
| baseline | `mmlu_10627` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10628` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10629` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10630` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10631` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10632` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10633` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10634` | `mcq` | true | `C` | `C. The authenticating requirement was necessary to further a compelling state interest.` |
| baseline | `mmlu_10635` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10636` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10637` | `mcq` | false | `B` | `C. invalid, because the executive order is beyond the scope of presidential power absent congressional authorization.` |
| baseline | `mmlu_10638` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10639` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10640` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10641` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10642` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10643` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10644` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10645` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10646` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10647` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10648` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10649` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10650` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10651` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10652` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10653` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10654` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10655` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10656` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10657` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10658` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10659` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10660` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10661` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10662` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10663` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10664` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10665` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10666` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10667` | `mcq` | false | `A` | `B. $55,000. 00` |
| baseline | `mmlu_10668` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10669` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10670` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10671` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10672` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10673` | `mcq` | true | `B` | `B. Equal protection problem` |
| baseline | `mmlu_10674` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10675` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10676` | `mcq` | false | `D` | `C. excluded, because his opinion is based upon facts not in evidence.` |
| baseline | `mmlu_10677` | `mcq` | false | `C` | `D. not prevail, because the lawyer was unconscious and unaware of what was happening for most of the confinement period.` |
| baseline | `mmlu_10678` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10679` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10680` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10681` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10683` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10684` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10685` | `mcq` | true | `B` | `B. Bob Wilson and Ted Lamar are liable jointly.` |
| baseline | `mmlu_10686` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10687` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10688` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10689` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10690` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10691` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10692` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10693` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10694` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10695` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10696` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10697` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10698` | `mcq` | false | `B` | `D. Friend // Associate` |
| baseline | `mmlu_10699` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10700` | `mcq` | false | `C` | `D. He can be convicted of both larceny and criminal mischief.` |
| baseline | `mmlu_10701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10702` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10703` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10704` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10705` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10706` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10707` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10708` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10709` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10710` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10711` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10712` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10713` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10714` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10715` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10716` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10717` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10718` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10719` | `mcq` | false | `A` | `D. No, because there was inadequate consideration for the covenant.` |
| baseline | `mmlu_10720` | `mcq` | false | `A` | `B. The investor.` |
| baseline | `mmlu_10721` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10722` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10723` | `mcq` | false | `B` | `C. Yes, because the printing company's shipping of the Thanksgiving cards on October 10 constituted an anticipatory brea` |
| baseline | `mmlu_10724` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10725` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10726` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10727` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10728` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10729` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10730` | `mcq` | true | `C` | `C. Yes, because the shutters had become fixtures.` |
| baseline | `mmlu_10731` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10732` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10733` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10734` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10735` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10736` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10737` | `mcq` | false | `A` | `D. inadmissible, under the Dead Man's Statute.` |
| baseline | `mmlu_10738` | `mcq` | false | `B` | `D. Murder.` |
| baseline | `mmlu_10739` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10740` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10741` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10742` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10743` | `mcq` | false | `C` | `D. not prevail, because specific performance will not be granted where there is an adequate remedy at law.` |
| baseline | `mmlu_10744` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10745` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10746` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10747` | `mcq` | false | `B` | `C. He exercised reasonable care under the circumstances.` |
| baseline | `mmlu_10748` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10749` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10750` | `mcq` | false | `C` | `D. The rule against perpetuities` |
| baseline | `mmlu_10751` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10752` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10753` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10754` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10755` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10756` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10757` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10758` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10759` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10760` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10761` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10762` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10763` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10764` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10765` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10766` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10767` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10768` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10769` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10770` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10771` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10772` | `mcq` | false | `A` | `B. dismiss the suit because the resident lacks standing.` |
| baseline | `mmlu_10773` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10775` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10776` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10777` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10778` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10779` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10780` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10781` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10782` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10783` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10784` | `mcq` | false | `B` | `A. sustain the objection, because the testimony is hearsay.` |
| baseline | `mmlu_10785` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10786` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10787` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10788` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10789` | `mcq` | false | `C` | `A. The collector is entitled to nominal damages, because the coin was received in a damaged condition.` |
| baseline | `mmlu_10790` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10791` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10792` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10793` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10794` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10795` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10796` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10797` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10798` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10799` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10800` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10801` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10802` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_10803` | `mcq` | true | `C` | `C. Yes, because her testimony is relevant to the mental state necessary for the commission of the crime.` |
| baseline | `mmlu_10804` | `mcq` | false | `B` | `C. No, because the man received the letter on May 4.` |
| baseline | `mmlu_10805` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10806` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10807` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10808` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10809` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10810` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10811` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10812` | `mcq` | false | `A` | `D. not prevail, because the young man was engaged in theft when he was shot.` |
| baseline | `mmlu_10813` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10814` | `mcq` | true | `C` | `C. not prevail, because the owner and the landscaper effectively modified their agreement, thereby depriving the son of ` |
| baseline | `mmlu_10815` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10816` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10817` | `mcq` | false | `A` | `D. No, the deed was invalid as to both grantors because partner two stepped outside his scope of authority.` |
| baseline | `mmlu_10818` | `mcq` | false | `B` | `C. Yes, because the Eleventh Amendment bars actions against a state in federal court.` |
| baseline | `mmlu_10819` | `mcq` | false | `A` | `D. not guilty of either solicitation or conspiracy to commit murder.` |
| baseline | `mmlu_10820` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10821` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10822` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10823` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10824` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10825` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10826` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10827` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10828` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10829` | `mcq` | true | `D` | `D. Yes, because the restriction is binding on the daughter as a successor.` |
| baseline | `mmlu_10830` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10831` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10832` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10833` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10834` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10835` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10836` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10837` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10838` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10839` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10840` | `mcq` | false | `D` | `A. Felony murder.` |
| baseline | `mmlu_10841` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10842` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10843` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10844` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10845` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10846` | `mcq` | false | `B` | `C. not recover, because the owner is not liable for the criminal acts of third persons.` |
| baseline | `mmlu_10847` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10848` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10849` | `mcq` | true | `C` | `C. not prevail, if the police officer reasonably believed that he was under attack.` |
| baseline | `mmlu_10850` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10851` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10852` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10853` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10854` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10855` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10856` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10857` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10858` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10859` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10860` | `mcq` | false | `B` | `C. The debt was already barred by the statute of limitations.` |
| baseline | `mmlu_10861` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10862` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10863` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10864` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10865` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10866` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10867` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10868` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10869` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10870` | `mcq` | true | `D` | `D. $75,000, or the commission equivalent of 5 percent on the sale of the property for $1,500,000, since the consummation` |
| baseline | `mmlu_10871` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10872` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10873` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10874` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10875` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10876` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10877` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10878` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10879` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10880` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10881` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10882` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10883` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10884` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10885` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10886` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10887` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10888` | `mcq` | true | `D` | `D. reverse both the conviction and the reimbursement order because the defendant was denied the right to represent himse` |
| baseline | `mmlu_10889` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10890` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10891` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10892` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10893` | `mcq` | true | `D` | `D. not prevail, because the husband was acting reasonably in an emergency.` |
| baseline | `mmlu_10894` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10895` | `mcq` | false | `B` | `D. inadmissible, under either the marital or spousal privileges.` |
| baseline | `mmlu_10896` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10897` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10898` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10899` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10900` | `mcq` | false | `A` | `D. The tenant, because the landlord has not shown good cause to terminate the tenancy.` |
| baseline | `mmlu_10901` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10902` | `mcq` | false | `B` | `D. not prevail, because the owner should not be responsible for the intentional acts of the employee.` |
| baseline | `mmlu_10903` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10904` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10905` | `mcq` | false | `C` | `D. Murder.` |
| baseline | `mmlu_10906` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10907` | `mcq` | false | `B` | `C. Yes, because there is no diversity of citizenship between the distributor and the wholesaler.` |
| baseline | `mmlu_10908` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10909` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10910` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10911` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10912` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10913` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10914` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10915` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10916` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10917` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10918` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_10919` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10920` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10921` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10922` | `mcq` | false | `B` | `C. affirmative covenant.` |
| baseline | `mmlu_10923` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10924` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10925` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10926` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10927` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10928` | `mcq` | true | `D` | `D. Yes, because a combination of factors makes it likely that the court will recognize unconscionability under these cir` |
| baseline | `mmlu_10929` | `mcq` | false | `A` | `D. unsuccessful, because the man did not intend to shoot the customer.` |
| baseline | `mmlu_10930` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10931` | `mcq` | true | `C` | `C. Yes, because a dismissal with prejudice operates as a judgment on the merits.` |
| baseline | `mmlu_10932` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10933` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10934` | `mcq` | true | `D` | `D. not recover.` |
| baseline | `mmlu_10935` | `mcq` | false | `C` | `D. not succeed, unless the farmer had constructive notice of the existence of the mortgage.` |
| baseline | `mmlu_10936` | `mcq` | false | `A` | `C. not guilty, because of his intoxication.` |
| baseline | `mmlu_10937` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10938` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10939` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10940` | `mcq` | true | `D` | `D. Reverse the conviction, because the judge's action in directing the verdict denied the defendant his constitutional r` |
| baseline | `mmlu_10941` | `mcq` | false | `A` | `C. Licensee.` |
| baseline | `mmlu_10942` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10943` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10944` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10945` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10946` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10947` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10948` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10949` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10950` | `mcq` | true | `B` | `B. Yes, because the company made no effort to inform the prosecutor that the registration fee had been paid in full.` |
| baseline | `mmlu_10951` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10952` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10953` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10954` | `mcq` | false | `B` | `D. not prevail, because the husband and wife sustained no legal damages in renting a comparable suite at another hotel f` |
| baseline | `mmlu_10955` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10956` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10957` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10958` | `mcq` | true | `D` | `D. Yes, the provision is enforceable because it is generally considered to be a reasonable restraint on alienation.` |
| baseline | `mmlu_10959` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10960` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10961` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10962` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10963` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10964` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10965` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10966` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10967` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10968` | `mcq` | false | `D` | `A. The statute of limitations has run, so Gordon's lawsuit is not timely.` |
| baseline | `mmlu_10969` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10970` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10971` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10972` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10973` | `mcq` | true | `D` | `D. Yes, the construction company has substantially performed the contract.` |
| baseline | `mmlu_10974` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10975` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10976` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10977` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10978` | `mcq` | true | `C` | `C. Yes, the lost profits damages were sufficiently proven by the evidence, including expert testimony.` |
| baseline | `mmlu_10979` | `mcq` | false | `C` | `B. Yes, because the conversation is hearsay and there are no exceptions that would allow it into evidence.` |
| baseline | `mmlu_10980` | `mcq` | false | `A` | `D. inadmissible, because it is hearsay not within any recognized exception.` |
| baseline | `mmlu_10981` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10982` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10983` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10984` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10985` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10986` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10987` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10988` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10989` | `mcq` | true | `C` | `C. not guilty, because he honestly believed that she was consenting.` |
| baseline | `mmlu_10990` | `mcq` | true | `D` | `D. The farmer, because he has put the water to a beneficial use prior to the rancher's use and has continuously used the` |
| baseline | `mmlu_10991` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10992` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10993` | `mcq` | false | `A` | `C. Yes, although hearsay, under the learned treatise exception to the hearsay rule.` |
| baseline | `mmlu_10994` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10995` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10996` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10997` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10998` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10999` | `mcq` | true | `C` | `C` |
