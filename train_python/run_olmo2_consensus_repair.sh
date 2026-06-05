#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

cmake --build build/cpp-wsl -j2

python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.85 \
  --poll-seconds 2 \
  --out outputs/olmo2_0425_1b_consensus_vs_random16_gpu_guard_c4_64.json \
  -- \
  python3 train_python/eval_weight_quant_ppl.py \
    --model allenai/OLMo-2-0425-1B-Instruct \
    --prompts data_eval/text_prompts/c4_en_validation_64.txt \
    --limit-prompts 64 \
    --max-length 160 \
    --device cuda \
    --dtype float16 \
    --group-size 128 \
    --reuse-model \
    --config-json data_eval/eval_configs/olmo2_0425_1b_consensus_vs_random16_compare.json \
    --out outputs/olmo2_0425_1b_consensus_vs_random16_ppl_c4_64_summary.json

python3 train_python/run_with_gpu_guard.py \
  --max-memory-ratio 0.85 \
  --poll-seconds 2 \
  --out outputs/olmo2_0425_1b_consensus_vs_random16_gpu_guard_wikitext2_64.json \
  -- \
  python3 train_python/eval_weight_quant_ppl.py \
    --model allenai/OLMo-2-0425-1B-Instruct \
    --prompts data_eval/text_prompts/wikitext2_validation_128.txt \
    --limit-prompts 64 \
    --max-length 160 \
    --device cuda \
    --dtype float16 \
    --group-size 128 \
    --reuse-model \
    --config-json data_eval/eval_configs/olmo2_0425_1b_consensus_vs_random16_compare.json \
    --out outputs/olmo2_0425_1b_consensus_vs_random16_ppl_wikitext2_64_summary.json

build/cpp-wsl/quant_evidence_matrix \
  --target wikitext_c4_consensus \
  --input outputs/olmo2_0425_1b_consensus_vs_random16_ppl_wikitext2_64_summary.json \
  --dataset olmo2_consensus_vs_random16_wikitext2_64 \
  --input outputs/olmo2_0425_1b_consensus_vs_random16_ppl_c4_64_summary.json \
  --dataset olmo2_consensus_vs_random16_c4_64 \
  --emit markdown \
  > outputs/olmo2_0425_1b_consensus_vs_random16_evidence_matrix.md

build/cpp-wsl/quant_evidence_matrix \
  --target wikitext_c4_consensus \
  --input outputs/olmo2_0425_1b_consensus_vs_random16_ppl_wikitext2_64_summary.json \
  --dataset olmo2_consensus_vs_random16_wikitext2_64 \
  --input outputs/olmo2_0425_1b_consensus_vs_random16_ppl_c4_64_summary.json \
  --dataset olmo2_consensus_vs_random16_c4_64 \
  --emit csv \
  > outputs/olmo2_0425_1b_consensus_vs_random16_evidence_matrix.csv

sed -n '1,80p' outputs/olmo2_0425_1b_consensus_vs_random16_evidence_matrix.md

