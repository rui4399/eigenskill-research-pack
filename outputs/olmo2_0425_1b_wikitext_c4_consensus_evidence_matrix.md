# Quant Evidence Matrix

Target: `wikitext_c4_consensus`

| dataset | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| OLMo2-0425-1B-WikiText2-64 | 18.8573 | 22.4888 | 21.0349 | 21.6281 | 21.4637 / 21.6140 / 21.7550 | 1.4539 | 0.4288 | 0.5791 |
| OLMo2-0425-1B-C4-64 | 32.2736 | 36.8334 | 35.4726 | 36.0493 | 35.8512 / 36.0334 / 36.3837 | 1.3608 | 0.3785 | 0.5608 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
