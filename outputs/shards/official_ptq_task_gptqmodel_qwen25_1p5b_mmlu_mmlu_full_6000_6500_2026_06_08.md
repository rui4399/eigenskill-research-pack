# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 332 / 500 | 0.6640 | 9.2211 | 0.174144 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_6000` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6001` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6002` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6003` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6004` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6005` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6006` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6007` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6008` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6009` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6010` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6011` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6012` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6013` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6014` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6015` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6016` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6017` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6018` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6019` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6020` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6021` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6022` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6023` | `mcq` | false | `D` | `B. The importance of ancestor worship.` |
| baseline | `mmlu_6024` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6025` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6026` | `mcq` | true | `C` | `C. Large-scale military losses and resentment of the working classes` |
| baseline | `mmlu_6027` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6028` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6029` | `mcq` | true | `A` | `A. European maritime exploration` |
| baseline | `mmlu_6030` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6031` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6032` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6033` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6034` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6035` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6036` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6037` | `mcq` | true | `D` | `D. Furs` |
| baseline | `mmlu_6038` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6039` | `mcq` | true | `B` | `B. The election of Nelson Mandela` |
| baseline | `mmlu_6040` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6041` | `mcq` | true | `B` | `B. Some elites converted to Islam, but lower classes kept their traditional beliefs.` |
| baseline | `mmlu_6042` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6043` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6044` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6045` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6046` | `mcq` | false | `C` | `A. Gave over his crown to King Ferdinand` |
| baseline | `mmlu_6047` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6048` | `mcq` | false | `D` | `C. Limited economic opportunities` |
| baseline | `mmlu_6049` | `mcq` | false | `B` | `A. The conquest of India by rival Muslim empires` |
| baseline | `mmlu_6050` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6051` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6052` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6053` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6054` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6055` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6056` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6057` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6058` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6059` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6060` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6061` | `mcq` | true | `B` | `B. The adaptation of Western literary forms by non-Western authors.` |
| baseline | `mmlu_6062` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6063` | `mcq` | false | `D` | `A. The Space Race with the United States` |
| baseline | `mmlu_6064` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6065` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6066` | `mcq` | true | `B` | `B. The compass` |
| baseline | `mmlu_6067` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6068` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6069` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6070` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6071` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6072` | `mcq` | true | `A` | `A. European merchants were confined to a few cities designated for foreign trade.` |
| baseline | `mmlu_6073` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6074` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6075` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6076` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6077` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6078` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6079` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6080` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6081` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6082` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6083` | `mcq` | true | `A` | `A. The competing ideologies of the Cold War` |
| baseline | `mmlu_6084` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6085` | `mcq` | true | `C` | `C. Labor unions` |
| baseline | `mmlu_6086` | `mcq` | true | `C` | `C. They had no interest in the products that Great Britain could provide.` |
| baseline | `mmlu_6087` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6088` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6089` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6090` | `mcq` | true | `B` | `B. Eating fish` |
| baseline | `mmlu_6091` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6092` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6094` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6095` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6096` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6097` | `mcq` | true | `A` | `A. Practice regular aerobic exercise` |
| baseline | `mmlu_6098` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6099` | `mcq` | true | `A` | `A. Many pessimists die at a younger age` |
| baseline | `mmlu_6100` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6101` | `mcq` | false | `B` | `C. Hormonal factors such as loss of estrogen.` |
| baseline | `mmlu_6102` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6103` | `mcq` | true | `B` | `B. B6 and B12` |
| baseline | `mmlu_6104` | `mcq` | true | `B` | `B. Identity` |
| baseline | `mmlu_6105` | `mcq` | false | `C` | `B. Social support` |
| baseline | `mmlu_6106` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6107` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6108` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6109` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6110` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6111` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6112` | `mcq` | true | `B` | `B. Neuroticism` |
| baseline | `mmlu_6113` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6114` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6115` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6116` | `mcq` | true | `A` | `A. Men than women` |
| baseline | `mmlu_6117` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6118` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6119` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6120` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6121` | `mcq` | true | `A` | `A. Normal metabolism` |
| baseline | `mmlu_6122` | `mcq` | true | `A` | `A. Ageism` |
| baseline | `mmlu_6123` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6124` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6125` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6126` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6127` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6128` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6129` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6130` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6131` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6132` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6133` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6134` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6135` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6136` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6137` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6138` | `mcq` | true | `A` | `A. Alone` |
| baseline | `mmlu_6139` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6140` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6141` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6142` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6143` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6144` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6145` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6146` | `mcq` | false | `B` | `A. Heart` |
| baseline | `mmlu_6147` | `mcq` | false | `D` | `B. Working` |
| baseline | `mmlu_6148` | `mcq` | false | `C` | `B. Show high satisfaction that steadily declines as the years pass` |
| baseline | `mmlu_6149` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6150` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6151` | `mcq` | true | `C` | `C. Older adults smoke less than younger adults.` |
| baseline | `mmlu_6152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6153` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6154` | `mcq` | false | `B` | `D. They change quite a lot` |
| baseline | `mmlu_6155` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6156` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6157` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6158` | `mcq` | false | `B` | `C. Florida` |
| baseline | `mmlu_6159` | `mcq` | false | `B` | `A. Traits` |
| baseline | `mmlu_6160` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6161` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6163` | `mcq` | false | `A` | `Prevalence` |
| baseline | `mmlu_6164` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6165` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6166` | `mcq` | true | `B` | `B. About 25%` |
| baseline | `mmlu_6167` | `mcq` | true | `B` | `B. Internal` |
| baseline | `mmlu_6168` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6169` | `mcq` | true | `B` | `B. Arthritis` |
| baseline | `mmlu_6170` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6171` | `mcq` | false | `A` | `B. 25%` |
| baseline | `mmlu_6172` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6173` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6174` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6175` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6176` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6177` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6178` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6179` | `mcq` | true | `B` | `B. Education about older adults` |
| baseline | `mmlu_6180` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6181` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6182` | `mcq` | true | `B` | `B. Nicotinic acid is known for lowering LDL (bad) cholesterol levels in the body.` |
| baseline | `mmlu_6183` | `mcq` | false | `B` | `D. Clinical depression` |
| baseline | `mmlu_6184` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6185` | `mcq` | false | `A` | `B. Increase insomnia` |
| baseline | `mmlu_6186` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6187` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6188` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6189` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6190` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6191` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6192` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6193` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6194` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6195` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6196` | `mcq` | true | `C` | `C. Japan` |
| baseline | `mmlu_6197` | `mcq` | true | `C` | `C. Complex` |
| baseline | `mmlu_6198` | `mcq` | true | `B` | `B. Internal` |
| baseline | `mmlu_6199` | `mcq` | false | `A` | `Living will` |
| baseline | `mmlu_6200` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6201` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6202` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6203` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6204` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6205` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6206` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6207` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6208` | `mcq` | true | `B` | `B. MMTI (Minnesota Multiperception Test for Children)` |
| baseline | `mmlu_6209` | `mcq` | false | `B` | `A. Accuracy` |
| baseline | `mmlu_6210` | `mcq` | true | `A` | `A. Japan` |
| baseline | `mmlu_6211` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6212` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6213` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6214` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6215` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6216` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6217` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6218` | `mcq` | false | `A` | `B. Some animals show little or no senescence` |
| baseline | `mmlu_6219` | `mcq` | false | `A` | `C. Changes in hormone levels` |
| baseline | `mmlu_6220` | `mcq` | true | `A` | `A. Stress and loss of social support` |
| baseline | `mmlu_6221` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6223` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6224` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6225` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6226` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6227` | `mcq` | true | `A` | `A. Activities of Daily Living` |
| baseline | `mmlu_6228` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6229` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6230` | `mcq` | true | `A` | `A. Jeanne Calment` |
| baseline | `mmlu_6231` | `mcq` | true | `A` | `A. Fluid pressure in the eye is above normal.` |
| baseline | `mmlu_6232` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6233` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6234` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6235` | `mcq` | false | `A` | `C. Size of our social networks` |
| baseline | `mmlu_6236` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6237` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6238` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6239` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6240` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6241` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6242` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6243` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6244` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6245` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6246` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6247` | `mcq` | true | `A` | `A. Age` |
| baseline | `mmlu_6248` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6249` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_6250` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6251` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6252` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6253` | `mcq` | false | `A` | `D. More than 50%` |
| baseline | `mmlu_6254` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6255` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6256` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6257` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6258` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6259` | `mcq` | true | `C` | `C. Ergonomic` |
| baseline | `mmlu_6260` | `mcq` | true | `B` | `B. Medicaid` |
| baseline | `mmlu_6261` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6262` | `mcq` | false | `C` | `A. Ask about their satisfaction with life and offer to help.` |
| baseline | `mmlu_6263` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6264` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6265` | `mcq` | true | `B` | `B. Personal control` |
| baseline | `mmlu_6266` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6267` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6268` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6269` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6270` | `mcq` | true | `B` | `B. Cardiovascular disease` |
| baseline | `mmlu_6271` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6272` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6273` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_6274` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6275` | `mcq` | true | `C` | `C. More than 50%` |
| baseline | `mmlu_6276` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6277` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_6278` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6279` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6280` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6281` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6282` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6283` | `mcq` | false | `A` | `B. 82` |
| baseline | `mmlu_6284` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6285` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6286` | `mcq` | true | `A` | `A. Height` |
| baseline | `mmlu_6287` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6288` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6289` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6290` | `mcq` | true | `C` | `C. Pretty much stays the same` |
| baseline | `mmlu_6291` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6292` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6293` | `mcq` | true | `B` | `B. SOD` |
| baseline | `mmlu_6294` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6295` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6296` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6297` | `mcq` | false | `D` | `A. Discrimination` |
| baseline | `mmlu_6298` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6299` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6300` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6301` | `mcq` | false | `C` | `B. Is 65` |
| baseline | `mmlu_6302` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6303` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6304` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6305` | `mcq` | false | `D` | `C. Be less productive` |
| baseline | `mmlu_6306` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6307` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6308` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6309` | `mcq` | true | `A` | `A. Social support` |
| baseline | `mmlu_6310` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6311` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6312` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6313` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6314` | `mcq` | false | `A` | `A/B/C/D` |
| baseline | `mmlu_6315` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6316` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6317` | `mcq` | true | `C` | `C. experienced guilt` |
| baseline | `mmlu_6318` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6319` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6320` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6321` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6322` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6323` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_6324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6325` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6326` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6327` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6328` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6329` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6330` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6331` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6332` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6333` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6334` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6335` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6336` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6337` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6338` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6339` | `mcq` | true | `C` | `C. Hormones` |
| baseline | `mmlu_6340` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6341` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6342` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6343` | `mcq` | false | `D` | `B. immediately before orgasm` |
| baseline | `mmlu_6344` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6345` | `mcq` | false | `A` | `C. Swedish` |
| baseline | `mmlu_6346` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6347` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6348` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6349` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6350` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6351` | `mcq` | false | `D` | `C. sympathetic` |
| baseline | `mmlu_6352` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_6353` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6354` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6355` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6356` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6357` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6358` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6359` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6360` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6361` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6362` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6363` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6364` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6365` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6366` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6367` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6368` | `mcq` | true | `B` | `B. necrophilia` |
| baseline | `mmlu_6369` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6370` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6371` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6372` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6373` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_6374` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6376` | `mcq` | false | `B` | `C. 6` |
| baseline | `mmlu_6377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6378` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_6379` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6380` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6381` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6382` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6383` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6384` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_6385` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6386` | `mcq` | true | `D` | `D. gonorrhea` |
| baseline | `mmlu_6387` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6388` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6389` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_6390` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_6391` | `mcq` | false | `D` | `C. decreased sperm production` |
| baseline | `mmlu_6392` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6393` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6394` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6395` | `mcq` | false | `B` | `A. woman-on-top` |
| baseline | `mmlu_6396` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6397` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6398` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6399` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6401` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6402` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6403` | `mcq` | true | `B` | `B. reproduction` |
| baseline | `mmlu_6404` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6405` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6406` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_6407` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6408` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6409` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6410` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6411` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6412` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_6413` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6414` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6415` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6416` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_6417` | `mcq` | false | `B` | `C. 15` |
| baseline | `mmlu_6418` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_6419` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6420` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6421` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6422` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6423` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6424` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6425` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6426` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6427` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_6428` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6429` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6430` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_6431` | `mcq` | true | `A` | `A. directly into the bloodstream` |
| baseline | `mmlu_6432` | `mcq` | true | `A` | `A. 1` |
| baseline | `mmlu_6433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_6434` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6435` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_6436` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6437` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6438` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6439` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_6440` | `mcq` | false | `D` | `C. gonorrhea` |
| baseline | `mmlu_6441` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6442` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_6443` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6444` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6445` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6446` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6447` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6448` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6449` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6450` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6451` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6452` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6453` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_6454` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6455` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6456` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6457` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6459` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6460` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_6461` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6462` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6463` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6464` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6465` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6466` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6467` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6468` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6469` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6470` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_6471` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6472` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6473` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_6474` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6475` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6476` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6477` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6478` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6479` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6480` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6481` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6482` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6483` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_6484` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6485` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6486` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6487` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_6488` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_6489` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6490` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6491` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_6492` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6493` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_6494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_6495` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6496` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_6497` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_6498` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_6499` | `mcq` | true | `B` | `B` |
