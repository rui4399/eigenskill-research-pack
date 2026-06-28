# Calibration Seed Stability Gate

Date: `2026-06-28T10:47:57+00:00`
Status: **PASS**

## Summary

- cases: `6`
- pairs: `15`
- finite pairs: `15`
- unique prompt selections: `6`
- mean score/cost Spearman: `0.6959`
- mean score/cost Spearman bootstrap 95% CI: `[0.6546, 0.7389]`
- min score/cost Spearman: `0.5959`
- mean top-20 Jaccard: `0.5761`
- mean top-20 Jaccard bootstrap 95% CI: `[0.5549, 0.5979]`
- min top-20 Jaccard: `0.5385`
- mean positive-set Jaccard: `0.7512`
- mean positive-set Jaccard bootstrap 95% CI: `[0.7303, 0.7718]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `seed00` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 16 | 20263200 | `[0, 1, 2, 3, 6, 7, 10, 12, 16, 18, 19, 24, 26, 28, 30, 31]` |
| `seed01` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 16 | 20263201 | `[0, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 18, 19, 22, 26]` |
| `seed02` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 16 | 20263202 | `[0, 1, 2, 5, 6, 8, 9, 14, 15, 16, 19, 22, 24, 29, 30, 31]` |
| `seed03` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 16 | 20263203 | `[0, 2, 3, 4, 6, 8, 10, 11, 13, 18, 22, 23, 25, 27, 28, 31]` |
| `seed04` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 16 | 20263204 | `[0, 1, 2, 4, 10, 14, 15, 16, 17, 19, 24, 26, 27, 28, 29, 30]` |
| `seed05` | `data_eval/text_prompts/wikitext2_validation_32.txt` | 32 | 16 | 20263205 | `[0, 1, 2, 4, 5, 6, 7, 12, 15, 16, 20, 22, 23, 24, 28, 31]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `seed00` | `seed01` | 225 | 0.6183 | 0.7037 | 0.6000 |
| `seed00` | `seed02` | 225 | 0.7635 | 0.7849 | 0.6000 |
| `seed00` | `seed03` | 225 | 0.6249 | 0.7158 | 0.5385 |
| `seed00` | `seed04` | 225 | 0.7995 | 0.8177 | 0.6000 |
| `seed00` | `seed05` | 225 | 0.8550 | 0.8000 | 0.6667 |
| `seed01` | `seed02` | 225 | 0.7029 | 0.7814 | 0.6667 |
| `seed01` | `seed03` | 225 | 0.5959 | 0.7112 | 0.6000 |
| `seed01` | `seed04` | 225 | 0.5965 | 0.7000 | 0.5385 |
| `seed01` | `seed05` | 225 | 0.6433 | 0.7120 | 0.5385 |
| `seed02` | `seed03` | 225 | 0.6049 | 0.7010 | 0.6000 |
| `seed02` | `seed04` | 225 | 0.7382 | 0.7619 | 0.5385 |
| `seed02` | `seed05` | 225 | 0.8076 | 0.7926 | 0.5385 |
| `seed03` | `seed04` | 225 | 0.6381 | 0.7302 | 0.5385 |
| `seed03` | `seed05` | 225 | 0.6941 | 0.7701 | 0.5385 |
| `seed04` | `seed05` | 225 | 0.7550 | 0.7861 | 0.5385 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
