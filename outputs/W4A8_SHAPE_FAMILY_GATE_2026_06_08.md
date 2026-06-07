# W4A8 Shape-Family Gate

Status: **PASS**

## Source

- JSONL: `outputs/rtx5070_int8_tensorcore_probe_2026_06_07/shape_family_4096/tuning_results.jsonl`

## Summary

- valid configs: `8/8`
- all packed W4 x INT8 configs beat FP16: `True`
- all W4-as-I8 x INT8 configs beat FP16: `True`
- all packed W4 x INT8 configs beat packed W4A16: `True`

| metric | min / median / max |
|---|---:|
| packed W4 x INT8 speedup vs torch FP16 | 1.2900 / 1.4490 / 1.7268 |
| W4-as-I8 x INT8 speedup vs torch FP16 | 1.4886 / 2.3873 / 3.1372 |
| packed W4 x INT8 speedup vs packed W4A16 | 1.6382 / 1.9977 / 2.5382 |
| weight payload compression vs FP16 | 3.9825 / 3.9825 / 3.9825 |
| activation added rel-L2 vs W4A16 | 0.0087 / 0.0087 / 0.0087 |
| guard peak memory ratio | 0.6134 / 0.6164 / 0.6219 |

## Thresholds

- min_configs: `8`
- min_packed_speedup: `1.0`
- min_packed_vs_w4a16_speedup: `1.0`
- min_compression: `3.5`
- max_added_rel_l2: `0.02`
- max_memory_ratio: `0.9`

## Failures

- none

## Claim Boundary

Valid claim: the committed RTX 5070 W4A8-style shape-family sweep passes kernel-level speed, compression, drift, and guard-memory thresholds.

Invalid claim: this gate does not prove end-to-end LLM speed, mobile deployment, energy savings, downstream task retention, or SOTA quantization.
