# Quant Evidence Matrix

Target: `loss_sensitive_full`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| wikitext2_128_full | `loss_sensitive_full` | 13.2171 | 18.7966 | 15.3641 | NA | 16.2050 / 18.5168 / 21.2702 | 3.4325 | 0.8409 | 3.1527 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
