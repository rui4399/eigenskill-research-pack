import argparse
from pathlib import Path

import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer, DataCollatorForSeq2Seq, Trainer, TrainingArguments
from trl import SFTTrainer


def add_completion(example):
    example["completion"] = " " + example["response"]
    example["text"] = example["prompt"] + example["completion"]
    return example


def tokenize_completion_only(example, tokenizer, max_length):
    prompt = example.get("prompt") or example.get("input") or ""
    eos = tokenizer.eos_token or ""
    completion = " " + example["response"] + eos

    prompt_ids = tokenizer(prompt, add_special_tokens=False)["input_ids"]
    completion_ids = tokenizer(completion, add_special_tokens=False)["input_ids"]
    if not completion_ids and tokenizer.eos_token_id is not None:
        completion_ids = [tokenizer.eos_token_id]
    if not completion_ids:
        raise ValueError("completion tokenization produced no tokens and tokenizer has no eos_token_id")

    if len(completion_ids) >= max_length:
        input_ids = completion_ids[-max_length:]
        labels = list(input_ids)
    else:
        prompt_budget = max_length - len(completion_ids)
        kept_prompt = prompt_ids[-prompt_budget:]
        input_ids = kept_prompt + completion_ids
        labels = [-100] * len(kept_prompt) + list(completion_ids)

    return {
        "input_ids": input_ids,
        "attention_mask": [1] * len(input_ids),
        "labels": labels,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="HuggingFaceTB/SmolLM2-360M-Instruct")
    parser.add_argument("--data", required=True)
    parser.add_argument("--eval-data", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--epochs", type=float, default=1)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--grad-accum", type=int, default=8)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--max-length", type=int, default=384)
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--no-gradient-checkpointing", action="store_true")
    parser.add_argument(
        "--completion-only-loss",
        action="store_true",
        help="Mask prompt tokens with -100 labels so LoRA learns only the JSON response tokens.",
    )
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        device_map="auto" if torch.cuda.is_available() else None,
    )
    model.config.pad_token_id = tokenizer.pad_token_id
    model.config.use_cache = False
    if not args.no_gradient_checkpointing:
        model.gradient_checkpointing_enable()

    target_modules = [
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
    ]
    peft_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=target_modules,
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    dataset = load_dataset("json", data_files={"train": args.data, "eval": args.eval_data})
    dataset = dataset.map(add_completion)

    train_args = TrainingArguments(
        output_dir=str(out),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        gradient_accumulation_steps=args.grad_accum,
        learning_rate=args.lr,
        lr_scheduler_type="cosine",
        warmup_ratio=0.03,
        logging_steps=10,
        eval_strategy="steps",
        eval_steps=100,
        save_steps=200,
        save_total_limit=2,
        seed=args.seed,
        fp16=torch.cuda.is_available(),
        bf16=False,
        gradient_checkpointing=not args.no_gradient_checkpointing,
        optim="adamw_torch",
        report_to=[],
    )

    if args.completion_only_loss:
        tokenized = dataset.map(
            lambda example: tokenize_completion_only(example, tokenizer, args.max_length),
            remove_columns=dataset["train"].column_names,
        )
        trainer = Trainer(
            model=model,
            args=train_args,
            train_dataset=tokenized["train"],
            eval_dataset=tokenized["eval"],
            data_collator=DataCollatorForSeq2Seq(
                tokenizer=tokenizer,
                model=model,
                label_pad_token_id=-100,
                pad_to_multiple_of=8 if torch.cuda.is_available() else None,
            ),
        )
    else:
        trainer = SFTTrainer(
            model=model,
            args=train_args,
            train_dataset=dataset["train"],
            eval_dataset=dataset["eval"],
        )
    trainer.train()
    trainer.save_model(str(out))
    tokenizer.save_pretrained(str(out))


if __name__ == "__main__":
    main()
