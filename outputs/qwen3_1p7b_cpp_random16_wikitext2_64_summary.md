# Quant Result Summary

Dataset: `Qwen3-1.7B-WikiText2-64`

Target: `cpp_loss_sensitive_budget`

- Target PPL: `27.6578`
- Target improvement vs uniform INT4: `3.5307` PPL
- Best random PPL: `27.6685` (`random_budget_seed_20260619`)
- Target margin vs best random: `0.0107` PPL
- Random PPL min/mean/max: `27.6685 / 28.2905 / 29.9682`

| rank | name | PPL | delta NLL vs FP16 |
|---:|---|---:|---:|
| 1 | `fp16` | 21.6552 | 0.0000 |
| 2 | `cpp_category_budget` | 27.4838 | 0.2384 |
| 3 | `cpp_loss_sensitive_budget` | 27.6578 | 0.2447 |
| 4 | `random_budget_seed_20260619` | 27.6685 | 0.2450 |
| 5 | `random_budget_seed_20260606` | 27.6800 | 0.2455 |
| 6 | `random_budget_seed_20260609` | 27.7297 | 0.2473 |
| 7 | `random_budget_seed_20260618` | 27.7688 | 0.2487 |
| 8 | `random_budget_seed_20260611` | 27.8652 | 0.2521 |
| 9 | `random_budget_seed_20260608` | 27.9929 | 0.2567 |
| 10 | `random_budget_seed_20260610` | 28.1279 | 0.2615 |
| 11 | `random_budget_seed_20260614` | 28.1372 | 0.2618 |
| 12 | `random_budget_seed_20260615` | 28.1498 | 0.2623 |
| 13 | `random_budget_seed_20260612` | 28.1563 | 0.2625 |
| 14 | `random_budget_seed_20260617` | 28.2508 | 0.2659 |
| 15 | `random_budget_seed_20260604` | 28.3799 | 0.2704 |
| 16 | `random_budget_seed_20260616` | 28.5793 | 0.2774 |
| 17 | `random_budget_seed_20260613` | 28.8365 | 0.2864 |
| 18 | `random_budget_seed_20260605` | 29.3575 | 0.3043 |
| 19 | `random_budget_seed_20260607` | 29.9682 | 0.3249 |
| 20 | `uniform_int4` | 31.1885 | 0.3648 |
