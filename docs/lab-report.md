# lab-report

实验报告全流程自动化技能。支持首次本地配置个人信息、学生友好入口、材料目录导入、自动模式、官方文件处理 skills 检查、课程模板记忆、证据映射，以及三种报告路径：可执行实验、已有数据、纯写作报告。

Automate lab reports with a local profile cache, student-friendly intake, material-folder
import, optional auto mode, official document-skill checks, course template memory, evidence
mapping, and three report paths: executable experiments, reports with provided data, and
paper-only writeups.

## 工作流 / Workflow

```text
入口向导 → 材料分类 → 判断报告路径 → 材料总结 → 草稿/执行/导入数据 → 证据映射 → 最终交付
Intake → Index materials → Classify path → Summarize → Draft/Execute/Import data → Evidence map → Delivery
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

自动模式下，普通实验命令失败不会频繁打断用户；skill 会跳过依赖失败结果的步骤，继续处理可独立完成的内容，并在最终交付时说明哪些步骤失败或跳过。

自动模式仍会在以下情况打断用户：

- 缺少实验材料或必要结果数据
- 实验步骤含糊，无法安全执行
- 涉及删除、提权、系统修改等危险操作
- 最终报告会缺少必要数据或留下 unresolved placeholders

Auto mode skips routine confirmations after startup. Ordinary command failures are summarized
at delivery time. It still stops for missing required data, ambiguous steps, destructive
operations, or unresolved final placeholders.

## 学生友好入口 / Student-Friendly Intake

你可以直接给一个材料目录：

```text
帮我写实验报告，材料都在 ./lab3-materials，进入无感模式，最后给我 Word 和 PDF。
```

skill 会自动整理材料并生成 `source_manifest.json`：

```bash
python lab-report/scripts/index_source_files.py --inputs "./lab3-materials" --output "<output_dir>/source_manifest.json"
```

材料会被归类为实验说明、PPT、数据表、截图/图片、日志、代码和其他文件，后续 summarizer 会按类别优先读取。

## 课程模板记忆 / Course Template Memory

如果老师有固定格式，可以让 skill 记住课程模板：

```text
以后《计算机网络》都用这个模板。
```

底层脚本会把模板索引保存到：

```text
~/.qoobee-skills/lab-report/course_templates.json
```

报告写作时优先级为：课程模板 → 本次用户提供模板 → 内置默认模板。

内置默认模板采用标准大学实验报告格式（10 节结构）：实验名称、实验项目名称、实验目的、实验内容、实验器材、实验步骤及操作、实验数据及结果分析、实验结论、总结及心得体会、改进建议，含学校/学院抬头和评分/签字栏。导出 DOCX 时自动应用大学报告排版规范（标题居中加粗大号、正文宋体/Times New Roman 12pt、表头加粗、标准学术页边距）。

## 文件处理能力 / File Processing

在读取实验材料前，skill 会检查用户环境中是否已安装 Anthropic 官方文件处理 skills：

```bash
python lab-report/scripts/check_official_skills.py --source-files "<path1>|<path2>"
```

如缺失，skill 会尝试通过 OpenSkill 自动安装：

```bash
python lab-report/scripts/check_official_skills.py --install --source-files "<path1>|<path2>"
```

支持映射如下：

| 文件格式 / Format | 官方 skill / Official skill |
|-------------------|-----------------------------|
| `.pdf` | `pdf` |
| `.doc`, `.docx` | `docx` |
| `.ppt`, `.pptx` | `pptx` |
| `.xls`, `.xlsx`, `.xlsm`, `.csv`, `.tsv` | `xlsx` |

如果当前机器没有 `npx`/Node.js，自动安装会停止并提示用户补齐环境，避免在缺少对应 skill 时硬解析文件。

## 子代理架构 / Sub-Agent Architecture

仿照 skill-creator 的子代理模式，三个子代理协同工作：

Modeled after skill-creator's sub-agent pattern, three agents work together:

| 子代理 / Agent | 文件 / File | 职责 / Role |
|---------------|------------|-------------|
| 实验总结器 / Experiment Summarizer | `agents/experiment-summarizer.md` | 读取材料，按报告路径产出结构化摘要和证据映射 / Read sources, summarize, and map evidence |
| 报告写作器 / Report Writer | `agents/report-writer.md` | 生成草稿、最终报告、DOCX/PDF 和交付清单 / Generate drafts, final reports, exports, and delivery manifest |
| 实验执行器 / Experiment Runner | `agents/experiment-runner.md` | 仅服务可执行实验路径，执行命令、截图并记录失败 / Run executable experiments and record failures |

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

> "帮我整理 ./lab3-materials 这个文件夹，按计算机网络课程模板写实验报告，最后导出 Word 和 PDF"

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
│   ├── report-template-zh.md        # 中文默认模板（标准大学10节格式）/ Default Chinese template
│   ├── report-template-en.md        # 英文默认模板（标准大学10节格式）/ Default English template
│   └── schemas.md                   # 数据结构约定 / Shared schemas
├── scripts/
│   ├── check_official_skills.py     # Anthropic 官方文件 skills 检查 / Official file skills check
│   ├── course_templates.py          # 课程模板记忆 / Course template memory
│   ├── index_source_files.py        # 材料目录索引 / Source material indexing
│   ├── init_output_dir.py           # 输出目录初始化 / Output dir initializer
│   └── profile_config.py            # 本地基础信息缓存 / local profile cache
├── assets/
└── outputs/                         # 用户输出（gitignored） / User outputs (gitignored)
```

输出目录示例 / Output directory example:

```text
outputs/<experiment-name>/
├── report_context.json
├── source_manifest.json
├── experiment_info.json
├── procedure_summary.md
├── evidence_map.md
├── report_draft.md
├── run_log.md
├── final_report.md
├── final_report.docx
├── final_report.pdf
├── delivery_manifest.json
├── screenshots/
└── raw_outputs/
```

`evidence_map.md` 会标明关键段落、数据、截图和结论来自哪里。`delivery_manifest.json` 会列出最终交付文件，以及自动模式下失败、跳过或未导出的内容。

## 依赖 / Dependencies

- **terminal-screenshot** — 用于可执行实验截图 / For executable experiment screenshots
- **Anthropic official skills** — `pdf`, `docx`, `pptx`, `xlsx` for source file processing
- **OpenSkill / npx skills** — 用于自动补装缺失官方 skills / Install missing official skills
- Python 3 — 运行初始化脚本 / Run init script
- 可选 / Optional: `pdftotext`, `python-docx`, `python-pptx`, `pandoc` — fallback parsers

## 许可证 / License

MIT
