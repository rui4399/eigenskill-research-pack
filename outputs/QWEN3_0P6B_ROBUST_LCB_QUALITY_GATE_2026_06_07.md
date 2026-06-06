# Robust LCB Quality Boundary Gate

Date: `2026-06-06T16:28:55+00:00`
Status: **PASS**
Cases: `2`
Target wins vs uniform: `2`
Target wins vs mean consensus: `0`
Max guard VRAM ratio: `0.7032`

## Cases

| case | FP16 PPL | uniform INT4 | mean consensus | robust LCB | margin vs uniform | margin vs mean | VRAM | source |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `wikitext2_64_len96` | 33.9865 | 54.6542 | 45.6559 | 49.2223 | 5.4318 | -3.5665 | 0.7032 | `outputs/qwen3_0p6b_robust_lcb_vs_mean_ppl_wikitext2_64_len96_summary.json` |
| `c4_64` | 36.1380 | 52.9352 | 44.9290 | 47.1293 | 5.8059 | -2.2003 | 0.6978 | `outputs/qwen3_0p6b_robust_lcb_vs_mean_ppl_c4_64_summary.json` |

## Failures

- none

## Claim Boundary

- Valid claim: on the measured guarded Qwen3-0.6B fake-quant PPL slices, robust-LCB improves over uniform INT4 and its comparison against mean consensus is explicitly reported. Invalid claim: this proves robust-LCB is the best allocation policy or establishes SOTA quantization quality.
