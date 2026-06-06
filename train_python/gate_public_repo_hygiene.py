#!/usr/bin/env python3
from __future__ import annotations

"""Gate public-repository hygiene for paper-facing artifact branches."""

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


FORBIDDEN_SUFFIXES = (".docx", ".pdf", ".zip")
FORBIDDEN_PREFIXES = (
    "research_pack_",
    "outputs/paper_delivery_",
    "docs/obsidian_quant_route/",
    "docs/notebooklm_enterprise_sources/",
)
PLACEHOLDER_PATTERNS = (
    re.compile(r"^\s*(Base model|Skills|Key v2 metrics|Useful commands|Build on Windows|Run):\s*$", re.IGNORECASE),
    re.compile(r"\b(TODO|TBD|FIXME)\b", re.IGNORECASE),
)


def normalize_path(path: str) -> str:
    return path.replace("\\", "/").strip()


def tracked_files(root: Path) -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files"],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )
    return [normalize_path(line) for line in proc.stdout.splitlines() if line.strip()]


def find_forbidden_files(paths: Iterable[str]) -> list[str]:
    bad: list[str] = []
    for path in paths:
        normalized = normalize_path(path)
        lower = normalized.lower()
        if lower.endswith(FORBIDDEN_SUFFIXES):
            bad.append(normalized)
            continue
        if any(normalized.startswith(prefix) for prefix in FORBIDDEN_PREFIXES):
            bad.append(normalized)
    return bad


def should_scan_text(path: str) -> bool:
    normalized = normalize_path(path)
    if normalized == "README.md":
        return True
    if normalized.startswith("docs/") and normalized.endswith(".md"):
        return True
    if normalized.startswith("paper_drafts/") and normalized.endswith(".md"):
        return True
    return False


def find_placeholders(root: Path, paths: Iterable[str]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for path in paths:
        normalized = normalize_path(path)
        if not should_scan_text(normalized):
            continue
        full_path = root / normalized
        if not full_path.exists():
            continue
        try:
            lines = full_path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(lines, start=1):
            if any(pattern.search(line) for pattern in PLACEHOLDER_PATTERNS):
                findings.append({"path": normalized, "line": lineno, "text": line.strip()})
    return findings


def build_report(root: Path, paths: list[str] | None = None) -> dict[str, object]:
    files = paths if paths is not None else tracked_files(root)
    forbidden = find_forbidden_files(files)
    placeholders = find_placeholders(root, files)
    failures: list[str] = []
    if forbidden:
        failures.append(f"forbidden tracked files: {len(forbidden)}")
    if placeholders:
        failures.append(f"placeholder lines: {len(placeholders)}")
    return {
        "date": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "passed": not failures,
        "summary": {
            "tracked_file_count": len(files),
            "forbidden_file_count": len(forbidden),
            "placeholder_count": len(placeholders),
        },
        "failures": failures,
        "forbidden_files": forbidden,
        "placeholders": placeholders,
    }


def write_markdown(path: Path, report: dict[str, object]) -> None:
    status = "PASS" if report["passed"] else "FAIL"
    summary = report["summary"]
    lines = [
        "# Public Repository Hygiene Gate",
        "",
        f"Date: `{report['date']}`",
        f"Status: **{status}**",
        "",
        "## Summary",
        "",
        f"- tracked files: `{summary['tracked_file_count']}`",
        f"- forbidden tracked files: `{summary['forbidden_file_count']}`",
        f"- placeholder lines: `{summary['placeholder_count']}`",
        "",
        "## Forbidden Files",
        "",
    ]
    forbidden = report["forbidden_files"]
    if forbidden:
        lines.extend(f"- `{path}`" for path in forbidden)
    else:
        lines.append("- none")
    lines.extend(["", "## Placeholders", ""])
    placeholders = report["placeholders"]
    if placeholders:
        for item in placeholders:
            lines.append(f"- `{item['path']}:{item['line']}` {item['text']}")
    else:
        lines.append("- none")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gate public repository hygiene.")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--out-json", type=Path)
    parser.add_argument("--out-md", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    report = build_report(root)
    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        args.out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.out_md:
        write_markdown(args.out_md, report)
    print(json.dumps({"passed": report["passed"], "summary": report["summary"], "failures": report["failures"]}, indent=2))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
