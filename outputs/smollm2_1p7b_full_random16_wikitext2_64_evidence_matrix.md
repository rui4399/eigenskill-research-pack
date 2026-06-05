# Quant Evidence Matrix

Target: `loss_sensitive_full`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| wikitext2_64_full | `loss_sensitive_full` | 12.6568 | 18.5164 | 14.8877 | NA | 15.6654 / 18.1114 / 20.5267 | 3.6286 | 0.7777 | 3.2236 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
