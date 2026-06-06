import tempfile
import unittest
from pathlib import Path

import run_with_gpu_guard as guard


class RunWithGpuGuardDiskTests(unittest.TestCase):
    def test_cleanup_repo_caches_removes_only_regenerated_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            keep = root / "train.py"
            keep.write_text("print('keep')\n", encoding="utf-8")
            pycache = root / "pkg" / "__pycache__"
            pycache.mkdir(parents=True)
            pyc = pycache / "mod.cpython-311.pyc"
            pyc.write_bytes(b"cache")
            pytest_cache = root / ".pytest_cache"
            pytest_cache.mkdir()
            (pytest_cache / "README.md").write_text("cache", encoding="utf-8")
            output_cache = root / "outputs" / "__pycache__"
            output_cache.mkdir(parents=True)
            (output_cache / "report.pyc").write_bytes(b"keep-output-cache")

            dry = guard.cleanup_repo_caches(root, dry_run=True)
            self.assertEqual(dry["target_count"], 2)
            self.assertTrue(pyc.exists())
            self.assertTrue(pytest_cache.exists())

            result = guard.cleanup_repo_caches(root)
            self.assertEqual(result["errors"], [])
            self.assertFalse(pycache.exists())
            self.assertFalse(pytest_cache.exists())
            self.assertTrue(keep.exists())
            self.assertTrue(output_cache.exists())

    def test_disk_state_reports_free_gb(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            state = guard.disk_state(Path(tmp))
        self.assertGreater(state["total_bytes"], 0)
        self.assertGreater(state["free_gb"], 0)
        self.assertIn("path", state)

    def test_timeout_expired_uses_zero_as_disabled(self) -> None:
        self.assertFalse(guard.timeout_expired(start_time=10.0, timeout_seconds=0.0, now=1000.0))
        self.assertFalse(guard.timeout_expired(start_time=10.0, timeout_seconds=30.0, now=39.9))
        self.assertTrue(guard.timeout_expired(start_time=10.0, timeout_seconds=30.0, now=40.0))

    def test_start_memory_guard_can_require_idle_gpu(self) -> None:
        busy = {"memory_used_mib": 5000, "memory_total_mib": 8151, "memory_used_ratio": 0.6134}
        idle = {"memory_used_mib": 2300, "memory_total_mib": 8151, "memory_used_ratio": 0.2822}

        self.assertFalse(guard.start_memory_allowed(busy, max_start_memory_ratio=0.45))
        self.assertTrue(guard.start_memory_allowed(idle, max_start_memory_ratio=0.45))
        self.assertTrue(guard.start_memory_allowed(busy, max_start_memory_ratio=0.0))


if __name__ == "__main__":
    unittest.main()
