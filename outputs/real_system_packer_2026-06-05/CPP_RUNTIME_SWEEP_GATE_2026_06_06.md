# C++ ESMP Runtime Sweep Gate

Status: **PASS**

## Summary

- total rows: 42
- ok rows: 42
- failed rows: 0
- wins vs full mixed GEMV: 42
- min selected/full speedup: 12.7607
- median selected/full speedup: 16.8259
- best selected/full speedup: 56.4888
- median selected ms: 0.205620
- median compression vs FP32: 7.6413x

## By Family

| family | count | median speedup | min speedup | median selected ms | median compression |
|---|---:|---:|---:|---:|---:|
| `attention` | 24 | 16.3918 | 14.9803 | 0.205620 | 7.6409x |
| `mlp` | 18 | 46.3437 | 12.7607 | 0.207805 | 7.6415x |

## By Layer Bucket

| bucket | count | median speedup | min speedup | median selected ms | median compression |
|---|---:|---:|---:|---:|---:|
| `early` | 14 | 17.5250 | 12.7607 | 0.269351 | 7.6411x |
| `late` | 14 | 16.8259 | 14.9272 | 0.254317 | 7.6414x |
| `middle` | 14 | 17.0703 | 15.5079 | 0.188833 | 7.6415x |

## Failures

- none

## Claim Boundary

- Valid claim: the C++ ESMP runtime has gated module-level selected-row speedup evidence.
- Invalid claim: this alone proves full LLM end-to-end acceleration.
