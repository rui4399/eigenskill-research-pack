#!/usr/bin/env bash
set -euo pipefail

export NVIDIA_SMI_PATH="${NVIDIA_SMI_PATH:-/usr/lib/wsl/lib/nvidia-smi}"
export PYTHONUNBUFFERED=1

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

DATE_TAG="${DATE_TAG:-2026_06_07}"
HF_MODEL="${HF_MODEL:-Qwen/Qwen2.5-1.5B-Instruct}"
AWQ_MODEL="${AWQ_MODEL:-/home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07}"
MMLU_JSONL="data_eval/public_task_benchmark_v1/mmlu_abstract_algebra_test_subset100.jsonl"
GSM8K_JSONL="data_eval/public_task_benchmark_v1/gsm8k_test_subset100.jsonl"

run_case() {
  local variant="$1"
  local loader="$2"
  local model="$3"
  local format="$4"
  local task_jsonl="$5"
  local max_new="$6"
  local lower_variant lower_format out_prefix
  lower_variant="$(echo "$variant" | tr '[:upper:]' '[:lower:]')"
  lower_format="$(echo "$format" | tr '[:upper:]' '[:lower:]')"
  out_prefix="official_ptq_task_${lower_variant}_qwen25_1p5b_${lower_format}_subset100"

  python3 train_python/run_with_gpu_guard.py \
    --max-memory-ratio 0.90 \
    --max-start-memory-ratio 0.90 \
    --max-length-ceiling 0 \
    --poll-seconds 2 \
    --timeout-sec 3600 \
    --cleanup-repo-caches \
    --cleanup-root . \
    --min-disk-free-gb 2 \
    --disk-check-path /home/rui \
    --out "outputs/${out_prefix}_gpu_guard_${DATE_TAG}.json" \
    python3 train_python/eval_chat_task_benchmark.py \
      --tasks-jsonl "$task_jsonl" \
      --task-format "$lower_format" \
      --model "$model" \
      --loader "$loader" \
      --device cuda \
      --dtype float16 \
      --max-new-tokens "$max_new" \
      --max-seq-len 512 \
      --limit 100 \
      --chat-template \
      --no-think \
      --local-files-only \
      --out-json "outputs/${out_prefix}_summary_${DATE_TAG}.json" \
      --out-md "outputs/OFFICIAL_PTQ_TASK_${variant}_QWEN25_1P5B_${format}_SUBSET100_${DATE_TAG}.md"
}

run_case "FP16" "hf" "$HF_MODEL" "MMLU" "$MMLU_JSONL" 16
run_case "FP16" "hf" "$HF_MODEL" "GSM8K" "$GSM8K_JSONL" 64
run_case "AWQ" "autoawq" "$AWQ_MODEL" "MMLU" "$MMLU_JSONL" 16
run_case "AWQ" "autoawq" "$AWQ_MODEL" "GSM8K" "$GSM8K_JSONL" 64
