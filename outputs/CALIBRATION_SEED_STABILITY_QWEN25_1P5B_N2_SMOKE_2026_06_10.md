# Calibration Seed Stability Gate

Date: `2026-06-10T11:11:34+00:00`
Status: **PASS**

## Summary

- cases: `3`
- pairs: `3`
- finite pairs: `3`
- unique prompt selections: `3`
- mean score/cost Spearman: `0.0942`
- mean score/cost Spearman bootstrap 95% CI: `[0.0377, 0.1864]`
- min score/cost Spearman: `0.0377`
- mean top-20 Jaccard: `0.2002`
- mean top-20 Jaccard bootstrap 95% CI: `[0.1765, 0.2121]`
- min top-20 Jaccard: `0.1765`
- mean positive-set Jaccard: `0.4067`
- mean positive-set Jaccard bootstrap 95% CI: `[0.3892, 0.4416]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `seed21` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260621 | `[5, 11]` |
| `seed22` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260622 | `[3, 13]` |
| `seed23` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260623 | `[9, 10]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `seed21` | `seed22` | 197 | 0.0584 | 0.3892 | 0.2121 |
| `seed21` | `seed23` | 197 | 0.0377 | 0.3892 | 0.1765 |
| `seed22` | `seed23` | 197 | 0.1864 | 0.4416 | 0.2121 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
