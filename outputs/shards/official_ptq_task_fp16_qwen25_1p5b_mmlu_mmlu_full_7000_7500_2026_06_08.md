# Chat Task Benchmark

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Tasks: `500`
Task format: `mmlu`
Chat template: `True`
No-think prompt: `True`

## Aggregate

| split | passes | accuracy | mean tok/s | mean TTFT s |
|---|---:|---:|---:|---:|
| baseline | 387 / 500 | 0.7740 | 5.1819 | 0.389599 |

## Rows

| split | id | type | passed | expected | generated |
|---|---|---|---:|---|---|
| baseline | `mmlu_7000` | `mcq` | false | `D` | `C. Global competition` |
| baseline | `mmlu_7001` | `mcq` | false | `D` | `B. Processes` |
| baseline | `mmlu_7002` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7003` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7004` | `mcq` | true | `D` | `D. Specific, measurable, achievable, rewarded and timely` |
| baseline | `mmlu_7005` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7006` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7007` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7008` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7009` | `mcq` | false | `D` | `C` |
| baseline | `mmlu_7010` | `mcq` | true | `B` | `B. Market penetration` |
| baseline | `mmlu_7011` | `mcq` | true | `D` | `D. remotely` |
| baseline | `mmlu_7012` | `mcq` | true | `D` | `D. Assertive and sociable` |
| baseline | `mmlu_7013` | `mcq` | true | `B` | `B. Mission statement` |
| baseline | `mmlu_7014` | `mcq` | true | `B` | `B. Strategy formulation` |
| baseline | `mmlu_7015` | `mcq` | true | `B` | `B. Time and motion studies` |
| baseline | `mmlu_7016` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7017` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7018` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7019` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7020` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7021` | `mcq` | false | `B` | `A. Bottom to top` |
| baseline | `mmlu_7022` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7023` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7024` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7025` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7026` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7027` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7028` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7029` | `mcq` | true | `A` | `A. Long-term` |
| baseline | `mmlu_7030` | `mcq` | false | `B` | `C. Formal` |
| baseline | `mmlu_7031` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7032` | `mcq` | true | `B` | `B. Events` |
| baseline | `mmlu_7033` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7034` | `mcq` | false | `D` | `C. Job characteristics model` |
| baseline | `mmlu_7035` | `mcq` | true | `C` | `C. Adam Smith` |
| baseline | `mmlu_7036` | `mcq` | true | `D` | `D. Productivity` |
| baseline | `mmlu_7037` | `mcq` | false | `C` | `D. planning, organising, controlling, leading` |
| baseline | `mmlu_7038` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7039` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7040` | `mcq` | false | `D` | `A` |
| baseline | `mmlu_7041` | `mcq` | true | `C` | `C. Worker empowerment` |
| baseline | `mmlu_7042` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7043` | `mcq` | true | `D` | `D. Strategic business unit` |
| baseline | `mmlu_7044` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7045` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7046` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7047` | `mcq` | true | `D` | `D. Running a business to create social benefits` |
| baseline | `mmlu_7048` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7049` | `mcq` | true | `D` | `D. Company` |
| baseline | `mmlu_7050` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7051` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7052` | `mcq` | false | `C` | `D. After the end of the Second World War.` |
| baseline | `mmlu_7053` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7054` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7055` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7056` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7057` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7058` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7059` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7060` | `mcq` | true | `C` | `C. By grouping together customers with similar needs, it provides a commercially viable method of serving these customer` |
| baseline | `mmlu_7061` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7062` | `mcq` | true | `A` | `A. Winner's curse.` |
| baseline | `mmlu_7063` | `mcq` | true | `B` | `B. Price elasticity.` |
| baseline | `mmlu_7064` | `mcq` | true | `C` | `C. Market exchanges.` |
| baseline | `mmlu_7065` | `mcq` | true | `C` | `C. Permission-based email marketing.` |
| baseline | `mmlu_7066` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7067` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7068` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7069` | `mcq` | true | `B` | `B. Weak theory.` |
| baseline | `mmlu_7070` | `mcq` | true | `C` | `C. Portfolio analysis.` |
| baseline | `mmlu_7071` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7072` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7073` | `mcq` | true | `B` | `B. Public relations.` |
| baseline | `mmlu_7074` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7075` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7076` | `mcq` | false | `A` | `C. Adoption process.` |
| baseline | `mmlu_7077` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7078` | `mcq` | true | `B` | `B. Early adopter.` |
| baseline | `mmlu_7079` | `mcq` | true | `A` | `A. Direct.` |
| baseline | `mmlu_7080` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7081` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7082` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7083` | `mcq` | true | `D` | `D. Brand imagery.` |
| baseline | `mmlu_7084` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7085` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7086` | `mcq` | true | `B` | `B. Research proposal.` |
| baseline | `mmlu_7087` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7088` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7089` | `mcq` | true | `B` | `B. cold canvassing` |
| baseline | `mmlu_7090` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7091` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7092` | `mcq` | true | `B` | `B. Demographics.` |
| baseline | `mmlu_7093` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7094` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7095` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7096` | `mcq` | true | `C` | `C. Relationship marketing.` |
| baseline | `mmlu_7097` | `mcq` | true | `C` | `C. Value.` |
| baseline | `mmlu_7098` | `mcq` | true | `A` | `A. Dialogue.` |
| baseline | `mmlu_7099` | `mcq` | true | `B` | `B. Learning.` |
| baseline | `mmlu_7100` | `mcq` | true | `A` | `A. Price skimming` |
| baseline | `mmlu_7101` | `mcq` | true | `B` | `B. Convenience stores.` |
| baseline | `mmlu_7102` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7103` | `mcq` | true | `D` | `D. Brand personalities.` |
| baseline | `mmlu_7104` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7105` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7106` | `mcq` | true | `B` | `B. Field marketing.` |
| baseline | `mmlu_7107` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7108` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7109` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7110` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7111` | `mcq` | true | `A` | `A. Test markets.` |
| baseline | `mmlu_7112` | `mcq` | true | `A` | `A. Low-contact service.` |
| baseline | `mmlu_7113` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7114` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7115` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7116` | `mcq` | true | `A` | `A. Stratified sample.` |
| baseline | `mmlu_7117` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7118` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7119` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7120` | `mcq` | true | `A` | `A. Test marketing.` |
| baseline | `mmlu_7121` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7122` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7123` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7124` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7125` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7126` | `mcq` | true | `C` | `C. Spam.` |
| baseline | `mmlu_7127` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7128` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7129` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7130` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7131` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7132` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7133` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7134` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7135` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7136` | `mcq` | true | `C` | `C. Price minimizer' purchasing.` |
| baseline | `mmlu_7137` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7138` | `mcq` | true | `D` | `D. Trademark` |
| baseline | `mmlu_7139` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7140` | `mcq` | true | `A` | `A. Internet marketing.` |
| baseline | `mmlu_7141` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7142` | `mcq` | true | `A` | `A. Purchase context.` |
| baseline | `mmlu_7143` | `mcq` | true | `A` | `A. Lead generation.` |
| baseline | `mmlu_7144` | `mcq` | true | `D` | `D. Public relations` |
| baseline | `mmlu_7145` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7146` | `mcq` | false | `B` | `D. Competitor orientation.` |
| baseline | `mmlu_7147` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7148` | `mcq` | true | `B` | `B. Legal environment.` |
| baseline | `mmlu_7149` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7150` | `mcq` | true | `D` | `D. Pay per click (PPC).` |
| baseline | `mmlu_7151` | `mcq` | true | `A` | `A. Distribution.` |
| baseline | `mmlu_7152` | `mcq` | true | `C` | `C. Perceptual maps.` |
| baseline | `mmlu_7153` | `mcq` | true | `C` | `C. $6,860` |
| baseline | `mmlu_7154` | `mcq` | false | `D` | `B. Price assurance.` |
| baseline | `mmlu_7155` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7156` | `mcq` | true | `B` | `B. Decoding.` |
| baseline | `mmlu_7157` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7158` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7159` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7160` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7161` | `mcq` | true | `B` | `B. Product lifecycle.` |
| baseline | `mmlu_7162` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7163` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7164` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7165` | `mcq` | false | `B` | `A. Luxury product.` |
| baseline | `mmlu_7166` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7167` | `mcq` | true | `A` | `A. Exhibitions.` |
| baseline | `mmlu_7168` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7169` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7170` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7171` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7172` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7173` | `mcq` | false | `A` | `D. Customer Service (CS).` |
| baseline | `mmlu_7174` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7175` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7176` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7177` | `mcq` | true | `C` | `C. Category-killer stores.` |
| baseline | `mmlu_7178` | `mcq` | true | `A` | `A. Two-step.` |
| baseline | `mmlu_7179` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7180` | `mcq` | true | `B` | `B. The political, economic, social, technological, legal, and ecological environments.` |
| baseline | `mmlu_7181` | `mcq` | true | `B` | `B. The market segment must have measurable purchasing power and size.` |
| baseline | `mmlu_7182` | `mcq` | true | `D` | `D. Promotion.` |
| baseline | `mmlu_7183` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7184` | `mcq` | true | `D` | `D. Threat from government.` |
| baseline | `mmlu_7185` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7186` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7187` | `mcq` | false | `A` | `D` |
| baseline | `mmlu_7188` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7189` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7190` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7191` | `mcq` | true | `B` | `B. empathy` |
| baseline | `mmlu_7192` | `mcq` | true | `A` | `A. Encoding.` |
| baseline | `mmlu_7193` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7194` | `mcq` | false | `D` | `C. Public relations.` |
| baseline | `mmlu_7195` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7196` | `mcq` | true | `D` | `D. Service encounters.` |
| baseline | `mmlu_7197` | `mcq` | true | `B` | `B. Place utility.` |
| baseline | `mmlu_7198` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7199` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7200` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7201` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7202` | `mcq` | true | `A` | `A. Self-actualization.` |
| baseline | `mmlu_7203` | `mcq` | false | `D` | `C.` |
| baseline | `mmlu_7204` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_7205` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7206` | `mcq` | true | `B` | `B. Information utility.` |
| baseline | `mmlu_7207` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7208` | `mcq` | true | `B` | `B. Social media.` |
| baseline | `mmlu_7209` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7210` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7211` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7212` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7213` | `mcq` | true | `A` | `A. Face validity.` |
| baseline | `mmlu_7214` | `mcq` | true | `C` | `C. Reliability.` |
| baseline | `mmlu_7215` | `mcq` | false | `D` | `C. Supply chain.` |
| baseline | `mmlu_7216` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7217` | `mcq` | true | `A` | `A. Integrated marketing communications (IMC).` |
| baseline | `mmlu_7218` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7219` | `mcq` | true | `C` | `C. Strategic marketing.` |
| baseline | `mmlu_7220` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7221` | `mcq` | true | `C` | `C. Sponsorship.` |
| baseline | `mmlu_7222` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7223` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7224` | `mcq` | true | `A` | `A. Socio-cultural environment.` |
| baseline | `mmlu_7225` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7226` | `mcq` | true | `D` | `D. All of the above.` |
| baseline | `mmlu_7227` | `mcq` | true | `A` | `A. Brand placement.` |
| baseline | `mmlu_7228` | `mcq` | true | `C` | `C. Digital marketing` |
| baseline | `mmlu_7229` | `mcq` | true | `B` | `B. Search engine optimization.` |
| baseline | `mmlu_7230` | `mcq` | true | `C` | `C. Internet advertising.` |
| baseline | `mmlu_7231` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7232` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7233` | `mcq` | false | `A` | `B. Differentiation.` |
| baseline | `mmlu_7234` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7235` | `mcq` | false | `A` | `B.` |
| baseline | `mmlu_7236` | `mcq` | true | `A` | `A. perpetual inventory` |
| baseline | `mmlu_7237` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7238` | `mcq` | true | `B` | `B. Long-term; customers and stakeholders.` |
| baseline | `mmlu_7239` | `mcq` | true | `B` | `B. Intensive distribution.` |
| baseline | `mmlu_7240` | `mcq` | true | `C` | `C. Causal research.` |
| baseline | `mmlu_7241` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7242` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7243` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7244` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7245` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7246` | `mcq` | true | `C` | `C. Relationship pricing.` |
| baseline | `mmlu_7247` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7248` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7249` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7250` | `mcq` | true | `B` | `B. Transfer pricing.` |
| baseline | `mmlu_7251` | `mcq` | true | `C` | `C. Pure price bundling.` |
| baseline | `mmlu_7252` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7253` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7254` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7255` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7256` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7257` | `mcq` | true | `C` | `C. Social media marketing (SMM)` |
| baseline | `mmlu_7258` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7259` | `mcq` | true | `C` | `C. Physiological needs.` |
| baseline | `mmlu_7260` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7261` | `mcq` | true | `B` | `B. Secondary research.` |
| baseline | `mmlu_7262` | `mcq` | true | `B` | `B. Mobile.` |
| baseline | `mmlu_7263` | `mcq` | true | `D` | `D. Perishability.` |
| baseline | `mmlu_7264` | `mcq` | false | `A` | `C` |
| baseline | `mmlu_7265` | `mcq` | true | `D` | `D. Feedback.` |
| baseline | `mmlu_7266` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7267` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7268` | `mcq` | true | `A` | `A. Direct marketing.` |
| baseline | `mmlu_7269` | `mcq` | true | `A` | `A. Reduced perceived risk.` |
| baseline | `mmlu_7270` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7271` | `mcq` | true | `C` | `C. Full-service agency.` |
| baseline | `mmlu_7272` | `mcq` | true | `D` | `D. positioning` |
| baseline | `mmlu_7273` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7274` | `mcq` | false | `A` | `D. Service satisfaction.` |
| baseline | `mmlu_7275` | `mcq` | true | `B` | `B. Primary research.` |
| baseline | `mmlu_7276` | `mcq` | true | `A` | `A. Direct response advertising.` |
| baseline | `mmlu_7277` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7278` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7279` | `mcq` | false | `C` | `A. Channel conflict.` |
| baseline | `mmlu_7280` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7281` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7282` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7283` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7284` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7285` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7286` | `mcq` | true | `A` | `A. 0.01` |
| baseline | `mmlu_7287` | `mcq` | true | `C` | `C. thymine.` |
| baseline | `mmlu_7288` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7289` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7290` | `mcq` | true | `D` | `D. all of these` |
| baseline | `mmlu_7291` | `mcq` | false | `C` | `A` |
| baseline | `mmlu_7292` | `mcq` | true | `D` | `D. Almost 100%` |
| baseline | `mmlu_7293` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7294` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7295` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7296` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7297` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7298` | `mcq` | true | `D` | `D. 45,X` |
| baseline | `mmlu_7299` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7300` | `mcq` | true | `A` | `A. 1.0/64` |
| baseline | `mmlu_7301` | `mcq` | false | `B` | `A. 10,000–15,000` |
| baseline | `mmlu_7302` | `mcq` | true | `C` | `C. Sister` |
| baseline | `mmlu_7303` | `mcq` | true | `D` | `D. APOE` |
| baseline | `mmlu_7304` | `mcq` | false | `D` | `B. 7` |
| baseline | `mmlu_7305` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7306` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7307` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7308` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7309` | `mcq` | false | `A` | `B` |
| baseline | `mmlu_7310` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7311` | `mcq` | false | `C` | `D. Pompe disease` |
| baseline | `mmlu_7312` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7313` | `mcq` | false | `D` | `A. 1 in 4` |
| baseline | `mmlu_7314` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7315` | `mcq` | false | `C` | `B. 0.64` |
| baseline | `mmlu_7316` | `mcq` | false | `D` | `B. HMG-CoA reductase` |
| baseline | `mmlu_7317` | `mcq` | false | `B` | `C. codominance` |
| baseline | `mmlu_7318` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7319` | `mcq` | true | `A` | `A. Recessive inheritance has` |
| baseline | `mmlu_7320` | `mcq` | true | `A` | `A. Huntington disease` |
| baseline | `mmlu_7321` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7322` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7323` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7324` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7325` | `mcq` | false | `C` | `A. 1 in 1000` |
| baseline | `mmlu_7326` | `mcq` | true | `C` | `C. Hexosaminidase A` |
| baseline | `mmlu_7327` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7328` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7329` | `mcq` | false | `A` | `D.` |
| baseline | `mmlu_7330` | `mcq` | true | `C` | `C. Developmental plasticity` |
| baseline | `mmlu_7331` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7332` | `mcq` | false | `C` | `B. 1.0/4` |
| baseline | `mmlu_7333` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7334` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7335` | `mcq` | false | `C` | `A. about 2` |
| baseline | `mmlu_7336` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7337` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7338` | `mcq` | true | `A` | `A. bind regions near a eukaryotic gene and allow an RNA polymerase to transcribe a gene` |
| baseline | `mmlu_7339` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7340` | `mcq` | true | `B` | `B. Prophase I.` |
| baseline | `mmlu_7341` | `mcq` | true | `D` | `D. mitochondrial DNA.` |
| baseline | `mmlu_7342` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7343` | `mcq` | false | `B` | `D. 46 pairs` |
| baseline | `mmlu_7344` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7345` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7346` | `mcq` | false | `C` | `B. 0.32` |
| baseline | `mmlu_7347` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7348` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7349` | `mcq` | true | `A` | `A. solving criminal and paternity cases` |
| baseline | `mmlu_7350` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7351` | `mcq` | false | `B` | `D` |
| baseline | `mmlu_7352` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7353` | `mcq` | true | `D` | `D. 45,Y` |
| baseline | `mmlu_7354` | `mcq` | true | `B` | `B. BRCA2` |
| baseline | `mmlu_7355` | `mcq` | true | `D` | `D. Succinylcholine` |
| baseline | `mmlu_7356` | `mcq` | false | `A` | `C.` |
| baseline | `mmlu_7357` | `mcq` | true | `C` | `C. 46` |
| baseline | `mmlu_7358` | `mcq` | false | `B` | `A/B/C/D` |
| baseline | `mmlu_7359` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7360` | `mcq` | true | `C` | `C. Huntington disease` |
| baseline | `mmlu_7361` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7362` | `mcq` | true | `A` | `A. Intron` |
| baseline | `mmlu_7363` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7364` | `mcq` | false | `B` | `C` |
| baseline | `mmlu_7365` | `mcq` | true | `D` | `D. Zellweger syndrome` |
| baseline | `mmlu_7366` | `mcq` | true | `B` | `B. hereditary non-polyposis colon cancer (HNPCC).` |
| baseline | `mmlu_7367` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7368` | `mcq` | false | `C` | `D.` |
| baseline | `mmlu_7369` | `mcq` | true | `B` | `B. phenotype` |
| baseline | `mmlu_7370` | `mcq` | true | `A` | `A. 47,XXX` |
| baseline | `mmlu_7371` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7372` | `mcq` | true | `D` | `D. chimaerism.` |
| baseline | `mmlu_7373` | `mcq` | true | `C` | `C. 1 in 100 to 1 in 200` |
| baseline | `mmlu_7374` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7375` | `mcq` | false | `B` | `A` |
| baseline | `mmlu_7376` | `mcq` | true | `B` | `B. neutral or deleterious` |
| baseline | `mmlu_7377` | `mcq` | true | `A` | `A. they allow genetic as opposed to environmental influences on variation in a trait to be estimated` |
| baseline | `mmlu_7378` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7379` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7380` | `mcq` | true | `C` | `C` |
| baseline | `mmlu_7381` | `mcq` | false | `D` | `B. less than 1%` |
| baseline | `mmlu_7382` | `mcq` | true | `A` | `A. differences in gene expression which may establish a pattern in the embryo as the cells divide` |
| baseline | `mmlu_7383` | `mcq` | true | `D` | `D` |
| baseline | `mmlu_7384` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7385` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7386` | `mcq` | true | `D` | `D. 451 degrees` |
| baseline | `mmlu_7387` | `mcq` | false | `C` | `D. Grape` |
| baseline | `mmlu_7388` | `mcq` | true | `B` | `B. Meriwether and William` |
| baseline | `mmlu_7389` | `mcq` | true | `C` | `C. Guided reading` |
| baseline | `mmlu_7390` | `mcq` | true | `C` | `C. the chicken pox virus` |
| baseline | `mmlu_7391` | `mcq` | true | `A` | `A. Copper` |
| baseline | `mmlu_7392` | `mcq` | true | `A` | `A. sophomore` |
| baseline | `mmlu_7393` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7394` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7395` | `mcq` | false | `B` | `D. Dwight Eisenhower` |
| baseline | `mmlu_7396` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7397` | `mcq` | true | `B` | `B. New plant varieties being patented` |
| baseline | `mmlu_7398` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7399` | `mcq` | false | `B` | `D. Groundhog Day` |
| baseline | `mmlu_7400` | `mcq` | true | `A` | `A. A grayish, milky fluid` |
| baseline | `mmlu_7401` | `mcq` | false | `A` | `B. rabbit` |
| baseline | `mmlu_7402` | `mcq` | true | `A` | `A. Beater` |
| baseline | `mmlu_7403` | `mcq` | true | `A` | `A. Ireland` |
| baseline | `mmlu_7404` | `mcq` | true | `D` | `D. Evaporation from the ocean surface` |
| baseline | `mmlu_7405` | `mcq` | true | `A` | `A. Cannes` |
| baseline | `mmlu_7406` | `mcq` | false | `C` | `A. Yahtzee` |
| baseline | `mmlu_7407` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7408` | `mcq` | true | `D` | `D. Friday the 13th'` |
| baseline | `mmlu_7409` | `mcq` | false | `C` | `A. Miss Jackie` |
| baseline | `mmlu_7410` | `mcq` | true | `C` | `C. bird` |
| baseline | `mmlu_7411` | `mcq` | true | `C` | `C. Stomach` |
| baseline | `mmlu_7412` | `mcq` | false | `D` | `C. Red` |
| baseline | `mmlu_7413` | `mcq` | true | `A` | `A. 0 degrees or below` |
| baseline | `mmlu_7414` | `mcq` | false | `D` | `A. cat` |
| baseline | `mmlu_7415` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7416` | `mcq` | false | `C` | `A.` |
| baseline | `mmlu_7417` | `mcq` | true | `D` | `D. 6 mol` |
| baseline | `mmlu_7418` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7419` | `mcq` | true | `C` | `C. to make holes` |
| baseline | `mmlu_7420` | `mcq` | true | `C` | `C. Carpals` |
| baseline | `mmlu_7421` | `mcq` | true | `D` | `D. calf` |
| baseline | `mmlu_7422` | `mcq` | true | `B` | `B. Fendi` |
| baseline | `mmlu_7423` | `mcq` | true | `B` | `B. increasing on-task behavior in the classroom` |
| baseline | `mmlu_7424` | `mcq` | true | `C` | `C. Spain` |
| baseline | `mmlu_7425` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7426` | `mcq` | false | `B` | `C. Emptying the gas tank` |
| baseline | `mmlu_7427` | `mcq` | true | `C` | `C. Thrust` |
| baseline | `mmlu_7428` | `mcq` | true | `D` | `D. Jupiter` |
| baseline | `mmlu_7429` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7430` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7431` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7432` | `mcq` | true | `C` | `C. 10,000 liters` |
| baseline | `mmlu_7433` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7434` | `mcq` | true | `B` | `B. work without pay` |
| baseline | `mmlu_7435` | `mcq` | true | `A` | `A. blue whale` |
| baseline | `mmlu_7436` | `mcq` | true | `C` | `C. Sanskrit` |
| baseline | `mmlu_7437` | `mcq` | true | `C` | `C. right` |
| baseline | `mmlu_7438` | `mcq` | false | `B` | `A. quick exposure time` |
| baseline | `mmlu_7439` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7440` | `mcq` | false | `C` | `B.` |
| baseline | `mmlu_7441` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7442` | `mcq` | true | `B` | `B. flat bread` |
| baseline | `mmlu_7443` | `mcq` | false | `B` | `A. St Augustine Florida` |
| baseline | `mmlu_7444` | `mcq` | true | `B` | `B` |
| baseline | `mmlu_7445` | `mcq` | false | `C` | `D. Law` |
| baseline | `mmlu_7446` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7447` | `mcq` | true | `D` | `D. Foreshortening` |
| baseline | `mmlu_7448` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7449` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7450` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7451` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7452` | `mcq` | true | `A` | `A` |
| baseline | `mmlu_7453` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7454` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7455` | `mcq` | true | `C` | `C. 10` |
| baseline | `mmlu_7456` | `mcq` | true | `B` | `B. Triangle` |
| baseline | `mmlu_7457` | `mcq` | true | `B` | `B. knife` |
| baseline | `mmlu_7458` | `mcq` | true | `C` | `C. stroll` |
| baseline | `mmlu_7459` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7460` | `mcq` | true | `B` | `B. gamma` |
| baseline | `mmlu_7461` | `mcq` | false | `C` | `D` |
| baseline | `mmlu_7462` | `mcq` | false | `C` | `B` |
| baseline | `mmlu_7463` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7464` | `mcq` | false | `C` | `A. France` |
| baseline | `mmlu_7465` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7466` | `mcq` | true | `C` | `C. orange` |
| baseline | `mmlu_7467` | `mcq` | false | `D` | `B.` |
| baseline | `mmlu_7468` | `mcq` | true | `C` | `C. Impasto` |
| baseline | `mmlu_7469` | `mcq` | false | `B` | `C.` |
| baseline | `mmlu_7470` | `mcq` | true | `C` | `C. Japan` |
| baseline | `mmlu_7471` | `mcq` | true | `D` | `D. rice` |
| baseline | `mmlu_7472` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7473` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7474` | `mcq` | false | `B` | `A. Increased varieties of each crop planted` |
| baseline | `mmlu_7475` | `mcq` | true | `D` | `D. Sherwood Forest` |
| baseline | `mmlu_7476` | `mcq` | true | `B` | `B. four` |
| baseline | `mmlu_7477` | `mcq` | true | `D` | `D. Guatemala` |
| baseline | `mmlu_7478` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7479` | `mcq` | true | `D` | `D. Kouroi` |
| baseline | `mmlu_7480` | `mcq` | false | `B` | `D.` |
| baseline | `mmlu_7481` | `mcq` | true | `C` | `C. from many one` |
| baseline | `mmlu_7482` | `mcq` | true | `B` | `B. 21-Mar` |
| baseline | `mmlu_7483` | `mcq` | false | `D` | `A.` |
| baseline | `mmlu_7484` | `mcq` | true | `D` | `D. Jaguar` |
| baseline | `mmlu_7485` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7486` | `mcq` | false | `B` | `A.` |
| baseline | `mmlu_7487` | `mcq` | true | `B` | `B.` |
| baseline | `mmlu_7488` | `mcq` | true | `C` | `C. pro wrestling` |
| baseline | `mmlu_7489` | `mcq` | true | `A` | `A.` |
| baseline | `mmlu_7490` | `mcq` | true | `A` | `A. 4` |
| baseline | `mmlu_7491` | `mcq` | true | `C` | `C. I and II only` |
| baseline | `mmlu_7492` | `mcq` | true | `B` | `B. Martin Luther` |
| baseline | `mmlu_7493` | `mcq` | true | `D` | `D. mercury` |
| baseline | `mmlu_7494` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7495` | `mcq` | false | `A` | `B. underproduce the good relative to the socially optimal level of output` |
| baseline | `mmlu_7496` | `mcq` | true | `C` | `C.` |
| baseline | `mmlu_7497` | `mcq` | true | `A` | `A. Wendy's` |
| baseline | `mmlu_7498` | `mcq` | true | `D` | `D.` |
| baseline | `mmlu_7499` | `mcq` | true | `A` | `A.` |
