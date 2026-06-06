# Baseline Environment Audit

This audit records whether public quantization baseline packages are
available in the current Python environment. It does not install
packages or mutate the environment.

## Python

- executable: `D:\anaconda3\python.exe`
- version: `3.13.9 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 19:09:58) [MSC v.1929 64 bit (AMD64)]`
- platform: `Windows-11-10.0.26200-SP0`

## Torch/CUDA

- torch available: `True`
- torch version: `2.12.0+cpu`
- cuda available: `False`
- cuda version: `None`
- devices: `[]`

## Baseline Packages

| package | available | version |
|---|---:|---|
| `auto_gptq` | False | `` |
| `awq` | False | `` |
| `llmcompressor` | False | `` |
| `optimum` | True | `2.1.0` |
| `bitsandbytes` | False | `` |
| `gptqmodel` | False | `` |
| `transformers` | True | `5.10.2` |
| `torch` | True | `2.12.0` |
| `triton` | False | `` |

## NVIDIA-SMI

```text
NVIDIA GeForce RTX 5070 Laptop GPU, 8151 MiB, 591.86
```

## Interpretation

If GPTQ/AWQ/SmoothQuant-style packages are unavailable, claims must stay
limited to the repository's fake-quant diagnostics until a pinned baseline
environment is installed and evaluated.
