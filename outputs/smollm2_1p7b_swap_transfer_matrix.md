# Quant Transfer Matrix

Base: `loss_sensitive_full`  Target: `swap_search_wikitext2_64`

| dataset | FP16 | uniform INT4 | base PPL | target PPL | improvement | guard |
|---|---:|---:|---:|---:|---:|---|
| wikitext2_128 | 13.2171 | 18.7966 | 15.3641 | 15.3127 | 0.0514 | pass (73.67%) |
| c4_64 | 18.4497 | 26.3475 | 21.4269 | 21.4356 | -0.0087 | pass (72.40%) |

Positive improvement means the target allocation lowers PPL relative to the base allocation on that dataset.
