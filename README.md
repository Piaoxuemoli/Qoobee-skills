# Auto-college

一套 Claude Code / Cursor Skills，让 AI 帮你搞定大学课程作业——实验报告、水课 PPT、小论文、读书报告、课堂展示稿、终端截图、开卷考试资料整理，从材料到成品一步到位。

A collection of Claude Code / Cursor Skills that automate college coursework — lab reports, lecture slides, short papers, reading reports, presentation scripts, terminal screenshots, and open-book exam preparation — from raw materials to polished deliverables in one step.

---

## 快速配置 / Quick Start

把本仓库的 skill 目录复制或 clone 到你的 Agent skills 路径：

| 环境 | Skills 路径 |
|------|------------|
| Claude Code | `.claude/commands/` （项目级）或 `~/.claude/commands/` （全局） |
| Cursor | `.cursor/skills/` （项目级）或 `~/.cursor/skills/` （全局） |
| 其他 | 参考对应平台的 custom instructions / skills 文档 |

```bash
# 示例：clone 到项目的 .claude/commands/
git clone https://github.com/Piaoxuemoli/Auto-college.git /tmp/auto-college
cp -r /tmp/auto-college/coursework-helper /tmp/auto-college/lab-report /tmp/auto-college/terminal-screenshot /tmp/auto-college/study-index .claude/commands/
```

配置完成后，直接在对话中描述任务即可：

```text
帮我根据实验手册生成实验报告
```

```text
帮我把这门通识课作业整理成 PPT 和小论文
```

```text
把这段 PowerShell 输出渲染成终端截图
```

```text
帮我整理这些 PPT 和文档，做成开卷考试速查手册
```

Agent 会自动匹配对应 skill。也可以明确指定：

```text
使用 terminal-screenshot skill，把这段终端输出做成 PNG
```

---

## Skills

### lab-report

实验报告全流程自动化：个人信息本地复用、材料目录一键导入、自动模式、课程模板记忆、证据映射。内置标准大学实验报告模板（10 节结构），导出 DOCX 自动应用学术排版。

Automate lab reports with reusable profile data, material-folder intake, auto mode, course template memory, and evidence maps. Standard university format (10-section) with academic styling on DOCX export.

### coursework-helper

通识课 / 选修课作业一键生成：PPT（15 个模板 + 主题系统 + Slidev 可选）、小论文、读书报告、观后感、演讲稿。内置 PPT 引擎，Markdown slide card 直接导出带 speaker notes 的 PPTX。视频链接默认 Bilibili 等国内平台。

Generate deliverables for general education coursework: slides (15 templates + theme system + optional Slidev), short papers, reading reports, reflection essays, and speech scripts. Built-in PPT engine exports styled PPTX with speaker notes from structured Markdown.

### terminal-screenshot

终端命令输出渲染为逼真 PNG 截图。支持 PowerShell、macOS zsh、Linux/SSH 高保真模板。

Render terminal command outputs as realistic PNG screenshots. High-fidelity templates for PowerShell, macOS zsh, and Linux/SSH.

![terminal-screenshot 示例 / Example](terminal-screenshot/example.png)

### study-index — [详细文档](docs/study-index.md)

将散乱的课程材料（PPT、PDF、文档、笔记）整理成一本带目录、带索引、带例题、带关键图片的速查手册。核心原则：不丢失信息——源材料中的关键图片、公式、图表必须提取并放到手册对应位置。输出 Markdown + PDF（可打印）。

Organize scattered course materials (PPTs, PDFs, documents, notes) into an indexed study handbook with table of contents, key images, formulas, and example problems. Core principle: no information loss — key images and diagrams are extracted and placed at the correct position. Outputs Markdown + PDF (printable).

---

![GitHub stars](https://img.shields.io/github/stars/Piaoxuemoli/Auto-college?style=social)
![GitHub Created At](https://img.shields.io/github/created-at/Piaoxuemoli/Auto-college)
