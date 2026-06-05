# Hugging Face Model Predownload Report

Model: `HuggingFaceTB/SmolLM2-1.7B-Instruct`
Started: `2026-06-05 11:35:30`
Elapsed seconds: `0.00`
Status: `incomplete_cache`
Cache root: `/home/rui/.cache/huggingface/hub`

## Cache State

| metric | before | after |
|---|---:|---:|
| total bytes | 33165855082 | 33165855082 |
| file count | 48 | 48 |
| incomplete files | 2 | 2 |

## Largest After Files

| bytes | path |
|---:|---|
| 6847602688 | `blobs/023686a59a534e45af70bc5f99ae70e592481701680591f9844fc140a3db220a` |
| 6847602688 | `snapshots/31b70e2e869a7173562077fd711b654946d38674/onnx/model.onnx_data` |
| 3422777952 | `blobs/f55217be716b6a997b97b9d8d7eb6fad02e00858f5010ec24f64603c3a98a0e8` |
| 3422777952 | `snapshots/31b70e2e869a7173562077fd711b654946d38674/model.safetensors` |
| 1714119778 | `blobs/db5cb9057f4e7014f00c38fd9764f0103e60bb4d145ad600b7144625f0d56930` |
| 1714119778 | `snapshots/31b70e2e869a7173562077fd711b654946d38674/onnx/model_int8.onnx` |
| 1411969607 | `blobs/467b7b8f62d99f184d3628d24b8d65c151e331695f6e9ea997616c4e279e9a51` |
| 1411969607 | `snapshots/31b70e2e869a7173562077fd711b654946d38674/onnx/model_q4.onnx` |
| 1326807956 | `blobs/3d891d77661f6339f727b3188f1c21b1429a1e4e55c40d1f60f85048b00a4348` |
| 1326807956 | `snapshots/31b70e2e869a7173562077fd711b654946d38674/onnx/model_fp16.onnx` |

## Incomplete Files

| bytes | path |
|---:|---|
| 1024000000 | `blobs/5f48c05c14ed97738f8dc5854c20c229ddc8661f43fa914085843901a4ba8740.incomplete` |
| 65374838 | `blobs/d94946187fb5f27579f3db4ba21fb7f7466c7cbd18956bd420d3981f75282f9c.incomplete` |

## Error

```text
snapshot_download returned a path, but cache audit found 2 incomplete blob(s).
```

## Interpretation

A `success` status means `snapshot_download` completed and the cache
audit found no `.incomplete` blobs for this repo. It does not mean any
quantization or PPL evaluation has run. A `failed` or
`incomplete_cache` status is a download/cache blocker and must not be
reported as a model-quality result.
