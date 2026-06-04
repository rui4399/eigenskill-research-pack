# Hugging Face Model Predownload Report

Model: `Qwen/Qwen2.5-0.5B-Instruct`
Started: `2026-06-04 21:10:04`
Elapsed seconds: `0.00`
Status: `success`
Cache root: `/home/rui/.cache/huggingface/hub`

## Cache State

| metric | before | after |
|---|---:|---:|
| total bytes | 1999172734 | 1999172734 |
| file count | 19 | 19 |
| incomplete files | 0 | 0 |

## Largest After Files

| bytes | path |
|---:|---|
| 988097824 | `blobs/fdf756fa7fcbe7404d5c60e26bff1a0c8b8aa1f72ced49e7dd0210fe288fb7fe` |
| 988097824 | `snapshots/7ae557604adf67be50417f59c2c2f167def9a775/model.safetensors` |
| 7031645 | `blobs/443909a61d429dff23010e5bddd28ff530edda00` |
| 7031645 | `snapshots/7ae557604adf67be50417f59c2c2f167def9a775/tokenizer.json` |
| 2776833 | `blobs/4783fe10ac3adce15ac8f358ef5462739852c569` |
| 2776833 | `snapshots/7ae557604adf67be50417f59c2c2f167def9a775/vocab.json` |
| 1671839 | `blobs/20024bfe7c83998e9aeaf98a0cd6a2ce6306c2f0` |
| 1671839 | `snapshots/7ae557604adf67be50417f59c2c2f167def9a775/merges.txt` |
| 7305 | `blobs/07bfe0640cb5a0037f9322287fbfc682806cf672` |
| 7305 | `snapshots/7ae557604adf67be50417f59c2c2f167def9a775/tokenizer_config.json` |

## Interpretation

A `success` status means `snapshot_download` completed and the cache
audit found no `.incomplete` blobs for this repo. It does not mean any
quantization or PPL evaluation has run. A `failed` or
`incomplete_cache` status is a download/cache blocker and must not be
reported as a model-quality result.
