# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 323 / 500 | 0.6460 | 12.2729 | 0.113914 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_13500` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13501` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13502` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13503` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13504` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13505` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13506` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13507` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13508` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13509` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13510` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13511` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13512` | `mcq` | true | `A` | `A. 30.70%` |
| baseline | `mmlu_13513` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13514` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13515` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13516` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13517` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13518` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13519` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13522` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13523` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13524` | `mcq` | true | `C` | `C. leading questions` |
| baseline | `mmlu_13525` | `mcq` | true | `B` | `B. Modernization theory` |
| baseline | `mmlu_13526` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13527` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13528` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13529` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13530` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13531` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13532` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13533` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13534` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13535` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13536` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13537` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13538` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13539` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13540` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13541` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13542` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13543` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13544` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13545` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13546` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13547` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13548` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13549` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13550` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13551` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13552` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13553` | `mcq` | true | `D` | `D. The family` |
| baseline | `mmlu_13554` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13555` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13556` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13557` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13558` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13559` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13560` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13561` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13562` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13563` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13564` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13565` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13566` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13567` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13568` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13569` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13570` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13571` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13572` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13573` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13574` | `mcq` | true | `B` | `B. Wider at the bottom than at the top` |
| baseline | `mmlu_13575` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13576` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13577` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13578` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13579` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13580` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_13581` | `mcq` | false | `B` | `C. Dollies` |
| baseline | `mmlu_13582` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13583` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13584` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13585` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13586` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13587` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13588` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13589` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13590` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13591` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13592` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13593` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13594` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13595` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13596` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13597` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13598` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13599` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13600` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13601` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13602` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13603` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13604` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13605` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13606` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13607` | `mcq` | true | `D` | `D. China` |
| baseline | `mmlu_13608` | `mcq` | true | `A` | `A. Richard Nixon` |
| baseline | `mmlu_13609` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13610` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13611` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13612` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13613` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13614` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13615` | `mcq` | true | `B` | `B. Local developments were viewed through a geopolitical lens` |
| baseline | `mmlu_13616` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13617` | `mcq` | true | `B` | `B. The distribution of power in the international system` |
| baseline | `mmlu_13618` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13619` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13620` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13621` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13622` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13623` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13624` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13625` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13626` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_13627` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13628` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13629` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13630` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13631` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13632` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13633` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13634` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13635` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13636` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13637` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13638` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13639` | `mcq` | true | `B` | `B. The US promoted the marketization of the Russian economy` |
| baseline | `mmlu_13640` | `mcq` | true | `D` | `D. 3 or more` |
| baseline | `mmlu_13641` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13642` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13643` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13644` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13645` | `mcq` | true | `B` | `B. Anarchy` |
| baseline | `mmlu_13646` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13647` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13648` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13649` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13650` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13651` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13652` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13653` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_13654` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13655` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13656` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13657` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13658` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13659` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13660` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13661` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13662` | `mcq` | true | `D` | `D. ALL of the above` |
| baseline | `mmlu_13663` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13664` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13665` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13666` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13667` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13668` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13669` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13670` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13671` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13672` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13673` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13674` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13675` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13676` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13677` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13679` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13680` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13681` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13683` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13684` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13685` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13686` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13687` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_13688` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13689` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13690` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13691` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13692` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13693` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_13694` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13695` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13696` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13697` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13698` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13699` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13700` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13701` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13702` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13703` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13704` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13705` | `mcq` | false | `A` | `D. unknown` |
| baseline | `mmlu_13706` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13707` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13708` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13709` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13710` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13711` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13712` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13713` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13714` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13715` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_13716` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13717` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13718` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13719` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13720` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13721` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13722` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13723` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13724` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13725` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13726` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13728` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13729` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13730` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13731` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13732` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13733` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13734` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13735` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13736` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13737` | `mcq` | false | `D` | `B. Identifying genetic variation` |
| baseline | `mmlu_13738` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13739` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13740` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13741` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13742` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13743` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13744` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13745` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13746` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13747` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13748` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13749` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13750` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13751` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13752` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13753` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13754` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13755` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13756` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13758` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13759` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13760` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13761` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13762` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13763` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13764` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13765` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13766` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13767` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_13768` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13769` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13770` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13771` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13772` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13773` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13774` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13775` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13776` | `mcq` | false | `B` | `A. Having 5 genera` |
| baseline | `mmlu_13777` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13778` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13779` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13780` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13781` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13782` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13783` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_13784` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13785` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13786` | `mcq` | false | `C` | `B. Long filamentous threads` |
| baseline | `mmlu_13787` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13788` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13789` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13790` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13791` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13792` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13793` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13794` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13795` | `mcq` | false | `D` | `C. Develop effective vaccines` |
| baseline | `mmlu_13796` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13797` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13798` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13799` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13800` | `mcq` | false | `D` | `C. The disease a virus causes` |
| baseline | `mmlu_13801` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13802` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13803` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13804` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13805` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13806` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13807` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13808` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13809` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13810` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13811` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13812` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13813` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13814` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13815` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13816` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13817` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13818` | `mcq` | true | `C` | `C. How many contacts will be infected from one case` |
| baseline | `mmlu_13819` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13820` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13821` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13822` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13823` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13824` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13825` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13826` | `mcq` | false | `C` | `B. The elderly` |
| baseline | `mmlu_13827` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13828` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13829` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13830` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13831` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13832` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13833` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13834` | `mcq` | false | `A` | `B. Air Travel` |
| baseline | `mmlu_13835` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13836` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13837` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13838` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13839` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13840` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13841` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_13842` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13843` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13844` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13845` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13846` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13847` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13848` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13849` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13850` | `mcq` | false | `A` | `C. Non-compliance` |
| baseline | `mmlu_13851` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13852` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13853` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13854` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13855` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13856` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13857` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13858` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13859` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13860` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13861` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13862` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13863` | `mcq` | false | `A` | `C. Increasing CRP level appears to increase the risk of heart attack/stroke.` |
| baseline | `mmlu_13864` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13865` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13866` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13867` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13868` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13869` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13870` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13871` | `mcq` | true | `D` | `D. Idols` |
| baseline | `mmlu_13872` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13873` | `mcq` | false | `D` | `A. 325 CE` |
| baseline | `mmlu_13874` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13875` | `mcq` | true | `D` | `D. Ikebana` |
| baseline | `mmlu_13876` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13877` | `mcq` | true | `A` | `A. Shabad` |
| baseline | `mmlu_13878` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13880` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13881` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13882` | `mcq` | true | `D` | `D. Soto Zen` |
| baseline | `mmlu_13883` | `mcq` | true | `B` | `B. Langar` |
| baseline | `mmlu_13884` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13885` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13886` | `mcq` | true | `D` | `D. No-self` |
| baseline | `mmlu_13887` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13888` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13889` | `mcq` | true | `D` | `D. Digambara` |
| baseline | `mmlu_13890` | `mcq` | true | `A` | `A. The Shema` |
| baseline | `mmlu_13891` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13892` | `mcq` | false | `C` | `D. The Battle of Badr` |
| baseline | `mmlu_13893` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13894` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13895` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13896` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13897` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13898` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13899` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13900` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_13901` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13902` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13903` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13904` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13905` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13906` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13907` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13908` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13909` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13910` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13911` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13912` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13913` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13914` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13915` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13916` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13917` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13918` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13919` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13920` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13921` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13922` | `mcq` | true | `B` | `B. Destruction of the Second Temple` |
| baseline | `mmlu_13923` | `mcq` | true | `C` | `C. Honen` |
| baseline | `mmlu_13924` | `mcq` | true | `C` | `C. Indonesia` |
| baseline | `mmlu_13925` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13926` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13927` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13928` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13929` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13930` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13931` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13932` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13933` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13934` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13935` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13936` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13937` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13938` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13939` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13940` | `mcq` | true | `B` | `B. Hukam` |
| baseline | `mmlu_13941` | `mcq` | false | `C` | `B. 29` |
| baseline | `mmlu_13942` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13943` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13944` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13945` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13946` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13947` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13948` | `mcq` | true | `C` | `C. Sri (Lakshmi)` |
| baseline | `mmlu_13949` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13950` | `mcq` | true | `C` | `C. Sarasvati` |
| baseline | `mmlu_13951` | `mcq` | true | `B` | `B. The Kaddish` |
| baseline | `mmlu_13952` | `mcq` | true | `B` | `B. Vishnu` |
| baseline | `mmlu_13953` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13954` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13955` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13956` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13957` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13958` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13959` | `mcq` | true | `A` | `A. Obon` |
| baseline | `mmlu_13960` | `mcq` | true | `A` | `A. "Great Hero"` |
| baseline | `mmlu_13961` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13962` | `mcq` | false | `C` | `B. China` |
| baseline | `mmlu_13963` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13964` | `mcq` | true | `C` | `C. Caliph` |
| baseline | `mmlu_13965` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13966` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13967` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13968` | `mcq` | false | `A` | `C. Diwali` |
| baseline | `mmlu_13969` | `mcq` | false | `D` | `A. 5–7 a.m.` |
| baseline | `mmlu_13970` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13971` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13972` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13973` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13974` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13975` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13976` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13977` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13978` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13979` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13980` | `mcq` | true | `C` | `C. Direction of prayer` |
| baseline | `mmlu_13981` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13982` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13983` | `mcq` | true | `A` | `A. Brahmins` |
| baseline | `mmlu_13984` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13985` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13986` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13987` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13988` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13989` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13990` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13991` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13992` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13993` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13994` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13995` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13996` | `mcq` | false | `D` | `C. Brit` |
| baseline | `mmlu_13997` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13998` | `mcq` | true | `B` | `B. Bishnoi` |
| baseline | `mmlu_13999` | `mcq` | false | `C` | `A` |
