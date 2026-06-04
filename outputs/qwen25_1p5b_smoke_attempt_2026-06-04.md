# Qwen2.5-1.5B Smoke Attempt

This is a failed-at-download attempt, not a model result.

## Command

```bash
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
python3 train_python/eval_weight_quant_ppl.py \
  --model Qwen/Qwen2.5-1.5B-Instruct \
  --prompts data_eval/text_prompts/wikitext2_validation_128.txt \
  --limit-prompts 16 \
  --max-length 128 \
  --group-size 128 \
  --config-json data_eval/eval_configs/qwen25_uniform_group128.json \
  --out outputs/qwen25_1p5b_fake_quant_ppl_uniform_group128_wikitext2_16_summary.json
```

## Observed State

```text
GPU: NVIDIA GeForce RTX 5070 Laptop GPU, 8151 MiB total
local cached Qwen models before attempt: Qwen2.5-0.5B-Instruct only
Qwen2.5-1.5B cache after ~13 minutes: 322 MB
largest incomplete blob: 325157245 bytes
output summary file produced: no
```

The process was terminated after the cache stopped progressing for several
polls. The script did not reach model loading or PPL evaluation, so no 1.5B PPL
claim should be made from this attempt.

## Next Action

Use one of these before rerunning the 1.5B smoke:

```text
1. authenticate Hugging Face with HF_TOKEN for faster/more reliable download;
2. pre-download Qwen/Qwen2.5-1.5B-Instruct through huggingface-cli;
3. use a local mirror or already-cached stronger model.
```

Once cached, rerun the same command and commit the resulting JSON only if it
contains completed FP16/uniform-INT4/uniform-INT3 metrics.
