# Quant Evidence Matrix

Target: `loss_sensitive_full`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| wikitext2_16_full | `loss_sensitive_full` | 12.6903 | 18.1431 | 13.9866 | NA | 14.7340 / 17.5858 / 19.9983 | 4.1565 | 0.7474 | 3.5992 |
| wikitext2_64_full | `loss_sensitive_full` | 12.6568 | 18.5164 | 14.8877 | NA | 15.6654 / 18.1114 / 20.5267 | 3.6286 | 0.7777 | 3.2236 |
| c4_64_full | `loss_sensitive_full` | 18.4497 | 26.3475 | 21.4269 | NA | 22.5529 / 26.1102 / 29.7791 | 4.9206 | 1.1260 | 4.6833 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
