# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 321 / 500 | 0.6420 | 4.9305 | 0.364909 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_8000` | `mcq` | true | `D` | `D. atheist` |
| baseline | `mmlu_8001` | `mcq` | false | `B` | `C. Bugs Bunny` |
| baseline | `mmlu_8002` | `mcq` | true | `B` | `B. chitlins` |
| baseline | `mmlu_8003` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8004` | `mcq` | true | `D` | `D. Financial Industry Regulatory Authority` |
| baseline | `mmlu_8005` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8006` | `mcq` | false | `B` | `D. 42` |
| baseline | `mmlu_8007` | `mcq` | true | `C` | `C. copperhead` |
| baseline | `mmlu_8008` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8009` | `mcq` | true | `A` | `A. red` |
| baseline | `mmlu_8010` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8011` | `mcq` | true | `D` | `D. antihistamines` |
| baseline | `mmlu_8012` | `mcq` | false | `B` | `A. Two` |
| baseline | `mmlu_8013` | `mcq` | true | `B` | `B. rapid eye movement` |
| baseline | `mmlu_8014` | `mcq` | true | `B` | `B. Prince William Sound` |
| baseline | `mmlu_8015` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8016` | `mcq` | true | `A` | `A. Describing and mapping the building types on a plat map` |
| baseline | `mmlu_8017` | `mcq` | true | `A` | `A. in glass-paneled cases` |
| baseline | `mmlu_8018` | `mcq` | true | `B` | `B. a shaker of salt` |
| baseline | `mmlu_8019` | `mcq` | true | `B` | `B. Decreasing the discount rate to member banks` |
| baseline | `mmlu_8020` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8021` | `mcq` | false | `D` | `A. red` |
| baseline | `mmlu_8022` | `mcq` | true | `D` | `D. pumice` |
| baseline | `mmlu_8023` | `mcq` | true | `C` | `C. Ann Landers` |
| baseline | `mmlu_8024` | `mcq` | true | `A` | `A. How the products and services will be priced` |
| baseline | `mmlu_8025` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8026` | `mcq` | true | `B` | `B. 33 1/3 rpm` |
| baseline | `mmlu_8027` | `mcq` | true | `B` | `B. War of 1812` |
| baseline | `mmlu_8028` | `mcq` | true | `D` | `D. Huey Dewey Louie` |
| baseline | `mmlu_8029` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8030` | `mcq` | true | `C` | `C. The site might belong to a nonprofit agency.` |
| baseline | `mmlu_8031` | `mcq` | false | `B` | `A. 11` |
| baseline | `mmlu_8032` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8033` | `mcq` | false | `D` | `C. black and white` |
| baseline | `mmlu_8034` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8035` | `mcq` | true | `B` | `B. Olympus` |
| baseline | `mmlu_8036` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8037` | `mcq` | false | `D` | `B. Jennifer Grey` |
| baseline | `mmlu_8038` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8039` | `mcq` | true | `B` | `B. trepanation` |
| baseline | `mmlu_8040` | `mcq` | false | `B` | `A. Jim Davis` |
| baseline | `mmlu_8041` | `mcq` | false | `B` | `D. guajillo` |
| baseline | `mmlu_8042` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8043` | `mcq` | true | `C` | `C. chocolate` |
| baseline | `mmlu_8044` | `mcq` | true | `B` | `B. ceramic` |
| baseline | `mmlu_8045` | `mcq` | true | `C` | `C. glaucoma` |
| baseline | `mmlu_8046` | `mcq` | true | `C` | `C. scarf` |
| baseline | `mmlu_8047` | `mcq` | true | `C` | `C. Alan Shepard` |
| baseline | `mmlu_8048` | `mcq` | true | `A` | `A. Paul McCartney` |
| baseline | `mmlu_8049` | `mcq` | true | `A` | `A. Outer core` |
| baseline | `mmlu_8050` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8051` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8052` | `mcq` | true | `A` | `A. musical instrument` |
| baseline | `mmlu_8053` | `mcq` | true | `D` | `D. French` |
| baseline | `mmlu_8054` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8055` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8056` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8057` | `mcq` | true | `B` | `B. bogey` |
| baseline | `mmlu_8058` | `mcq` | false | `C` | `B. Farrah Fawcett` |
| baseline | `mmlu_8059` | `mcq` | true | `C` | `C. George Bernard Shaw` |
| baseline | `mmlu_8060` | `mcq` | true | `D` | `D. drag racing` |
| baseline | `mmlu_8061` | `mcq` | true | `C` | `C. MTV` |
| baseline | `mmlu_8062` | `mcq` | false | `B` | `D. Fannie Mae` |
| baseline | `mmlu_8063` | `mcq` | true | `D` | `D. Internet Service Provider` |
| baseline | `mmlu_8064` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8065` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8066` | `mcq` | true | `A` | `A. Bill Viola` |
| baseline | `mmlu_8067` | `mcq` | true | `B` | `B. The sudden demise of the dinosaurs` |
| baseline | `mmlu_8068` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8069` | `mcq` | true | `C` | `C. 3 billion cups per week` |
| baseline | `mmlu_8070` | `mcq` | true | `B` | `B. New York` |
| baseline | `mmlu_8071` | `mcq` | false | `C` | `D. silver` |
| baseline | `mmlu_8072` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8073` | `mcq` | true | `B` | `B. chicken` |
| baseline | `mmlu_8074` | `mcq` | true | `B` | `B. electric current` |
| baseline | `mmlu_8075` | `mcq` | true | `A` | `A. effective depth` |
| baseline | `mmlu_8076` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8077` | `mcq` | true | `A` | `A. visa` |
| baseline | `mmlu_8078` | `mcq` | true | `A` | `A. Ganymede` |
| baseline | `mmlu_8079` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8080` | `mcq` | true | `A` | `A. Perskippity` |
| baseline | `mmlu_8081` | `mcq` | false | `A` | `C. Larrabee` |
| baseline | `mmlu_8082` | `mcq` | true | `B` | `B. trifecta` |
| baseline | `mmlu_8083` | `mcq` | true | `A` | `A. entropy` |
| baseline | `mmlu_8084` | `mcq` | false | `C` | `A. About 0.1%` |
| baseline | `mmlu_8085` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8086` | `mcq` | true | `A` | `A. transpiration` |
| baseline | `mmlu_8087` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8088` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8089` | `mcq` | true | `D` | `D. goalkeeper` |
| baseline | `mmlu_8090` | `mcq` | false | `D` | `A. California` |
| baseline | `mmlu_8091` | `mcq` | true | `C` | `C. magic carpet` |
| baseline | `mmlu_8092` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8093` | `mcq` | true | `C` | `C. hinny` |
| baseline | `mmlu_8094` | `mcq` | true | `A` | `A. Carbon dioxide` |
| baseline | `mmlu_8095` | `mcq` | false | `D` | `C. wabe` |
| baseline | `mmlu_8096` | `mcq` | false | `D` | `A. America` |
| baseline | `mmlu_8097` | `mcq` | true | `D` | `D. Espy` |
| baseline | `mmlu_8098` | `mcq` | true | `C` | `C. School` |
| baseline | `mmlu_8099` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8100` | `mcq` | true | `C` | `C. about 1000 miles per hour` |
| baseline | `mmlu_8101` | `mcq` | false | `D` | `B. Reservoir` |
| baseline | `mmlu_8102` | `mcq` | true | `C` | `C. prevent business behavior that hampers competition` |
| baseline | `mmlu_8103` | `mcq` | true | `B` | `B. 23` |
| baseline | `mmlu_8104` | `mcq` | true | `A` | `A. ENIAC` |
| baseline | `mmlu_8105` | `mcq` | true | `A` | `A. condensation` |
| baseline | `mmlu_8106` | `mcq` | true | `D` | `D. Tensional` |
| baseline | `mmlu_8107` | `mcq` | true | `B` | `B. Greenware` |
| baseline | `mmlu_8108` | `mcq` | true | `B` | `B. 1929` |
| baseline | `mmlu_8109` | `mcq` | true | `A` | `A. England` |
| baseline | `mmlu_8110` | `mcq` | true | `C` | `C. Flora` |
| baseline | `mmlu_8111` | `mcq` | true | `A` | `A. cursing them` |
| baseline | `mmlu_8112` | `mcq` | true | `B` | `B. Seine` |
| baseline | `mmlu_8113` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8114` | `mcq` | false | `A` | `B. The Attractions` |
| baseline | `mmlu_8115` | `mcq` | true | `B` | `B. Riverdale High` |
| baseline | `mmlu_8116` | `mcq` | false | `C` | `D. Chicken pot pie` |
| baseline | `mmlu_8117` | `mcq` | true | `A` | `A. Chicago` |
| baseline | `mmlu_8118` | `mcq` | true | `A` | `A. White balance` |
| baseline | `mmlu_8119` | `mcq` | false | `B` | `C. 40 mph` |
| baseline | `mmlu_8120` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8121` | `mcq` | false | `B` | `C. Pictionary` |
| baseline | `mmlu_8122` | `mcq` | false | `D` | `A. wrestling` |
| baseline | `mmlu_8123` | `mcq` | true | `C` | `C. Mixing vinegar with baking soda` |
| baseline | `mmlu_8124` | `mcq` | true | `A` | `A. Arrangement of soil particles` |
| baseline | `mmlu_8125` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8126` | `mcq` | true | `C` | `C. electric guitar` |
| baseline | `mmlu_8127` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8128` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8129` | `mcq` | true | `C` | `C. Inca` |
| baseline | `mmlu_8130` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8131` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8132` | `mcq` | true | `A` | `A. gingham` |
| baseline | `mmlu_8133` | `mcq` | true | `B` | `B. oui` |
| baseline | `mmlu_8134` | `mcq` | true | `D` | `D. hoot` |
| baseline | `mmlu_8135` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8136` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8137` | `mcq` | true | `D` | `D. Diagnosis` |
| baseline | `mmlu_8138` | `mcq` | true | `C` | `C. Sinn Fein` |
| baseline | `mmlu_8139` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8140` | `mcq` | false | `C` | `B. Correct use of incisors while eating` |
| baseline | `mmlu_8141` | `mcq` | false | `D` | `A. politics` |
| baseline | `mmlu_8142` | `mcq` | false | `D` | `B. Freckles` |
| baseline | `mmlu_8143` | `mcq` | true | `D` | `D. An extruder` |
| baseline | `mmlu_8144` | `mcq` | true | `A` | `A. stationary bicycle` |
| baseline | `mmlu_8145` | `mcq` | false | `C` | `B. Empire State Building` |
| baseline | `mmlu_8146` | `mcq` | false | `C` | `A. baking soda` |
| baseline | `mmlu_8147` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8148` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8149` | `mcq` | true | `C` | `C. The effect the plant will have on the environment` |
| baseline | `mmlu_8150` | `mcq` | true | `C` | `C. New York Yankees` |
| baseline | `mmlu_8151` | `mcq` | true | `A` | `A. Law of Inertia` |
| baseline | `mmlu_8152` | `mcq` | false | `D` | `B. Sheryl Swoopes` |
| baseline | `mmlu_8153` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8154` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8155` | `mcq` | true | `A` | `A. Zaire` |
| baseline | `mmlu_8156` | `mcq` | true | `C` | `C. Land of Enchantment'` |
| baseline | `mmlu_8157` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8158` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8159` | `mcq` | true | `A` | `A. Nautilus` |
| baseline | `mmlu_8160` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8161` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8163` | `mcq` | false | `B` | `D. Jupiter and Saturn` |
| baseline | `mmlu_8164` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8165` | `mcq` | true | `A` | `A. Philadelphia` |
| baseline | `mmlu_8166` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8167` | `mcq` | true | `A` | `A. jus in bello.` |
| baseline | `mmlu_8168` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8169` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8170` | `mcq` | true | `C` | `C. both its quantity and its quality.` |
| baseline | `mmlu_8171` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8172` | `mcq` | true | `C` | `C. somatic cell nuclear transfer` |
| baseline | `mmlu_8173` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8174` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8175` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8176` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8177` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8178` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8179` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8180` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8181` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8182` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8183` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8184` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8185` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8186` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8187` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8188` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8189` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8190` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8191` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8192` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8193` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8194` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8195` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8196` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8197` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8198` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8199` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8200` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8201` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8202` | `mcq` | false | `A` | `D. none of the above.` |
| baseline | `mmlu_8203` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8204` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8205` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8206` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8208` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8209` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8210` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8211` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8212` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8213` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8214` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8215` | `mcq` | true | `B` | `B. an actual or hypothetical social agreement of some sort.` |
| baseline | `mmlu_8216` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8217` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8218` | `mcq` | false | `B` | `D. All of the above.` |
| baseline | `mmlu_8219` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8220` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8221` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8222` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8223` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8224` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8225` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8226` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8227` | `mcq` | false | `D` | `A. murder` |
| baseline | `mmlu_8228` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8229` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8230` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8231` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8232` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8233` | `mcq` | false | `B` | `A. just war theory.` |
| baseline | `mmlu_8234` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8235` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8236` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8237` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8238` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8239` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8240` | `mcq` | true | `B` | `B. consequentialist theory` |
| baseline | `mmlu_8241` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8242` | `mcq` | true | `D` | `D. none of the above` |
| baseline | `mmlu_8243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8244` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8245` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8246` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8247` | `mcq` | true | `C` | `C. desirable as a means.` |
| baseline | `mmlu_8248` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8249` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8250` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8251` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8252` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8253` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8254` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_8255` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8256` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8257` | `mcq` | true | `B` | `B. letting die.` |
| baseline | `mmlu_8258` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8259` | `mcq` | false | `B` | `D. all of the above` |
| baseline | `mmlu_8260` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8261` | `mcq` | false | `A` | `B. by eliminating the patient's capacity for self-determination` |
| baseline | `mmlu_8262` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8263` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8264` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8265` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8266` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8267` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8268` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8269` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8270` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8271` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8272` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8273` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8274` | `mcq` | false | `C` | `D. none of the above` |
| baseline | `mmlu_8275` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8276` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8277` | `mcq` | false | `B` | `A. direct moral standing.` |
| baseline | `mmlu_8278` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_8279` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8280` | `mcq` | false | `C` | `A. life.` |
| baseline | `mmlu_8281` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8282` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8283` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8284` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8285` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8286` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8287` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8288` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8289` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8290` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8291` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8292` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8293` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8294` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8295` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8297` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8298` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_8299` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8300` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_8301` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8302` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8303` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8304` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8305` | `mcq` | false | `C` | `D. John Stuart Mill` |
| baseline | `mmlu_8306` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8307` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8308` | `mcq` | false | `C` | `D. virtue.` |
| baseline | `mmlu_8309` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8310` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8311` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8312` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8313` | `mcq` | false | `C` | `D. all of the above` |
| baseline | `mmlu_8314` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8316` | `mcq` | true | `C` | `C. embryonic stage` |
| baseline | `mmlu_8317` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8318` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_8319` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8320` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8321` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8322` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8323` | `mcq` | true | `B` | `B. honesty` |
| baseline | `mmlu_8324` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8325` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8326` | `mcq` | true | `A` | `A. causing global warming.` |
| baseline | `mmlu_8327` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8328` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8329` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8330` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8331` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8332` | `mcq` | true | `C` | `C. sentience` |
| baseline | `mmlu_8333` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8334` | `mcq` | true | `B` | `B. "ought."` |
| baseline | `mmlu_8335` | `mcq` | false | `A` | `B. minimize distorted thinking.` |
| baseline | `mmlu_8336` | `mcq` | true | `C` | `C. virtue ethics approach` |
| baseline | `mmlu_8337` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8338` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8339` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8340` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8341` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8342` | `mcq` | false | `C` | `D. all of the above.` |
| baseline | `mmlu_8343` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8344` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8345` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8346` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8347` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8348` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8349` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8350` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8351` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8353` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8354` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_8355` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8356` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8357` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8358` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_8359` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8360` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8361` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8362` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8363` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_8364` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8365` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8366` | `mcq` | true | `A` | `A. "good is to be done, evil to be avoided."` |
| baseline | `mmlu_8367` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8368` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8369` | `mcq` | true | `C` | `C. it would lead to a "tragedy of the commons."` |
| baseline | `mmlu_8370` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8371` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8372` | `mcq` | false | `C` | `A. "something bad"` |
| baseline | `mmlu_8373` | `mcq` | false | `C` | `B. the pursuit of justice by marking out racism, sexism, and classism.` |
| baseline | `mmlu_8374` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8376` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8377` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8378` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8379` | `mcq` | false | `C` | `D. legislators` |
| baseline | `mmlu_8380` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8381` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8382` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8383` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8384` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8385` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8386` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8387` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8388` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8389` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8390` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8391` | `mcq` | true | `D` | `D. pollution.` |
| baseline | `mmlu_8392` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8393` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8394` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8395` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_8396` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8397` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8398` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8399` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8400` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8401` | `mcq` | true | `C` | `C. we do not know whether wasteful driving is wrong.` |
| baseline | `mmlu_8402` | `mcq` | true | `B` | `B. Kantianism` |
| baseline | `mmlu_8403` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_8404` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8405` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_8406` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8407` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8408` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8409` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8410` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8411` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_8412` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8413` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8414` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8415` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_8416` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_8417` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_8418` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8419` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8420` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8421` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8422` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8423` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8424` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8425` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8426` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8427` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8428` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8429` | `mcq` | true | `A` | `A. those who value a strong right to privacy` |
| baseline | `mmlu_8430` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8431` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_8432` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8433` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8434` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8435` | `mcq` | true | `C` | `C. membership in a legitimate self-governing community.` |
| baseline | `mmlu_8436` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8437` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8438` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8439` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8440` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8441` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8442` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8443` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8444` | `mcq` | false | `B` | `D. A and B are equally good athletes.` |
| baseline | `mmlu_8445` | `mcq` | false | `D` | `C. both causal and expressive harm` |
| baseline | `mmlu_8446` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_8447` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8448` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8449` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8450` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8451` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_8452` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8453` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8454` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8455` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8456` | `mcq` | true | `C` | `C. consider such speech hate speech.` |
| baseline | `mmlu_8457` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8458` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8459` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8460` | `mcq` | false | `B` | `C. dichotomous thinking` |
| baseline | `mmlu_8461` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8462` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8463` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8464` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8465` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_8466` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8467` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8468` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_8469` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_8470` | `mcq` | true | `C` | `C. active/passive euthanasia` |
| baseline | `mmlu_8471` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8472` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_8473` | `mcq` | true | `D` | `D. dignity.` |
| baseline | `mmlu_8474` | `mcq` | true | `C` | `C. distributive` |
| baseline | `mmlu_8475` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8476` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8477` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_8478` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8479` | `mcq` | true | `C` | `C` |
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
| baseline | `mmlu_8490` | `mcq` | false | `B` | `A. freedom of speech` |
| baseline | `mmlu_8491` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8492` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_8493` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_8494` | `mcq` | true | `A` | `A. The SCNT individual has genetic material primarily from one person instead of two.` |
| baseline | `mmlu_8495` | `mcq` | false | `C` | `D. all of the above` |
| baseline | `mmlu_8496` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_8497` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8498` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_8499` | `mcq` | false | `B` | `C.` |
