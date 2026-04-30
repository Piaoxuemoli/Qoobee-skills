# lab-report

实验报告全流程自动化技能。支持首次本地配置个人信息、自动模式，以及三种报告路径：可执行实验、已有数据、纯写作报告。

Automate lab reports with a local profile cache, optional auto mode, and three report paths:
executable experiments, reports with provided data, and paper-only writeups.

## 工作流 / Workflow

```text
启动配置 → 判断报告路径 → 材料总结 → 草稿/执行/导入数据 → 最终报告
Startup → Classify path → Summarize → Draft/Execute/Import data → Final report
```

| 路径 / Path | 适用场景 / Use case | 是否执行命令 / Runs commands |
|-------------|---------------------|------------------------------|
| `standard-executable` | 实验材料包含可执行步骤或命令 / materials include executable steps | 是 / Yes |
| `data-provided` | 用户已有数据、截图、日志或表格 / user already has data or logs | 否 / No |
| `paper-only` | 理论报告、课程报告、实验总结 / theoretical or writing-only report | 否 / No |

## 首次配置 / First-Time Profile

首次运行时，skill 会一次性收集常用基础信息，并保存到本地：

```text
~/.qoobee-skills/lab-report/profile.json
```

缓存字段包括姓名、学号、班级、课程、指导老师和学校。后续实验报告会自动预填这些信息，避免每次重复询问。

On first use, the skill stores reusable profile fields locally: name, student ID, class,
course, instructor, and institution. Later reports reuse this profile automatically.

## 自动模式 / Auto Mode

启动时会询问是否进入无需确认的自动模式。开启后，skill 会自动推进模板生成、普通实验步骤执行和最终报告生成。

自动模式仍会在以下情况打断用户：

- 缺少实验材料或必要结果数据
- 实验步骤含糊，无法安全执行
- 命令失败且阻塞后续流程
- 涉及删除、提权、系统修改等危险操作

Auto mode skips routine confirmations after startup. It still stops for missing data,
ambiguous steps, blocking command failures, or destructive operations.

## 子代理架构 / Sub-Agent Architecture

仿照 skill-creator 的子代理模式，三个子代理协同工作：

Modeled after skill-creator's sub-agent pattern, three agents work together:

| 子代理 / Agent | 文件 / File | 职责 / Role |
|---------------|------------|-------------|
| 实验总结器 / Experiment Summarizer | `agents/experiment-summarizer.md` | 读取材料，按报告路径产出结构化摘要 / Read sources and summarize by report path |
| 报告写作器 / Report Writer | `agents/report-writer.md` | 生成草稿并填充最终报告 / Generate drafts and final reports |
| 实验执行器 / Experiment Runner | `agents/experiment-runner.md` | 仅服务可执行实验路径，执行命令并截图 / Run executable experiments only |

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

Skill 会自动触发，先判断报告路径，再选择合适的流程。

The skill auto-triggers, classifies the report path, and runs the matching workflow.

## 文件结构 / File Structure

```
lab-report/
├── SKILL.md                         # 主编排器 / Main orchestrator
├── agents/
│   ├── experiment-summarizer.md     # 子代理1: 总结流程 / Summarize procedure
│   ├── report-writer.md             # 子代理2: 写报告 / Write report
│   └── experiment-runner.md         # 子代理3: 执行实验 / Execute experiment
├── references/
│   ├── file-readers.md              # 文件读取策略 / File reading strategies
│   ├── report-template-zh.md        # 中文默认模板 / Default Chinese template
│   ├── report-template-en.md        # 英文默认模板 / Default English template
│   └── schemas.md                   # 数据结构约定 / Shared schemas
├── scripts/
│   ├── init_output_dir.py           # 输出目录初始化 / Output dir initializer
│   └── profile_config.py            # 本地基础信息缓存 / local profile cache
├── assets/
└── outputs/                         # 用户输出（gitignored） / User outputs (gitignored)
```

输出目录示例 / Output directory example:

```text
outputs/<experiment-name>/
├── report_context.json
├── experiment_info.json
├── procedure_summary.md
├── report_draft.md
├── run_log.md
├── final_report.md
├── screenshots/
└── raw_outputs/
```

## 依赖 / Dependencies

- **terminal-screenshot** — 用于 Phase 3 截图 / For Phase 3 screenshot capture
- Python 3 — 运行初始化脚本 / Run init script
- 可选 / Optional: `pdftotext`, `python-docx`, `python-pptx` — 用于文件解析 / For file parsing

## 许可证 / License

MIT
