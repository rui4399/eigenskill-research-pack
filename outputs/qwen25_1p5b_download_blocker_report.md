# Qwen2.5-1.5B Download Blocker Report

This report records the stronger-model attempt. No 1.5B PPL result exists yet.

## What Was Added

```text
train_python/predownload_hf_model.py
```

The helper audits the Hugging Face cache before and after `snapshot_download`
and treats `.incomplete` blobs as a blocker even when `snapshot_download`
returns a snapshot path.

## Completed Cache Sanity Check

`Qwen/Qwen2.5-0.5B-Instruct` is locally complete:

```text
status: success
cache bytes: 1999172734
incomplete blobs: 0
```

Evidence:

```text
outputs/qwen25_0p5b_cache_audit_summary.json
outputs/qwen25_0p5b_cache_audit_report.md
```

## 1.5B State

`Qwen/Qwen2.5-1.5B-Instruct` is not complete:

```text
status: incomplete_cache
latest audited cache bytes: 101959673
incomplete blobs: 1
```

Observed attempts:

```text
regular unauthenticated download: stalled on the large safetensors blob
HF_HUB_ENABLE_HF_TRANSFER=1: deprecated by huggingface_hub 1.15.0
HF_XET_HIGH_PERFORMANCE=1: still did not complete in the short retry window
```

Evidence:

```text
outputs/qwen25_1p5b_smoke_attempt_2026-06-04.md
outputs/qwen25_1p5b_cache_after_stalled_download_summary.json
outputs/qwen25_1p5b_cache_after_stalled_download_report.md
outputs/qwen25_1p5b_cache_after_xet_attempt_summary.json
outputs/qwen25_1p5b_cache_after_xet_attempt_report.md
```

## Required Next Step

Before claiming stronger-model results, complete one of these:

```text
1. set HF_TOKEN in the WSL environment and rerun predownload_hf_model.py;
2. use a reliable local mirror for Qwen/Qwen2.5-1.5B-Instruct;
3. manually pre-populate the Hugging Face cache with the full snapshot.
```

Then run:

```bash
python3 train_python/predownload_hf_model.py \
  --model Qwen/Qwen2.5-1.5B-Instruct \
  --out-json outputs/qwen25_1p5b_predownload_summary.json \
  --out-md outputs/qwen25_1p5b_predownload_report.md
```

Only after that returns `status: success` and `incomplete: 0` should the 1.5B
PPL smoke be rerun.
