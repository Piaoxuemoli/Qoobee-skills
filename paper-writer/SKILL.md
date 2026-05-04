---
name: paper-writer
description: >
  学术论文路由器：自动分析需求、按需加载 137 个专业 skills、调度子代理执行、
  格式检查、DOCX 导出。Use when the user mentions 小论文, 课程论文, IEEE,
  论文写作, 学术论文, 文献综述, literature review, paper writing,
  scientific paper, 研究报告, 学术报告.
---

# Paper Writer Router

学术论文写作的智能路由层。不自己实现具体能力，而是按需从 137 个专业 skills 中
加载所需能力，调度子代理执行，最后负责格式检查和 DOCX 导出。

## Architecture

```text
User request
  -> Analyze: 解析需求（任务类型、主题、字数、格式）
  -> Route: 查 skill-catalog.md 选择所需 skills
  -> Load: 读取选中 skills 的 SKILL.md 注入上下文
  -> Execute: 调度子代理执行（检索 + 写作 + 图表等）
  -> Check: 格式检查 (check_paper.py)
  -> Export: DOCX 导出 (export_docx.py)
```

## Workflow

### Step 1: Initialize

```bash
python paper-writer/scripts/init_output_dir.py "<paper-name>" --target-words 1500
```

### Step 2: Analyze & Route

读取 `paper-writer/references/skill-catalog.md`，根据用户需求选择 skills。

常见任务对应的 skills 组合：

| 任务 | 推荐 skills |
|------|------------|
| 写学术论文 | scientific-writing, paper-lookup, citation-management |
| 文献综述 | literature-review, paper-lookup, parallel-web |
| 论文审阅改进 | peer-review, scientific-critical-thinking, scholar-evaluation |
| 论文转网页/视频/海报 | paper-2-web |
| 生成论文图表 | scientific-schematics, scientific-visualization, matplotlib |
| 查询学术数据库 | database-lookup, paper-lookup, bgpt-paper-search |
| 研究构思 | hypothesis-generation, scientific-brainstorming, what-if-oracle |
| 格式转换导出 | pdf, docx, pptx, xlsx |
| 统计分析 | statistical-analysis, exploratory-data-analysis |
| 期刊投稿 | venue-templates, scientific-slides, latex-posters |

### Step 3: Load Skills

读取选中的 SKILL.md 文件，注入子代理上下文：

```
paper-writer/skills/<skill-name>/SKILL.md
```

### Step 4: Execute via Sub-Agent

使用 Agent 工具调度子代理，传入：
- 用户需求
- 加载的 skill 上下文
- 输出目录路径

子代理根据 skill 指引完成具体工作（文献检索、写作、图表生成等）。

### Step 5: Check & Export

```bash
# 格式检查
python paper-writer/scripts/check_paper.py \
    --input "<output_dir>/04_final/final_paper.md" \
    --target-words 1500 \
    --output "<output_dir>/06_qa/check_report.json"

# DOCX 导出
python paper-writer/scripts/export_docx.py \
    --input "<output_dir>/04_final/final_paper.md" \
    --output "<output_dir>/05_exports/final_paper.docx"
```

## Skill Catalog

完整索引见 `paper-writer/references/skill-catalog.md`，覆盖 137 个 skills，
分为 22 个类别：数据库、集成、生物信息、化学信息、ML、数据分析、文档处理、
学术交流、研究方法等。

## Dependencies

- Python + `python-docx` for DOCX export
- Python + `requests` / `urllib` for citation search
- Internet access for academic database APIs
