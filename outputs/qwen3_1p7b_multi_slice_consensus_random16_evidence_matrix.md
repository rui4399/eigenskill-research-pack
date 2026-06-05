# Quant Evidence Matrix

Target: `wikitext_c4_consensus`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| wikitext2_64 | `wikitext_c4_consensus` | 21.6552 | 31.1885 | 26.3260 | 27.4838 | 27.6685 / 28.2905 / 29.9682 | 4.8626 | 1.3425 | 1.9646 |
| c4_64 | `wikitext_c4_consensus` | 25.5510 | 30.7410 | 28.3303 | 29.2760 | 28.4562 / 29.4357 / 30.0408 | 2.4107 | 0.1259 | 1.1053 |
| wikitext2_128 | `wikitext_c4_consensus` | 20.2931 | 28.2125 | 24.2065 | 25.3040 | 25.1876 / 26.0827 / 28.1645 | 4.0060 | 0.9811 | 1.8762 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
