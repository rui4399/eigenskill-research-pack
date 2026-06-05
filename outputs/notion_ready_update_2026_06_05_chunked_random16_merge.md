# EigenSkill-Q 2026-06-05 Update: Chunked Random16 Merge Path

## Summary

This update adds the CPU/C++ infrastructure needed to finish the Qwen3-1.7B
C4-128 random16 audit without disturbing an active Steam gaming session or
crossing the 85% GPU-memory guard.

The GPU was not used for new training/evaluation in this step because the
desktop GPU already had several GiB of VRAM occupied by the running game. This
is an operational constraint, not a failed experiment.

## What Changed

- Added `inference_cpp/src/quant_ppl_summary_merge.cpp`.
- Added CMake target `quant_ppl_summary_merge`.
- Added two CTest smoke tests:
  - merge two PPL summary files;
  - feed the merged output into `quant_random_baseline_audit`.
- Added three C4-128 random16 batch configs for seeds 20260608-20260619.
- Added `docs/qwen3_1p7b_c4_128_random16_chunked_runbook.md`.
- Updated `README.md` to document the C4-128 random4 result and the chunked
  random16 path.

## Verified Result So Far

The current completed Qwen3-1.7B C4-128 row is still the guarded random4 run:

| Dataset | FP16 | uniform INT4 | consensus | category | random min/mean/max |
|---|---:|---:|---:|---:|---:|
| C4-128 | 29.4065 | 35.7923 | 32.8806 | 34.1947 | 33.2734 / 34.5656 / 35.1416 |

Margins:

- consensus vs uniform INT4: +2.9117 PPL
- consensus vs category: +1.3141 PPL
- consensus vs best random4: +0.3928 PPL
- consensus vs random4 mean: +1.6849 PPL

GPU guard:

```text
6884 / 8151 MiB = 84.46%
max GPU util = 74%
status = pass
```

## Why The New C++ Merge Tool Matters

The full C4-128 random16 command previously exceeded the 85% guard when run as
one process, peaking around 86.3%. The new merge tool allows this experiment to
be completed as four guarded chunks:

1. existing batch0: FP16, uniform INT4, consensus, category, random seeds
   20260604-20260607;
2. batch1: random seeds 20260608-20260611;
3. batch2: random seeds 20260612-20260615;
4. batch3: random seeds 20260616-20260619.

The merged file is designed to be consumed directly by:

```text
build/cpp-wsl/quant_evidence_matrix
build/cpp-wsl/quant_random_baseline_audit
build/cpp-wsl/gpu_guard_summary
```

## Verification

```text
cmake --build build/cpp-wsl -j2
ctest --test-dir build/cpp-wsl --output-on-failure
```

Result:

```text
16/16 tests passed
```

Additional smoke:

```text
quant_ppl_summary_merge on fixture summaries
quant_random_baseline_audit on merged fixture
quant_ppl_summary_merge self-merge on real Qwen3 C4-128 random4 summary
```

The real random4 self-merge preserved the audit result:

```text
target PPL: 32.880630
seed_count: 4
wins/losses/ties: 4 / 0 / 0
margin_vs_best_seed: +0.392768
```

## GitHub

Latest infrastructure commit before this documentation update:

```text
0bc7243e2d770692f5816111a25022dc7e4add64
```

Repo:

```text
https://github.com/rui4399/eigenskill-research-pack
```

## Next GPU Step

When the GPU is free, run the three batch commands in:

```text
docs/qwen3_1p7b_c4_128_random16_chunked_runbook.md
```

Then merge and regenerate:

```text
outputs/qwen3_1p7b_c4_128_consensus_random16_merged_ppl_summary.json
outputs/qwen3_1p7b_c4_128_consensus_random16_evidence_matrix.md
outputs/qwen3_1p7b_c4_128_consensus_random16_random_seed_audit.md
outputs/qwen3_1p7b_c4_128_consensus_random16_gpu_guard_summary.md
```
