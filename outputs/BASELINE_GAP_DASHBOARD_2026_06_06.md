# Baseline Gap Dashboard

Date: `2026-06-07T00:17:29+00:00`
Status: **NOT READY** for paper claims that require external baselines
Items: `15`

## Status Counts

| status | count |
|---|---:|
| `covered` | 11 |
| `missing` | 1 |
| `partial` | 1 |
| `proxy_only` | 2 |

## Missing Paper Blockers

- `official_awq_gptq_competitive`
- `official_rotation_family`
- `official_allocation_family`
- `mobile_redmi_k80_pro`

## Baseline Items

| id | family | priority | blocker | status | evidence | tasks | partial | proxy | packages | boundary |
|---|---|---|---:|---|---:|---:|---:|---:|---|---|
| `random_budget_allocation` | in_repo_allocation | required | False | **covered** | 49 | 0 | 0 | 0 | n/a | Useful sanity baseline only; beating random does not prove method novelty. |
| `heuristic_structural_allocation` | in_repo_allocation | required | False | **covered** | 1 | 0 | 0 | 0 | n/a | Heuristic ablation, not an external SOTA comparator. |
| `consensus_vs_random_ppl` | in_repo_allocation | required | False | **covered** | 3 | 0 | 0 | 0 | n/a | Short-slice fake-quant PPL evidence only. |
| `calibration_split_instability` | calibration_robustness | required | False | **covered** | 1 | 0 | 0 | 0 | n/a | Defines the measured problem setting; not a quality-retention proof by itself. |
| `official_awq_smoke` | external_ptq_readiness | optional | False | **covered** | 2 | 0 | 0 | 0 | autoawq=yes | Readiness probe only: it may show that AutoAWQ can run locally, but it is not a matched AWQ baseline or quality-retention comparison. |
| `official_awq_matched_ppl_smoke` | external_ptq_readiness | optional | False | **covered** | 6 | 0 | 0 | 0 | autoawq=yes | Readiness PPL probe only: it may show same-prompt FP16-vs-AutoAWQ comparisons, but it is not a full public-dataset AWQ/GPTQ baseline. |
| `official_awq_public_calibrated_bundle` | external_ptq_readiness | optional | False | **covered** | 4 | 0 | 0 | 0 | autoawq=yes | Partial official-package readiness: it uses public calibration and public eval slices, but it is still one AutoAWQ tiny-slice bundle, not a matched AWQ/GPTQ competitive baseline. |
| `official_gptqmodel_public_calibrated_smoke` | external_ptq_readiness | optional | False | **covered** | 5 | 0 | 0 | 0 | gptqmodel=yes | Partial official-package readiness: it proves GPTQModel can quantize, save, reload, and evaluate tiny public WikiText2/C4 slices locally, but it is not a full GPTQ/AWQ competitive baseline or task-retention result. |
| `official_awq_gptq_competitive` | external_ptq | high | True | **partial** | 0 | 0 | 23 | 2 | autoawq=yes, awq=yes, auto_gptq=no, gptqmodel=yes | Smoke and proxy artifacts are useful readiness diagnostics, but they do not cover faithful official AWQ/GPTQ baseline claims without matched calibration, budget, PPL, and task comparisons. |
| `official_rotation_family` | external_rotation | high | True | **proxy_only** | 0 | 0 | 0 | 2 | n/a | Current rotation-family proxy artifacts are useful related-family diagnostics, but they do not cover faithful QuaRot/SpinQuant implementation or activation/KV quality claims. |
| `official_allocation_family` | external_allocation | high | True | **proxy_only** | 0 | 0 | 0 | 2 | n/a | Current Q-Palette-style proxy artifacts are useful related-family diagnostics, but they do not cover faithful Q-Palette/IMPQ/WINDQuant reproduction claims. |
| `public_task_schema_smoke` | capability_retention | required | False | **covered** | 3 | 8 | 0 | 0 | n/a | Proves public-schema task ingestion and guarded execution only; not leaderboard-scale retention. |
| `public_task_benchmarks` | capability_retention | high | True | **covered** | 6 | 208 | 4 | 0 | n/a | A guarded 100-row public MMLU/GSM8K subset is covered; leaderboard-scale retention and fused-model public quality remain missing. |
| `packed_kernel_shape_family` | system_kernel | required | False | **covered** | 1 | 0 | 0 | 0 | torch=yes, triton=yes | Kernel-level evidence only; not end-to-end LLM acceleration. |
| `mobile_redmi_k80_pro` | mobile_system | high | True | **missing** | 0 | 0 | 0 | 0 | n/a | No mobile deployment claim until real device logs exist. |

## Claim Boundary

- This dashboard is a gap index, not an evidence ledger.
- `NOT READY` means at least one paper-blocking external baseline, public task benchmark, or deployment claim is still missing.
- A missing row should be reported as future work unless a committed artifact is added and the dashboard is regenerated.
