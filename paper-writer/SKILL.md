---
name: paper-writer
description: >
  学术小论文写作：自动检索真实文献、反AI检测写作、IEEE格式导出。
  Use when the user mentions 小论文, 课程论文, IEEE, 论文写作, 学术论文,
  or needs to write a short academic paper with real citations.
---

# Paper Writer Skill

独立的学术小论文写作工具。自动检索真实文献、按 IEEE 单栏格式写作、
反 AI 检测、字数精确控制、导出 DOCX。

## Architecture

```text
User request
  -> Init: create output directory
  -> Plan: search citations + create outline
  -> Write: anti-AI writing + word count control
  -> Check: format validation
  -> Export: IEEE single-column DOCX
```

## Workflow

### Step 1: Initialize

```bash
python paper-writer/scripts/init_output_dir.py "<paper-name>" --target-words 1500
```

### Step 2: Plan (AI)

Read `agents/paper-planner.md`.

- Parse user requirements
- Search real citations via `search_citations.py`
- Create outline with citation plan

### Step 3: Write (AI)

Read `agents/paper-writer.md`.

- Write paper following outline
- Apply anti-AI writing rules
- Control word count (±10%)
- Integrate citations naturally

### Step 4: Check

```bash
python paper-writer/scripts/check_paper.py \
    --input "<output_dir>/04_final/final_paper.md" \
    --target-words 1500 \
    --output "<output_dir>/06_qa/check_report.json"
```

Fix any issues found (word count, missing sections, orphan citations).

### Step 5: Export DOCX

```bash
python paper-writer/scripts/export_docx.py \
    --input "<output_dir>/04_final/final_paper.md" \
    --output "<output_dir>/05_exports/final_paper.docx"
```

## Dependencies

- Python + `python-docx` for DOCX export
- Python + `requests` (stdlib `urllib`) for citation search
- Internet access for Semantic Scholar / arXiv API
