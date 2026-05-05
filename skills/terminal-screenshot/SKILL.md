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

Render terminal command output as realistic PNG screenshots. Prefer a session-profile
approach: identify the operating system, shell, host context, and prompt grammar first,
then choose a visual preset. This avoids the common failure mode where every screenshot
looks like the same generic dark terminal with different text pasted into it.

## Workflow

```
User provides command + output (or asks to run a command)
  → Step 1: Determine session profile (OS + shell + local/remote host)
  → Step 2: Select the matching high-fidelity preset from references/terminal-types.md
  → Step 3: Build HTML using the matching template from references/html-templates.md
  → Step 4: Convert HTML to PNG using scripts/html_to_png.py
  → Step 5: Deliver the PNG, optionally keep the HTML
```

## Step 1: Determine Session Profile

Read `references/terminal-types.md` for the full catalog. First infer the session profile
from the content and surrounding user request:

| Content Signal | Session Profile | Use Preset |
|----------------|-----------------|------------|
| `PS C:\...>`, `pwsh`, `Get-ChildItem`, `Set-ExecutionPolicy`, `winget`, Windows paths | Local Windows PowerShell 7 | **Windows Terminal PowerShell 7** |
| `C:\...>`, `cmd.exe`, `dir`, `ipconfig`, `chkdsk` without `PS` | Windows Command Prompt | **Windows Terminal / cmd tab** |
| `brew`, `xcodebuild`, `launchctl`, `pbcopy`, `~/Library`, prompt ending in `%` | Local macOS zsh | **macOS Terminal zsh** |
| `ssh user@host`, prompt like `user@host:~/path$`, `sudo`, `systemctl`, `apt`, `journalctl`, GPU/server tools | Remote Linux server | **SSH Server Session** |
| `nvidia-smi`, `nvcc`, `nvprof`, `cuda`, `torchrun`, `deepspeed` | GPU server | **SSH Server Session** unless user says it is local |
| `gcc`, `make`, `gdb`, `vim`, `objdump` | Developer shell | **SSH Server Session** for Linux/server context, **macOS zsh** for macOS context |
| Retro/game/hacking context | Stylized retro terminal | **Green or Amber Phosphor CRT** |
| User explicitly requests a style | Use that style directly | User intent overrides all heuristics |

If uncertain, inspect the prompt text before choosing. `PS` means PowerShell, `%` usually
means zsh on macOS, `$`/`#` after `user@host:path` usually means Linux. If still uncertain,
default to **SSH Server Session** for experiment reports and technical docs, because most
terminal evidence in reports is remote Linux output rather than a local desktop terminal.

Do not make a "server" screenshot by inventing a separate server-looking GUI. Real server
work is normally shown through a local terminal window connected over SSH. The realistic
choice is therefore: local terminal chrome + remote Linux prompt.

## Step 2: Select Color Scheme and Effects

From `references/terminal-types.md`, obtain:
- Foreground/background hex colors
- ANSI 16-color palette (if applicable)
- Window chrome style (macOS / Windows / CRT monitor)
- Font stack and font size for that platform
- Prompt grammar and token colors for that shell
- CRT effects CSS classes only for retro presets

**CRT effects are always enabled** for phosphor-based terminals (green, amber, white, red).
Modern terminals use clean rendering without scanlines.

**Frame policy: choose one of two categories before writing HTML.**

1. **Full terminal session** — use window chrome. Choose this when the provided text includes
   startup banners, multiple prompts, an SSH login transition, tab/title context, or the user
   explicitly asks to simulate the whole terminal. PowerShell and macOS examples often belong
   here when the title bar is part of the request.
2. **Command evidence snippet** — do not use fake window chrome. Choose this for short command
   output, pasted Linux/server command results, single prompts, CI snippets, or anything meant
   to be embedded in a report. Use a clean terminal block instead.

Linux/server screenshots need special restraint: a remote server normally has no visible
desktop frame. If the text does not show the local SSH command or a full SSH session, render
it as a borderless command evidence snippet with Linux prompt styling. Only use the SSH Server
window frame when the screenshot intentionally includes the local terminal connected to SSH.

For remote SSH, choose the chrome from the user's local environment if known. On Windows, use
a Windows Terminal tab named after the remote host. On macOS, use Terminal.app with a title
like `user@host — ssh — 100x30`.

## Step 3: Build HTML

Use the templates in `references/html-templates.md` as the base. Prefer the high-fidelity
presets near the top of that file:

1. **Template P1: Windows Terminal PowerShell 7**
2. **Template M1: macOS Terminal zsh**
3. **Template S1: Remote Linux SSH Server**

The older generic templates remain available for fallbacks, CRT styling, or user-requested
looks.

Key rules:
- **Every template includes `overflow: hidden` on html/body** — no scrollbars appear
- Terminal window width should match the preset: PowerShell and server screenshots often
  look more real at 900-980px; macOS Terminal often looks best around 820-900px.
- Set `<body>` background to `#2a2a2a` so the terminal window stands out
- Wrap content in the appropriate window chrome div structure
- Use `<span>` with CSS classes (`.prompt`, `.cmd`, `.output`, `.stderr`) to color parts
- For multi-command sessions, separate each command block with a blank line
- Use platform fonts from the preset rather than a single universal stack
- Add a subtle block cursor (`<span class="cursor"></span>`) at the final prompt when the
  screenshot represents an interactive session
- For category 2 snippets, use the shell-specific body styling but omit the titlebar/tab
  controls entirely.

**Prompt and command formatting is more important than decorative chrome.** Match the shell:

```html
<!-- PowerShell -->
<span class="prompt">PS C:\Users\qoobee\Desktop\Qoobee-skills&gt;</span> <span class="ps-command">Get-ChildItem</span> <span class="ps-param">-Force</span>

<!-- macOS zsh -->
<span class="prompt">qoobee@MacBook-Pro Qoobee-skills %</span> <span class="cmd">brew install node</span>

<!-- Linux SSH -->
<span class="prompt"><span class="user">ubuntu</span>@<span class="host">gpu-a100-01</span>:<span class="path">~/train</span>$</span> <span class="cmd">nvidia-smi</span>
```

## Step 3.5: Run Quality Checks

Before converting to PNG, run the built-in checks in `scripts/html_to_png.py`. The renderer
prints `[quality-check]` warnings when the generated HTML looks visually suspect. Treat those
warnings as instructions to revise the HTML before accepting the screenshot.

Checks currently cover:
- **Chrome alignment:** Windows Terminal tab controls (`+` and dropdown) must be vertically
  centered; the active tab can sit on the bottom edge, but adjacent controls must not sag.
- **Frame policy:** very short content should not get a fake titlebar unless the input includes
  terminal startup/title context or the user asked for a full terminal simulation.
- **Linux/server restraint:** short Linux/server command output should be a clean snippet unless
  the text includes an SSH transition or a full remote session.
- **Prompt grammar:** PowerShell uses `PS ...>`, macOS zsh uses `%`, Linux SSH uses
  `user@host:path$` or `root@host:path#`.

## Step 4: Convert to PNG

Run `scripts/html_to_png.py` with the HTML file path and normally omit the output PNG path.
The script will create a time-partitioned output directory automatically:

```text
terminal-screenshot/
  outputs/
    YYYY-MM-DD/
      HHMMSS-description/
        description.html
        description.png
```

Recommended call:

```bash
python scripts/html_to_png.py path/to/source.html --name short-description
```

Only pass an explicit `output.png` when the user asks for a specific path. Keeping HTML and
PNG together in `outputs/` makes generated screenshots easy to find, compare, and delete.

The script handles tool availability in three phases with clear priorities:

### Phase A — Auto-Configuration (highest priority)

The script attempts to install **Playwright** automatically via `pip install playwright`
and `playwright install chromium`. This is the best quality tool and should always be
preferred. If installation fails, it retries up to **3 times** before giving up.

### Phase B — Fallback (lower priority)

Only if auto-configuration fails after 3 attempts, the script falls back to detecting
pre-installed tools on the system:

1. **Puppeteer** (Chrome/Chromium) — `node -e "require('puppeteer')"`
2. **Edge headless** (direct `msedge.exe --headless --screenshot`) — no npm required
3. **Chrome headless** — `google-chrome` / `chromium`
4. **wkhtmltoimage** — limited CSS support, last resort

### Phase C — Skip

If both auto-configuration AND all fallback tools fail, the script exits with code 2.
**This is not an error** — it means screenshots are unavailable for this session.
Simply tell the user "Screenshots are not available (no rendering tool found), continuing
without them" and proceed — do not block the workflow.

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | Screenshot generated successfully |
| 1 | Input error (HTML not found, etc.) |
| 2 | No tool available — skip screenshot and continue |

## Step 5: Deliver

- Always deliver the **PNG** as the primary output
- Keep the HTML file alongside the PNG in the same time-partitioned output directory so the
  user can tweak and re-render
- Name files descriptively with `--name`, for example `--name git-fetch-powershell`
- Report the output directory path, not just the PNG path
- Clean up temporary/source HTML only if the user explicitly asks
