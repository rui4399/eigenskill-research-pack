# Quant Evidence Matrix

Target: `auto`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| qwen3_0p6b_wikitext2_64 | `cpp_loss_sensitive_budget` | 31.1808 | 49.7895 | 39.0053 | 42.1917 | 41.9059 / 44.0596 / 46.3992 | 10.7842 | 2.9006 | 5.0543 |
| qwen3_0p6b_c4_64 | `cpp_loss_sensitive_budget` | 36.1380 | 52.9352 | 45.0623 | 47.7182 | 47.1666 / 48.5346 / 50.0268 | 7.8729 | 2.1043 | 3.4723 |
| qwen3_1p7b_wikitext2_64 | `wikitext_c4_consensus` | 21.6552 | 31.1885 | 26.3260 | 27.4838 | 27.6685 / 28.2905 / 29.9682 | 4.8626 | 1.3425 | 1.9646 |
| qwen3_1p7b_wikitext2_128 | `wikitext_c4_consensus` | 20.2931 | 28.2125 | 24.2065 | 25.3040 | 25.1876 / 26.0827 / 28.1645 | 4.0060 | 0.9811 | 1.8762 |
| qwen3_1p7b_c4_64 | `wikitext_c4_consensus` | 25.5510 | 30.7410 | 28.3303 | 29.2760 | 28.4562 / 29.4357 / 30.0408 | 2.4107 | 0.1259 | 1.1053 |
| olmo2_0425_1b_wikitext2_64_consensus | `wikitext_c4_consensus` | 18.8573 | 22.4888 | 21.0349 | NA | 21.4637 / 21.6765 / 22.1512 | 1.4539 | 0.4288 | 0.6416 |
| olmo2_0425_1b_c4_64_consensus | `wikitext_c4_consensus` | 32.2736 | 36.8334 | 35.4726 | NA | 35.5846 / 36.0382 / 36.5191 | 1.3608 | 0.1120 | 0.5656 |
| smollm2_1p7b_wikitext2_16_full | `loss_sensitive_full` | 12.6903 | 18.1431 | 13.9866 | NA | 14.7340 / 17.5858 / 19.9983 | 4.1565 | 0.7474 | 3.5992 |
| smollm2_1p7b_wikitext2_64_full | `loss_sensitive_full` | 12.6568 | 18.5164 | 14.8877 | NA | 15.6654 / 18.1114 / 20.5267 | 3.6286 | 0.7777 | 3.2236 |
| smollm2_1p7b_wikitext2_128_full | `loss_sensitive_full` | 13.2171 | 18.7966 | 15.3641 | NA | 16.2050 / 18.5168 / 21.2702 | 3.4325 | 0.8409 | 3.1527 |
| smollm2_1p7b_c4_64_full | `loss_sensitive_full` | 18.4497 | 26.3475 | 21.4269 | NA | 22.5529 / 26.1102 / 29.7791 | 4.9206 | 1.1260 | 4.6833 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
