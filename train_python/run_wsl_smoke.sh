#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 train_python/generate_skill_data.py \
  --out data_eval/eigenskill_smoke \
  --train-per-skill 8 \
  --eval-per-skill 2

python3 train_python/train_lora.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --data data_eval/eigenskill_smoke/train.jsonl \
  --eval-data data_eval/eigenskill_smoke/eval.jsonl \
  --out models/eigenskill-smollm2-360m-lora-smoke \
  --epochs 1 \
  --batch-size 1 \
  --grad-accum 4 \
  --lr 2e-4 \
  --max-length 256

python3 train_python/eval_skills.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-smoke \
  --data data_eval/eigenskill_smoke/eval.jsonl \
  --out outputs/eigenskill_smoke_eval.json \
  --limit 8

