#!/usr/bin/env python3
from __future__ import annotations

"""Triton benchmark for row-wise mixed INT4/INT8 dequantized matmul.

This is a PC-side kernel experiment, not a production transformer runtime. It
packs rows as either INT4 or INT8 and reports wall-clock latency against torch
fp16 matmul on the active CUDA device.

Two low-bit paths are reported:

* rowwise: one Triton program per output row and batch item. This is deliberately
  simple and exposes the overhead of naive dynamic mixed precision.
* grouped: split INT4 and INT8 rows into homogeneous groups and use block
  Triton dot kernels. This keeps the real packed low-bit storage but avoids a
  branch per row and gives the GPU enough tile work to amortize unpack/dequant.
"""

import argparse
import json
import time
from pathlib import Path
from statistics import median

import torch

try:
    import triton
    import triton.language as tl
except ModuleNotFoundError:  # pragma: no cover - runtime dependency
    triton = None
    tl = None


def _jit(fn):
    if triton is None:
        return fn
    return triton.jit(fn)


@_jit
def _mixed_dequant_matmul_kernel(
    x_ptr,
    q4_ptr,
    q8_ptr,
    row_bits_ptr,
    row_slots_ptr,
    scales_ptr,
    y_ptr,
    rows: tl.constexpr,
    cols: tl.constexpr,
    batch: tl.constexpr,
    stride_xb: tl.constexpr,
    block_cols: tl.constexpr,
):
    row = tl.program_id(0)
    b = tl.program_id(1)
    offsets = tl.arange(0, block_cols)
    mask = offsets < cols
    bits = tl.load(row_bits_ptr + row)
    scale = tl.load(scales_ptr + row).to(tl.float32)
    slot = tl.load(row_slots_ptr + row)
    x = tl.load(x_ptr + b * stride_xb + offsets, mask=mask, other=0.0).to(tl.float32)

    if bits == 4:
        byte_offsets = slot * ((cols + 1) // 2) + offsets // 2
        packed = tl.load(q4_ptr + byte_offsets, mask=mask, other=0).to(tl.int32)
        low = packed & 15
        high = (packed >> 4) & 15
        raw = tl.where((offsets & 1) == 0, low, high)
        q = tl.where(raw >= 8, raw - 16, raw).to(tl.float32)
    else:
        q8 = tl.load(q8_ptr + slot * cols + offsets, mask=mask, other=0).to(tl.int32)
        q = q8.to(tl.float32)

    acc = tl.sum(q * scale * x, axis=0)
    tl.store(y_ptr + b * rows + row, acc)


@_jit
def _int4_grouped_matmul_kernel(
    x_ptr,
    q4_ptr,
    row_indices_ptr,
    scales_ptr,
    y_ptr,
    group_rows: tl.constexpr,
    rows: tl.constexpr,
    cols: tl.constexpr,
    batch: tl.constexpr,
    q4_stride: tl.constexpr,
    BLOCK_M: tl.constexpr,
    BLOCK_N: tl.constexpr,
    BLOCK_K: tl.constexpr,
):
    pid_m = tl.program_id(0)
    pid_n = tl.program_id(1)
    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)
    row_ids = tl.load(row_indices_ptr + offs_m, mask=offs_m < group_rows, other=0)
    scales = tl.load(scales_ptr + row_ids, mask=offs_m < group_rows, other=0.0).to(tl.float32)
    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)

    for k0 in range(0, cols, BLOCK_K):
        k = k0 + offs_k
        packed = tl.load(
            q4_ptr + offs_m[:, None] * q4_stride + (k[None, :] // 2),
            mask=(offs_m[:, None] < group_rows) & (k[None, :] < cols),
            other=0,
        ).to(tl.int32)
        low = packed & 15
        high = (packed >> 4) & 15
        raw = tl.where((k[None, :] & 1) == 0, low, high)
        signed = tl.where(raw >= 8, raw - 16, raw).to(tl.float32)
        w = (signed * scales[:, None]).to(tl.float16)
        x = tl.load(
            x_ptr + offs_n[:, None] * cols + k[None, :],
            mask=(offs_n[:, None] < batch) & (k[None, :] < cols),
            other=0.0,
        ).to(tl.float16)
        acc += tl.dot(w, tl.trans(x))

    tl.store(
        y_ptr + offs_n[None, :] * rows + row_ids[:, None],
        acc,
        mask=(offs_m[:, None] < group_rows) & (offs_n[None, :] < batch),
    )


@_jit
def _int8_grouped_matmul_kernel(
    x_ptr,
    q8_ptr,
    row_indices_ptr,
    scales_ptr,
    y_ptr,
    group_rows: tl.constexpr,
    rows: tl.constexpr,
    cols: tl.constexpr,
    batch: tl.constexpr,
    BLOCK_M: tl.constexpr,
    BLOCK_N: tl.constexpr,
    BLOCK_K: tl.constexpr,
):
    pid_m = tl.program_id(0)
    pid_n = tl.program_id(1)
    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)
    row_ids = tl.load(row_indices_ptr + offs_m, mask=offs_m < group_rows, other=0)
    scales = tl.load(scales_ptr + row_ids, mask=offs_m < group_rows, other=0.0).to(tl.float32)
    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)

    for k0 in range(0, cols, BLOCK_K):
        k = k0 + offs_k
        q = tl.load(
            q8_ptr + offs_m[:, None] * cols + k[None, :],
            mask=(offs_m[:, None] < group_rows) & (k[None, :] < cols),
            other=0,
        ).to(tl.float32)
        w = (q * scales[:, None]).to(tl.float16)
        x = tl.load(
            x_ptr + offs_n[:, None] * cols + k[None, :],
            mask=(offs_n[:, None] < batch) & (k[None, :] < cols),
            other=0.0,
        ).to(tl.float16)
        acc += tl.dot(w, tl.trans(x))

    tl.store(
        y_ptr + offs_n[None, :] * rows + row_ids[:, None],
        acc,
        mask=(offs_m[:, None] < group_rows) & (offs_n[None, :] < batch),
    )


@_jit
def _int4_selected_matmul_kernel(
    x_ptr,
    q4_ptr,
    q4_slots_ptr,
    row_ids_ptr,
    out_pos_ptr,
    scales_ptr,
    y_ptr,
    group_rows: tl.constexpr,
    selected_rows: tl.constexpr,
    cols: tl.constexpr,
    batch: tl.constexpr,
    q4_stride: tl.constexpr,
    BLOCK_M: tl.constexpr,
    BLOCK_N: tl.constexpr,
    BLOCK_K: tl.constexpr,
):
    pid_m = tl.program_id(0)
    pid_n = tl.program_id(1)
    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)
    q4_slots = tl.load(q4_slots_ptr + offs_m, mask=offs_m < group_rows, other=0)
    row_ids = tl.load(row_ids_ptr + offs_m, mask=offs_m < group_rows, other=0)
    out_pos = tl.load(out_pos_ptr + offs_m, mask=offs_m < group_rows, other=0)
    scales = tl.load(scales_ptr + row_ids, mask=offs_m < group_rows, other=0.0).to(tl.float32)
    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)

    for k0 in range(0, cols, BLOCK_K):
        k = k0 + offs_k
        packed = tl.load(
            q4_ptr + q4_slots[:, None] * q4_stride + (k[None, :] // 2),
            mask=(offs_m[:, None] < group_rows) & (k[None, :] < cols),
            other=0,
        ).to(tl.int32)
        low = packed & 15
        high = (packed >> 4) & 15
        raw = tl.where((k[None, :] & 1) == 0, low, high)
        signed = tl.where(raw >= 8, raw - 16, raw).to(tl.float32)
        w = (signed * scales[:, None]).to(tl.float16)
        x = tl.load(
            x_ptr + offs_n[:, None] * cols + k[None, :],
            mask=(offs_n[:, None] < batch) & (k[None, :] < cols),
            other=0.0,
        ).to(tl.float16)
        acc += tl.dot(w, tl.trans(x))

    tl.store(
        y_ptr + offs_n[None, :] * selected_rows + out_pos[:, None],
        acc,
        mask=(offs_m[:, None] < group_rows) & (offs_n[None, :] < batch),
    )


@_jit
def _int8_selected_matmul_kernel(
    x_ptr,
    q8_ptr,
    q8_slots_ptr,
    row_ids_ptr,
    out_pos_ptr,
    scales_ptr,
    y_ptr,
    group_rows: tl.constexpr,
    selected_rows: tl.constexpr,
    cols: tl.constexpr,
    batch: tl.constexpr,
    BLOCK_M: tl.constexpr,
    BLOCK_N: tl.constexpr,
    BLOCK_K: tl.constexpr,
):
    pid_m = tl.program_id(0)
    pid_n = tl.program_id(1)
    offs_m = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offs_n = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    offs_k = tl.arange(0, BLOCK_K)
    q8_slots = tl.load(q8_slots_ptr + offs_m, mask=offs_m < group_rows, other=0)
    row_ids = tl.load(row_ids_ptr + offs_m, mask=offs_m < group_rows, other=0)
    out_pos = tl.load(out_pos_ptr + offs_m, mask=offs_m < group_rows, other=0)
    scales = tl.load(scales_ptr + row_ids, mask=offs_m < group_rows, other=0.0).to(tl.float32)
    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)

    for k0 in range(0, cols, BLOCK_K):
        k = k0 + offs_k
        q = tl.load(
            q8_ptr + q8_slots[:, None] * cols + k[None, :],
            mask=(offs_m[:, None] < group_rows) & (k[None, :] < cols),
            other=0,
        ).to(tl.float32)
        w = (q * scales[:, None]).to(tl.float16)
        x = tl.load(
            x_ptr + offs_n[:, None] * cols + k[None, :],
            mask=(offs_n[:, None] < batch) & (k[None, :] < cols),
            other=0.0,
        ).to(tl.float16)
        acc += tl.dot(w, tl.trans(x))

    tl.store(
        y_ptr + offs_n[None, :] * selected_rows + out_pos[:, None],
        acc,
        mask=(offs_m[:, None] < group_rows) & (offs_n[None, :] < batch),
    )


def pack_int4(weight: torch.Tensor, scales: torch.Tensor) -> torch.Tensor:
    rows, cols = weight.shape
    q = torch.round(weight / scales[:, None]).clamp(-7, 7).to(torch.int16)
    encoded = torch.where(q < 0, q + 16, q).to(torch.uint8)
    if cols % 2:
        encoded = torch.nn.functional.pad(encoded, (0, 1))
    low = encoded[:, 0::2]
    high = encoded[:, 1::2] << 4
    return (low | high).contiguous()


def pack_int8(weight: torch.Tensor, scales: torch.Tensor) -> torch.Tensor:
    return torch.round(weight / scales[:, None]).clamp(-127, 127).to(torch.int8).contiguous()


def synchronize() -> None:
    if torch.cuda.is_available():
        torch.cuda.synchronize()


def time_ms(fn, iters: int, warmup: int) -> float:
    for _ in range(warmup):
        fn()
    synchronize()
    start = time.perf_counter()
    for _ in range(iters):
        fn()
    synchronize()
    return (time.perf_counter() - start) * 1000.0 / max(iters, 1)


def time_ms_samples(fn, iters: int, warmup: int, repeats: int) -> list[float]:
    return [time_ms(fn, iters, warmup) for _ in range(max(repeats, 1))]


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark Triton row-wise mixed INT4/INT8 matmul.")
    parser.add_argument("--rows", type=int, default=2048)
    parser.add_argument("--cols", type=int, default=1024)
    parser.add_argument("--batch", type=int, default=1)
    parser.add_argument("--high-every", type=int, default=16)
    parser.add_argument("--iters", type=int, default=100)
    parser.add_argument("--warmup", type=int, default=20)
    parser.add_argument("--repeats", type=int, default=1)
    parser.add_argument("--block-m", type=int, default=16)
    parser.add_argument("--block-n", type=int, default=16)
    parser.add_argument("--block-k", type=int, default=64)
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    if triton is None or tl is None:
        raise SystemExit("missing dependency: pip install triton")
    if not torch.cuda.is_available():
        raise SystemExit("CUDA is required for this Triton benchmark")

    device = torch.device("cuda")
    torch.manual_seed(20260605)
    weight = torch.randn(args.rows, args.cols, device=device, dtype=torch.float16) * 0.04
    x = torch.randn(args.batch, args.cols, device=device, dtype=torch.float16)
    row_bits = torch.full((args.rows,), 4, device=device, dtype=torch.uint8)
    row_bits[:: args.high_every] = 8
    qmax = torch.where(row_bits == 8, torch.tensor(127.0, device=device), torch.tensor(7.0, device=device))
    scales = weight.abs().amax(dim=1).float().clamp_min(1.0e-8) / qmax
    low_rows = torch.nonzero(row_bits == 4, as_tuple=False).flatten()
    high_rows = torch.nonzero(row_bits == 8, as_tuple=False).flatten()
    row_slots = torch.empty((args.rows,), device=device, dtype=torch.int32)
    row_slots[low_rows] = torch.arange(low_rows.numel(), device=device, dtype=torch.int32)
    row_slots[high_rows] = torch.arange(high_rows.numel(), device=device, dtype=torch.int32)
    q4 = pack_int4(weight[low_rows].float(), scales[low_rows]).to(device)
    q8 = pack_int8(weight[high_rows].float(), scales[high_rows]).to(device)
    y_mixed = torch.empty(args.batch, args.rows, device=device, dtype=torch.float32)
    y_grouped = torch.empty(args.batch, args.rows, device=device, dtype=torch.float32)

    def run_mixed() -> None:
        grid = (args.rows, args.batch)
        _mixed_dequant_matmul_kernel[grid](
            x,
            q4,
            q8,
            row_bits,
            row_slots,
            scales,
            y_mixed,
            args.rows,
            args.cols,
            args.batch,
            args.cols,
            triton.next_power_of_2(args.cols),
            num_warps=8,
        )

    def run_fp16() -> None:
        torch.matmul(x, weight.t())

    def run_grouped() -> None:
        if low_rows.numel():
            grid4 = (triton.cdiv(low_rows.numel(), args.block_m), triton.cdiv(args.batch, args.block_n))
            _int4_grouped_matmul_kernel[grid4](
                x,
                q4,
                low_rows,
                scales,
                y_grouped,
                low_rows.numel(),
                args.rows,
                args.cols,
                args.batch,
                q4.shape[1],
                args.block_m,
                args.block_n,
                args.block_k,
                num_warps=4,
            )
        if high_rows.numel():
            grid8 = (triton.cdiv(high_rows.numel(), args.block_m), triton.cdiv(args.batch, args.block_n))
            _int8_grouped_matmul_kernel[grid8](
                x,
                q8,
                high_rows,
                scales,
                y_grouped,
                high_rows.numel(),
                args.rows,
                args.cols,
                args.batch,
                args.block_m,
                args.block_n,
                args.block_k,
                num_warps=4,
            )

    mixed_samples = time_ms_samples(run_mixed, args.iters, args.warmup, args.repeats)
    grouped_samples = time_ms_samples(run_grouped, args.iters, args.warmup, args.repeats)
    fp16_samples = time_ms_samples(run_fp16, args.iters, args.warmup, args.repeats)
    mixed_ms = median(mixed_samples)
    grouped_ms = median(grouped_samples)
    fp16_ms = median(fp16_samples)
    ref = torch.matmul(x.float(), weight.float().t())
    run_mixed()
    run_grouped()
    rowwise_rel_l2 = torch.linalg.vector_norm(y_mixed - ref) / torch.linalg.vector_norm(ref).clamp_min(1.0e-12)
    grouped_rel_l2 = torch.linalg.vector_norm(y_grouped - ref) / torch.linalg.vector_norm(ref).clamp_min(1.0e-12)
    grouped_vs_rowwise_rel_l2 = torch.linalg.vector_norm(y_grouped - y_mixed) / torch.linalg.vector_norm(y_mixed).clamp_min(1.0e-12)
    mixed_payload_bytes = int(q4.numel() + q8.numel() + row_bits.numel() + row_slots.numel() * 4 + scales.numel() * 4)
    fp16_bytes = int(weight.numel() * 2)
    result = {
        "rows": args.rows,
        "cols": args.cols,
        "batch": args.batch,
        "high_every": args.high_every,
        "low_rows": int(low_rows.numel()),
        "high_rows": int(high_rows.numel()),
        "rowwise_mixed_ms": mixed_ms,
        "grouped_mixed_ms": grouped_ms,
        "torch_fp16_ms": fp16_ms,
        "rowwise_mixed_ms_samples": mixed_samples,
        "grouped_mixed_ms_samples": grouped_samples,
        "torch_fp16_ms_samples": fp16_samples,
        "timing_repeats": max(args.repeats, 1),
        "rowwise_speedup_vs_torch_fp16": fp16_ms / mixed_ms if mixed_ms > 0 else None,
        "grouped_speedup_vs_torch_fp16": fp16_ms / grouped_ms if grouped_ms > 0 else None,
        "grouped_speedup_vs_rowwise": mixed_ms / grouped_ms if grouped_ms > 0 else None,
        "rowwise_rel_l2": float(rowwise_rel_l2.detach().cpu()),
        "grouped_rel_l2": float(grouped_rel_l2.detach().cpu()),
        "grouped_vs_rowwise_rel_l2": float(grouped_vs_rowwise_rel_l2.detach().cpu()),
        "block_m": args.block_m,
        "block_n": args.block_n,
        "block_k": args.block_k,
        "mixed_payload_bytes": mixed_payload_bytes,
        "fp16_weight_bytes": fp16_bytes,
        "compression_ratio_vs_fp16": fp16_bytes / max(mixed_payload_bytes, 1),
        "device": torch.cuda.get_device_name(0),
        "max_memory_allocated_mib": torch.cuda.max_memory_allocated() / (1024 * 1024),
    }
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
