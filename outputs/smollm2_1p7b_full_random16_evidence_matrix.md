# Quant Evidence Matrix

Target: `loss_sensitive_full`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| wikitext2_16_full | `loss_sensitive_full` | 12.6903 | 18.1431 | 13.9866 | NA | 14.7340 / 17.5858 / 19.9983 | 4.1565 | 0.7474 | 3.5992 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
