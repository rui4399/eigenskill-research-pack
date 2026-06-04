#!/usr/bin/env python3
from __future__ import annotations

"""Build one-line prompt files from public text datasets.

The fake-quant PPL evaluator accepts a plain text file with one prompt per line.
This helper creates reproducible prompt slices from datasets such as WikiText2
without hard-coding evaluation text into the repository.
"""

import argparse
import json
import re
from pathlib import Path

try:
    from datasets import load_dataset
except ModuleNotFoundError:
    load_dataset = None


def normalize_text(text: str, max_chars: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if max_chars and len(text) > max_chars:
        text = text[:max_chars].rsplit(" ", 1)[0].strip()
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="wikitext")
    parser.add_argument("--name", default="wikitext-2-raw-v1")
    parser.add_argument("--split", default="validation")
    parser.add_argument("--text-field", default="text")
    parser.add_argument("--limit", type=int, default=32)
    parser.add_argument("--min-chars", type=int, default=160)
    parser.add_argument("--max-chars", type=int, default=900)
    parser.add_argument("--out", default="data_eval/text_prompts/wikitext2_validation_32.txt")
    parser.add_argument("--streaming", action="store_true", help="stream dataset rows instead of downloading all shards")
    args = parser.parse_args()

    if load_dataset is None:
        raise SystemExit("This script requires the datasets package. Run it in the WSL Python environment.")

    dataset = load_dataset(args.dataset, args.name, split=args.split, streaming=args.streaming)
    prompts = []
    scanned = 0
    for row in dataset:
        scanned += 1
        raw = str(row.get(args.text_field, ""))
        text = normalize_text(raw, args.max_chars)
        if len(text) < args.min_chars:
            continue
        prompts.append(text)
        if args.limit and len(prompts) >= args.limit:
            break

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(prompts) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "dataset": args.dataset,
                "name": args.name,
                "split": args.split,
                "scanned_rows": scanned,
                "prompts": len(prompts),
                "min_chars": args.min_chars,
                "max_chars": args.max_chars,
                "streaming": args.streaming,
                "out": str(out),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
