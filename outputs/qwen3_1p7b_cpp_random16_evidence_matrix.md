# Quant Evidence Matrix

Target: `cpp_loss_sensitive_budget`

| dataset | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| Qwen3-1.7B-WikiText2-64 | 21.6552 | 31.1885 | 27.6578 | 27.4838 | 27.6685 / 28.2905 / 29.9682 | 3.5307 | 0.0107 | 0.6327 |
| Qwen3-1.7B-C4-64 | 25.5510 | 30.7410 | 29.2030 | 29.2760 | 28.4562 / 29.4357 / 30.0408 | 1.5380 | -0.7467 | 0.2327 |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
