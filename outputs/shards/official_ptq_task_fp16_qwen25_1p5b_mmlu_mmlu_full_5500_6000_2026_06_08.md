# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 335 / 500 | 0.6700 | 4.6768 | 0.415551 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_5500` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5501` | `mcq` | false | `B` | `C. I and III` |
| baseline | `mmlu_5502` | `mcq` | true | `C` | `C. Use of a confounding variable to control the placebo effect` |
| baseline | `mmlu_5503` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5504` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5505` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5506` | `mcq` | false | `D` | `B. 5.290 pounds` |
| baseline | `mmlu_5507` | `mcq` | true | `B` | `B. The distribution of the sample proportion will be less spread out.` |
| baseline | `mmlu_5508` | `mcq` | false | `D` | `B. 8.0%` |
| baseline | `mmlu_5509` | `mcq` | false | `C` | `B. 67 pounds` |
| baseline | `mmlu_5510` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5512` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5513` | `mcq` | false | `C` | `B. 17.1%` |
| baseline | `mmlu_5514` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5515` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5516` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5517` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5518` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5519` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5520` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5521` | `mcq` | false | `C` | `B. An unnecessary stoppage of the production process` |
| baseline | `mmlu_5522` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_5523` | `mcq` | true | `D` | `D. None of the above are true statements.` |
| baseline | `mmlu_5524` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5525` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5526` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5527` | `mcq` | false | `D` | `B. The correlation coefficient is 0.71.` |
| baseline | `mmlu_5528` | `mcq` | true | `D` | `D. No, because not every group of 30 employees has the same chance of being selected.` |
| baseline | `mmlu_5529` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5530` | `mcq` | true | `C` | `C. Selection bias makes this a poorly designed survey.` |
| baseline | `mmlu_5531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5532` | `mcq` | false | `D` | `A. 0.313` |
| baseline | `mmlu_5533` | `mcq` | true | `A` | `A. 6` |
| baseline | `mmlu_5534` | `mcq` | false | `C` | `B. 53 minutes to 281 minutes` |
| baseline | `mmlu_5535` | `mcq` | true | `B` | `B. Her grade will go up by 20.4 points.` |
| baseline | `mmlu_5536` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5537` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5538` | `mcq` | true | `A` | `A. by blocking on exercise intensity` |
| baseline | `mmlu_5539` | `mcq` | false | `C` | `B. 18%` |
| baseline | `mmlu_5540` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5541` | `mcq` | true | `D` | `D. Follow up with those that did not return the survey to encourage them to respond.` |
| baseline | `mmlu_5542` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5543` | `mcq` | true | `A` | `A. 0.235` |
| baseline | `mmlu_5544` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5545` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5546` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5547` | `mcq` | true | `D` | `D. The answer cannot be determined without knowing the size of the jury pool.` |
| baseline | `mmlu_5548` | `mcq` | false | `D` | `B. 144` |
| baseline | `mmlu_5549` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5550` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5551` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5552` | `mcq` | true | `C` | `C. For both companies, the probability that a fuse will last at least 1 hour is 0.159` |
| baseline | `mmlu_5553` | `mcq` | true | `D` | `D. We are 90% confident that the difference in proportions between Toyota and Subaru car owners who are satisfied with t` |
| baseline | `mmlu_5554` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5555` | `mcq` | true | `C` | `C. The number of successes and the number of failures for the two groups are not all large enough.` |
| baseline | `mmlu_5556` | `mcq` | false | `B` | `C. 12 - 2.576(0.3) ounces` |
| baseline | `mmlu_5557` | `mcq` | false | `D` | `A. 66.80%` |
| baseline | `mmlu_5558` | `mcq` | false | `D` | `B. 0.1667` |
| baseline | `mmlu_5559` | `mcq` | true | `D` | `D. The player will lose about $1.44.` |
| baseline | `mmlu_5560` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5561` | `mcq` | false | `D` | `B. 0.34` |
| baseline | `mmlu_5562` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5563` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5564` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5565` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5566` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5567` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5568` | `mcq` | true | `B` | `B. Because tis less extreme than the critical value of t for 17 degrees of freedom, he should not reject the null hypoth` |
| baseline | `mmlu_5569` | `mcq` | true | `B` | `B. All county residents` |
| baseline | `mmlu_5570` | `mcq` | true | `D` | `D. No, because not every sample of the intended size has an equal chance of being selected.` |
| baseline | `mmlu_5571` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5572` | `mcq` | false | `D` | `A. 0.42` |
| baseline | `mmlu_5573` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5574` | `mcq` | false | `C` | `B. Dialysis center: Type I error, towel manufacturer: Type II error` |
| baseline | `mmlu_5575` | `mcq` | false | `A` | `B. Cluster sample, because the population is divided into five clusters—namely, five offices in five different countries` |
| baseline | `mmlu_5576` | `mcq` | false | `D` | `C. 0.8` |
| baseline | `mmlu_5577` | `mcq` | true | `D` | `D. The median of all the salaries.` |
| baseline | `mmlu_5578` | `mcq` | true | `D` | `D. No, because the entire population information was used from both offices. Because no samples were taken, a t-test sho` |
| baseline | `mmlu_5579` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5580` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5581` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5582` | `mcq` | true | `C` | `C. P(t > 2) with 15 degrees of freedom` |
| baseline | `mmlu_5583` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5584` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5585` | `mcq` | false | `C` | `B. μ = 15,100; σ = 6200` |
| baseline | `mmlu_5586` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5587` | `mcq` | false | `D` | `C. 118 points` |
| baseline | `mmlu_5588` | `mcq` | true | `C` | `C. if n is large, no matter what the distribution of the original population.` |
| baseline | `mmlu_5589` | `mcq` | false | `B` | `D. All of the above are valid conclusions.` |
| baseline | `mmlu_5590` | `mcq` | false | `B` | `A. $6,984` |
| baseline | `mmlu_5591` | `mcq` | false | `C` | `A. 8.05` |
| baseline | `mmlu_5592` | `mcq` | true | `D` | `D. An experiment` |
| baseline | `mmlu_5593` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5594` | `mcq` | false | `B` | `A. 0.78` |
| baseline | `mmlu_5595` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5596` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5597` | `mcq` | true | `D` | `D. 0.74` |
| baseline | `mmlu_5598` | `mcq` | true | `D` | `D. Interquartile range` |
| baseline | `mmlu_5599` | `mcq` | false | `C` | `B. reduce confounding.` |
| baseline | `mmlu_5600` | `mcq` | false | `B` | `D. Independent samples comparison of population means` |
| baseline | `mmlu_5601` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5602` | `mcq` | true | `A` | `A. 0.0057` |
| baseline | `mmlu_5603` | `mcq` | true | `C` | `C. Stratified sample` |
| baseline | `mmlu_5604` | `mcq` | false | `D` | `A. 0.07` |
| baseline | `mmlu_5605` | `mcq` | false | `C` | `A. 1536` |
| baseline | `mmlu_5606` | `mcq` | true | `B` | `B. The sample mean and sample median are equal.` |
| baseline | `mmlu_5607` | `mcq` | true | `A` | `A. (3,034, 3,466)` |
| baseline | `mmlu_5608` | `mcq` | false | `D` | `B. 0.540` |
| baseline | `mmlu_5609` | `mcq` | false | `A` | `C. Closing the park when the lead levels are in excess of the allowed limit` |
| baseline | `mmlu_5610` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5611` | `mcq` | false | `C` | `B. 603.8` |
| baseline | `mmlu_5612` | `mcq` | false | `B` | `A. It will remain the same.` |
| baseline | `mmlu_5613` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5614` | `mcq` | false | `B` | `A. 42.2 g` |
| baseline | `mmlu_5615` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5616` | `mcq` | true | `D` | `D. There is insufficient information to answer this question.` |
| baseline | `mmlu_5617` | `mcq` | true | `D` | `D. We should be 90% confident that the difference in life expectancies is between 6 and 12 years.` |
| baseline | `mmlu_5618` | `mcq` | true | `B` | `B. 0.4096` |
| baseline | `mmlu_5619` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5620` | `mcq` | false | `C` | `B. 0.0112` |
| baseline | `mmlu_5621` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5622` | `mcq` | true | `C` | `C. Too high, because of undercoverage bias.` |
| baseline | `mmlu_5623` | `mcq` | false | `A` | `B. Standard deviation` |
| baseline | `mmlu_5624` | `mcq` | false | `C` | `A. Use the 88 who did respond, using 88 as the sample size in the analysis.` |
| baseline | `mmlu_5625` | `mcq` | false | `D` | `A. 0.44, 0.5, 0.2` |
| baseline | `mmlu_5626` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5627` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5628` | `mcq` | false | `D` | `A. -0.65` |
| baseline | `mmlu_5629` | `mcq` | false | `D` | `B. 17.8%` |
| baseline | `mmlu_5630` | `mcq` | true | `B` | `B. 0.1446` |
| baseline | `mmlu_5631` | `mcq` | true | `A` | `A. P(A and B) = P(A) · P(B)` |
| baseline | `mmlu_5632` | `mcq` | false | `A` | `B. An experiment, thus making cause and effect a reasonable conclusion` |
| baseline | `mmlu_5633` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5634` | `mcq` | false | `D` | `B. $91` |
| baseline | `mmlu_5635` | `mcq` | true | `D` | `D. 9% of the variability in job satisfaction can be explained by the linear model with self-efficacy as a predictor.` |
| baseline | `mmlu_5636` | `mcq` | true | `D` | `D. There is insufficient information to answer this question.` |
| baseline | `mmlu_5637` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5638` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5639` | `mcq` | false | `A` | `B. I and III only` |
| baseline | `mmlu_5640` | `mcq` | false | `D` | `B. 64` |
| baseline | `mmlu_5641` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_5642` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_5643` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5644` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5645` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5646` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5647` | `mcq` | true | `D` | `D. Influential point` |
| baseline | `mmlu_5648` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5649` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5650` | `mcq` | true | `D` | `D. Reconstruction` |
| baseline | `mmlu_5651` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5652` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5653` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5654` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5655` | `mcq` | true | `A` | `A. The Social Gospel` |
| baseline | `mmlu_5656` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5657` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5658` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5659` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5660` | `mcq` | false | `A` | `C. all Christians only` |
| baseline | `mmlu_5661` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5662` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5663` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5664` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5665` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5666` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5667` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5668` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5669` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5670` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5671` | `mcq` | true | `B` | `B. Containment` |
| baseline | `mmlu_5672` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5673` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5674` | `mcq` | true | `D` | `D. Improve conditions in urban neighborhoods` |
| baseline | `mmlu_5675` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5676` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5678` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5679` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5680` | `mcq` | true | `A` | `A. The Nineteenth Amendment.` |
| baseline | `mmlu_5681` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5682` | `mcq` | true | `C` | `C. Greater rights for unions` |
| baseline | `mmlu_5683` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5684` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5685` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5686` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5687` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5688` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5689` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5690` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5691` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5692` | `mcq` | true | `C` | `C. William M. Tweed` |
| baseline | `mmlu_5693` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5694` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5695` | `mcq` | true | `C` | `C. Progressive Liberals` |
| baseline | `mmlu_5696` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5697` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5698` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5699` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5700` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5701` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5702` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5703` | `mcq` | true | `C` | `C. still an underdeveloped cultural backwater` |
| baseline | `mmlu_5704` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5705` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5706` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5707` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5708` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5709` | `mcq` | true | `C` | `C. Plessy v. Ferguson` |
| baseline | `mmlu_5710` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5711` | `mcq` | true | `A` | `A. The bombing of Pearl Harbor` |
| baseline | `mmlu_5712` | `mcq` | true | `B` | `B. Government efforts to prevent the publication of the Pentagon Papers in 1971` |
| baseline | `mmlu_5713` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5714` | `mcq` | true | `C` | `C. The USA Patriot Act of 2001` |
| baseline | `mmlu_5715` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5716` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5717` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5718` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5719` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5720` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5721` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5722` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5723` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5724` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5725` | `mcq` | true | `D` | `D. New Dealers of the 1930s` |
| baseline | `mmlu_5726` | `mcq` | true | `D` | `D. Ireland` |
| baseline | `mmlu_5727` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5728` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5729` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5730` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5731` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5732` | `mcq` | true | `C` | `C. U.S. involvement in Vietnam and the civil rights movement` |
| baseline | `mmlu_5733` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5734` | `mcq` | true | `B` | `B. Expanding territories under Spanish control` |
| baseline | `mmlu_5735` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5736` | `mcq` | true | `A` | `A. fishing.` |
| baseline | `mmlu_5737` | `mcq` | true | `C` | `C. they were religious Separatists looking for a place to freely practice their faith.` |
| baseline | `mmlu_5738` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5739` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5740` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5741` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5742` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5743` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5744` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5745` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5746` | `mcq` | false | `A` | `C. The Cold War` |
| baseline | `mmlu_5747` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5748` | `mcq` | true | `C` | `C. Manifest Destiny` |
| baseline | `mmlu_5749` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5750` | `mcq` | true | `C` | `C. Insurgence vs. retreat` |
| baseline | `mmlu_5751` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5752` | `mcq` | true | `D` | `D. Declaration of Independence.` |
| baseline | `mmlu_5753` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5754` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5755` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5756` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5757` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5758` | `mcq` | true | `C` | `C. Self-government` |
| baseline | `mmlu_5759` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5760` | `mcq` | true | `C` | `C. middle-class college students.` |
| baseline | `mmlu_5761` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5762` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5763` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5764` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5765` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5766` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5767` | `mcq` | true | `A` | `A. James K. Polk` |
| baseline | `mmlu_5768` | `mcq` | true | `D` | `D. the balanced budget mandate` |
| baseline | `mmlu_5769` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5770` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5771` | `mcq` | true | `C` | `C. Powerful nations have a moral duty to govern less developed nations.` |
| baseline | `mmlu_5772` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5773` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5774` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5775` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5776` | `mcq` | false | `B` | `A. violated the Constitutional injunction against bills of attainder.` |
| baseline | `mmlu_5777` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5778` | `mcq` | true | `C` | `C. Increased economic and political opportunities for women` |
| baseline | `mmlu_5779` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5780` | `mcq` | true | `B` | `B. Executive Order 9066 interning Japanese Americans` |
| baseline | `mmlu_5781` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5782` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5783` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5784` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5785` | `mcq` | true | `C` | `C. Spanish-American War` |
| baseline | `mmlu_5786` | `mcq` | true | `C` | `C. Republican motherhood` |
| baseline | `mmlu_5787` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5788` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5789` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5790` | `mcq` | false | `D` | `C. an evolving relationship between the federal government and issues of health and poverty.` |
| baseline | `mmlu_5791` | `mcq` | false | `A` | `B. a flourishing economy and a baby boom had led people to desire greater incomes.` |
| baseline | `mmlu_5792` | `mcq` | true | `D` | `D. The Pure Food and Drug Act` |
| baseline | `mmlu_5793` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5794` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5795` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5796` | `mcq` | true | `B` | `B. immigration quotas` |
| baseline | `mmlu_5797` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5798` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5799` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5800` | `mcq` | true | `B` | `B. The Second Great Awakening.` |
| baseline | `mmlu_5801` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5802` | `mcq` | true | `C` | `C. Theodore Roosevelt` |
| baseline | `mmlu_5803` | `mcq` | false | `A` | `D. Eighteenth century scientific racism` |
| baseline | `mmlu_5804` | `mcq` | false | `A` | `C. Plessy v. Ferguson (1896)` |
| baseline | `mmlu_5805` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5806` | `mcq` | false | `A` | `B. Supportive of the policies of Thomas Jefferson` |
| baseline | `mmlu_5807` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5808` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5809` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5810` | `mcq` | true | `A` | `A. The rise of the United States to the status of a great power` |
| baseline | `mmlu_5811` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5812` | `mcq` | true | `D` | `D. farmers, who hoped that a more generous money supply would ease their debt burdens` |
| baseline | `mmlu_5813` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5814` | `mcq` | true | `C` | `C. The Spanish–American War` |
| baseline | `mmlu_5815` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5816` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5817` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5818` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5819` | `mcq` | false | `B` | `A. Puritanism` |
| baseline | `mmlu_5820` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5821` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5822` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5823` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5824` | `mcq` | true | `C` | `C. Taking advantage of divisions among the Indians` |
| baseline | `mmlu_5825` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5826` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5827` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5828` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5829` | `mcq` | true | `B` | `B. Equal Rights Amendment.` |
| baseline | `mmlu_5830` | `mcq` | true | `A` | `A. The New Deal` |
| baseline | `mmlu_5831` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5832` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_5833` | `mcq` | true | `A` | `A. Support for Manifest Destiny` |
| baseline | `mmlu_5834` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5835` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5836` | `mcq` | true | `C` | `C. Quakers` |
| baseline | `mmlu_5837` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5838` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5839` | `mcq` | false | `D` | `B. Respecting Indian territory and sovereignty` |
| baseline | `mmlu_5840` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5841` | `mcq` | true | `A` | `A. Many Southern and Eastern Europeans turned to America for financial gain and political freedom.` |
| baseline | `mmlu_5842` | `mcq` | true | `D` | `D. Plessy v. Ferguson (1896).` |
| baseline | `mmlu_5843` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5844` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5845` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5846` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5847` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5848` | `mcq` | true | `D` | `D. the end of the Cold War.` |
| baseline | `mmlu_5849` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5850` | `mcq` | false | `B` | `D. British impressments of American sailors and interference with American trade` |
| baseline | `mmlu_5851` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5852` | `mcq` | true | `A` | `A. The formation of the non-aligned movement` |
| baseline | `mmlu_5853` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5854` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5855` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5856` | `mcq` | true | `D` | `D. Korea remains divided into two nations near the 38th parallel.` |
| baseline | `mmlu_5857` | `mcq` | true | `C` | `C. Cynical, enthusiastic` |
| baseline | `mmlu_5858` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5859` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5860` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5861` | `mcq` | true | `B` | `B. can be viewed as a reaction to the systemic brute force with which the British governed India.` |
| baseline | `mmlu_5862` | `mcq` | true | `B` | `B. He doesn't earn enough on his own.` |
| baseline | `mmlu_5863` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5864` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5865` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5866` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5867` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5868` | `mcq` | true | `A` | `A. Development of socialized programs throughout much of Europe` |
| baseline | `mmlu_5869` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5870` | `mcq` | true | `B` | `B. The ability of the Tang emperor to project military power on the frontier in order to impose his will.` |
| baseline | `mmlu_5871` | `mcq` | true | `A` | `A. Emphasis on trade networks` |
| baseline | `mmlu_5872` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5873` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5874` | `mcq` | true | `B` | `B. Nonviolent resistance` |
| baseline | `mmlu_5875` | `mcq` | true | `C` | `C. The encomienda system` |
| baseline | `mmlu_5876` | `mcq` | false | `B` | `D. The presence of highly developed port cities` |
| baseline | `mmlu_5877` | `mcq` | false | `A` | `B. The use of religion to justify armed violence` |
| baseline | `mmlu_5878` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5879` | `mcq` | true | `D` | `D. The defeat of Indian rebels and the imposition of direct rule by the British government` |
| baseline | `mmlu_5880` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5881` | `mcq` | true | `D` | `D. apartheid.` |
| baseline | `mmlu_5882` | `mcq` | true | `C` | `C. the Enlightenment` |
| baseline | `mmlu_5883` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5884` | `mcq` | true | `B` | `B. The invasion of Anatolia by the Seljuk Turks` |
| baseline | `mmlu_5885` | `mcq` | false | `B` | `A. Rules of royal succession` |
| baseline | `mmlu_5886` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5887` | `mcq` | false | `B` | `D. State-sponsored campaigns of genocide` |
| baseline | `mmlu_5888` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5889` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5890` | `mcq` | false | `D` | `A. Highlight the extent of the author's property losses` |
| baseline | `mmlu_5891` | `mcq` | true | `D` | `D. Overhunting and depletion of furbearing animals` |
| baseline | `mmlu_5892` | `mcq` | true | `C` | `C. Women's power increasingly fell within the private sphere.` |
| baseline | `mmlu_5893` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5894` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5895` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5896` | `mcq` | true | `D` | `D. Socialism` |
| baseline | `mmlu_5897` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5898` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5899` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5900` | `mcq` | true | `C` | `C. They logically decided to develop weapons better suited to their immediate military needs.` |
| baseline | `mmlu_5901` | `mcq` | false | `C` | `D. The country turned inward and closed its ports to all foreigners.` |
| baseline | `mmlu_5902` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5903` | `mcq` | true | `D` | `D. Hardening of anti-immigrant sentiment` |
| baseline | `mmlu_5904` | `mcq` | true | `D` | `D. Persia was brought into the Arabian orbit over the course of the period.` |
| baseline | `mmlu_5905` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5906` | `mcq` | true | `D` | `D. The Crusades` |
| baseline | `mmlu_5907` | `mcq` | false | `B` | `D. John Wycliffe` |
| baseline | `mmlu_5908` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5909` | `mcq` | true | `C` | `C. Pan-Africanism` |
| baseline | `mmlu_5910` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5911` | `mcq` | true | `D` | `D. Unforeseen consequences of British imperialism` |
| baseline | `mmlu_5912` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5913` | `mcq` | false | `A` | `C. He had lost the blessing of the gods.` |
| baseline | `mmlu_5914` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5915` | `mcq` | true | `C` | `C. A state or secular authority` |
| baseline | `mmlu_5916` | `mcq` | false | `A` | `C. The urban middle class` |
| baseline | `mmlu_5917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5918` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5919` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5920` | `mcq` | false | `A` | `D. The rise of a warrior elite whose deeds were worthy of praise and recording` |
| baseline | `mmlu_5921` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5922` | `mcq` | true | `D` | `D. The New World` |
| baseline | `mmlu_5923` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5924` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5925` | `mcq` | true | `A` | `A. Rulers derived legitimacy for their rule by their sponsorship of religion and chief priests.` |
| baseline | `mmlu_5926` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5927` | `mcq` | true | `C` | `C. European participation in East Asian trade patterns` |
| baseline | `mmlu_5928` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5929` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5930` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5931` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5932` | `mcq` | false | `C` | `D. The political nature of the church` |
| baseline | `mmlu_5933` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5934` | `mcq` | true | `A` | `A. Railroad construction` |
| baseline | `mmlu_5935` | `mcq` | false | `D` | `C. The king's lack of interest in the welfare of Native American subjects` |
| baseline | `mmlu_5936` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5937` | `mcq` | true | `A` | `A. Emerging systems of coerced labor` |
| baseline | `mmlu_5938` | `mcq` | true | `A` | `A. Rigid societal gender roles` |
| baseline | `mmlu_5939` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5940` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5941` | `mcq` | true | `B` | `B. Centralized and state-directed campaigns of modernization` |
| baseline | `mmlu_5942` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5943` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5944` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5945` | `mcq` | false | `A` | `C. The Industrial Revolution` |
| baseline | `mmlu_5946` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5947` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5948` | `mcq` | true | `C` | `C. The establishment of the Tokugawa Shogunate` |
| baseline | `mmlu_5949` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5950` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5951` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5952` | `mcq` | true | `C` | `C. A proposal to increase the standing of Africa in the modern world` |
| baseline | `mmlu_5953` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5954` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5955` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5956` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5957` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5958` | `mcq` | true | `A` | `A. Laissez-faire` |
| baseline | `mmlu_5959` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5960` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5961` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5962` | `mcq` | true | `B` | `B. Unfair systems of taxation` |
| baseline | `mmlu_5963` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5964` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5965` | `mcq` | true | `C` | `C. The end justifies the means` |
| baseline | `mmlu_5966` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5967` | `mcq` | true | `A` | `A. Existentialism` |
| baseline | `mmlu_5968` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5969` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5970` | `mcq` | true | `A` | `A. He is found everywhere and contained in everything.` |
| baseline | `mmlu_5971` | `mcq` | true | `C` | `C. The importance of sacrifice to the gods` |
| baseline | `mmlu_5972` | `mcq` | true | `B` | `B. It was a continuation of a preexisting cultural pattern.` |
| baseline | `mmlu_5973` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5974` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5975` | `mcq` | true | `C` | `C. The use of religion to ponder conceptions of the afterlife` |
| baseline | `mmlu_5976` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5977` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5978` | `mcq` | false | `B` | `D. Colonial powers preparing their colonies for independence` |
| baseline | `mmlu_5979` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5980` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5981` | `mcq` | true | `B` | `B. The fight for independence in South America` |
| baseline | `mmlu_5982` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5983` | `mcq` | true | `A` | `A. Policies of religious toleration` |
| baseline | `mmlu_5984` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5985` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5986` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5987` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5988` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5989` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5990` | `mcq` | true | `C` | `C. contact with Muslim trade caravans.` |
| baseline | `mmlu_5991` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5992` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5993` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5994` | `mcq` | false | `B` | `A. The world is too afraid of South Africa to oppose apartheid.` |
| baseline | `mmlu_5995` | `mcq` | true | `C` | `C. World War II` |
| baseline | `mmlu_5996` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5997` | `mcq` | false | `C` | `D. Reform` |
| baseline | `mmlu_5998` | `mcq` | false | `C` | `A. All adult men born within the geographic boundaries of the state` |
| baseline | `mmlu_5999` | `mcq` | true | `C` | `C. Decolonization` |
