#!/usr/bin/env python3
from __future__ import annotations

"""Collect Redmi K80 Pro ADB profile and optional on-device benchmark metrics.

The script is intentionally generic: it can collect device properties by
itself, and it can also run a caller-provided shell command that prints JSON
metrics such as TTFT, tokens/s, and peak memory. It does not claim mobile LLM
evidence unless a real device is connected and the command returns usable
metrics.
"""

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def run_command(command: list[str], timeout: int = 30) -> dict[str, Any]:
    started = time.perf_counter()
    try:
        proc = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
        return {
            "command": command,
            "returncode": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
            "wall_seconds": time.perf_counter() - started,
        }
    except subprocess.TimeoutExpired as error:
        return {
            "command": command,
            "returncode": None,
            "stdout": (error.stdout or "").strip() if isinstance(error.stdout, str) else "",
            "stderr": (error.stderr or "").strip() if isinstance(error.stderr, str) else "",
            "timeout": True,
            "wall_seconds": time.perf_counter() - started,
        }


def parse_devices(output: str) -> list[dict[str, str]]:
    devices: list[dict[str, str]] = []
    for raw_line in output.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("List of devices"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        row = {"serial": parts[0], "state": parts[1], "raw": line}
        for token in parts[2:]:
            if ":" in token:
                key, value = token.split(":", 1)
                row[key] = value
        devices.append(row)
    return devices


def adb_prefix(serial: str = "") -> list[str]:
    return ["adb", "-s", serial] if serial else ["adb"]


def adb_shell(command: str, serial: str = "", timeout: int = 30) -> dict[str, Any]:
    return run_command([*adb_prefix(serial), "shell", command], timeout=timeout)


def select_online_serial(devices: list[dict[str, str]], requested_serial: str = "") -> str:
    online = [device for device in devices if device.get("state") == "device"]
    if requested_serial:
        online_serials = {device.get("serial", "") for device in online}
        return requested_serial if requested_serial in online_serials else ""
    return online[0]["serial"] if online else ""


def collect_props(serial: str = "") -> dict[str, Any]:
    keys = [
        "ro.product.manufacturer",
        "ro.product.brand",
        "ro.product.model",
        "ro.product.marketname",
        "ro.product.device",
        "ro.product.name",
        "ro.product.vendor.model",
        "ro.product.vendor.marketname",
        "ro.product.odm.model",
        "ro.soc.model",
        "ro.hardware",
        "ro.build.version.release",
        "ro.build.version.sdk",
    ]
    props = {}
    for key in keys:
        result = adb_shell(f"getprop {key}", serial=serial)
        props[key] = result.get("stdout", "")
    return props


def parse_json_object(text: str) -> dict[str, Any]:
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end < start:
        return {}
    try:
        payload = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def collect(args: argparse.Namespace) -> dict[str, Any]:
    devices_result = run_command(["adb", "devices", "-l"], timeout=20)
    devices = parse_devices(str(devices_result.get("stdout", "")))
    selected = select_online_serial(devices, args.serial)
    result: dict[str, Any] = {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "target": "Redmi K80 Pro",
        "devices": devices,
        "requested_serial": args.serial,
        "selected_serial": selected,
        "real_device_connected": bool(selected),
        "adb_devices": devices_result,
        "claim_boundary": (
            "Valid claim only when real_device_connected=true and benchmark metrics include TTFT, tokens/s, "
            "and peak memory from a real on-device run."
        ),
    }
    if not selected:
        result["status"] = "missing_device"
        return result

    result["device_props"] = collect_props(selected)
    result["meminfo"] = adb_shell("cat /proc/meminfo | head -40", serial=selected)
    result["thermal"] = adb_shell("dumpsys thermalservice", serial=selected, timeout=20)

    if args.benchmark_command:
        bench = adb_shell(args.benchmark_command, serial=selected, timeout=args.benchmark_timeout)
        result["benchmark_command"] = bench
        result["benchmark_metrics"] = parse_json_object(str(bench.get("stdout", "")))
    else:
        result["benchmark_metrics"] = {}
    return result


def write_markdown(path: Path, result: dict[str, Any]) -> None:
    props = result.get("device_props", {}) or {}
    metrics = result.get("benchmark_metrics", {}) or {}
    lines = [
        "# Redmi K80 Pro ADB Metrics Probe",
        "",
        f"Date: `{result['date']}`",
        f"Connected: `{result['real_device_connected']}`",
        f"Selected serial: `{result.get('selected_serial', '')}`",
        "",
        "## Device",
        "",
        f"- manufacturer: `{props.get('ro.product.manufacturer', '')}`",
        f"- model: `{props.get('ro.product.model', '')}`",
        f"- device: `{props.get('ro.product.device', '')}`",
        f"- SoC: `{props.get('ro.soc.model', '')}`",
        f"- Android: `{props.get('ro.build.version.release', '')}`",
        "",
        "## Benchmark Metrics",
        "",
        "```json",
        json.dumps(metrics, ensure_ascii=False, indent=2),
        "```",
        "",
        "## Claim Boundary",
        "",
        f"- {result['claim_boundary']}",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect ADB device profile and optional benchmark metrics.")
    parser.add_argument("--serial", default="")
    parser.add_argument("--benchmark-command", default="")
    parser.add_argument("--benchmark-timeout", type=int, default=180)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    result = collect(args)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, result)
    print(json.dumps({"connected": result["real_device_connected"], "out_json": str(args.out_json)}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["real_device_connected"] else 2)


if __name__ == "__main__":
    main()
