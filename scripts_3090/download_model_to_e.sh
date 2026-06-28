#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 REPO_ID LOCAL_NAME" >&2
  exit 2
fi

REPO_ID="$1"
LOCAL_NAME="$2"

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
  --repo-id "$REPO_ID" \
  --local-dir "/mnt/e/models/$LOCAL_NAME" \
  --cache-dir /mnt/e/hf_cache/hub \
  --max-workers 8
