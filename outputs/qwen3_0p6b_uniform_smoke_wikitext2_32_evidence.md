# Quant Evidence Matrix

Target: `uniform_int4`

| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | target vs uniform | target vs best random | target vs random mean |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| qwen3_0p6b_wikitext2_32 | `uniform_int4` | 31.6892 | 49.9061 | 49.9061 | NA | NA / NA / NA | 0.0000 | NA | NA |

Positive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.
