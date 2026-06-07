# Official AutoAWQ Smoke Summary

Date: `2026-06-07T11:52:11+00:00`
Status: **PASS**
Model: `Qwen/Qwen2.5-1.5B-Instruct`
Package: `autoawq 0.2.9`
Quant config: `{'zero_point': True, 'q_group_size': 128, 'w_bit': 4, 'version': 'GEMM'}`
Calibration samples: `4`
Calibration source: `['data_eval/public_calib_prompts_2026_06_07/wikitext2_test_ppl_prompts.txt', 'data_eval/public_calib_prompts_2026_06_07/c4_validation_ppl_prompts.txt']`
Expected AWQ calibration blocks: `2`
Accepted calibration tokens: `381`
Elapsed seconds: `263.273`

## Artifact

- path: `/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07`
- files: `6`
- bytes: `1159233350`
- suffix counts: `{'.jinja': 1, '.safetensors': 1, '.json': 4}`

## Generation Smoke

- ok: `True`
- prompt: `Give one short reason calibration robustness matters.`
- text: `Give one short reason calibration robustness matters. Calibration is the process of adjusting a model`

## Claim Boundary

- This is a minimal official AutoAWQ execution smoke, not a competitive AWQ benchmark.
- Quantized weights are local ignored artifacts; only this summary is intended for GitHub.
