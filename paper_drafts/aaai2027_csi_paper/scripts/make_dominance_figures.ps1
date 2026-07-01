param(
  [string]$OutDir = (Join-Path $PSScriptRoot '..\figures')
)

Add-Type -AssemblyName System.Drawing

$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

function New-BitmapCanvas([int]$W, [int]$H) {
  $bmp = [System.Drawing.Bitmap]::new($W, $H)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
  $g.Clear([System.Drawing.Color]::White)
  return @{ Bitmap = $bmp; Graphics = $g }
}

function Color-Hex([string]$hex) {
  return [System.Drawing.ColorTranslator]::FromHtml($hex)
}

function Draw-Text($g, [string]$text, [float]$x, [float]$y, [float]$size = 18, [string]$style = 'Regular', [string]$color = '#20242a') {
  $fontStyle = [System.Drawing.FontStyle]::$style
  $font = [System.Drawing.Font]::new('Arial', $size, $fontStyle)
  $brush = [System.Drawing.SolidBrush]::new((Color-Hex $color))
  $g.DrawString($text, $font, $brush, $x, $y)
  $font.Dispose()
  $brush.Dispose()
}

function Draw-CenteredText($g, [string]$text, [System.Drawing.RectangleF]$rect, [float]$size = 16, [string]$style = 'Regular', [string]$color = '#20242a') {
  $font = [System.Drawing.Font]::new('Arial', $size, [System.Drawing.FontStyle]::$style)
  $brush = [System.Drawing.SolidBrush]::new((Color-Hex $color))
  $fmt = [System.Drawing.StringFormat]::new()
  $fmt.Alignment = [System.Drawing.StringAlignment]::Center
  $fmt.LineAlignment = [System.Drawing.StringAlignment]::Center
  $g.DrawString($text, $font, $brush, $rect, $fmt)
  $fmt.Dispose()
  $font.Dispose()
  $brush.Dispose()
}

function Draw-Line($g, [float]$x1, [float]$y1, [float]$x2, [float]$y2, [string]$color = '#2b3036', [float]$width = 2) {
  $pen = [System.Drawing.Pen]::new((Color-Hex $color), $width)
  $g.DrawLine($pen, $x1, $y1, $x2, $y2)
  $pen.Dispose()
}

function Draw-Rect($g, [float]$x, [float]$y, [float]$w, [float]$h, [string]$fill, [string]$stroke = '#ffffff', [float]$strokeWidth = 1) {
  $brush = [System.Drawing.SolidBrush]::new((Color-Hex $fill))
  $pen = [System.Drawing.Pen]::new((Color-Hex $stroke), $strokeWidth)
  $g.FillRectangle($brush, $x, $y, $w, $h)
  $g.DrawRectangle($pen, $x, $y, $w, $h)
  $brush.Dispose()
  $pen.Dispose()
}

function Draw-Circle($g, [float]$cx, [float]$cy, [float]$r, [string]$fill, [string]$stroke = '#ffffff') {
  $brush = [System.Drawing.SolidBrush]::new((Color-Hex $fill))
  $pen = [System.Drawing.Pen]::new((Color-Hex $stroke), 2)
  $g.FillEllipse($brush, $cx - $r, $cy - $r, 2 * $r, 2 * $r)
  $g.DrawEllipse($pen, $cx - $r, $cy - $r, 2 * $r, 2 * $r)
  $brush.Dispose()
  $pen.Dispose()
}

function Save-Png($canvas, [string]$name) {
  $path = Join-Path $OutDir $name
  $canvas.Bitmap.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
  $canvas.Graphics.Dispose()
  $canvas.Bitmap.Dispose()
  Write-Host $path
}

function Map-X([double]$x, [double]$xmin, [double]$xmax, [double]$left, [double]$right) {
  return [float]($left + ($x - $xmin) * ($right - $left) / ($xmax - $xmin))
}

function Map-Y([double]$y, [double]$ymin, [double]$ymax, [double]$bottom, [double]$top) {
  return [float]($bottom - ($y - $ymin) * ($bottom - $top) / ($ymax - $ymin))
}

function Draw-Axes($g, [float]$left, [float]$top, [float]$right, [float]$bottom, [string]$xlabel, [string]$ylabel) {
  Draw-Line $g $left $bottom $right $bottom '#4b535c' 2
  Draw-Line $g $left $bottom $left $top '#4b535c' 2
  Draw-Text $g $xlabel (($left + $right) / 2 - 70) ($bottom + 36) 16 'Regular' '#343a40'
  Draw-Text $g $ylabel ($left - 54) ($top - 34) 16 'Regular' '#343a40'
}

# Figure A: regime evidence / dominance audit.
$c = New-BitmapCanvas 1400 720
$g = $c.Graphics
Draw-Text $g 'Regime Evidence Map: current evidence vs. missing dominance rows' 42 30 28 'Bold'
Draw-Text $g 'Filled cells are measured artifacts; empty cells define the submission-critical experiment.' 44 72 17 'Regular' '#555f6b'

$left = 130; $top = 145; $cellW = 210; $cellH = 86
$cols = @('8-bit / FP16', '4-bit', '3-bit', '2-bit', 'CSI alloc.')
$rows = @('Full MMLU', 'Full GSM8K', 'Local PPL smoke', 'Stress scaffold')
for ($i = 0; $i -lt $cols.Count; $i++) {
  Draw-CenteredText $g $cols[$i] ([System.Drawing.RectangleF]::new($left + $i * $cellW, 105, $cellW, 34)) 15 'Bold'
}
for ($r = 0; $r -lt $rows.Count; $r++) {
  Draw-CenteredText $g $rows[$r] ([System.Drawing.RectangleF]::new(18, $top + $r * $cellH, 100, $cellH)) 14 'Bold'
}

$cells = @{
  '0,0' = @{ fill='#d8f3dc'; text='FP16`n0.5864'; sub='full' }
  '0,1' = @{ fill='#e8f5e9'; text='AWQ/GPTQ`n0.5648 / 0.5362'; sub='full' }
  '0,2' = @{ fill='#fff3bf'; text='missing'; sub='run 3-bit' }
  '0,3' = @{ fill='#fff3bf'; text='missing'; sub='run 2-bit' }
  '0,4' = @{ fill='#ffe8cc'; text='missing'; sub='CSI downstream' }
  '1,0' = @{ fill='#d8f3dc'; text='FP16`n0.0811'; sub='full' }
  '1,1' = @{ fill='#e8f5e9'; text='AWQ/GPTQ`n0.0788 / 0.0728'; sub='full' }
  '1,2' = @{ fill='#fff3bf'; text='missing'; sub='run 3-bit' }
  '1,3' = @{ fill='#fff3bf'; text='missing'; sub='run 2-bit' }
  '1,4' = @{ fill='#ffe8cc'; text='missing'; sub='CSI downstream' }
  '2,0' = @{ fill='#d8f3dc'; text='FP16 PPL'; sub='0.5B/1.5B' }
  '2,1' = @{ fill='#d8f3dc'; text='INT4 PPL'; sub='0.5B/1.5B' }
  '2,2' = @{ fill='#e7f5ff'; text='INT3 collapse'; sub='0.5B measured' }
  '2,3' = @{ fill='#f8f9fa'; text='not run'; sub='local limit' }
  '2,4' = @{ fill='#d8f3dc'; text='CSI < INT4'; sub='5/5 PPL smokes' }
  '3,0' = @{ fill='#f8f9fa'; text='n/a'; sub='scaffold' }
  '3,1' = @{ fill='#e8f5e9'; text='INT4 ref'; sub='1.0x' }
  '3,2' = @{ fill='#ffe8cc'; text='INT3'; sub='4.0x distortion' }
  '3,3' = @{ fill='#ffc9c9'; text='INT2'; sub='16.0x distortion' }
  '3,4' = @{ fill='#e7f5ff'; text='budget alloc'; sub='2.6/3.6-bit proxy' }
}

for ($r = 0; $r -lt $rows.Count; $r++) {
  for ($i = 0; $i -lt $cols.Count; $i++) {
    $key = "$r,$i"
    $cell = $cells[$key]
    $x = $left + $i * $cellW
    $y = $top + $r * $cellH
    Draw-Rect $g $x $y ($cellW - 8) ($cellH - 8) $cell.fill '#ffffff' 2
    $text = $cell.text -replace '`n', "`n"
    Draw-CenteredText $g $text ([System.Drawing.RectangleF]::new($x + 5, $y + 8, $cellW - 18, 38)) 14 'Bold'
    Draw-CenteredText $g $cell.sub ([System.Drawing.RectangleF]::new($x + 5, $y + 47, $cellW - 18, 24)) 11 'Regular' '#5f6b76'
  }
}
Draw-Rect $g 1040 515 310 76 '#f1f3f5' '#ced4da' 2
Draw-Text $g 'Dominance claim gate' 1060 528 17 'Bold'
Draw-Text $g 'Allowed now: evidence map.' 1060 553 13 'Regular' '#495057'
Draw-Text $g 'Needed: same-budget full retention.' 1060 572 13 'Regular' '#495057'
Save-Png $c 'regime_dominance_map.png'

# Figure B: failure separation heatmap.
$c = New-BitmapCanvas 1300 700
$g = $c.Graphics
Draw-Text $g 'Failure Separation Map' 42 30 28 'Bold'
Draw-Text $g 'Darker cells indicate higher un-audited risk in a calibration-driven mixed-precision allocation pipeline.' 44 72 17 'Regular' '#555f6b'
$methods = @('GPTQ', 'AWQ', 'SmoothQuant', 'OmniQuant', 'CSI gate')
$modes = @('split drift', 'ranking collapse', 'scaling mismatch', 'constraint conflict', 'retention gap')
$risk = @(
  @(3,2,1,3,2),
  @(2,3,1,2,2),
  @(3,2,3,2,2),
  @(2,2,2,2,2),
  @(1,1,1,1,3)
)
$colors = @('#e9ecef', '#d8f3dc', '#fff3bf', '#ffa8a8')
$left = 220; $top = 140; $cellW = 190; $cellH = 74
for ($i=0; $i -lt $modes.Count; $i++) {
  Draw-CenteredText $g $modes[$i] ([System.Drawing.RectangleF]::new($left + $i*$cellW, 98, $cellW-6, 40)) 13 'Bold'
}
for ($r=0; $r -lt $methods.Count; $r++) {
  Draw-CenteredText $g $methods[$r] ([System.Drawing.RectangleF]::new(38, $top + $r*$cellH, 160, $cellH-8)) 15 'Bold'
  for ($i=0; $i -lt $modes.Count; $i++) {
    $v = $risk[$r][$i]
    $label = @('n/a','low','medium','high')[$v]
    Draw-Rect $g ($left + $i*$cellW) ($top + $r*$cellH) ($cellW-8) ($cellH-8) $colors[$v] '#ffffff' 2
    Draw-CenteredText $g $label ([System.Drawing.RectangleF]::new($left + $i*$cellW, $top + $r*$cellH, $cellW-8, $cellH-8)) 15 'Bold'
  }
}
Draw-Text $g 'Reading: CSI is not a backend replacement; it suppresses allocation-decision risks while still requiring direct retention rows.' 54 560 16 'Regular' '#495057'
Draw-Rect $g 54 610 250 36 '#d8f3dc' '#ffffff' 1
Draw-Text $g 'low / controlled' 70 618 14 'Regular'
Draw-Rect $g 330 610 250 36 '#fff3bf' '#ffffff' 1
Draw-Text $g 'medium / backend-dependent' 346 618 14 'Regular'
Draw-Rect $g 606 610 250 36 '#ffa8a8' '#ffffff' 1
Draw-Text $g 'high / unaudited' 622 618 14 'Regular'
Save-Png $c 'failure_separation_map.png'

# Figure C: constraint effect landscape.
$c = New-BitmapCanvas 1500 760
$g = $c.Graphics
Draw-Text $g 'Constraint Effect Landscape' 42 28 28 'Bold'
Draw-Text $g 'Three measurable links: calibration size improves stability, budget constraints are satisfied, and gated allocation lowers PPL in smoke tests.' 44 70 16 'Regular' '#555f6b'

# Panel 1: stability curves.
$p1 = @{ l=80; t=145; r=455; b=560 }
Draw-Text $g 'A. Calibration size -> stability' $p1.l 108 17 'Bold'
Draw-Axes $g $p1.l $p1.t $p1.r $p1.b 'calibration prompts' 'Spearman'
$qwen = @(@(2,0.1410),@(4,0.2869),@(8,0.4918))
$smol = @(@(4,0.3133),@(8,0.4136),@(16,0.6959))
foreach ($series in @(@{data=$qwen;color='#1864ab';name='Qwen2.5-1.5B'}, @{data=$smol;color='#2b8a3e';name='SmolLM2-360M'})) {
  $prev = $null
  foreach ($pt in $series.data) {
    $x = Map-X $pt[0] 2 16 $p1.l $p1.r
    $y = Map-Y $pt[1] 0 0.75 $p1.b $p1.t
    if ($prev) { Draw-Line $g $prev[0] $prev[1] $x $y $series.color 4 }
    Draw-Circle $g $x $y 7 $series.color
    $prev = @($x,$y)
  }
}
Draw-Text $g 'Qwen2.5' 300 165 13 'Regular' '#1864ab'
Draw-Text $g 'SmolLM2' 300 187 13 'Regular' '#2b8a3e'

# Panel 2: budget gate.
$p2 = @{ l=570; t=145; r=940; b=560 }
Draw-Text $g 'B. Lagrangian budget gate' $p2.l 108 17 'Bold'
Draw-Axes $g $p2.l $p2.t $p2.r $p2.b 'case index' 'budget use'
$budget = @(0.999927,0.999927,0.999982,0.999980,0.999965,0.999967)
$prev = $null
for ($i=0; $i -lt $budget.Count; $i++) {
  $x = Map-X ($i+1) 1 6 $p2.l $p2.r
  $y = Map-Y $budget[$i] 0.9998 1.00005 $p2.b $p2.t
  if ($prev) { Draw-Line $g $prev[0] $prev[1] $x $y '#862e9c' 4 }
  Draw-Circle $g $x $y 7 '#862e9c'
  $prev = @($x,$y)
}
$targetY = Map-Y 1.0 0.9998 1.00005 $p2.b $p2.t
Draw-Line $g $p2.l $targetY $p2.r $targetY '#868e96' 2
Draw-Text $g 'target = 1.0' ($p2.r - 115) ($targetY - 28) 12 'Regular' '#495057'

# Panel 3: PPL smoke ratios.
$p3 = @{ l=1060; t=145; r=1430; b=560 }
Draw-Text $g 'C. Allocation PPL / INT4 PPL' $p3.l 108 17 'Bold'
Draw-Axes $g $p3.l $p3.t $p3.r $p3.b 'smoke case' 'ratio'
$ratios = @(0.7900,0.8538,0.7659,0.8517,0.8640)
for ($i=0; $i -lt $ratios.Count; $i++) {
  $x = Map-X ($i+1) 1 5 $p3.l $p3.r
  $y = Map-Y $ratios[$i] 0.70 1.02 $p3.b $p3.t
  Draw-Rect $g ($x-22) $y 44 ($p3.b-$y) '#339af0' '#ffffff' 1
  Draw-CenteredText $g ($ratios[$i].ToString('0.00')) ([System.Drawing.RectangleF]::new($x-32, $y-28, 64, 22)) 11 'Regular' '#1c3d5a'
}
$oneY = Map-Y 1.0 0.70 1.02 $p3.b $p3.t
Draw-Line $g $p3.l $oneY $p3.r $oneY '#868e96' 2
Draw-Text $g 'uniform INT4' ($p3.r - 118) ($oneY - 28) 12 'Regular' '#495057'

Draw-Text $g 'Claim boundary: these panels support controlled-system behavior, not full downstream CSI superiority.' 86 685 16 'Regular' '#495057'
Save-Png $c 'constraint_effect_landscape.png'
