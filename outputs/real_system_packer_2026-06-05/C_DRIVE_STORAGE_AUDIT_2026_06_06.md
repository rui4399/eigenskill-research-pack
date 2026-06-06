# C Drive Storage Audit

Date: `2026-06-06`

Raw scan: `C:\Users\18042\Documents\Codex\2026-06-01\chatgpt-context-request-algorithm-system-co\storage_scan_2026_06_06.json`

## Current State

- C drive total: about `500.4 GB`
- Latest guarded run free space: about `19.12 GiB`
- Latest Windows readback after the second low-risk cleanup pass and latest CodeGraph sync: about `20.07 GB` decimal free
- Training/eval commands should keep using `--min-disk-free-gb 15`

## Main Pressure Points

| path | size | action |
|---|---:|---|
| `C:\Users\18042\AppData\Local\wsl` | about 62.8 GB | Do not edit files manually; compact VHD only from elevated PowerShell when no WSL jobs are running. |
| `C:\Program Files (x86)\Steam` | about 51.2 GB | User-managed games; do not delete from Codex. |
| `C:\Program Files\Lenovo` | about 33.8 GB | Installed vendor software; user/app uninstaller only. |
| `C:\Program Files\Epic Games` | about 33.7 GB | User-managed games; do not delete from Codex. |
| `C:\Users\18042\.codex` | about 12.1 GB | Contains active logs/tools/sessions; only targeted cleanup after Codex-safe review. |
| `C:\Users\18042\.ollama` | about 8.6 GB | Model cache; keep unless Rui explicitly chooses to remove models. |
| `C:\Users\18042\.lmstudio` | about 5.7 GB | Model/app cache; keep unless Rui explicitly chooses to remove models. |
| `C:\Users\18042\AppData\Local\Docker` | about 9.0 GB | Docker data; user-managed cleanup only. |
| `C:\Users\18042\AppData\Local\Temp` | now smaller after cleanup | Low-risk temp directory `d54byrr5` was removed; rescan before deleting more. |

## Cleanup Performed

- Removed `C:\Users\18042\AppData\Local\Temp\d54byrr5`, about `1265.66 MB`.
- Removed `C:\Users\18042\AppData\Local\uv\cache`, about `121.86 MB`.
- Removed repo-local `train_python\__pycache__`, about `0.20 MB`.
- Total measured immediate reclaim: about `1.316 GB`.
- Second low-risk cleanup pass:
  - removed `C:\Users\18042\AppData\Local\Temp\wsl-crashes`, about `299.07 MB`.
  - removed refreshed `C:\Users\18042\AppData\Local\uv\cache`, about `169.70 MB`.
  - removed most of `C:\Users\18042\AppData\Local\NVIDIA\DXCache` / `GLCache`, about `257.01 MB`; a few locked shader files remained.
  - removed `C:\Users\18042\AppData\Local\D3DSCache`, repo-local `__pycache__`, `CrashDumps`, and Explorer thumbnail cache, about `192 MB` combined.
  - total measured reclaim for this second pass: about `918 MB`; C: readback ended at about `20.17 GB` free, then about `20.07 GB` after the latest CodeGraph sync.
- No HuggingFace/Ollama/LM Studio/model caches were deleted.
- WSL HuggingFace cache is about `17 GB`; moving it to D: and compacting the WSL VHD could reduce C: materially, but that is a structural migration and was not performed automatically.

## Safe Defaults For Future Runs

- Keep repo-local cleanup enabled:
  - `--cleanup-repo-caches --cleanup-root .`
- Keep disk guard enabled:
  - `--min-disk-free-gb 15`
- Do not download new large models until C drive is above about `25 GB` free.
- Do not delete HuggingFace/Ollama/LM Studio caches without an explicit user choice.

## Elevated WSL VHD Compaction

Use only from elevated/admin PowerShell and only when no WSL experiments are running:

```powershell
wsl.exe --shutdown
$vhd = 'C:\Users\18042\AppData\Local\wsl\{437898f7-8f9f-4634-98cd-99603dd9b5ec}\ext4.vhdx'
$script = "$env:TEMP\compact-wsl-vhd.txt"
@"
select vdisk file="$vhd"
attach vdisk readonly
compact vdisk
detach vdisk
exit
"@ | Set-Content -LiteralPath $script -Encoding ASCII
diskpart.exe /s $script
Remove-Item -LiteralPath $script -Force
```
