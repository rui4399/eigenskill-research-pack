# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 334 / 500 | 0.6680 | 5.4318 | 0.357734 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_13500` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13501` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13502` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13503` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13504` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13505` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13506` | `mcq` | true | `C` | `C. participant observation` |
| baseline | `mmlu_13507` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13508` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13509` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13510` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13511` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13512` | `mcq` | true | `A` | `A. 30.70%` |
| baseline | `mmlu_13513` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13514` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13515` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13516` | `mcq` | true | `C` | `C. economically dependent on the wealthy countries that exploited them` |
| baseline | `mmlu_13517` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13518` | `mcq` | true | `A` | `A. mass production, mass circulation, and the decline of serious content` |
| baseline | `mmlu_13519` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13520` | `mcq` | true | `C` | `C. it uncovers rich, detailed accounts from an insider's perspective` |
| baseline | `mmlu_13521` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13522` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13523` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13524` | `mcq` | true | `C` | `C. leading questions` |
| baseline | `mmlu_13525` | `mcq` | true | `B` | `B. Modernization theory` |
| baseline | `mmlu_13526` | `mcq` | true | `D` | `D. occupation` |
| baseline | `mmlu_13527` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13528` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13529` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13530` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13531` | `mcq` | true | `D` | `D. increased state regulation through national testing and inspections` |
| baseline | `mmlu_13532` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13533` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13534` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13535` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13536` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13537` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13538` | `mcq` | true | `B` | `B. non-probability sampling` |
| baseline | `mmlu_13539` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13540` | `mcq` | true | `D` | `D. including working class organizations in political bargaining and representation` |
| baseline | `mmlu_13541` | `mcq` | true | `A` | `A. Acculturation` |
| baseline | `mmlu_13542` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13543` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13544` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13545` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13546` | `mcq` | false | `B` | `D. all of the above` |
| baseline | `mmlu_13547` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13548` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13549` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13550` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13551` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13552` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13553` | `mcq` | true | `D` | `D. The family` |
| baseline | `mmlu_13554` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13555` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13556` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13557` | `mcq` | true | `C` | `C. car manufacturing in assembly plants` |
| baseline | `mmlu_13558` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13559` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13560` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13561` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13562` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13563` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13564` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13565` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13566` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13567` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13568` | `mcq` | true | `B` | `B. stability and the structure of society` |
| baseline | `mmlu_13569` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13570` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13571` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13572` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13573` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13574` | `mcq` | true | `B` | `B. Wider at the bottom than at the top` |
| baseline | `mmlu_13575` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13576` | `mcq` | true | `A` | `A. Glass ceiling` |
| baseline | `mmlu_13577` | `mcq` | true | `B` | `B. organized crime` |
| baseline | `mmlu_13578` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_13579` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13580` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13581` | `mcq` | true | `B` | `B. mollies` |
| baseline | `mmlu_13582` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13583` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13584` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13585` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13586` | `mcq` | true | `A` | `A. Functionalism` |
| baseline | `mmlu_13587` | `mcq` | false | `C` | `B. confidential medical records` |
| baseline | `mmlu_13588` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13589` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13590` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_13591` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13592` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13593` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13594` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13595` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_13596` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13597` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13598` | `mcq` | true | `B` | `B. deceiving the respondents as to the reason for your presence` |
| baseline | `mmlu_13599` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13600` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13601` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13602` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_13603` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13604` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13605` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13606` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13607` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13608` | `mcq` | true | `A` | `A. Richard Nixon` |
| baseline | `mmlu_13609` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13610` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13611` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13612` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13613` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13614` | `mcq` | true | `D` | `D. Congress.` |
| baseline | `mmlu_13615` | `mcq` | true | `B` | `B. Local developments were viewed through a geopolitical lens` |
| baseline | `mmlu_13616` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13617` | `mcq` | true | `B` | `B. The distribution of power in the international system` |
| baseline | `mmlu_13618` | `mcq` | true | `D` | `D. ALL of the above` |
| baseline | `mmlu_13619` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13620` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13621` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13622` | `mcq` | true | `B` | `B. Costs of free trade are concentrated, but benefits are dispersed` |
| baseline | `mmlu_13623` | `mcq` | true | `C` | `C. Limited UN mandate and fear of a protracted conflict` |
| baseline | `mmlu_13624` | `mcq` | true | `B` | `B. They serve American interests` |
| baseline | `mmlu_13625` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13626` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_13627` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13628` | `mcq` | true | `B` | `B. The growing costs of war with France` |
| baseline | `mmlu_13629` | `mcq` | false | `C` | `B. George Soros` |
| baseline | `mmlu_13630` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13631` | `mcq` | true | `A` | `A. Promotion of Democracy, free-trade and international institutions` |
| baseline | `mmlu_13632` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13633` | `mcq` | true | `C` | `C. That military spending gave the arms industry unwarranted influence on politics and government` |
| baseline | `mmlu_13634` | `mcq` | true | `A` | `A. the Security Council.` |
| baseline | `mmlu_13635` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13636` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13637` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13638` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13639` | `mcq` | true | `B` | `B. The US promoted the marketization of the Russian economy` |
| baseline | `mmlu_13640` | `mcq` | true | `D` | `D. 3 or more` |
| baseline | `mmlu_13641` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13642` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13643` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13644` | `mcq` | true | `A` | `A. Realism` |
| baseline | `mmlu_13645` | `mcq` | true | `B` | `B. Anarchy` |
| baseline | `mmlu_13646` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13647` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13648` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13649` | `mcq` | true | `A` | `A. Richard Nixon.` |
| baseline | `mmlu_13650` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13651` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13652` | `mcq` | true | `D` | `D. All of the above are true.` |
| baseline | `mmlu_13653` | `mcq` | false | `C` | `B. the National Security Council.` |
| baseline | `mmlu_13654` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13655` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13656` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13657` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13658` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13659` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13660` | `mcq` | true | `A` | `A. the United Nations.` |
| baseline | `mmlu_13661` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13662` | `mcq` | true | `D` | `D. ALL of the above` |
| baseline | `mmlu_13663` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13664` | `mcq` | true | `B` | `B. "brinkmanship."` |
| baseline | `mmlu_13665` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13666` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13667` | `mcq` | true | `C` | `C. I, II, and III` |
| baseline | `mmlu_13668` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13669` | `mcq` | false | `B` | `A. Fewer than 7` |
| baseline | `mmlu_13670` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13671` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13672` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13673` | `mcq` | true | `B` | `B. They see it as an ideological façade for US imperialism` |
| baseline | `mmlu_13674` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13675` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13676` | `mcq` | false | `A` | `D. All of the above` |
| baseline | `mmlu_13677` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13679` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13680` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13681` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13682` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13683` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13684` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13685` | `mcq` | true | `C` | `C. Creation of the National Intelligence Director` |
| baseline | `mmlu_13686` | `mcq` | true | `A` | `A. the National Security Council.` |
| baseline | `mmlu_13687` | `mcq` | false | `C` | `B. Class consciousness` |
| baseline | `mmlu_13688` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13689` | `mcq` | true | `A` | `A. Realism` |
| baseline | `mmlu_13690` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13691` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13692` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13693` | `mcq` | false | `D` | `C. The Presidency welcomed the influence of Congress` |
| baseline | `mmlu_13694` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13695` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13696` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13697` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13698` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13699` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13700` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13702` | `mcq` | true | `A` | `A. Voluntary reliance on an external power for security` |
| baseline | `mmlu_13703` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13704` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_13705` | `mcq` | false | `A` | `D.unknown` |
| baseline | `mmlu_13706` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13707` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13708` | `mcq` | false | `B` | `C. This period commonly lasts for a few days` |
| baseline | `mmlu_13709` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13710` | `mcq` | true | `A` | `A. Innovators` |
| baseline | `mmlu_13711` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13712` | `mcq` | true | `B` | `B. Gastroenteritis in children` |
| baseline | `mmlu_13713` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13714` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13715` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13716` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13717` | `mcq` | true | `B` | `B. Serial cross-sectional` |
| baseline | `mmlu_13718` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13719` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13720` | `mcq` | true | `A` | `A. 350 million` |
| baseline | `mmlu_13721` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13722` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13723` | `mcq` | true | `B` | `B. Interacting with a T helper cell.` |
| baseline | `mmlu_13724` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13725` | `mcq` | true | `C` | `C. The virion RNA acting as mRNA` |
| baseline | `mmlu_13726` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13727` | `mcq` | false | `D` | `A. HIV` |
| baseline | `mmlu_13728` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13729` | `mcq` | true | `A` | `A. Behavioral intervention, treatment and structural interventions` |
| baseline | `mmlu_13730` | `mcq` | true | `B` | `B. By MMR vaccine` |
| baseline | `mmlu_13731` | `mcq` | true | `C` | `C. Hygiene and social distancing` |
| baseline | `mmlu_13732` | `mcq` | false | `A` | `C. Bats` |
| baseline | `mmlu_13733` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13734` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13735` | `mcq` | false | `B` | `A. Replicate in dividing cells and encodes three oncogenic proteins E5, E6 and E7` |
| baseline | `mmlu_13736` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13737` | `mcq` | false | `D` | `B. Identifying genetic variation` |
| baseline | `mmlu_13738` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13739` | `mcq` | false | `D` | `B. To search for drug resistant mutants` |
| baseline | `mmlu_13740` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_13741` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_13742` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13743` | `mcq` | true | `A` | `A. Enveloped spherical particles with an icosahedral structure` |
| baseline | `mmlu_13744` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13745` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13746` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13747` | `mcq` | false | `D` | `B. Acyclovir` |
| baseline | `mmlu_13748` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13749` | `mcq` | true | `B` | `B. Children not exposed to the chemical waste who do not suffer from ALL` |
| baseline | `mmlu_13750` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_13751` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13752` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13753` | `mcq` | false | `C` | `D. Haemorrhagic cystitis` |
| baseline | `mmlu_13754` | `mcq` | true | `A` | `A. Shot gun sequencing` |
| baseline | `mmlu_13755` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13756` | `mcq` | false | `A` | `B. Attending a funeral of a victim outside` |
| baseline | `mmlu_13757` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13758` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13759` | `mcq` | false | `A` | `C. Aerosols of urine from infected small mammals` |
| baseline | `mmlu_13760` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13761` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13762` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13763` | `mcq` | false | `C` | `A. The microscopist Antonie van Leeuwenhoek` |
| baseline | `mmlu_13764` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13765` | `mcq` | true | `C` | `C. Jaundice and abdominal discomfort` |
| baseline | `mmlu_13766` | `mcq` | false | `B` | `C. In cells using replicon systems` |
| baseline | `mmlu_13767` | `mcq` | false | `C` | `B. Bias` |
| baseline | `mmlu_13768` | `mcq` | false | `C` | `B. An icosahedral structure with an envelope` |
| baseline | `mmlu_13769` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13770` | `mcq` | false | `A` | `B. SARS` |
| baseline | `mmlu_13771` | `mcq` | false | `A` | `C. Short (2-3 days) incubation` |
| baseline | `mmlu_13772` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13773` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13774` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13775` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13776` | `mcq` | false | `B` | `A. Having 5 genera` |
| baseline | `mmlu_13777` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13778` | `mcq` | true | `C` | `C. Basic knowledge of hand washing and food hygiene` |
| baseline | `mmlu_13779` | `mcq` | false | `A` | `B. Cohort study` |
| baseline | `mmlu_13780` | `mcq` | true | `A` | `A. Africa` |
| baseline | `mmlu_13781` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13782` | `mcq` | false | `B` | `C. Pandemic` |
| baseline | `mmlu_13783` | `mcq` | false | `D` | `C. Genetic factors` |
| baseline | `mmlu_13784` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13785` | `mcq` | false | `D` | `B. Small linear ss DNA` |
| baseline | `mmlu_13786` | `mcq` | false | `C` | `B. Long filamentous threads` |
| baseline | `mmlu_13787` | `mcq` | true | `C` | `C. From DNA to RNA to protein` |
| baseline | `mmlu_13788` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_13789` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13790` | `mcq` | true | `C` | `C. The enzyme reverse transcriptase` |
| baseline | `mmlu_13791` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13792` | `mcq` | true | `B` | `B. Homosexual males` |
| baseline | `mmlu_13793` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13794` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13795` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_13796` | `mcq` | false | `A` | `C. Africa and S. America` |
| baseline | `mmlu_13797` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13798` | `mcq` | true | `D` | `D. Both a and c` |
| baseline | `mmlu_13799` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13800` | `mcq` | false | `D` | `C. The disease a virus causes` |
| baseline | `mmlu_13801` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13802` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13803` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13804` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13805` | `mcq` | false | `C` | `B. Long-term survivors` |
| baseline | `mmlu_13806` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13807` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13808` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13809` | `mcq` | true | `B` | `B. Induces apoptosis via caspases` |
| baseline | `mmlu_13810` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13811` | `mcq` | false | `A` | `B. The central United States (Kansas, Missouri etc.)` |
| baseline | `mmlu_13812` | `mcq` | true | `A` | `A. Confounding` |
| baseline | `mmlu_13813` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13814` | `mcq` | true | `B` | `B. "Opt-out"` |
| baseline | `mmlu_13815` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13816` | `mcq` | true | `A` | `A. Use of cellular scaffolding in the nucleus and cytoplasm` |
| baseline | `mmlu_13817` | `mcq` | true | `B` | `B. Mother's viral load` |
| baseline | `mmlu_13818` | `mcq` | true | `C` | `C. How many contacts will be infected from one case` |
| baseline | `mmlu_13819` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13820` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13821` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_13822` | `mcq` | false | `D` | `C. Hepatitis` |
| baseline | `mmlu_13823` | `mcq` | false | `B` | `A. The virus is so antigenically variable` |
| baseline | `mmlu_13824` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13825` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_13826` | `mcq` | false | `C` | `B. The elderly` |
| baseline | `mmlu_13827` | `mcq` | true | `B` | `B. Attention to handwashing and hygiene` |
| baseline | `mmlu_13828` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13829` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13830` | `mcq` | false | `B` | `A. CD4+` |
| baseline | `mmlu_13831` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13832` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13833` | `mcq` | false | `A` | `D. Direct-acting Antivirals such as daclatasvir and sofosbuvir` |
| baseline | `mmlu_13834` | `mcq` | false | `A` | `B. Air Travel` |
| baseline | `mmlu_13835` | `mcq` | false | `A` | `D. Sub unit chemically inactivated vaccine` |
| baseline | `mmlu_13836` | `mcq` | true | `B` | `B. Gastroenteritis in children` |
| baseline | `mmlu_13837` | `mcq` | false | `A` | `B. Unlinked anonymous` |
| baseline | `mmlu_13838` | `mcq` | false | `A` | `B. Median` |
| baseline | `mmlu_13839` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13840` | `mcq` | false | `B` | `C. Avoid observer and subject bias` |
| baseline | `mmlu_13841` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_13842` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13843` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13844` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13845` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_13846` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_13847` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13848` | `mcq` | true | `A` | `A. Very restricted replication in the gut` |
| baseline | `mmlu_13849` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_13850` | `mcq` | false | `A` | `D. Effect modification (interaction)` |
| baseline | `mmlu_13851` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13852` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13853` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_13854` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_13855` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13856` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13857` | `mcq` | false | `A` | `C. Hygiene and social distancing` |
| baseline | `mmlu_13858` | `mcq` | false | `A` | `C. Cohort study` |
| baseline | `mmlu_13859` | `mcq` | false | `B` | `C. Yellow Fever` |
| baseline | `mmlu_13860` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13861` | `mcq` | true | `D` | `D. Both a and c` |
| baseline | `mmlu_13862` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13863` | `mcq` | false | `A` | `C. Increasing CRP level appears to increase the risk of heart attack/stroke.` |
| baseline | `mmlu_13864` | `mcq` | false | `C` | `A. Double shelled icosahedron` |
| baseline | `mmlu_13865` | `mcq` | true | `B` | `B. Icosahedron with slender fibres` |
| baseline | `mmlu_13866` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13867` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13868` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_13869` | `mcq` | true | `B` | `B. The superficial appearance of a 'star' on negative straining electron microscopy` |
| baseline | `mmlu_13870` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13871` | `mcq` | true | `D` | `D. Idols` |
| baseline | `mmlu_13872` | `mcq` | true | `B` | `B. Yin-Yang School` |
| baseline | `mmlu_13873` | `mcq` | false | `D` | `A. 325 CE` |
| baseline | `mmlu_13874` | `mcq` | true | `A` | `A. Akitu` |
| baseline | `mmlu_13875` | `mcq` | true | `D` | `D. Ikebana` |
| baseline | `mmlu_13876` | `mcq` | true | `A` | `A. Harmony and balance` |
| baseline | `mmlu_13877` | `mcq` | true | `A` | `A. Shabad` |
| baseline | `mmlu_13878` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13880` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13881` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_13882` | `mcq` | true | `D` | `D. Soto Zen` |
| baseline | `mmlu_13883` | `mcq` | true | `B` | `B. Langar` |
| baseline | `mmlu_13884` | `mcq` | true | `B` | `B. Daoism` |
| baseline | `mmlu_13885` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13886` | `mcq` | true | `D` | `D. No-self` |
| baseline | `mmlu_13887` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13888` | `mcq` | true | `C` | `C. Mahayana` |
| baseline | `mmlu_13889` | `mcq` | true | `D` | `D. Digambara` |
| baseline | `mmlu_13890` | `mcq` | true | `A` | `A. The Shema` |
| baseline | `mmlu_13891` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13892` | `mcq` | false | `C` | `D. The Battle of Badr` |
| baseline | `mmlu_13893` | `mcq` | true | `A` | `A. Remembering the Divine Name` |
| baseline | `mmlu_13894` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_13895` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13896` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13897` | `mcq` | true | `A` | `A. Anointed one` |
| baseline | `mmlu_13898` | `mcq` | false | `D` | `C. Non-matter` |
| baseline | `mmlu_13899` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13900` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_13901` | `mcq` | false | `B` | `C. Judging and vengeful` |
| baseline | `mmlu_13902` | `mcq` | true | `A` | `A. Palestine and Babylonia` |
| baseline | `mmlu_13903` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13904` | `mcq` | true | `A` | `A. Kali yuga` |
| baseline | `mmlu_13905` | `mcq` | true | `A` | `A. Hymns` |
| baseline | `mmlu_13906` | `mcq` | true | `A` | `A. Pure Land` |
| baseline | `mmlu_13907` | `mcq` | true | `A` | `A. Sita` |
| baseline | `mmlu_13908` | `mcq` | true | `B` | `B. Rabi'a` |
| baseline | `mmlu_13909` | `mcq` | true | `A` | `A. Andal` |
| baseline | `mmlu_13910` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13911` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_13912` | `mcq` | true | `D` | `D. Quakers` |
| baseline | `mmlu_13913` | `mcq` | true | `A` | `A. Peter` |
| baseline | `mmlu_13914` | `mcq` | true | `A` | `A. 1935` |
| baseline | `mmlu_13915` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_13916` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13917` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13918` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13919` | `mcq` | false | `A` | `C. 33` |
| baseline | `mmlu_13920` | `mcq` | true | `D` | `D. Cow` |
| baseline | `mmlu_13921` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_13922` | `mcq` | true | `B` | `B. Destruction of the Second Temple` |
| baseline | `mmlu_13923` | `mcq` | false | `C` | `D. Shinran` |
| baseline | `mmlu_13924` | `mcq` | true | `C` | `C. Indonesia` |
| baseline | `mmlu_13925` | `mcq` | true | `A` | `A. Gregory` |
| baseline | `mmlu_13926` | `mcq` | false | `A` | `B. Worthy ones` |
| baseline | `mmlu_13927` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13928` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13929` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13930` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_13931` | `mcq` | true | `B` | `B. Sri Lakshmi` |
| baseline | `mmlu_13932` | `mcq` | false | `B` | `A. China` |
| baseline | `mmlu_13933` | `mcq` | true | `B` | `B. Patanjali` |
| baseline | `mmlu_13934` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_13935` | `mcq` | true | `B` | `B. Ganesha` |
| baseline | `mmlu_13936` | `mcq` | true | `C` | `C. Rsabha` |
| baseline | `mmlu_13937` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13938` | `mcq` | true | `A` | `A. 36,000` |
| baseline | `mmlu_13939` | `mcq` | true | `A` | `A. Ultimate Reality` |
| baseline | `mmlu_13940` | `mcq` | true | `B` | `B. Hukam` |
| baseline | `mmlu_13941` | `mcq` | false | `C` | `B. 29` |
| baseline | `mmlu_13942` | `mcq` | true | `C` | `C. Humanistic Buddhism` |
| baseline | `mmlu_13943` | `mcq` | true | `B` | `B. They believed that nakedness was an elemental expression of non-attachment` |
| baseline | `mmlu_13944` | `mcq` | true | `A` | `A. Namokar Mantra` |
| baseline | `mmlu_13945` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_13946` | `mcq` | false | `C` | `B. 42` |
| baseline | `mmlu_13947` | `mcq` | true | `C` | `C. Ocean of Wisdom` |
| baseline | `mmlu_13948` | `mcq` | true | `C` | `C. Sri (Lakshmi)` |
| baseline | `mmlu_13949` | `mcq` | true | `C` | `C. Devotion` |
| baseline | `mmlu_13950` | `mcq` | true | `C` | `C. Sarasvati` |
| baseline | `mmlu_13951` | `mcq` | true | `B` | `B. The Kaddish` |
| baseline | `mmlu_13952` | `mcq` | true | `B` | `B. Vishnu` |
| baseline | `mmlu_13953` | `mcq` | true | `C` | `C. Rulers, warriors` |
| baseline | `mmlu_13954` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_13955` | `mcq` | false | `C` | `A. Correct knowledge` |
| baseline | `mmlu_13956` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13957` | `mcq` | false | `A` | `D. John of the Cross` |
| baseline | `mmlu_13958` | `mcq` | true | `A` | `A. Paap` |
| baseline | `mmlu_13959` | `mcq` | true | `A` | `A. Obon` |
| baseline | `mmlu_13960` | `mcq` | true | `A` | `A. "Great Hero"` |
| baseline | `mmlu_13961` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13962` | `mcq` | false | `C` | `B. China` |
| baseline | `mmlu_13963` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_13964` | `mcq` | true | `C` | `C. Caliph` |
| baseline | `mmlu_13965` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_13966` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_13967` | `mcq` | true | `A` | `A. Bardo Thodol` |
| baseline | `mmlu_13968` | `mcq` | false | `A` | `C. Diwali` |
| baseline | `mmlu_13969` | `mcq` | false | `D` | `B. 9–11 p.m.` |
| baseline | `mmlu_13970` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13971` | `mcq` | true | `B` | `B. At least 17` |
| baseline | `mmlu_13972` | `mcq` | false | `A` | `C. Reconstructionism` |
| baseline | `mmlu_13973` | `mcq` | true | `A` | `A. Khalsa` |
| baseline | `mmlu_13974` | `mcq` | true | `B` | `B. Guru Nanak` |
| baseline | `mmlu_13975` | `mcq` | true | `C` | `C. Auspiciousness` |
| baseline | `mmlu_13976` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13977` | `mcq` | true | `A` | `A. Thesmophoria` |
| baseline | `mmlu_13978` | `mcq` | true | `C` | `C. Pentecostalism` |
| baseline | `mmlu_13979` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_13980` | `mcq` | true | `C` | `C. Direction of prayer` |
| baseline | `mmlu_13981` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_13982` | `mcq` | true | `A` | `A. Hizmet` |
| baseline | `mmlu_13983` | `mcq` | true | `A` | `A. Brahmins` |
| baseline | `mmlu_13984` | `mcq` | false | `B` | `A. Hwanin` |
| baseline | `mmlu_13985` | `mcq` | true | `B` | `B. Bhikshunis` |
| baseline | `mmlu_13986` | `mcq` | true | `C` | `C. Zohar` |
| baseline | `mmlu_13987` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_13988` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13989` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_13990` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_13991` | `mcq` | true | `A` | `A. Baptism and Eucharist` |
| baseline | `mmlu_13992` | `mcq` | true | `C` | `C. Baisakhi Day` |
| baseline | `mmlu_13993` | `mcq` | true | `C` | `C. Waraqah` |
| baseline | `mmlu_13994` | `mcq` | false | `C` | `A. Life stories` |
| baseline | `mmlu_13995` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_13996` | `mcq` | false | `D` | `C. Brit` |
| baseline | `mmlu_13997` | `mcq` | false | `D` | `C. Direct lineage of ancestors` |
| baseline | `mmlu_13998` | `mcq` | true | `B` | `B. Bishnoi` |
| baseline | `mmlu_13999` | `mcq` | false | `C` | `B. Kannon` |
