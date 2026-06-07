# Calibration Seed Stability Gate

Date: `2026-06-07T08:06:32+00:00`
Status: **PASS**

## Summary

- cases: `6`
- pairs: `15`
- finite pairs: `15`
- unique prompt selections: `6`
- mean score/cost Spearman: `0.3725`
- mean score/cost Spearman bootstrap 95% CI: `[0.2960, 0.4519]`
- min score/cost Spearman: `0.1128`
- mean top-20 Jaccard: `0.3797`
- mean top-20 Jaccard bootstrap 95% CI: `[0.3336, 0.4270]`
- min top-20 Jaccard: `0.1765`
- mean positive-set Jaccard: `0.5485`
- mean positive-set Jaccard bootstrap 95% CI: `[0.5151, 0.5852]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `n2_seed11` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260611 | `[7, 8]` |
| `n2_seed12` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260612 | `[3, 5]` |
| `n2_seed13` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260613 | `[3, 13]` |
| `n2_seed14` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260614 | `[5, 9]` |
| `n2_seed15` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260615 | `[13, 14]` |
| `n2_seed17` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260617 | `[2, 3]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `n2_seed11` | `n2_seed12` | 169 | 0.3825 | 0.5538 | 0.3333 |
| `n2_seed11` | `n2_seed13` | 169 | 0.3352 | 0.5481 | 0.3793 |
| `n2_seed11` | `n2_seed14` | 169 | 0.2710 | 0.4672 | 0.3333 |
| `n2_seed11` | `n2_seed15` | 169 | 0.3999 | 0.5252 | 0.4286 |
| `n2_seed11` | `n2_seed17` | 169 | 0.2879 | 0.5105 | 0.3793 |
| `n2_seed12` | `n2_seed13` | 169 | 0.5712 | 0.6429 | 0.4815 |
| `n2_seed12` | `n2_seed14` | 169 | 0.4813 | 0.5794 | 0.4286 |
| `n2_seed12` | `n2_seed15` | 169 | 0.3217 | 0.5108 | 0.3793 |
| `n2_seed12` | `n2_seed17` | 169 | 0.5874 | 0.6212 | 0.5385 |
| `n2_seed13` | `n2_seed14` | 169 | 0.1128 | 0.4714 | 0.2500 |
| `n2_seed13` | `n2_seed15` | 169 | 0.4851 | 0.5839 | 0.3793 |
| `n2_seed13` | `n2_seed17` | 169 | 0.6646 | 0.7266 | 0.5385 |
| `n2_seed14` | `n2_seed15` | 169 | 0.2048 | 0.5036 | 0.1765 |
| `n2_seed14` | `n2_seed17` | 169 | 0.2032 | 0.4589 | 0.2903 |
| `n2_seed15` | `n2_seed17` | 169 | 0.2794 | 0.5238 | 0.3793 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
