# ESMPQ001 Binary Format

ESMPQ001 is the local EigenSkill-Q mixed-precision matrix package used by the
C++ packer/runtime benchmarks and the Python reconstruction/generation tools.
It is intentionally narrow: a row-major Linear weight matrix with one bit width
and one symmetric scale per output row.

This format is an experiment artifact boundary, not a general model container.

## Layout

All integer fields are little-endian.

```text
header:   64 bytes
row meta: rows * 24 bytes
payload:  packed signed integer weights
```

## Header

| offset | type | field |
|---:|---|---|
| 0 | char[8] | magic, `ESMPQ001` |
| 8 | u32 | version, currently `1` |
| 12 | u32 | header bytes, currently `64` |
| 16 | u64 | rows |
| 24 | u64 | cols |
| 32 | u64 | row metadata offset, currently `64` |
| 40 | u64 | payload offset |
| 48 | u64 | payload bytes |
| 56 | u32 | quant scheme, currently `1` |
| 60 | u32 | reserved |

Quant scheme `1` means signed symmetric per-row quantization.

## Row Metadata

Each row has a 24-byte record:

| offset in record | type | field |
|---:|---|---|
| 0 | u8 | bit width, inclusive range `[2, 8]` |
| 1 | u8 | reserved |
| 2 | u8 | reserved |
| 3 | u8 | reserved |
| 4 | f32 | row scale |
| 8 | u64 | row bit offset from start of payload |
| 16 | i32 | sum of signed quantized row values |
| 20 | u32 | reserved |

Row bit offsets must be contiguous. For row `r`, the next expected offset is:

```text
row_bit_offsets[r] + row_bits[r] * cols
```

The payload byte count must equal:

```text
ceil(total_row_bits / 8)
```

## Signed Payload Encoding

Values are stored least-significant-bit first within each row bit stream.
For a row with `b` bits, decoded unsigned value `u` maps to signed value:

```text
q = u - 2^b, if u has the sign bit set
q = u,       otherwise
```

The reconstructed weight is:

```text
w[row, col] = q[row, col] * row_scale[row]
```

## Shared Readers

- C++: `inference_cpp/include/eigenskill/esmp_format.hpp`
- Python: `train_python/esmp_format.py`

Both readers validate magic, version, dimensions, offsets, bit-width range,
contiguous row bit offsets, and payload byte count.

## Artifact Integrity Checks

The format is now checked through two runnable tools:

```bash
./build/cpp-wsl/esmp_inspect \
  --input build/cpp-wsl/mixed_precision_packer_smoke.esmp \
  --expect-rows 64 \
  --expect-cols 96 \
  --min-compression-vs-fp32 4.0 \
  --require-bits 4,8 \
  --verify-row-sums
```

`esmp_inspect` reads the binary package directly and emits JSON with dimensions,
bit histogram, payload bytes, file bytes, compression ratio, and optional row-sum
verification.

```bash
python train_python/verify_esmp_package.py \
  --summary outputs/real_system_packer_2026-06-05/qwen3_0p6b_full_esmp/pack_summary.json \
  --limit-modules 8 \
  --min-checked 8 \
  --max-missing 0
```

`verify_esmp_package.py` verifies three layers agree for each packed module:

- `pack_summary.json`;
- per-module manifest JSON emitted by `mixed_precision_packer`;
- the ESMP binary header and row metadata parsed by `train_python/esmp_format.py`.

This is an artifact-integrity check. It does not measure model quality or
latency.
