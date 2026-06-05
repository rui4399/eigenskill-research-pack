# Quant Evidence Matrix

Target: `loss_sensitive_full`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| c4_64_full | `loss_sensitive_full` | 18.4497 | 26.3475 | 21.4269 | NA | 22.5529 / 26.1102 / 29.7791 | 4.9206 | 1.1260 | 4.6833 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
