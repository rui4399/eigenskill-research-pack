$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path

$wsl = Get-Command wsl.exe -ErrorAction SilentlyContinue
if ($null -ne $wsl) {
    $driveForMount = $null
    $wslRoot = $repoRoot -replace '\\', '/'
    if ($wslRoot -match '^([A-Za-z]):/(.*)$') {
        $drive = $matches[1].ToLowerInvariant()
        $driveForMount = $matches[1].ToUpperInvariant()
        $rest = $matches[2]
        $wslRoot = "/mnt/$drive/$rest"
    }

    & wsl.exe -e bash -lc "test -d '$wslRoot'"
    if ($LASTEXITCODE -ne 0 -and $null -ne $driveForMount) {
        $mountDriveLower = $driveForMount.ToLowerInvariant()
        & wsl.exe -u root -e bash -lc "mkdir -p '/mnt/$mountDriveLower' && (mountpoint -q '/mnt/$mountDriveLower' || mount -t drvfs '$driveForMount`:' '/mnt/$mountDriveLower')"
    }

    & wsl.exe -e bash -lc "test -d '$wslRoot'"
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "WSL could not access $wslRoot; falling back to native Windows Python."
    }
    else {
        & wsl.exe -e bash -lc "cd '$wslRoot' && bash scripts_3090/run_rtx3090_env_guard.sh"
        exit $LASTEXITCODE
    }
}

$python = Get-Command python -ErrorAction SilentlyContinue
if ($null -eq $python) {
    $python = Get-Command py -ErrorAction SilentlyContinue
}
if ($null -eq $python) {
    throw 'Python not found.'
}

& $python.Source (Join-Path $scriptDir 'rtx3090_env_guard.py') --repo-root $repoRoot
