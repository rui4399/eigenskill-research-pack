# Calibration Seed Stability Gate

Date: `2026-06-10T11:24:32+00:00`
Status: **PASS**

## Summary

- cases: `6`
- pairs: `15`
- finite pairs: `15`
- unique prompt selections: `6`
- mean score/cost Spearman: `0.1410`
- mean score/cost Spearman bootstrap 95% CI: `[0.0779, 0.2133]`
- min score/cost Spearman: `-0.0140`
- mean top-20 Jaccard: `0.2604`
- mean top-20 Jaccard bootstrap 95% CI: `[0.2213, 0.3060]`
- min top-20 Jaccard: `0.1765`
- mean positive-set Jaccard: `0.4244`
- mean positive-set Jaccard bootstrap 95% CI: `[0.3954, 0.4564]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `seed21` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260621 | `[5, 11]` |
| `seed22` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260622 | `[3, 13]` |
| `seed23` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260623 | `[9, 10]` |
| `seed24` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260624 | `[4, 12]` |
| `seed25` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260625 | `[4, 7]` |
| `seed26` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 2 | 20260626 | `[0, 3]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `seed21` | `seed22` | 197 | 0.0584 | 0.3892 | 0.2121 |
| `seed21` | `seed23` | 197 | 0.0377 | 0.3892 | 0.1765 |
| `seed21` | `seed24` | 197 | 0.2018 | 0.4706 | 0.1765 |
| `seed21` | `seed25` | 197 | 0.1754 | 0.4258 | 0.2500 |
| `seed21` | `seed26` | 197 | 0.1314 | 0.4540 | 0.2121 |
| `seed22` | `seed23` | 197 | 0.1864 | 0.4416 | 0.2121 |
| `seed22` | `seed24` | 197 | 0.0822 | 0.3694 | 0.2903 |
| `seed22` | `seed25` | 197 | 0.0030 | 0.3791 | 0.2121 |
| `seed22` | `seed26` | 197 | 0.4310 | 0.5442 | 0.4815 |
| `seed23` | `seed24` | 197 | -0.0068 | 0.3438 | 0.2500 |
| `seed23` | `seed25` | 197 | -0.0140 | 0.3354 | 0.2121 |
| `seed23` | `seed26` | 197 | 0.0811 | 0.4367 | 0.2500 |
| `seed24` | `seed25` | 197 | 0.4284 | 0.5455 | 0.3793 |
| `seed24` | `seed26` | 197 | 0.1070 | 0.3924 | 0.2121 |
| `seed25` | `seed26` | 197 | 0.2121 | 0.4497 | 0.3793 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
