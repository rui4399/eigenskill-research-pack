# Quant Evidence Matrix

Target: `wikitext_c4_consensus`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| wikitext2_64_len96 | `wikitext_c4_consensus` | 33.9865 | 54.6542 | 45.6559 | 50.4746 | 48.5030 / 50.4985 / 52.6347 | 8.9983 | 2.8471 | 4.8426 |
| c4_64 | `wikitext_c4_consensus` | 36.1380 | 52.9352 | 44.9290 | 48.6222 | 48.3840 / 49.4629 / 50.7971 | 8.0062 | 3.4551 | 4.5339 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
