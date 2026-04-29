# Qoobee Skills

Claude Code 技能集合 — 自动化实验报告、终端截图等常用工作流。

A collection of Claude Code skills — automating lab reports, terminal screenshots, and other common workflows.

---

## Skills

### [lab-report](lab-report/) — [详细文档](docs/lab-report.md)

实验报告全流程自动化：从实验手册提取流程 → 生成模板 → 执行实验并截图 → 完成最终报告。

Automate the full lab-report pipeline: extract procedures from source materials → generate templates → execute experiments with screenshots → produce the final report.

### [terminal-screenshot](terminal-screenshot/) — [详细文档](docs/terminal-screenshot.md)

将终端命令输出渲染为逼真的 PNG 截图。支持多种终端风格、CRT 效果，自动配置渲染工具。

Render terminal command outputs as realistic PNG screenshots. Multiple terminal styles, CRT effects, auto-configuring rendering tools.

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
