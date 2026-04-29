---
name: terminal-screenshot
description: >
  Render terminal command outputs as realistic PNG screenshots. Use this skill whenever
  the user wants to "screenshot" a terminal command, generate terminal output images,
  visualize CLI results, create terminal-style screenshots for reports or documentation,
  or any time terminal output needs to be captured as an image. Also trigger proactively
  when the user is writing experiment reports, technical docs, or lab reports that would
  benefit from terminal evidence — suggest capturing the output as a screenshot.
---

# Terminal Screenshot Simulator

Render terminal command output as realistic PNG screenshots, with automatic terminal type
detection, color scheme selection, and CRT effects.

## Workflow

```
User provides command + output (or asks to run a command)
  → Step 1: Determine terminal type to simulate
  → Step 2: Select color scheme and effects from references/terminal-types.md
  → Step 3: Build HTML using templates from references/html-templates.md
  → Step 4: Convert HTML to PNG using scripts/html_to_png.py
  → Step 5: Deliver the PNG, optionally keep the HTML
```

## Step 1: Determine Terminal Type

Read `references/terminal-types.md` for the full catalog. Use these heuristics to
auto-select the terminal type based on the *content and context* of the screenshot:

| Content Signal | Terminal Type | Rationale |
|----------------|---------------|-----------|
| `nvidia-smi`, `nvcc`, `nvprof`, `cuda`, GPU commands | **Modern Dark** (Windows Terminal / GNOME Dark) | Server/GPU environments look best in modern dark terminals |
| `gcc`, `make`, `gdb`, `vim`, kernel code, `objdump` | **Green Phosphor CRT** | Classic hacker/developer aesthetic |
| `pip`, `npm`, `brew`, `apt`, package managers | **macOS Terminal Pro** or **Modern Dark** | Developer tooling, modern feel |
| Windows commands (`dir`, `ipconfig`, `ping`, `chkdsk`) | **Windows Terminal Campbell** | Native Windows feel |
| macOS-specific (`brew`, `xcodebuild`, `launchctl`) | **macOS Terminal Pro** | Native macOS feel |
| Retro/game/hacking context | **Amber Phosphor CRT** | Warmer retro feel |
| User explicitly requests a style | Use that style directly | User intent overrides all heuristics |

If uncertain, default to **Modern Dark** (GNOME Dark variant) — it's the most versatile.

## Step 2: Select Color Scheme and Effects

From `references/terminal-types.md`, obtain:
- Foreground/background hex colors
- ANSI 16-color palette (if applicable)
- CRT effects CSS classes (if applicable)
- Window chrome style (macOS / Windows / CRT monitor)

**CRT effects are always enabled** for phosphor-based terminals (green, amber, white, red).
Modern terminals use clean rendering without scanlines.

**Window decorations** (title bar, buttons, border):
- Apply when: the screenshot has **>40 lines** of output, or represents a **full terminal session**
- Skip when: the output is **small** (a single command or few lines), or the user asks for "just the content"
- Rationale: large outputs look better framed; small snippets look cleaner bare

## Step 3: Build HTML

Use the templates in `references/html-templates.md` as the base. These are production-ready
HTML/CSS snippets for each terminal type.

Key rules:
- **Every template includes `overflow: hidden` on html/body** — no scrollbars appear
- Terminal window is fixed at **740px width** (80 columns × 14px font) for realistic proportions
- Set `<body>` background to `#2a2a2a` so the terminal window stands out
- Wrap content in the appropriate window chrome div structure
- Use `<span>` with CSS classes (`.prompt`, `.cmd`, `.output`, `.stderr`) to color parts
- For multi-command sessions, separate each command block with a blank line
- Font stack: `'Consolas', 'Courier New', 'Microsoft YaHei', monospace`
- Font size: 14px, line-height: 1.4 (matches real terminal density)

## Step 4: Convert to PNG

Run `scripts/html_to_png.py` with the HTML file path. The script auto-detects available
tools in this order:

1. **Playwright** (Chromium/Edge) — best quality, supports all CSS
2. **Puppeteer** (Chrome/Chromium) — equivalent quality
3. **Edge headless** (direct `msedge.exe --headless --screenshot`) — no npm required
4. **wkhtmltoimage** — fallback, limited CSS support

The script outputs the PNG path on success. If all tools fail, it reports what's missing
so the user can install one.

## Step 5: Deliver

- Always deliver the **PNG** as the primary output
- Keep the HTML file alongside the PNG so the user can tweak and re-render
- Name files descriptively: `terminal_<description>.png` / `.html`
- Clean up temporary HTML only if the user explicitly asks
