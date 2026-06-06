# Calibration Robustness Stress Gate

Date: `2026-06-06T17:00:37+00:00`
Status: **PASS**

## Summary

- cases: `11`
- target wins vs uniform: `11`
- target wins vs best random: `11`
- target wins vs random mean: `11`
- mean margin vs uniform: `4.2942`
- worst margin vs uniform: `1.3608`
- mean margin vs best random: `1.1622`
- worst margin vs best random: `0.1120`
- mean FP16 regret: `4.1683`

## Cases

| case | target | FP16 | uniform | target | best random | random mean | margin vs uniform | margin vs best random | FP16 regret |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `qwen3_0p6b_wikitext2_64` | `wikitext_c4_consensus` | 33.9865 | 54.6542 | 45.6559 | 48.5030 | 50.4985 | 8.9983 | 2.8471 | 11.6693 |
| `qwen3_0p6b_c4_64` | `wikitext_c4_consensus` | 36.1380 | 52.9352 | 44.9290 | 48.3840 | 49.4629 | 8.0062 | 3.4551 | 8.7910 |
| `qwen3_1p7b_wikitext2_64` | `wikitext_c4_consensus` | 21.6552 | 31.1885 | 26.3260 | 27.6685 | 28.2905 | 4.8626 | 1.3425 | 4.6707 |
| `qwen3_1p7b_wikitext2_128` | `wikitext_c4_consensus` | 20.2931 | 28.2125 | 24.2065 | 25.1876 | 26.0827 | 4.0060 | 0.9811 | 3.9134 |
| `qwen3_1p7b_c4_64` | `wikitext_c4_consensus` | 25.5510 | 30.7410 | 28.3303 | 28.4562 | 29.4357 | 2.4107 | 0.1259 | 2.7794 |
| `olmo2_1b_wikitext2_64` | `wikitext_c4_consensus` | 18.8573 | 22.4888 | 21.0349 | 21.4637 | 21.6765 | 1.4539 | 0.4288 | 2.1776 |
| `olmo2_1b_c4_64` | `wikitext_c4_consensus` | 32.2736 | 36.8334 | 35.4726 | 35.5846 | 36.0382 | 1.3608 | 0.1120 | 3.1990 |
| `smollm2_1p7b_wikitext2_16` | `loss_sensitive_full` | 12.6903 | 18.1431 | 13.9866 | 14.7340 | 17.5858 | 4.1565 | 0.7474 | 1.2963 |
| `smollm2_1p7b_wikitext2_64` | `loss_sensitive_full` | 12.6568 | 18.5164 | 14.8877 | 15.6654 | 18.1114 | 3.6286 | 0.7777 | 2.2309 |
| `smollm2_1p7b_wikitext2_128` | `loss_sensitive_full` | 13.2171 | 18.7966 | 15.3641 | 16.2050 | 18.5168 | 3.4325 | 0.8409 | 2.1469 |
| `smollm2_1p7b_c4_64` | `loss_sensitive_full` | 18.4497 | 26.3475 | 21.4269 | 22.5529 | 26.1102 | 4.9206 | 1.1260 | 2.9772 |

## Interpretation

Positive margins mean the target policy has lower PPL than the comparator. This is a robustness stress gate over committed fake-quant summaries, not a production quantizer or SOTA claim.

## Failures

- none
