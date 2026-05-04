# paper-writer

学术论文路由器：收集需求、起子代理自动检索并加载 137 个专业 skills、调度执行、格式检查、DOCX 导出。主 agent 不加载任何 skill 内容。

Academic paper router: collects requirements, spawns a sub-agent that self-discovers and
loads from 137 professional skills on demand, executes the workflow, checks format, and
exports DOCX. The main agent never loads any skill content.

## 工作流 / Workflow

```text
收集需求 → 初始化目录 → 起子代理 → 子代理自发现 skills → 执行 → 检查 → 导出
Collect needs → Init dir → Spawn sub-agent → Sub-agent discovers skills → Execute → Check → Export
```

## 架构：Design B 路由器 / Router Architecture

**主 agent（SKILL.md）** 只做三件事：
1. 收集用户需求参数（主题、字数、语种、署名、格式等）
2. 初始化输出目录
3. 起一个子代理，把需求打包传给它

**子代理（router-agent.md）** 全权负责：
1. 读取 `references/skill-catalog.md` 发现 137 个可用 skills
2. 按需选择并加载 skills 的 `SKILL.md`
3. 执行文献检索、写作、图表生成等具体工作
4. 调用 `check_paper.py` 检查格式
5. 调用 `export_docx.py` 导出

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

## 137 个专业 Skills / Professional Skills

子代理从以下 22 个类别中按需加载 skills：

| 类别 | 数量 | 示例 |
|------|------|------|
| Scientific Databases | 6 | database-lookup, depmap, hugging-science |
| Scientific Integrations | 9 | benchling-integration, omero-integration |
| Bioinformatics & Genomics | 20 | scanpy, biopython, pysam |
| Data Management | 3 | lamindb, modal, optimize-for-gpu |
| Cheminformatics & Drug Discovery | 10 | rdkit, deepchem, diffdock |
| Proteomics | 2 | matchms, pyopenms |
| Medical Imaging | 3 | histolab, pathml, pydicom |
| Healthcare AI | 2 | neurokit2, pyhealth |
| Clinical Documentation | 3 | clinical-decision-support, treatment-plans |
| Neuroscience | 1 | neuropixels-analysis |
| Protein Engineering | 3 | esm, adaptyv, glycoengineering |
| Machine Learning & DL | 14 | scikit-learn, pytorch-lightning, transformers |
| Materials Science & Chemistry | 7 | pymatgen, cirq, qiskit |
| Engineering & Simulation | 4 | matlab, fluidsim, simpy, sympy |
| Data Analysis & Visualization | 11 | matplotlib, seaborn, geopandas, polars |
| Document Processing | 5 | pdf, docx, xlsx, pptx, markitdown |
| Scientific Communication | 16 | paper-lookup, scientific-writing, citation-management |
| Research Methodology | 12 | hypothesis-generation, scientific-brainstorming |
| Laboratory Automation | 1 | pylabrobot |
| Multi-omics | 1 | hypogenic |
| Regulatory | 1 | iso-13485-certification |
| Meta & Agent Tools | 2 | autoskill, get-available-resources |

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
│   └── skill-catalog.md            # 137 个 skills 完整索引
├── scripts/
│   ├── init_output_dir.py          # 输出目录初始化
│   ├── check_paper.py              # 格式检查
│   └── export_docx.py              # DOCX 导出
├── templates/
│   └── ieee_single.md              # IEEE 单栏模板
└── outputs/                        # 用户输出（gitignored）
```
