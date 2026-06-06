# Selected-Row Benchmark Gate

Status: **PASS**

## Summary

- model: `Qwen/Qwen3-0.6B`
- modules: 3
- batches: `[1, 12, 64]`
- selected rows: `[16, 64, 256]`
- ok rows: 108
- failed rows: 0
- guard peak memory: 3561 / 8151 MiB (0.4369)

## Runtime Summaries

| runtime | cases | wins vs full | median speedup vs full | best speedup vs full | max rel-L2 |
|---|---:|---:|---:|---:|---:|
| `triton_selected` | 27 | 4 | 0.4235 | 2.2406 | 0.1958 |
| `cached_selected` | 27 | 18 | 1.2565 | 7.3587 | 0.1958 |
| `dense_selected` | 27 | 17 | 1.1558 | 5.9976 | 0.0000 |

## Failures

- none

## Claim Boundary

- Valid claim: selected-row routing has gated module-level evidence under the configured thresholds.
- Invalid claim: this alone proves end-to-end token latency acceleration.
