# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 304 / 500 | 0.6080 | 9.0087 | 0.181712 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_8000` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8001` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8002` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8003` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8004` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8005` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8006` | `mcq` | true | `B` | `B. 24` |
| baseline | `mmlu_8007` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8008` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8009` | `mcq` | true | `A` | `A. red` |
| baseline | `mmlu_8010` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8011` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8012` | `mcq` | false | `B` | `Five` |
| baseline | `mmlu_8013` | `mcq` | true | `B` | `B. rapid eye movement` |
| baseline | `mmlu_8014` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8015` | `mcq` | true | `D` | `D. Swee'pea` |
| baseline | `mmlu_8016` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8017` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8018` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8019` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8020` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8021` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8022` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8023` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8024` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8025` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8026` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8027` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8028` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8029` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8030` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8031` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8032` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8033` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8034` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8035` | `mcq` | true | `B` | `B. Olympus` |
| baseline | `mmlu_8036` | `mcq` | true | `B` | `B. Mary Had a Little Lamb'` |
| baseline | `mmlu_8037` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8038` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8039` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8040` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8041` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8042` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8043` | `mcq` | true | `C` | `C. chocolate` |
| baseline | `mmlu_8044` | `mcq` | true | `B` | `B. ceramic` |
| baseline | `mmlu_8045` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8046` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8047` | `mcq` | true | `C` | `C. Alan Shepard` |
| baseline | `mmlu_8048` | `mcq` | true | `A` | `A. Paul McCartney` |
| baseline | `mmlu_8049` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8050` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8051` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8052` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8053` | `mcq` | true | `D` | `D. French` |
| baseline | `mmlu_8054` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8055` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8056` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8057` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8058` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8059` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8060` | `mcq` | true | `D` | `D. Drag Racing` |
| baseline | `mmlu_8061` | `mcq` | false | `C` | `B. WB` |
| baseline | `mmlu_8062` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8063` | `mcq` | true | `D` | `D. Internet Service Provider` |
| baseline | `mmlu_8064` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8065` | `mcq` | false | `A` | `C. Friday` |
| baseline | `mmlu_8066` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8067` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8068` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8069` | `mcq` | false | `C` | `B. 1 billion cups per week` |
| baseline | `mmlu_8070` | `mcq` | true | `B` | `B. New York` |
| baseline | `mmlu_8071` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8072` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8073` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8074` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8075` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8076` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8077` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8078` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8079` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8080` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8081` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8082` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8083` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8084` | `mcq` | false | `C` | `A. About 0.1%` |
| baseline | `mmlu_8085` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8086` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8087` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8088` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8089` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8090` | `mcq` | true | `D` | `D. Pennsylvania` |
| baseline | `mmlu_8091` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8092` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8093` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8094` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8095` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8096` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8097` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8098` | `mcq` | true | `C` | `C. School` |
| baseline | `mmlu_8099` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8100` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8101` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8102` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8103` | `mcq` | true | `B` | `B. 23` |
| baseline | `mmlu_8104` | `mcq` | true | `A` | `A. ENIAC` |
| baseline | `mmlu_8105` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8106` | `mcq` | true | `D` | `D. Tensional` |
| baseline | `mmlu_8107` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8108` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8109` | `mcq` | true | `A` | `A. England` |
| baseline | `mmlu_8110` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8111` | `mcq` | true | `A` | `A. cursing them` |
| baseline | `mmlu_8112` | `mcq` | true | `B` | `B. Seine` |
| baseline | `mmlu_8113` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8114` | `mcq` | false | `A` | `B. The Attractions` |
| baseline | `mmlu_8115` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8116` | `mcq` | false | `C` | `D. Chicken pot pie` |
| baseline | `mmlu_8117` | `mcq` | true | `A` | `A. Chicago` |
| baseline | `mmlu_8118` | `mcq` | true | `A` | `A. White balance` |
| baseline | `mmlu_8119` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8120` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8121` | `mcq` | false | `B` | `C. Pictionary` |
| baseline | `mmlu_8122` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8123` | `mcq` | true | `C` | `C. Mixing vinegar with baking soda` |
| baseline | `mmlu_8124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8125` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8126` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8127` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8128` | `mcq` | false | `A` | `Japanese` |
| baseline | `mmlu_8129` | `mcq` | true | `C` | `C. Inca` |
| baseline | `mmlu_8130` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8131` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8132` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8133` | `mcq` | true | `B` | `B. oui` |
| baseline | `mmlu_8134` | `mcq` | true | `D` | `D. hoot` |
| baseline | `mmlu_8135` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8136` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8137` | `mcq` | true | `D` | `D. Diagnosis` |
| baseline | `mmlu_8138` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8139` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8140` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8141` | `mcq` | false | `D` | `A. politics` |
| baseline | `mmlu_8142` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8143` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8144` | `mcq` | true | `A` | `A. stationary bicycle` |
| baseline | `mmlu_8145` | `mcq` | false | `C` | `B. Empire State Building` |
| baseline | `mmlu_8146` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8147` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8148` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8149` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8150` | `mcq` | true | `C` | `C. New York Yankees` |
| baseline | `mmlu_8151` | `mcq` | true | `A` | `A. Law of Inertia` |
| baseline | `mmlu_8152` | `mcq` | false | `D` | `B. Sheryl Swoopes` |
| baseline | `mmlu_8153` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8154` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8155` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8156` | `mcq` | true | `C` | `C. Land of Enchantment'` |
| baseline | `mmlu_8157` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8158` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8159` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8160` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8161` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8163` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8164` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8165` | `mcq` | true | `A` | `A. Philadelphia` |
| baseline | `mmlu_8166` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8167` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8168` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8169` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8170` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8171` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8172` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8173` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8174` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8175` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8176` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8177` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8178` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8179` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8180` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8181` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8182` | `mcq` | true | `C` | `C. both of the above` |
| baseline | `mmlu_8183` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8184` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8185` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8186` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8187` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8188` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8189` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8190` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8191` | `mcq` | false | `B` | `A. Identical treatment.` |
| baseline | `mmlu_8192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8193` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8194` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8195` | `mcq` | false | `C` | `D. All of the above` |
| baseline | `mmlu_8196` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8197` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8198` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8199` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8200` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8201` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8202` | `mcq` | false | `A` | `D. none of the above.` |
| baseline | `mmlu_8203` | `mcq` | false | `C` | `B. 52 percent` |
| baseline | `mmlu_8204` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8205` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8206` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8208` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8209` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8210` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8211` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8212` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8213` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8214` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8215` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8216` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8217` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8218` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8219` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8220` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8221` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8222` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8223` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8224` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8225` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8226` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8227` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8228` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8229` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8230` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8231` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8232` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8233` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8234` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8235` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8236` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8237` | `mcq` | true | `C` | `C. Activities.` |
| baseline | `mmlu_8238` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8239` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8240` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8241` | `mcq` | true | `B` | `B. including bodily harm to persons and the destruction of property.` |
| baseline | `mmlu_8242` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8244` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8245` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8246` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8247` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8248` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8249` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8250` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8251` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8252` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8253` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8254` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8255` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8256` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8257` | `mcq` | true | `B` | `B. letting die.` |
| baseline | `mmlu_8258` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8259` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8260` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8261` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8262` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8263` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8264` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8265` | `mcq` | true | `B` | `B. least` |
| baseline | `mmlu_8266` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8267` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8268` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8269` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8270` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8271` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8272` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8273` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8274` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8275` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8276` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8277` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8278` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8279` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8280` | `mcq` | false | `C` | `A. life.` |
| baseline | `mmlu_8281` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8282` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8283` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8284` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8285` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8286` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8287` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8288` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8289` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8290` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8291` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8292` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8293` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8294` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8295` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8297` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8298` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8299` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8300` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8301` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8302` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8303` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8304` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8305` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8306` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8307` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8308` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8309` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8310` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8311` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8312` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8313` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8314` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8316` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8317` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8318` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8319` | `mcq` | false | `C` | `B. positive duties towards the global poor.` |
| baseline | `mmlu_8320` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8321` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8322` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8323` | `mcq` | true | `B` | `B. honesty` |
| baseline | `mmlu_8324` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8325` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8326` | `mcq` | false | `A` | `B. handing out too much foreign aid, which increases need.` |
| baseline | `mmlu_8327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8328` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8329` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8330` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8331` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8332` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8333` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8334` | `mcq` | true | `B` | `B. "ought."` |
| baseline | `mmlu_8335` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8336` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8337` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8338` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8339` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8340` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8341` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8342` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8343` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8344` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8345` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8346` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8347` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8348` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8349` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8350` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8351` | `mcq` | false | `C` | `A. He would say this begs the question because the immigration question is identical to the freedom-of-movement question` |
| baseline | `mmlu_8352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8353` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8354` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8355` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8356` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8357` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8358` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8359` | `mcq` | true | `B` | `B. Obesity` |
| baseline | `mmlu_8360` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8361` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8362` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8363` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8364` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8365` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8366` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8367` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8368` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8369` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8370` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8371` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8372` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8373` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8374` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8376` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8377` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8378` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8379` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8380` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8381` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8382` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8383` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8384` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8385` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8386` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8387` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8388` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8389` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8390` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8391` | `mcq` | true | `D` | `D. pollution.` |
| baseline | `mmlu_8392` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8393` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8394` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8395` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8396` | `mcq` | true | `A` | `A. must not conflict with the rights and duties that liberal egalitarianism itself prescribes.` |
| baseline | `mmlu_8397` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8398` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8399` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8400` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8401` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8402` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8403` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8404` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8405` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8406` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8407` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8408` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8409` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8410` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8411` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8412` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8413` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8414` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8415` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8416` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8417` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8418` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8419` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8420` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8421` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8422` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8423` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8424` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8425` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8426` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8427` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8428` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8429` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8430` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8431` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8432` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8433` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8434` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8435` | `mcq` | true | `C` | `C. Membership in a legitimate self-governing community.` |
| baseline | `mmlu_8436` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8437` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8438` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8439` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8440` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8441` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8442` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8443` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8444` | `mcq` | false | `B` | `D. A and B are equally good athletes.` |
| baseline | `mmlu_8445` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8446` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8447` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8448` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8449` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8450` | `mcq` | false | `C` | `D. none of the above` |
| baseline | `mmlu_8451` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8452` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8453` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8454` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8455` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8456` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8457` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8458` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8459` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8460` | `mcq` | false | `B` | `C. dichotomous thinking` |
| baseline | `mmlu_8461` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8462` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8463` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8464` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8465` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8466` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8467` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8468` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8470` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8471` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8472` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8473` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8474` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8475` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8476` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8477` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8478` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8479` | `mcq` | true | `C` | `C. Both A and B` |
| baseline | `mmlu_8480` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8481` | `mcq` | true | `A` | `A. exclude` |
| baseline | `mmlu_8482` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8483` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8484` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8485` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8486` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8487` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8488` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8489` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8490` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8491` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8492` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8493` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8494` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8495` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8496` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8497` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8498` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8499` | `mcq` | false | `B` | `C` |
