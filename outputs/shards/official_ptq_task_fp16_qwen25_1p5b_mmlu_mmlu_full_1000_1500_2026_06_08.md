# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 264 / 500 | 0.5280 | 5.0129 | 0.427731 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_1000` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1001` | `mcq` | false | `C` | `D. M = 6, m = 4` |
| baseline | `mmlu_1002` | `mcq` | false | `C` | `D. I and III only` |
| baseline | `mmlu_1003` | `mcq` | false | `B` | `C. III only` |
| baseline | `mmlu_1004` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1005` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1006` | `mcq` | false | `D` | `B. III only` |
| baseline | `mmlu_1007` | `mcq` | false | `A` | `B. n + 1` |
| baseline | `mmlu_1008` | `mcq` | true | `A` | `A. 3` |
| baseline | `mmlu_1009` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_1010` | `mcq` | false | `A` | `C. III only` |
| baseline | `mmlu_1011` | `mcq` | true | `D` | `D. None of the above` |
| baseline | `mmlu_1012` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1013` | `mcq` | false | `B` | `D. context-free, but not regular` |
| baseline | `mmlu_1014` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1015` | `mcq` | false | `D` | `C. I and II only` |
| baseline | `mmlu_1016` | `mcq` | true | `D` | `D. One-time pad` |
| baseline | `mmlu_1017` | `mcq` | false | `B` | `A. Finding a longest simple cycle in G` |
| baseline | `mmlu_1018` | `mcq` | true | `A` | `A. Routing packets through the network` |
| baseline | `mmlu_1019` | `mcq` | false | `A` | `B. K-1/K` |
| baseline | `mmlu_1020` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1021` | `mcq` | true | `D` | `D. I and II` |
| baseline | `mmlu_1022` | `mcq` | true | `C` | `C. Symbol Table` |
| baseline | `mmlu_1023` | `mcq` | true | `D` | `D. Quicksort` |
| baseline | `mmlu_1024` | `mcq` | true | `D` | `D. II and III only` |
| baseline | `mmlu_1025` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1026` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1027` | `mcq` | true | `D` | `D. I, II, and IV` |
| baseline | `mmlu_1028` | `mcq` | false | `D` | `B. 999` |
| baseline | `mmlu_1029` | `mcq` | false | `A` | `D. I and III` |
| baseline | `mmlu_1030` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1031` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1032` | `mcq` | true | `C` | `C. Merge sort` |
| baseline | `mmlu_1033` | `mcq` | false | `D` | `A. 20 and 10 seconds` |
| baseline | `mmlu_1034` | `mcq` | false | `D` | `C. Two's complement and one's complement only` |
| baseline | `mmlu_1035` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1036` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1037` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1038` | `mcq` | false | `A` | `D. I and III` |
| baseline | `mmlu_1039` | `mcq` | false | `D` | `A. 1/(n^2)` |
| baseline | `mmlu_1040` | `mcq` | true | `D` | `D. I and II` |
| baseline | `mmlu_1041` | `mcq` | true | `C` | `C. III only` |
| baseline | `mmlu_1042` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1043` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1044` | `mcq` | true | `A` | `A. 0` |
| baseline | `mmlu_1045` | `mcq` | false | `D` | `C. I and II only` |
| baseline | `mmlu_1046` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1047` | `mcq` | false | `B` | `D. II and III only` |
| baseline | `mmlu_1048` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1049` | `mcq` | true | `C` | `C. Merge sort` |
| baseline | `mmlu_1050` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1051` | `mcq` | true | `C` | `C. 3` |
| baseline | `mmlu_1052` | `mcq` | true | `D` | `D. (I, II) and (I, III) only` |
| baseline | `mmlu_1053` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1054` | `mcq` | false | `B` | `A. k + 2` |
| baseline | `mmlu_1055` | `mcq` | false | `D` | `C. III only` |
| baseline | `mmlu_1056` | `mcq` | true | `D` | `D. II and III` |
| baseline | `mmlu_1057` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1058` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1059` | `mcq` | true | `A` | `A. Recursive procedures` |
| baseline | `mmlu_1060` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1061` | `mcq` | true | `C` | `C. Θ(n^2)` |
| baseline | `mmlu_1062` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1063` | `mcq` | false | `B` | `C. I and II only` |
| baseline | `mmlu_1064` | `mcq` | false | `B` | `C. 5/3` |
| baseline | `mmlu_1065` | `mcq` | true | `A` | `A. 0x01001234; page mapped with READ/WRITE access` |
| baseline | `mmlu_1066` | `mcq` | false | `D` | `C. I and III only` |
| baseline | `mmlu_1067` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1068` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1069` | `mcq` | true | `C` | `C. 100,000 bytes/ second` |
| baseline | `mmlu_1070` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_1071` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1072` | `mcq` | true | `A` | `A. n^m` |
| baseline | `mmlu_1073` | `mcq` | false | `B` | `D. 1/w + 1/x < 1/y + 1/z` |
| baseline | `mmlu_1074` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1075` | `mcq` | false | `D` | `B. 25%` |
| baseline | `mmlu_1076` | `mcq` | false | `B` | `A. I only` |
| baseline | `mmlu_1077` | `mcq` | false | `C` | `B. Maximum level of nesting` |
| baseline | `mmlu_1078` | `mcq` | true | `D` | `D. II and III` |
| baseline | `mmlu_1079` | `mcq` | true | `A` | `A. Round-robin` |
| baseline | `mmlu_1080` | `mcq` | false | `D` | `B. O(N log N)` |
| baseline | `mmlu_1081` | `mcq` | false | `D` | `C. 1 / 2` |
| baseline | `mmlu_1082` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1083` | `mcq` | false | `B` | `C. I and II only` |
| baseline | `mmlu_1084` | `mcq` | false | `C` | `A. 4` |
| baseline | `mmlu_1085` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1086` | `mcq` | false | `C` | `A. 0` |
| baseline | `mmlu_1087` | `mcq` | false | `C` | `B. 208/5` |
| baseline | `mmlu_1088` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1089` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1090` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1091` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1092` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1093` | `mcq` | true | `D` | `D. I and III` |
| baseline | `mmlu_1094` | `mcq` | true | `C` | `C. 1.6 microseconds` |
| baseline | `mmlu_1095` | `mcq` | true | `D` | `D. 99.80%` |
| baseline | `mmlu_1096` | `mcq` | false | `B` | `A. k = 0 and n = 1` |
| baseline | `mmlu_1097` | `mcq` | false | `D` | `B. 1` |
| baseline | `mmlu_1098` | `mcq` | false | `D` | `B. n = 1 and r = 7` |
| baseline | `mmlu_1099` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_1100` | `mcq` | false | `C` | `A. 2/69` |
| baseline | `mmlu_1101` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1102` | `mcq` | false | `C` | `B. 6*sqrt(2)` |
| baseline | `mmlu_1103` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1104` | `mcq` | false | `C` | `D. III only` |
| baseline | `mmlu_1105` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1106` | `mcq` | true | `D` | `D. 45` |
| baseline | `mmlu_1107` | `mcq` | true | `B` | `B. 15/64` |
| baseline | `mmlu_1108` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1109` | `mcq` | true | `B` | `B. 7` |
| baseline | `mmlu_1110` | `mcq` | false | `D` | `A. 0.64` |
| baseline | `mmlu_1111` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_1112` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_1113` | `mcq` | false | `C` | `A. -1/4` |
| baseline | `mmlu_1114` | `mcq` | false | `D` | `C. I and III only` |
| baseline | `mmlu_1115` | `mcq` | true | `A` | `A. 3` |
| baseline | `mmlu_1116` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1117` | `mcq` | false | `D` | `A. None` |
| baseline | `mmlu_1118` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_1119` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1120` | `mcq` | true | `B` | `B. True, False` |
| baseline | `mmlu_1121` | `mcq` | true | `D` | `D. III only` |
| baseline | `mmlu_1122` | `mcq` | false | `D` | `A. 9/2 days` |
| baseline | `mmlu_1123` | `mcq` | false | `A` | `C. sqrt(2)` |
| baseline | `mmlu_1124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1125` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1126` | `mcq` | false | `C` | `D. S(n) is not true for any n >= n0` |
| baseline | `mmlu_1127` | `mcq` | true | `B` | `B. (3/7, 3/14, 9/14)` |
| baseline | `mmlu_1128` | `mcq` | true | `B` | `B. For 3, 5, 7, and 11 only` |
| baseline | `mmlu_1129` | `mcq` | false | `C` | `D. 4` |
| baseline | `mmlu_1130` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_1131` | `mcq` | false | `D` | `B. (x^2 + y^2 + z^2)^2 = 8 + 36(x^2 + z^2)` |
| baseline | `mmlu_1132` | `mcq` | false | `A` | `D. y = x + 1` |
| baseline | `mmlu_1133` | `mcq` | true | `A` | `A. 2` |
| baseline | `mmlu_1134` | `mcq` | false | `A` | `B. True, False` |
| baseline | `mmlu_1135` | `mcq` | true | `C` | `C. 3` |
| baseline | `mmlu_1136` | `mcq` | false | `B` | `A. the entire real axis` |
| baseline | `mmlu_1137` | `mcq` | false | `D` | `B. cyclic` |
| baseline | `mmlu_1138` | `mcq` | false | `D` | `A. 3` |
| baseline | `mmlu_1139` | `mcq` | false | `A` | `C. I and II only` |
| baseline | `mmlu_1140` | `mcq` | false | `D` | `A. 1` |
| baseline | `mmlu_1141` | `mcq` | false | `A` | `B. True, False` |
| baseline | `mmlu_1142` | `mcq` | false | `B` | `C. π/3` |
| baseline | `mmlu_1143` | `mcq` | true | `B` | `B. pi` |
| baseline | `mmlu_1144` | `mcq` | true | `C` | `C. (I) and (IV)` |
| baseline | `mmlu_1145` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_1146` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_1147` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1148` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1149` | `mcq` | true | `C` | `C. 12*sqrt(3)` |
| baseline | `mmlu_1150` | `mcq` | false | `A` | `C. 8` |
| baseline | `mmlu_1151` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1152` | `mcq` | false | `B` | `A. 4` |
| baseline | `mmlu_1153` | `mcq` | true | `D` | `D. 0, 1, and 2 only` |
| baseline | `mmlu_1154` | `mcq` | false | `C` | `B. π` |
| baseline | `mmlu_1155` | `mcq` | true | `A` | `A. 9` |
| baseline | `mmlu_1156` | `mcq` | false | `B` | `A. None` |
| baseline | `mmlu_1157` | `mcq` | false | `A` | `C. 10^(20) - 2^(10)` |
| baseline | `mmlu_1158` | `mcq` | false | `A` | `D. Both (a) and (b).` |
| baseline | `mmlu_1159` | `mcq` | false | `D` | `C. 1/2` |
| baseline | `mmlu_1160` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_1161` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_1162` | `mcq` | false | `C` | `B. -2` |
| baseline | `mmlu_1163` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1164` | `mcq` | true | `A` | `A. π/3` |
| baseline | `mmlu_1165` | `mcq` | true | `A` | `A. Sunday` |
| baseline | `mmlu_1166` | `mcq` | false | `D` | `C. -8/(3π) cm/min` |
| baseline | `mmlu_1167` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1168` | `mcq` | false | `D` | `A. f(c)` |
| baseline | `mmlu_1169` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_1170` | `mcq` | false | `C` | `A. 1/(2e)` |
| baseline | `mmlu_1171` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1172` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1173` | `mcq` | true | `C` | `C. 0` |
| baseline | `mmlu_1174` | `mcq` | false | `B` | `A. x^2/9` |
| baseline | `mmlu_1175` | `mcq` | true | `B` | `B. True, False` |
| baseline | `mmlu_1176` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1177` | `mcq` | true | `B` | `B. 30` |
| baseline | `mmlu_1178` | `mcq` | false | `B` | `A. 4` |
| baseline | `mmlu_1179` | `mcq` | true | `C` | `C. 35` |
| baseline | `mmlu_1180` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1181` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1182` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1183` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_1184` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1185` | `mcq` | false | `C` | `A. G is abelian` |
| baseline | `mmlu_1186` | `mcq` | false | `B` | `A. -2` |
| baseline | `mmlu_1187` | `mcq` | false | `C` | `D. I and III only` |
| baseline | `mmlu_1188` | `mcq` | false | `C` | `B. 7/12` |
| baseline | `mmlu_1189` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1190` | `mcq` | true | `D` | `D. 32i` |
| baseline | `mmlu_1191` | `mcq` | false | `D` | `C. 0 or 1` |
| baseline | `mmlu_1192` | `mcq` | false | `C` | `A. closed` |
| baseline | `mmlu_1193` | `mcq` | true | `C` | `C. x^2 + y^2 = 9` |
| baseline | `mmlu_1194` | `mcq` | false | `D` | `C. 28` |
| baseline | `mmlu_1195` | `mcq` | true | `A` | `A. (1, 6)` |
| baseline | `mmlu_1196` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1197` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1198` | `mcq` | true | `D` | `D. I and III only` |
| baseline | `mmlu_1199` | `mcq` | false | `D` | `C. about 1 minute.` |
| baseline | `mmlu_1200` | `mcq` | true | `A` | `A. 13 m/s^2` |
| baseline | `mmlu_1201` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1202` | `mcq` | true | `A` | `A. Heart surgery patients who cannot run on treadmills may benefit from sauna use.` |
| baseline | `mmlu_1203` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1204` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1205` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1206` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1207` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1208` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1209` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1210` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1211` | `mcq` | false | `B` | `D. Not enough information given.` |
| baseline | `mmlu_1212` | `mcq` | true | `C` | `C. in the nucleus.` |
| baseline | `mmlu_1213` | `mcq` | true | `B` | `B. Transferase` |
| baseline | `mmlu_1214` | `mcq` | false | `B` | `C. Lower than the pOH` |
| baseline | `mmlu_1215` | `mcq` | true | `B` | `B. the entire DNA sequence of an organism.` |
| baseline | `mmlu_1216` | `mcq` | true | `C` | `C. I and III` |
| baseline | `mmlu_1217` | `mcq` | true | `D` | `D. bound to albumin.` |
| baseline | `mmlu_1218` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_1219` | `mcq` | true | `A` | `A. Osmosis` |
| baseline | `mmlu_1220` | `mcq` | true | `B` | `B. the components of the electron transport chain.` |
| baseline | `mmlu_1221` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1222` | `mcq` | false | `C` | `A. 941 Hz` |
| baseline | `mmlu_1223` | `mcq` | true | `D` | `D. a = g (sin ? – µ cos ?)` |
| baseline | `mmlu_1224` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1225` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1226` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1227` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1228` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1229` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1230` | `mcq` | false | `D` | `B. increasing respiration rate` |
| baseline | `mmlu_1231` | `mcq` | false | `B` | `A. One gram of glucose` |
| baseline | `mmlu_1232` | `mcq` | true | `D` | `D. increased oxygen binding to hemoglobin in the tissues.` |
| baseline | `mmlu_1233` | `mcq` | true | `D` | `D. More women are now engaged in sport.` |
| baseline | `mmlu_1234` | `mcq` | false | `D` | `C. Calcium-troponin interaction` |
| baseline | `mmlu_1235` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1236` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1237` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_1238` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1239` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1240` | `mcq` | false | `C` | `D. cannot be determined` |
| baseline | `mmlu_1241` | `mcq` | false | `D` | `C. 2CO2 and 12ATP` |
| baseline | `mmlu_1242` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1243` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1244` | `mcq` | true | `B` | `B. Maintains alveoli in an open state` |
| baseline | `mmlu_1245` | `mcq` | true | `C` | `C. 264g` |
| baseline | `mmlu_1246` | `mcq` | true | `D` | `D. Replenish fluids with filtered water.` |
| baseline | `mmlu_1247` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1248` | `mcq` | true | `C` | `C. 300 kJ` |
| baseline | `mmlu_1249` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1250` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1251` | `mcq` | true | `B` | `B. Insulin` |
| baseline | `mmlu_1252` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1253` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1254` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1255` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1256` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1257` | `mcq` | true | `D` | `D. I and IV` |
| baseline | `mmlu_1258` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1259` | `mcq` | false | `C` | `B. I and II only` |
| baseline | `mmlu_1260` | `mcq` | false | `D` | `A. 400 kJ/min.` |
| baseline | `mmlu_1261` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1262` | `mcq` | true | `B` | `B. An 86-year old male mayor who is revered in the community.` |
| baseline | `mmlu_1263` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1264` | `mcq` | true | `D` | `D. a lack of oxygen.` |
| baseline | `mmlu_1265` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1266` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1267` | `mcq` | false | `C` | `D. 4 minutes` |
| baseline | `mmlu_1268` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1269` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1270` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1271` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1272` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1273` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1274` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_1275` | `mcq` | true | `A` | `A. yields 8 molecules of acetyl-CoA and some ATP and water.` |
| baseline | `mmlu_1276` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1277` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1278` | `mcq` | false | `B` | `D. I and III and IV only` |
| baseline | `mmlu_1279` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1280` | `mcq` | true | `A` | `A. the nerve stimulus is removed.` |
| baseline | `mmlu_1281` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1282` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1283` | `mcq` | true | `A` | `A. deoxyribonucleic acid.` |
| baseline | `mmlu_1284` | `mcq` | false | `C` | `B. Narcissistic` |
| baseline | `mmlu_1285` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1286` | `mcq` | false | `B` | `A. Anal` |
| baseline | `mmlu_1287` | `mcq` | true | `A` | `A. Peptide bonds` |
| baseline | `mmlu_1288` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1289` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1290` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1291` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1292` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1293` | `mcq` | false | `A` | `D. He critiques his study methods and tries to find out which led to poor returns.` |
| baseline | `mmlu_1294` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_1295` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1296` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1298` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_1299` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1300` | `mcq` | true | `C` | `C. cytoplasm.` |
| baseline | `mmlu_1301` | `mcq` | true | `A` | `A. Hierarchical` |
| baseline | `mmlu_1302` | `mcq` | true | `A` | `A. Ammonia, hypoxanthine and uric acid.` |
| baseline | `mmlu_1303` | `mcq` | true | `D` | `D. phosphofructokinase.` |
| baseline | `mmlu_1304` | `mcq` | true | `C` | `C. failure of the ATP supply to match the demand.` |
| baseline | `mmlu_1305` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1307` | `mcq` | true | `A` | `A. slightly less than 20L` |
| baseline | `mmlu_1308` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1309` | `mcq` | true | `A` | `A. elevating the pH and buffering capacity of the extracellular fluid allowing a faster efflux of hydrogen ions from mus` |
| baseline | `mmlu_1310` | `mcq` | true | `D` | `D. Transgender, homosexual` |
| baseline | `mmlu_1311` | `mcq` | true | `C` | `C. Carnosine` |
| baseline | `mmlu_1312` | `mcq` | true | `B` | `B. Miss` |
| baseline | `mmlu_1313` | `mcq` | false | `A` | `C. Microculture` |
| baseline | `mmlu_1314` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1315` | `mcq` | true | `A` | `A. triplet sequences of nucleotide bases in mRNA or DNA.` |
| baseline | `mmlu_1316` | `mcq` | false | `B` | `D. Increases throughout the course of the game as the players become more fatigued.` |
| baseline | `mmlu_1317` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1318` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1319` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1320` | `mcq` | true | `B` | `B. phosphocreatine breakdown.` |
| baseline | `mmlu_1321` | `mcq` | false | `A` | `C. Active transport` |
| baseline | `mmlu_1322` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1323` | `mcq` | true | `C` | `C. I and III only` |
| baseline | `mmlu_1324` | `mcq` | true | `B` | `B. glucose-1-phosphate.` |
| baseline | `mmlu_1325` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1326` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1327` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_1328` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1329` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1330` | `mcq` | false | `D` | `C. Arginine` |
| baseline | `mmlu_1331` | `mcq` | true | `A` | `A. Thymine` |
| baseline | `mmlu_1332` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_1333` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1334` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_1335` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1336` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1337` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1338` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1339` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1340` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1341` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1342` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1343` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1344` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_1345` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1346` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1347` | `mcq` | false | `D` | `A. I, II, and III` |
| baseline | `mmlu_1348` | `mcq` | true | `A` | `A. ATP.` |
| baseline | `mmlu_1349` | `mcq` | true | `C` | `C. The primary transcripts of many genes can be spliced in various ways to produce different mRNAs, a process known as a` |
| baseline | `mmlu_1350` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1351` | `mcq` | true | `B` | `B. Steroid` |
| baseline | `mmlu_1352` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1353` | `mcq` | true | `A` | `A. I only` |
| baseline | `mmlu_1354` | `mcq` | false | `C` | `B. Decrease in histone deacetyltransferase activity` |
| baseline | `mmlu_1355` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1356` | `mcq` | true | `D` | `D. Amino acid` |
| baseline | `mmlu_1357` | `mcq` | true | `C` | `C. 29` |
| baseline | `mmlu_1358` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1359` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1360` | `mcq` | false | `D` | `C. 5 m/s` |
| baseline | `mmlu_1361` | `mcq` | false | `B` | `A. 6 ATP.` |
| baseline | `mmlu_1362` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1363` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1364` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1365` | `mcq` | true | `A` | `A. DNA polymerase I` |
| baseline | `mmlu_1366` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1367` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1368` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_1369` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1370` | `mcq` | false | `C` | `A. 500 nm` |
| baseline | `mmlu_1371` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1372` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1373` | `mcq` | true | `B` | `B. The Pauli exclusion principle` |
| baseline | `mmlu_1374` | `mcq` | false | `C` | `A. 1/2` |
| baseline | `mmlu_1375` | `mcq` | false | `D` | `B. V_0/3` |
| baseline | `mmlu_1376` | `mcq` | false | `A` | `C. 0.67mc^2` |
| baseline | `mmlu_1377` | `mcq` | true | `A` | `A. Planck’s constant` |
| baseline | `mmlu_1378` | `mcq` | false | `D` | `B. mc/(2^(1/2))` |
| baseline | `mmlu_1379` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1380` | `mcq` | false | `D` | `B. 0.048 m` |
| baseline | `mmlu_1381` | `mcq` | true | `D` | `D. Hall coefficient` |
| baseline | `mmlu_1382` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1383` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1384` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1385` | `mcq` | true | `B` | `B. The Pauli exclusion principle` |
| baseline | `mmlu_1386` | `mcq` | false | `A` | `C. 0.48 mJ` |
| baseline | `mmlu_1387` | `mcq` | false | `B` | `A. 1.6 ns` |
| baseline | `mmlu_1388` | `mcq` | false | `A` | `C. 0.67mc^2` |
| baseline | `mmlu_1389` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1390` | `mcq` | true | `D` | `D. 10` |
| baseline | `mmlu_1391` | `mcq` | false | `B` | `A. 0.25 mm` |
| baseline | `mmlu_1392` | `mcq` | true | `C` | `C. 2 x 10^-5 N` |
| baseline | `mmlu_1393` | `mcq` | true | `B` | `B. Hall coefficient` |
| baseline | `mmlu_1394` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1395` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_1396` | `mcq` | false | `B` | `A. 0.50c` |
| baseline | `mmlu_1397` | `mcq` | false | `B` | `A. deflected in the +x-direction` |
| baseline | `mmlu_1398` | `mcq` | false | `D` | `A. 0.04 V` |
| baseline | `mmlu_1399` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1400` | `mcq` | true | `D` | `D. The orbits would remain unchanged.` |
| baseline | `mmlu_1401` | `mcq` | false | `B` | `A. 414 Hz` |
| baseline | `mmlu_1402` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_1403` | `mcq` | false | `D` | `C. (3/2) k T` |
| baseline | `mmlu_1404` | `mcq` | true | `D` | `D. 5,000 s` |
| baseline | `mmlu_1405` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1406` | `mcq` | true | `A` | `A. Electron` |
| baseline | `mmlu_1407` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1408` | `mcq` | false | `D` | `B. 4` |
| baseline | `mmlu_1409` | `mcq` | true | `D` | `D. 4 W` |
| baseline | `mmlu_1410` | `mcq` | true | `B` | `B. 1.00032` |
| baseline | `mmlu_1411` | `mcq` | false | `C` | `B. 1 eV` |
| baseline | `mmlu_1412` | `mcq` | false | `B` | `A. 1/4` |
| baseline | `mmlu_1413` | `mcq` | false | `B` | `C. 300 nm` |
| baseline | `mmlu_1414` | `mcq` | false | `B` | `C. 1,100 J` |
| baseline | `mmlu_1415` | `mcq` | false | `C` | `B. 606 Hz` |
| baseline | `mmlu_1416` | `mcq` | false | `D` | `B. 288 m` |
| baseline | `mmlu_1417` | `mcq` | false | `D` | `C. 5/6 c` |
| baseline | `mmlu_1418` | `mcq` | false | `D` | `A. 0.1 GeV/c^2` |
| baseline | `mmlu_1419` | `mcq` | false | `B` | `D. 10,000` |
| baseline | `mmlu_1420` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1421` | `mcq` | true | `A` | `A. real` |
| baseline | `mmlu_1422` | `mcq` | false | `D` | `A. F_B = 1/4 F_A` |
| baseline | `mmlu_1423` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1424` | `mcq` | false | `D` | `B. 10%` |
| baseline | `mmlu_1425` | `mcq` | true | `C` | `C. 45°` |
| baseline | `mmlu_1426` | `mcq` | true | `D` | `D. Increases by a factor of 81.` |
| baseline | `mmlu_1427` | `mcq` | false | `D` | `A. 0.04 V` |
| baseline | `mmlu_1428` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1429` | `mcq` | true | `D` | `D. None` |
| baseline | `mmlu_1430` | `mcq` | true | `A` | `A. gamma rays` |
| baseline | `mmlu_1431` | `mcq` | false | `D` | `B. 196 Hz` |
| baseline | `mmlu_1432` | `mcq` | true | `D` | `D. 5` |
| baseline | `mmlu_1433` | `mcq` | true | `A` | `A. L_B = 4L_A` |
| baseline | `mmlu_1434` | `mcq` | false | `D` | `C.真空极化` |
| baseline | `mmlu_1435` | `mcq` | false | `B` | `A. 0.50c` |
| baseline | `mmlu_1436` | `mcq` | false | `A` | `C. 51.8 eV` |
| baseline | `mmlu_1437` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_1438` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1439` | `mcq` | false | `D` | `C. 10,000 J` |
| baseline | `mmlu_1440` | `mcq` | true | `C` | `C. 0.8c` |
| baseline | `mmlu_1441` | `mcq` | true | `C` | `C. 3 N` |
| baseline | `mmlu_1442` | `mcq` | true | `B` | `B. 0.5c` |
| baseline | `mmlu_1443` | `mcq` | true | `C` | `C. 1,000,000 J` |
| baseline | `mmlu_1444` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1445` | `mcq` | true | `C` | `C. 3 N` |
| baseline | `mmlu_1446` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_1447` | `mcq` | true | `D` | `D. 8k` |
| baseline | `mmlu_1448` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_1449` | `mcq` | false | `A` | `C. 10 mm` |
| baseline | `mmlu_1450` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_1451` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_1452` | `mcq` | false | `D` | `A. 588 Hz` |
| baseline | `mmlu_1453` | `mcq` | false | `A` | `C. decreased by a factor of 81` |
| baseline | `mmlu_1454` | `mcq` | true | `D` | `D. 4mc^2` |
| baseline | `mmlu_1455` | `mcq` | true | `D` | `D. Gas laser` |
| baseline | `mmlu_1456` | `mcq` | false | `D` | `C. 50%` |
| baseline | `mmlu_1457` | `mcq` | false | `D` | `B. 1,750 Hz` |
| baseline | `mmlu_1458` | `mcq` | false | `A` | `C. decreased by a factor of 81` |
| baseline | `mmlu_1459` | `mcq` | false | `B` | `A. 1/4` |
| baseline | `mmlu_1460` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_1461` | `mcq` | false | `A` | `C. 0.27 J` |
| baseline | `mmlu_1462` | `mcq` | false | `C` | `B. 1 eV` |
| baseline | `mmlu_1463` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1464` | `mcq` | true | `D` | `D. 19.6 m` |
| baseline | `mmlu_1465` | `mcq` | false | `C` | `B. 1/4` |
| baseline | `mmlu_1466` | `mcq` | false | `C` | `A. 500 nm` |
| baseline | `mmlu_1467` | `mcq` | true | `A` | `A. 2.5 * 10^-23 kg` |
| baseline | `mmlu_1468` | `mcq` | false | `B` | `D. 100 m/s north and 40 m/s down` |
| baseline | `mmlu_1469` | `mcq` | false | `A` | `D. 13.6 eV` |
| baseline | `mmlu_1470` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_1471` | `mcq` | true | `C` | `C. Whitebox` |
| baseline | `mmlu_1472` | `mcq` | false | `A` | `D. False, True` |
| baseline | `mmlu_1473` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_1474` | `mcq` | true | `A` | `A. Receiver` |
| baseline | `mmlu_1475` | `mcq` | true | `A` | `A. Troya` |
| baseline | `mmlu_1476` | `mcq` | true | `B` | `B. Buffer-overrun` |
| baseline | `mmlu_1477` | `mcq` | true | `A` | `A. all instructions that modify segment state` |
| baseline | `mmlu_1478` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1479` | `mcq` | true | `A` | `A. No string boundary checks in predefined functions` |
| baseline | `mmlu_1480` | `mcq` | true | `B` | `B. Authenticated` |
| baseline | `mmlu_1481` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1482` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_1483` | `mcq` | true | `C` | `C. Forward secrecy` |
| baseline | `mmlu_1484` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_1485` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_1486` | `mcq` | true | `B` | `B. Access Point` |
| baseline | `mmlu_1487` | `mcq` | true | `B` | `B. 128` |
| baseline | `mmlu_1488` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_1489` | `mcq` | false | `A` | `D. All of the above` |
| baseline | `mmlu_1490` | `mcq` | true | `D` | `D. Taking care to avoid activities during a penetration test that might attract attention, e.g., by operators or IDS ser` |
| baseline | `mmlu_1491` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_1492` | `mcq` | false | `C` | `D. Blinding adds a random amount of time to the decryption due to the multiplication and division by the blinding random` |
| baseline | `mmlu_1493` | `mcq` | true | `D` | `D. False, True` |
| baseline | `mmlu_1494` | `mcq` | true | `C` | `C. Key exchange` |
| baseline | `mmlu_1495` | `mcq` | true | `A` | `A. Silk Road` |
| baseline | `mmlu_1496` | `mcq` | true | `C` | `C. Dark web` |
| baseline | `mmlu_1497` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_1498` | `mcq` | true | `B` | `B. Sender’s Public key` |
| baseline | `mmlu_1499` | `mcq` | true | `C` | `C` |
