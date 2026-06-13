# Qwen2.5-1.5B Partial IFEval Execution Evidence

Date: `2026-06-13`

Status: **PARTIAL / NON-GATE**

This artifact records a guarded attempt to broaden Qwen2.5-1.5B official PTQ
task evidence from MMLU/GSM8K into deterministic IFEval-style tasks. It is not
counted in the current `75 / 75` evidence ledger because the matched FP16 row
did not complete.

## Summary

| variant | tasks | passes | accuracy | mean tok/s | mean TTFT s | guard rc | timeout | peak VRAM | source |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `autoawq` | 8 | 1 | 0.1250 | 18.2283 | 0.548219 | 0 | false | 0.4977 | `outputs/official_ptq_task_autoawq_qwen25_1p5b_ifeval_deterministic_v2_summary_2026_06_13.json` |
| `gptqmodel` | 8 | 0 | 0.0000 | 15.3932 | 0.528889 | 0 | false | 0.4542 | `outputs/official_ptq_task_gptqmodel_qwen25_1p5b_ifeval_deterministic_v2_summary_2026_06_13.json` |
| `fp16` | n/a | n/a | n/a | n/a | n/a | -15 | true | 0.2860 | `outputs/official_ptq_task_fp16_qwen25_1p5b_ifeval_deterministic_v2_gpu_guard_2026_06_13.json` |

## Interpretation

- AutoAWQ and GPTQModel Qwen2.5-1.5B artifacts loaded and executed the same
  8-row deterministic IFEval fixture under GPU guard.
- The FP16 row did not finish. The guarded command timed out after `2400`
  seconds with low GPU utilization and low VRAM use, consistent with waiting on
  incomplete Hugging Face cache/model materialization rather than running
  generation.
- This is execution-path evidence for the quantized local packages and a
  concrete blocker for the matched FP16 IFEval row.

## Claim Boundary

Valid claim:

```text
AutoAWQ and GPTQModel Qwen2.5-1.5B local artifacts can execute the deterministic
8-row IFEval-style fixture under the existing GPU guard; the matched FP16 row is
not yet complete.
```

Invalid claims:

- this is a matched FP16/AutoAWQ/GPTQModel retention matrix;
- this proves IFEval retention;
- this proves statistical superiority, SOTA PTQ quality, production runtime,
  mobile deployment, or energy savings.

## Next Step

Materialize a complete local FP16 Qwen2.5-1.5B cache or point the FP16 loader to
a complete local snapshot, then rerun the same fixture and promote the result
through `train_python/gate_official_ptq_task_retention.py` only if all required
cases pass.

