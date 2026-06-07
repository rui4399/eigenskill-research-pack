# Official PTQ IFEval Deterministic V2 Execution Matrix

Date: `2026-06-07T08:48:16+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['ifeval']`
- total tasks across cases: `24`
- total passes across cases: `2`
- max accuracy drop vs `fp16`: `-0.1250`
- zero-accuracy baseline formats: `['ifeval']`
- peak guard VRAM ratio: `0.5113`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `ifeval` | 8 | 0 | 0.0000 | 30.6348 | 0.264942 | 0.5113 | `outputs/official_ptq_task_fp16_ifeval_v2_summary_2026_06_07.json` |
| `autoawq` | `ifeval` | 8 | 1 | 0.1250 | 6.7130 | 0.586322 | 0.4536 | `outputs/official_ptq_task_awq_ifeval_v2_summary_2026_06_07.json` |
| `gptqmodel` | `ifeval` | 8 | 1 | 0.1250 | 12.3554 | 0.425140 | 0.4518 | `outputs/official_ptq_task_gptqmodel_ifeval_v2_summary_2026_06_07.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `ifeval` | 0.0000 | 0.1250 | -0.1250 |
| `gptqmodel` | `ifeval` | 0.0000 | 0.1250 | -0.1250 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same deterministic IFEval-style instruction-following v2 tasks under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
