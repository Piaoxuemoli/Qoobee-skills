# Terminal Types & Color Schemes Reference

This catalog documents terminal types for the terminal-screenshot skill. Each entry
includes hex colors, CSS classes, CRT effects, and window chrome style.

---

## 1. Green Phosphor CRT (P1)

The iconic "hacker terminal." Used in IBM 3270, DEC VT100, early oscilloscopes.

| Property | Value |
|----------|-------|
| Background | `#0A0A0A` (slightly lifted black for glow effect) |
| Foreground | `#33FF33` |
| Bold/Bright | `#66FF66` |
| Dim | `#1A991A` |
| ANSI Black | `#000000` |
| ANSI Red | `#33FF33` (monochrome — all colors map to green variants) |
| Prompt color | `#33FF33` |
| Cursor | `#33FF33` block |

**CRT Effects CSS:**
- Scanlines: `repeating-linear-gradient(0deg, rgba(0,0,0,0.15) 0px, rgba(0,0,0,0.15) 1px, transparent 1px, transparent 3px)`
- Text glow: `text-shadow: 0 0 3px rgba(51,255,51,0.5), 0 0 8px rgba(51,255,51,0.2)`
- Vignette: `radial-gradient(ellipse at center, transparent 60%, rgba(0,0,0,0.4) 100%)`
- Screen curvature: subtle `border-radius: 8px` on the screen element

**Window Chrome:** CRT monitor bezel — dark gray frame around the screen, with a small
label text below (e.g., "IBM 3270 TERMINAL").

**CSS classes:** `terminal-crt-green`, `crt-scanlines`, `crt-glow`, `crt-vignette`

---

## 2. Amber Phosphor CRT (P3)

Warmer, retro feel. Used in DEC VT220, ADM-3A terminals.

| Property | Value |
|----------|-------|
| Background | `#0A0A0A` |
| Foreground | `#FFB000` |
| Bold/Bright | `#FFCC33` |
| Dim | `#996600` |
| Prompt color | `#FFB000` |
| Cursor | `#FFB000` block |

**CRT Effects CSS:** Same structure as green phosphor, with amber colors:
- Text glow: `text-shadow: 0 0 3px rgba(255,176,0,0.5), 0 0 8px rgba(255,176,0,0.2)`

**Window Chrome:** Same CRT monitor bezel, label "ADM-3A TERMINAL" or "VT220".

**CSS classes:** `terminal-crt-amber`, `crt-scanlines`, `crt-glow-amber`, `crt-vignette`

---

## 3. White Phosphor CRT (P4)

Later-generation monochrome CRT. Clean, high-contrast look.

| Property | Value |
|----------|-------|
| Background | `#0A0A0A` |
| Foreground | `#E0E0E0` |
| Bold/Bright | `#FFFFFF` |
| Dim | `#888888` |
| Prompt color | `#E0E0E0` |
| Cursor | `#FFFFFF` block |

**CRT Effects CSS:**
- Text glow: `text-shadow: 0 0 2px rgba(224,224,224,0.4), 0 0 6px rgba(224,224,224,0.15)`
- Scanlines: same pattern, slightly lighter

**CSS classes:** `terminal-crt-white`, `crt-scanlines`, `crt-glow-white`, `crt-vignette`

---

## 4. Modern Dark Terminal (GNOME / generic Linux)

Clean, professional. The default for most server screenshots.

| Property | Value |
|----------|-------|
| Background | `#1E1E1E` |
| Foreground | `#D4D4D4` |
| Bold/Bright | `#FFFFFF` |
| Prompt (user@host) | `#569CD6` (blue) |
| Prompt ($) | `#D4D4D4` |
| Command | `#D4D4D4` |
| Output | `#CCCCCC` |
| Error/Stderr | `#F44747` (red) |
| ANSI Black | `#000000` |
| ANSI Red | `#CD3131` |
| ANSI Green | `#0DBC79` |
| ANSI Yellow | `#E5E510` |
| ANSI Blue | `#2472C8` |
| ANSI Magenta | `#BC3FBC` |
| ANSI Cyan | `#11A8CD` |
| ANSI White | `#E5E5E5` |
| ANSI Bright Black | `#666666` |
| ANSI Bright Red | `#F14C4C` |
| ANSI Bright Green | `#23D18B` |
| ANSI Bright Yellow | `#F5F543` |
| ANSI Bright Blue | `#3B8EEA` |
| ANSI Bright Magenta | `#D670D6` |
| ANSI Bright Cyan | `#29B8DB` |
| ANSI Bright White | `#FFFFFF` |

**Effects:** None (clean modern rendering).

**Window Chrome:** GNOME-style — dark title bar with subtle border, no traffic light buttons.

**CSS classes:** `terminal-modern-dark`, `terminal-gnome`

---

## 5. macOS Terminal Pro

Apple's default Terminal.app dark theme.

| Property | Value |
|----------|-------|
| Background | `#1E1E1E` |
| Foreground | `#D4D4D4` |
| Selection | `#264F78` |
| ANSI Black | `#000000` |
| ANSI Red | `#C91B00` |
| ANSI Green | `#00C600` |
| ANSI Yellow | `#C7C400` |
| ANSI Blue | `#0225C7` |
| ANSI Magenta | `#CA30C7` |
| ANSI Cyan | `#00C5C7` |
| ANSI White | `#C7C7C7` |
| ANSI Bright Black | `#676767` |
| ANSI Bright Red | `#FF6D67` |
| ANSI Bright Green | `#5FF967` |
| ANSI Bright Yellow | `#FEFB67` |
| ANSI Bright Blue | `#6871FF` |
| ANSI Bright Magenta | `#FF76FF` |
| ANSI Bright Cyan | `#5FFDCF` |
| ANSI Bright White | `#FEFB67` |

**Effects:** None (clean modern rendering).

**Window Chrome:** macOS title bar with red/yellow/green traffic light buttons on the left,
title text centered ("username — -zsh — 80x24"), dark background `#323233`.

**CSS classes:** `terminal-macos-pro`, `macos-titlebar`

---

## 6. Windows Terminal Campbell

Microsoft's default Windows Terminal dark theme.

| Property | Value |
|----------|-------|
| Background | `#0C0C0C` |
| Foreground | `#CCCCCC` |
| Selection | `#264F78` |
| ANSI Black | `#0C0C0C` |
| ANSI Red | `#C50F1F` |
| ANSI Green | `#13A10E` |
| ANSI Yellow | `#C19C00` |
| ANSI Blue | `#0037DA` |
| ANSI Magenta | `#881798` |
| ANSI Cyan | `#3A96DD` |
| ANSI White | `#CCCCCC` |
| ANSI Bright Black | `#767676` |
| ANSI Bright Red | `#E74856` |
| ANSI Bright Green | `#16C60C` |
| ANSI Bright Yellow | `#F9F1A5` |
| ANSI Bright Blue | `#3B78FF` |
| ANSI Bright Magenta | `#B4009E` |
| ANSI Bright Cyan | `#61D6D6` |
| ANSI Bright White | `#F2F2F2` |

**Effects:** None (clean modern rendering).

**Window Chrome:** Windows Terminal style — dark title bar with a tab ("PowerShell" or "bash"),
minimize/maximize/close buttons on the right. Tab has a colored underline accent.

**CSS classes:** `terminal-windows-campbell`, `win-titlebar`, `win-tab`

---

## 7. Solarized Dark

Ethan Schoonover's carefully balanced, eye-friendly scheme.

| Property | Value |
|----------|-------|
| Background | `#002B36` |
| Foreground | `#839496` |
| Bold | `#93A1A1` |
| ANSI Red | `#DC322F` |
| ANSI Green | `#859900` |
| ANSI Yellow | `#B58900` |
| ANSI Blue | `#268BD2` |
| ANSI Magenta | `#D33682` |
| ANSI Cyan | `#2AA198` |

**Effects:** None.

**Window Chrome:** Usually macOS or GNOME frame.

**CSS classes:** `terminal-solarized-dark`

---

## 8. xterm (Classic Light)

Original X11 terminal — white background, black text. Useful for "clean print" screenshots.

| Property | Value |
|----------|-------|
| Background | `#FFFFFF` |
| Foreground | `#000000` |
| Prompt | `#000000` |

**Effects:** None.

**Window Chrome:** Minimal X11 window frame or none.

**CSS classes:** `terminal-xterm-light`

---

## Auto-Detection Heuristics

When the user does not explicitly specify a terminal type, apply these rules in order:

```
1. Content contains GPU/CUDA keywords (nvidia-smi, nvcc, nvprof, cudaMalloc, Tesla, GPU)
   → Modern Dark Terminal

2. Content contains Windows commands (dir, ipconfig, netstat, chkdsk, PowerShell prompt)
   → Windows Terminal Campbell

3. Content contains macOS commands (brew, launchctl, pbcopy, osascript)
   → macOS Terminal Pro

4. Content is a simple "ls -la", "cat file", or small bash output
   → If retro/hacker context: Green Phosphor CRT
   → Otherwise: Modern Dark Terminal

5. User is writing an experiment report, technical documentation, or lab report
   → Modern Dark Terminal (server/data-center context)

6. Content is from a real remote server session (SSH)
   → Modern Dark Terminal with window chrome

7. Explicit user request overrides all heuristics
```

## Font Stack

Always use: `'Consolas', 'Courier New', 'Microsoft YaHei', monospace`

This covers:
- Windows: Consolas (best terminal font on Windows)
- macOS: Courier New (fallback, SF Mono not universally available as webfont)
- Linux: Courier New or system monospace
- CJK: Microsoft YaHei for Chinese characters in output
