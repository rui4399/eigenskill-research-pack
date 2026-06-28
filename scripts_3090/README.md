# scripts_3090

These launchers are WSL-aware and Windows-aware.

## Use from WSL

```bash
cd /mnt/e/eigenskill-rtx3090-experiments-2026-06-16
bash scripts_3090/run_rtx3090_env_guard.sh
```

## Use from Windows

```powershell
Set-Location E:\eigenskill-rtx3090-experiments-2026-06-16
powershell -ExecutionPolicy Bypass -File scripts_3090\run_rtx3090_env_guard.ps1
```

If the USB drive is not already mounted in WSL, the PowerShell launcher mounts
the drive with `drvfs` before calling the Bash launcher.

## Design rules

- no absolute repo paths inside the scripts
- no model weights copied to USB
- outputs are written under the pack's own `outputs/`
- WSL paths and Windows paths both resolve from the script location

## Experiment ladder

Detailed runbook: `RTX3090_EXPERIMENT_LADDER.md`

```bash
STAGE=p0 bash scripts_3090/run_rtx3090_experiment_ladder.sh
STAGE=p1 TASK_LIMIT=25 bash scripts_3090/run_rtx3090_experiment_ladder.sh
STAGE=p2 TASK_LIMIT=100 bash scripts_3090/run_rtx3090_experiment_ladder.sh
```

For non-P0 stages, set model paths on the target machine:

```bash
export RTX3090_FP16_MODEL=/path/to/Qwen2.5-7B-Instruct
export RTX3090_AWQ_MODEL=/path/to/qwen25-7b-awq
export RTX3090_GPTQ_MODEL=/path/to/qwen25-7b-gptq
```
