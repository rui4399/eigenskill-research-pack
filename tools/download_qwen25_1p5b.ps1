param(
  [string]$Destination = "$env:USERPROFILE\models\Qwen2.5-1.5B-Instruct",
  [switch]$SkipExisting
)

$ErrorActionPreference = "Stop"

$repo = "https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct/resolve/main"
$files = @(
  ".gitattributes",
  "LICENSE",
  "README.md",
  "config.json",
  "generation_config.json",
  "merges.txt",
  "tokenizer.json",
  "tokenizer_config.json",
  "vocab.json",
  "model.safetensors"
)

New-Item -ItemType Directory -Force -Path $Destination | Out-Null

foreach ($file in $files) {
  $url = "$repo/$file"
  $out = Join-Path $Destination $file
  if ($SkipExisting -and (Test-Path -LiteralPath $out)) {
    Write-Host "skip existing $file"
    continue
  }
  Write-Host "download $file"
  & curl.exe -fL -C - --retry 30 --retry-all-errors --retry-delay 5 `
    --connect-timeout 30 --speed-time 120 --speed-limit 1024 `
    -o $out $url
  if ($LASTEXITCODE -ne 0) {
    throw "curl failed for $file with exit code $LASTEXITCODE"
  }
}

Get-ChildItem -LiteralPath $Destination | Sort-Object Name | Select-Object Name,Length
