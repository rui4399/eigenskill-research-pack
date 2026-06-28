# RTX 3090 Experiment Ladder

This file is the portable runbook for the USB pack. It assumes a single RTX
3090-class 24 GB GPU and either WSL or Windows PowerShell with WSL installed.

## Stage Order

1. `p0`: environment guard only.
2. `p1`: 7B smoke on short MMLU/GSM8K slices.
3. `p2`: 7B matched subset, using the same task path with a larger limit.
4. `p3`: CSI curve gates from completed seed-stability JSON files.
5. `p4`: 14B quantized smoke only.

Do not run `p2`, `p3`, or `p4` before the environment guard has written a fresh
`outputs/RTX3090_ENV_GUARD_YYYY_MM_DD.md` file for the target machine.

## WSL First Run

```bash
cd /mnt/e/eigenskill-rtx3090-experiments-2026-06-16
bash scripts_3090/run_rtx3090_env_guard.sh
```

## PowerShell First Run

```powershell
Set-Location E:\eigenskill-rtx3090-experiments-2026-06-16
powershell -ExecutionPolicy Bypass -File scripts_3090\run_rtx3090_env_guard.ps1
```

The PowerShell script mounts the removable drive into WSL with `drvfs` when
needed.

## 7B Smoke

Set model variables on the RTX 3090 machine. Use local model paths when
possible; the USB pack does not include model weights.

```bash
export RTX3090_FP16_MODEL=/path/to/Qwen2.5-7B-Instruct
export RTX3090_AWQ_MODEL=/path/to/qwen25-7b-awq
export RTX3090_GPTQ_MODEL=/path/to/qwen25-7b-gptq
export TASK_LIMIT=25
STAGE=p1 bash scripts_3090/run_rtx3090_experiment_ladder.sh
```

If only FP16 is available, omit `RTX3090_AWQ_MODEL` and `RTX3090_GPTQ_MODEL`.

## 7B Matched Subset

```bash
export RTX3090_FP16_MODEL=/path/to/Qwen2.5-7B-Instruct
export RTX3090_AWQ_MODEL=/path/to/qwen25-7b-awq
export RTX3090_GPTQ_MODEL=/path/to/qwen25-7b-gptq
export TASK_LIMIT=100
STAGE=p2 bash scripts_3090/run_rtx3090_experiment_ladder.sh
```

## CSI Gates

Generate or copy the n=4, n=8, and n=16 seed-stability JSON files into
`outputs/`, then run:

```bash
export CSI_N4_JSON=outputs/<n4-seed-stability>.json
export CSI_N8_JSON=outputs/<n8-seed-stability>.json
export CSI_N16_JSON=outputs/<n16-seed-stability>.json
STAGE=p3 bash scripts_3090/run_rtx3090_experiment_ladder.sh
```

## 14B Quantized Smoke

```bash
export RTX3090_14B_AWQ_MODEL=/path/to/14b-awq-or-compatible-artifact
export TASK_LIMIT=10
STAGE=p4 bash scripts_3090/run_rtx3090_experiment_ladder.sh
```

## Claim Boundary

These scripts produce local evidence. They do not create official leaderboard
claims, SOTA claims, or production-runtime claims. Update the public docs only
after the relevant JSON and Markdown artifacts exist under `outputs/`.
