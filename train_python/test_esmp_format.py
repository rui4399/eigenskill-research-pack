from __future__ import annotations

import struct
import tempfile
import unittest
from pathlib import Path

try:
    import numpy as np
    import torch
except ModuleNotFoundError:  # pragma: no cover
    np = None
    torch = None

from esmp_format import HEADER_BYTES, MAGIC, ROW_META_BYTES, dequantize_esmp_weight, read_esmp


def _fixture_bytes() -> bytes:
    rows = 2
    cols = 4
    row0_payload = bytes([0x0F, 0x21])  # [-1, 0, 1, 2] in signed INT4, low nibble first.
    row1_payload = bytes([254, 255, 0, 1])  # [-2, -1, 0, 1] in signed INT8.
    payload = row0_payload + row1_payload
    row_meta_offset = HEADER_BYTES
    data_offset = HEADER_BYTES + rows * ROW_META_BYTES
    header = bytearray()
    header.extend(MAGIC)
    header.extend(struct.pack("<IIQQQQQI", 1, HEADER_BYTES, rows, cols, row_meta_offset, data_offset, len(payload), 1))
    header.extend(struct.pack("<I", 0))
    assert len(header) == HEADER_BYTES

    meta = bytearray()
    meta.extend(struct.pack("<BBBBfQiI", 4, 0, 0, 0, 0.5, 0, 2, 0))
    meta.extend(struct.pack("<BBBBfQiI", 8, 0, 0, 0, 0.25, 16, -2, 0))
    assert len(meta) == rows * ROW_META_BYTES
    return bytes(header + meta + payload)


@unittest.skipIf(np is None or torch is None, "numpy and torch are required")
class EsmpFormatTest(unittest.TestCase):
    def test_read_and_dequantize_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.esmp"
            path.write_bytes(_fixture_bytes())
            esmp = read_esmp(path)

        self.assertEqual(esmp.rows, 2)
        self.assertEqual(esmp.cols, 4)
        self.assertEqual(esmp.bit_histogram, {"4": 1, "8": 1})
        self.assertAlmostEqual(esmp.avg_bits, 6.0)
        self.assertEqual(esmp.package_bytes, HEADER_BYTES + 2 * ROW_META_BYTES + 6)

        weight = dequantize_esmp_weight(esmp)
        expected = torch.tensor(
            [
                [-0.5, 0.0, 0.5, 1.0],
                [-0.5, -0.25, 0.0, 0.25],
            ],
            dtype=torch.float32,
        )
        self.assertTrue(torch.allclose(weight, expected))


if __name__ == "__main__":
    unittest.main()
