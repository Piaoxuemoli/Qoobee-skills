# terminal-screenshot

将终端命令输出渲染为逼真的 PNG 截图。支持多种终端风格、自动配置渲染工具、复古终端的 CRT 效果。

Render terminal command output as realistic PNG screenshots. Multiple terminal styles,
auto-configuring rendering tools, CRT effects for retro terminals.

## 快速示例 / Quick Example

```bash
python terminal-screenshot/scripts/html_to_png.py example.html example.png
```

![Example](example.png)

> macOS Terminal Pro 风格，通过 Playwright 生成。内容：CUDA 向量加法实验的编译、执行及 Tesla T4 上的 nvprof 性能分析。
>
> macOS Terminal Pro style, generated via Playwright. Content: CUDA vector addition
> experiment compilation, execution, and nvprof performance analysis on Tesla T4.

## 支持的终端类型 / Supported Terminal Types

| 类型 / Type | 风格 / Style | 效果 / Effects |
|-------------|-------------|----------------|
| 绿色荧光 CRT | 黑 + 绿 `#33FF33` | 扫描线、发光、暗角 |
| 琥珀色荧光 CRT | 黑 + 琥珀 `#FFB000` | 扫描线、发光、暗角 |
| 现代暗色 (GNOME) | `#1E1E1E` + `#D4D4D4` | 简洁 |
| macOS 终端专业版 | `#1E1E1E` + `#D4D4D4` | 红绿灯按钮 |
| Windows 终端 | `#0C0C0C` + `#CCCCCC` | 标签栏、窗口按钮 |
| xterm 亮色 | 白 + 黑 | 简洁 |

> | Type | Style | Effects |
> |------|-------|---------|
> | Green Phosphor CRT | Black + Green `#33FF33` | Scanlines, glow, vignette |
> | Amber Phosphor CRT | Black + Amber `#FFB000` | Scanlines, glow, vignette |
> | Modern Dark (GNOME) | `#1E1E1E` + `#D4D4D4` | Clean |
> | macOS Terminal Pro | `#1E1E1E` + `#D4D4D4` | Traffic light buttons |
> | Windows Terminal | `#0C0C0C` + `#CCCCCC` | Tab bar, caption buttons |
> | xterm Light | White + Black | Clean |

## 安装 / Installation

复制到 `~/.claude/skills/terminal-screenshot/`：

Copy to `~/.claude/skills/terminal-screenshot/`:

```bash
cp -r terminal-screenshot ~/.claude/skills/
```

## 渲染工具 / Rendering Tools

脚本自动按以下优先级获取渲染工具：

The script resolves rendering tools with this priority:

1. **自动配置 / Auto-config** — 尝试 `pip install playwright` + `playwright install chromium`（最多重试 3 次）/ attempts to install Playwright (up to 3 retries)
2. **降级 / Fallback** — 检测系统已有工具：Edge headless → Chrome headless → wkhtmltoimage / detects existing system tools
3. **跳过 / Skip** — 全部不可用时跳过截图，不阻塞工作流 / skips screenshots gracefully if nothing works

## 工作原理 / How It Works

1. **检测终端类型** — 基于命令内容启发式判断（GPU→现代暗色, gcc→绿色 CRT 等）
2. **选择配色方案** — 来自 `references/terminal-types.md`（8 种类型，完整十六进制色板）
3. **构建 HTML** — 使用 `references/html-templates.md` 中的模板
4. **转换为 PNG** — 通过 `scripts/html_to_png.py`，自动配置 → 降级 → 跳过

> 1. **Detect terminal type** — heuristics based on command content (GPU→Modern Dark, gcc→Green CRT, etc.)
> 2. **Select color scheme** — from `references/terminal-types.md` (8 types, full hex palettes)
> 3. **Build HTML** — using templates from `references/html-templates.md`
> 4. **Convert to PNG** — via `scripts/html_to_png.py` with auto-config → fallback → skip

## 文件结构 / File Structure

```
terminal-screenshot/
├── README.md
├── SKILL.md                    # Skill 指令 / Skill instructions
├── example.png                 # 样例输出 / Sample output
├── references/
│   ├── terminal-types.md       # 色板与检测规则 / Color palettes & detection rules
│   └── html-templates.md       # HTML/CSS 模板 / HTML/CSS templates
├── scripts/
│   └── html_to_png.py          # HTML→PNG 转换器 / converter with auto-config + fallback
└── assets/                     # 预留 / reserved
```

## 许可证 / License

MIT
