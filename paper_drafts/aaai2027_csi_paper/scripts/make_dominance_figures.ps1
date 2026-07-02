param(
  [string]$OutDir = (Join-Path $PSScriptRoot '..\figures')
)

Add-Type -AssemblyName System.Drawing
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

function Color-Hex([string]$hex) {
  return [System.Drawing.ColorTranslator]::FromHtml($hex)
}

function New-Canvas([int]$W, [int]$H) {
  $bmp = [System.Drawing.Bitmap]::new($W, $H)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
  $g.Clear([System.Drawing.Color]::White)
  return @{ Bitmap = $bmp; Graphics = $g }
}

function Save-Png($canvas, [string[]]$names) {
  foreach ($name in $names) {
    $path = Join-Path $OutDir $name
    $canvas.Bitmap.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Host $path
  }
  $canvas.Graphics.Dispose()
  $canvas.Bitmap.Dispose()
}

function Font([float]$size, [string]$style = 'Regular') {
  return [System.Drawing.Font]::new('Arial', $size, [System.Drawing.FontStyle]::$style)
}

function Draw-Text($g, [string]$text, [float]$x, [float]$y, [float]$size = 18, [string]$style = 'Regular', [string]$color = '#20242a') {
  $font = Font $size $style
  $brush = [System.Drawing.SolidBrush]::new((Color-Hex $color))
  $g.DrawString($text, $font, $brush, $x, $y)
  $brush.Dispose()
  $font.Dispose()
}

function Draw-CenteredText($g, [string]$text, [System.Drawing.RectangleF]$rect, [float]$size = 16, [string]$style = 'Regular', [string]$color = '#20242a') {
  $font = Font $size $style
  $brush = [System.Drawing.SolidBrush]::new((Color-Hex $color))
  $fmt = [System.Drawing.StringFormat]::new()
  $fmt.Alignment = [System.Drawing.StringAlignment]::Center
  $fmt.LineAlignment = [System.Drawing.StringAlignment]::Center
  $g.DrawString($text, $font, $brush, $rect, $fmt)
  $fmt.Dispose()
  $brush.Dispose()
  $font.Dispose()
}

function Draw-Rect($g, [float]$x, [float]$y, [float]$w, [float]$h, [string]$fill, [string]$stroke = '#ffffff', [float]$strokeWidth = 1) {
  $brush = [System.Drawing.SolidBrush]::new((Color-Hex $fill))
  $pen = [System.Drawing.Pen]::new((Color-Hex $stroke), $strokeWidth)
  $g.FillRectangle($brush, $x, $y, $w, $h)
  $g.DrawRectangle($pen, $x, $y, $w, $h)
  $brush.Dispose()
  $pen.Dispose()
}

function Draw-RoundRect($g, [float]$x, [float]$y, [float]$w, [float]$h, [float]$r, [string]$fill, [string]$stroke = '#495057', [float]$strokeWidth = 2) {
  $path = [System.Drawing.Drawing2D.GraphicsPath]::new()
  $d = 2 * $r
  $path.AddArc($x, $y, $d, $d, 180, 90)
  $path.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
  $path.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
  $path.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
  $path.CloseFigure()
  $brush = [System.Drawing.SolidBrush]::new((Color-Hex $fill))
  $pen = [System.Drawing.Pen]::new((Color-Hex $stroke), $strokeWidth)
  $g.FillPath($brush, $path)
  $g.DrawPath($pen, $path)
  $brush.Dispose()
  $pen.Dispose()
  $path.Dispose()
}

function Draw-Line($g, [float]$x1, [float]$y1, [float]$x2, [float]$y2, [string]$color = '#2b3036', [float]$width = 2) {
  $pen = [System.Drawing.Pen]::new((Color-Hex $color), $width)
  $pen.StartCap = [System.Drawing.Drawing2D.LineCap]::Round
  $pen.EndCap = [System.Drawing.Drawing2D.LineCap]::Round
  $g.DrawLine($pen, $x1, $y1, $x2, $y2)
  $pen.Dispose()
}

function Draw-Arrow($g, [float]$x1, [float]$y1, [float]$x2, [float]$y2, [string]$color = '#495057', [float]$width = 3) {
  $pen = [System.Drawing.Pen]::new((Color-Hex $color), $width)
  $pen.CustomEndCap = [System.Drawing.Drawing2D.AdjustableArrowCap]::new(5, 6)
  $g.DrawLine($pen, $x1, $y1, $x2, $y2)
  $pen.CustomEndCap.Dispose()
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

function Map-X([double]$x, [double]$xmin, [double]$xmax, [double]$left, [double]$right) {
  return [float]($left + ($x - $xmin) * ($right - $left) / ($xmax - $xmin))
}

function Map-Y([double]$y, [double]$ymin, [double]$ymax, [double]$bottom, [double]$top) {
  return [float]($bottom - ($y - $ymin) * ($bottom - $top) / ($ymax - $ymin))
}

function Draw-Axes($g, [float]$left, [float]$top, [float]$right, [float]$bottom, [string]$xlabel, [string]$ylabel) {
  Draw-Line $g $left $bottom $right $bottom '#4b535c' 2
  Draw-Line $g $left $bottom $left $top '#4b535c' 2
  Draw-Text $g $xlabel (($left + $right) / 2 - 82) ($bottom + 36) 16 'Regular' '#343a40'
  Draw-Text $g $ylabel ($left - 55) ($top - 34) 16 'Regular' '#343a40'
}

function Draw-Polyline($g, [object[]]$points, [string]$color, [float]$width = 4) {
  for ($i = 1; $i -lt $points.Count; $i++) {
    Draw-Line $g $points[$i-1][0] $points[$i-1][1] $points[$i][0] $points[$i][1] $color $width
  }
}

# Fig 1: CSI policy-driven feedback loop.
$c = New-Canvas 1400 620
$g = $c.Graphics
Draw-Text $g 'CSI Decision Feedback Loop' 44 28 30 'Bold'
Draw-Text $g 'Calibration stability as a policy-driven allocation audit' 46 70 17 'Regular' '#555f6b'
$boxes = @(
  @{t='Calibration Splits'; s='seeded prompt subsets'; x=70; y=180; fill='#e7f5ff'},
  @{t='CSI Estimator'; s='rank + set agreement'; x=350; y=180; fill='#fff3bf'},
  @{t='Decision State'; s='Reject / AuditOnly / Validate'; x=630; y=180; fill='#ffe3e3'},
  @{t='Allocation Policy'; s='protect modules or rerun'; x=910; y=180; fill='#d8f3dc'},
  @{t='Downstream Check'; s='fixed-budget retention'; x=910; y=410; fill='#e6fcf5'},
  @{t='Evidence Update'; s='thresholds + claim boundary'; x=350; y=410; fill='#f1f3f5'}
)
$w = 205; $h = 108
for ($i = 0; $i -lt $boxes.Count; $i++) {
  $x = $boxes[$i].x
  $y = $boxes[$i].y
  $fill = $boxes[$i].fill
  Draw-RoundRect $g $x $y $w $h 14 $fill '#5c6770' 2
  Draw-CenteredText $g $boxes[$i].t ([System.Drawing.RectangleF]::new($x+10, $y+22, $w-20, 34)) 15 'Bold'
  Draw-CenteredText $g $boxes[$i].s ([System.Drawing.RectangleF]::new($x+12, $y+62, $w-24, 36)) 11 'Regular' '#495057'
}
Draw-Arrow $g 280 234 345 234 '#495057' 3
Draw-Arrow $g 560 234 625 234 '#495057' 3
Draw-Arrow $g 840 234 905 234 '#495057' 3
Draw-Arrow $g 1012 292 1012 405 '#495057' 3
Draw-Arrow $g 910 464 560 464 '#495057' 3
Draw-Arrow $g 350 464 170 292 '#495057' 3
Draw-Text $g 'action' 873 206 13 'Bold' '#495057'
Draw-Text $g 'outcome' 1026 340 13 'Bold' '#495057'
Draw-Text $g 'feedback' 627 435 13 'Bold' '#495057'
Draw-Text $g 'update / rerun' 158 395 13 'Bold' '#495057'
Draw-Rect $g 86 532 1110 52 '#f8f9fa' '#ced4da' 2
Draw-CenteredText $g 'Policy invariant: CSI gates allocation claims before action, then downstream outcomes update thresholds and claim boundaries.' ([System.Drawing.RectangleF]::new(100, 540, 1080, 36)) 15 'Bold' '#343a40'
Save-Png $c @('fig1_pipeline.png', 'framework_overview.png')

# Fig 2: phase transition curve.
$c = New-Canvas 980 700
$g = $c.Graphics
Draw-Text $g 'CSI Phase Transition' 44 28 28 'Bold'
Draw-Text $g 'Qwen2.5-1.5B stability metrics improve as calibration size increases' 46 68 15 'Regular' '#555f6b'
$left=110; $top=130; $right=900; $bottom=585
Draw-Axes $g $left $top $right $bottom 'calibration size n' 'stability'
$series = @(
  @{name='Spearman rho'; data=@(@(2,0.1410),@(4,0.2869),@(8,0.4918)); color='#1864ab'},
  @{name='Top-K Jaccard'; data=@(@(2,0.2604),@(4,0.3313),@(8,0.4401)); color='#2b8a3e'},
  @{name='Positive Jaccard'; data=@(@(2,0.4244),@(4,0.5189),@(8,0.5992)); color='#c92a2a'}
)
foreach ($s in $series) {
  $pts = @()
  foreach ($pt in $s.data) {
    $x = Map-X $pt[0] 2 8 $left $right
    $yy = Map-Y $pt[1] 0.1 0.65 $bottom $top
    $pts += ,@($x,$yy)
  }
  Draw-Polyline $g $pts $s.color 4
  foreach ($p in $pts) { Draw-Circle $g $p[0] $p[1] 8 $s.color }
}
$tx = Map-X 4 2 8 $left $right
Draw-Line $g $tx $top $tx $bottom '#868e96' 2
Draw-Text $g 'audit transition' ($tx + 12) ($top + 10) 13 'Bold' '#495057'
Draw-Text $g 'unstable regime' ($left + 10) ($bottom - 50) 14 'Regular' '#868e96'
Draw-Text $g 'higher-stability regime' ($tx + 28) ($bottom - 50) 14 'Regular' '#868e96'
for ($i=0; $i -lt $series.Count; $i++) {
  Draw-Rect $g 650 (150 + $i*34) 22 12 $series[$i].color $series[$i].color 1
  Draw-Text $g $series[$i].name 682 (143 + $i*34) 13 'Regular'
}
Save-Png $c @('fig2_phase_transition.png', 'csi_stability_curves.png')

# Fig 3: cross-model robustness.
$c = New-Canvas 980 700
$g = $c.Graphics
Draw-Text $g 'Cross-Model CSI Robustness' 44 28 28 'Bold'
Draw-Text $g 'Spearman stability improves across Qwen2.5 scales and a second-pool SmolLM2 replication' 46 68 15 'Regular' '#555f6b'
$left=110; $top=130; $right=900; $bottom=585
Draw-Axes $g $left $top $right $bottom 'calibration size n' 'Spearman'
$series = @(
  @{name='Qwen2.5-0.5B'; data=@(@(2,0.3725),@(4,0.4324),@(8,0.6645)); color='#1864ab'},
  @{name='Qwen2.5-1.5B'; data=@(@(2,0.1410),@(4,0.2869),@(8,0.4918)); color='#c92a2a'},
  @{name='SmolLM2-360M'; data=@(@(4,0.3133),@(8,0.4136),@(16,0.6959)); color='#2b8a3e'}
)
foreach ($s in $series) {
  $pts = @()
  foreach ($pt in $s.data) {
    $x = Map-X $pt[0] 2 16 $left $right
    $yy = Map-Y $pt[1] 0.1 0.75 $bottom $top
    $pts += ,@($x,$yy)
  }
  Draw-Polyline $g $pts $s.color 4
  foreach ($p in $pts) { Draw-Circle $g $p[0] $p[1] 8 $s.color }
}
for ($i=0; $i -lt $series.Count; $i++) {
  Draw-Rect $g 650 (150 + $i*34) 22 12 $series[$i].color $series[$i].color 1
  Draw-Text $g $series[$i].name 682 (143 + $i*34) 13 'Regular'
}
Draw-Text $g 'Second-pool replication uses n = 4, 8, 16.' 120 618 13 'Regular' '#5f6b76'
Save-Png $c @('fig3_cross_model.png')

# Fig 4: CSI vs allocation risk proxy.
$c = New-Canvas 980 700
$g = $c.Graphics
Draw-Text $g 'CSI Stability vs Allocation Risk Proxy' 44 28 28 'Bold'
Draw-Text $g 'Risk is a claim-boundary proxy derived from calibration instability and stress evidence' 46 68 15 'Regular' '#555f6b'
$left=110; $top=130; $right=900; $bottom=585
Draw-Axes $g $left $top $right $bottom 'CSI stability score' 'allocation-risk proxy'
$riskPts = @(
  @(0.1410,0.86,'Qwen n=2'),
  @(0.2869,0.66,'Qwen n=4'),
  @(0.4918,0.38,'Qwen n=8'),
  @(0.6959,0.18,'Smol n=16')
)
$pts = @()
foreach ($pt in $riskPts) {
  $x = Map-X $pt[0] 0.1 0.75 $left $right
  $yy = Map-Y $pt[1] 0.1 0.95 $bottom $top
  $pts += ,@($x,$yy)
}
Draw-Polyline $g $pts '#5f3dc4' 4
for ($i=0; $i -lt $riskPts.Count; $i++) {
  Draw-Circle $g $pts[$i][0] $pts[$i][1] 9 '#5f3dc4'
  Draw-Text $g $riskPts[$i][2] ($pts[$i][0] + 12) ($pts[$i][1] - 13) 12 'Regular' '#343a40'
}
Draw-Rect $g 120 610 730 46 '#f8f9fa' '#ced4da' 1
Draw-CenteredText $g 'Interpretation: higher CSI reduces allocation-audit risk; full downstream risk must still be measured.' ([System.Drawing.RectangleF]::new(130, 616, 710, 30)) 13 'Regular' '#495057'
Save-Png $c @('fig4_risk.png')

# Fig 5: failure mode heatmap.
$c = New-Canvas 1300 700
$g = $c.Graphics
Draw-Text $g 'Failure Mode Heatmap' 42 30 28 'Bold'
Draw-Text $g 'Darker cells indicate higher un-audited risk in a calibration-driven mixed-precision allocation pipeline.' 44 72 17 'Regular' '#555f6b'
$methods = @('GPTQ', 'AWQ', 'SmoothQuant', 'OmniQuant', 'CSI gate')
$modes = @('calibration drift', 'rank instability', 'allocation risk')
$risk = @(
  @(3,2,3),
  @(2,3,2),
  @(3,3,2),
  @(2,2,2),
  @(1,1,1)
)
$colors = @('#e9ecef', '#d8f3dc', '#fff3bf', '#ffa8a8')
$left = 270; $top = 145; $cellW = 260; $cellH = 78
for ($i=0; $i -lt $modes.Count; $i++) {
  Draw-CenteredText $g $modes[$i] ([System.Drawing.RectangleF]::new($left + $i*$cellW, 100, $cellW-8, 36)) 14 'Bold'
}
for ($r=0; $r -lt $methods.Count; $r++) {
  Draw-CenteredText $g $methods[$r] ([System.Drawing.RectangleF]::new(44, $top + $r*$cellH, 190, $cellH-8)) 16 'Bold'
  for ($i=0; $i -lt $modes.Count; $i++) {
    $v = $risk[$r][$i]
    $label = @('n/a','low','medium','high')[$v]
    Draw-Rect $g ($left + $i*$cellW) ($top + $r*$cellH) ($cellW-8) ($cellH-8) $colors[$v] '#ffffff' 2
    Draw-CenteredText $g $label ([System.Drawing.RectangleF]::new($left + $i*$cellW, $top + $r*$cellH, $cellW-8, $cellH-8)) 16 'Bold'
  }
}
Draw-Text $g 'CSI is an audit layer above native quantizers; it does not replace backend-specific reconstruction or smoothing.' 54 580 15 'Regular' '#495057'
Save-Png $c @('fig5_failure.png', 'failure_separation_map.png')

# Fig 6: claim boundary / decision boundary.
$c = New-Canvas 1300 620
$g = $c.Graphics
Draw-Text $g 'CSI Claim Boundary' 44 28 30 'Bold'
Draw-Text $g 'How evidence is promoted from diagnostic signal to paper-facing allocation claim' 46 70 17 'Regular' '#555f6b'
$nodes = @(
  @{t='Diagnostic Evidence'; s='CSI curves, seed-pair tests'; fill='#e7f5ff'},
  @{t='Gate Pass'; s='stability + budget + stress'; fill='#d8f3dc'},
  @{t='Paper-facing Claim'; s='bounded audit claim'; fill='#fff3bf'},
  @{t='Downstream Required'; s='same-budget MMLU/GSM8K'; fill='#ffe8cc'}
)
$x=80; $y=205; $w=245; $h=118; $gap=60
for ($i=0; $i -lt $nodes.Count; $i++) {
  $xx = $x + $i*($w+$gap)
  Draw-RoundRect $g $xx $y $w $h 14 $nodes[$i].fill '#5c6770' 2
  Draw-CenteredText $g $nodes[$i].t ([System.Drawing.RectangleF]::new($xx+12, $y+22, $w-24, 32)) 16 'Bold'
  Draw-CenteredText $g $nodes[$i].s ([System.Drawing.RectangleF]::new($xx+14, $y+64, $w-28, 34)) 12 'Regular' '#495057'
  if ($i -lt $nodes.Count - 1) {
    Draw-Arrow $g ($xx+$w+8) ($y+$h/2) ($xx+$w+$gap-8) ($y+$h/2) '#495057' 3
  }
}
Draw-Rect $g 120 420 1060 76 '#f8f9fa' '#ced4da' 2
Draw-CenteredText $g 'Boundary rule: diagnostic and local PPL evidence can justify an audit system, but only direct same-budget downstream rows justify method-superiority claims.' ([System.Drawing.RectangleF]::new(140, 430, 1020, 52)) 16 'Bold' '#343a40'
Save-Png $c @('fig6_boundary.png', 'regime_dominance_map.png')
