from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

try:
    import numpy as np
except ModuleNotFoundError:  # pragma: no cover
    np = None

import verify_esmp_package as verifier
from test_esmp_format import _fixture_bytes


def write_fixture_package(root: Path, bad_manifest_rows: bool = False) -> Path:
    package = root / "fixture.esmp"
    manifest = root / "fixture.json"
    summary = root / "pack_summary.json"
    package.write_bytes(_fixture_bytes())
    manifest_payload = {
        "format": "ESMPQ001",
        "version": 1,
        "quantization": "signed_symmetric_per_row_mixed_lowbit",
        "rows": 3 if bad_manifest_rows else 2,
        "cols": 4,
        "avg_bits": 6.0,
        "raw_fp32_bytes": 32,
        "packed_payload_bytes": 6,
        "row_metadata_bytes": 48,
        "total_package_bytes": 118,
        "compression_ratio_vs_fp32": 32 / 118,
        "row_bits_histogram": {"4": 1, "8": 1},
        "binary_path": str(package),
        "verify_requested": True,
        "verify_gemv_rel_l2": 0.0,
        "verify_ok": True,
    }
    manifest.write_text(json.dumps(manifest_payload), encoding="utf-8")
    summary.write_text(
        json.dumps(
            {
                "model": "fixture-model",
                "method": "fixture-method",
                "modules": [
                    {
                        "module": "fixture.linear",
                        "bits": 4,
                        "rows": 2,
                        "cols": 4,
                        "out": str(package),
                        "manifest": str(manifest),
                        "packer": {
                            "ok": True,
                            "format": "ESMPQ001",
                            "rows": 2,
                            "cols": 4,
                            "total_package_bytes": 118,
                            "verify_ok": True,
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return summary


@unittest.skipIf(np is None, "numpy is required")
class VerifyEsmpPackageTests(unittest.TestCase):
    def test_verifies_summary_manifest_and_binary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            summary = write_fixture_package(Path(tmp))
            report = verifier.verify_summary(summary, min_checked=1, min_compression_vs_fp32=0.1)
            self.assertTrue(report["passed"])
            self.assertEqual(report["checked_module_count"], 1)
            self.assertEqual(report["failed_module_count"], 0)

    def test_manifest_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            summary = write_fixture_package(Path(tmp), bad_manifest_rows=True)
            report = verifier.verify_summary(summary, min_checked=1)
            self.assertFalse(report["passed"])
            self.assertEqual(report["failed_module_count"], 1)
            self.assertIn("module metadata mismatches", report["failures"][0])

    def test_missing_files_are_counted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            summary = root / "pack_summary.json"
            summary.write_text(
                json.dumps(
                    {
                        "model": "fixture-model",
                        "method": "fixture-method",
                        "modules": [
                            {
                                "module": "missing.linear",
                                "out": str(root / "missing.esmp"),
                                "manifest": str(root / "missing.json"),
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            report = verifier.verify_summary(summary, min_checked=0, max_missing=0)
            self.assertFalse(report["passed"])
            self.assertEqual(report["missing_file_count"], 2)


if __name__ == "__main__":
    unittest.main()
