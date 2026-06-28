#!/usr/bin/env bash
set -euo pipefail

cd /mnt/e/eigenskill-rtx3090-experiments-2026-06-16

export HF_HOME=/mnt/e/hf_cache
export HF_HUB_CACHE=/mnt/e/hf_cache/hub
export TRANSFORMERS_CACHE=/mnt/e/hf_cache/transformers
export XDG_CACHE_HOME=/mnt/e/cache
export TMPDIR=/mnt/e/tmp
export TEMP=/mnt/e/tmp
export TMP=/mnt/e/tmp

mkdir -p /mnt/e/hf_cache/hub /mnt/e/hf_cache/transformers /mnt/e/cache /mnt/e/models /mnt/e/tmp

/home/dell/anaconda3/envs/zr3090/bin/python3 scripts_3090/download_hf_snapshot.py \
  --repo-id Qwen/Qwen2.5-7B-Instruct \
  --local-dir /mnt/e/models/Qwen2.5-7B-Instruct \
  --cache-dir /mnt/e/hf_cache/hub \
  --max-workers 8
