# EigenSkill-Q 2026-06-05 Update: Chunked Random16 Merge Path

## Summary

This update adds and verifies the CPU/C++ infrastructure needed to finish the
Qwen3-1.7B C4-128 random16 audit under the 85% GPU-memory guard.

Status changed from "planned chunked run" to "completed low-memory chunked
run". The first `--reuse-model` chunk was killed at `6936/8151 MiB = 85.09%`;
the regenerated low-memory plan removed `--reuse-model`, reloaded per config,
and completed the remaining random16 batches at about 68% peak VRAM.

## What Changed

- Added `inference_cpp/src/quant_ppl_summary_merge.cpp`.
- Added CMake target `quant_ppl_summary_merge`.
- Added two CTest smoke tests:
  - merge two PPL summary files;
  - feed the merged output into `quant_random_baseline_audit`.
- Added three C4-128 random16 batch configs for seeds 20260608-20260619.
- Added `docs/qwen3_1p7b_c4_128_random16_chunked_runbook.md`.
- Added `quant_seed_coverage_check`, a C++ audit tool for detecting missing,
  duplicate, or out-of-range random seed result names across chunked configs or
  merged summaries.
- Added `quant_chunked_eval_plan`, a C++ command-plan generator that emits the
  guarded batch script and Markdown plan for the C4-128 random16 run.
- Committed the generated shell entrypoint:
  `tools/run_qwen3_1p7b_c4_128_random16_chunked.sh`.
- Updated `README.md` to document the C4-128 random4 result and the chunked
  random16 path.
- Extended `quant_sensitivity_stability` with Calibration Split Instability
  metrics and JSON output.
- Added `docs/calibration_split_instability_position_2026_06_05.md` to reframe
  the paper track as calibration robustness, not a new quantizer claim.
- Generated OLMo2 WikiText2/C4 CSI reports:
  `outputs/olmo2_0425_1b_wikitext_c4_calibration_split_instability_cpp.md`
  and `.json`.

## Verified Result

The completed Qwen3-1.7B C4-128 random16 row is:

| Dataset | FP16 | uniform INT4 | consensus | category | random min/mean/max |
|---|---:|---:|---:|---:|---:|
| C4-128 | 29.4065 | 35.7923 | 32.8806 | 34.1947 | 33.1374 / 34.3623 / 35.1416 |

Margins:

- consensus vs uniform INT4: +2.9117 PPL
- consensus vs category: +1.3141 PPL
- consensus vs best random16: +0.2568 PPL
- consensus vs random16 mean: +1.4817 PPL
- random-seed audit: 16 wins / 0 losses / 0 ties

GPU guard:

```text
batch0: 6884 / 8151 MiB = 84.46%
batch1: 5538 / 8151 MiB = 67.94%
batch2: 5546 / 8151 MiB = 68.04%
batch3: 5538 / 8151 MiB = 67.94%
status: all pass
```

## Why The New C++ Merge Tool Matters

The full C4-128 random16 command exceeded the 85% guard when run as one
process, and `--reuse-model` also failed on the first four-seed chunk at 85.09%.
The new merge tool and low-memory planner allow this experiment to be completed
as four guarded chunks:

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

Latest result:

```text
21/21 tests passed
```

Additional smoke:

```text
quant_ppl_summary_merge on fixture summaries
quant_random_baseline_audit on merged fixture
quant_ppl_summary_merge self-merge on real Qwen3 C4-128 random4 summary
quant_seed_coverage_check on fixture configs, including duplicate-failure test
quant_chunked_eval_plan bash/markdown CTest smoke
quant_sensitivity_stability csv/json CTest smoke
```

The real random4 self-merge preserved the audit result:

```text
target PPL: 32.880630
seed_count: 4
wins/losses/ties: 4 / 0 / 0
margin_vs_best_seed: +0.392768
```

The real C4-128 random16 config coverage check now passes before the remaining
GPU batches are run:

```text
expected seeds: 16
matched seeds: 16
missing: 0
duplicates: 0
out-of-range: 0
missing required baseline names: 0
```

## Calibration Split Instability Reframe

The paper-facing framing should now be:

```text
Calibration Split Instability + conservative consensus allocation diagnostics
```

It should not be described as "a new quantizer." The random16 audit is a sanity
guardrail; the stronger research problem is that small calibration splits can
produce unstable module-sensitivity rankings.

OLMo2 WikiText2 vs C4 CSI:

```text
positive-set instability: 0.5488
sign instability:         0.3982
score-rank instability:   0.4078
mean top-k Jaccard:       0.1640
top-k instability:        0.8360
CSI:                      0.5477
```

## GitHub

Latest pushed infrastructure commit before this documentation update:

```text
0bc7243e2d770692f5816111a25022dc7e4add64
```

Repo:

```text
https://github.com/rui4399/eigenskill-research-pack
```

## Next GPU Step

The Qwen3-1.7B C4-128 random16 GPU step is complete. Next GPU work should move
to either a stronger non-Qwen small model or a task benchmark beyond PPL, not
more random seeds on the same slice.

```text
Candidate next targets:
ibm-granite/granite-3.3-2b-instruct
HuggingFaceTB/SmolLM3-3B
MMLU/GSM8K/IFEval-style smoke evaluation
```
