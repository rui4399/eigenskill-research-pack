# Quant Result Summary

Dataset: `olmo2-wikitext2-64`

Target: `cpp_loss_sensitive_budget`

- Target PPL: `21.1191`
- Target improvement vs uniform INT4: `1.3696` PPL
- Best random PPL: `21.4637` (`random_seed_20260610`)
- Target margin vs best random: `0.3445` PPL
- Random PPL min/mean/max: `21.4637 / 21.6140 / 21.7550`

| rank | name | PPL | delta NLL vs FP16 |
|---:|---|---:|---:|
| 1 | `fp16` | 18.8573 | 0.0000 |
| 2 | `cpp_loss_sensitive_budget` | 21.1191 | 0.1133 |
| 3 | `blend_sensitivity_85` | 21.1331 | 0.1139 |
| 4 | `random_seed_20260610` | 21.4637 | 0.1295 |
| 5 | `random_seed_20260609` | 21.5127 | 0.1317 |
| 6 | `random_seed_20260611` | 21.5701 | 0.1344 |
| 7 | `random_seed_20260612` | 21.5917 | 0.1354 |
| 8 | `cpp_category_budget` | 21.6281 | 0.1371 |
| 9 | `cpp_random_budget` | 21.6367 | 0.1375 |
| 10 | `random_seed_20260607` | 21.6419 | 0.1377 |
| 11 | `random_seed_20260608` | 21.7403 | 0.1423 |
| 12 | `random_seed_20260606` | 21.7550 | 0.1429 |
| 13 | `uniform_int4` | 22.4888 | 0.1761 |
