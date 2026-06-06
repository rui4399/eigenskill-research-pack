#!/usr/bin/env python3
from __future__ import annotations

"""Merge baseline environment audits from multiple local Python environments."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def package_key(item: dict[str, Any]) -> str:
    return str(item.get("name") or "")


def merge_packages(audits: list[tuple[str, dict[str, Any]]]) -> list[dict[str, Any]]:
    by_name: dict[str, dict[str, Any]] = {}
    for label, audit in audits:
        for item in audit.get("packages", []) or []:
            if not isinstance(item, dict):
                continue
            name = package_key(item)
            if not name:
                continue
            row = by_name.setdefault(name, {"name": name, "available": False, "version": "", "sources": []})
            available = bool(item.get("available"))
            version = str(item.get("version", ""))
            row["sources"].append({"label": label, "available": available, "version": version})
            if available and not row["available"]:
                row["available"] = True
                row["version"] = version
            elif available and not row["version"] and version:
                row["version"] = version
    return [by_name[name] for name in sorted(by_name)]


def choose_torch(audits: list[tuple[str, dict[str, Any]]]) -> dict[str, Any]:
    torch_rows = []
    for label, audit in audits:
        row = dict(audit.get("torch", {}) or {})
        row["source_label"] = label
        torch_rows.append(row)
    cuda_rows = [row for row in torch_rows if row.get("cuda_available")]
    if cuda_rows:
        return cuda_rows[0]
    available_rows = [row for row in torch_rows if row.get("available")]
    return available_rows[0] if available_rows else {"available": False}


def environments(audits: list[tuple[str, dict[str, Any]]]) -> list[dict[str, Any]]:
    rows = []
    for label, audit in audits:
        rows.append(
            {
                "label": label,
                "python": audit.get("python", {}),
                "torch": audit.get("torch", {}),
                "nvidia_smi": audit.get("nvidia_smi", {}),
            }
        )
    return rows


def merge(audits: list[tuple[str, dict[str, Any]]]) -> dict[str, Any]:
    nvidia = next((audit.get("nvidia_smi", {}) for _label, audit in audits if audit.get("nvidia_smi", {}).get("stdout")), {})
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "audit_mode": "multi_environment_union",
        "python": {
            "executable": "multi-environment",
            "version": "see environments[]",
            "platform": "see environments[]",
        },
        "packages": merge_packages(audits),
        "torch": choose_torch(audits),
        "nvidia_smi": nvidia,
        "environments": environments(audits),
        "interpretation": (
            "Package availability is the union across the listed local environments. "
            "Use environment-specific audit files to determine where a package actually ran."
        ),
    }


def write_markdown(path: Path, data: dict[str, Any]) -> None:
    lines = [
        "# Baseline Environment Audit",
        "",
        f"Date: `{data['date']}`",
        f"Mode: `{data['audit_mode']}`",
        "",
        "## Merged Packages",
        "",
        "| package | available | version | sources |",
        "|---|---:|---|---|",
    ]
    for item in data["packages"]:
        sources = ", ".join(
            f"{src['label']}={'yes' if src['available'] else 'no'}:{src['version']}"
            for src in item.get("sources", [])
        )
        lines.append(f"| `{item['name']}` | {item['available']} | `{item['version']}` | `{sources}` |")
    lines.extend(
        [
            "",
            "## Torch/CUDA Selected For Dashboard",
            "",
            f"- source: `{data['torch'].get('source_label', '')}`",
            f"- torch available: `{data['torch'].get('available', False)}`",
            f"- torch version: `{data['torch'].get('version', '')}`",
            f"- cuda available: `{data['torch'].get('cuda_available', False)}`",
            f"- devices: `{data['torch'].get('device_names', [])}`",
            "",
            "## Environments",
            "",
            "| label | python | platform | torch | cuda |",
            "|---|---|---|---|---:|",
        ]
    )
    for env in data["environments"]:
        python = env.get("python", {})
        torch = env.get("torch", {})
        lines.append(
            f"| `{env['label']}` | `{python.get('executable', '')}` | `{python.get('platform', '')}` | "
            f"`{torch.get('version', '')}` | {bool(torch.get('cuda_available'))} |"
        )
    lines.extend(["", "## Interpretation", "", f"- {data['interpretation']}"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_input(spec: str) -> tuple[str, Path]:
    if "=" not in spec:
        raise ValueError(f"input must be LABEL=PATH: {spec}")
    label, raw_path = spec.split("=", 1)
    return label.strip(), Path(raw_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge baseline environment audits.")
    parser.add_argument("--input", action="append", required=True, help="LABEL=JSON")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-md", type=Path, required=True)
    args = parser.parse_args()

    audits = [(label, load_json(path)) for label, path in map(parse_input, args.input)]
    data = merge(audits)
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(args.out_md, data)
    print(json.dumps({"out_json": str(args.out_json), "packages": len(data["packages"])}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
