# Robust LCB Consensus Gate

Date: `2026-07-01T15:28:16+00:00`
Status: **PASS**
Cases: `1`
Total high-bit modules: `65`
Consistent selected modules: `30`

## Cases

| case | model | avg bits | high-bit modules | selected | consistent selected | protected ratio | bit hist | source |
|---|---|---:|---:|---:|---:|---:|---|---|
| `local` | `/mnt/c/Users/18042/models/Qwen2.5-1.5B-Instruct` | 4.499338 | 65 | 30 | 30 | 0.544531 | `{'8': 65, '4': 132}` | `outputs/LOCAL_SMOKE_QWEN25_1P5B_CONSENSUS_ALLOC_2026_07_01.json` |

## Failures

- none

## Claim Boundary

- Valid claim: robust-LCB consensus allocation artifacts exist across the gated model family, respect the configured average-bit budget, and expose selected-module consistency evidence. Invalid claim: this gate proves downstream PPL, task accuracy, mobile deployment, or SOTA quality.
