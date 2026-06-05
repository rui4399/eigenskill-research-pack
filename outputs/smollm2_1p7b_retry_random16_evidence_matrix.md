# Quant Evidence Matrix

Target: `loss_sensitive_limit8`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| wikitext2_16 | `loss_sensitive_limit8` | 12.6903 | 18.1431 | 12.8844 | NA | 12.8503 / 12.9795 / 13.0977 | 5.2587 | -0.0341 | 0.0951 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
