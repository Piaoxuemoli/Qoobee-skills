# terminal-screenshot

将终端命令输出渲染为逼真的 PNG 截图。支持多种终端风格、自动检测渲染工具、复古终端的 CRT 效果。

Render terminal command output as realistic PNG screenshots. Multiple terminal styles,
auto-detection of rendering tools, CRT effects for retro terminals.

## 快速示例 / Quick Example

```bash
# CLI 用法 / CLI usage
python terminal-screenshot/scripts/html_to_png.py example.html example.png
```

![Example](terminal-screenshot/example.png)

> macOS Terminal Pro 风格，通过 Edge headless 生成。内容：CUDA 向量加法实验的编译、执行及 Tesla T4 上的 nvprof 性能分析。
>
> macOS Terminal Pro style, generated via Edge headless. Content: CUDA vector addition
> experiment compilation, execution, and nvprof performance analysis on Tesla T4.

## 支持的终端类型 / Supported Terminal Types

| 类型 / Type | 风格 / Style | 效果 / Effects |
|-------------|-------------|----------------|
| 绿色荧光 CRT | 黑 `#0A0A0A` + 绿 `#33FF33` | 扫描线、发光、暗角 |
| 琥珀色荧光 CRT | 黑 + 琥珀 `#FFB000` | 扫描线、发光、暗角 |
| 现代暗色 (GNOME) | `#1E1E1E` + `#D4D4D4` | 简洁 |
| macOS 终端专业版 | `#1E1E1E` + `#D4D4D4` | 红绿灯按钮 |
| Windows 终端 | `#0C0C0C` + `#CCCCCC` | 标签栏、窗口按钮 |
| xterm 亮色 | 白 + 黑 | 简洁 |

> | Type | Style | Effects |
> |------|-------|---------|
> | Green Phosphor CRT | Black `#0A0A0A` + Green `#33FF33` | Scanlines, glow, vignette |
> | Amber Phosphor CRT | Black + Amber `#FFB000` | Scanlines, glow, vignette |
> | Modern Dark (GNOME) | `#1E1E1E` + `#D4D4D4` | Clean |
> | macOS Terminal Pro | `#1E1E1E` + `#D4D4D4` | Traffic light buttons |
> | Windows Terminal | `#0C0C0C` + `#CCCCCC` | Tab bar, caption buttons |
> | xterm Light | White + Black | Clean |

## 安装 / Installation

将 skill 目录复制到 `~/.claude/skills/terminal-screenshot/`：

Copy the skill directory to `~/.claude/skills/terminal-screenshot/`:

```bash
cp -r terminal-screenshot ~/.claude/skills/
```

或作为项目本地 skill：

Or for a project-local skill:

```bash
cp -r terminal-screenshot /path/to/project/.claude/skills/
```

## 依赖要求 / Requirements

至少需要一种截图工具：

At least one screenshot tool:

| 工具 / Tool | 安装 / Install |
|------------|----------------|
| **Playwright**（推荐 / best） | `pip install playwright && playwright install chromium` |
| **Puppeteer** | `npm install puppeteer` |
| **Edge headless** | Windows 10+ 内置 |
| **Chrome headless** | `google-chrome` / `chromium` |

按上述顺序自动检测，失败时自动降级。

Auto-detected in that order. Falls back gracefully.

## 工作原理 / How It Works

1. **检测终端类型** — 基于命令内容启发式判断（GPU→现代暗色, gcc→绿色 CRT 等）
2. **选择配色方案** — 来自 `terminal-screenshot/references/terminal-types.md`（8 种类型，完整十六进制色板）
3. **构建 HTML** — 使用 `terminal-screenshot/references/html-templates.md` 中的模板
4. **转换为 PNG** — 通过 `terminal-screenshot/scripts/html_to_png.py`，带多工具降级链

> 1. **Detect terminal type** — heuristics based on command content (GPU→Modern Dark, gcc→Green CRT, etc.)
> 2. **Select color scheme** — from `terminal-screenshot/references/terminal-types.md` (8 types, full hex palettes)
> 3. **Build HTML** — using templates from `terminal-screenshot/references/html-templates.md`
> 4. **Convert to PNG** — via `terminal-screenshot/scripts/html_to_png.py` with multi-tool fallback

## 文件结构 / File Structure

```
Qoobee-skills/
├── README.md
└── terminal-screenshot/
    ├── SKILL.md                    # 主 skill 说明 / Main skill instructions
    ├── example.png                 # 样例输出 / Sample output
    ├── references/
    │   ├── terminal-types.md       # 色板与自动检测规则 / Color palettes & auto-detection rules
    │   └── html-templates.md       # 6 个 HTML/CSS 模板 (A-F) / 6 HTML/CSS templates (A-F)
    ├── scripts/
    │   └── html_to_png.py          # HTML→PNG 转换器（带降级链） / HTML→PNG converter with fallback chain
    └── assets/                     # （预留 / reserved）
```

## 许可证 / License

MIT
