# Official PTQ Readiness Matrix

Date: `2026-06-07T05:16:26+00:00`
Status: **PASS**

## Summary

- packages: `['autoawq', 'gptqmodel']`
- models: `['Qwen/Qwen2.5-0.5B-Instruct']`
- quant shapes: `[{'bits': 4, 'group_size': 128}]`
- common eval labels: `['c4', 'wikitext2']`
- total eval tokens across probes: `5714`

## Matrix

| package | slice | prompts | tokens | FP16 PPL | quant PPL | ratio | peak VRAM |
|---|---|---:|---:|---:|---:|---:|---:|
| `autoawq` | `wikitext2` | 16 | 1413 | 24.590745 | 29.788817 | 1.211383 | 0.549258 |
| `autoawq` | `c4` | 16 | 1444 | 29.917597 | 35.374649 | 1.182403 | 0.567783 |
| `gptqmodel` | `wikitext2` | 16 | 1413 | 24.590745 | 30.909568 | 1.256959 | 0.574653 |
| `gptqmodel` | `c4` | 16 | 1444 | 29.917597 | 36.362052 | 1.215407 | 0.556619 |

## Failures

- none

## Claim Boundary

- Valid claim: official-package readiness probes are presented in one aligned matrix for the same model family, W-bit/group-size shape, and tiny public eval labels. Invalid claim: this matrix proves AWQ/GPTQ competitiveness, SOTA PTQ quality, task retention, or production runtime readiness.
