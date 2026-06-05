# EigenSkill-Q 2026-06-05 Update: Qwen3-0.6B Random16 Audit

## Summary

This update strengthens the short-cycle Qwen3-0.6B evidence by moving beyond a
uniform INT4 comparison. The same 4.5 average-bit `{4,8}` loss-sensitive
allocation is now compared against:

- uniform INT4
- C++ category heuristic budget
- C++ aggregate random budget
- 15 explicit random-seed budgets
- two public-text slices: WikiText2-64 len96 and C4-64
- the 85% GPU-memory guard requested by Rui

The result is useful but not overclaimed: Qwen3-0.6B loss-sensitive allocation
wins strongly on C4 and wins the random-seed mean on WikiText2, but one
WikiText2 random seed still beats it.

## Main Numbers

| Dataset | FP16 | uniform INT4 | loss-sensitive | category | random_seed min/mean/max | random_seed win/loss/tie |
|---|---:|---:|---:|---:|---:|---:|
| WikiText2-64 len96 | 33.9865 | 54.6542 | 49.5352 | 50.4746 | 48.5030 / 50.4787 / 52.6347 | 12 / 3 / 0 |
| C4-64 | 36.1380 | 52.9352 | 47.5872 | 48.6222 | 48.3840 / 49.4427 / 50.7971 | 15 / 0 / 0 |

Margins:

- WikiText2: `+5.1189` PPL vs uniform INT4, `+0.9435` vs random-seed mean, `-1.0322` vs best random seed.
- C4: `+5.3480` PPL vs uniform INT4, `+1.8556` vs random-seed mean, `+0.7969` vs best random seed.

Positive margin means the loss-sensitive target has lower PPL.

## GPU Guard

Both runs stayed far below the requested 85% VRAM ceiling:

| Run | Peak VRAM | Peak Ratio | Peak GPU Util | Guard |
|---|---:|---:|---:|---|
| WikiText2-64 len96 | 4260 / 8151 MiB | 52.26% | 56% | pass |
| C4-64 | 4270 / 8151 MiB | 52.39% | 57% | pass |

## New C++ Artifact

Added:

```text
inference_cpp/src/quant_random_baseline_audit.cpp
```

This tool reads fake-quant PPL summary JSON and reports:

- target PPL
- best random seed
- random-seed min/mean/max
- win/loss/tie count against `random_seed_*`
- margin vs best random seed
- margin vs random-seed mean

It deliberately excludes aggregate configs such as `cpp_random_budget` from the
seed win-rate calculation.

Generated outputs:

```text
outputs/qwen3_0p6b_lowmem_cpp_random16_random_seed_audit.md
outputs/qwen3_0p6b_lowmem_cpp_random16_random_seed_audit.json
outputs/qwen3_0p6b_lowmem_cpp_random16_random_seed_audit.csv
outputs/qwen3_0p6b_lowmem_cpp_random16_wikitext2_len96_c4_evidence_matrix.md
outputs/qwen3_0p6b_lowmem_cpp_random16_gpu_guard_summary.md
```

## Interpretation

This is stronger in-repo evidence than comparing only against uniform INT4.
However, it is still a PyTorch fake-quant diagnostic, not a packed INT4/INT8
runtime and not a SOTA quantization claim.

The clean claim is:

> On Qwen3-0.6B short public-text slices, a 4-prompt loss-sensitive C++ planner
> allocation improves over uniform INT4, category, and random-seed mean under a
> 4.5 average-bit budget, while C4 also beats all 15 tested random seeds.

The honest caveat is:

> On WikiText2-64 len96, one random seed still beats the loss-sensitive
> allocation, so the single-split loss probe is not robust enough by itself.

This supports the next research direction: cross-dataset consensus allocation,
more calibration prompts, and eventually GPTQ/AWQ/rotation baselines.

## Reproduce

Build the C++ tools:

```bash
cmake -S inference_cpp -B build/cpp-wsl -DCMAKE_BUILD_TYPE=Release
cmake --build build/cpp-wsl -j2
ctest --test-dir build/cpp-wsl --output-on-failure
```

Regenerate the random-seed audit from committed summaries:

```bash
build/cpp-wsl/quant_random_baseline_audit \
  --input outputs/qwen3_0p6b_lowmem_cpp_random16_ppl_wikitext2_64_len96_summary.json \
  --dataset wikitext2_64_len96 \
  --input outputs/qwen3_0p6b_lowmem_cpp_random16_ppl_c4_64_summary.json \
  --dataset c4_64 \
  --target cpp_loss_sensitive_budget \
  --emit markdown
```

## Next

1. Push this result to GitHub.
2. Add an actual packed/real quantizer baseline where possible: GPTQ, AWQ,
   SmoothQuant, QuaRot/SpinQuant/OptRot-style rotations.
3. Extend Qwen3-0.6B from a single 4-prompt calibration split to a
   WikiText2+C4 consensus allocation, matching the stronger Qwen3-1.7B/OLMo2
   evidence pattern.
4. Keep C++ work moving: more reporting and eventually runtime-side packed
   kernel checks, not just Python fake-quant evaluation.
