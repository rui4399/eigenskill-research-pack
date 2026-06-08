# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 288 / 500 | 0.5760 | 11.0274 | 0.139941 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_10000` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10001` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10002` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10003` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10004` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10005` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10006` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10007` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10008` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10009` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10010` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10011` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10012` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10013` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10014` | `mcq` | true | `C` | `C. identity theory` |
| baseline | `mmlu_10015` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10016` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10017` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10018` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10019` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10020` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10021` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10022` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10023` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10024` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10025` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10026` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10027` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10028` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10029` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10030` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10031` | `mcq` | false | `C` | `B. random scratches and not a meaningful script or written language.` |
| baseline | `mmlu_10032` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10033` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10034` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10035` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10036` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10037` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10038` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10039` | `mcq` | true | `C` | `C. Lapita` |
| baseline | `mmlu_10040` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10041` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10042` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10043` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10044` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10045` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10046` | `mcq` | false | `B` | `D. Nenana Complex` |
| baseline | `mmlu_10047` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10048` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10049` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10050` | `mcq` | false | `B` | `C. 4,000 B.P.` |
| baseline | `mmlu_10051` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10052` | `mcq` | false | `A` | `B. 12,000 B.P.` |
| baseline | `mmlu_10053` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10054` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10055` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10056` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10057` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10058` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10059` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10060` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10061` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10062` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10063` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10064` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10065` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10066` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10067` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10068` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10069` | `mcq` | false | `A` | `D. all of the above` |
| baseline | `mmlu_10070` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10071` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10072` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10073` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10074` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10075` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10076` | `mcq` | true | `B` | `B. potatoes` |
| baseline | `mmlu_10077` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10078` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10079` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10080` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10081` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10082` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10083` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10084` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10085` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10086` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10087` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10088` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10089` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10090` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10091` | `mcq` | true | `B` | `B. 200,000 people.` |
| baseline | `mmlu_10092` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10093` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10094` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_10095` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10096` | `mcq` | true | `B` | `B. petroglyph.` |
| baseline | `mmlu_10097` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10098` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10099` | `mcq` | false | `B` | `D. all of the above` |
| baseline | `mmlu_10100` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10101` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10102` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10103` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10104` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10105` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10106` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10107` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10108` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10109` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10110` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10111` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10112` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10113` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10114` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10115` | `mcq` | true | `D` | `D. catastrophist.` |
| baseline | `mmlu_10116` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10117` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10118` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10119` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10120` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10121` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10122` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10123` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10124` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10125` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10126` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10127` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10128` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10129` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10130` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10131` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10132` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10133` | `mcq` | true | `D` | `D. China.` |
| baseline | `mmlu_10134` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10135` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10136` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10137` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10138` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10139` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10140` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10141` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10142` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10143` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10144` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10145` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10146` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10147` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10148` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10149` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_10150` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10151` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10152` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10153` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10154` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10155` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10156` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10157` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10158` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10159` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10160` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10161` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10162` | `mcq` | false | `D` | `C. largest` |
| baseline | `mmlu_10163` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10164` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10165` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10166` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10167` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10168` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10169` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10170` | `mcq` | true | `C` | `C. Thule` |
| baseline | `mmlu_10171` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10172` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10173` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10174` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10175` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10176` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10177` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10178` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10179` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10180` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10181` | `mcq` | false | `D` | `B. about half way through the film` |
| baseline | `mmlu_10182` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10183` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10184` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10185` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10186` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10187` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10188` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10189` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10190` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10191` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10192` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10193` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10194` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_10195` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10196` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10197` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10198` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10199` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10200` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10201` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10202` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_10203` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10204` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10205` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10206` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10207` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10208` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10209` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_10210` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10211` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10212` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10213` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10214` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10215` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_10216` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10217` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10218` | `mcq` | true | `C` | `C. Thule` |
| baseline | `mmlu_10219` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10220` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10221` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10222` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10223` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10224` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10225` | `mcq` | true | `C` | `C. site.` |
| baseline | `mmlu_10226` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10227` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10228` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10229` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10230` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10231` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10232` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10233` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10234` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10235` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10236` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10237` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10238` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10239` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10240` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10241` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10242` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10243` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10244` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10245` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10246` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10247` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10248` | `mcq` | true | `D` | `D. Mesopotamia` |
| baseline | `mmlu_10249` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10250` | `mcq` | true | `C` | `C. the foramen magnum` |
| baseline | `mmlu_10251` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10252` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10253` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10254` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10255` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10256` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10257` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10258` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10259` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10260` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10261` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10262` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10263` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10264` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10265` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10266` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10267` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10268` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10269` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10270` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10271` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10272` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10273` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10274` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10275` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10276` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10277` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10278` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10279` | `mcq` | true | `C` | `C. 1450 A.D.` |
| baseline | `mmlu_10280` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10281` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10282` | `mcq` | true | `D` | `D. all the above` |
| baseline | `mmlu_10283` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10284` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10285` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10286` | `mcq` | false | `C` | `B. Inca` |
| baseline | `mmlu_10287` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10288` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10289` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10290` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10291` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10292` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10293` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10294` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10295` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10296` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10297` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10298` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10299` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10300` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10301` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10302` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_10303` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10304` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10305` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10306` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10307` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10308` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10309` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10310` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10311` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10312` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10313` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10314` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_10315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10316` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10317` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10318` | `mcq` | true | `D` | `D. cave paintings` |
| baseline | `mmlu_10319` | `mcq` | true | `B` | `B. just after A.D. 1000` |
| baseline | `mmlu_10320` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10321` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10322` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10323` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10324` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10325` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10326` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10328` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10329` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10330` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10331` | `mcq` | false | `A` | `D. Australia` |
| baseline | `mmlu_10332` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10333` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10334` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10335` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10336` | `mcq` | true | `D` | `D. All the above` |
| baseline | `mmlu_10337` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10338` | `mcq` | true | `D` | `D. Asia` |
| baseline | `mmlu_10339` | `mcq` | false | `C` | `B. 100,000 years` |
| baseline | `mmlu_10340` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10341` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10342` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10343` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10344` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10345` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10346` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10347` | `mcq` | true | `B` | `B. 3100 B.P.` |
| baseline | `mmlu_10348` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10349` | `mcq` | false | `A` | `B. 1.64%` |
| baseline | `mmlu_10350` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10351` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10352` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10353` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10354` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10355` | `mcq` | false | `D` | `B. Understated Overstated` |
| baseline | `mmlu_10356` | `mcq` | false | `D` | `B. $104.29` |
| baseline | `mmlu_10357` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10358` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10359` | `mcq` | false | `D` | `A. $100` |
| baseline | `mmlu_10360` | `mcq` | false | `B` | `A. $0` |
| baseline | `mmlu_10361` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10362` | `mcq` | true | `B` | `B. $22,500` |
| baseline | `mmlu_10363` | `mcq` | false | `C` | `A. $100 billion` |
| baseline | `mmlu_10364` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10365` | `mcq` | false | `C` | `B. $25,000` |
| baseline | `mmlu_10366` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10367` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10368` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10369` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10370` | `mcq` | false | `D` | `A. 600` |
| baseline | `mmlu_10371` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10372` | `mcq` | true | `C` | `C. $830,000` |
| baseline | `mmlu_10373` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10374` | `mcq` | false | `B` | `C. $0 $1200` |
| baseline | `mmlu_10375` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10376` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10377` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10378` | `mcq` | true | `C` | `C. $82` |
| baseline | `mmlu_10379` | `mcq` | true | `B` | `B. $492,500` |
| baseline | `mmlu_10380` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10381` | `mcq` | false | `A` | `D. A B and C.` |
| baseline | `mmlu_10382` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10383` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10384` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10385` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10386` | `mcq` | false | `C` | `B. 8.50%` |
| baseline | `mmlu_10387` | `mcq` | false | `D` | `B. 6.25 percent` |
| baseline | `mmlu_10388` | `mcq` | false | `D` | `A. $25000 $25000 $0` |
| baseline | `mmlu_10389` | `mcq` | false | `C` | `B. $5,000` |
| baseline | `mmlu_10390` | `mcq` | true | `D` | `D. $242,000` |
| baseline | `mmlu_10391` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10392` | `mcq` | true | `A` | `A. January.` |
| baseline | `mmlu_10393` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10394` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10395` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10396` | `mcq` | false | `B` | `A. $0` |
| baseline | `mmlu_10397` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_10398` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10399` | `mcq` | false | `A` | `B. (2,2),(2,3),(4,2)` |
| baseline | `mmlu_10400` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10401` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10402` | `mcq` | false | `D` | `C. Six months.` |
| baseline | `mmlu_10403` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10404` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10405` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10406` | `mcq` | true | `D` | `D. $8,500,000` |
| baseline | `mmlu_10407` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_10408` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_10409` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10410` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10411` | `mcq` | false | `D` | `B. $280,000` |
| baseline | `mmlu_10412` | `mcq` | false | `A` | `B. $19,000` |
| baseline | `mmlu_10413` | `mcq` | false | `B` | `A. $0` |
| baseline | `mmlu_10414` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10415` | `mcq` | true | `C` | `C. $14,000` |
| baseline | `mmlu_10416` | `mcq` | false | `C` | `B. $150,000` |
| baseline | `mmlu_10417` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10418` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10419` | `mcq` | false | `B` | `A. 36000` |
| baseline | `mmlu_10420` | `mcq` | false | `C` | `B. $100,276` |
| baseline | `mmlu_10421` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10422` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10423` | `mcq` | false | `B` | `C. $5.00` |
| baseline | `mmlu_10424` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10425` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10426` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_10427` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10428` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10429` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_10430` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_10431` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10432` | `mcq` | false | `B` | `A. $2.69` |
| baseline | `mmlu_10433` | `mcq` | true | `C` | `C. $5,333` |
| baseline | `mmlu_10434` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10435` | `mcq` | false | `A` | `C. $62.50` |
| baseline | `mmlu_10436` | `mcq` | false | `C` | `B. $7,000` |
| baseline | `mmlu_10437` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10438` | `mcq` | false | `B` | `A. $23.22` |
| baseline | `mmlu_10439` | `mcq` | false | `D` | `C. January 31, year 3.` |
| baseline | `mmlu_10440` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10441` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10442` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_10443` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10444` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10445` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10446` | `mcq` | true | `B` | `B. Sunk costs` |
| baseline | `mmlu_10447` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10448` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10449` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10450` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10451` | `mcq` | true | `C` | `C. $480,000.00` |
| baseline | `mmlu_10452` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10453` | `mcq` | true | `A` | `A. $10,000` |
| baseline | `mmlu_10454` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10455` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_10456` | `mcq` | true | `A` | `A. 9.4% and 11.2%` |
| baseline | `mmlu_10457` | `mcq` | true | `B` | `B. $644,000` |
| baseline | `mmlu_10458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_10459` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10460` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10461` | `mcq` | true | `D` | `D. Monitoring.` |
| baseline | `mmlu_10462` | `mcq` | false | `B` | `A. $50` |
| baseline | `mmlu_10463` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10464` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10465` | `mcq` | false | `A` | `B. Yes No` |
| baseline | `mmlu_10466` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10467` | `mcq` | true | `C` | `C. $140,000` |
| baseline | `mmlu_10468` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10469` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10470` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_10471` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10472` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10473` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_10474` | `mcq` | false | `D` | `C. 7.4` |
| baseline | `mmlu_10475` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10476` | `mcq` | false | `A` | `B. Higher Higher` |
| baseline | `mmlu_10477` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_10478` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_10479` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10480` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_10481` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_10482` | `mcq` | false | `C` | `A. $0` |
| baseline | `mmlu_10483` | `mcq` | false | `D` | `A. $0` |
| baseline | `mmlu_10484` | `mcq` | false | `B` | `A. $0` |
| baseline | `mmlu_10485` | `mcq` | false | `C` | `B. $560,000` |
| baseline | `mmlu_10486` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_10487` | `mcq` | false | `B` | `A. -$9,500` |
| baseline | `mmlu_10488` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_10489` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_10490` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_10491` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_10492` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_10493` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10494` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_10495` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_10496` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_10497` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_10498` | `mcq` | true | `A` | `A. $12.20` |
| baseline | `mmlu_10499` | `mcq` | false | `A` | `B. $118,500` |
