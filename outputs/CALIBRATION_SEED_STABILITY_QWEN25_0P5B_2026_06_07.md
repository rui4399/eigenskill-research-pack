# Calibration Seed Stability Gate

Date: `2026-06-07T06:18:39+00:00`
Status: **PASS**

## Summary

- cases: `3`
- pairs: `3`
- finite pairs: `3`
- unique prompt selections: `3`
- mean score/cost Spearman: `0.4230`
- min score/cost Spearman: `0.2741`
- mean top-20 Jaccard: `0.4652`
- min top-20 Jaccard: `0.4286`
- mean positive-set Jaccard: `0.5517`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `seed11` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260611 | `[7, 8, 13, 15]` |
| `seed12` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260612 | `[0, 3, 5, 6]` |
| `seed13` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 4 | 20260613 | `[3, 8, 12, 13]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `seed11` | `seed12` | 169 | 0.2741 | 0.4638 | 0.4286 |
| `seed11` | `seed13` | 169 | 0.6838 | 0.6614 | 0.5385 |
| `seed12` | `seed13` | 169 | 0.3110 | 0.5299 | 0.4286 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
