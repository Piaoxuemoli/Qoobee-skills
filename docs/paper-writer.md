# paper-writer

学术论文路由器：收集需求、起子代理自动检索并加载 233 个专业 skills、调度执行、格式检查、DOCX 导出。主 agent 不加载任何 skill 内容。

Academic paper router: collects requirements, spawns a sub-agent that self-discovers and
loads from 233 professional skills on demand, executes the workflow, checks format, and
exports DOCX. The main agent never loads any skill content.

## 工作流 / Workflow

```text
收集需求 → 初始化目录 → 起子代理 → 三层检索 skills → 执行 → 检查 → 导出
Collect needs → Init dir → Spawn sub-agent → Tiered skill retrieval → Execute → Check → Export
```

## 架构：Design B 路由器 / Router Architecture

**主 agent（SKILL.md）** 只做三件事：
1. 收集用户需求参数（主题、字数、语种、署名、格式等）
2. 初始化输出目录
3. 起一个子代理，把需求打包传给它

**子代理（router-agent.md）** 全权负责分层检索：
1. **核心层（10 个）** — 无条件加载：scientific-writing, citation-management, paper-lookup 等
2. **领域层（164 个）** — 按主题关键词匹配：ML/AI、Biology、Chemistry、Physics 等 9 个领域
3. **工具层（59 个）** — 按需选取：可视化、数据统计、文档处理、研究自动化等 5 个类别
4. 执行文献检索、写作、图表生成等具体工作
5. 调用 `check_paper.py` 检查格式
6. 调用 `export_docx.py` 导出

这种设计保证主 agent 上下文不被 skill 内容污染。

## 需求参数 / Parameters

| 参数 | 默认值 | 说明 |
|------|--------|------|
| topic | （必填） | 论文主题 |
| paper_type | 课程论文 | 课程论文 / 小论文 / 研究报告 / 文献综述 |
| lang | English | 论文写作语言：English / 中文 / 双语 |
| author | 不写 | 署名信息（姓名、学号、院系），空则不写 |
| target_words | 1500 | 正文字数目标（不含参考文献） |
| format | IEEE 单栏 | 排版格式：IEEE 单栏 / APA / MLA / 自定义 |
| citation_style | IEEE | 引用风格：IEEE 数字 [1] / APA / MLA / Chicago |
| min_refs | 不限 | 最少参考文献数 |
| deadline | 不限 | 截止时间（可选） |
| plagiarism_check | 常规 | 查重要求：常规 / AIGC / 两者 |

## 使用方式 / Usage

```text
帮我写一篇关于分布式计算的1500字小论文，IEEE格式
```

```text
Write a 2000-word paper on reinforcement learning in robotics, APA style, with author "张三 2021001 计算机系"
```

```text
帮我写一篇文献综述，主题是大语言模型在医疗领域的应用，中文，至少20篇参考文献
```

## 233 个专业 Skills / Professional Skills — 三层检索

### Tier 1: 核心 skills（10 个，必加载）
scientific-writing, citation-management, literature-review, paper-lookup, peer-review, compiler, venue-templates, database-lookup, research-lookup, scientific-brainstorming

### Tier 2: 领域 skills（164 个，按主题匹配）

| 领域 | 数量 | 关键词 |
|------|------|--------|
| ML/AI | 87 | machine learning, deep learning, transformer, LLM, training, PyTorch |
| Biology | 35 | biology, genomics, RNA, DNA, gene, protein, single-cell, CRISPR |
| Chemistry | 14 | chemistry, drug discovery, molecule, SMILES, docking |
| Physics | 7 | physics, quantum, simulation, fluid dynamics, astrophysics |
| Medicine | 10 | medical, clinical, pathology, radiology, DICOM |
| Earth Science | 2 | geospatial, GIS, remote sensing, climate |
| Neuroscience | 2 | neuroscience, brain, EEG, ECG, electrophysiology |
| Finance | 2 | finance, economics, market, fiscal, investment |
| Writing | 8 | grant, NSF, NIH, hypothesis, scholarly evaluation |

### Tier 3: 工具 skills（59 个，按需选取）

| 类别 | 触发条件 | 数量 |
|------|---------|------|
| 可视化 | 需要图表、示意图、海报 | 12 |
| 数据统计 | 需要数据分析、统计建模 | 14 |
| 文档处理 | 需要读写 PDF/DOCX/PPTX/XLSX | 7 |
| 研究自动化 | 需要自主研究、假设生成 | 10 |
| 基础设施 | 需要资源检测、文献管理 | 4 |

完整索引见 [skill-catalog.md](../paper-writer/references/skill-catalog.md)。

## 检查与导出 / Check & Export

```bash
# 格式检查（字数、章节、引用、AI 填充词）
python paper-writer/scripts/check_paper.py \
    --input "<output_dir>/04_final/final_paper.md" \
    --target-words 1500 \
    --lang English \
    --output "<output_dir>/06_qa/check_report.json"

# DOCX 导出
python paper-writer/scripts/export_docx.py \
    --input "<output_dir>/04_final/final_paper.md" \
    --output "<output_dir>/05_exports/final_paper.docx"
```

检查项：
- 字数在目标 ±10% 范围内
- 必需章节存在（按语种：中文/英文/双语）
- 正文引用 [N] 与参考文献条目匹配
- 无空章节
- 检测常见 AI 填充词

## 文件结构 / File Structure

```
paper-writer/
├── SKILL.md                        # 主路由器（收集需求 + 起子代理）
├── README.md                       # 本文件 / This file
├── agents/
│   └── router-agent.md             # 子代理指令（自发现 + 执行）
├── references/
│   └── skill-catalog.md            # 233 个 skills 三层分类索引
├── scripts/
│   ├── init_output_dir.py          # 输出目录初始化
│   ├── check_paper.py              # 格式检查
│   └── export_docx.py              # DOCX 导出
├── templates/
│   └── ieee_single.md              # IEEE 单栏模板
└── outputs/                        # 用户输出（gitignored）
```
