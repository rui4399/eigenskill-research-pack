# Baseline Environment Audit

This audit records whether public quantization baseline packages are
available in the current Python environment. It does not install
packages or mutate the environment.

## Python

- executable: `/mnt/d/Caches/eigenskill-venvs/gptqmodel/bin/python`
- version: `3.10.12 (main, Mar  3 2026, 11:56:32) [GCC 11.4.0]`
- platform: `Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.35`

## Torch/CUDA

- torch available: `True`
- torch version: `2.12.0+cu130`
- cuda available: `True`
- cuda version: `13.0`
- devices: `['NVIDIA GeForce RTX 5070 Laptop GPU']`

## Baseline Packages

| package | available | version |
|---|---:|---|
| `auto_gptq` | False | `` |
| `autoawq` | True | `0.2.9` |
| `awq` | True | `` |
| `llmcompressor` | False | `` |
| `optimum` | False | `` |
| `bitsandbytes` | False | `` |
| `gptqmodel` | True | `7.0.0` |
| `transformers` | True | `5.8.1` |
| `torch` | True | `2.12.0+cu130` |
| `triton` | True | `3.7.0` |

## NVIDIA-SMI

```text
NVIDIA GeForce RTX 5070 Laptop GPU, 8151 MiB, 591.86
```

## Interpretation

If GPTQ/AWQ/SmoothQuant-style packages are unavailable, claims must stay
limited to the repository's fake-quant diagnostics until a pinned baseline
environment is installed and evaluated.
