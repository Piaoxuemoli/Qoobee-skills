# lab-report

实验报告全流程自动化技能。从实验材料中提取流程，生成模板，执行实验并截图，最终完成报告。

Automate the full experiment-report pipeline: extract procedures from source materials,
generate report templates, execute experiments with terminal screenshots, and produce
the final report.

## 工作流 / Workflow

```
实验材料 (PDF/PPT/Word) → 总结流程 → 生成模板 → 执行实验+截图 → 完成报告
Source materials → Summarize → Template → Execute+Screenshot → Final report
```

| 阶段 / Phase | 说明 / Description |
|-------------|-------------------|
| 0 — 初始化 / Setup | 创建输出目录 / Initialize output directory |
| 1 — 总结 / Summarize | 从实验材料提取流程，确认个人信息 / Extract procedure, confirm metadata |
| 2 — 模板 / Template | 生成带占位符的报告草稿 / Generate draft with placeholders |
| 3 — 执行 / Execute | 逐步执行实验命令，调用 terminal-screenshot 截图 / Run experiment step-by-step |
| 4 — 完成 / Complete | 用实际结果和截图填充最终报告 / Fill in final report with real data |

## 子代理架构 / Sub-Agent Architecture

仿照 skill-creator 的子代理模式，三个子代理协同工作：

Modeled after skill-creator's sub-agent pattern, three agents work together:

| 子代理 / Agent | 文件 / File | 职责 / Role |
|---------------|------------|-------------|
| 实验总结器 / Experiment Summarizer | `agents/experiment-summarizer.md` | 读取 PDF/DOCX/PPTX，提取实验流程，收集个人信息 / Read source files, extract procedure, collect metadata |
| 报告写作器 / Report Writer | `agents/report-writer.md` | 双模式：生成模板 + 填充结果 / Dual-mode: template generation + final fill-in |
| 实验执行器 / Experiment Runner | `agents/experiment-runner.md` | 逐步执行命令，调用 terminal-screenshot 截图 / Execute commands step-by-step, capture screenshots |

## 快速开始 / Quick Start

### 1. 安装 / Installation

```bash
cp -r lab-report ~/.claude/skills/
```

### 2. 使用 / Usage

在 Claude Code 中说：

Say this in Claude Code:

> "帮我写一份实验报告，实验手册是 lab3.pdf"

> "Write a lab report for my experiment, the lab manual is lab3.pdf"

Skill 会自动触发，引导你完成四个阶段。

The skill auto-triggers and guides you through all four phases.

## 文件结构 / File Structure

```
lab-report/
├── README.md
├── SKILL.md                         # 主编排器 / Main orchestrator
├── agents/
│   ├── experiment-summarizer.md     # 子代理1: 总结流程 / Summarize procedure
│   ├── report-writer.md             # 子代理2: 写报告 / Write report
│   └── experiment-runner.md         # 子代理3: 执行实验 / Execute experiment
├── references/
│   ├── file-readers.md              # 文件读取策略 / File reading strategies
│   ├── report-template-zh.md        # 中文默认模板 / Default Chinese template
│   └── report-template-en.md        # 英文默认模板 / Default English template
├── scripts/
│   └── init_output_dir.py           # 输出目录初始化 / Output dir initializer
├── assets/
└── outputs/                         # 用户输出（gitignored） / User outputs (gitignored)
```

## 依赖 / Dependencies

- **terminal-screenshot** — 用于 Phase 3 截图 / For Phase 3 screenshot capture
- Python 3 — 运行初始化脚本 / Run init script
- 可选 / Optional: `pdftotext`, `python-docx`, `python-pptx` — 用于文件解析 / For file parsing

## 许可证 / License

MIT
