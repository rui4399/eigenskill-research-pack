# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 329 / 500 | 0.6580 | 4.8043 | 0.365087 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_9500` | `mcq` | false | `C` | `A. 0.900 g/cm3` |
| baseline | `mmlu_9501` | `mcq` | true | `B` | `B. The group of people that may experience the outcome we want to study.` |
| baseline | `mmlu_9502` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9503` | `mcq` | false | `C` | `D. All of the above` |
| baseline | `mmlu_9504` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9505` | `mcq` | false | `D` | `C. Increasing muscle glycogen use during exercise` |
| baseline | `mmlu_9506` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9507` | `mcq` | false | `B` | `C. Ketone bodies` |
| baseline | `mmlu_9508` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9509` | `mcq` | true | `B` | `B. Selenocysteine` |
| baseline | `mmlu_9510` | `mcq` | true | `D` | `D. Meat and Dairy products` |
| baseline | `mmlu_9511` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9512` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9513` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9514` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9515` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9516` | `mcq` | true | `D` | `D. Both a and c` |
| baseline | `mmlu_9517` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9518` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9519` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9520` | `mcq` | false | `A` | `B. Tryptophan` |
| baseline | `mmlu_9521` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9522` | `mcq` | true | `B` | `B. Dual-energy X-ray absorptiometry` |
| baseline | `mmlu_9523` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9524` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9525` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9526` | `mcq` | true | `D` | `D. 32` |
| baseline | `mmlu_9527` | `mcq` | true | `A` | `A. When intakes exceed established ULs (Upper Levels)` |
| baseline | `mmlu_9528` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9529` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9530` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9531` | `mcq` | true | `A` | `A. potassium` |
| baseline | `mmlu_9532` | `mcq` | false | `C` | `A. 75-95%` |
| baseline | `mmlu_9533` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9534` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9535` | `mcq` | true | `A` | `A. Hemoglobin A1c` |
| baseline | `mmlu_9536` | `mcq` | false | `D` | `A. Brain` |
| baseline | `mmlu_9537` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9538` | `mcq` | true | `B` | `B. They are all derived from plant foods` |
| baseline | `mmlu_9539` | `mcq` | true | `C` | `C. The plasma activity of alkaline phosphatase` |
| baseline | `mmlu_9540` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9541` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9542` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9543` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9544` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9545` | `mcq` | false | `B` | `A. 20%` |
| baseline | `mmlu_9546` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9547` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9548` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9549` | `mcq` | true | `A` | `A. Wernicke-Korsakoff syndrome` |
| baseline | `mmlu_9550` | `mcq` | true | `C` | `C. Cytosine` |
| baseline | `mmlu_9551` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9552` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9553` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9554` | `mcq` | true | `C` | `C. Four-compartment model` |
| baseline | `mmlu_9555` | `mcq` | true | `B` | `B. Cholesterol mainly occurs in the cell walls of mammalian cells` |
| baseline | `mmlu_9556` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9557` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9558` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9559` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9560` | `mcq` | false | `B` | `A. the muscle fibre` |
| baseline | `mmlu_9561` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9562` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9563` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9564` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9565` | `mcq` | true | `C` | `C. acetaldehyde` |
| baseline | `mmlu_9566` | `mcq` | true | `C` | `C. 1 unit of BMI` |
| baseline | `mmlu_9567` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9568` | `mcq` | false | `A` | `B. Chylomicrons and VLDL` |
| baseline | `mmlu_9569` | `mcq` | true | `A` | `A. Folate` |
| baseline | `mmlu_9570` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9571` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9572` | `mcq` | true | `B` | `B. Potassium` |
| baseline | `mmlu_9573` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9574` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9575` | `mcq` | true | `B` | `B. The MUST tool` |
| baseline | `mmlu_9576` | `mcq` | false | `C` | `D. DNA polymerase` |
| baseline | `mmlu_9577` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9578` | `mcq` | true | `B` | `B. The Mediterranean diet` |
| baseline | `mmlu_9579` | `mcq` | true | `A` | `A. DNMT1` |
| baseline | `mmlu_9580` | `mcq` | false | `B` | `A. 11%` |
| baseline | `mmlu_9581` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9582` | `mcq` | false | `B` | `A. 10` |
| baseline | `mmlu_9583` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9584` | `mcq` | true | `D` | `D. vitamin C and thiamin` |
| baseline | `mmlu_9585` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9586` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9587` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9588` | `mcq` | false | `B` | `C. Reduced gluconeogenesis` |
| baseline | `mmlu_9589` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9590` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9591` | `mcq` | true | `D` | `D. All of the options given.` |
| baseline | `mmlu_9592` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9593` | `mcq` | true | `D` | `D. All of the options given are correct` |
| baseline | `mmlu_9594` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9595` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9596` | `mcq` | true | `D` | `D. Iron deficiency` |
| baseline | `mmlu_9597` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9598` | `mcq` | true | `D` | `D. all of the options given are correct` |
| baseline | `mmlu_9599` | `mcq` | true | `D` | `D. All options given are correct` |
| baseline | `mmlu_9600` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9601` | `mcq` | true | `D` | `D. C20 and C22 polyunsaturated fatty acids` |
| baseline | `mmlu_9602` | `mcq` | false | `D` | `C. Aspartate` |
| baseline | `mmlu_9603` | `mcq` | true | `A` | `A. underwater weighing` |
| baseline | `mmlu_9604` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9605` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9606` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9607` | `mcq` | false | `C` | `D. Broccoli` |
| baseline | `mmlu_9608` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9609` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9610` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9611` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9612` | `mcq` | false | `C` | `B. 5.7` |
| baseline | `mmlu_9613` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_9614` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9615` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9616` | `mcq` | true | `D` | `D. BP < 130/80, Trig <150, LDL < 100` |
| baseline | `mmlu_9617` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9618` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9619` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9620` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9621` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9622` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9623` | `mcq` | false | `B` | `A. 30 to 50%` |
| baseline | `mmlu_9624` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9625` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9626` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9627` | `mcq` | true | `C` | `C. <10%` |
| baseline | `mmlu_9628` | `mcq` | true | `D` | `D. All of the options given are correct` |
| baseline | `mmlu_9629` | `mcq` | true | `D` | `D. All of the options given are correct` |
| baseline | `mmlu_9630` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9631` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9632` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9633` | `mcq` | true | `D` | `D. All of the above were among the causes.` |
| baseline | `mmlu_9634` | `mcq` | true | `C` | `C. The daily intake of the substance by humans consuming the food` |
| baseline | `mmlu_9635` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9636` | `mcq` | true | `D` | `D. All of the options listed are correct` |
| baseline | `mmlu_9637` | `mcq` | true | `B` | `B. Children with severe malnutrition or diarrhoea` |
| baseline | `mmlu_9638` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9639` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9640` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9641` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9642` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9643` | `mcq` | true | `D` | `D. Thiamin` |
| baseline | `mmlu_9644` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9645` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9646` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9647` | `mcq` | true | `C` | `C. Weight and height` |
| baseline | `mmlu_9648` | `mcq` | true | `D` | `D. Total urinary nitrogen excretion alone` |
| baseline | `mmlu_9649` | `mcq` | true | `C` | `C. VLDL` |
| baseline | `mmlu_9650` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9651` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9652` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9653` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9654` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9655` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9656` | `mcq` | true | `B` | `B. Dietary fiber` |
| baseline | `mmlu_9657` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9658` | `mcq` | true | `B` | `B. Leptin and ghrelin` |
| baseline | `mmlu_9659` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9660` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9661` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9662` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9663` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9664` | `mcq` | true | `C` | `C. High dose ß-carotene supplements` |
| baseline | `mmlu_9665` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9666` | `mcq` | true | `B` | `B. Muscle contains more water than fat` |
| baseline | `mmlu_9667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9668` | `mcq` | false | `D` | `B. Plasma free fatty acids` |
| baseline | `mmlu_9669` | `mcq` | false | `B` | `C. An additional 200 kCal throughout pregnancy` |
| baseline | `mmlu_9670` | `mcq` | true | `C` | `C. The time for blood to clot` |
| baseline | `mmlu_9671` | `mcq` | true | `D` | `D. All of the above` |
| baseline | `mmlu_9672` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9673` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_9674` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9675` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9676` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9677` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9678` | `mcq` | false | `A` | `C. Zinc` |
| baseline | `mmlu_9679` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9680` | `mcq` | true | `D` | `D. Food frequency questionnaire` |
| baseline | `mmlu_9681` | `mcq` | false | `B` | `A. 29` |
| baseline | `mmlu_9682` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_9683` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9684` | `mcq` | true | `D` | `D. Folate, vitamins B6 and B12` |
| baseline | `mmlu_9685` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9686` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9687` | `mcq` | true | `A` | `A. N-3 fatty acids` |
| baseline | `mmlu_9688` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9689` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9690` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9691` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9692` | `mcq` | true | `D` | `D. Cohort` |
| baseline | `mmlu_9693` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9694` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9695` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9696` | `mcq` | true | `C` | `C. Chylomicrons` |
| baseline | `mmlu_9697` | `mcq` | true | `A` | `A. Long-term intervention studies that have a large sample size with fracture as an endpoint` |
| baseline | `mmlu_9698` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9699` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9700` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9701` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9702` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9703` | `mcq` | false | `D` | `A. 60 g glucose per hour` |
| baseline | `mmlu_9704` | `mcq` | true | `B` | `B. Muscle glycogen` |
| baseline | `mmlu_9705` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9706` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9707` | `mcq` | true | `A` | `A. Acetaldehyde, acetate, Pyruvate, beta-hydroxybutyrate` |
| baseline | `mmlu_9708` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_9709` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9710` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9711` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9712` | `mcq` | true | `A` | `A. Mutans streptococci` |
| baseline | `mmlu_9713` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9714` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9715` | `mcq` | true | `D` | `D. the soul` |
| baseline | `mmlu_9716` | `mcq` | true | `D` | `D. a good will` |
| baseline | `mmlu_9717` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9718` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9719` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9721` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9722` | `mcq` | true | `A` | `A. knowledge` |
| baseline | `mmlu_9723` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9724` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9725` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9726` | `mcq` | false | `B` | `A. duty.` |
| baseline | `mmlu_9727` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9728` | `mcq` | false | `D` | `A. rational` |
| baseline | `mmlu_9729` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9730` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9731` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9732` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_9733` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9734` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9735` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9736` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9737` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9738` | `mcq` | true | `B` | `B. free and unhindered; servile and subject to hindrance` |
| baseline | `mmlu_9739` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9740` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9741` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9742` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9743` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9744` | `mcq` | true | `A` | `A. expression` |
| baseline | `mmlu_9745` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9746` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9747` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9748` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9749` | `mcq` | true | `B` | `B. the philosophical method` |
| baseline | `mmlu_9750` | `mcq` | false | `B` | `A. determine which one is objectively most pleasurable` |
| baseline | `mmlu_9751` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9752` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9753` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9754` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9755` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9756` | `mcq` | false | `C` | `B. He claims to have offered an account of just such a property.` |
| baseline | `mmlu_9757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9758` | `mcq` | true | `C` | `C. Socrates` |
| baseline | `mmlu_9759` | `mcq` | true | `D` | `D. greater and grander` |
| baseline | `mmlu_9760` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9761` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9762` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9763` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9764` | `mcq` | false | `D` | `C. loving God.` |
| baseline | `mmlu_9765` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9766` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9767` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9768` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9769` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9770` | `mcq` | true | `B` | `B. freedom of the will.` |
| baseline | `mmlu_9771` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9772` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9773` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9775` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9776` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9777` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9778` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9779` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9780` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9781` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9782` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9783` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9784` | `mcq` | true | `D` | `D. arbitrary` |
| baseline | `mmlu_9785` | `mcq` | true | `C` | `C. some good.` |
| baseline | `mmlu_9786` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9787` | `mcq` | false | `B` | `D. all of the above.` |
| baseline | `mmlu_9788` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9789` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9790` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9791` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9792` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9793` | `mcq` | true | `B` | `B. In case individuals, places, or organizations can be harmed through identification or disclosure of personal informat` |
| baseline | `mmlu_9794` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9795` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9796` | `mcq` | false | `B` | `C. both a and b.` |
| baseline | `mmlu_9797` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9798` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9799` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9800` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9801` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9802` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9803` | `mcq` | true | `C` | `C. reflecting on what we really think.` |
| baseline | `mmlu_9804` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9805` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9806` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9807` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9808` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9809` | `mcq` | true | `B` | `B. war` |
| baseline | `mmlu_9810` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9811` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9812` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9813` | `mcq` | false | `D` | `A. life.` |
| baseline | `mmlu_9814` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9815` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9816` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9817` | `mcq` | true | `A` | `A. entirely subjective` |
| baseline | `mmlu_9818` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9819` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_9820` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9821` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9822` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9823` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9824` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9825` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9826` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9827` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9828` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9829` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9830` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9831` | `mcq` | true | `D` | `D. reductio ad absurdum` |
| baseline | `mmlu_9832` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9833` | `mcq` | false | `B` | `C. God.` |
| baseline | `mmlu_9834` | `mcq` | true | `D` | `D. philosophers and nonphilosophers` |
| baseline | `mmlu_9835` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9836` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9837` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9838` | `mcq` | false | `B` | `A. the external view and the internal view` |
| baseline | `mmlu_9839` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9840` | `mcq` | true | `B` | `B. common` |
| baseline | `mmlu_9841` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9842` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9843` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9844` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9845` | `mcq` | true | `A` | `A. Because to know something that is false is to know no real thing, nothing (i.e., not to know at all).` |
| baseline | `mmlu_9846` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9847` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9848` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_9849` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9850` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9851` | `mcq` | true | `B` | `B. God` |
| baseline | `mmlu_9852` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9853` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_9854` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9855` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9856` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9857` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9858` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9859` | `mcq` | true | `D` | `D. no real concept at all.` |
| baseline | `mmlu_9860` | `mcq` | true | `D` | `D. no quality in things themselves` |
| baseline | `mmlu_9861` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9862` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9863` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9864` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9865` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9866` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9867` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9868` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9869` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9870` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9871` | `mcq` | true | `C` | `C. consequentialist` |
| baseline | `mmlu_9872` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9873` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9874` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9875` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9876` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9877` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9878` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9879` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9880` | `mcq` | true | `B` | `B. need not be performed before each action, but should always be kept in mind.` |
| baseline | `mmlu_9881` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9882` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_9883` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9884` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9885` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9886` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_9887` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9888` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9889` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9890` | `mcq` | false | `B` | `A. TRUE` |
| baseline | `mmlu_9891` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9892` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_9893` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9894` | `mcq` | true | `A` | `A. pain and pleasure.` |
| baseline | `mmlu_9895` | `mcq` | true | `C` | `C. soul-body dualism` |
| baseline | `mmlu_9896` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9897` | `mcq` | true | `D` | `D. enjoyments` |
| baseline | `mmlu_9898` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9899` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9900` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9901` | `mcq` | true | `A` | `A. easily procured.` |
| baseline | `mmlu_9902` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_9903` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9904` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9905` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9906` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9907` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9908` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9909` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9910` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_9911` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9912` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9913` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9914` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9915` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_9916` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9917` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9918` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9919` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9920` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9921` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9922` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9923` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9924` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9925` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9926` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_9927` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9928` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9929` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9930` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9931` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9932` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9933` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9934` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9935` | `mcq` | true | `C` | `C. He became religious.` |
| baseline | `mmlu_9936` | `mcq` | true | `D` | `D. Legalilty` |
| baseline | `mmlu_9937` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9938` | `mcq` | true | `D` | `D. war of every man against every man.` |
| baseline | `mmlu_9939` | `mcq` | true | `C` | `C. representation` |
| baseline | `mmlu_9940` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9941` | `mcq` | true | `C` | `C. exists only in the understanding` |
| baseline | `mmlu_9942` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9943` | `mcq` | true | `C` | `C. serves some important function` |
| baseline | `mmlu_9944` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9945` | `mcq` | true | `B` | `B. man` |
| baseline | `mmlu_9946` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9947` | `mcq` | false | `A` | `D. all of the above.` |
| baseline | `mmlu_9948` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_9949` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9950` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9951` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9952` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_9953` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_9954` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_9955` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_9956` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9957` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_9958` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_9959` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9960` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9961` | `mcq` | true | `C` | `C. formalism` |
| baseline | `mmlu_9962` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_9963` | `mcq` | false | `B` | `C. whether it violates any duties.` |
| baseline | `mmlu_9964` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9965` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9966` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9967` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9968` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9969` | `mcq` | true | `C` | `C. both a and b.` |
| baseline | `mmlu_9970` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_9971` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_9972` | `mcq` | false | `A` | `B. amoralists.` |
| baseline | `mmlu_9973` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9974` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_9975` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_9976` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_9977` | `mcq` | true | `A` | `A. cause behavior` |
| baseline | `mmlu_9978` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9979` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_9980` | `mcq` | false | `C` | `D. emotion.` |
| baseline | `mmlu_9981` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_9982` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9983` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_9984` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9985` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_9986` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_9987` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9988` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9989` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9990` | `mcq` | true | `D` | `D. all of the above.` |
| baseline | `mmlu_9991` | `mcq` | true | `C` | `C. substance dualism` |
| baseline | `mmlu_9992` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_9993` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9994` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_9995` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_9996` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_9997` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_9998` | `mcq` | true | `C` | `C. man is nothing else but what he makes of himself` |
| baseline | `mmlu_9999` | `mcq` | true | `A` | `A` |
