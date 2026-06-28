# Calibration Seed Stability Gate

Date: `2026-06-28T10:47:56+00:00`
Status: **PASS**

## Summary

- cases: `6`
- pairs: `15`
- finite pairs: `15`
- unique prompt selections: `6`
- mean score/cost Spearman: `0.3133`
- mean score/cost Spearman bootstrap 95% CI: `[0.2570, 0.3700]`
- min score/cost Spearman: `0.1168`
- mean top-20 Jaccard: `0.3779`
- mean top-20 Jaccard bootstrap 95% CI: `[0.3254, 0.4319]`
- min top-20 Jaccard: `0.2121`
- mean positive-set Jaccard: `0.5390`
- mean positive-set Jaccard bootstrap 95% CI: `[0.5086, 0.5681]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `seed00` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 4 | 20261600 | `[3, 8, 15, 24]` |
| `seed01` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 4 | 20262001 | `[4, 6, 10, 19]` |
| `seed02` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 4 | 20262002 | `[11, 22, 26, 27]` |
| `seed03` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 4 | 20262003 | `[1, 10, 14, 22]` |
| `seed04` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 4 | 20262004 | `[7, 10, 19, 27]` |
| `seed05` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 4 | 20262005 | `[0, 10, 21, 24]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `seed00` | `seed01` | 225 | 0.1168 | 0.4293 | 0.2121 |
| `seed00` | `seed02` | 225 | 0.2625 | 0.5134 | 0.2500 |
| `seed00` | `seed03` | 225 | 0.1581 | 0.4824 | 0.2500 |
| `seed00` | `seed04` | 225 | 0.2370 | 0.4586 | 0.2903 |
| `seed00` | `seed05` | 225 | 0.4347 | 0.5314 | 0.3333 |
| `seed01` | `seed02` | 225 | 0.1535 | 0.4845 | 0.2903 |
| `seed01` | `seed03` | 225 | 0.3765 | 0.6129 | 0.4815 |
| `seed01` | `seed04` | 225 | 0.5486 | 0.6503 | 0.4286 |
| `seed01` | `seed05` | 225 | 0.3938 | 0.5690 | 0.3793 |
| `seed02` | `seed03` | 225 | 0.3175 | 0.6162 | 0.3793 |
| `seed02` | `seed04` | 225 | 0.3365 | 0.5372 | 0.3333 |
| `seed02` | `seed05` | 225 | 0.2650 | 0.5103 | 0.5385 |
| `seed03` | `seed04` | 225 | 0.3444 | 0.5759 | 0.5385 |
| `seed03` | `seed05` | 225 | 0.3583 | 0.5482 | 0.4815 |
| `seed04` | `seed05` | 225 | 0.3966 | 0.5657 | 0.4815 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
