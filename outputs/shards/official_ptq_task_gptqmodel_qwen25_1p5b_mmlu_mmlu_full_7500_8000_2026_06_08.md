# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 338 / 500 | 0.6760 | 9.6742 | 0.194288 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_7500` | `mcq` | false | `C` | `D. dishwater blond` |
| baseline | `mmlu_7501` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7502` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7503` | `mcq` | true | `B` | `B. Big Gulp` |
| baseline | `mmlu_7504` | `mcq` | true | `A` | `A. Japan` |
| baseline | `mmlu_7505` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7506` | `mcq` | true | `B` | `B. Ireland` |
| baseline | `mmlu_7507` | `mcq` | true | `B` | `B. Ivory` |
| baseline | `mmlu_7508` | `mcq` | true | `C` | `C. Liverpool` |
| baseline | `mmlu_7509` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7510` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7511` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7512` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7514` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7515` | `mcq` | false | `C` | `A. 13` |
| baseline | `mmlu_7516` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7517` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7518` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7519` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7520` | `mcq` | false | `C` | `Bichon Frise` |
| baseline | `mmlu_7521` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7522` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7523` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7524` | `mcq` | false | `C` | `B. Chex` |
| baseline | `mmlu_7525` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7526` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7527` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7528` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7529` | `mcq` | true | `D` | `D./big toe` |
| baseline | `mmlu_7530` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7531` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7532` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7533` | `mcq` | true | `D` | `D. Reptiles and amphibians.` |
| baseline | `mmlu_7534` | `mcq` | false | `D` | `B. Leukemia` |
| baseline | `mmlu_7535` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7536` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7537` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7538` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7539` | `mcq` | false | `B` | `C. Jeff Beck` |
| baseline | `mmlu_7540` | `mcq` | false | `B` | `C. Killing an enemy` |
| baseline | `mmlu_7541` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7542` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7543` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7544` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7545` | `mcq` | true | `D` | `D. Richard Nixon` |
| baseline | `mmlu_7546` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7547` | `mcq` | false | `B` | `A. 1 seconds` |
| baseline | `mmlu_7548` | `mcq` | true | `D` | `D. the working class` |
| baseline | `mmlu_7549` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7550` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7551` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7552` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7553` | `mcq` | true | `A` | `A. China` |
| baseline | `mmlu_7554` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7555` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7556` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7557` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7558` | `mcq` | false | `A` | `C. 60 years` |
| baseline | `mmlu_7559` | `mcq` | true | `A` | `A. crazy` |
| baseline | `mmlu_7560` | `mcq` | true | `B` | `B. omega` |
| baseline | `mmlu_7561` | `mcq` | true | `C` | `C. Tempo` |
| baseline | `mmlu_7562` | `mcq` | false | `A` | `B. seven` |
| baseline | `mmlu_7563` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7564` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7565` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7566` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7567` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7568` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7569` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7570` | `mcq` | true | `C` | `C. Hemlock` |
| baseline | `mmlu_7571` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7572` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7573` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7574` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7575` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7576` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7577` | `mcq` | false | `B` | `C. HGI` |
| baseline | `mmlu_7578` | `mcq` | false | `D` | `A. The instructional objectives` |
| baseline | `mmlu_7579` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7580` | `mcq` | true | `D` | `D. Israel` |
| baseline | `mmlu_7581` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7582` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7583` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7584` | `mcq` | true | `D` | `D. Hyundai` |
| baseline | `mmlu_7585` | `mcq` | true | `C` | `C. Acceleration` |
| baseline | `mmlu_7586` | `mcq` | true | `A` | `A. Weaving` |
| baseline | `mmlu_7587` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7588` | `mcq` | true | `B` | `B. ichthyologist` |
| baseline | `mmlu_7589` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7590` | `mcq` | true | `A` | `A. four inches` |
| baseline | `mmlu_7591` | `mcq` | false | `B` | `C. 7` |
| baseline | `mmlu_7592` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7593` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7594` | `mcq` | true | `B` | `B. Walter Mondale` |
| baseline | `mmlu_7595` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7596` | `mcq` | true | `B` | `B. Links` |
| baseline | `mmlu_7597` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7598` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7599` | `mcq` | true | `C` | `C. six years` |
| baseline | `mmlu_7600` | `mcq` | true | `A` | `A. head` |
| baseline | `mmlu_7601` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7602` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7603` | `mcq` | true | `C` | `C. Rhea` |
| baseline | `mmlu_7604` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7605` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7606` | `mcq` | true | `B` | `B. Chloroplast` |
| baseline | `mmlu_7607` | `mcq` | false | `D` | `A. Dallas` |
| baseline | `mmlu_7608` | `mcq` | true | `C` | `C. Homer` |
| baseline | `mmlu_7609` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7610` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7611` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7612` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7613` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7614` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7616` | `mcq` | true | `B` | `B. 1940s` |
| baseline | `mmlu_7617` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7618` | `mcq` | true | `B` | `B. Portfolio assessment.` |
| baseline | `mmlu_7619` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7620` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7621` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7622` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7623` | `mcq` | true | `A` | `A. black` |
| baseline | `mmlu_7624` | `mcq` | true | `C` | `C. IRA` |
| baseline | `mmlu_7625` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7626` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7627` | `mcq` | false | `C` | `D. Brown` |
| baseline | `mmlu_7628` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7629` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7630` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7631` | `mcq` | true | `C` | `C. Large-scale deforestation of the Amazon or Congo basin tropical forests.` |
| baseline | `mmlu_7632` | `mcq` | true | `D` | `D. Bobby Riggs` |
| baseline | `mmlu_7633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7634` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7635` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7636` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7637` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7638` | `mcq` | true | `A` | `A. Ninth` |
| baseline | `mmlu_7639` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7640` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7641` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7642` | `mcq` | true | `D` | `D. Personification` |
| baseline | `mmlu_7643` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7644` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7645` | `mcq` | true | `D` | `D. A grammar guide.` |
| baseline | `mmlu_7646` | `mcq` | true | `B` | `B. India` |
| baseline | `mmlu_7647` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7648` | `mcq` | false | `C` | `B. Woody Guthrie` |
| baseline | `mmlu_7649` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7650` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7651` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7652` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7653` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7654` | `mcq` | true | `A` | `A. Chicken Little` |
| baseline | `mmlu_7655` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7656` | `mcq` | false | `A` | `Domain` |
| baseline | `mmlu_7657` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7658` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7659` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7660` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7661` | `mcq` | true | `C` | `C. New York City` |
| baseline | `mmlu_7662` | `mcq` | false | `A` | `B. USC` |
| baseline | `mmlu_7663` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7664` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7665` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7666` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7667` | `mcq` | true | `A` | `A. Paris` |
| baseline | `mmlu_7668` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7669` | `mcq` | true | `B` | `B. Primary` |
| baseline | `mmlu_7670` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7671` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7672` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7674` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7675` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7676` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7677` | `mcq` | false | `A` | `C. 7:00 AM` |
| baseline | `mmlu_7678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7679` | `mcq` | true | `C` | `C. Stonefish` |
| baseline | `mmlu_7680` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7681` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7682` | `mcq` | false | `B` | `D. chili peppers` |
| baseline | `mmlu_7683` | `mcq` | false | `B` | `C. 18` |
| baseline | `mmlu_7684` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7685` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7686` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7687` | `mcq` | true | `D` | `D. France` |
| baseline | `mmlu_7688` | `mcq` | true | `B` | `B. seven` |
| baseline | `mmlu_7689` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7690` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7691` | `mcq` | true | `A` | `A. Bismarck` |
| baseline | `mmlu_7692` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7693` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7694` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7695` | `mcq` | true | `D` | `D. Labrador retriever` |
| baseline | `mmlu_7696` | `mcq` | true | `B` | `B. Madonna` |
| baseline | `mmlu_7697` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7698` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7699` | `mcq` | true | `B` | `B. film production` |
| baseline | `mmlu_7700` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7702` | `mcq` | true | `B` | `B. $1.2 billion annual Revenue` |
| baseline | `mmlu_7703` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7704` | `mcq` | true | `C` | `C. 88` |
| baseline | `mmlu_7705` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7706` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7707` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7708` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7709` | `mcq` | false | `C` | `A. Atlantis` |
| baseline | `mmlu_7710` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7711` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7712` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7713` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7714` | `mcq` | true | `A` | `A. sea horse` |
| baseline | `mmlu_7715` | `mcq` | false | `B` | `D. 320,000` |
| baseline | `mmlu_7716` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7717` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7718` | `mcq` | true | `B` | `B. Cronus` |
| baseline | `mmlu_7719` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7720` | `mcq` | true | `B` | `B. Janis Joplin` |
| baseline | `mmlu_7721` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7722` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7723` | `mcq` | true | `B` | `B. HTTP` |
| baseline | `mmlu_7724` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7725` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7726` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7728` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7729` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7730` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7731` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7733` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7734` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7735` | `mcq` | true | `A` | `A. gaggle` |
| baseline | `mmlu_7736` | `mcq` | true | `C` | `C. directory assistance` |
| baseline | `mmlu_7737` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7738` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7739` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7740` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7741` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7742` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7743` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7744` | `mcq` | false | `B` | `D. Four` |
| baseline | `mmlu_7745` | `mcq` | false | `B` | `D. The Iron Sheik` |
| baseline | `mmlu_7746` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7747` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7748` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7749` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7750` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7751` | `mcq` | false | `B` | `A. Frank and Bill` |
| baseline | `mmlu_7752` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7753` | `mcq` | true | `C` | `C. Wookiee` |
| baseline | `mmlu_7754` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7755` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7756` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7757` | `mcq` | false | `C` | `D. Navy` |
| baseline | `mmlu_7758` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7759` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7760` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7761` | `mcq` | true | `C` | `C. six` |
| baseline | `mmlu_7762` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7763` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7764` | `mcq` | true | `B` | `B. the stockholders` |
| baseline | `mmlu_7765` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7766` | `mcq` | false | `C` | `D. New York City` |
| baseline | `mmlu_7767` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7768` | `mcq` | true | `D` | `D. Sensation'` |
| baseline | `mmlu_7769` | `mcq` | true | `D` | `D. Fidelio'` |
| baseline | `mmlu_7770` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7771` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7772` | `mcq` | true | `D` | `D. quickly` |
| baseline | `mmlu_7773` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7774` | `mcq` | true | `B` | `B. thistle` |
| baseline | `mmlu_7775` | `mcq` | true | `C` | `C. $1 billion` |
| baseline | `mmlu_7776` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7777` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7778` | `mcq` | true | `B` | `B. Appropriating funds.` |
| baseline | `mmlu_7779` | `mcq` | true | `B` | `B. Japan` |
| baseline | `mmlu_7780` | `mcq` | true | `B` | `B. Asia` |
| baseline | `mmlu_7781` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7782` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7783` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7784` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7785` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7786` | `mcq` | true | `B` | `B. the home team` |
| baseline | `mmlu_7787` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7788` | `mcq` | false | `A` | `B. 13` |
| baseline | `mmlu_7789` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7790` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7791` | `mcq` | false | `A` | `C. Elizabeth Arden` |
| baseline | `mmlu_7792` | `mcq` | true | `B` | `B. German` |
| baseline | `mmlu_7793` | `mcq` | true | `D` | `D. Meat` |
| baseline | `mmlu_7794` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7795` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7796` | `mcq` | true | `C` | `C. Funding the construction of the interstate highway system.` |
| baseline | `mmlu_7797` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7798` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7799` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7800` | `mcq` | true | `C` | `C. SEC` |
| baseline | `mmlu_7801` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7802` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7803` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7804` | `mcq` | true | `C` | `C. 4.5 billion years` |
| baseline | `mmlu_7805` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7806` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7809` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7810` | `mcq` | true | `A` | `A. declaring bankruptcy` |
| baseline | `mmlu_7811` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7812` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7813` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7814` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7815` | `mcq` | false | `B` | `C. Magellan` |
| baseline | `mmlu_7816` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7817` | `mcq` | true | `B` | `B. Cow` |
| baseline | `mmlu_7818` | `mcq` | true | `A` | `A. file transfer protocol` |
| baseline | `mmlu_7819` | `mcq` | true | `A` | `A. calligraphy` |
| baseline | `mmlu_7820` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7821` | `mcq` | true | `B` | `B. 1980` |
| baseline | `mmlu_7822` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7823` | `mcq` | true | `B` | `B. Silicon` |
| baseline | `mmlu_7824` | `mcq` | true | `B` | `B. Stephen King` |
| baseline | `mmlu_7825` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7827` | `mcq` | true | `D` | `D. Beethoven` |
| baseline | `mmlu_7828` | `mcq` | false | `C` | `A. Chicago` |
| baseline | `mmlu_7829` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7830` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7831` | `mcq` | true | `A` | `A. Gulf of Sidra` |
| baseline | `mmlu_7832` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7833` | `mcq` | true | `D` | `D. Spanish` |
| baseline | `mmlu_7834` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7835` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7836` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7837` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7838` | `mcq` | false | `C` | `A. Paradise Lost'` |
| baseline | `mmlu_7839` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7840` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7841` | `mcq` | true | `A` | `A. print lock` |
| baseline | `mmlu_7842` | `mcq` | false | `C` | `A. John Paul Revere` |
| baseline | `mmlu_7843` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7844` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7845` | `mcq` | false | `D` | `C. Paul Anka` |
| baseline | `mmlu_7846` | `mcq` | true | `B` | `B. Mini-Me` |
| baseline | `mmlu_7847` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7848` | `mcq` | true | `A` | `A. California` |
| baseline | `mmlu_7849` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7850` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7851` | `mcq` | true | `A` | `A. Two` |
| baseline | `mmlu_7852` | `mcq` | true | `B` | `B. blue` |
| baseline | `mmlu_7853` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7854` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7855` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7856` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7857` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7858` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7859` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7860` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7861` | `mcq` | false | `A` | `B. Outside` |
| baseline | `mmlu_7862` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7863` | `mcq` | true | `A` | `A. stop` |
| baseline | `mmlu_7864` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7865` | `mcq` | true | `C` | `C. Water` |
| baseline | `mmlu_7866` | `mcq` | true | `A` | `A. France` |
| baseline | `mmlu_7867` | `mcq` | true | `C` | `C. Blue Whale` |
| baseline | `mmlu_7868` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7869` | `mcq` | true | `B` | `B. Yellow` |
| baseline | `mmlu_7870` | `mcq` | true | `C` | `C. eye` |
| baseline | `mmlu_7871` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7872` | `mcq` | false | `D` | `B. Two` |
| baseline | `mmlu_7873` | `mcq` | true | `A` | `A. Nomadic` |
| baseline | `mmlu_7874` | `mcq` | true | `D` | `D. Dutch` |
| baseline | `mmlu_7875` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7876` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7877` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7878` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7879` | `mcq` | false | `B` | `C. Lancelot` |
| baseline | `mmlu_7880` | `mcq` | true | `D` | `D. Read-Only Memory` |
| baseline | `mmlu_7881` | `mcq` | false | `C` | `A. 11` |
| baseline | `mmlu_7882` | `mcq` | false | `B` | `D. Tisha Campbell` |
| baseline | `mmlu_7883` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7884` | `mcq` | true | `B` | `B. Euclidean` |
| baseline | `mmlu_7885` | `mcq` | false | `D` | `B. Marginal cost` |
| baseline | `mmlu_7886` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7887` | `mcq` | true | `B` | `B. Wellington` |
| baseline | `mmlu_7888` | `mcq` | true | `B` | `B. Hula Hoop` |
| baseline | `mmlu_7889` | `mcq` | false | `C` | `B. May` |
| baseline | `mmlu_7890` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7891` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7892` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7893` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7894` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7895` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7896` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7897` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7898` | `mcq` | true | `C` | `C. is more willing to take people at face value` |
| baseline | `mmlu_7899` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7900` | `mcq` | true | `D` | `D. Miriam` |
| baseline | `mmlu_7901` | `mcq` | true | `B` | `B. Pennsylvania` |
| baseline | `mmlu_7902` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7903` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7904` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7905` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7906` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7907` | `mcq` | true | `C` | `C. Cinco de Mayo` |
| baseline | `mmlu_7908` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7909` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7910` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7911` | `mcq` | true | `D` | `D. Paul Allen` |
| baseline | `mmlu_7912` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7913` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7914` | `mcq` | true | `A` | `A. Knock on it.` |
| baseline | `mmlu_7915` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7916` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7917` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7918` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7919` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7920` | `mcq` | true | `A` | `A. Wood` |
| baseline | `mmlu_7921` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7922` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7923` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7924` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7925` | `mcq` | true | `A` | `A. Lisa 2` |
| baseline | `mmlu_7926` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7927` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7928` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7929` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7930` | `mcq` | true | `A` | `A. pink` |
| baseline | `mmlu_7931` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7932` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7933` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7934` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7935` | `mcq` | true | `C` | `C. Price` |
| baseline | `mmlu_7936` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7937` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7938` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7939` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7940` | `mcq` | true | `B` | `B. kangaroo` |
| baseline | `mmlu_7941` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7942` | `mcq` | true | `C` | `C. Bones` |
| baseline | `mmlu_7943` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7944` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7945` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7946` | `mcq` | true | `D` | `D. .exe` |
| baseline | `mmlu_7947` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7948` | `mcq` | true | `B` | `B. mitosis` |
| baseline | `mmlu_7949` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7950` | `mcq` | true | `B` | `B. Mercury` |
| baseline | `mmlu_7951` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7952` | `mcq` | false | `D` | `B. dairy` |
| baseline | `mmlu_7953` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7954` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7955` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7956` | `mcq` | true | `B` | `B. China` |
| baseline | `mmlu_7957` | `mcq` | true | `D` | `D. IKEA` |
| baseline | `mmlu_7958` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7959` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7960` | `mcq` | true | `C` | `C. England` |
| baseline | `mmlu_7961` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7962` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7963` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7964` | `mcq` | true | `C` | `C. performance art` |
| baseline | `mmlu_7965` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7966` | `mcq` | true | `A` | `A. Spanish` |
| baseline | `mmlu_7967` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7968` | `mcq` | true | `B` | `B. oil` |
| baseline | `mmlu_7969` | `mcq` | true | `A` | `A. African National Congress` |
| baseline | `mmlu_7970` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7971` | `mcq` | false | `C` | `B. Two` |
| baseline | `mmlu_7972` | `mcq` | false | `D` | `B. Photosphere` |
| baseline | `mmlu_7973` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7974` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7975` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7976` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7977` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7978` | `mcq` | false | `C` | `A. 12` |
| baseline | `mmlu_7979` | `mcq` | true | `C` | `C. deficient` |
| baseline | `mmlu_7980` | `mcq` | true | `B` | `B. Garnet` |
| baseline | `mmlu_7981` | `mcq` | false | `B` | `D. He kills himself` |
| baseline | `mmlu_7982` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7983` | `mcq` | false | `B` | `A. Monday's child` |
| baseline | `mmlu_7984` | `mcq` | true | `B` | `B. a truck` |
| baseline | `mmlu_7985` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7986` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7987` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7988` | `mcq` | false | `D` | `A. Milan` |
| baseline | `mmlu_7989` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7990` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7991` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7992` | `mcq` | true | `B` | `B. Action and movement.` |
| baseline | `mmlu_7993` | `mcq` | true | `C` | `C. corned beef` |
| baseline | `mmlu_7994` | `mcq` | true | `D` | `D. 10-K filings with the SEC` |
| baseline | `mmlu_7995` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7996` | `mcq` | true | `A` | `A. Eros` |
| baseline | `mmlu_7997` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7998` | `mcq` | true | `D` | `D. Sherman` |
| baseline | `mmlu_7999` | `mcq` | false | `B` | `A.` |
