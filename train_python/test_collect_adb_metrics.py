from __future__ import annotations

import argparse
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


def load_collector():
    path = Path(__file__).resolve().parents[1] / "mobile" / "redmi_k80_pro" / "collect_adb_metrics.py"
    spec = importlib.util.spec_from_file_location("collect_adb_metrics", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


collector = load_collector()


class CollectAdbMetricsTests(unittest.TestCase):
    def test_parse_devices_keeps_online_and_non_online_rows(self) -> None:
        output = "\n".join(
            [
                "List of devices attached",
                "abc123 device product:miro model:REDMI_K80_Pro device:miro transport_id:1",
                "stale offline transport_id:2",
                "blocked unauthorized transport_id:3",
            ]
        )
        devices = collector.parse_devices(output)
        self.assertEqual([device["state"] for device in devices], ["device", "offline", "unauthorized"])
        self.assertEqual(devices[0]["model"], "REDMI_K80_Pro")

    def test_requested_serial_must_be_online_to_count_as_real_device(self) -> None:
        args = argparse.Namespace(serial="stale", benchmark_command="", benchmark_timeout=1)

        def fake_run(command, timeout=30):
            if command == ["adb", "devices", "-l"]:
                return {
                    "command": command,
                    "returncode": 0,
                    "stdout": "List of devices attached\nabc123 device model:REDMI_K80_Pro\nstale offline\n",
                    "stderr": "",
                }
            raise AssertionError(f"unexpected adb command for offline serial: {command}")

        with patch.object(collector, "run_command", side_effect=fake_run):
            result = collector.collect(args)

        self.assertFalse(result["real_device_connected"])
        self.assertEqual(result["selected_serial"], "")
        self.assertEqual(result["status"], "missing_device")

    def test_parse_json_object_extracts_embedded_metrics(self) -> None:
        parsed = collector.parse_json_object('prefix {"ttft_seconds": 1.2, "tokens_per_second": 3.4} suffix')
        self.assertEqual(parsed["ttft_seconds"], 1.2)
        self.assertEqual(parsed["tokens_per_second"], 3.4)


if __name__ == "__main__":
    unittest.main()
