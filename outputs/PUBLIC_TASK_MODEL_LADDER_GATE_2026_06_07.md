# Public Task Model Ladder Gate

Date: `2026-06-06T19:57:34+00:00`
Status: **PASS**
Models: `2`
Total tasks: `200`
Total passes: `43`
Best model: `qwen25_7b` / `huihui_ai/qwen2.5-abliterate:7b-instruct`
Best passes: `39`
Best accuracy: `0.3900`
Peak guard VRAM ratio: `0.8865`

## Model Cases

| label | model | formats | tasks | passes | accuracy | mean tok/s | mean TTFT s | VRAM ratio | source |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `qwen35_4b` | `huihui-qwen35-4b-pmra:latest` | `gsm8k,mmlu` | 100 | 4 | 0.0400 | 83.0283 | 0.398259 | 0.8826 | `outputs/public_task_benchmark_ollama_qwen35_4b_gate_2026_06_06.json` |
| `qwen25_7b` | `huihui_ai/qwen2.5-abliterate:7b-instruct` | `gsm8k,mmlu` | 100 | 39 | 0.3900 | 21.0416 | 0.817018 | 0.8865 | `outputs/public_task_benchmark_ollama_qwen25_abliterate_7b_gate_2026_06_07.json` |

## Failures

- none

## Claim Boundary

- Valid claim: public-task evidence is reported as a guarded multi-model ladder. Invalid claim: this proves monotonic scaling, fused quantized retention, SOTA quality, or leaderboard performance.
