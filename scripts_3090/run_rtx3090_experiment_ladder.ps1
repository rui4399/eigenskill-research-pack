$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path

$wslRoot = $repoRoot -replace '\\', '/'
$driveForMount = $null
if ($wslRoot -match '^([A-Za-z]):/(.*)$') {
    $drive = $matches[1].ToLowerInvariant()
    $driveForMount = $matches[1].ToUpperInvariant()
    $rest = $matches[2]
    $wslRoot = "/mnt/$drive/$rest"
}

$wsl = Get-Command wsl.exe -ErrorAction SilentlyContinue
if ($null -eq $wsl) {
    throw 'WSL is required for the experiment ladder. Run the environment guard PowerShell script for Windows-only fallback.'
}

& wsl.exe -e bash -lc "test -d '$wslRoot'"
if ($LASTEXITCODE -ne 0 -and $null -ne $driveForMount) {
    $mountDriveLower = $driveForMount.ToLowerInvariant()
    & wsl.exe -u root -e bash -lc "mkdir -p '/mnt/$mountDriveLower' && (mountpoint -q '/mnt/$mountDriveLower' || mount -t drvfs '$driveForMount`:' '/mnt/$mountDriveLower')"
}

& wsl.exe -e bash -lc "test -d '$wslRoot'"
if ($LASTEXITCODE -ne 0) {
    throw "WSL could not access $wslRoot"
}

& wsl.exe -e bash -lc "cd '$wslRoot' && bash scripts_3090/run_rtx3090_experiment_ladder.sh"
exit $LASTEXITCODE
