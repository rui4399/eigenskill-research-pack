# EigenSkill-Q RTX 3090 Experiment Pack

This USB pack is designed to run from either:

- Windows: `E:\eigenskill-rtx3090-experiments-2026-06-16`
- WSL: `/mnt/e/eigenskill-rtx3090-experiments-2026-06-16`

## What is included

- repo source for the experiment code
- task fixtures and prompt pools
- paper-facing docs and runbooks
- selected outputs used as evidence
- WSL/Windows bootstrap scripts under `scripts_3090/`

## What is not included

- model weights
- `.git`
- local build caches
- CodeGraph index cache

## First run

### In WSL

```bash
cd /mnt/e/eigenskill-rtx3090-experiments-2026-06-16
bash scripts_3090/run_rtx3090_env_guard.sh
```

### In Windows PowerShell

```powershell
Set-Location E:\eigenskill-rtx3090-experiments-2026-06-16
powershell -ExecutionPolicy Bypass -File scripts_3090\run_rtx3090_env_guard.ps1
```

The PowerShell wrapper checks whether the USB drive is visible inside WSL. If a
removable drive such as `E:` is not mounted at `/mnt/e`, it mounts the drive via
`drvfs` using WSL root and then runs the Linux launcher. If WSL still cannot
see the path, it falls back to native Windows Python.

## What the scripts do

- auto-detect repo root from the script location
- work on Windows or WSL without hard-coded path edits
- check `nvidia-smi`, Python, Torch, and CUDA availability
- write `outputs/RTX3090_ENV_GUARD_YYYY_MM_DD.md/json`
- report git branch/commit and runtime paths
- read `PACK_METADATA.json` when `.git` is absent from the USB pack
- provide a staged 3090 experiment ladder under `scripts_3090/`

## Experiment ladder

See `scripts_3090/RTX3090_EXPERIMENT_LADDER.md`.

WSL:

```bash
cd /mnt/e/eigenskill-rtx3090-experiments-2026-06-16
STAGE=p1 TASK_LIMIT=25 bash scripts_3090/run_rtx3090_experiment_ladder.sh
```

PowerShell:

```powershell
Set-Location E:\eigenskill-rtx3090-experiments-2026-06-16
$env:STAGE='p1'
$env:TASK_LIMIT='25'
powershell -ExecutionPolicy Bypass -File scripts_3090\run_rtx3090_experiment_ladder.ps1
```

Model weights are intentionally not on the USB. On the RTX 3090 machine, set
`RTX3090_FP16_MODEL`, `RTX3090_AWQ_MODEL`, `RTX3090_GPTQ_MODEL`, or
`RTX3090_14B_AWQ_MODEL` to local model directories before running non-P0
stages.

## Suggested 3090 order

1. Environment guard
2. 7B smoke
3. matched subset gate
4. CSI `n=4/8/16` on a second prompt pool
5. 14B quantized smoke
