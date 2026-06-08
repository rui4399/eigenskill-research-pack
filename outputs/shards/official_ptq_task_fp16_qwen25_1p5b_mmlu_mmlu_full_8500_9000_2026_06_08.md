# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 159 / 500 | 0.3180 | 5.9637 | 0.430353 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_8500` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8501` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_8502` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8503` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_8504` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_8505` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8506` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_8507` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8508` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8509` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_8510` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_8511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_8512` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_8513` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8514` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8515` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8516` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8517` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8518` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8519` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8520` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8521` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8522` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8523` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8524` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8525` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8526` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8527` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8528` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8529` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8530` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8531` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8532` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8533` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8534` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8535` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8536` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8537` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8538` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8539` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8540` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8541` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8542` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8543` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8544` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8545` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8546` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8547` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8548` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8549` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8550` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8551` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8552` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8553` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8554` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8555` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8556` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8557` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8558` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8559` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8560` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8561` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8562` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8563` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8564` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8565` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8566` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8567` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8568` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8569` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8570` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8571` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8572` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8573` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8574` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8575` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8576` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8577` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8578` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8579` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8580` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8581` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8582` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8583` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8584` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8585` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8586` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8587` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8588` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8589` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8590` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8591` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8592` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8593` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8594` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8595` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8596` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8597` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8598` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8599` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8600` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8601` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8602` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8603` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8604` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8605` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8606` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8607` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8608` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8609` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8610` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8611` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8612` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8613` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8614` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8615` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8616` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8617` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8618` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8619` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8620` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8621` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8622` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8623` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8624` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8625` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8626` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8627` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8628` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8629` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8630` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8631` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8632` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8633` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8634` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8635` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8636` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8637` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8638` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8639` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8640` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8641` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8642` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8643` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8644` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8645` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8646` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8647` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8648` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8649` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8650` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8651` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8652` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8653` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8654` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8655` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8656` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8657` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8658` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8659` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8660` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8661` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8662` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8663` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8664` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8665` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8666` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8667` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8668` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8669` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8670` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8671` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8672` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8673` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8674` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8675` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8676` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8677` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8678` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8679` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8680` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8681` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8682` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8683` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8684` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8685` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8686` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8687` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8688` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8689` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8690` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8691` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8692` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8693` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8694` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8695` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8696` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8697` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8698` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8699` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8700` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8701` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8702` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8703` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8704` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8705` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8706` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8707` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8708` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8709` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8710` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8711` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8712` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8713` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8714` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8715` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8716` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8717` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8718` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8719` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8720` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8721` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8722` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8723` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8724` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8725` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8726` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8727` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8728` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8729` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8730` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8731` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8732` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8733` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8734` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8735` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8736` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8737` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8738` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8739` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8740` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8741` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8742` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8743` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8744` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8745` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8746` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8747` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8748` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8749` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8750` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8751` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8752` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8753` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8754` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8755` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8756` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8757` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8758` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8759` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8760` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8761` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8762` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8763` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8764` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8765` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8766` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8767` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8768` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8769` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8770` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8771` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8772` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8773` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8774` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8775` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8776` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8777` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8778` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8779` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8780` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8781` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8782` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8783` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8784` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8785` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8786` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8787` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8788` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8789` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8790` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8791` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8792` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8793` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8794` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8795` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8796` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8797` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8798` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8799` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8800` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8801` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8802` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8803` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8804` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8805` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8806` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8807` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8808` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8809` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8810` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8811` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8812` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8813` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8814` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8815` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8816` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8817` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8818` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8819` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8820` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8821` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8822` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8823` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8824` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8825` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8826` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8827` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8828` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8829` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8830` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8831` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8832` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8833` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8834` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8835` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8836` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8837` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8838` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8839` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8840` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8841` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8842` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8843` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8844` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8845` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8846` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8847` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8848` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8849` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8850` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8851` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8852` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8853` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8854` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8855` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8856` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8857` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8858` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8859` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8860` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8861` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8862` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8863` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8864` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8865` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8866` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8867` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8868` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8869` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8870` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8871` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8872` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8873` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8874` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8875` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8876` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8877` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8878` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8879` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8880` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8881` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8882` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8883` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8884` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8885` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8886` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8887` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8888` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8889` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8890` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8891` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8892` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8893` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8894` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8895` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8896` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8897` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8898` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8899` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8900` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8901` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8902` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8903` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8904` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8905` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8906` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8907` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8908` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8909` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8910` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8911` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8912` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8913` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8914` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8915` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8916` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8917` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8918` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8919` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8920` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8921` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8922` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8923` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8924` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8925` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8926` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8927` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8928` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8929` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8930` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8931` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8932` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8933` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8934` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8935` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8936` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8937` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8938` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8939` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8940` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8941` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8942` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8943` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8944` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8945` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8946` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8947` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8948` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8949` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8950` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8951` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8952` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8953` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8954` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8955` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8956` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8957` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8958` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8959` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8960` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8961` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8962` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8963` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8964` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8965` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8966` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8967` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8968` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8969` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8970` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8971` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8972` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8973` | `mcq` | false | `B` | `A. Wrong, Wrong` |
| baseline | `mmlu_8974` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8975` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8976` | `mcq` | false | `D` | `A. Wrong, Wrong` |
| baseline | `mmlu_8977` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8978` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8979` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8980` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8981` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8982` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8983` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8984` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8985` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8986` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8987` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8988` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8989` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8990` | `mcq` | false | `A` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8991` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8992` | `mcq` | true | `A` | `A. Wrong, Wrong` |
| baseline | `mmlu_8993` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8994` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8995` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8996` | `mcq` | true | `B` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8997` | `mcq` | false | `C` | `A. Wrong, Wrong` |
| baseline | `mmlu_8998` | `mcq` | false | `C` | `B. Wrong, Not wrong` |
| baseline | `mmlu_8999` | `mcq` | false | `D` | `B. Wrong, Not wrong` |
