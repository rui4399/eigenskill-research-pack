# Quant Evidence Matrix

Target: `cpp_loss_sensitive_budget`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| wikitext2_64_len96 | `cpp_loss_sensitive_budget` | 33.9865 | 54.6542 | 49.5352 | 50.4746 | 48.5030 / 50.4985 / 52.6347 | 5.1189 | -1.0322 | 0.9632 |
| c4_64 | `cpp_loss_sensitive_budget` | 36.1380 | 52.9352 | 47.5872 | 48.6222 | 48.3840 / 49.4629 / 50.7971 | 5.3480 | 0.7969 | 1.8757 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
