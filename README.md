# Qoobee Skills

Claude Code 技能集合 — 自动化实验报告、课程作业、终端截图等常用工作流。

A collection of Claude Code skills — automating lab reports, coursework deliverables, terminal screenshots, and other common workflows.

---

## 快速配置 / Quick Start

打开 Cursor / Claude Code，把下面这句话发给 Agent：

```text
下载 https://github.com/Piaoxuemoli/Qoobee-skills，并把里面的 skills 配置到我的 Agent 环境里
```

Agent 会下载仓库、识别 skill 目录，并按当前环境完成配置。

### 使用方式 / Usage

配置完成后，在 Agent 对话里直接描述任务即可：

```text
帮我根据实验手册生成实验报告
```

```text
帮我把这门通识课作业整理成 PPT 和小论文
```

```text
把这段 PowerShell 输出渲染成终端截图
```

Agent 会根据 skill 描述自动选择 `lab-report`、`coursework-helper` 或 `terminal-screenshot`。如果没有自动触发，可以明确点名：

```text
使用 terminal-screenshot skill，把这段终端输出做成 PNG
```

---

## Skills

### [lab-report](lab-report/) — [详细文档](docs/lab-report.md)

实验报告全流程自动化：首次配置个人信息，本地复用；支持材料目录一键导入、自动模式、课程模板记忆、证据映射、Anthropic 官方文件处理 skills 检查，以及可执行实验、已有数据、纯写作三类报告路径。内置模板采用标准大学实验报告格式（10 节结构），导出 DOCX 时自动应用学术排版规范。

Automate lab reports with reusable local profile data, material-folder intake, optional auto mode, course template memory, evidence maps, official document-skill checks, and three paths: executable experiments, provided-data reports, and paper-only writeups. Built-in templates follow standard university format (10-section), with academic styling auto-applied on DOCX export.

### [coursework-helper](coursework-helper/) — [详细文档](docs/coursework-helper.md)

面向大学通识课、选修课和低风险课程作业：快速生成 PPT、小论文、读书报告、观后感、课堂展示稿和演讲稿。内置 PPT 引擎（15 个模板、中文主题系统、slide card 解析器），支持 Markdown slide card 直接导出为带样式和 speaker notes 的 PPTX。支持材料目录索引、证据备注、Markdown/DOCX/PDF/PPTX 交付。

Create practical deliverables for general education and low-stakes coursework: slides, short papers, reading reports, reflection essays, classroom presentations, and speech scripts. Built-in PPT engine with 15 templates, Chinese theme system, and slide card parser — exports styled PPTX with speaker notes directly from structured Markdown.

### [terminal-screenshot](terminal-screenshot/) — [详细文档](docs/terminal-screenshot.md)

将终端命令输出渲染为逼真的 PNG 截图。支持 PowerShell、macOS zsh、Linux/SSH 等高保真模板，自动配置渲染工具，并按时间分区保存输出。

Render terminal command outputs as realistic PNG screenshots. High-fidelity templates for PowerShell, macOS zsh, Linux/SSH, auto-configuring rendering tools, and time-partitioned outputs.

![terminal-screenshot 示例 / Example](terminal-screenshot/example.png)

---

## 结构 / Structure

```
Qoobee-skills/
├── README.md
├── .claude/rules/          # 工作流规范（branching, references, readme）
├── docs/                   # 详细文档（与 skill 代码分离）
│   ├── coursework-helper.md
│   ├── lab-report.md
│   └── terminal-screenshot.md
├── coursework-helper/      # 通识课/水课作业 skill 代码
│   ├── SKILL.md
│   ├── engine/             # PPT 引擎（theme, builder, 15 templates, parser）
│   ├── agents/             # 子 agent 定义
│   ├── scripts/            # 工具脚本
│   └── ...
├── lab-report/             # 实验报告 skill 代码
│   ├── SKILL.md
│   └── ...
├── terminal-screenshot/    # 终端截图 skill 代码
│   ├── SKILL.md
│   └── ...
└── references/             # 外部参考代码（git-ignored）
    ├── mckinsey-pptx/
    ├── office-ppt-mcp/
    ├── supercurses-powerpoint/
    └── okppt/
```

每个 skill 的 SKILL.md 是 Claude Code 自动加载的技能指令文件，详细文档在 `docs/` 目录中。

Each skill's SKILL.md is the instruction file loaded by Claude Code. Detailed docs live in `docs/`, separated from skill code.
