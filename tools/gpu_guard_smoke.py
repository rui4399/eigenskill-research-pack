#!/usr/bin/env python3
from __future__ import annotations

import time

import torch


def main() -> None:
    if not torch.cuda.is_available():
        raise SystemExit("CUDA is not available")
    tensor = torch.empty((128, 128), device="cuda")
    torch.cuda.synchronize()
    print(torch.cuda.get_device_name(0))
    print(int(tensor.numel()))
    time.sleep(0.5)


if __name__ == "__main__":
    main()
