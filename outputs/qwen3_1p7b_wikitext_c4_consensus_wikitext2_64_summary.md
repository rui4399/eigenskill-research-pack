# Quant Result Summary

Dataset: `Qwen3-1.7B-WikiText2-64`

Target: `wikitext_c4_consensus`

- Target PPL: `26.3260`
- Target improvement vs uniform INT4: `4.8626` PPL
- Best random PPL: `27.6685` (`random_budget_seed_20260619`)
- Target margin vs best random: `1.3425` PPL
- Random PPL min/mean/max: `27.6685 / 27.9124 / 28.1563`

| rank | name | PPL | delta NLL vs FP16 |
|---:|---|---:|---:|
| 1 | `fp16` | 21.6552 | 0.0000 |
| 2 | `wikitext_c4_consensus` | 26.3260 | 0.1953 |
| 3 | `c4_loss_sensitive` | 26.6878 | 0.2090 |
| 4 | `cpp_category_budget` | 27.4838 | 0.2384 |
| 5 | `wikitext_loss_sensitive` | 27.6578 | 0.2447 |
| 6 | `random_budget_seed_20260619` | 27.6685 | 0.2450 |
| 7 | `random_budget_seed_20260612` | 28.1563 | 0.2625 |
| 8 | `uniform_int4` | 31.1885 | 0.3648 |
