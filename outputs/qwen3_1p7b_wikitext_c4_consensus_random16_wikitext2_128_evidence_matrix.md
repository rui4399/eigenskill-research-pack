# Quant Evidence Matrix

Target: `wikitext_c4_consensus`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| wikitext2_128 | `wikitext_c4_consensus` | 20.2931 | 28.2125 | 24.2065 | 25.3040 | 25.1876 / 26.0827 / 28.1645 | 4.0060 | 0.9811 | 1.8762 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
