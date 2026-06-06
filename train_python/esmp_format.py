from __future__ import annotations

"""Python reader/dequantizer for the ESMPQ001 mixed-precision package format."""

import struct
from pathlib import Path

try:
    import numpy as np
except ModuleNotFoundError:  # pragma: no cover - checked by callers at runtime
    np = None

try:
    import torch
except ModuleNotFoundError:  # pragma: no cover - checked by callers at runtime
    torch = None


MAGIC = b"ESMPQ001"
VERSION = 1
HEADER_BYTES = 64
ROW_META_BYTES = 24
SIGNED_SYMMETRIC_PER_ROW = 1


class EsmpMatrix:
    def __init__(
        self,
        rows: int,
        cols: int,
        row_bits,
        row_scales,
        row_bit_offsets,
        payload: bytes,
        data_bytes: int,
        path: Path,
    ) -> None:
        self.rows = rows
        self.cols = cols
        self.row_bits = row_bits
        self.row_scales = row_scales
        self.row_bit_offsets = row_bit_offsets
        self.payload = payload
        self.data_bytes = data_bytes
        self.path = path

    @property
    def avg_bits(self) -> float:
        return float(self.row_bits.astype(np.float64).mean()) if self.rows else 0.0

    @property
    def bit_histogram(self) -> dict[str, int]:
        unique, counts = np.unique(self.row_bits, return_counts=True)
        return {str(int(bit)): int(count) for bit, count in zip(unique, counts)}

    @property
    def raw_fp32_bytes(self) -> int:
        return int(self.rows * self.cols * 4)

    @property
    def package_bytes(self) -> int:
        return int(HEADER_BYTES + self.rows * ROW_META_BYTES + self.data_bytes)

    @property
    def compression_vs_fp32(self) -> float:
        return self.raw_fp32_bytes / max(float(self.package_bytes), 1.0)


def _require_numpy() -> None:
    if np is None:
        raise RuntimeError("ESMP parsing requires numpy")


def _require_torch() -> None:
    if torch is None:
        raise RuntimeError("ESMP dequantization requires torch")


def read_esmp(path: Path) -> EsmpMatrix:
    _require_numpy()
    data = path.read_bytes()
    if len(data) < HEADER_BYTES:
        raise ValueError(f"ESMP file too small: {path}")
    if data[:8] != MAGIC:
        raise ValueError(f"bad ESMP magic: {path}")
    version, header_bytes = struct.unpack_from("<II", data, 8)
    if version != VERSION or header_bytes != HEADER_BYTES:
        raise ValueError(f"unsupported ESMP header: version={version} header={header_bytes}")
    rows, cols = struct.unpack_from("<QQ", data, 16)
    row_meta_offset, data_offset, data_bytes = struct.unpack_from("<QQQ", data, 32)
    (scheme,) = struct.unpack_from("<I", data, 56)
    if scheme != SIGNED_SYMMETRIC_PER_ROW:
        raise ValueError(f"unsupported ESMP quant scheme: {scheme}")
    expected_data_offset = HEADER_BYTES + int(rows) * ROW_META_BYTES
    if row_meta_offset != HEADER_BYTES or data_offset != expected_data_offset:
        raise ValueError(f"inconsistent ESMP offsets in {path}")
    if int(data_offset + data_bytes) != len(data):
        raise ValueError(f"payload length mismatch in {path}")

    row_bits = np.empty(int(rows), dtype=np.uint8)
    row_scales = np.empty(int(rows), dtype=np.float32)
    row_offsets = np.empty(int(rows), dtype=np.uint64)
    expected_bit_offset = 0
    for row in range(int(rows)):
        offset = int(row_meta_offset) + row * ROW_META_BYTES
        bits = data[offset]
        if bits < 2 or bits > 8:
            raise ValueError(f"invalid ESMP row bit width in {path}: row={row} bits={bits}")
        row_bit_offset = struct.unpack_from("<Q", data, offset + 8)[0]
        if int(row_bit_offset) != expected_bit_offset:
            raise ValueError(f"non-contiguous ESMP row bit offsets in {path}: row={row}")
        row_bits[row] = bits
        row_scales[row] = struct.unpack_from("<f", data, offset + 4)[0]
        row_offsets[row] = row_bit_offset
        expected_bit_offset += int(bits) * int(cols)
    expected_payload_bytes = (expected_bit_offset + 7) // 8
    if expected_payload_bytes != int(data_bytes):
        raise ValueError(f"ESMP payload byte count does not match row metadata in {path}")

    return EsmpMatrix(
        rows=int(rows),
        cols=int(cols),
        row_bits=row_bits,
        row_scales=row_scales,
        row_bit_offsets=row_offsets,
        payload=data[int(data_offset) :],
        data_bytes=int(data_bytes),
        path=path,
    )


def _decode_int4_row(row_bytes, cols: int):
    low = row_bytes & np.uint8(0x0F)
    high = row_bytes >> np.uint8(4)
    out = np.empty(cols, dtype=np.int8)
    out[0::2] = low.astype(np.int8)
    out[1::2] = high[: len(out[1::2])].astype(np.int8)
    out[out >= 8] -= np.int8(16)
    return out


def _decode_generic_row(payload: bytes, bit_offset: int, bits: int, cols: int):
    values = np.empty(cols, dtype=np.int8)
    sign = 1 << (bits - 1)
    full = 1 << bits
    for col in range(cols):
        encoded = 0
        start = bit_offset + col * bits
        for bit in range(bits):
            absolute = start + bit
            one = (payload[absolute // 8] >> (absolute % 8)) & 1
            encoded |= one << bit
        values[col] = encoded - full if encoded & sign else encoded
    return values


def dequantize_esmp_weight(esmp: EsmpMatrix):
    _require_numpy()
    _require_torch()
    weight = np.empty((esmp.rows, esmp.cols), dtype=np.float32)
    payload_u8 = np.frombuffer(esmp.payload, dtype=np.uint8)
    for row in range(esmp.rows):
        bits = int(esmp.row_bits[row])
        bit_offset = int(esmp.row_bit_offsets[row])
        byte_offset = bit_offset // 8
        if bits == 8 and bit_offset % 8 == 0:
            q = payload_u8[byte_offset : byte_offset + esmp.cols].view(np.int8).astype(np.float32)
        elif bits == 4 and bit_offset % 8 == 0:
            nbytes = (esmp.cols + 1) // 2
            q = _decode_int4_row(payload_u8[byte_offset : byte_offset + nbytes], esmp.cols).astype(np.float32)
        else:
            q = _decode_generic_row(esmp.payload, bit_offset, bits, esmp.cols).astype(np.float32)
        weight[row, :] = q * float(esmp.row_scales[row])
    return torch.from_numpy(weight)
