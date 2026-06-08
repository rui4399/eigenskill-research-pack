# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 166 / 500 | 0.3320 | 10.3285 | 0.198775 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_9000` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9001` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9002` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9003` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9004` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9005` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9006` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9007` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9008` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9009` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9010` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9011` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9012` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9013` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9014` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9015` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9016` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9017` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9018` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9019` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9020` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9021` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9022` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9023` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9024` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9025` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9026` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9027` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9028` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9029` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9030` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9031` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9032` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9033` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9034` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9035` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9036` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9037` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9038` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9039` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9040` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9041` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9042` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9043` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9044` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9045` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9046` | `mcq` | false | `C` | `Wrong, Not wrong` |
| baseline | `mmlu_9047` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9048` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9049` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9050` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9051` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9052` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9053` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9054` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9055` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9056` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9057` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9058` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9059` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9060` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9061` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9062` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9063` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9064` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9065` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9066` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9067` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9068` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9069` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9070` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9071` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9072` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9073` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9074` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9075` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9076` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9077` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9078` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9079` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9080` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9081` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9082` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9083` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9084` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9085` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9086` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9087` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9088` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9089` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9090` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9091` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9092` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9093` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9094` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9095` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9096` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9097` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9098` | `mcq` | false | `B` | `Wrong, Not wrong` |
| baseline | `mmlu_9099` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9100` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9101` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9102` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9103` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9104` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9105` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9106` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9107` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9108` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9109` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9110` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9111` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9112` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9113` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9114` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9115` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9116` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9117` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9118` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9119` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9120` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9121` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9122` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9123` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9124` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9125` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9126` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9127` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9128` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9129` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9130` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9131` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9132` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9133` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9134` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9135` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9136` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9137` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9138` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9139` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9140` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9141` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9142` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9143` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9144` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9145` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9146` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9147` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9148` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9149` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9150` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9151` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9152` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9153` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9154` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9155` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9156` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9157` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9158` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9159` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9160` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9161` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9162` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9163` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9164` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9165` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9166` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9167` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9168` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9169` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9170` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9171` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9172` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9173` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9174` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9175` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9176` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9177` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9178` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9179` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9180` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9181` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9182` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9183` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9184` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9185` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9186` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9187` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9188` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9189` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9190` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9191` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9192` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9193` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9194` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9195` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9196` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9197` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9198` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9199` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9200` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9201` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9202` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9203` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9204` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9205` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9206` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9207` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9208` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9209` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9210` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9211` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9212` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9213` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9214` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9215` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9216` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9217` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9218` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9219` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9220` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9221` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9222` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9223` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9224` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9225` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9226` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9227` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9228` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9229` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9230` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9231` | `mcq` | false | `D` | `Wrong, Not wrong` |
| baseline | `mmlu_9232` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9233` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9234` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9235` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9236` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9237` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9238` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9239` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9240` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9241` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9242` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9243` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9244` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9245` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9246` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9247` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9248` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9249` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9250` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9251` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9252` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9253` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9254` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9255` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9256` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9257` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9258` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9259` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9260` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9261` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9262` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9263` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9264` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9265` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9266` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9267` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9268` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9269` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9270` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9271` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9272` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9273` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9274` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9275` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9276` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9277` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9278` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9279` | `mcq` | false | `C` | `Wrong, Not wrong` |
| baseline | `mmlu_9280` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9281` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9282` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9283` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9284` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9285` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9286` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9287` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9288` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9289` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9290` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9291` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9292` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9293` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9294` | `mcq` | false | `A` | `Wrong, Not wrong` |
| baseline | `mmlu_9295` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9296` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9297` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9298` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9299` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9300` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9301` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9302` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9303` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9304` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9305` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9306` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9307` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9308` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9309` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9310` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9311` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9312` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9313` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9314` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9315` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9316` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9317` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9318` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9319` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9320` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9321` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9322` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9323` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9324` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9325` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9326` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9327` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9328` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9329` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9330` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9331` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9332` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9333` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9334` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9335` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9336` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9337` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9338` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9339` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9340` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9341` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9342` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9343` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9344` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9345` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9346` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9347` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9348` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9349` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9350` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9351` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9352` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9353` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9354` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9355` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9356` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9357` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9358` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9359` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9360` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9361` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9362` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9363` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9364` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9365` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9366` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9367` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9368` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9369` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9370` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9371` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9372` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9373` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9374` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9375` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9376` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9377` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9378` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9379` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9380` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9381` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9382` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9383` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9384` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9385` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9386` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9387` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9388` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9389` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9390` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9391` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9392` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9393` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9394` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9395` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9396` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9397` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9398` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9399` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9400` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9401` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9402` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9403` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9404` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9405` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9406` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9407` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_9408` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9409` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9410` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9411` | `mcq` | true | `A` | `A. Increased energy quantity/density and a more sedentary lifestyle` |
| baseline | `mmlu_9412` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9413` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9414` | `mcq` | true | `B` | `B. Oestrogen` |
| baseline | `mmlu_9415` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9416` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9417` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9418` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9419` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9420` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9421` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9422` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9423` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9424` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9425` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9426` | `mcq` | true | `A` | `A. China` |
| baseline | `mmlu_9427` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9428` | `mcq` | true | `B` | `B. Because blood haemoglobin levels can also respond to a variety of other factors and insults, such as lead poisoning, ` |
| baseline | `mmlu_9429` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9430` | `mcq` | true | `C` | `C. Both of the options given are correct.` |
| baseline | `mmlu_9431` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9432` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9433` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9434` | `mcq` | false | `D` | `A. Liver glycogen` |
| baseline | `mmlu_9435` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9436` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9437` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9438` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9439` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9440` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9441` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9442` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9443` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9444` | `mcq` | false | `D` | `A. Processed meat` |
| baseline | `mmlu_9445` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9446` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9447` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9448` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9449` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9450` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9451` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9452` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9453` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9454` | `mcq` | true | `B` | `B. 70%-75%` |
| baseline | `mmlu_9455` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9456` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9457` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9458` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9459` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9460` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9461` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9462` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9463` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9464` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9465` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9466` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9467` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9468` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9469` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9470` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9471` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9472` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9473` | `mcq` | true | `C` | `C. Meat and meat products` |
| baseline | `mmlu_9474` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9475` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9476` | `mcq` | false | `A` | `C. Approximately 50%` |
| baseline | `mmlu_9477` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9478` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9479` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9480` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9481` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9482` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9483` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9484` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9485` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9486` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9487` | `mcq` | false | `C` | `A. glucose` |
| baseline | `mmlu_9488` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9489` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9490` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9491` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9492` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9493` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9495` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9496` | `mcq` | false | `A` | `A, C` |
| baseline | `mmlu_9497` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9498` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9499` | `mcq` | true | `A` | `A` |
