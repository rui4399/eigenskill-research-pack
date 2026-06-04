# Quant Result Summary

Dataset: `olmo2-c4-64`

Target: `cpp_loss_sensitive_budget`

- Target PPL: `35.8428`
- Target improvement vs uniform INT4: `0.9906` PPL
- Best random PPL: `35.8512` (`cpp_random_budget`)
- Target margin vs best random: `0.0084` PPL
- Random PPL min/mean/max: `35.8512 / 36.0334 / 36.3837`

| rank | name | PPL | delta NLL vs FP16 |
|---:|---|---:|---:|
| 1 | `fp16` | 32.2736 | 0.0000 |
| 2 | `cpp_loss_sensitive_budget` | 35.8428 | 0.1049 |
| 3 | `cpp_random_budget` | 35.8512 | 0.1051 |
| 4 | `random_seed_20260609` | 35.8660 | 0.1055 |
| 5 | `blend_sensitivity_85` | 35.8817 | 0.1060 |
| 6 | `random_seed_20260610` | 35.8882 | 0.1062 |
| 7 | `random_seed_20260611` | 35.9422 | 0.1077 |
| 8 | `random_seed_20260607` | 36.0363 | 0.1103 |
| 9 | `random_seed_20260612` | 36.0433 | 0.1105 |
| 10 | `cpp_category_budget` | 36.0493 | 0.1106 |
| 11 | `random_seed_20260608` | 36.2566 | 0.1164 |
| 12 | `random_seed_20260606` | 36.3837 | 0.1199 |
| 13 | `uniform_int4` | 36.8334 | 0.1322 |
