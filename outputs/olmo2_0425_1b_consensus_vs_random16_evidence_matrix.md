# Quant Evidence Matrix

Target: `wikitext_c4_consensus`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| olmo2_consensus_vs_random16_wikitext2_64 | `wikitext_c4_consensus` | 18.8573 | 22.4888 | 21.0349 | NA | 21.4637 / 21.6765 / 22.1512 | 1.4539 | 0.4288 | 0.6416 |
| olmo2_consensus_vs_random16_c4_64 | `wikitext_c4_consensus` | 32.2736 | 36.8334 | 35.4726 | NA | 35.5846 / 36.0382 / 36.5191 | 1.3608 | 0.1120 | 0.5656 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
