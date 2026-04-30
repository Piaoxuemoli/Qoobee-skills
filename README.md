# Qoobee Skills

Claude Code 技能集合 — 自动化实验报告、终端截图等常用工作流。

A collection of Claude Code skills — automating lab reports, terminal screenshots, and other common workflows.

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
把这段 PowerShell 输出渲染成终端截图
```

Agent 会根据 skill 描述自动选择 `lab-report` 或 `terminal-screenshot`。如果没有自动触发，可以明确点名：

```text
使用 terminal-screenshot skill，把这段终端输出做成 PNG
```

---

## Skills

### [lab-report](lab-report/) — [详细文档](docs/lab-report.md)

实验报告全流程自动化：首次配置个人信息，本地复用；支持自动模式、Anthropic 官方文件处理 skills 检查，以及可执行实验、已有数据、纯写作三类报告路径。

Automate lab reports with reusable local profile data, optional auto mode, official document-skill checks, and three paths: executable experiments, provided-data reports, and paper-only writeups.

### [terminal-screenshot](terminal-screenshot/) — [详细文档](docs/terminal-screenshot.md)

将终端命令输出渲染为逼真的 PNG 截图。支持 PowerShell、macOS zsh、Linux/SSH 等高保真模板，自动配置渲染工具，并按时间分区保存输出。

Render terminal command outputs as realistic PNG screenshots. High-fidelity templates for PowerShell, macOS zsh, Linux/SSH, auto-configuring rendering tools, and time-partitioned outputs.

![terminal-screenshot 示例 / Example](terminal-screenshot/example.png)

---

## 结构 / Structure

```
Qoobee-skills/
├── README.md
├── docs/                   # 详细文档（与 skill 代码分离）
│   ├── lab-report.md
│   └── terminal-screenshot.md
├── lab-report/             # 实验报告 skill 代码
│   ├── SKILL.md
│   └── ...
└── terminal-screenshot/    # 终端截图 skill 代码
    ├── SKILL.md
    └── ...
```

每个 skill 的 SKILL.md 是 Claude Code 自动加载的技能指令文件，详细文档在 `docs/` 目录中。

Each skill's SKILL.md is the instruction file loaded by Claude Code. Detailed docs live in `docs/`, separated from skill code.
