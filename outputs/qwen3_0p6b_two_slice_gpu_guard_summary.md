# GPU Guard Summary

Max allowed memory ratio: `85.00%`

| label | returncode | killed | max memory | max ratio | max util | status |
|---|---:|---:|---:|---:|---:|---|
| qwen3_sensitivity | 0 | false | 3310 / 8151 MiB | 40.61% | 59% | pass |
| qwen3_wikitext2_64_len96 | 0 | false | 4236 / 8151 MiB | 51.97% | 36% | pass |
| qwen3_c4_eval | 0 | false | 3177 / 8151 MiB | 38.98% | 56% | pass |
| qwen3_wikitext2_64_len128_guard_fail | -15 | true | 6933 / 8151 MiB | 85.06% | 100% | fail |
