# Qwen2.5-7B Quantizer Baseline Summary

Generated: 2026-07-09

This closes the reviewer-facing strong-quantizer baseline slot for the 7B sprint slice. AWQ is recorded as an external checkpoint baseline; GPTQ is recorded as an environment/schema blocker rather than silently omitted.

## Downstream Retention

| Task | Method | Exact / 100 | Accuracy | Role |
|---|---|---:|---:|---|
| MMLU100 | fp16 | 65 | 0.65 | upper reference |
| MMLU100 | uniform_int4 | 63 | 0.63 | equal-bit local fake-quant reference |
| MMLU100 | awq_int4_checkpoint | 64 | 0.64 | external quantizer baseline |
| GSM8K100 | fp16 | 4 | 0.04 | upper reference |
| GSM8K100 | uniform_int4 | 5 | 0.05 | equal-bit local fake-quant reference |
| GSM8K100 | awq_int4_checkpoint | 2 | 0.02 | external quantizer baseline |

## Interpretation

- MMLU100: FP16 65/100, local uniform INT4 63/100, AWQ checkpoint 64/100.
- GSM8K100: FP16 4/100, local uniform INT4 5/100, AWQ checkpoint 2/100 under the current first-number scoring protocol.
- AWQ therefore strengthens the 7B baseline panel but does not change the main CSI claim boundary: 7B remains mixed scale evidence rather than universal CSI dominance.

## GPTQ Boundary

- Initial GPTQ load failed because `optimum` was missing.
- After installing `optimum`, the same checkpoint still failed with `NameError("name 'QuantizeConfig' is not defined")`.
- No GPTQ downstream number is claimed from this environment; the blocker is preserved for reproducibility.
## GPTQ Dependency Follow-up

A follow-up dependency attempt installed `gptqmodel 2.2.0+cu121torch2.5`. This moved the blocker past missing `QuantizeConfig`, but the current Windows Python 3.9 stack now fails in `gptqmodel.models._const.normalize_device` with `TypeError("unsupported operand type(s) for |: 'type' and 'EnumMeta'")`. See `qwen25_7b_gptq_dependency_blocker_2026_07_09.{json,md}`.
