param(
  [string]$Configuration = "Release",
  [switch]$NoAvx2
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$BuildDir = Join-Path $PSScriptRoot "build"
$Source = Join-Path $PSScriptRoot "src\eigenskill_bench.cpp"
$Exe = Join-Path $BuildDir "eigenskill_bench.exe"

New-Item -ItemType Directory -Force -Path $BuildDir | Out-Null

$VsWhere = "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe"
if (-not (Test-Path -LiteralPath $VsWhere)) {
  throw "vswhere.exe not found. Install Visual Studio Build Tools or Visual Studio with C++ tools."
}

$VsInstall = & $VsWhere -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath
if (-not $VsInstall) {
  throw "No Visual Studio installation with C++ x64 tools found."
}

$VcVars = Join-Path $VsInstall "VC\Auxiliary\Build\vcvars64.bat"
if (-not (Test-Path -LiteralPath $VcVars)) {
  throw "vcvars64.bat not found at $VcVars"
}

$ArchFlag = if ($NoAvx2) { "" } else { "/arch:AVX2" }
$Defines = "/DNOMINMAX /D_CRT_SECURE_NO_WARNINGS"
$CompilerFlags = "/nologo /std:c++17 /O2 /EHsc $ArchFlag $Defines"

$Command = "`"$VcVars`" && cl $CompilerFlags /Fe:`"$Exe`" `"$Source`""
cmd.exe /c $Command

if (-not (Test-Path -LiteralPath $Exe)) {
  throw "Build failed; executable not found: $Exe"
}

Write-Host "Built: $Exe"

