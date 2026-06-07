# Calibration Seed Stability Gate

Date: `2026-06-07T07:12:49+00:00`
Status: **PASS**

## Summary

- cases: `6`
- pairs: `15`
- finite pairs: `15`
- unique prompt selections: `6`
- mean score/cost Spearman: `0.4324`
- mean score/cost Spearman bootstrap 95% CI: `[0.3557, 0.5174]`
- min score/cost Spearman: `0.2284`
- mean top-20 Jaccard: `0.4672`
- mean top-20 Jaccard bootstrap 95% CI: `[0.4200, 0.5292]`
- min top-20 Jaccard: `0.3793`
- mean positive-set Jaccard: `0.5734`
- mean positive-set Jaccard bootstrap 95% CI: `[0.5375, 0.6120]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `seed11` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260611 | `[7, 8, 13, 15]` |
| `seed12` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260612 | `[0, 3, 5, 6]` |
| `seed13` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260613 | `[3, 8, 12, 13]` |
| `seed14` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260614 | `[2, 4, 5, 9]` |
| `seed15` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260615 | `[4, 6, 13, 14]` |
| `seed16` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260616 | `[3, 8, 10, 13]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `seed11` | `seed12` | 169 | 0.2741 | 0.4638 | 0.4286 |
| `seed11` | `seed13` | 169 | 0.6838 | 0.6614 | 0.5385 |
| `seed11` | `seed14` | 169 | 0.2726 | 0.4658 | 0.3793 |
| `seed11` | `seed15` | 169 | 0.4625 | 0.5597 | 0.5385 |
| `seed11` | `seed16` | 169 | 0.7037 | 0.6953 | 0.5385 |
| `seed12` | `seed13` | 169 | 0.3110 | 0.5299 | 0.4286 |
| `seed12` | `seed14` | 169 | 0.5124 | 0.6378 | 0.4286 |
| `seed12` | `seed15` | 169 | 0.4073 | 0.5615 | 0.3793 |
| `seed12` | `seed16` | 169 | 0.3660 | 0.5515 | 0.4286 |
| `seed13` | `seed14` | 169 | 0.2284 | 0.5069 | 0.3793 |
| `seed13` | `seed15` | 169 | 0.4385 | 0.5704 | 0.4815 |
| `seed13` | `seed16` | 169 | 0.7442 | 0.7323 | 0.8182 |
| `seed14` | `seed15` | 169 | 0.4160 | 0.5693 | 0.3793 |
| `seed14` | `seed16` | 169 | 0.2810 | 0.5274 | 0.3793 |
| `seed15` | `seed16` | 169 | 0.3845 | 0.5683 | 0.4815 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
