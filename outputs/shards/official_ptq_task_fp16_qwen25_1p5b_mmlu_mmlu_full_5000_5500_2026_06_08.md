# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 374 / 500 | 0.7480 | 4.8511 | 0.424304 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_5000` | `mcq` | true | `C` | `C. shape constancy` |
| baseline | `mmlu_5001` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5002` | `mcq` | false | `C` | `A. engage in risky behavior.` |
| baseline | `mmlu_5003` | `mcq` | true | `A` | `A. Tip-of-the-Tongue Phenomenon` |
| baseline | `mmlu_5004` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5005` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5006` | `mcq` | true | `D` | `D. language acquisition device` |
| baseline | `mmlu_5007` | `mcq` | true | `C` | `C. Ecological` |
| baseline | `mmlu_5008` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5009` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5010` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5011` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5012` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5013` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5014` | `mcq` | true | `B` | `B. standardized` |
| baseline | `mmlu_5015` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5016` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5017` | `mcq` | true | `C` | `C. Pairing an unconditioned stimulus with a conditioned stimulus` |
| baseline | `mmlu_5018` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5019` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_5020` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5021` | `mcq` | true | `B` | `B. hindbrain and midbrain.` |
| baseline | `mmlu_5022` | `mcq` | true | `D` | `D. linear perspective` |
| baseline | `mmlu_5023` | `mcq` | true | `D` | `D. difference threshold` |
| baseline | `mmlu_5024` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5025` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5026` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5027` | `mcq` | true | `A` | `A. endorphins` |
| baseline | `mmlu_5028` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5029` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5030` | `mcq` | false | `C` | `B. MRI` |
| baseline | `mmlu_5031` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5032` | `mcq` | true | `D` | `D. median` |
| baseline | `mmlu_5033` | `mcq` | true | `D` | `D. morphemes` |
| baseline | `mmlu_5034` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5035` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5036` | `mcq` | false | `D` | `C. variable ratio` |
| baseline | `mmlu_5037` | `mcq` | true | `A` | `A. expectation` |
| baseline | `mmlu_5038` | `mcq` | true | `B` | `B. sublimation` |
| baseline | `mmlu_5039` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5040` | `mcq` | true | `D` | `D. linear perspective` |
| baseline | `mmlu_5041` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5042` | `mcq` | false | `C` | `A.	object permanence` |
| baseline | `mmlu_5043` | `mcq` | true | `D` | `D. Maintenance rehearsal` |
| baseline | `mmlu_5044` | `mcq` | true | `D` | `D. hypothalamus` |
| baseline | `mmlu_5045` | `mcq` | false | `A` | `D. lists 3 and 4 only` |
| baseline | `mmlu_5046` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5047` | `mcq` | true | `C` | `C. balance` |
| baseline | `mmlu_5048` | `mcq` | true | `A` | `A. superordinate goals` |
| baseline | `mmlu_5049` | `mcq` | true | `B` | `B. negative punishment` |
| baseline | `mmlu_5050` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5051` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5052` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_5053` | `mcq` | false | `B` | `C. James-Lange theory` |
| baseline | `mmlu_5054` | `mcq` | true | `B` | `B. Preoperational` |
| baseline | `mmlu_5055` | `mcq` | true | `C` | `C. Projection` |
| baseline | `mmlu_5056` | `mcq` | false | `D` | `A. Bias` |
| baseline | `mmlu_5057` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5058` | `mcq` | true | `A` | `A. Schizophrenia` |
| baseline | `mmlu_5059` | `mcq` | true | `C` | `C. hypothalamus` |
| baseline | `mmlu_5060` | `mcq` | true | `C` | `C. shaping.` |
| baseline | `mmlu_5061` | `mcq` | true | `A` | `A. amplitude of the wave` |
| baseline | `mmlu_5062` | `mcq` | true | `C` | `C. pituitary gland` |
| baseline | `mmlu_5063` | `mcq` | true | `D` | `D. psychoanalytic` |
| baseline | `mmlu_5064` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5065` | `mcq` | true | `D` | `D. major depressive disorder.` |
| baseline | `mmlu_5066` | `mcq` | true | `A` | `A. talking to a patient` |
| baseline | `mmlu_5067` | `mcq` | true | `B` | `B. acquisition` |
| baseline | `mmlu_5068` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5069` | `mcq` | true | `D` | `D. proximity` |
| baseline | `mmlu_5070` | `mcq` | true | `D` | `D. in-group bias` |
| baseline | `mmlu_5071` | `mcq` | true | `A` | `A. Selye's general adaptation syndrome` |
| baseline | `mmlu_5072` | `mcq` | true | `A` | `A. elevate mood and reduce pain` |
| baseline | `mmlu_5073` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5074` | `mcq` | false | `B` | `D. Alliance formation` |
| baseline | `mmlu_5075` | `mcq` | true | `B` | `B. satisfying needs from the next step in the hierarchy` |
| baseline | `mmlu_5076` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5077` | `mcq` | false | `C` | `D. sex` |
| baseline | `mmlu_5078` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5079` | `mcq` | false | `D` | `B. generalization.` |
| baseline | `mmlu_5080` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5081` | `mcq` | true | `B` | `B. Cognitive` |
| baseline | `mmlu_5082` | `mcq` | true | `C` | `C. uncon` |
| baseline | `mmlu_5083` | `mcq` | true | `D` | `D. I, II, and III` |
| baseline | `mmlu_5084` | `mcq` | true | `A` | `A. traits` |
| baseline | `mmlu_5085` | `mcq` | true | `C` | `C. Broca's area` |
| baseline | `mmlu_5086` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5087` | `mcq` | true | `C` | `C. REM sleep` |
| baseline | `mmlu_5088` | `mcq` | true | `A` | `A. humanistic` |
| baseline | `mmlu_5089` | `mcq` | true | `D` | `D. experiencing a physical problem without a physical cause` |
| baseline | `mmlu_5090` | `mcq` | true | `C` | `C. unconditional positive regard` |
| baseline | `mmlu_5091` | `mcq` | true | `B` | `B. Increase the speed with which messages can be transmitted` |
| baseline | `mmlu_5092` | `mcq` | true | `C` | `C. Inter-rater reliability` |
| baseline | `mmlu_5093` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5094` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5095` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5096` | `mcq` | true | `A` | `A. the representativeness heuristic and the availability heuristic` |
| baseline | `mmlu_5097` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5098` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5099` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5100` | `mcq` | true | `D` | `D. denial` |
| baseline | `mmlu_5101` | `mcq` | false | `A` | `D. association areas` |
| baseline | `mmlu_5102` | `mcq` | true | `C` | `C. reinforced` |
| baseline | `mmlu_5103` | `mcq` | false | `A` | `C. sense of time urgency` |
| baseline | `mmlu_5104` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5105` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5106` | `mcq` | true | `B` | `B. white` |
| baseline | `mmlu_5107` | `mcq` | true | `D` | `D. Dopamine` |
| baseline | `mmlu_5108` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5109` | `mcq` | true | `D` | `D. generalization` |
| baseline | `mmlu_5110` | `mcq` | false | `C` | `A. Bob ate a snack.` |
| baseline | `mmlu_5111` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5112` | `mcq` | false | `D` | `C. touch.` |
| baseline | `mmlu_5113` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5114` | `mcq` | true | `C` | `C. thalamus` |
| baseline | `mmlu_5115` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5116` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5117` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5118` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5119` | `mcq` | true | `D` | `D. separation anxiety` |
| baseline | `mmlu_5120` | `mcq` | true | `B` | `B. confirmation bias` |
| baseline | `mmlu_5121` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5122` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5123` | `mcq` | true | `C` | `C. Attribution theory` |
| baseline | `mmlu_5124` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5125` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5126` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5127` | `mcq` | false | `C` | `A. black` |
| baseline | `mmlu_5128` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5129` | `mcq` | false | `B` | `D. 1 in 10,000.` |
| baseline | `mmlu_5130` | `mcq` | false | `A` | `B. simultaneous` |
| baseline | `mmlu_5131` | `mcq` | true | `A` | `A. GAD.` |
| baseline | `mmlu_5132` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5133` | `mcq` | false | `B` | `A. recognition` |
| baseline | `mmlu_5134` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5135` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5136` | `mcq` | true | `C` | `C. Shaping` |
| baseline | `mmlu_5137` | `mcq` | true | `C` | `C. closure` |
| baseline | `mmlu_5138` | `mcq` | true | `B` | `B. inferential statistics` |
| baseline | `mmlu_5139` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5140` | `mcq` | true | `D` | `D. more neurons firing more frequently` |
| baseline | `mmlu_5141` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5142` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5143` | `mcq` | true | `D` | `D. risk of psychological harm` |
| baseline | `mmlu_5144` | `mcq` | true | `A` | `A. -1` |
| baseline | `mmlu_5145` | `mcq` | true | `B` | `B. cerebral cortex` |
| baseline | `mmlu_5146` | `mcq` | false | `D` | `B. Variable ratio schedules of reinforcements produce results more quickly.` |
| baseline | `mmlu_5147` | `mcq` | true | `A` | `A. serotonin` |
| baseline | `mmlu_5148` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5149` | `mcq` | true | `D` | `D. collective unconscious` |
| baseline | `mmlu_5150` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5151` | `mcq` | true | `D` | `D. chemotherapy` |
| baseline | `mmlu_5152` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5153` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5154` | `mcq` | true | `C` | `C. hypothalamus` |
| baseline | `mmlu_5155` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5156` | `mcq` | false | `B` | `A. alcohol abuse` |
| baseline | `mmlu_5157` | `mcq` | false | `C` | `A. Variable-ratio` |
| baseline | `mmlu_5158` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_5159` | `mcq` | true | `D` | `D. Meta-analysis` |
| baseline | `mmlu_5160` | `mcq` | true | `D` | `D. modeling` |
| baseline | `mmlu_5161` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5162` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5163` | `mcq` | true | `C` | `C. compliance strategy` |
| baseline | `mmlu_5164` | `mcq` | true | `D` | `D. rational emotive` |
| baseline | `mmlu_5165` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5166` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5167` | `mcq` | false | `D` | `B. yellow` |
| baseline | `mmlu_5168` | `mcq` | true | `D` | `D. superego` |
| baseline | `mmlu_5169` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5170` | `mcq` | true | `D` | `D. incentive` |
| baseline | `mmlu_5171` | `mcq` | true | `B` | `B. Visual imagery` |
| baseline | `mmlu_5172` | `mcq` | false | `B` | `A. Caring for one's children` |
| baseline | `mmlu_5173` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5174` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5175` | `mcq` | false | `C` | `B. behavior therapy` |
| baseline | `mmlu_5176` | `mcq` | true | `A` | `A. above average` |
| baseline | `mmlu_5177` | `mcq` | true | `B` | `B. selective attention` |
| baseline | `mmlu_5178` | `mcq` | true | `D` | `D.traits, the environment, and behavior` |
| baseline | `mmlu_5179` | `mcq` | true | `D` | `D. prefrontal cortex` |
| baseline | `mmlu_5180` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5181` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5182` | `mcq` | true | `A` | `A. The parasympathetic nervous system resumes control and reverses the sympathetic responses.` |
| baseline | `mmlu_5183` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_5184` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5185` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5186` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5187` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5188` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5189` | `mcq` | true | `D` | `D. learning` |
| baseline | `mmlu_5190` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5191` | `mcq` | true | `D` | `D. Hallucinations` |
| baseline | `mmlu_5192` | `mcq` | true | `A` | `A. humanistic` |
| baseline | `mmlu_5193` | `mcq` | true | `C` | `C. Developmental psychologists` |
| baseline | `mmlu_5194` | `mcq` | true | `B` | `B. depressive` |
| baseline | `mmlu_5195` | `mcq` | true | `D` | `D. 60` |
| baseline | `mmlu_5196` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5197` | `mcq` | true | `A` | `A. cognitive dissonance` |
| baseline | `mmlu_5198` | `mcq` | true | `D` | `D. major depressive disorder` |
| baseline | `mmlu_5199` | `mcq` | true | `B` | `B. groupthink` |
| baseline | `mmlu_5200` | `mcq` | true | `D` | `D. attachment` |
| baseline | `mmlu_5201` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5202` | `mcq` | true | `D` | `D. chunking` |
| baseline | `mmlu_5203` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5204` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5205` | `mcq` | true | `C` | `C. leading questions` |
| baseline | `mmlu_5206` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5207` | `mcq` | true | `B` | `B. reflex` |
| baseline | `mmlu_5208` | `mcq` | true | `C` | `C. Catharsis hypothesis` |
| baseline | `mmlu_5209` | `mcq` | false | `A` | `B. Rorschach inkblot test` |
| baseline | `mmlu_5210` | `mcq` | true | `B` | `B. recalling the name of your junior high school shop teacher` |
| baseline | `mmlu_5211` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5212` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5213` | `mcq` | true | `D` | `D. sensory memory` |
| baseline | `mmlu_5214` | `mcq` | true | `D` | `D. trait` |
| baseline | `mmlu_5215` | `mcq` | true | `B` | `B. dopamine` |
| baseline | `mmlu_5216` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5217` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5218` | `mcq` | true | `A` | `A. the color of the paper` |
| baseline | `mmlu_5219` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5220` | `mcq` | true | `C` | `C. set point theory` |
| baseline | `mmlu_5221` | `mcq` | true | `D` | `D. approach-approach` |
| baseline | `mmlu_5222` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5223` | `mcq` | true | `A` | `A. Duty to warn and protect` |
| baseline | `mmlu_5224` | `mcq` | false | `D` | `A. opponent-process theory` |
| baseline | `mmlu_5225` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5226` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5227` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5228` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5229` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5230` | `mcq` | true | `D` | `D. cones` |
| baseline | `mmlu_5231` | `mcq` | false | `D` | `A. the synapse` |
| baseline | `mmlu_5232` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5233` | `mcq` | false | `A` | `D. Love` |
| baseline | `mmlu_5234` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5235` | `mcq` | true | `D` | `D. Authoritative` |
| baseline | `mmlu_5236` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5237` | `mcq` | true | `B` | `B. double blind study` |
| baseline | `mmlu_5238` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5239` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5240` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5241` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5242` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5243` | `mcq` | true | `D` | `D. Difference threshold` |
| baseline | `mmlu_5244` | `mcq` | true | `D` | `D. Systems approach` |
| baseline | `mmlu_5245` | `mcq` | true | `B` | `B. Experiments isolate the effects of independent variables on dependent variables.` |
| baseline | `mmlu_5246` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5247` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5248` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5249` | `mcq` | false | `B` | `A. Median` |
| baseline | `mmlu_5250` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5251` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5252` | `mcq` | true | `C` | `C. Homeostasis` |
| baseline | `mmlu_5253` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5254` | `mcq` | false | `B` | `A. primary` |
| baseline | `mmlu_5255` | `mcq` | true | `B` | `B. "It's the law."` |
| baseline | `mmlu_5256` | `mcq` | true | `D` | `D. agoraphobia` |
| baseline | `mmlu_5257` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5258` | `mcq` | true | `A` | `A. psychoanalysis` |
| baseline | `mmlu_5259` | `mcq` | true | `B` | `B. crystallized intelligence` |
| baseline | `mmlu_5260` | `mcq` | true | `C` | `C. cognitive dissonance` |
| baseline | `mmlu_5261` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5262` | `mcq` | true | `A` | `A. self-efficacy` |
| baseline | `mmlu_5263` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5264` | `mcq` | true | `D` | `D./aptitude	test.` |
| baseline | `mmlu_5265` | `mcq` | true | `B` | `B. four legs and a seat.` |
| baseline | `mmlu_5266` | `mcq` | true | `D` | `D. left temporal` |
| baseline | `mmlu_5267` | `mcq` | true | `B` | `B. semantic memory` |
| baseline | `mmlu_5268` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5269` | `mcq` | true | `D` | `D. License` |
| baseline | `mmlu_5270` | `mcq` | true | `A` | `A. naturalistic observation` |
| baseline | `mmlu_5271` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5272` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5273` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5274` | `mcq` | false | `C` | `A. United States of America` |
| baseline | `mmlu_5275` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5276` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5277` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5278` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5279` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5281` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5282` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5283` | `mcq` | true | `B` | `B. semantic memory` |
| baseline | `mmlu_5284` | `mcq` | true | `B` | `B. facial expressions` |
| baseline | `mmlu_5285` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5286` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5287` | `mcq` | true | `B` | `B. trait` |
| baseline | `mmlu_5288` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5289` | `mcq` | true | `A` | `A. cell body` |
| baseline | `mmlu_5290` | `mcq` | true | `B` | `B. Alzheimer's disease` |
| baseline | `mmlu_5291` | `mcq` | false | `D` | `B. MRI` |
| baseline | `mmlu_5292` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5293` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5294` | `mcq` | true | `B` | `B. a compulsion` |
| baseline | `mmlu_5295` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5296` | `mcq` | true | `D` | `D. thalamus` |
| baseline | `mmlu_5297` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5298` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5299` | `mcq` | true | `D` | `D. group polarization` |
| baseline | `mmlu_5300` | `mcq` | true | `D` | `D. intrinsic motivation` |
| baseline | `mmlu_5301` | `mcq` | true | `B` | `B. external validity` |
| baseline | `mmlu_5302` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5303` | `mcq` | true | `D` | `D. morpheme` |
| baseline | `mmlu_5304` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5305` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5306` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_5307` | `mcq` | true | `B` | `B. systematic desensitization` |
| baseline | `mmlu_5308` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_5309` | `mcq` | true | `D` | `D. Sensory adaptation` |
| baseline | `mmlu_5310` | `mcq` | true | `C` | `C. Hormones released in the womb` |
| baseline | `mmlu_5311` | `mcq` | false | `D` | `C. id` |
| baseline | `mmlu_5312` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5313` | `mcq` | true | `B` | `B. sympathetic nervous system` |
| baseline | `mmlu_5314` | `mcq` | true | `A` | `A. acetylcholine` |
| baseline | `mmlu_5315` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5316` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5317` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5318` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5319` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5320` | `mcq` | true | `B` | `B. modeling.` |
| baseline | `mmlu_5321` | `mcq` | true | `C` | `C. median` |
| baseline | `mmlu_5322` | `mcq` | true | `B` | `B. inductive reasoning` |
| baseline | `mmlu_5323` | `mcq` | true | `A` | `A. the Big Five` |
| baseline | `mmlu_5324` | `mcq` | true | `D` | `D. environments` |
| baseline | `mmlu_5325` | `mcq` | true | `A` | `A. constructing reality out of their own experiences` |
| baseline | `mmlu_5326` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5327` | `mcq` | true | `C` | `C. identify the origin of a sound.` |
| baseline | `mmlu_5328` | `mcq` | true | `D` | `D. Diffusion of responsibility` |
| baseline | `mmlu_5329` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5330` | `mcq` | false | `A` | `D. left cerebral cortex` |
| baseline | `mmlu_5331` | `mcq` | false | `D` | `A. frequency` |
| baseline | `mmlu_5332` | `mcq` | true | `D` | `D. Gender` |
| baseline | `mmlu_5333` | `mcq` | false | `D` | `B. negative reinforcement` |
| baseline | `mmlu_5334` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_5335` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5336` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5337` | `mcq` | false | `B` | `A. case study` |
| baseline | `mmlu_5338` | `mcq` | true | `B` | `B. random sampling` |
| baseline | `mmlu_5339` | `mcq` | true | `A` | `A. delay between the CS and the UCS is too long` |
| baseline | `mmlu_5340` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5341` | `mcq` | true | `A` | `A. nomothetic` |
| baseline | `mmlu_5342` | `mcq` | true | `B` | `B. the mind-body problem` |
| baseline | `mmlu_5343` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5344` | `mcq` | true | `D` | `D. Providing acceleration for gifted students, especially within the areas of their interests and skills.` |
| baseline | `mmlu_5345` | `mcq` | true | `D` | `D. sight` |
| baseline | `mmlu_5346` | `mcq` | true | `C` | `C. place` |
| baseline | `mmlu_5347` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5348` | `mcq` | true | `A` | `A. relative deprivation` |
| baseline | `mmlu_5349` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5350` | `mcq` | false | `B` | `A. difference threshold` |
| baseline | `mmlu_5351` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5352` | `mcq` | true | `D` | `D. The retina` |
| baseline | `mmlu_5353` | `mcq` | true | `C` | `C. Broca's area` |
| baseline | `mmlu_5354` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5355` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5356` | `mcq` | true | `B` | `B. psychiatrist` |
| baseline | `mmlu_5357` | `mcq` | true | `D` | `D. reflex` |
| baseline | `mmlu_5358` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5359` | `mcq` | true | `A` | `A. receptor, afferent neuron, interneuron, efferent neuron, effector` |
| baseline | `mmlu_5360` | `mcq` | true | `A` | `A. Jim and Tim will have very similar IQs.` |
| baseline | `mmlu_5361` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5362` | `mcq` | true | `B` | `B. DSM-5` |
| baseline | `mmlu_5363` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5364` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5365` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5366` | `mcq` | true | `D` | `D. correlation` |
| baseline | `mmlu_5367` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5368` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5369` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5370` | `mcq` | true | `C` | `C. flashbulb memory` |
| baseline | `mmlu_5371` | `mcq` | false | `C` | `A. behavioral` |
| baseline | `mmlu_5372` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5373` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5374` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_5375` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5376` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5377` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5378` | `mcq` | true | `D` | `D. Anthropologists` |
| baseline | `mmlu_5379` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5380` | `mcq` | true | `C` | `C. Down syndrome` |
| baseline | `mmlu_5381` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5382` | `mcq` | true | `D` | `D. dissociative disorder` |
| baseline | `mmlu_5383` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5384` | `mcq` | false | `C` | `A. frequency` |
| baseline | `mmlu_5385` | `mcq` | false | `C` | `B. 3 months` |
| baseline | `mmlu_5386` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5387` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5388` | `mcq` | true | `B` | `B. optic chiasm.` |
| baseline | `mmlu_5389` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5390` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_5391` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_5392` | `mcq` | true | `B` | `B. inferential statistics` |
| baseline | `mmlu_5393` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5394` | `mcq` | true | `D` | `D. Sleep apnea` |
| baseline | `mmlu_5395` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5396` | `mcq` | false | `A` | `D. surface processing` |
| baseline | `mmlu_5397` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5398` | `mcq` | true | `A` | `A. Occipital` |
| baseline | `mmlu_5399` | `mcq` | true | `D` | `D. Causes of all mental disorders` |
| baseline | `mmlu_5400` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_5401` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_5402` | `mcq` | true | `D` | `D. Changes in behavior over time` |
| baseline | `mmlu_5403` | `mcq` | false | `B` | `D. I and II only` |
| baseline | `mmlu_5404` | `mcq` | true | `D` | `D. Implementing a class-wide behavior management plan, such as a response-cost raffle.` |
| baseline | `mmlu_5405` | `mcq` | true | `C` | `C. industrial/organizational` |
| baseline | `mmlu_5406` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5407` | `mcq` | false | `D` | `C. it is difficult to convince medical professionals that one has a disorder when one does not.` |
| baseline | `mmlu_5408` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5409` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5410` | `mcq` | true | `B` | `B. authoritative` |
| baseline | `mmlu_5411` | `mcq` | true | `C` | `C. phallic stage.` |
| baseline | `mmlu_5412` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_5413` | `mcq` | false | `C` | `A. going to lecture classes` |
| baseline | `mmlu_5414` | `mcq` | true | `D` | `D. deindividuation` |
| baseline | `mmlu_5415` | `mcq` | true | `C` | `C. Wundt set up a laboratory and focused on empirical evidence that could be replicated.` |
| baseline | `mmlu_5416` | `mcq` | false | `D` | `C. cold` |
| baseline | `mmlu_5417` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5418` | `mcq` | true | `C` | `C. influencing patients by controlling the consequences of their actions` |
| baseline | `mmlu_5419` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5420` | `mcq` | false | `D` | `B. behavior therapy` |
| baseline | `mmlu_5421` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5422` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5423` | `mcq` | true | `C` | `C. the local community college and distant community colleges` |
| baseline | `mmlu_5424` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_5425` | `mcq` | true | `B` | `B. The neural connections to the primary visual cortex are not fully connected.` |
| baseline | `mmlu_5426` | `mcq` | true | `D` | `D. medulla` |
| baseline | `mmlu_5427` | `mcq` | true | `A` | `A. The self-fulfilling prophecy` |
| baseline | `mmlu_5428` | `mcq` | true | `D` | `D. insight` |
| baseline | `mmlu_5429` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5430` | `mcq` | false | `A` | `B. the "wire" mother versus the "cloth" mother` |
| baseline | `mmlu_5431` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_5432` | `mcq` | true | `B` | `B. 2P(t > 1.54) with df = 6` |
| baseline | `mmlu_5433` | `mcq` | true | `C` | `C. 25.3 to 44.7 minutes` |
| baseline | `mmlu_5434` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5435` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5436` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5437` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5438` | `mcq` | true | `D` | `D. The probability of a Type I error would stay the same and the power would increase.` |
| baseline | `mmlu_5439` | `mcq` | true | `D` | `D. The woman, because her height is 1.33 standard deviations above the mean height of all women, whereas the man’s heigh` |
| baseline | `mmlu_5440` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5441` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5442` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5443` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_5444` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5445` | `mcq` | false | `C` | `D. decreases the interval size by 57%.` |
| baseline | `mmlu_5446` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5447` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_5448` | `mcq` | false | `B` | `D. III only` |
| baseline | `mmlu_5449` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5450` | `mcq` | false | `D` | `B. 0.0016` |
| baseline | `mmlu_5451` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_5452` | `mcq` | true | `D` | `D. –0.21` |
| baseline | `mmlu_5453` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5454` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_5455` | `mcq` | false | `B` | `A. -1` |
| baseline | `mmlu_5456` | `mcq` | true | `A` | `A. $23,000` |
| baseline | `mmlu_5457` | `mcq` | false | `D` | `B. $23,700` |
| baseline | `mmlu_5458` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_5459` | `mcq` | true | `A` | `A. Her procedure makes use of chance.` |
| baseline | `mmlu_5460` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5461` | `mcq` | false | `D` | `A. 1.345 < t< 1.761` |
| baseline | `mmlu_5462` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5463` | `mcq` | false | `D` | `B. 1.96` |
| baseline | `mmlu_5464` | `mcq` | true | `D` | `D. None of the above are appropriate.` |
| baseline | `mmlu_5465` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_5466` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_5467` | `mcq` | true | `D` | `D. III only` |
| baseline | `mmlu_5468` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_5469` | `mcq` | true | `A` | `A. We are 95 percent confident that the proportion of women interested in shopping on Sundays exceeds the proportion of ` |
| baseline | `mmlu_5470` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_5471` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_5472` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5473` | `mcq` | false | `D` | `B. 100` |
| baseline | `mmlu_5474` | `mcq` | true | `A` | `A. It is likely that the true proportion of high school students afraid to go to school is between 38% and 48%.` |
| baseline | `mmlu_5475` | `mcq` | false | `A` | `B. Sample survey` |
| baseline | `mmlu_5476` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_5477` | `mcq` | false | `B` | `A. Plan I` |
| baseline | `mmlu_5478` | `mcq` | true | `B` | `B. because a sample statistic is used to estimate a population parameter.` |
| baseline | `mmlu_5479` | `mcq` | false | `C` | `A. I and III only` |
| baseline | `mmlu_5480` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_5481` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5482` | `mcq` | true | `D` | `D. The population of SAT scores from each group is normally distributed.` |
| baseline | `mmlu_5483` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_5484` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5485` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5486` | `mcq` | true | `D` | `D. None of the above can affect the r value.` |
| baseline | `mmlu_5487` | `mcq` | false | `D` | `C. It multiples the interval size by 1.732.` |
| baseline | `mmlu_5488` | `mcq` | true | `A` | `A. 0.19` |
| baseline | `mmlu_5489` | `mcq` | false | `D` | `A. z = 0.04` |
| baseline | `mmlu_5490` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_5491` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_5492` | `mcq` | true | `C` | `C. 86.65; she qualifies.` |
| baseline | `mmlu_5493` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_5494` | `mcq` | true | `D` | `D. None of the above.` |
| baseline | `mmlu_5495` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_5496` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_5497` | `mcq` | true | `D` | `D. The population of the sales records at each location is normally distributed.` |
| baseline | `mmlu_5498` | `mcq` | true | `B` | `B. 0.40` |
| baseline | `mmlu_5499` | `mcq` | false | `B` | `A. μ = 3.677, σ = 3.561` |
