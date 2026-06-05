# Quant Evidence Matrix

Target: `auto`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| qwen3_0p6b_wikitext2_64 | `cpp_loss_sensitive_budget` | 31.1808 | 49.7895 | 39.0053 | 42.1917 | 41.9059 / 44.0596 / 46.3992 | 10.7842 | 2.9006 | 5.0543 |
| qwen3_0p6b_c4_64 | `cpp_loss_sensitive_budget` | 36.1380 | 52.9352 | 45.0623 | 47.7182 | 47.1666 / 48.5346 / 50.0268 | 7.8729 | 2.1043 | 3.4723 |
| qwen3_1p7b_wikitext2_64 | `wikitext_c4_consensus` | 21.6552 | 31.1885 | 26.3260 | 27.4838 | 27.6685 / 28.2905 / 29.9682 | 4.8626 | 1.3425 | 1.9646 |
| qwen3_1p7b_c4_64 | `wikitext_c4_consensus` | 25.5510 | 30.7410 | 28.3303 | 29.2760 | 28.4562 / 29.4357 / 30.0408 | 2.4107 | 0.1259 | 1.1053 |
| olmo2_0425_1b_wikitext2_64_random16 | `cpp_loss_sensitive_budget` | 18.8573 | 22.4888 | 21.1191 | 21.6281 | 21.4637 / 21.6765 / 22.1512 | 1.3696 | 0.3445 | 0.5573 |
| olmo2_0425_1b_c4_64_random16 | `cpp_loss_sensitive_budget` | 32.2736 | 36.8334 | 35.8428 | 36.0493 | 35.5846 / 36.0382 / 36.5191 | 0.9906 | -0.2582 | 0.1954 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
