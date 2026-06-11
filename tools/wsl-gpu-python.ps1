param(
    [string] $CommandLine = "",

    [string] $BashCommand = "",

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $PythonArgs
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

    throw "wsl.exe not found"
}

function ConvertTo-BashSingleQuote {
    param([string] $Text)
    return "'" + ($Text -replace "'", "'\''") + "'"
}

function Invoke-WslScript {
    param(
        [string] $Body
    )

    $wsl = Resolve-Wsl
    $tempPath = [System.IO.Path]::ChangeExtension([System.IO.Path]::GetTempFileName(), ".sh")
    $script = @(
        "#!/usr/bin/env bash",
        "set -e",
        "cd $(ConvertTo-BashSingleQuote $wslRoot)",
        $Body,
        ""
    ) -join "`n"

    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($tempPath, $script, $utf8NoBom)
    try {
        $wslScript = (& $wsl -e wslpath -a $tempPath).Trim()
        & $wsl -e bash $wslScript
        $script:LastWslExitCode = $LASTEXITCODE
    } finally {
        Remove-Item -LiteralPath $tempPath -ErrorAction SilentlyContinue
    }
}

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$wslRoot = (& (Resolve-Wsl) -e wslpath -a $repoRoot).Trim()

if ($BashCommand) {
    Invoke-WslScript -Body $BashCommand
    exit $script:LastWslExitCode
}

if ($CommandLine) {
    Invoke-WslScript -Body "python3 $CommandLine"
    exit $script:LastWslExitCode
}

if (-not $PythonArgs -or $PythonArgs.Count -eq 0) {
    $PythonArgs = @("-c", "import sys, torch; print(sys.executable); print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'no cuda')")
}

$quotedArgs = $PythonArgs | ForEach-Object {
    "'" + ($_ -replace "'", "'\''") + "'"
}

$body = "python3 " + ($quotedArgs -join " ")
Invoke-WslScript -Body $body
exit $script:LastWslExitCode
