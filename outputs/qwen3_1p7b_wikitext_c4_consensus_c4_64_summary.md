# Quant Result Summary

Dataset: `Qwen3-1.7B-C4-64`

Target: `wikitext_c4_consensus`

- Target PPL: `28.3303`
- Target improvement vs uniform INT4: `2.4107` PPL
- Best random PPL: `28.4562` (`random_budget_seed_20260612`)
- Target margin vs best random: `0.1259` PPL
- Random PPL min/mean/max: `28.4562 / 28.7118 / 28.9674`

| rank | name | PPL | delta NLL vs FP16 |
|---:|---|---:|---:|
| 1 | `fp16` | 25.5510 | 0.0000 |
| 2 | `wikitext_c4_consensus` | 28.3303 | 0.1033 |
| 3 | `c4_loss_sensitive` | 28.3505 | 0.1040 |
| 4 | `random_budget_seed_20260612` | 28.4562 | 0.1077 |
| 5 | `random_budget_seed_20260619` | 28.9674 | 0.1255 |
| 6 | `wikitext_loss_sensitive` | 29.2030 | 0.1336 |
| 7 | `cpp_category_budget` | 29.2760 | 0.1361 |
| 8 | `uniform_int4` | 30.7410 | 0.1849 |
