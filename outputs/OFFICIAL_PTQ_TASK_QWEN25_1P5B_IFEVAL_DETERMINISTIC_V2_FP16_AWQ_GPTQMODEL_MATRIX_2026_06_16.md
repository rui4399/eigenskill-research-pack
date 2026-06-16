# Qwen2.5-1.5B Deterministic IFEval FP16/AutoAWQ/GPTQModel Matrix

Date: `2026-06-16T05:31:25+00:00`
Status: **PASS**

## Summary

- variants: `['autoawq', 'fp16', 'gptqmodel']`
- task formats: `['ifeval']`
- total tasks across cases: `24`
- total passes across cases: `1`
- max accuracy drop vs `fp16`: `0.0000`
- zero-accuracy baseline formats: `['ifeval']`
- peak guard VRAM ratio: `0.8762`

## Cases

| variant | format | tasks | passes | accuracy | mean tok/s | mean TTFT s | peak VRAM | source |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fp16` | `ifeval` | 8 | 0 | 0.0000 | 24.1735 | 0.261944 | 0.8762 | `outputs/official_ptq_task_fp16_qwen25_1p5b_ifeval_deterministic_v2_summary_2026_06_16.json` |
| `autoawq` | `ifeval` | 8 | 1 | 0.1250 | 18.2283 | 0.548219 | 0.4977 | `outputs/official_ptq_task_autoawq_qwen25_1p5b_ifeval_deterministic_v2_summary_2026_06_13.json` |
| `gptqmodel` | `ifeval` | 8 | 0 | 0.0000 | 15.3932 | 0.528889 | 0.4542 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_ifeval_deterministic_v2_summary_2026_06_13.json` |

## Comparisons Against Baseline

| variant | format | baseline accuracy | quant accuracy | drop |
|---|---|---:|---:|---:|
| `autoawq` | `ifeval` | 0.0000 | 0.1250 | -0.1250 |
| `gptqmodel` | `ifeval` | 0.0000 | 0.0000 | 0.0000 |

## Failures

- none

## Claim Boundary

- Valid claim: FP16 and official-package quantized artifacts are loadable and evaluated on the same 8-row deterministic IFEval-style fixture under GPU guard. Formats with zero FP16 accuracy are execution-only evidence. Invalid claim: this is leaderboard-scale task retention, SOTA PTQ quality, or a production inference benchmark.
