# Chat Task Benchmark

Model: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 283 / 500 | 0.5660 | 10.4325 | 0.152137 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_4500` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4501` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4502` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4503` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4504` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4505` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4506` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4507` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4508` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4509` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4510` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4511` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4512` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4513` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4514` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4515` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4516` | `mcq` | true | `B` | `B. Market failure` |
| baseline | `mmlu_4517` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4518` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4519` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4520` | `mcq` | true | `D` | `D. I and III only.` |
| baseline | `mmlu_4521` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4522` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4523` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4524` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4525` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4526` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4527` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4528` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4529` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4530` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4531` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4532` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4533` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4534` | `mcq` | true | `B` | `B. substitution effect.` |
| baseline | `mmlu_4535` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4536` | `mcq` | false | `A` | `C. increase price as demand is elastic.` |
| baseline | `mmlu_4537` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4538` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4539` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4540` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4541` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4542` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4543` | `mcq` | true | `D` | `D. The International Space Station` |
| baseline | `mmlu_4544` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4545` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4546` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4547` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4548` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4549` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4550` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4551` | `mcq` | true | `B` | `B. elastic.` |
| baseline | `mmlu_4552` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4553` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4554` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4555` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4556` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4557` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4558` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4559` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4560` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4561` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4562` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4563` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4564` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4565` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4566` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4567` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4568` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4569` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4570` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4571` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4572` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4573` | `mcq` | false | `D` | `A. decrease price because demand is elastic` |
| baseline | `mmlu_4574` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4575` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4576` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4577` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4578` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4579` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4580` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4581` | `mcq` | false | `D` | `A. I, III, and V only` |
| baseline | `mmlu_4582` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4583` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4584` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4585` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4586` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4587` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4588` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4589` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4590` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4591` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4592` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4593` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4594` | `mcq` | true | `B` | `B. Price rises, but the change in quantity is ambiguous.` |
| baseline | `mmlu_4595` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4596` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4597` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4598` | `mcq` | true | `D` | `D. opportunity cost.` |
| baseline | `mmlu_4599` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4600` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4601` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4602` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4603` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4604` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4605` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4606` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4607` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4608` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4609` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4610` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4611` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4612` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4613` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4614` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4615` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4616` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4617` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4618` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4619` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4620` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4621` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4622` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4623` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4624` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4625` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4626` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4627` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4628` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4629` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4630` | `mcq` | true | `B` | `B. Subsidize the firm or its customers.` |
| baseline | `mmlu_4631` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4632` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4633` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4634` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4635` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4636` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4637` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4638` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4639` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4640` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4641` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4642` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4643` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4644` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4645` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4646` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4647` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4648` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4649` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4650` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4651` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4652` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4653` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4654` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4655` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4656` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4657` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4658` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4659` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4660` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4661` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4662` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4663` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4664` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4665` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4666` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4667` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4668` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4669` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4670` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4671` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4672` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4673` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4674` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4675` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4676` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4677` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4678` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4679` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4680` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4681` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4682` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4683` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4684` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4685` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4686` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4687` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4688` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4689` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4690` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4691` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4692` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4693` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4694` | `mcq` | true | `C` | `C. the marginal cost curve intersects the demand curve` |
| baseline | `mmlu_4695` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4696` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4697` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4698` | `mcq` | true | `B` | `B. law of demand` |
| baseline | `mmlu_4699` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4700` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4701` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4702` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4703` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4704` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4705` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4706` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4707` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4708` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4709` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4710` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4711` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4712` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4713` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4714` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4715` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4716` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4717` | `mcq` | true | `B` | `B. Increases` |
| baseline | `mmlu_4718` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4719` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4720` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4721` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4722` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4723` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4724` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4725` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4726` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4727` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4728` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4729` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4730` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4731` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4732` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4733` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4734` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4735` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4736` | `mcq` | false | `B` | `C. 0.02 C` |
| baseline | `mmlu_4737` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4738` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4739` | `mcq` | false | `C` | `A. Less` |
| baseline | `mmlu_4740` | `mcq` | false | `D` | `A. I only` |
| baseline | `mmlu_4741` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4742` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4743` | `mcq` | true | `C` | `C. 0.05 J` |
| baseline | `mmlu_4744` | `mcq` | true | `A` | `A. v0^2/(2μg)` |
| baseline | `mmlu_4745` | `mcq` | false | `B` | `C. 2 s` |
| baseline | `mmlu_4746` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4747` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4748` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4749` | `mcq` | false | `B` | `D. 0.03 s` |
| baseline | `mmlu_4750` | `mcq` | false | `B` | `D. 0.5 N/kg` |
| baseline | `mmlu_4751` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4752` | `mcq` | false | `D` | `A. 1 nm` |
| baseline | `mmlu_4753` | `mcq` | false | `C` | `B. 100 cm` |
| baseline | `mmlu_4754` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4755` | `mcq` | false | `D` | `A. –165 V` |
| baseline | `mmlu_4756` | `mcq` | true | `B` | `B. 300 J out of the system` |
| baseline | `mmlu_4757` | `mcq` | false | `C` | `B. It will quadruple.` |
| baseline | `mmlu_4758` | `mcq` | true | `A` | `A. 5 × 10^15 Hz` |
| baseline | `mmlu_4759` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4760` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4761` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4762` | `mcq` | false | `C` | `B. 6 m/s` |
| baseline | `mmlu_4763` | `mcq` | false | `C` | `A. 1/3 V` |
| baseline | `mmlu_4764` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4765` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4766` | `mcq` | true | `A` | `A. 1.41v` |
| baseline | `mmlu_4767` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4768` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4769` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4770` | `mcq` | false | `C` | `D. I & III only` |
| baseline | `mmlu_4771` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4772` | `mcq` | false | `C` | `A. 5.0 × 10^6 m/s` |
| baseline | `mmlu_4773` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4774` | `mcq` | false | `A` | `B. 150 J of heat was removed from the gas.` |
| baseline | `mmlu_4775` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4776` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4777` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4778` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4779` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4780` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4781` | `mcq` | false | `B` | `C. 2.0/3` |
| baseline | `mmlu_4782` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4783` | `mcq` | false | `B` | `D. 1/2d` |
| baseline | `mmlu_4784` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4785` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4786` | `mcq` | true | `A` | `A. 2 cm ≤ D ≤ 10 cm` |
| baseline | `mmlu_4787` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4788` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4789` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4790` | `mcq` | false | `B` | `C. 2f` |
| baseline | `mmlu_4791` | `mcq` | false | `D` | `A. -3/5 cm` |
| baseline | `mmlu_4792` | `mcq` | false | `C` | `D. -99m` |
| baseline | `mmlu_4793` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4794` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4795` | `mcq` | false | `C` | `A. 1 N` |
| baseline | `mmlu_4796` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4797` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4798` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4799` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4800` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4801` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4802` | `mcq` | false | `C` | `A. 5.0 × 10^5 m/s` |
| baseline | `mmlu_4803` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4804` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4805` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4806` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4807` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4808` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4809` | `mcq` | false | `B` | `D. 4v` |
| baseline | `mmlu_4810` | `mcq` | false | `A` | `B. only when the enclosed charge is symmetrically distributed` |
| baseline | `mmlu_4811` | `mcq` | true | `B` | `B. speed and wavelength` |
| baseline | `mmlu_4812` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4813` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_4814` | `mcq` | true | `D` | `D. All reach the base at the same time.` |
| baseline | `mmlu_4815` | `mcq` | false | `A` | `B. 300 m` |
| baseline | `mmlu_4816` | `mcq` | false | `D` | `C. 45°` |
| baseline | `mmlu_4817` | `mcq` | false | `D` | `B. 41°` |
| baseline | `mmlu_4818` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4819` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4820` | `mcq` | false | `A` | `C. 200 μN` |
| baseline | `mmlu_4821` | `mcq` | false | `A` | `D. Linear momentum` |
| baseline | `mmlu_4822` | `mcq` | false | `C` | `D. 60 m` |
| baseline | `mmlu_4823` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4824` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4825` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4826` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4827` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4828` | `mcq` | false | `C` | `B. 1.0 m/s` |
| baseline | `mmlu_4829` | `mcq` | false | `D` | `C. The image gets smaller at first and then bigger in size.` |
| baseline | `mmlu_4830` | `mcq` | false | `D` | `A. Zero` |
| baseline | `mmlu_4831` | `mcq` | false | `B` | `A. 200 N` |
| baseline | `mmlu_4832` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4833` | `mcq` | false | `C` | `A. 5.4 × 10–10 J` |
| baseline | `mmlu_4834` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4835` | `mcq` | false | `C` | `A. 0.16 N` |
| baseline | `mmlu_4836` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4837` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4838` | `mcq` | true | `B` | `B. 25 m/s, downward` |
| baseline | `mmlu_4839` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4840` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4841` | `mcq` | false | `B` | `D. Decreasing the mass of the ball` |
| baseline | `mmlu_4842` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4843` | `mcq` | false | `D` | `B. 0.8 m` |
| baseline | `mmlu_4844` | `mcq` | true | `C` | `C. 4 s` |
| baseline | `mmlu_4845` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4846` | `mcq` | false | `B` | `C. 9.8 m/s^2` |
| baseline | `mmlu_4847` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4848` | `mcq` | true | `A` | `A. Static friction` |
| baseline | `mmlu_4849` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4850` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4851` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4852` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4853` | `mcq` | false | `C` | `B. 2h` |
| baseline | `mmlu_4854` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4855` | `mcq` | true | `C` | `C. 10^19 N` |
| baseline | `mmlu_4856` | `mcq` | false | `D` | `C. 60%` |
| baseline | `mmlu_4857` | `mcq` | true | `C` | `C. 18 m/s^2` |
| baseline | `mmlu_4858` | `mcq` | false | `A` | `D. No.` |
| baseline | `mmlu_4859` | `mcq` | false | `A` | `B. 10.5 s` |
| baseline | `mmlu_4860` | `mcq` | true | `D` | `D. I and II only` |
| baseline | `mmlu_4861` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4862` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4863` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4864` | `mcq` | false | `D` | `A. 100 μC` |
| baseline | `mmlu_4865` | `mcq` | false | `B` | `C. 4.5 N` |
| baseline | `mmlu_4866` | `mcq` | true | `D` | `D. a combination of the normal force and the friction force` |
| baseline | `mmlu_4867` | `mcq` | true | `C` | `C. 50 m/s` |
| baseline | `mmlu_4868` | `mcq` | true | `D` | `D. It remains the same.` |
| baseline | `mmlu_4869` | `mcq` | false | `B` | `A. 0.25 A` |
| baseline | `mmlu_4870` | `mcq` | false | `B` | `A. P decreases by a factor of 16.` |
| baseline | `mmlu_4871` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4872` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4873` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4874` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4875` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4876` | `mcq` | true | `C` | `C. Both the length and area` |
| baseline | `mmlu_4877` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4878` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4879` | `mcq` | false | `A` | `D. 1/2 F` |
| baseline | `mmlu_4880` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4881` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4882` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4883` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4884` | `mcq` | false | `D` | `C. (1/5) AU` |
| baseline | `mmlu_4885` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4886` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4887` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4888` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4889` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4890` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4891` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4892` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4893` | `mcq` | true | `A` | `A. variance` |
| baseline | `mmlu_4894` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4895` | `mcq` | false | `A` | `B. in the middle of the list` |
| baseline | `mmlu_4896` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4897` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4898` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4899` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4900` | `mcq` | true | `B` | `B. standardized` |
| baseline | `mmlu_4901` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4902` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4903` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4904` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4905` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4906` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4907` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4908` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4909` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4910` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4911` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4912` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4913` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4914` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4915` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4916` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4917` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4918` | `mcq` | true | `A` | `A. Inferential statistics` |
| baseline | `mmlu_4919` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4920` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4921` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4922` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4923` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4924` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4925` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4926` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4927` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4928` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4929` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4930` | `mcq` | true | `B` | `B. remembering how to tie a tie` |
| baseline | `mmlu_4931` | `mcq` | true | `D` | `D. survey` |
| baseline | `mmlu_4932` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4933` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4934` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4935` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4936` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4937` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4938` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4939` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4940` | `mcq` | true | `D` | `D. dissociative` |
| baseline | `mmlu_4941` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4942` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4943` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4944` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4945` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4946` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4947` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4948` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4949` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4950` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4951` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4952` | `mcq` | false | `B` | `C. red` |
| baseline | `mmlu_4953` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4954` | `mcq` | true | `A` | `A. olfactory receptors` |
| baseline | `mmlu_4955` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4956` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4957` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4958` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4959` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4960` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4961` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4962` | `mcq` | true | `D` | `D. positive psychology` |
| baseline | `mmlu_4963` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4964` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4965` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4966` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4967` | `mcq` | true | `D` | `D. brain plasticity` |
| baseline | `mmlu_4968` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4969` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4970` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4971` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4972` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4973` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4974` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4975` | `mcq` | false | `B` | `A. 9` |
| baseline | `mmlu_4976` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4977` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4978` | `mcq` | true | `B` | `B. long-term potentiation` |
| baseline | `mmlu_4979` | `mcq` | false | `C` | `A. sensation and perception` |
| baseline | `mmlu_4980` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4981` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4982` | `mcq` | true | `D` | `D. post-traumatic stress disorder` |
| baseline | `mmlu_4983` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4984` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4985` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4986` | `mcq` | true | `D` | `D. Melatonin` |
| baseline | `mmlu_4987` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4988` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4989` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4990` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4991` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4992` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4993` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4994` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4995` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4996` | `mcq` | true | `D` | `D. Mania` |
| baseline | `mmlu_4997` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4998` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4999` | `mcq` | true | `C` | `C. 90` |
