# Quant Evidence Matrix

Target: `cpp_loss_sensitive_budget`

| dataset | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| Qwen3-0.6B-WikiText2-64 | 31.1808 | 49.7895 | 39.0053 | 42.1917 | 41.9059 / 44.0596 / 46.3992 | 10.7842 | 2.9006 | 5.0543 |
| Qwen3-0.6B-C4-64 | 36.1380 | 52.9352 | 45.0623 | 47.7182 | 47.1666 / 48.5346 / 50.0268 | 7.8729 | 2.1043 | 3.4723 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
