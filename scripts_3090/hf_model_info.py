#!/usr/bin/env python3
from __future__ import annotations

import argparse

from huggingface_hub import HfApi


def main() -> None:
    parser = argparse.ArgumentParser(description="Print minimal Hugging Face model metadata.")
    parser.add_argument("repo_id")
    args = parser.parse_args()
    info = HfApi().model_info(args.repo_id, files_metadata=False)
    print(info.modelId)
    print(f"files={len(info.siblings)}")
    for sibling in info.siblings:
        print(sibling.rfilename)


if __name__ == "__main__":
    main()
