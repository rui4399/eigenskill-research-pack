# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 248 / 500 | 0.4960 | 5.1815 | 0.429641 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_4000` | `mcq` | false | `D` | `A. households provide goods to firms in exchange for wage payments.` |
| baseline | `mmlu_4001` | `mcq` | false | `C` | `A. increase imports` |
| baseline | `mmlu_4002` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4003` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4004` | `mcq` | true | `C` | `C. Decreasing     Increasing` |
| baseline | `mmlu_4005` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4006` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4007` | `mcq` | true | `D` | `D. Higher government funding of research on clean energy supplies` |
| baseline | `mmlu_4008` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4009` | `mcq` | false | `D` | `A. 10 years.` |
| baseline | `mmlu_4010` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4011` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4012` | `mcq` | true | `A` | `A. The capital account` |
| baseline | `mmlu_4013` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4014` | `mcq` | true | `B` | `B. Structural unemployment` |
| baseline | `mmlu_4015` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4016` | `mcq` | true | `A` | `A. 10 percent $450 in excess reserves` |
| baseline | `mmlu_4017` | `mcq` | true | `B` | `B. expansionary   4   -3` |
| baseline | `mmlu_4018` | `mcq` | false | `A` | `D. Decreased demand     Depreciating` |
| baseline | `mmlu_4019` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4020` | `mcq` | true | `A` | `A. Nation A has comparative advantage in the production of that good.` |
| baseline | `mmlu_4021` | `mcq` | false | `D` | `A. Increase` |
| baseline | `mmlu_4022` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4023` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4024` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4025` | `mcq` | true | `C` | `C. Medium of exchange` |
| baseline | `mmlu_4026` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4027` | `mcq` | false | `D` | `B. Increased demand   Rising   Appreciates` |
| baseline | `mmlu_4028` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4029` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4030` | `mcq` | true | `D` | `D. Inflation` |
| baseline | `mmlu_4031` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4032` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4033` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4034` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4035` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4036` | `mcq` | false | `D` | `B. Increase in demand   Buying Rising` |
| baseline | `mmlu_4037` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4038` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4039` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4040` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4041` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4042` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_4043` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4044` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_4045` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4046` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4047` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4048` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4049` | `mcq` | true | `C` | `C. The entire consumption function would shift upward.` |
| baseline | `mmlu_4050` | `mcq` | true | `C` | `C. Increases in the interest rate` |
| baseline | `mmlu_4051` | `mcq` | false | `D` | `C. I and III are correct.` |
| baseline | `mmlu_4052` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4053` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4054` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4055` | `mcq` | false | `C` | `B. decreased by 4 percent.` |
| baseline | `mmlu_4056` | `mcq` | true | `D` | `D. Deposits` |
| baseline | `mmlu_4057` | `mcq` | true | `C` | `C. Real GDP per capita.` |
| baseline | `mmlu_4058` | `mcq` | false | `D` | `A. $400` |
| baseline | `mmlu_4059` | `mcq` | true | `D` | `D. An increase in aggregate supply.` |
| baseline | `mmlu_4060` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_4061` | `mcq` | false | `C` | `A. 25% $750 M = ¼` |
| baseline | `mmlu_4062` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4063` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4064` | `mcq` | true | `D` | `D. Decreases   Decreases    Decreases` |
| baseline | `mmlu_4065` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4066` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4067` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4068` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4069` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4070` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4071` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4072` | `mcq` | true | `A` | `A. 125` |
| baseline | `mmlu_4073` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4074` | `mcq` | true | `D` | `D. Lower taxes on personal income` |
| baseline | `mmlu_4075` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4076` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4077` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4078` | `mcq` | true | `D` | `D. Higher consumer prices and a misallocation of resources away from efficient producers` |
| baseline | `mmlu_4079` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4080` | `mcq` | true | `C` | `C. decrease interest rates and risk an inflationary period.` |
| baseline | `mmlu_4081` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4082` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4083` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_4084` | `mcq` | false | `D` | `B. Decrease     Decrease     Decrease     Increase` |
| baseline | `mmlu_4085` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4086` | `mcq` | false | `D` | `C. output and population must have increased.` |
| baseline | `mmlu_4087` | `mcq` | true | `D` | `D. not counted in GDP.` |
| baseline | `mmlu_4088` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4089` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4090` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4091` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4092` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4093` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4094` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4095` | `mcq` | true | `D` | `D. Increase     Decrease     Increase` |
| baseline | `mmlu_4096` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4097` | `mcq` | false | `C` | `B. Money supply remains constant the interest rate does not fall and AD does not increase.` |
| baseline | `mmlu_4098` | `mcq` | false | `D` | `A. current-account balance only` |
| baseline | `mmlu_4099` | `mcq` | true | `D` | `D. Investment tax credits.` |
| baseline | `mmlu_4100` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4101` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4102` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4103` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4104` | `mcq` | false | `C` | `B. 5.0 percent.` |
| baseline | `mmlu_4105` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4106` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4107` | `mcq` | false | `A` | `B. (B) Increased     Increased` |
| baseline | `mmlu_4108` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4109` | `mcq` | false | `D` | `C. Real GDP will remain unchanged.` |
| baseline | `mmlu_4110` | `mcq` | true | `D` | `D. Increased     Decreased` |
| baseline | `mmlu_4111` | `mcq` | false | `C` | `B. $1,200` |
| baseline | `mmlu_4112` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4113` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4114` | `mcq` | true | `D` | `D. An increase in government spending` |
| baseline | `mmlu_4115` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4116` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4117` | `mcq` | true | `D` | `D. Saving is equal to zero when consumption equals disposable income.` |
| baseline | `mmlu_4118` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4119` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4120` | `mcq` | true | `B` | `B. A new production technique that lowers costs.` |
| baseline | `mmlu_4121` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4122` | `mcq` | false | `C` | `A/B/C/D` |
| baseline | `mmlu_4123` | `mcq` | true | `B` | `B. determined by supply and demand.` |
| baseline | `mmlu_4124` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4125` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4126` | `mcq` | true | `B` | `B. $4,500` |
| baseline | `mmlu_4127` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4128` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4129` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4130` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4131` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4132` | `mcq` | true | `B` | `B. $3,000` |
| baseline | `mmlu_4133` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4134` | `mcq` | true | `D` | `D. all of the above` |
| baseline | `mmlu_4135` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_4136` | `mcq` | true | `C` | `C. depository institutions decide to hold more excess reserves.` |
| baseline | `mmlu_4137` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4138` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4139` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4140` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4141` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4142` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4143` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4144` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4145` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4146` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4147` | `mcq` | false | `D` | `A. Decrease   Increase   Increase` |
| baseline | `mmlu_4148` | `mcq` | true | `B` | `B. supply shocks` |
| baseline | `mmlu_4149` | `mcq` | false | `B` | `A. Only I is true.` |
| baseline | `mmlu_4150` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_4151` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4152` | `mcq` | false | `B` | `D. Greater than $200 but less than $500` |
| baseline | `mmlu_4153` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4154` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4155` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4156` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4157` | `mcq` | true | `A` | `A. Higher disposable income higher consumption higher real GDP lower unemployment` |
| baseline | `mmlu_4158` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4159` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_4160` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4161` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_4162` | `mcq` | true | `D` | `D. An increase in demand increasing the interest rate.` |
| baseline | `mmlu_4163` | `mcq` | false | `D` | `A. Decreases appreciate decreases` |
| baseline | `mmlu_4164` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4165` | `mcq` | false | `D` | `B` |
| baseline | `mmlu_4166` | `mcq` | true | `D` | `D. Frictional` |
| baseline | `mmlu_4167` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_4168` | `mcq` | false | `C` | `D. $1,900` |
| baseline | `mmlu_4169` | `mcq` | false | `D` | `C. The equilibrium price level and quantity of output increase.` |
| baseline | `mmlu_4170` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4171` | `mcq` | false | `A` | `D. I and III` |
| baseline | `mmlu_4172` | `mcq` | true | `B` | `B. More investment in capital infrastructure and less consumption of nondurable goods and services` |
| baseline | `mmlu_4173` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4174` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4175` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4176` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4177` | `mcq` | false | `A` | `B. Decrease   Decrease    Increase` |
| baseline | `mmlu_4178` | `mcq` | true | `C` | `C. Buying Treasury securities from commercial banks` |
| baseline | `mmlu_4179` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4180` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4181` | `mcq` | false | `D` | `A. Increases            Increases      Increases` |
| baseline | `mmlu_4182` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4183` | `mcq` | true | `A` | `A. appreciate.` |
| baseline | `mmlu_4184` | `mcq` | true | `A` | `A. deficit recession surplus expansion` |
| baseline | `mmlu_4185` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4186` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4187` | `mcq` | true | `A` | `A. Shifts down     Falls     Rises` |
| baseline | `mmlu_4188` | `mcq` | false | `C` | `D. France has the absolute advantage in cheese.` |
| baseline | `mmlu_4189` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_4190` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4191` | `mcq` | true | `D` | `D. I and III.` |
| baseline | `mmlu_4192` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4193` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4194` | `mcq` | false | `A` | `B. this will cause the supply of the product to decrease right now.` |
| baseline | `mmlu_4195` | `mcq` | true | `B` | `B. the checking deposits increase.` |
| baseline | `mmlu_4196` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4197` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4198` | `mcq` | false | `A` | `B. increases decreases deficit` |
| baseline | `mmlu_4199` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4200` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4201` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4202` | `mcq` | false | `B` | `A. budget surpluses and higher discount rates.` |
| baseline | `mmlu_4203` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4204` | `mcq` | true | `B` | `B. Unit of account` |
| baseline | `mmlu_4205` | `mcq` | false | `B` | `A. higher taxes on corporate profits.` |
| baseline | `mmlu_4206` | `mcq` | true | `A` | `A. the aggregate demand curve should be shifted to the right.` |
| baseline | `mmlu_4207` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4208` | `mcq` | true | `B` | `B. Depreciation in the international value of the dollar` |
| baseline | `mmlu_4209` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_4210` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4211` | `mcq` | true | `D` | `D. Increasing money spent to pay for government projects` |
| baseline | `mmlu_4212` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4213` | `mcq` | false | `B` | `A. increase by $200 million.` |
| baseline | `mmlu_4214` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_4215` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4216` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4217` | `mcq` | true | `B` | `B. increase aggregate demand which will increase real output and increase employment.` |
| baseline | `mmlu_4218` | `mcq` | false | `B` | `C. I and IV only` |
| baseline | `mmlu_4219` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_4220` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4221` | `mcq` | false | `D` | `A. Lower interest rates in the United States relative to China` |
| baseline | `mmlu_4222` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_4223` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_4224` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4225` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4226` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_4227` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4228` | `mcq` | false | `D` | `A. (0, – 3)` |
| baseline | `mmlu_4229` | `mcq` | true | `C` | `C. 50` |
| baseline | `mmlu_4230` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4231` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4232` | `mcq` | true | `C` | `C. (-inf, 8)` |
| baseline | `mmlu_4233` | `mcq` | false | `B` | `A. 396` |
| baseline | `mmlu_4234` | `mcq` | false | `C` | `A. 0.16` |
| baseline | `mmlu_4235` | `mcq` | false | `A` | `C. 36` |
| baseline | `mmlu_4236` | `mcq` | false | `C` | `A. \(\frac{125}{648}\)` |
| baseline | `mmlu_4237` | `mcq` | false | `B` | `A. 8` |
| baseline | `mmlu_4238` | `mcq` | false | `D` | `B. 14` |
| baseline | `mmlu_4239` | `mcq` | false | `D` | `C. 2048` |
| baseline | `mmlu_4240` | `mcq` | true | `D` | `D. 4` |
| baseline | `mmlu_4241` | `mcq` | false | `B` | `C. 94.5` |
| baseline | `mmlu_4242` | `mcq` | false | `D` | `B. L <= T <= M <= R` |
| baseline | `mmlu_4243` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4244` | `mcq` | true | `A` | `A. 8` |
| baseline | `mmlu_4245` | `mcq` | false | `B` | `A. -2` |
| baseline | `mmlu_4246` | `mcq` | false | `A` | `C. 0` |
| baseline | `mmlu_4247` | `mcq` | false | `B` | `A. (-∞,-1)∪(1,+∞)` |
| baseline | `mmlu_4248` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4249` | `mcq` | false | `B` | `C. -32` |
| baseline | `mmlu_4250` | `mcq` | false | `D` | `A. 7` |
| baseline | `mmlu_4251` | `mcq` | false | `B` | `A. 4` |
| baseline | `mmlu_4252` | `mcq` | false | `A` | `B. Thursday` |
| baseline | `mmlu_4253` | `mcq` | false | `C` | `B. 3` |
| baseline | `mmlu_4254` | `mcq` | true | `D` | `D. 70` |
| baseline | `mmlu_4255` | `mcq` | false | `C` | `B. 5 min` |
| baseline | `mmlu_4256` | `mcq` | false | `C` | `D. (-inf, -1) U (-1, 4) U (4, inf)` |
| baseline | `mmlu_4257` | `mcq` | true | `D` | `D. 1/e` |
| baseline | `mmlu_4258` | `mcq` | true | `C` | `C. 0` |
| baseline | `mmlu_4259` | `mcq` | false | `A` | `C. 24` |
| baseline | `mmlu_4260` | `mcq` | false | `D` | `C. 840` |
| baseline | `mmlu_4261` | `mcq` | true | `A` | `A. 8788` |
| baseline | `mmlu_4262` | `mcq` | false | `A` | `C. -6` |
| baseline | `mmlu_4263` | `mcq` | false | `D` | `A. 15` |
| baseline | `mmlu_4264` | `mcq` | false | `C` | `B. 4680` |
| baseline | `mmlu_4265` | `mcq` | false | `C` | `A. 4.5` |
| baseline | `mmlu_4266` | `mcq` | true | `A` | `A. 240` |
| baseline | `mmlu_4267` | `mcq` | false | `A` | `B. 5` |
| baseline | `mmlu_4268` | `mcq` | false | `B` | `C. -1` |
| baseline | `mmlu_4269` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4270` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4271` | `mcq` | false | `C` | `A. (6-3x)(6+3x)` |
| baseline | `mmlu_4272` | `mcq` | false | `C` | `B. 90950` |
| baseline | `mmlu_4273` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4274` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4275` | `mcq` | false | `A` | `B. 5` |
| baseline | `mmlu_4276` | `mcq` | false | `D` | `A. 792` |
| baseline | `mmlu_4277` | `mcq` | true | `B` | `B. -75` |
| baseline | `mmlu_4278` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4279` | `mcq` | true | `A` | `A. 100` |
| baseline | `mmlu_4280` | `mcq` | true | `B` | `B. 9` |
| baseline | `mmlu_4281` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4282` | `mcq` | false | `C` | `B. \frac{1}{64}` |
| baseline | `mmlu_4283` | `mcq` | false | `A` | `B. \(\frac{25}{6}\)` |
| baseline | `mmlu_4284` | `mcq` | false | `B` | `C. \(\frac{1}{7}\)` |
| baseline | `mmlu_4285` | `mcq` | false | `B` | `C. 3, 9` |
| baseline | `mmlu_4286` | `mcq` | true | `B` | `B. 120` |
| baseline | `mmlu_4287` | `mcq` | false | `C` | `A. 1` |
| baseline | `mmlu_4288` | `mcq` | true | `D` | `D. 2793` |
| baseline | `mmlu_4289` | `mcq` | true | `B` | `B. 4.875` |
| baseline | `mmlu_4290` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_4291` | `mcq` | false | `D` | `B. 2321` |
| baseline | `mmlu_4292` | `mcq` | true | `C` | `C. -128` |
| baseline | `mmlu_4293` | `mcq` | false | `B` | `A. –12` |
| baseline | `mmlu_4294` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_4295` | `mcq` | false | `B` | `C. 18` |
| baseline | `mmlu_4296` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4297` | `mcq` | true | `A` | `A. 5` |
| baseline | `mmlu_4298` | `mcq` | true | `C` | `C. 625` |
| baseline | `mmlu_4299` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4300` | `mcq` | false | `A` | `C. 27` |
| baseline | `mmlu_4301` | `mcq` | false | `C` | `B. 13` |
| baseline | `mmlu_4302` | `mcq` | true | `B` | `B. 1` |
| baseline | `mmlu_4303` | `mcq` | false | `D` | `A. 10240` |
| baseline | `mmlu_4304` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4305` | `mcq` | false | `A` | `C. 11` |
| baseline | `mmlu_4306` | `mcq` | true | `C` | `C. Friday` |
| baseline | `mmlu_4307` | `mcq` | true | `B` | `B. January 21st` |
| baseline | `mmlu_4308` | `mcq` | true | `B` | `B. 76` |
| baseline | `mmlu_4309` | `mcq` | true | `A` | `A. 89` |
| baseline | `mmlu_4310` | `mcq` | false | `C` | `A. 11` |
| baseline | `mmlu_4311` | `mcq` | false | `D` | `A. 6` |
| baseline | `mmlu_4312` | `mcq` | false | `D` | `C. 60` |
| baseline | `mmlu_4313` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_4314` | `mcq` | false | `D` | `C. 18` |
| baseline | `mmlu_4315` | `mcq` | false | `A` | `B. 72` |
| baseline | `mmlu_4316` | `mcq` | false | `D` | `C. 32` |
| baseline | `mmlu_4317` | `mcq` | false | `C` | `D. 0` |
| baseline | `mmlu_4318` | `mcq` | false | `B` | `A. 36` |
| baseline | `mmlu_4319` | `mcq` | false | `C` | `A. \(\frac{x-5}{3}\)` |
| baseline | `mmlu_4320` | `mcq` | false | `B` | `A. 1` |
| baseline | `mmlu_4321` | `mcq` | false | `D` | `B. 16` |
| baseline | `mmlu_4322` | `mcq` | false | `A` | `C. \(\frac{7}{12}\)` |
| baseline | `mmlu_4323` | `mcq` | true | `A` | `A. -1/144` |
| baseline | `mmlu_4324` | `mcq` | false | `A` | `C. 0.33` |
| baseline | `mmlu_4325` | `mcq` | true | `B` | `B. 30%` |
| baseline | `mmlu_4326` | `mcq` | false | `C` | `A. 9` |
| baseline | `mmlu_4327` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4328` | `mcq` | true | `B` | `B. x+11` |
| baseline | `mmlu_4329` | `mcq` | false | `D` | `A. 13` |
| baseline | `mmlu_4330` | `mcq` | false | `C` | `D. 54,320` |
| baseline | `mmlu_4331` | `mcq` | true | `D` | `D. 25` |
| baseline | `mmlu_4332` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4333` | `mcq` | true | `A` | `A. 2` |
| baseline | `mmlu_4334` | `mcq` | true | `B` | `B. 31` |
| baseline | `mmlu_4335` | `mcq` | false | `C` | `A. 34` |
| baseline | `mmlu_4336` | `mcq` | false | `C` | `B. 16` |
| baseline | `mmlu_4337` | `mcq` | false | `D` | `B. \(\frac{7}{9}\)` |
| baseline | `mmlu_4338` | `mcq` | false | `C` | `A. 2.62` |
| baseline | `mmlu_4339` | `mcq` | false | `C` | `A. 300` |
| baseline | `mmlu_4340` | `mcq` | false | `A` | `B. 46` |
| baseline | `mmlu_4341` | `mcq` | true | `A` | `A. 12^(1/7)` |
| baseline | `mmlu_4342` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_4343` | `mcq` | true | `A` | `A. 80` |
| baseline | `mmlu_4344` | `mcq` | false | `C` | `B. 1` |
| baseline | `mmlu_4345` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_4346` | `mcq` | true | `A` | `A. 288` |
| baseline | `mmlu_4347` | `mcq` | false | `B` | `A. 16` |
| baseline | `mmlu_4348` | `mcq` | false | `B` | `D. 999` |
| baseline | `mmlu_4349` | `mcq` | true | `A` | `A. \(\frac{1}{2}\)` |
| baseline | `mmlu_4350` | `mcq` | false | `D` | `A. 337125` |
| baseline | `mmlu_4351` | `mcq` | true | `B` | `B. 10` |
| baseline | `mmlu_4352` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_4353` | `mcq` | true | `D` | `D. 20` |
| baseline | `mmlu_4354` | `mcq` | false | `A` | `B. 592,704` |
| baseline | `mmlu_4355` | `mcq` | false | `C` | `B. 0.86` |
| baseline | `mmlu_4356` | `mcq` | true | `C` | `C. 0.547` |
| baseline | `mmlu_4357` | `mcq` | false | `B` | `C. 4` |
| baseline | `mmlu_4358` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_4359` | `mcq` | false | `B` | `C. -38` |
| baseline | `mmlu_4360` | `mcq` | true | `D` | `D. 71` |
| baseline | `mmlu_4361` | `mcq` | true | `B` | `B. 320` |
| baseline | `mmlu_4362` | `mcq` | false | `B` | `A. $227.50` |
| baseline | `mmlu_4363` | `mcq` | false | `B` | `C. 100` |
| baseline | `mmlu_4364` | `mcq` | true | `B` | `B. 6` |
| baseline | `mmlu_4365` | `mcq` | true | `B` | `B. 135` |
| baseline | `mmlu_4366` | `mcq` | true | `B` | `B. 5400` |
| baseline | `mmlu_4367` | `mcq` | true | `D` | `D. 8.6` |
| baseline | `mmlu_4368` | `mcq` | false | `D` | `A. Domain and range remain the same` |
| baseline | `mmlu_4369` | `mcq` | false | `B` | `C. 112` |
| baseline | `mmlu_4370` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_4371` | `mcq` | true | `A` | `A. 90` |
| baseline | `mmlu_4372` | `mcq` | true | `D` | `D. 25` |
| baseline | `mmlu_4373` | `mcq` | true | `D` | `D. 104/3` |
| baseline | `mmlu_4374` | `mcq` | false | `A` | `B. 99` |
| baseline | `mmlu_4375` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4376` | `mcq` | false | `D` | `A. -\frac{7}{12}` |
| baseline | `mmlu_4377` | `mcq` | false | `D` | `A. 54` |
| baseline | `mmlu_4378` | `mcq` | true | `C` | `C. -1.5` |
| baseline | `mmlu_4379` | `mcq` | false | `C` | `D. 574` |
| baseline | `mmlu_4380` | `mcq` | false | `C` | `A. 12` |
| baseline | `mmlu_4381` | `mcq` | true | `B` | `B. 298` |
| baseline | `mmlu_4382` | `mcq` | true | `A` | `A. \(\frac{8}{45}\)` |
| baseline | `mmlu_4383` | `mcq` | false | `C` | `B. 8` |
| baseline | `mmlu_4384` | `mcq` | false | `D` | `A. 18` |
| baseline | `mmlu_4385` | `mcq` | false | `D` | `A. 1` |
| baseline | `mmlu_4386` | `mcq` | false | `B` | `A. 38` |
| baseline | `mmlu_4387` | `mcq` | true | `A` | `A. 7` |
| baseline | `mmlu_4388` | `mcq` | false | `A` | `C. \(\frac{10}{3}\)` |
| baseline | `mmlu_4389` | `mcq` | true | `B` | `B. $8,902` |
| baseline | `mmlu_4390` | `mcq` | true | `D` | `D. 3,003` |
| baseline | `mmlu_4391` | `mcq` | false | `C` | `B. 2.931` |
| baseline | `mmlu_4392` | `mcq` | true | `B` | `B. 0` |
| baseline | `mmlu_4393` | `mcq` | false | `D` | `B. 1024` |
| baseline | `mmlu_4394` | `mcq` | true | `B` | `B. 40` |
| baseline | `mmlu_4395` | `mcq` | true | `B` | `B. –33%` |
| baseline | `mmlu_4396` | `mcq` | true | `B` | `B. \(\frac{15}{2}\)` |
| baseline | `mmlu_4397` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_4398` | `mcq` | false | `D` | `C. 4-i` |
| baseline | `mmlu_4399` | `mcq` | true | `C` | `C. 39` |
| baseline | `mmlu_4400` | `mcq` | true | `B` | `B. 3` |
| baseline | `mmlu_4401` | `mcq` | false | `C` | `B. $\frac{7}{12}$` |
| baseline | `mmlu_4402` | `mcq` | true | `C` | `C. 20%` |
| baseline | `mmlu_4403` | `mcq` | true | `C` | `C. 3980` |
| baseline | `mmlu_4404` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4405` | `mcq` | false | `D` | `B. \(\frac{17}{66}\)` |
| baseline | `mmlu_4406` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4407` | `mcq` | false | `D` | `B. 32π/3` |
| baseline | `mmlu_4408` | `mcq` | true | `A` | `A. \(\frac{5}{4}\)` |
| baseline | `mmlu_4409` | `mcq` | true | `D` | `D. 2π` |
| baseline | `mmlu_4410` | `mcq` | false | `A` | `B. 34` |
| baseline | `mmlu_4411` | `mcq` | false | `C` | `A. 2` |
| baseline | `mmlu_4412` | `mcq` | false | `C` | `B. 22140` |
| baseline | `mmlu_4413` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_4414` | `mcq` | false | `D` | `A. \(\frac{1}{4}\)` |
| baseline | `mmlu_4415` | `mcq` | true | `C` | `C. 36` |
| baseline | `mmlu_4416` | `mcq` | true | `B` | `B. 55` |
| baseline | `mmlu_4417` | `mcq` | true | `A` | `A. 29` |
| baseline | `mmlu_4418` | `mcq` | false | `C` | `A. \(\frac{5}{24}\)` |
| baseline | `mmlu_4419` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_4420` | `mcq` | false | `B` | `A. 3` |
| baseline | `mmlu_4421` | `mcq` | false | `C` | `B. 6` |
| baseline | `mmlu_4422` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_4423` | `mcq` | false | `C` | `A. 6` |
| baseline | `mmlu_4424` | `mcq` | true | `D` | `D. p+q-r` |
| baseline | `mmlu_4425` | `mcq` | true | `B` | `B. 2 × 5` |
| baseline | `mmlu_4426` | `mcq` | false | `D` | `B. 6` |
| baseline | `mmlu_4427` | `mcq` | false | `C` | `D. (–3, –2)` |
| baseline | `mmlu_4428` | `mcq` | false | `C` | `B. 20` |
| baseline | `mmlu_4429` | `mcq` | false | `D` | `B. \frac{8}{15}` |
| baseline | `mmlu_4430` | `mcq` | false | `D` | `A. 67` |
| baseline | `mmlu_4431` | `mcq` | true | `B` | `B. -14` |
| baseline | `mmlu_4432` | `mcq` | true | `A` | `A. 50 + 50i` |
| baseline | `mmlu_4433` | `mcq` | false | `D` | `A. 10` |
| baseline | `mmlu_4434` | `mcq` | false | `A` | `C. -40` |
| baseline | `mmlu_4435` | `mcq` | false | `C` | `A. 46/3` |
| baseline | `mmlu_4436` | `mcq` | true | `A` | `A. -4` |
| baseline | `mmlu_4437` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_4438` | `mcq` | false | `C` | `B. 36 inches` |
| baseline | `mmlu_4439` | `mcq` | false | `C` | `A. \(\frac{13}{4}\)` |
| baseline | `mmlu_4440` | `mcq` | false | `C` | `A. 2` |
| baseline | `mmlu_4441` | `mcq` | false | `D` | `A. $\frac{3}{4}$` |
| baseline | `mmlu_4442` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_4443` | `mcq` | false | `B` | `C. I` |
| baseline | `mmlu_4444` | `mcq` | false | `D` | `C. 0 ≤ y ≤ 6` |
| baseline | `mmlu_4445` | `mcq` | true | `D` | `D. y – 4 = ln 2(x – 5)` |
| baseline | `mmlu_4446` | `mcq` | true | `A` | `A. \(\frac{1}{2}\)` |
| baseline | `mmlu_4447` | `mcq` | false | `B` | `A. 7` |
| baseline | `mmlu_4448` | `mcq` | false | `D` | `B. 2` |
| baseline | `mmlu_4449` | `mcq` | true | `B` | `B. 400` |
| baseline | `mmlu_4450` | `mcq` | true | `B` | `B. \(\frac{161}{36}\)` |
| baseline | `mmlu_4451` | `mcq` | true | `A` | `A. 112` |
| baseline | `mmlu_4452` | `mcq` | false | `D` | `C. 12` |
| baseline | `mmlu_4453` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_4454` | `mcq` | false | `A` | `B. 120` |
| baseline | `mmlu_4455` | `mcq` | false | `B` | `C. 2.427` |
| baseline | `mmlu_4456` | `mcq` | false | `C` | `B. 64` |
| baseline | `mmlu_4457` | `mcq` | false | `B` | `C. 87` |
| baseline | `mmlu_4458` | `mcq` | true | `A` | `A. 165` |
| baseline | `mmlu_4459` | `mcq` | false | `C` | `A. 0 or –1/3` |
| baseline | `mmlu_4460` | `mcq` | false | `A` | `B. 276` |
| baseline | `mmlu_4461` | `mcq` | false | `C` | `A. 28` |
| baseline | `mmlu_4462` | `mcq` | false | `D` | `C. 2` |
| baseline | `mmlu_4463` | `mcq` | false | `C` | `A. 5,760` |
| baseline | `mmlu_4464` | `mcq` | false | `C` | `B. 33` |
| baseline | `mmlu_4465` | `mcq` | false | `A` | `B. 12` |
| baseline | `mmlu_4466` | `mcq` | false | `B` | `A. \(\frac{4\sqrt{3}}{33}\)` |
| baseline | `mmlu_4467` | `mcq` | true | `A` | `A. 1/e` |
| baseline | `mmlu_4468` | `mcq` | false | `A` | `B. \(\frac{27}{128}\)` |
| baseline | `mmlu_4469` | `mcq` | true | `B` | `B. east` |
| baseline | `mmlu_4470` | `mcq` | false | `C` | `A. 15` |
| baseline | `mmlu_4471` | `mcq` | false | `C` | `B. 4` |
| baseline | `mmlu_4472` | `mcq` | false | `C` | `B. (\(\frac{231}{20}\), \(\frac{21}{20}\))` |
| baseline | `mmlu_4473` | `mcq` | false | `C` | `B. θ = 0.39` |
| baseline | `mmlu_4474` | `mcq` | false | `D` | `A. 4.68` |
| baseline | `mmlu_4475` | `mcq` | false | `C` | `A. none` |
| baseline | `mmlu_4476` | `mcq` | false | `D` | `C. 4` |
| baseline | `mmlu_4477` | `mcq` | false | `C` | `A. [-\frac{1}{2}, 0]` |
| baseline | `mmlu_4478` | `mcq` | true | `B` | `B. 2` |
| baseline | `mmlu_4479` | `mcq` | false | `D` | `B. 2049` |
| baseline | `mmlu_4480` | `mcq` | false | `B` | `A. 3` |
| baseline | `mmlu_4481` | `mcq` | false | `B` | `C. 9.2` |
| baseline | `mmlu_4482` | `mcq` | true | `B` | `B. 800,000 + 650 D` |
| baseline | `mmlu_4483` | `mcq` | false | `B` | `C. 4` |
| baseline | `mmlu_4484` | `mcq` | false | `D` | `B. -2` |
| baseline | `mmlu_4485` | `mcq` | true | `B` | `B. 27` |
| baseline | `mmlu_4486` | `mcq` | true | `B` | `B. \frac{1}{12}` |
| baseline | `mmlu_4487` | `mcq` | true | `A` | `A. (0, 9)` |
| baseline | `mmlu_4488` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_4489` | `mcq` | false | `C` | `B. 4680` |
| baseline | `mmlu_4490` | `mcq` | true | `A` | `A. 5, 14` |
| baseline | `mmlu_4491` | `mcq` | true | `D` | `D. 1920` |
| baseline | `mmlu_4492` | `mcq` | false | `D` | `C. 3.999` |
| baseline | `mmlu_4493` | `mcq` | false | `C` | `A. 16401` |
| baseline | `mmlu_4494` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_4495` | `mcq` | false | `B` | `C. 7.98` |
| baseline | `mmlu_4496` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_4497` | `mcq` | false | `B` | `A. -80` |
| baseline | `mmlu_4498` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_4499` | `mcq` | false | `C` | `B` |
