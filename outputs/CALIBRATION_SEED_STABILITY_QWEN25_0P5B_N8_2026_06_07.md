# Calibration Seed Stability Gate

Date: `2026-06-07T07:35:01+00:00`
Status: **PASS**

## Summary

- cases: `6`
- pairs: `15`
- finite pairs: `15`
- unique prompt selections: `6`
- mean score/cost Spearman: `0.6645`
- mean score/cost Spearman bootstrap 95% CI: `[0.6236, 0.7048]`
- min score/cost Spearman: `0.5171`
- mean top-20 Jaccard: `0.6449`
- mean top-20 Jaccard bootstrap 95% CI: `[0.5962, 0.6915]`
- min top-20 Jaccard: `0.5385`
- mean positive-set Jaccard: `0.7282`
- mean positive-set Jaccard bootstrap 95% CI: `[0.7050, 0.7520]`

## Prompt Selections

| label | source | pool | sample | seed | selected indices |
|---|---|---:|---:|---:|---|
| `n8_seed11` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260611 | `[2, 3, 7, 8, 9, 11, 13, 15]` |
| `n8_seed12` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260612 | `[0, 3, 5, 6, 8, 13, 14, 15]` |
| `n8_seed13` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260613 | `[0, 2, 3, 6, 8, 11, 12, 13]` |
| `n8_seed14` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260614 | `[2, 4, 5, 7, 8, 9, 13, 15]` |
| `n8_seed15` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260615 | `[3, 4, 6, 8, 12, 13, 14, 15]` |
| `n8_seed16` | `data_eval/public_ppl_prompts_16_2026_06_07/wikitext2_test_ppl_prompts.txt` | 16 | 8 | 20260616 | `[3, 4, 5, 7, 8, 10, 12, 13]` |

## Pairwise Stability

| left | right | shared modules | score/cost Spearman | positive Jaccard | top-20 Jaccard |
|---|---|---:|---:|---:|---:|
| `n8_seed11` | `n8_seed12` | 169 | 0.6769 | 0.7231 | 0.8182 |
| `n8_seed11` | `n8_seed13` | 169 | 0.6614 | 0.7090 | 0.5385 |
| `n8_seed11` | `n8_seed14` | 169 | 0.7829 | 0.8110 | 0.7391 |
| `n8_seed11` | `n8_seed15` | 169 | 0.5764 | 0.6716 | 0.5385 |
| `n8_seed11` | `n8_seed16` | 169 | 0.6900 | 0.7348 | 0.7391 |
| `n8_seed12` | `n8_seed13` | 169 | 0.7504 | 0.7752 | 0.6667 |
| `n8_seed12` | `n8_seed14` | 169 | 0.5710 | 0.6912 | 0.7391 |
| `n8_seed12` | `n8_seed15` | 169 | 0.6895 | 0.7638 | 0.5385 |
| `n8_seed12` | `n8_seed16` | 169 | 0.6607 | 0.7218 | 0.7391 |
| `n8_seed13` | `n8_seed14` | 169 | 0.5171 | 0.6549 | 0.5385 |
| `n8_seed13` | `n8_seed15` | 169 | 0.6672 | 0.7348 | 0.6000 |
| `n8_seed13` | `n8_seed16` | 169 | 0.5718 | 0.6714 | 0.5385 |
| `n8_seed14` | `n8_seed15` | 169 | 0.5926 | 0.6912 | 0.6000 |
| `n8_seed14` | `n8_seed16` | 169 | 0.7631 | 0.8077 | 0.7391 |
| `n8_seed15` | `n8_seed16` | 169 | 0.7968 | 0.7615 | 0.6000 |

## Claim Boundary

Valid claim: deterministic prompt-seed sensitivity artifacts can be audited for pairwise ranking stability under the same model and prompt pool. Invalid claim: this alone proves downstream quality retention, SOTA quantization, or deployment speed.

## Failures

- none
