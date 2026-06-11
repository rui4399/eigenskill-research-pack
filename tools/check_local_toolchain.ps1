param(
    [switch] $Json
)

$ErrorActionPreference = "Stop"

function Resolve-Wsl {
    $candidates = @(
        "$env:WINDIR\Sysnative\wsl.exe",
        "$env:WINDIR\System32\wsl.exe",
        "wsl.exe"
    )

    foreach ($candidate in $candidates) {
        $command = Get-Command $candidate -ErrorAction SilentlyContinue
        if ($command) {
            return $command.Source
        }
    }

    return $null
}

function Run-Text {
    param([scriptblock] $Block)

    try {
        $text = & $Block 2>&1
        [pscustomobject]@{
            ok = $true
            text = (($text | Out-String).Trim())
        }
    } catch {
        [pscustomobject]@{
            ok = $false
            text = $_.Exception.Message
        }
    }
}

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$wsl = Resolve-Wsl

$nvidiaSmi = Run-Text {
    nvidia-smi --query-gpu=name,memory.total,memory.used,driver_version --format=csv,noheader
}

$windowsPython = Run-Text {
    python -c "import sys; print(sys.executable); import torch; print(torch.__version__); print(torch.cuda.is_available())"
}

$wslPython = if ($wsl) {
    $wslRoot = (& $wsl -e wslpath -a $repoRoot).Trim()
    Run-Text {
        & $wsl -e bash -lc "cd '$wslRoot'; python3 - <<'PY'
import sys
print(sys.executable)
try:
    import torch
    print(torch.__version__)
    print(torch.cuda.is_available())
    print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'no cuda')
except Exception as exc:
    print(type(exc).__name__ + ': ' + str(exc))
PY"
    }
} else {
    [pscustomobject]@{
        ok = $false
        text = "wsl.exe not found"
    }
}

$codegraphVersion = Run-Text {
    codegraph --version
}

$codegraphStatus = Run-Text {
    codegraph status $repoRoot --json
}

$codexConfigPath = "C:\Users\18042\.codex\config.toml"
$codexCodegraphMcp = if (Test-Path -LiteralPath $codexConfigPath) {
    $configText = Get-Content -Raw -LiteralPath $codexConfigPath
    ($configText -match '\[mcp_servers\.codegraph\]') -and
        ($configText -match 'serve') -and
        ($configText -match '--mcp')
} else {
    $false
}

$skillRoots = @(
    "C:\Users\18042\.codex\skills\experiment-design\SKILL.md",
    "C:\Users\18042\.codex\skills\academic-skills\SKILL.md"
)

$result = [pscustomobject]@{
    repoRoot = $repoRoot
    nvidiaSmi = $nvidiaSmi
    windowsPython = $windowsPython
    wslPython = $wslPython
    codegraphVersion = $codegraphVersion
    codegraphStatus = $codegraphStatus
    codexCodegraphMcpConfigured = $codexCodegraphMcp
    skillFiles = $skillRoots | ForEach-Object {
        [pscustomobject]@{
            path = $_
            exists = Test-Path -LiteralPath $_
        }
    }
    recommendation = "Use tools\wsl-gpu-python.ps1 or WSL python3 for CUDA experiments; Windows base python is CPU-only on this machine."
}

if ($Json) {
    $result | ConvertTo-Json -Depth 5
} else {
    "== NVIDIA SMI =="
    $result.nvidiaSmi.text
    ""
    "== Windows Python =="
    $result.windowsPython.text
    ""
    "== WSL Python =="
    $result.wslPython.text
    ""
    "== CodeGraph =="
    $result.codegraphVersion.text
    $result.codegraphStatus.text
    "Codex MCP configured: $($result.codexCodegraphMcpConfigured)"
    ""
    "== Skill Files =="
    foreach ($skill in $result.skillFiles) {
        "{0}  exists={1}" -f $skill.path, $skill.exists
    }
    ""
    "Recommendation: $($result.recommendation)"
}
