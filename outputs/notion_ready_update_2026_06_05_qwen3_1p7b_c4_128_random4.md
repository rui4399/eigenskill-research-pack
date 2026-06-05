# EigenSkill-Q 2026-06-05 Update: Qwen3-1.7B C4-128 Guard-Filling Run

## Summary

This update follows Rui's instruction to use the NVIDIA GPU more aggressively
while keeping VRAM below 85%. The experiment expands the Qwen3-1.7B consensus
path from C4-64 to C4-128, but uses a lighter random4 comparison set so the
run stays inside the guard.

Two full random16 C4-128 attempts were intentionally rejected by the GPU guard:

- `max_length=128`: killed at 7033 / 8151 MiB = 86.28%
- `max_length=96`: killed at 7035 / 8151 MiB = 86.31%

The accepted run uses C4-128, `max_length=128`, and a smaller comparison set:
FP16, uniform INT4, WikiText2+C4 consensus, category, and four explicit random
seed allocations.

## Main Result

| Dataset | FP16 | uniform INT4 | consensus | category | random min/mean/max |
|---|---:|---:|---:|---:|---:|
| C4-128 | 29.4065 | 35.7923 | 32.8806 | 34.1947 | 33.2734 / 34.5656 / 35.1416 |

Margins:

- consensus vs uniform INT4: +2.9117 PPL
- consensus vs category: +1.3141 PPL
- consensus vs best random4: +0.3928 PPL
- consensus vs random4 mean: +1.6849 PPL

Positive margin means the consensus target has lower PPL.

## Random Audit

| Dataset | target PPL | seed count | win/loss/tie | best seed | margin vs best seed |
|---|---:|---:|---:|---|---:|
| C4-128 | 32.8806 | 4 | 4 / 0 / 0 | `random_budget_seed_20260606` | +0.3928 |

The C++ random audit now accepts both `random_seed_*` and
`random_budget_seed_*` result names while still excluding aggregate
`cpp_random_budget` rows.

## GPU Guard

| Run | Peak VRAM | Peak Ratio | Peak GPU Util | Status |
|---|---:|---:|---:|---|
| C4-128 random4 | 6884 / 8151 MiB | 84.46% | 74% | pass |

This is currently the best example of "use the GPU hard without crossing the
85% VRAM line" in the repo.

## Generated Evidence

```text
data_eval/text_prompts/c4_en_validation_128.txt
data_eval/eval_configs/qwen3_1p7b_c4_128_consensus_random4_compare.json
outputs/qwen3_1p7b_c4_128_consensus_random4_ppl_summary.json
outputs/qwen3_1p7b_c4_128_consensus_random4_evidence_matrix.md
outputs/qwen3_1p7b_c4_128_consensus_random4_random_seed_audit.md
outputs/qwen3_1p7b_c4_128_consensus_random4_gpu_guard_summary.md
```

## Interpretation

This does not replace the random16 rows on C4-64. It is a larger-prompt
C4-128 stress row showing that the consensus allocation remains ahead of a
small random-seed pool while nearly saturating the requested VRAM ceiling.

The next clean step is to add chunked evaluation or sequential config batches
so C4-128 can eventually cover random16 without exceeding 85%.
