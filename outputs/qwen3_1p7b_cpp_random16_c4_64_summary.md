# Quant Result Summary

Dataset: `Qwen3-1.7B-C4-64`

Target: `cpp_loss_sensitive_budget`

- Target PPL: `29.2030`
- Target improvement vs uniform INT4: `1.5380` PPL
- Best random PPL: `28.4562` (`random_budget_seed_20260612`)
- Target margin vs best random: `-0.7467` PPL
- Random PPL min/mean/max: `28.4562 / 29.4357 / 30.0408`

| rank | name | PPL | delta NLL vs FP16 |
|---:|---|---:|---:|
| 1 | `fp16` | 25.5510 | 0.0000 |
| 2 | `random_budget_seed_20260612` | 28.4562 | 0.1077 |
| 3 | `random_budget_seed_20260606` | 28.5016 | 0.1093 |
| 4 | `random_budget_seed_20260619` | 28.9674 | 0.1255 |
| 5 | `random_budget_seed_20260610` | 29.0335 | 0.1278 |
| 6 | `random_budget_seed_20260608` | 29.1366 | 0.1313 |
| 7 | `cpp_loss_sensitive_budget` | 29.2030 | 0.1336 |
| 8 | `cpp_category_budget` | 29.2760 | 0.1361 |
| 9 | `random_budget_seed_20260618` | 29.3247 | 0.1378 |
| 10 | `random_budget_seed_20260617` | 29.4638 | 0.1425 |
| 11 | `random_budget_seed_20260611` | 29.5736 | 0.1462 |
| 12 | `random_budget_seed_20260609` | 29.6139 | 0.1476 |
| 13 | `random_budget_seed_20260615` | 29.6204 | 0.1478 |
| 14 | `random_budget_seed_20260613` | 29.7818 | 0.1532 |
| 15 | `random_budget_seed_20260604` | 29.8302 | 0.1548 |
| 16 | `random_budget_seed_20260614` | 29.8601 | 0.1558 |
| 17 | `random_budget_seed_20260605` | 29.8723 | 0.1563 |
| 18 | `random_budget_seed_20260607` | 29.8935 | 0.1570 |
| 19 | `random_budget_seed_20260616` | 30.0408 | 0.1619 |
| 20 | `uniform_int4` | 30.7410 | 0.1849 |
