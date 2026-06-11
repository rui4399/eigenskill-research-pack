# Calibration Seed Stability Gate

Date: `2026-06-11T11:02:52+00:00`
Status: **PASS**

## Summary

- cases: `6`
- pairs: `15`
- finite pairs: `15`
- unique prompt selections: `6`
- mean score/cost Spearman: `0.4918`
- mean score/cost Spearman bootstrap 95% CI: `[0.4432, 0.5458]`
- min score/cost Spearman: `0.3092`
- mean top-20 Jaccard: `0.4401`
- mean top-20 Jaccard bootstrap 95% CI: `[0.3979, 0.4777]`
- min top-20 Jaccard: `0.2500`
- mean positive-set Jaccard: `0.5992`
- mean positive-set Jaccard bootstrap 95% CI: `[0.5773, 0.6221]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `seed41` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260641 | `[0, 1, 2, 5, 6, 10, 14, 15]` |
| `seed42` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260642 | `[0, 6, 7, 9, 10, 11, 13, 14]` |
| `seed43` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260643 | `[1, 4, 5, 8, 9, 12, 13, 14]` |
| `seed44` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260644 | `[3, 6, 8, 9, 10, 11, 12, 15]` |
| `seed45` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260645 | `[2, 4, 5, 6, 8, 10, 12, 14]` |
| `seed46` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260646 | `[0, 1, 4, 7, 9, 10, 11, 14]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `seed41` | `seed42` | 197 | 0.5136 | 0.6067 | 0.4286 |
| `seed41` | `seed43` | 197 | 0.4393 | 0.6062 | 0.4815 |
| `seed41` | `seed44` | 197 | 0.3092 | 0.5094 | 0.4286 |
| `seed41` | `seed45` | 197 | 0.6755 | 0.6667 | 0.5385 |
| `seed41` | `seed46` | 197 | 0.5662 | 0.6118 | 0.4815 |
| `seed42` | `seed43` | 197 | 0.4028 | 0.5443 | 0.3793 |
| `seed42` | `seed44` | 197 | 0.5283 | 0.5764 | 0.4815 |
| `seed42` | `seed45` | 197 | 0.4379 | 0.5695 | 0.2500 |
| `seed42` | `seed46` | 197 | 0.6989 | 0.6812 | 0.5385 |
| `seed43` | `seed44` | 197 | 0.4215 | 0.5882 | 0.3793 |
| `seed43` | `seed45` | 197 | 0.5242 | 0.6429 | 0.5385 |
| `seed43` | `seed46` | 197 | 0.5330 | 0.6316 | 0.4815 |
| `seed44` | `seed45` | 197 | 0.4891 | 0.6164 | 0.3333 |
| `seed44` | `seed46` | 197 | 0.3928 | 0.5608 | 0.4815 |
| `seed45` | `seed46` | 197 | 0.4448 | 0.5752 | 0.3793 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
