# Baseline Environment Audit

Date: `2026-06-06T23:41:00+00:00`
Mode: `multi_environment_union`

## Merged Packages

| package | available | version | sources |
|---|---:|---|---|
| `auto_gptq` | False | `` | `windows=no:, wsl_gpu=no:` |
| `autoawq` | True | `0.2.9` | `wsl_gpu=yes:0.2.9` |
| `awq` | True | `` | `windows=no:, wsl_gpu=yes:` |
| `bitsandbytes` | False | `` | `windows=no:, wsl_gpu=no:` |
| `gptqmodel` | True | `7.0.0` | `windows=no:, wsl_gpu=yes:7.0.0` |
| `llmcompressor` | False | `` | `windows=no:, wsl_gpu=no:` |
| `optimum` | True | `2.1.0` | `windows=yes:2.1.0, wsl_gpu=no:` |
| `torch` | True | `2.12.0` | `windows=yes:2.12.0, wsl_gpu=yes:2.12.0+cu130` |
| `transformers` | True | `5.10.2` | `windows=yes:5.10.2, wsl_gpu=yes:5.8.1` |
| `triton` | True | `3.7.0` | `windows=no:, wsl_gpu=yes:3.7.0` |

## Torch/CUDA Selected For Dashboard

- source: `wsl_gpu`
- torch available: `True`
- torch version: `2.12.0+cu130`
- cuda available: `True`
- devices: `['NVIDIA GeForce RTX 5070 Laptop GPU']`

## Environments

| label | python | platform | torch | cuda |
|---|---|---|---|---:|
| `windows` | `D:\anaconda3\python.exe` | `Windows-11-10.0.26200-SP0` | `2.12.0+cpu` | False |
| `wsl_gpu` | `/mnt/d/Caches/eigenskill-venvs/gptqmodel/bin/python` | `Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35` | `2.12.0+cu130` | True |

## Interpretation

- Package availability is the union across the listed local environments. Use environment-specific audit files to determine where a package actually ran.
