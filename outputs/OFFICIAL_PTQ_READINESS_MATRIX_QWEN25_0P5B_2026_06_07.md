# Official PTQ Readiness Matrix

Date: `2026-06-07T00:42:18+00:00`
Status: **PASS**

## Summary

- packages: `['autoawq', 'gptqmodel']`
- models: `['Qwen/Qwen2.5-0.5B-Instruct']`
- quant shapes: `[{'bits': 4, 'group_size': 128}]`
- common eval labels: `['c4', 'wikitext2']`
- total eval tokens across probes: `2974`

## Matrix

| package | slice | prompts | tokens | FP16 PPL | quant PPL | ratio | peak VRAM |
|---|---|---:|---:|---:|---:|---:|---:|
| `autoawq` | `wikitext2` | 8 | 760 | 24.675866 | 29.080631 | 1.178505 | 0.611581 |
| `autoawq` | `c4` | 8 | 727 | 32.951664 | 38.172702 | 1.158445 | 0.611581 |
| `gptqmodel` | `wikitext2` | 8 | 760 | 24.675866 | 31.952564 | 1.294891 | 0.611091 |
| `gptqmodel` | `c4` | 8 | 727 | 32.951664 | 39.809985 | 1.208133 | 0.609741 |

## Failures

- none

## Claim Boundary

- Valid claim: official-package readiness probes are presented in one aligned matrix for the same model family, W-bit/group-size shape, and tiny public eval labels. Invalid claim: this matrix proves AWQ/GPTQ competitiveness, SOTA PTQ quality, task retention, or production runtime readiness.
