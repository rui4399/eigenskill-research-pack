# Quant Evidence Matrix

Target: `wikitext_c4_consensus`

| dataset | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| Qwen3-1.7B-WikiText2-64 | 21.6552 | 31.1885 | 26.3260 | 27.4838 | 27.6685 / 27.9124 / 28.1563 | 4.8626 | 1.3425 | 1.5865 |
| Qwen3-1.7B-C4-64 | 25.5510 | 30.7410 | 28.3303 | 29.2760 | 28.4562 / 28.7118 / 28.9674 | 2.4107 | 0.1259 | 0.3815 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
