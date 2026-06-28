# Calibration Seed Stability Gate

Date: `2026-06-28T10:47:56+00:00`
Status: **PASS**

## Summary

- cases: `6`
- pairs: `15`
- finite pairs: `15`
- unique prompt selections: `6`
- mean score/cost Spearman: `0.4136`
- mean score/cost Spearman bootstrap 95% CI: `[0.3474, 0.4765]`
- min score/cost Spearman: `0.1468`
- mean top-20 Jaccard: `0.4363`
- mean top-20 Jaccard bootstrap 95% CI: `[0.3955, 0.4779]`
- min top-20 Jaccard: `0.3333`
- mean positive-set Jaccard: `0.5991`
- mean positive-set Jaccard bootstrap 95% CI: `[0.5659, 0.6305]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `seed00` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 8 | 20262400 | `[0, 1, 9, 12, 15, 23, 24, 29]` |
| `seed01` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 8 | 20262401 | `[0, 7, 12, 13, 16, 18, 23, 24]` |
| `seed02` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 8 | 20262402 | `[5, 6, 10, 18, 23, 25, 26, 30]` |
| `seed03` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 8 | 20262403 | `[4, 6, 8, 10, 11, 25, 29, 30]` |
| `seed04` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 8 | 20262404 | `[7, 8, 12, 16, 21, 28, 29, 31]` |
| `seed05` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 8 | 20262405 | `[3, 12, 13, 20, 21, 24, 25, 27]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `seed00` | `seed01` | 225 | 0.6102 | 0.6793 | 0.5385 |
| `seed00` | `seed02` | 225 | 0.3498 | 0.5608 | 0.4815 |
| `seed00` | `seed03` | 225 | 0.4758 | 0.6373 | 0.4815 |
| `seed00` | `seed04` | 225 | 0.4864 | 0.6875 | 0.3793 |
| `seed00` | `seed05` | 225 | 0.5447 | 0.6578 | 0.4815 |
| `seed01` | `seed02` | 225 | 0.2474 | 0.5054 | 0.3793 |
| `seed01` | `seed03` | 225 | 0.2517 | 0.5357 | 0.3333 |
| `seed01` | `seed04` | 225 | 0.5463 | 0.6613 | 0.3793 |
| `seed01` | `seed05` | 225 | 0.4993 | 0.6389 | 0.4286 |
| `seed02` | `seed03` | 225 | 0.4933 | 0.6124 | 0.6000 |
| `seed02` | `seed04` | 225 | 0.1468 | 0.4824 | 0.4286 |
| `seed02` | `seed05` | 225 | 0.2858 | 0.5108 | 0.3333 |
| `seed03` | `seed04` | 225 | 0.4889 | 0.6373 | 0.5385 |
| `seed03` | `seed05` | 225 | 0.4127 | 0.5729 | 0.3333 |
| `seed04` | `seed05` | 225 | 0.3655 | 0.6062 | 0.4286 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
