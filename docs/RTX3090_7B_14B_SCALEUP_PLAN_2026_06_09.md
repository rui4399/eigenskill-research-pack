# RTX 3090 7B/14B Scale-Up Plan

Date: 2026-06-09

This note defines the next local scale-up path for EigenSkill-Q once an RTX
3090-class 24 GB GPU is available. It is a public experiment plan, not evidence
that the runs have already been completed.

## Purpose

The current paper-facing spine is Calibration Split Instability (CSI) for
mixed-precision LLM quantization. Larger-model runs should serve that spine:

```text
Do module-sensitivity rankings remain unstable at 7B/14B scale, and can
cross-split consensus reduce noisy bit-allocation decisions under the same
budget?
```

The scale-up work should therefore prioritize matched diagnostics and claim
boundaries over raw benchmark chasing.

## Hardware Assumption

The planned environment is:

```text
GPU: NVIDIA RTX 3090
VRAM: 24 GB
OS/runtime: Windows or WSL with CUDA
```

The first artifact for any scale-up run should be an environment guard:

```text
outputs/RTX3090_ENV_GUARD_2026_MM_DD.md
outputs/rtx3090_env_guard_2026_mm_dd.json
```

Minimum contents:

- GPU name and VRAM;
- driver and CUDA versions;
- Python, PyTorch, Transformers, AutoAWQ, GPTQModel, and any runtime backend
  versions;
- model identifiers and local artifact paths;
- guard threshold and observed peak VRAM.

## Realistic Boundary

7B models are the first target. FP16 or BF16 may be practical for short
batch-1 guarded evaluations, while W4/W8 paths are more appropriate for
throughput and memory comparisons.

14B models should start with quantized inference only. A full FP16 14B baseline
is not a default single-3090 target because weights alone are roughly above the
24 GB budget before KV cache and runtime overhead.

## Execution Ladder

### P0: Environment Guard

Run no long benchmark until the environment guard is written.

Required checks:

```text
nvidia-smi
torch.cuda.is_available()
torch.cuda.get_device_name(0)
torch.cuda.get_device_properties(0).total_memory
```

Boundary:

- this proves environment readiness only;
- it is not model-quality, retention, or runtime evidence.

### P1: 7B Smoke

Run a minimal 7B smoke before any full fixture:

- one FP16/BF16 or native baseline path if it fits;
- one quantized path, such as AWQ, GPTQ, GGUF, or another explicitly named
  backend;
- 10 to 50 task rows;
- batch size 1;
- short, fixed prompts.

Required outputs:

```text
outputs/RTX3090_7B_SMOKE_MATRIX_2026_MM_DD.md
outputs/rtx3090_7b_smoke_matrix_2026_mm_dd.json
outputs/RTX3090_7B_SMOKE_RUNTIME_PROFILE_2026_MM_DD.md
outputs/rtx3090_7b_smoke_runtime_profile_2026_mm_dd.json
```

Boundary:

- smoke proves loading and execution only;
- it is not leaderboard-scale retention;
- it is not a production runtime claim.

### P2: 7B Matched Subset

After smoke passes, run matched subsets:

- GSM8K 100 or 200 rows;
- MMLU Broad5x20 or Broad10x20;
- identical task fixtures across variants;
- matrix, runtime profile, and statistics artifacts.

Recommended names:

```text
outputs/OFFICIAL_PTQ_TASK_QWEN25_7B_MMLU_BROAD10X20_FP16_AWQ_GPTQMODEL_MATRIX_2026_MM_DD.md
outputs/OFFICIAL_PTQ_QWEN25_7B_MMLU_BROAD10X20_FP16_AWQ_GPTQMODEL_RUNTIME_PROFILE_2026_MM_DD.md
outputs/OFFICIAL_PTQ_TASK_QWEN25_7B_MMLU_BROAD10X20_FP16_AWQ_GPTQMODEL_STATISTICS_2026_MM_DD.md
```

Boundary:

- matched subset evidence can support local retention and runtime discussion;
- it is not full MMLU unless all 57 subjects and all rows are run;
- it is not official leaderboard evidence.

### P3: 7B CSI-vs-n

The first scale-up experiment that directly strengthens the CSI paper should
measure calibration-size sensitivity at 7B:

- calibration sizes such as n=4, n=8, and n=16;
- at least four deterministic seeds, preferably six if runtime permits;
- Spearman rank correlation;
- top-k Jaccard;
- positive-set Jaccard;
- bootstrap gain intervals;
- permutation null and Holm adjustment when comparing size pairs.

Expected artifact family:

```text
outputs/CSI_VS_N_CURVE_QWEN25_7B_2026_MM_DD.md
outputs/CSI_TREND_SIGNIFICANCE_QWEN25_7B_2026_MM_DD.md
outputs/CSI_NULL_PERMUTATION_QWEN25_7B_2026_MM_DD.md
```

Boundary:

- this is calibration-ranking evidence;
- it does not by itself prove downstream task retention or production speed.

### P4: 14B Quantized Smoke

Only after 7B smoke and subset gates are stable should 14B be attempted.

Initial 14B scope:

- quantized path first;
- batch size 1;
- short context;
- 10 to 50 rows;
- explicit OOM and fallback logging.

Boundary:

- 14B quantized smoke proves feasibility of loading and guarded execution only;
- it is not full retention;
- it is not an FP16 comparison unless an FP16 baseline actually runs under the
  same guard.

### P5: 14B Matched Subset

If 14B quantized smoke is stable:

- run GSM8K 100;
- run MMLU Broad5x20;
- expand only if runtime and VRAM are stable;
- preserve all failure cases.

Boundary:

- this is scale coverage;
- it should not override the 7B CSI evidence unless it includes matching CSI
  metrics.

## Claim Rules

Allowed statements after completed 3090 gates:

- the named model and backend ran under the recorded 3090 guard;
- the artifact reports local TTFT, tokens/s, and peak VRAM;
- the matched fixture reports local accuracy or exact-match for the named rows;
- CSI metrics were measured for the named calibration sizes and seeds.

Disallowed statements without further evidence:

- state-of-the-art quantizer;
- official leaderboard quality;
- universal CSI scaling law;
- mobile deployment;
- production Tensor Core runtime;
- board-level energy improvement;
- full 14B FP16 comparison when only quantized runs fit.

## Integration Into Public Docs

After a 3090 run completes, update in this order:

1. `docs/SYSTEM_EVIDENCE_GATES.md` with the new gate row.
2. `docs/ARTIFACT_MANIFEST.md` with the artifact family.
3. `docs/PAPER_CLAIM_MATRIX.md` with an explicit allowed claim and boundary.
4. `docs/SYSTEM_EVIDENCE_RUNBOOK.md` with the reproducible command.
5. Root `README.md` only if the evidence changes the high-level status table.

