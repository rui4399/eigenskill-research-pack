# Quant Evidence Matrix

Target: `wikitext_c4_consensus`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| c4_128 | `wikitext_c4_consensus` | 29.4065 | 35.7923 | 32.8806 | 34.1947 | 33.2734 / 34.5656 / 35.1416 | 2.9117 | 0.3928 | 1.6849 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
