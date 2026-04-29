# terminal-screenshot

Render terminal command output as realistic PNG screenshots. Multiple terminal styles,
auto-detection of rendering tools, CRT effects for retro terminals.

## Quick Example

```bash
# CLI usage
python terminal-screenshot/scripts/html_to_png.py example.html example.png
```

![Example](terminal-screenshot/example.png)

> macOS Terminal Pro style, generated via Edge headless. Content: CUDA vector addition
> experiment compilation, execution, and nvprof performance analysis on Tesla T4.

## Supported Terminal Types

| Type | Style | Effects |
|------|-------|---------|
| Green Phosphor CRT | Black `#0A0A0A` + Green `#33FF33` | Scanlines, glow, vignette |
| Amber Phosphor CRT | Black + Amber `#FFB000` | Scanlines, glow, vignette |
| Modern Dark (GNOME) | `#1E1E1E` + `#D4D4D4` | Clean |
| macOS Terminal Pro | `#1E1E1E` + `#D4D4D4` | Traffic light buttons |
| Windows Terminal | `#0C0C0C` + `#CCCCCC` | Tab bar, caption buttons |
| xterm Light | White + Black | Clean |

## Installation

Copy the skill directory to `~/.claude/skills/terminal-screenshot/`:

```bash
cp -r terminal-screenshot ~/.claude/skills/
```

Or for a project-local skill:

```bash
cp -r terminal-screenshot /path/to/project/.claude/skills/
```

## Requirements

At least one screenshot tool:

| Tool | Install |
|------|---------|
| **Playwright** (best) | `pip install playwright && playwright install chromium` |
| **Puppeteer** | `npm install puppeteer` |
| **Edge headless** | Built-in on Windows 10+ |
| **Chrome headless** | `google-chrome` / `chromium` |

Auto-detected in that order. Falls back gracefully.

## How It Works

1. **Detect terminal type** — heuristics based on command content (GPU→Modern Dark, gcc→Green CRT, etc.)
2. **Select color scheme** — from `terminal-screenshot/references/terminal-types.md` (8 types, full hex palettes)
3. **Build HTML** — using templates from `terminal-screenshot/references/html-templates.md`
4. **Convert to PNG** — via `terminal-screenshot/scripts/html_to_png.py` with multi-tool fallback

## File Structure

```
Qoobee-skills/
├── README.md
└── terminal-screenshot/
    ├── SKILL.md                    # Main skill instructions
    ├── example.png                 # Sample output
    ├── references/
    │   ├── terminal-types.md       # Color palettes & auto-detection rules
    │   └── html-templates.md       # 6 HTML/CSS templates (A-F)
    ├── scripts/
    │   └── html_to_png.py          # HTML→PNG converter with fallback chain
    └── assets/                     # (reserved)
```

## License

MIT
