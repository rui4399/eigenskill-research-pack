#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

PYTHON_BIN="${PYTHON_BIN:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  PYTHON_BIN="python"
fi

export NVIDIA_SMI_PATH="${NVIDIA_SMI_PATH:-/usr/lib/wsl/lib/nvidia-smi}"
export PYTHONUNBUFFERED=1

DATE_TAG="${DATE_TAG:-$(date +%Y_%m_%d)}"
STAGE="${STAGE:-p0}"
TASK_LIMIT="${TASK_LIMIT:-}"
MAX_MEMORY_RATIO="${MAX_MEMORY_RATIO:-0.92}"
MIN_DISK_FREE_GB="${MIN_DISK_FREE_GB:-8}"
DISK_CHECK_PATH="${DISK_CHECK_PATH:-$REPO_ROOT}"
RTX3090_FP16_MODEL="${RTX3090_FP16_MODEL:-Qwen/Qwen2.5-7B-Instruct}"
RTX3090_AWQ_MODEL="${RTX3090_AWQ_MODEL:-}"
RTX3090_GPTQ_MODEL="${RTX3090_GPTQ_MODEL:-}"
RTX3090_14B_AWQ_MODEL="${RTX3090_14B_AWQ_MODEL:-}"
MODEL_SLUG="${MODEL_SLUG:-qwen25_7b}"
MODEL_LABEL="${MODEL_LABEL:-QWEN25_7B}"

guarded() {
  "$PYTHON_BIN" train_python/run_with_gpu_guard.py \
    --max-memory-ratio "$MAX_MEMORY_RATIO" \
    --max-start-memory-ratio "$MAX_MEMORY_RATIO" \
    --poll-seconds 2 \
    --timeout-sec "${TIMEOUT_SEC:-7200}" \
    --cleanup-repo-caches \
    --cleanup-root . \
    --min-disk-free-gb "$MIN_DISK_FREE_GB" \
    --disk-check-path "$DISK_CHECK_PATH" \
    --out "$1" \
    "${@:2}"
}

task_case() {
  local variant="$1"
  local loader="$2"
  local model="$3"
  local format="$4"
  local task_jsonl="$5"
  local max_new="$6"
  local limit="$7"
  local lower_variant lower_format out_prefix
  lower_variant="$(echo "$variant" | tr '[:upper:]' '[:lower:]')"
  lower_format="$(echo "$format" | tr '[:upper:]' '[:lower:]')"
  out_prefix="rtx3090_${lower_variant}_${MODEL_SLUG}_${lower_format}_${limit}"

  guarded "outputs/${out_prefix}_gpu_guard_${DATE_TAG}.json" \
    "$PYTHON_BIN" train_python/eval_chat_task_benchmark.py \
      --tasks-jsonl "$task_jsonl" \
      --task-format "$lower_format" \
      --model "$model" \
      --loader "$loader" \
      --device cuda \
      --dtype float16 \
      --max-new-tokens "$max_new" \
      --max-seq-len 512 \
      --limit "$limit" \
      --chat-template \
      --no-think \
      --local-files-only \
      --out-json "outputs/${out_prefix}_summary_${DATE_TAG}.json" \
      --out-md "outputs/RTX3090_${variant}_${MODEL_LABEL}_${format}_${limit}_${DATE_TAG}.md"
}

run_p0() {
  bash scripts_3090/run_rtx3090_env_guard.sh
}

run_p1_7b_smoke() {
  local limit="${TASK_LIMIT:-25}"
  task_case "FP16" "hf" "$RTX3090_FP16_MODEL" "MMLU" "data_eval/public_task_benchmark_v1/mmlu_broad5x20_test.jsonl" 16 "$limit"
  task_case "FP16" "hf" "$RTX3090_FP16_MODEL" "GSM8K" "data_eval/public_task_benchmark_v1/gsm8k_test_subset100.jsonl" 64 "$limit"
  if [[ -n "$RTX3090_AWQ_MODEL" ]]; then
    task_case "AWQ" "autoawq" "$RTX3090_AWQ_MODEL" "MMLU" "data_eval/public_task_benchmark_v1/mmlu_broad5x20_test.jsonl" 16 "$limit"
    task_case "AWQ" "autoawq" "$RTX3090_AWQ_MODEL" "GSM8K" "data_eval/public_task_benchmark_v1/gsm8k_test_subset100.jsonl" 64 "$limit"
  fi
  if [[ -n "$RTX3090_GPTQ_MODEL" ]]; then
    task_case "GPTQMODEL" "gptqmodel" "$RTX3090_GPTQ_MODEL" "MMLU" "data_eval/public_task_benchmark_v1/mmlu_broad5x20_test.jsonl" 16 "$limit"
    task_case "GPTQMODEL" "gptqmodel" "$RTX3090_GPTQ_MODEL" "GSM8K" "data_eval/public_task_benchmark_v1/gsm8k_test_subset100.jsonl" 64 "$limit"
  fi
}

run_p2_7b_matched_subset() {
  TASK_LIMIT="${TASK_LIMIT:-100}"
  run_p1_7b_smoke
}

run_p3_csi_gates() {
  cat <<'EOF'
P3 CSI gates consume existing seed-stability JSON files. Set:
  CSI_N4_JSON=outputs/...
  CSI_N8_JSON=outputs/...
  CSI_N16_JSON=outputs/...
Then rerun:
  STAGE=p3 bash scripts_3090/run_rtx3090_experiment_ladder.sh
EOF
  : "${CSI_N4_JSON:?set CSI_N4_JSON}"
  : "${CSI_N8_JSON:?set CSI_N8_JSON}"
  : "${CSI_N16_JSON:?set CSI_N16_JSON}"
  "$PYTHON_BIN" train_python/gate_csi_vs_n_curve.py \
    --case "4=$CSI_N4_JSON" \
    --case "8=$CSI_N8_JSON" \
    --case "16=$CSI_N16_JSON" \
    --out-json "outputs/csi_vs_n_curve_qwen25_7b_${DATE_TAG}.json" \
    --out-md "outputs/CSI_VS_N_CURVE_QWEN25_7B_${DATE_TAG}.md"
  "$PYTHON_BIN" train_python/gate_csi_trend_significance.py \
    --case "4=$CSI_N4_JSON" \
    --case "8=$CSI_N8_JSON" \
    --case "16=$CSI_N16_JSON" \
    --out-json "outputs/csi_trend_significance_qwen25_7b_${DATE_TAG}.json" \
    --out-md "outputs/CSI_TREND_SIGNIFICANCE_QWEN25_7B_${DATE_TAG}.md"
  "$PYTHON_BIN" train_python/gate_csi_null_permutation.py \
    --case "4=$CSI_N4_JSON" \
    --case "8=$CSI_N8_JSON" \
    --case "16=$CSI_N16_JSON" \
    --out-json "outputs/csi_null_permutation_qwen25_7b_${DATE_TAG}.json" \
    --out-md "outputs/CSI_NULL_PERMUTATION_QWEN25_7B_${DATE_TAG}.md"
}

run_p4_14b_quantized_smoke() {
  : "${RTX3090_14B_AWQ_MODEL:?set RTX3090_14B_AWQ_MODEL to a local 14B quantized artifact}"
  TASK_LIMIT="${TASK_LIMIT:-10}"
  MODEL_SLUG="qwen25_14b"
  MODEL_LABEL="QWEN25_14B"
  task_case "AWQ14B" "autoawq" "$RTX3090_14B_AWQ_MODEL" "MMLU" "data_eval/public_task_benchmark_v1/mmlu_broad5x20_test.jsonl" 16 "$TASK_LIMIT"
}

case "$STAGE" in
  p0) run_p0 ;;
  p1) run_p0; run_p1_7b_smoke ;;
  p2) run_p0; run_p2_7b_matched_subset ;;
  p3) run_p3_csi_gates ;;
  p4) run_p0; run_p4_14b_quantized_smoke ;;
  all) run_p0; run_p1_7b_smoke; run_p2_7b_matched_subset ;;
  *)
    echo "Unknown STAGE=$STAGE. Use p0, p1, p2, p3, p4, or all." >&2
    exit 2
    ;;
esac
