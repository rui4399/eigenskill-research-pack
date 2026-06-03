# quant_v0 smoke 训练结果

日期：2026-06-03

## 目的

验证新的无泄漏量化策略数据集 `eigenskill_quant_v0` 能够进入 LoRA 训练流程，并产出可用 adapter。这个 smoke 训练不是最终模型，只是确认训练链路可运行。

## 数据

```text
data_eval/eigenskill_quant_v0/train.jsonl  900 rows
data_eval/eigenskill_quant_v0/eval.jsonl   300 rows
data_eval/eigenskill_quant_v0/test.jsonl   300 rows
```

审计：

```text
train_eval_exact_overlap = 0
train_eval_input_overlap = 0
train_test_exact_overlap = 0
train_test_input_overlap = 0
eval_test_exact_overlap = 0
eval_test_input_overlap = 0
```

## 训练命令

```bash
CUDA_VISIBLE_DEVICES=0 python3 train_python/train_lora.py \
  --model HuggingFaceTB/SmolLM2-360M-Instruct \
  --data data_eval/eigenskill_quant_v0/train.jsonl \
  --eval-data data_eval/eigenskill_quant_v0/eval.jsonl \
  --out models/eigenskill-quant-v0-smollm2-360m-lora-smoke \
  --epochs 0.3 \
  --batch-size 1 \
  --grad-accum 8 \
  --lr 1.2e-4 \
  --max-length 384 \
  --lora-r 8 \
  --lora-alpha 16
```

## 训练结果

训练完成，输出目录：

```text
models/eigenskill-quant-v0-smollm2-360m-lora-smoke
```

关键文件：

```text
adapter_config.json
adapter_model.safetensors
checkpoint-34
README.md
tokenizer.json
tokenizer_config.json
training_args.bin
```

日志路径：

```text
outputs/eigenskill_quant_v0_train_smoke.log
```

最终日志摘要：

```text
eval_loss = 1.833
eval_runtime = 27.75s
eval_samples_per_second = 10.81
eval_mean_token_accuracy = 0.6494
train_runtime = 151.9s
train_samples_per_second = 1.778
train_steps_per_second = 0.224
train_loss = 1.992
epoch = 0.3022
```

## 解释

这是一个 smoke run，只训练 0.3 epoch，所以指标不能作为模型能力结论。它证明的是：

1. WSL 侧 GPU 和 Python 训练依赖可用；
2. 新无泄漏量化策略数据集能被 `train_lora.py` 正常加载；
3. SmolLM2-360M LoRA 训练链路能完成；
4. adapter 文件能成功保存；
5. 后续可以把训练轮数提高到 1-3 epoch，并接 `eval_skills.py` 做 exact/schema 指标。

## 下一步

1. 增加 `eval_quant_policy.py`，按 JSON policy 精确匹配而不是只看 token accuracy。
2. 跑 1 epoch 正式版：`models/eigenskill-quant-v0-smollm2-360m-lora-fp16`。
3. 评估 test split，保留 no-leak audit。
4. 再进入真正的模型量化实验：RTN/GPTQ/AWQ/Sensitivity-rate-distortion allocation。
