# Robust LCB Consensus Gate

Date: `2026-06-06T16:10:18+00:00`
Status: **PASS**
Cases: `3`
Total high-bit modules: `99`
Consistent selected modules: `80`

## Cases

| case | model | avg bits | high-bit modules | selected | consistent selected | protected ratio | bit hist | source |
|---|---|---:|---:|---:|---:|---:|---|---|
| `qwen3_0p6b` | `Qwen/Qwen3-0.6B` | 4.499670 | 38 | 30 | 30 | 0.320160 | `{'4': 159, '8': 38}` | `outputs/qwen3_0p6b_robust_lcb_wikitext_c4_consensus_alloc_4to8_group128_summary.json` |
| `qwen3_1p7b` | `Qwen/Qwen3-1.7B` | 4.497334 | 41 | 30 | 30 | 0.401828 | `{'8': 41, '4': 156}` | `outputs/qwen3_1p7b_robust_lcb_wikitext_c4_consensus_alloc_4to8_group128_summary.json` |
| `olmo2_0425_1b` | `allenai/OLMo-2-0425-1B-Instruct` | 4.498361 | 20 | 20 | 20 | 0.330085 | `{'8': 20, '4': 93}` | `outputs/olmo2_0425_1b_robust_lcb_wikitext_c4_consensus_alloc_4to8_group128_summary.json` |

## Failures

- none

## Claim Boundary

- Valid claim: robust-LCB consensus allocation artifacts exist across the gated model family, respect the configured average-bit budget, and expose selected-module consistency evidence. Invalid claim: this gate proves downstream PPL, task accuracy, mobile deployment, or SOTA quality.
