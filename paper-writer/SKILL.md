---
name: paper-writer
description: >
  学术论文路由器：收集需求、起子代理自动检索并加载 233 个专业 skills、
  调度执行、格式检查、DOCX 导出。主 agent 不加载任何 skill 内容。
  Use when the user mentions 小论文, 课程论文, IEEE, 论文写作, 学术论文,
  文献综述, literature review, paper writing, scientific paper, 研究报告.
---

# Paper Writer Router

薄路由器：只收集用户需求，起子代理完成全部工作。主 agent 不读任何 skill 内容。

## 工作流程

### Step 1: 收集需求

从用户输入中提取以下参数（缺失的用默认值）：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| topic | （必填） | 论文主题 |
| paper_name | （自动生成） | 输出目录名，英文短横线格式 |
| paper_type | 课程论文 | 课程论文 / 小论文 / 研究报告 / 文献综述 |
| lang | English | 论文写作语言：English / 中文 / 双语 |
| author | 不写 | 署名信息（姓名、学号、院系），空则不写 |
| target_words | 1500 | 正文字数目标（不含参考文献） |
| format | IEEE 单栏 | 排版格式：IEEE 单栏 / APA / MLA / 自定义 |
| citation_style | IEEE | 引用风格：IEEE 数字 [1] / APA / MLA / Chicago |
| min_refs | 不限 | 最少参考文献数 |
| deadline | 不限 | 截止时间（可选） |
| plagiarism_check | 常规 | 查重要求：常规 / AIGC / 两者 |
| extra | （无） | 其他特殊要求 |

如果用户输入中缺少关键参数（topic），先问清楚再继续。

### Step 2: 初始化目录

```bash
python paper-writer/scripts/init_output_dir.py "<paper_name>" \
    --target-words <target_words> \
    --lang <lang> \
    --author "<author>"
```

### Step 3: 起子代理

使用 Agent 工具创建子代理，**只传入以下信息**，不传 skill 内容：

```
你是论文写作子代理。请按以下要求完成任务：

## 需求
- 主题: <topic>
- 论文类型: <paper_type>
- 语种: <lang>
- 署名: <author>
- 目标字数: <target_words>
- 格式: <format>
- 引用风格: <citation_style>
- 最少文献数: <min_refs>
- 查重要求: <plagiarism_check>
- 其他: <extra>

## 输出目录
<paper_name> 输出到 paper-writer/outputs/<paper_name>/

## 你需要做的
1. 读 paper-writer/references/skill-catalog.md 了解可用 skills
2. 根据需求选择合适的 skills
3. 读取选中 skills 的 SKILL.md（路径在 catalog 中）
4. 按照 skill 指引执行（文献检索、写作、图表生成等）
5. 完成后调用检查和导出脚本

## 检查与导出
```bash
python paper-writer/scripts/check_paper.py \
    --input "paper-writer/outputs/<paper_name>/04_final/final_paper.md" \
    --target-words <target_words> \
    --lang <lang> \
    --output "paper-writer/outputs/<paper_name>/06_qa/check_report.json"

python paper-writer/scripts/export_docx.py \
    --input "paper-writer/outputs/<paper_name>/04_final/final_paper.md" \
    --output "paper-writer/outputs/<paper_name>/05_exports/final_paper.docx"
```
```

### Step 4: 报告结果

子代理完成后，向用户报告：
- 输出文件位置
- 字数 / 文献数等统计数据
- 检查结果（是否有 warning）
- 如果有 deadline，提醒用户

## 重要原则

- **主 agent 不读 skill-catalog.md**
- **主 agent 不读任何 skills/<name>/SKILL.md**
- **主 agent 只负责收集需求 + 起子代理 + 报告结果**
- **子代理全权负责 skill 发现、加载、执行、检查、导出**
