# MMLU PTQ Shard Plan: broad20x20

Date: `2026-06-07T22:49:45+00:00`
Subjects: `20`
Planned rows: `400`
Shard size: `100`

## Claim Boundary

- This is a command plan only. It proves no model quality until the fixture, shard summaries, merged summaries, GPU guard logs, and gates are produced and committed.
- Generated commands must still be run under the GPU guard before any paper-facing claim is added.

## Fixture Command

```bash
python3 train_python/build_public_task_smoke.py --out-dir data_eval/public_task_benchmark_v1 --gsm8k-count 0 --mmlu-count 0 --mmlu-count-per-subject 20 --file-tag broad20x20 --mmlu-combined-file mmlu_broad20x20_test.jsonl --title 'Public Task Benchmark MMLU broad20x20 Manifest' --claim-boundary 'Public MMLU fixture for guarded local PTQ retention; not full leaderboard evidence until all shards and gates pass.' --source datasets-server --out-json outputs/public_task_benchmark_mmlu_broad20x20_manifest_2026_06_08.json --out-md outputs/PUBLIC_TASK_BENCHMARK_MMLU_BROAD20X20_MANIFEST_2026_06_08.md --mmlu-subject abstract_algebra --mmlu-subject anatomy --mmlu-subject business_ethics --mmlu-subject clinical_knowledge --mmlu-subject college_computer_science --mmlu-subject computer_security --mmlu-subject high_school_mathematics --mmlu-subject high_school_us_history --mmlu-subject machine_learning --mmlu-subject professional_law --mmlu-subject astronomy --mmlu-subject college_biology --mmlu-subject college_chemistry --mmlu-subject college_mathematics --mmlu-subject college_medicine --mmlu-subject conceptual_physics --mmlu-subject econometrics --mmlu-subject electrical_engineering --mmlu-subject formal_logic --mmlu-subject global_facts
```

## Variant Shards

### fp16

Shard `0` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model Qwen/Qwen2.5-1.5B-Instruct --loader hf --max-new-tokens 64 --limit 100 --offset 0 --chat-template --no-think --out-json outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08.json --out-md outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08.md --hf-device-map auto --hf-max-gpu-memory-mib 2400
```

Shard `100` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model Qwen/Qwen2.5-1.5B-Instruct --loader hf --max-new-tokens 64 --limit 100 --offset 100 --chat-template --no-think --out-json outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08.json --out-md outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08.md --hf-device-map auto --hf-max-gpu-memory-mib 2400
```

Shard `200` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model Qwen/Qwen2.5-1.5B-Instruct --loader hf --max-new-tokens 64 --limit 100 --offset 200 --chat-template --no-think --out-json outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08.json --out-md outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08.md --hf-device-map auto --hf-max-gpu-memory-mib 2400
```

Shard `300` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model Qwen/Qwen2.5-1.5B-Instruct --loader hf --max-new-tokens 64 --limit 100 --offset 300 --chat-template --no-think --out-json outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08.json --out-md outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08.md --hf-device-map auto --hf-max-gpu-memory-mib 2400
```

Merge:

```bash
python3 train_python/merge_chat_task_shards.py --out-json outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json --out-md outputs/OFFICIAL_PTQ_TASK_FP16_QWEN25_1P5B_MMLU_BROAD20X20_2026_06_08.md --out-guard-json outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08.json=outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08.json=outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08.json=outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08.json=outputs/shards/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08_gpu_guard.json
```

### autoawq

Shard `0` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model /home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07 --loader autoawq --max-new-tokens 64 --limit 100 --offset 0 --chat-template --no-think --out-json outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08.json --out-md outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08.md
```

Shard `100` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model /home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07 --loader autoawq --max-new-tokens 64 --limit 100 --offset 100 --chat-template --no-think --out-json outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08.json --out-md outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08.md
```

Shard `200` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model /home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07 --loader autoawq --max-new-tokens 64 --limit 100 --offset 200 --chat-template --no-think --out-json outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08.json --out-md outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08.md
```

Shard `300` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model /home/rui/eigenskill_artifacts/qwen25_1p5b_awq_model_2026_06_07 --loader autoawq --max-new-tokens 64 --limit 100 --offset 300 --chat-template --no-think --out-json outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08.json --out-md outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08.md
```

Merge:

```bash
python3 train_python/merge_chat_task_shards.py --out-json outputs/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json --out-md outputs/OFFICIAL_PTQ_TASK_AUTOAWQ_QWEN25_1P5B_MMLU_BROAD20X20_2026_06_08.md --out-guard-json outputs/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08.json=outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08.json=outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08.json=outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08.json=outputs/shards/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08_gpu_guard.json
```

### gptqmodel

Shard `0` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model /home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08 --loader gptqmodel --max-new-tokens 64 --limit 100 --offset 0 --chat-template --no-think --out-json outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08.json --out-md outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08.md
```

Shard `100` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model /home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08 --loader gptqmodel --max-new-tokens 64 --limit 100 --offset 100 --chat-template --no-think --out-json outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08.json --out-md outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08.md
```

Shard `200` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model /home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08 --loader gptqmodel --max-new-tokens 64 --limit 100 --offset 200 --chat-template --no-think --out-json outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08.json --out-md outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08.md
```

Shard `300` + `100`:

```bash
python3 train_python/run_with_gpu_guard.py --max-memory-ratio 0.90 --max-start-memory-ratio 0.85 --min-disk-free-gb 20 --disk-check-path /home/rui --timeout-sec 1800 --out outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08_gpu_guard.json -- python3 train_python/eval_chat_task_benchmark.py --tasks-jsonl data_eval/public_task_benchmark_v1/mmlu_broad20x20_test.jsonl --task-format mmlu --model /home/rui/eigenskill_artifacts/qwen25_1p5b_gptq_model_smoke4_2026_06_08 --loader gptqmodel --max-new-tokens 64 --limit 100 --offset 300 --chat-template --no-think --out-json outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08.json --out-md outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08.md
```

Merge:

```bash
python3 train_python/merge_chat_task_shards.py --out-json outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json --out-md outputs/OFFICIAL_PTQ_TASK_GPTQMODEL_QWEN25_1P5B_MMLU_BROAD20X20_2026_06_08.md --out-guard-json outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08.json=outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_0_100_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08.json=outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_100_200_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08.json=outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_200_300_2026_06_08_gpu_guard.json --shard outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08.json=outputs/shards/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_300_400_2026_06_08_gpu_guard.json
```

## Gate Commands

### task_retention

```bash
python3 train_python/gate_official_ptq_task_retention.py --baseline-variant fp16 --required-variant fp16 --required-variant autoawq --required-variant gptqmodel --required-format mmlu --min-tasks-per-case 400 --max-memory-ratio 0.90 --max-accuracy-drop 0.1500 --matrix-title 'Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel MMLU broad20x20 task matrix' --evidence-label 'matched Qwen2.5-1.5B local MMLU broad20x20 task evidence for FP16, AutoAWQ, and GPTQModel' --out-json outputs/official_ptq_task_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_matrix_2026_06_08.json --out-md outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_BROAD20X20_FP16_AWQ_GPTQMODEL_MATRIX_2026_06_08.md --case fp16:mmlu=outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json=outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08_gpu_guard.json --case autoawq:mmlu=outputs/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json=outputs/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08_gpu_guard.json --case gptqmodel:mmlu=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08_gpu_guard.json
```

### runtime_profile

```bash
python3 train_python/gate_official_ptq_runtime_profile.py --matrix-json outputs/official_ptq_task_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_matrix_2026_06_08.json --baseline-variant fp16 --required-variant fp16 --required-variant autoawq --required-variant gptqmodel --min-cases-per-variant 1 --max-memory-ratio 0.90 --out-json outputs/official_ptq_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_runtime_profile_2026_06_08.json --out-md outputs/OFFICIAL_PTQ_QWEN25_1P5B_MMLU_BROAD20X20_FP16_AWQ_GPTQMODEL_RUNTIME_PROFILE_2026_06_08.md
```

### task_statistics

```bash
python3 train_python/gate_official_ptq_task_statistics.py --baseline-variant fp16 --min-tasks-per-case 400 --min-shared-tasks 400 --max-ci-accuracy-drop 0.1500 --bootstrap-samples 4000 --matrix-title 'Qwen2.5-1.5B FP16 vs AutoAWQ vs GPTQModel MMLU broad20x20 task statistics' --out-json outputs/official_ptq_task_qwen25_1p5b_mmlu_broad20x20_fp16_awq_gptqmodel_statistics_2026_06_08.json --out-md outputs/OFFICIAL_PTQ_TASK_QWEN25_1P5B_MMLU_BROAD20X20_FP16_AWQ_GPTQMODEL_STATISTICS_2026_06_08.md --case fp16:mmlu=outputs/official_ptq_task_fp16_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json --case autoawq:mmlu=outputs/official_ptq_task_autoawq_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json --case gptqmodel:mmlu=outputs/official_ptq_task_gptqmodel_qwen25_1p5b_mmlu_broad20x20_summary_2026_06_08.json
```
