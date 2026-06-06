# Official AutoAWQ Smoke Summary

Date: `2026-06-06T20:42:27+00:00`
Status: **PASS**
Model: `Qwen/Qwen2.5-0.5B-Instruct`
Package: `autoawq 0.2.9`
Quant config: `{'zero_point': True, 'q_group_size': 128, 'w_bit': 4, 'version': 'GEMM'}`
Calibration samples: `4`
Elapsed seconds: `85.514`

## Artifact

- path: `outputs/official_awq_smoke_2026_06_07/qwen25_0p5b_awq_model`
- files: `6`
- bytes: `469809733`
- suffix counts: `{'.jinja': 1, '.json': 4, '.safetensors': 1}`

## Generation Smoke

- ok: `True`
- prompt: `Give one short reason calibration robustness matters.`
- text: `Give one short reason calibration robustness matters. Calibration is a critical aspect of the measurement process because it involves`

## Claim Boundary

- This is a minimal official AutoAWQ execution smoke, not a competitive AWQ benchmark.
- Quantized weights are local ignored artifacts; only this summary is intended for GitHub.
