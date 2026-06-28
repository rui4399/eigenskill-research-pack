#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import platform
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class GuardResult:
    date: str
    repo_root: str
    cwd: str
    branch: str | None
    commit: str | None
    pack_metadata: dict[str, Any] | None
    is_wsl: bool
    python_executable: str
    python_version: str
    torch_available: bool
    torch_version: str | None
    torch_cuda_version: str | None
    cuda_available: bool
    gpu_name: str | None
    gpu_count: int
    gpu_total_mib: int | None
    nvidia_smi: str | None
    notes: list[str]


def _run(cmd: list[str], cwd: Path | None = None, timeout: int = 30) -> tuple[int, str]:
    try:
        proc = subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True, timeout=timeout)
        out = (proc.stdout or "") + (proc.stderr or "")
        return proc.returncode, out.strip()
    except FileNotFoundError:
        return 127, ""
    except subprocess.TimeoutExpired:
        return 124, ""


def _git(repo_root: Path, *args: str) -> str | None:
    code, out = _run(["git", *args], cwd=repo_root)
    return out if code == 0 and out else None


def _pack_metadata(repo_root: Path) -> dict[str, Any] | None:
    path = repo_root / "PACK_METADATA.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"error": f"could not read PACK_METADATA.json: {exc}"}


def _torch_info() -> tuple[bool, str | None, str | None, bool, str | None, int, int | None]:
    try:
        import torch  # type: ignore

        cuda_available = bool(torch.cuda.is_available())
        gpu_name = torch.cuda.get_device_name(0) if cuda_available else None
        gpu_count = int(torch.cuda.device_count()) if cuda_available else 0
        gpu_total_mib = int(torch.cuda.get_device_properties(0).total_memory / (1024 * 1024)) if cuda_available else None
        return True, str(torch.__version__), str(getattr(torch.version, "cuda", None)), cuda_available, gpu_name, gpu_count, gpu_total_mib
    except Exception:
        return False, None, None, False, None, 0, None


def _is_wsl() -> bool:
    if platform.system().lower() != "linux":
        return False
    try:
        return "microsoft" in Path("/proc/version").read_text(encoding="utf-8", errors="ignore").lower()
    except Exception:
        return False


def build_result(repo_root: Path) -> GuardResult:
    notes: list[str] = []
    pack_metadata = _pack_metadata(repo_root)
    code, smi = _run(["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"], cwd=repo_root)
    if code != 0:
        smi = None
        notes.append("nvidia-smi unavailable")

    torch_available, torch_version, torch_cuda_version, cuda_available, gpu_name, gpu_count, gpu_total_mib = _torch_info()
    if not torch_available:
        notes.append("torch unavailable")
    elif not cuda_available:
        notes.append("torch CUDA unavailable")

    branch = _git(repo_root, "rev-parse", "--abbrev-ref", "HEAD")
    commit = _git(repo_root, "rev-parse", "HEAD")
    if branch is None and isinstance(pack_metadata, dict):
        branch = pack_metadata.get("source", {}).get("branch")
    if commit is None and isinstance(pack_metadata, dict):
        commit = pack_metadata.get("source", {}).get("commit")
    return GuardResult(
        date=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        repo_root=str(repo_root),
        cwd=str(Path.cwd()),
        branch=branch,
        commit=commit,
        pack_metadata=pack_metadata,
        is_wsl=_is_wsl(),
        python_executable=str(Path(__import__("sys").executable)),
        python_version=platform.python_version(),
        torch_available=torch_available,
        torch_version=torch_version,
        torch_cuda_version=torch_cuda_version,
        cuda_available=cuda_available,
        gpu_name=gpu_name,
        gpu_count=gpu_count,
        gpu_total_mib=gpu_total_mib,
        nvidia_smi=smi,
        notes=notes,
    )


def write_outputs(result: GuardResult, repo_root: Path, out_dir: Path) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y_%m_%d")
    json_path = out_dir / f"rtx3090_env_guard_{stamp}.json"
    md_path = out_dir / f"RTX3090_ENV_GUARD_{stamp}.md"
    payload: dict[str, Any] = asdict(result)
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# RTX3090 Environment Guard",
        "",
        f"Date: `{result.date}`",
        f"Repo root: `{repo_root}`",
        f"WSL: `{result.is_wsl}`",
        f"Branch: `{result.branch or 'n/a'}`",
        f"Commit: `{result.commit or 'n/a'}`",
        "",
        "## Pack Metadata",
        "",
        f"- pack name: `{(result.pack_metadata or {}).get('pack_name', 'n/a')}`",
        f"- source repo: `{((result.pack_metadata or {}).get('source') or {}).get('origin_url', 'n/a')}`",
        f"- source path: `{((result.pack_metadata or {}).get('source') or {}).get('path', 'n/a')}`",
        f"- source branch: `{((result.pack_metadata or {}).get('source') or {}).get('branch', 'n/a')}`",
        f"- source commit: `{((result.pack_metadata or {}).get('source') or {}).get('commit', 'n/a')}`",
        f"- filesystem: `{((result.pack_metadata or {}).get('usb') or {}).get('filesystem', 'n/a')}`",
        "",
        "## Runtime",
        "",
        f"- Python: `{result.python_version}`",
        f"- Executable: `{result.python_executable}`",
        f"- Torch available: `{result.torch_available}`",
        f"- Torch version: `{result.torch_version or 'n/a'}`",
        f"- Torch CUDA version: `{result.torch_cuda_version or 'n/a'}`",
        f"- CUDA available: `{result.cuda_available}`",
        f"- GPU name: `{result.gpu_name or 'n/a'}`",
        f"- GPU count: `{result.gpu_count}`",
        f"- GPU total MiB: `{result.gpu_total_mib or 'n/a'}`",
        "",
        "## nvidia-smi",
        "",
        "```text",
        result.nvidia_smi or "nvidia-smi unavailable",
        "```",
        "",
        "## Notes",
        "",
    ]
    lines.extend(f"- {note}" for note in result.notes or ["none"])
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, md_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=None)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    out_dir = args.out_dir or (repo_root / "outputs")
    result = build_result(repo_root)
    json_path, md_path = write_outputs(result, repo_root, out_dir)
    print(json.dumps({"out_json": str(json_path), "out_md": str(md_path)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
