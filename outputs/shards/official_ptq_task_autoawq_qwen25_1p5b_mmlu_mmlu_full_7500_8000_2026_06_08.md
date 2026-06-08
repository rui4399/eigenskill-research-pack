# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 355 / 500 | 0.7100 | 11.9560 | 0.156394 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_7500` | `mcq` | false | `C` | `A. brown` |
| baseline | `mmlu_7501` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7502` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7503` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7504` | `mcq` | true | `A` | `A. Japan` |
| baseline | `mmlu_7505` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7506` | `mcq` | true | `B` | `B. Ireland` |
| baseline | `mmlu_7507` | `mcq` | true | `B` | `B. Ivory` |
| baseline | `mmlu_7508` | `mcq` | true | `C` | `C. Liverpool` |
| baseline | `mmlu_7509` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7510` | `mcq` | true | `B` | `B. 100` |
| baseline | `mmlu_7511` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7512` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7513` | `mcq` | true | `D` | `D. North Pole` |
| baseline | `mmlu_7514` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7515` | `mcq` | true | `C` | `C. 50` |
| baseline | `mmlu_7516` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7517` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7518` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7519` | `mcq` | true | `B` | `B. $200,000,000` |
| baseline | `mmlu_7520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7521` | `mcq` | false | `C` | `B. 2,000,000,000` |
| baseline | `mmlu_7522` | `mcq` | false | `A` | `D. caramel` |
| baseline | `mmlu_7523` | `mcq` | true | `C` | `C. red` |
| baseline | `mmlu_7524` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7525` | `mcq` | false | `C` | `B. 2` |
| baseline | `mmlu_7526` | `mcq` | false | `B` | `A. Joey` |
| baseline | `mmlu_7527` | `mcq` | false | `B` | `A. regressive` |
| baseline | `mmlu_7528` | `mcq` | true | `D` | `D. institutionalism` |
| baseline | `mmlu_7529` | `mcq` | true | `D` | `D. big toe` |
| baseline | `mmlu_7530` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7531` | `mcq` | true | `C` | `C. hemophilia` |
| baseline | `mmlu_7532` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7533` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7534` | `mcq` | true | `D` | `D. Chicken pox` |
| baseline | `mmlu_7535` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7536` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7537` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7538` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7539` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7540` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7541` | `mcq` | true | `B` | `B. St Louis` |
| baseline | `mmlu_7542` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7543` | `mcq` | true | `B` | `B. the Gold Glove` |
| baseline | `mmlu_7544` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7545` | `mcq` | true | `D` | `D. Richard Nixon` |
| baseline | `mmlu_7546` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7547` | `mcq` | false | `B` | `A. 1 seconds` |
| baseline | `mmlu_7548` | `mcq` | true | `D` | `D. the working class` |
| baseline | `mmlu_7549` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7550` | `mcq` | false | `C` | `D. major general` |
| baseline | `mmlu_7551` | `mcq` | true | `A` | `A. 6'` |
| baseline | `mmlu_7552` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7553` | `mcq` | true | `A` | `A. China` |
| baseline | `mmlu_7554` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7555` | `mcq` | true | `C` | `C. nine` |
| baseline | `mmlu_7556` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7557` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7558` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7559` | `mcq` | true | `A` | `A. crazy` |
| baseline | `mmlu_7560` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7561` | `mcq` | true | `C` | `C. Tempo` |
| baseline | `mmlu_7562` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7563` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7564` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7565` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7566` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7567` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7568` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7569` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7570` | `mcq` | true | `C` | `C. Hemlock` |
| baseline | `mmlu_7571` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7572` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7573` | `mcq` | true | `D` | `D. Pinch hitter` |
| baseline | `mmlu_7574` | `mcq` | true | `C` | `C. Argentina` |
| baseline | `mmlu_7575` | `mcq` | true | `C` | `C. 81` |
| baseline | `mmlu_7576` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7577` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7578` | `mcq` | false | `D` | `A. The instructional objectives` |
| baseline | `mmlu_7579` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7580` | `mcq` | true | `D` | `D. Israel` |
| baseline | `mmlu_7581` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7582` | `mcq` | true | `C` | `C. birds` |
| baseline | `mmlu_7583` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7584` | `mcq` | true | `D` | `D. Hyundai` |
| baseline | `mmlu_7585` | `mcq` | true | `C` | `C. Acceleration` |
| baseline | `mmlu_7586` | `mcq` | true | `A` | `A. Weaving` |
| baseline | `mmlu_7587` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7588` | `mcq` | true | `B` | `B. ichthyologist` |
| baseline | `mmlu_7589` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7590` | `mcq` | false | `A` | `C. ten inches` |
| baseline | `mmlu_7591` | `mcq` | false | `B` | `D. 0` |
| baseline | `mmlu_7592` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7593` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7594` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7595` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7596` | `mcq` | true | `B` | `B. Links` |
| baseline | `mmlu_7597` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7598` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7599` | `mcq` | false | `C` | `B. four years` |
| baseline | `mmlu_7600` | `mcq` | true | `A` | `A. head` |
| baseline | `mmlu_7601` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7602` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7603` | `mcq` | true | `C` | `C. Rhea` |
| baseline | `mmlu_7604` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7605` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7606` | `mcq` | true | `B` | `B. Chloroplast` |
| baseline | `mmlu_7607` | `mcq` | false | `D` | `A. Dallas` |
| baseline | `mmlu_7608` | `mcq` | true | `C` | `C. Homer` |
| baseline | `mmlu_7609` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7610` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7611` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7612` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7613` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7614` | `mcq` | true | `D` | `D. San Antonio Spurs` |
| baseline | `mmlu_7615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7616` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7617` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7618` | `mcq` | true | `B` | `B. Portfolio assessment` |
| baseline | `mmlu_7619` | `mcq` | true | `B` | `B. through a human body` |
| baseline | `mmlu_7620` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7621` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7622` | `mcq` | false | `B` | `A. shrimp` |
| baseline | `mmlu_7623` | `mcq` | true | `A` | `A. black` |
| baseline | `mmlu_7624` | `mcq` | true | `C` | `C. IRA` |
| baseline | `mmlu_7625` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7626` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7627` | `mcq` | false | `C` | `A. yellow` |
| baseline | `mmlu_7628` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7629` | `mcq` | true | `A` | `A. 1600` |
| baseline | `mmlu_7630` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7631` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7632` | `mcq` | true | `D` | `D. Bobby Riggs` |
| baseline | `mmlu_7633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7634` | `mcq` | false | `A` | `D. Dick Dastardly` |
| baseline | `mmlu_7635` | `mcq` | true | `C` | `C. goat` |
| baseline | `mmlu_7636` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7637` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7638` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7639` | `mcq` | true | `B` | `B. Caricature` |
| baseline | `mmlu_7640` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7641` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7642` | `mcq` | true | `D` | `D. Personification` |
| baseline | `mmlu_7643` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7644` | `mcq` | true | `C` | `C. chocolate` |
| baseline | `mmlu_7645` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7646` | `mcq` | true | `B` | `B. India` |
| baseline | `mmlu_7647` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7648` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7649` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7650` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7651` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7652` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7653` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7654` | `mcq` | true | `A` | `A. Chicken Little` |
| baseline | `mmlu_7655` | `mcq` | false | `A` | `B. kazoo` |
| baseline | `mmlu_7656` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7657` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7658` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7659` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7660` | `mcq` | false | `D` | `A. The man pays` |
| baseline | `mmlu_7661` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7662` | `mcq` | true | `A` | `A. Notre Dame` |
| baseline | `mmlu_7663` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7664` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7665` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7666` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7667` | `mcq` | true | `A` | `A. Paris` |
| baseline | `mmlu_7668` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7669` | `mcq` | true | `B` | `B. Primary` |
| baseline | `mmlu_7670` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7671` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7672` | `mcq` | true | `D` | `D. thousand` |
| baseline | `mmlu_7673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7674` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7675` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7676` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7677` | `mcq` | false | `A` | `C. 7:00 AM` |
| baseline | `mmlu_7678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7679` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7680` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7681` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7682` | `mcq` | true | `B` | `B. meat` |
| baseline | `mmlu_7683` | `mcq` | false | `B` | `C. 18` |
| baseline | `mmlu_7684` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7685` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7686` | `mcq` | true | `A` | `A. 2` |
| baseline | `mmlu_7687` | `mcq` | true | `D` | `D. France` |
| baseline | `mmlu_7688` | `mcq` | true | `B` | `B. seven` |
| baseline | `mmlu_7689` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7690` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7691` | `mcq` | true | `A` | `A. Bismarck` |
| baseline | `mmlu_7692` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7693` | `mcq` | false | `C` | `A. I only` |
| baseline | `mmlu_7694` | `mcq` | false | `A` | `B. 4*10^12 kg` |
| baseline | `mmlu_7695` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7696` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7697` | `mcq` | true | `B` | `B. in reverse` |
| baseline | `mmlu_7698` | `mcq` | true | `A` | `A. iris` |
| baseline | `mmlu_7699` | `mcq` | true | `B` | `B. film production` |
| baseline | `mmlu_7700` | `mcq` | true | `B` | `B. Louis XIV` |
| baseline | `mmlu_7701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7702` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7703` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7704` | `mcq` | true | `C` | `C. 88` |
| baseline | `mmlu_7705` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7706` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7707` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7708` | `mcq` | true | `B` | `B. nearsighted` |
| baseline | `mmlu_7709` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7710` | `mcq` | true | `C` | `C. Captain Kangaroo` |
| baseline | `mmlu_7711` | `mcq` | true | `B` | `B. courtroom` |
| baseline | `mmlu_7712` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7713` | `mcq` | false | `A` | `B. Yanni` |
| baseline | `mmlu_7714` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7715` | `mcq` | false | `B` | `D. 320,000` |
| baseline | `mmlu_7716` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7717` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7718` | `mcq` | true | `B` | `B. Cronus` |
| baseline | `mmlu_7719` | `mcq` | true | `A` | `A. cancer` |
| baseline | `mmlu_7720` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7721` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7722` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7723` | `mcq` | true | `B` | `B. HTTP` |
| baseline | `mmlu_7724` | `mcq` | true | `B` | `B. Albuquerque` |
| baseline | `mmlu_7725` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7726` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7727` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7728` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7729` | `mcq` | true | `C` | `C. 19th` |
| baseline | `mmlu_7730` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7731` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7732` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7733` | `mcq` | true | `B` | `B. Bloat` |
| baseline | `mmlu_7734` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7735` | `mcq` | true | `A` | `A. gaggle` |
| baseline | `mmlu_7736` | `mcq` | true | `C` | `C. directory assistance` |
| baseline | `mmlu_7737` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7738` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7739` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7740` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7741` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7742` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7743` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7744` | `mcq` | false | `B` | `D. four` |
| baseline | `mmlu_7745` | `mcq` | false | `B` | `D. The Iron Sheik` |
| baseline | `mmlu_7746` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7747` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7748` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7749` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7750` | `mcq` | true | `C` | `C. tangelo` |
| baseline | `mmlu_7751` | `mcq` | true | `B` | `B. Tom and Dick` |
| baseline | `mmlu_7752` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7753` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7754` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7755` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7756` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7757` | `mcq` | false | `C` | `B. Air Force` |
| baseline | `mmlu_7758` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7759` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7760` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7761` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7762` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7763` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7764` | `mcq` | true | `B` | `B. the stockholders` |
| baseline | `mmlu_7765` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7766` | `mcq` | false | `C` | `D. New York City` |
| baseline | `mmlu_7767` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7768` | `mcq` | true | `D` | `D. Sensation'` |
| baseline | `mmlu_7769` | `mcq` | true | `D` | `D. Fidelio` |
| baseline | `mmlu_7770` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7771` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7772` | `mcq` | true | `D` | `D. quickly` |
| baseline | `mmlu_7773` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7774` | `mcq` | true | `B` | `B. thistle` |
| baseline | `mmlu_7775` | `mcq` | true | `C` | `C. $1 billion` |
| baseline | `mmlu_7776` | `mcq` | true | `D` | `D. Yogi Bear` |
| baseline | `mmlu_7777` | `mcq` | true | `D` | `D. Nyctophobia` |
| baseline | `mmlu_7778` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7779` | `mcq` | true | `B` | `B. Japan` |
| baseline | `mmlu_7780` | `mcq` | true | `B` | `B. Asia` |
| baseline | `mmlu_7781` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7782` | `mcq` | true | `A` | `A. whooping cough` |
| baseline | `mmlu_7783` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7784` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7785` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7786` | `mcq` | true | `B` | `B. the home team` |
| baseline | `mmlu_7787` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7788` | `mcq` | true | `A` | `A. 11` |
| baseline | `mmlu_7789` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7790` | `mcq` | false | `C` | `A. Pluto` |
| baseline | `mmlu_7791` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7792` | `mcq` | true | `B` | `B. German` |
| baseline | `mmlu_7793` | `mcq` | true | `D` | `D. meat` |
| baseline | `mmlu_7794` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7795` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7796` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7797` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7798` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7799` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7800` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7801` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7802` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7803` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7804` | `mcq` | true | `C` | `C. 4.5 billion years` |
| baseline | `mmlu_7805` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7806` | `mcq` | true | `A` | `A. grenadine` |
| baseline | `mmlu_7807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7809` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7810` | `mcq` | true | `A` | `A. declaring bankruptcy` |
| baseline | `mmlu_7811` | `mcq` | true | `C` | `C. ten thousand` |
| baseline | `mmlu_7812` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7813` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7814` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7815` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7816` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7817` | `mcq` | true | `B` | `B. Cow` |
| baseline | `mmlu_7818` | `mcq` | true | `A` | `A. file transfer protocol` |
| baseline | `mmlu_7819` | `mcq` | true | `A` | `A. calligraphy` |
| baseline | `mmlu_7820` | `mcq` | true | `D` | `D. the Trinity` |
| baseline | `mmlu_7821` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7822` | `mcq` | true | `A` | `A. heredity` |
| baseline | `mmlu_7823` | `mcq` | true | `B` | `B. Silicon` |
| baseline | `mmlu_7824` | `mcq` | true | `B` | `B. Stephen King` |
| baseline | `mmlu_7825` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_7826` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7827` | `mcq` | true | `D` | `D. Beethoven` |
| baseline | `mmlu_7828` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7829` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7830` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7831` | `mcq` | true | `A` | `A. Gulf of Sidra` |
| baseline | `mmlu_7832` | `mcq` | true | `D` | `D. Old Sparky` |
| baseline | `mmlu_7833` | `mcq` | true | `D` | `D. Spanish` |
| baseline | `mmlu_7834` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7835` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7836` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7837` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7838` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7839` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7840` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7841` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7842` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7843` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7844` | `mcq` | true | `B` | `B. Luigi` |
| baseline | `mmlu_7845` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7846` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7847` | `mcq` | true | `D` | `D. melting` |
| baseline | `mmlu_7848` | `mcq` | true | `A` | `A. California` |
| baseline | `mmlu_7849` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7850` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7851` | `mcq` | true | `A` | `A. Two` |
| baseline | `mmlu_7852` | `mcq` | false | `B` | `D. really big` |
| baseline | `mmlu_7853` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7855` | `mcq` | true | `C` | `C. 0.75` |
| baseline | `mmlu_7856` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7857` | `mcq` | true | `B` | `B. indicate the depth of certain readers' feelings about science fiction` |
| baseline | `mmlu_7858` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7859` | `mcq` | true | `B` | `B. 74 m.p.h.` |
| baseline | `mmlu_7860` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7861` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7862` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7863` | `mcq` | true | `A` | `A. stop` |
| baseline | `mmlu_7864` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7865` | `mcq` | true | `C` | `C. Water` |
| baseline | `mmlu_7866` | `mcq` | true | `A` | `A. France` |
| baseline | `mmlu_7867` | `mcq` | false | `C` | `B. sperm whale` |
| baseline | `mmlu_7868` | `mcq` | true | `C` | `C. dog` |
| baseline | `mmlu_7869` | `mcq` | false | `B` | `C. green` |
| baseline | `mmlu_7870` | `mcq` | true | `C` | `C. eye` |
| baseline | `mmlu_7871` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7872` | `mcq` | false | `D` | `B. two` |
| baseline | `mmlu_7873` | `mcq` | true | `A` | `A. Nomadic` |
| baseline | `mmlu_7874` | `mcq` | true | `D` | `D. Dutch` |
| baseline | `mmlu_7875` | `mcq` | true | `D` | `D. shellfish` |
| baseline | `mmlu_7876` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7877` | `mcq` | true | `C` | `C. hygrometer` |
| baseline | `mmlu_7878` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7879` | `mcq` | false | `B` | `C. Lancelot` |
| baseline | `mmlu_7880` | `mcq` | true | `D` | `D. Read-Only Memory` |
| baseline | `mmlu_7881` | `mcq` | false | `C` | `D. 21` |
| baseline | `mmlu_7882` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7883` | `mcq` | false | `A` | `C. 2000` |
| baseline | `mmlu_7884` | `mcq` | true | `B` | `B. euclidean` |
| baseline | `mmlu_7885` | `mcq` | false | `D` | `B. Marginal cost` |
| baseline | `mmlu_7886` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7887` | `mcq` | true | `B` | `B. Wellington` |
| baseline | `mmlu_7888` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7889` | `mcq` | false | `C` | `B. May` |
| baseline | `mmlu_7890` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7891` | `mcq` | true | `D` | `D. palette` |
| baseline | `mmlu_7892` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7893` | `mcq` | true | `D` | `D. silver` |
| baseline | `mmlu_7894` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7895` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7896` | `mcq` | true | `A` | `A. pig` |
| baseline | `mmlu_7897` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7898` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7899` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7900` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7901` | `mcq` | true | `B` | `B. Pennsylvania` |
| baseline | `mmlu_7902` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7903` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7904` | `mcq` | false | `C` | `B. 8*10^23` |
| baseline | `mmlu_7905` | `mcq` | true | `A` | `A. Richard Rodgers` |
| baseline | `mmlu_7906` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7907` | `mcq` | true | `C` | `C. Cinco de Mayo` |
| baseline | `mmlu_7908` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7909` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7910` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7911` | `mcq` | true | `D` | `D. Paul Allen` |
| baseline | `mmlu_7912` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7913` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7914` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7915` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7916` | `mcq` | false | `A` | `D. syphilis` |
| baseline | `mmlu_7917` | `mcq` | true | `C` | `C. Uranium` |
| baseline | `mmlu_7918` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7919` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7920` | `mcq` | true | `A` | `A. Wood` |
| baseline | `mmlu_7921` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7922` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7923` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7924` | `mcq` | true | `B` | `B. America Online` |
| baseline | `mmlu_7925` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7926` | `mcq` | false | `C` | `B. Thailand` |
| baseline | `mmlu_7927` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7928` | `mcq` | true | `C` | `C. five` |
| baseline | `mmlu_7929` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7930` | `mcq` | true | `A` | `A. pink` |
| baseline | `mmlu_7931` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7932` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7933` | `mcq` | true | `C` | `C. Sioux` |
| baseline | `mmlu_7934` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7935` | `mcq` | true | `C` | `C. Price` |
| baseline | `mmlu_7936` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7937` | `mcq` | false | `C` | `D. Super Bowl` |
| baseline | `mmlu_7938` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7939` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7940` | `mcq` | true | `B` | `B. kangaroo` |
| baseline | `mmlu_7941` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7942` | `mcq` | true | `C` | `C. Bones` |
| baseline | `mmlu_7943` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7944` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7945` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7946` | `mcq` | true | `D` | `D. .exe` |
| baseline | `mmlu_7947` | `mcq` | true | `C` | `C. anagram` |
| baseline | `mmlu_7948` | `mcq` | true | `B` | `B. mitosis` |
| baseline | `mmlu_7949` | `mcq` | true | `B` | `B. rabies` |
| baseline | `mmlu_7950` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7951` | `mcq` | false | `D` | `B. laundry` |
| baseline | `mmlu_7952` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7953` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7954` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7955` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7956` | `mcq` | true | `B` | `B. China` |
| baseline | `mmlu_7957` | `mcq` | true | `D` | `D. IKEA` |
| baseline | `mmlu_7958` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7959` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7960` | `mcq` | true | `C` | `C. England` |
| baseline | `mmlu_7961` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7962` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7963` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7964` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7965` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7966` | `mcq` | true | `A` | `A. Spanish` |
| baseline | `mmlu_7967` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7968` | `mcq` | true | `B` | `B. oil` |
| baseline | `mmlu_7969` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7970` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7971` | `mcq` | false | `C` | `B. Two` |
| baseline | `mmlu_7972` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7973` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7974` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7975` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7976` | `mcq` | false | `C` | `A. Order of business` |
| baseline | `mmlu_7977` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7978` | `mcq` | true | `C` | `C. 16` |
| baseline | `mmlu_7979` | `mcq` | true | `C` | `C. deficient` |
| baseline | `mmlu_7980` | `mcq` | true | `B` | `B. garnet` |
| baseline | `mmlu_7981` | `mcq` | false | `B` | `D. He kills himself` |
| baseline | `mmlu_7982` | `mcq` | false | `B` | `A. United States` |
| baseline | `mmlu_7983` | `mcq` | false | `B` | `A. Monday's child` |
| baseline | `mmlu_7984` | `mcq` | true | `B` | `B. a truck` |
| baseline | `mmlu_7985` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7986` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7987` | `mcq` | false | `A` | `B. 10^-29 %` |
| baseline | `mmlu_7988` | `mcq` | true | `D` | `D. San Francisco` |
| baseline | `mmlu_7989` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7990` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7991` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7992` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7993` | `mcq` | true | `C` | `C. corned beef` |
| baseline | `mmlu_7994` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7995` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7996` | `mcq` | true | `A` | `A. Eros` |
| baseline | `mmlu_7997` | `mcq` | false | `B` | `D. Division` |
| baseline | `mmlu_7998` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7999` | `mcq` | false | `B` | `A.` |
