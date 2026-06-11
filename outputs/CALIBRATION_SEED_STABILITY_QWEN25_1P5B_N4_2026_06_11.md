# Calibration Seed Stability Gate

Date: `2026-06-10T17:05:36+00:00`
Status: **PASS**

## Summary

- cases: `6`
- pairs: `15`
- finite pairs: `15`
- unique prompt selections: `6`
- mean score/cost Spearman: `0.2869`
- mean score/cost Spearman bootstrap 95% CI: `[0.2312, 0.3506]`
- min score/cost Spearman: `0.1490`
- mean top-20 Jaccard: `0.3313`
- mean top-20 Jaccard bootstrap 95% CI: `[0.2973, 0.3697]`
- min top-20 Jaccard: `0.2500`
- mean positive-set Jaccard: `0.5189`
- mean positive-set Jaccard bootstrap 95% CI: `[0.4954, 0.5449]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `seed31` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260631 | `[3, 4, 9, 14]` |
| `seed32` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260632 | `[6, 7, 8, 13]` |
| `seed33` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260633 | `[0, 8, 9, 14]` |
| `seed34` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260634 | `[0, 4, 8, 15]` |
| `seed35` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260635 | `[0, 2, 4, 13]` |
| `seed36` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260636 | `[1, 2, 6, 15]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `seed31` | `seed32` | 197 | 0.1598 | 0.4780 | 0.2500 |
| `seed31` | `seed33` | 197 | 0.5073 | 0.6178 | 0.4815 |
| `seed31` | `seed34` | 197 | 0.1753 | 0.4596 | 0.3333 |
| `seed31` | `seed35` | 197 | 0.2603 | 0.5253 | 0.2500 |
| `seed31` | `seed36` | 197 | 0.1490 | 0.4969 | 0.2903 |
| `seed32` | `seed33` | 197 | 0.3934 | 0.5933 | 0.3333 |
| `seed32` | `seed34` | 197 | 0.3768 | 0.5068 | 0.3793 |
| `seed32` | `seed35` | 197 | 0.1771 | 0.4771 | 0.2500 |
| `seed32` | `seed36` | 197 | 0.1770 | 0.4586 | 0.2903 |
| `seed33` | `seed34` | 197 | 0.3552 | 0.5519 | 0.4815 |
| `seed33` | `seed35` | 197 | 0.1938 | 0.4671 | 0.3333 |
| `seed33` | `seed36` | 197 | 0.1941 | 0.4940 | 0.2500 |
| `seed34` | `seed35` | 197 | 0.5164 | 0.6028 | 0.3333 |
| `seed34` | `seed36` | 197 | 0.2865 | 0.4870 | 0.3333 |
| `seed35` | `seed36` | 197 | 0.3821 | 0.5667 | 0.3793 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
