# Hugging Face Model Predownload Report

Model: `Qwen/Qwen2.5-1.5B-Instruct`
Started: `2026-06-04 21:10:04`
Elapsed seconds: `0.00`
Status: `incomplete_cache`
Cache root: `/home/rui/.cache/huggingface/hub`

## Cache State

| metric | before | after |
|---|---:|---:|
| total bytes | 251056194 | 251056194 |
| file count | 24 | 24 |
| incomplete files | 1 | 1 |

## Largest After Files

| bytes | path |
|---:|---|
| 228043548 | `blobs/dd924a11b4c220f385b51ffa522daea7c9f3d850e31b162bb5661df483c6d3ee.incomplete` |
| 7031645 | `blobs/443909a61d429dff23010e5bddd28ff530edda00` |
| 7031645 | `snapshots/989aa7980e4cf806f80c7fef2b1adb7bc71aa306/tokenizer.json` |
| 2776833 | `blobs/4783fe10ac3adce15ac8f358ef5462739852c569` |
| 2776833 | `snapshots/989aa7980e4cf806f80c7fef2b1adb7bc71aa306/vocab.json` |
| 1671839 | `blobs/20024bfe7c83998e9aeaf98a0cd6a2ce6306c2f0` |
| 1671839 | `snapshots/989aa7980e4cf806f80c7fef2b1adb7bc71aa306/merges.txt` |
| 11343 | `blobs/6634c8cc3133b3848ec74b9f275acaaa1ea618ab` |
| 11343 | `snapshots/989aa7980e4cf806f80c7fef2b1adb7bc71aa306/LICENSE` |
| 7305 | `blobs/07bfe0640cb5a0037f9322287fbfc682806cf672` |

## Incomplete Files

| bytes | path |
|---:|---|
| 228043548 | `blobs/dd924a11b4c220f385b51ffa522daea7c9f3d850e31b162bb5661df483c6d3ee.incomplete` |

## Error

```text
snapshot_download returned a path, but cache audit found 1 incomplete blob(s).
```

## Interpretation

A `success` status means `snapshot_download` completed and the cache
audit found no `.incomplete` blobs for this repo. It does not mean any
quantization or PPL evaluation has run. A `failed` or
`incomplete_cache` status is a download/cache blocker and must not be
reported as a model-quality result.
