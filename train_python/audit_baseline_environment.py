#!/usr/bin/env python3
from __future__ import annotations

import importlib.metadata
import importlib.util
import json
import platform
import subprocess
import sys
from pathlib import Path


PACKAGES = [
    "auto_gptq",
    "awq",
    "llmcompressor",
    "optimum",
    "bitsandbytes",
    "gptqmodel",
    "transformers",
    "torch",
]


def package_status(name: str) -> dict:
    found = importlib.util.find_spec(name) is not None
    version = ""
    if found:
        try:
            version = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            version = ""
    return {"name": name, "available": found, "version": version}


def run_command(command: list[str]) -> dict:
    try:
        proc = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
        return {
            "command": command,
            "returncode": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        }
    except Exception as error:  # pragma: no cover - diagnostic path
        return {"command": command, "error": str(error)}


def torch_status() -> dict:
    if importlib.util.find_spec("torch") is None:
        return {"available": False}
    import torch

    return {
        "available": True,
        "version": getattr(torch, "__version__", ""),
        "cuda_available": bool(torch.cuda.is_available()),
        "cuda_version": getattr(torch.version, "cuda", ""),
        "device_count": int(torch.cuda.device_count()) if torch.cuda.is_available() else 0,
        "device_names": [
            torch.cuda.get_device_name(index) for index in range(torch.cuda.device_count())
        ]
        if torch.cuda.is_available()
        else [],
    }


def markdown_report(data: dict) -> str:
    lines = [
        "# Baseline Environment Audit",
        "",
        "This audit records whether public quantization baseline packages are",
        "available in the current WSL Python environment. It does not install",
        "packages or mutate the environment.",
        "",
        "## Python",
        "",
        f"- executable: `{data['python']['executable']}`",
        f"- version: `{data['python']['version']}`",
        f"- platform: `{data['python']['platform']}`",
        "",
        "## Torch/CUDA",
        "",
        f"- torch available: `{data['torch']['available']}`",
        f"- torch version: `{data['torch'].get('version', '')}`",
        f"- cuda available: `{data['torch'].get('cuda_available', False)}`",
        f"- cuda version: `{data['torch'].get('cuda_version', '')}`",
        f"- devices: `{data['torch'].get('device_names', [])}`",
        "",
        "## Baseline Packages",
        "",
        "| package | available | version |",
        "|---|---:|---|",
    ]
    for item in data["packages"]:
        lines.append(f"| `{item['name']}` | {item['available']} | `{item['version']}` |")
    lines.extend(
        [
            "",
            "## NVIDIA-SMI",
            "",
            "```text",
            data.get("nvidia_smi", {}).get("stdout", "") or data.get("nvidia_smi", {}).get("stderr", ""),
            "```",
            "",
            "## Interpretation",
            "",
            "If GPTQ/AWQ/SmoothQuant-style packages are unavailable, claims must stay",
            "limited to the repository's fake-quant diagnostics until a pinned baseline",
            "environment is installed and evaluated.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    out_json = Path("outputs/baseline_environment_audit.json")
    out_md = Path("outputs/baseline_environment_audit.md")
    data = {
        "python": {
            "executable": sys.executable,
            "version": sys.version.replace("\n", " "),
            "platform": platform.platform(),
        },
        "packages": [package_status(name) for name in PACKAGES],
        "torch": torch_status(),
        "nvidia_smi": run_command(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total,driver_version",
                "--format=csv,noheader",
            ]
        ),
    }
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    out_md.write_text(markdown_report(data), encoding="utf-8")
    print(json.dumps({"out_json": str(out_json), "out_md": str(out_md)}, indent=2))


if __name__ == "__main__":
    main()
