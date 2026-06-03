#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 train_python/generate_skill_data.py \
  --out data_eval/eigenskill_v0 \
  --train-per-skill 600 \
  --eval-per-skill 120

python3 train_python/train_lora.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --data data_eval/eigenskill_v0/train.jsonl \
  --eval-data data_eval/eigenskill_v0/eval.jsonl \
  --out models/eigenskill-smollm2-360m-lora-fp16 \
  --epochs 2 \
  --batch-size 1 \
  --grad-accum 16 \
  --lr 2e-4 \
  --max-length 384

python3 train_python/eval_skills.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-fp16 \
  --data data_eval/eigenskill_v0/eval.jsonl \
  --out outputs/eigenskill_v0_eval.json

python3 train_python/export_model.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --adapter models/eigenskill-smollm2-360m-lora-fp16 \
  --out models/eigenskill-smollm2-360m-merged-fp16 \
  --precision fp16

