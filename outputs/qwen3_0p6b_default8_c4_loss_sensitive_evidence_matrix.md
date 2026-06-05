# Quant Evidence Matrix

Target: `allocation_loss_sensitive_4to8`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| default_prompts_8 | `allocation_loss_sensitive_4to8` | 285.9696 | 287.3424 | 225.0283 | NA | NA / NA / NA | 62.3141 | NA | NA |
| c4_64 | `allocation_loss_sensitive_4to8` | 36.1380 | 52.9352 | 47.5872 | NA | NA / NA / NA | 5.3480 | NA | NA |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
