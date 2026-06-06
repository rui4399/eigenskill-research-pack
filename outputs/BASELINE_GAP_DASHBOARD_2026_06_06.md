# Baseline Gap Dashboard

Date: `2026-06-06T12:30:21+00:00`
Status: **NOT READY** for paper claims that require external baselines
Items: `11`

## Status Counts

| status | count |
|---|---:|
| `covered` | 6 |
| `missing` | 4 |
| `partial` | 1 |

## Missing Paper Blockers

- `awq_or_gptq`
- `rotation_family`
- `allocation_family`
- `public_task_benchmarks`
- `mobile_redmi_k80_pro`

## Baseline Items

| id | family | priority | blocker | status | evidence | tasks | partial | packages | boundary |
|---|---|---|---:|---|---:|---:|---:|---|---|
| `random_budget_allocation` | in_repo_allocation | required | False | **covered** | 49 | 0 | 0 | n/a | Useful sanity baseline only; beating random does not prove method novelty. |
| `heuristic_structural_allocation` | in_repo_allocation | required | False | **covered** | 1 | 0 | 0 | n/a | Heuristic ablation, not an external SOTA comparator. |
| `consensus_vs_random_ppl` | in_repo_allocation | required | False | **covered** | 3 | 0 | 0 | n/a | Short-slice fake-quant PPL evidence only. |
| `calibration_split_instability` | calibration_robustness | required | False | **covered** | 1 | 0 | 0 | n/a | Defines the measured problem setting; not a quality-retention proof by itself. |
| `awq_or_gptq` | external_ptq | high | True | **missing** | 0 | 0 | 0 | awq=no, auto_gptq=no, gptqmodel=no, optimum=no | Needed before claiming competitiveness against common PTQ practice. |
| `rotation_family` | external_rotation | high | True | **missing** | 0 | 0 | 0 | n/a | Required before making activation/KV or outlier-mitigation claims. |
| `allocation_family` | external_allocation | high | True | **missing** | 0 | 0 | 0 | n/a | Needed before claiming algorithmic novelty in bit allocation. |
| `public_task_schema_smoke` | capability_retention | required | False | **covered** | 3 | 8 | 0 | n/a | Proves public-schema task ingestion and guarded execution only; not leaderboard-scale retention. |
| `public_task_benchmarks` | capability_retention | high | True | **partial** | 2 | 8 | 4 | n/a | Current deterministic stress gate is partial; broad public task retention is still missing. |
| `packed_kernel_shape_family` | system_kernel | required | False | **covered** | 1 | 0 | 0 | torch=yes, triton=yes | Kernel-level evidence only; not end-to-end LLM acceleration. |
| `mobile_redmi_k80_pro` | mobile_system | high | True | **missing** | 0 | 0 | 0 | n/a | No mobile deployment claim until real device logs exist. |

## Claim Boundary

- This dashboard is a gap index, not an evidence ledger.
- `NOT READY` means at least one paper-blocking external baseline, public task benchmark, or deployment claim is still missing.
- A missing row should be reported as future work unless a committed artifact is added and the dashboard is regenerated.
