---
name: study-index
description: >
  整理课程材料为带目录索引的速查手册。适用于开卷考试复习资料、课程笔记整理、
  知识收藏整理。输入多个 PPT/PDF/文档，输出结构化 Markdown + PDF。
  Use when the user mentions 开卷考试, 复习资料, 考试速查, 知识整理, 整理笔记,
  资料汇总, 速查手册, or asks to organize scattered course materials into an
  indexed handbook for studying or open-book exams.
  Proactively suggest this skill when the user has multiple course files (PPTs,
  PDFs, documents) and needs to consolidate them for review or exam preparation.
---

# Study Index Skill

将散乱的课程材料（PPT、PDF、文档、笔记）整理成一本带目录、带索引、带例题、带关键图片的速查手册。核心原则：**不丢失信息**，源材料中的关键图片、公式、图表必须提取并放到手册对应位置。

## Architecture

```text
User provides course materials
  -> Extract: pull text + images from each source file
  -> Organize: group by topic/chapter, identify key images
  -> Write: structured handbook with TOC, knowledge points, examples, images
  -> Export: Markdown + PDF (printable)
```

## Startup Layer

### 1. Intake

Infer from user input:

- `course_name`: course or topic name
- `source_files`: list of PPT/PDF/DOCX/MD/TXT files or directories
- `delivery_formats`: `md` + `pdf` (default), or user-specified
- `purpose`: exam prep (default), review, reference
- `language`: Chinese if prompt is Chinese, English if English

Default assumptions:

| Missing item | Default |
|--------------|---------|
| Language | Chinese if prompt is Chinese |
| Output formats | Markdown + PDF |
| Organization | By chapter/topic (auto-detected from source structure) |
| Images | Extract all, keep key images in final handbook |

### 2. Initialize Workspace

```bash
python study-index/scripts/init_output_dir.py <course-name> \
  --source-files "<path1>|<path2>" \
  --delivery-formats "md|pdf"
```

Creates:

```text
study-index/outputs/<course-name>/
├── 00_admin/
│   ├── study_context.json
│   └── extract_manifest.json
├── 01_extracted/          # text + images by source
│   ├── <source-1>/
│   │   ├── slide_01.txt
│   │   ├── slide_01_img_01.png
│   │   └── ...
│   └── <source-2>/
│       ├── page_01.txt
│       └── ...
├── 02_outline/
│   └── outline.md
├── 03_drafts/
│   └── draft_handbook.md
├── 04_final/
│   └── final_handbook.md
├── 05_exports/
│   └── final_handbook.pdf
├── 06_qa/
│   └── qa_report.md
└── assets/
```

### 3. Check Official Skills

Ensure document reading skills are available:

| File type | Skill |
|-----------|-------|
| `.pdf` | `pdf` |
| `.doc`, `.docx` | `docx` |
| `.ppt`, `.pptx` | `pptx` |
| `.xls`, `.xlsx` | `xlsx` |

If `lab-report/scripts/check_official_skills.py` is available:

```bash
python lab-report/scripts/check_official_skills.py --install --source-files "<path1>|<path2>"
```

## Workflow

### Step 1: Extract Content

Read `agents/material-extractor.md`.

Run the extraction script:

```bash
python study-index/scripts/extract_content.py \
  --inputs "<source1>|<source2>|..." \
  --output "<output_dir>/01_extracted/" \
  --manifest "<output_dir>/00_admin/extract_manifest.json"
```

This extracts text and images from all source files into per-source directories.

### Step 2: Organize Knowledge

Read `agents/knowledge-organizer.md`.

- Read all extracted text from `01_extracted/`
- Browse extracted images to identify key ones (formulas, diagrams, charts, important screenshots)
- Group content by chapter/topic
- Write `02_outline/outline.md` with structured knowledge map

### Step 3: Write Handbook

Read `agents/handbook-writer.md`.

- Write `03_drafts/draft_handbook.md` first
- Polish into `04_final/final_handbook.md`
- Images referenced with relative paths: `![desc](../01_extracted/source/slide_01_img_01.png)`
- Run QA checks on image references and content completeness

### Step 4: Export

Convert Markdown to PDF:

```bash
# Try pandoc first
pandoc 04_final/final_handbook.md -o 05_exports/final_handbook.pdf \
  --resource-path="<output_dir>/04_final:<output_dir>/01_extracted"

# Fallback: Python weasyprint
python -c "
from study_index_export import md_to_pdf
md_to_pdf('<output_dir>/04_final/final_handbook.md',
          '<output_dir>/05_exports/final_handbook.pdf',
          resource_dirs=['<output_dir>/01_extracted'])
"
```

## Quality Bar

A good study handbook should:

- Cover all topics from source materials without gaps
- Include every key image, formula, and diagram from the sources
- Have a clear table of contents for quick navigation
- Attach relevant example problems to each knowledge point
- Be printable as a single PDF with images inline
- Use consistent formatting throughout
- Have a keyword index for quick lookup during exams

## Safety and Honesty

- Do not fabricate content not present in source materials.
- If a source file cannot be read, record the failure in `extract_manifest.json` and continue.
- If an image cannot be extracted, note it in the output with a `[图片提取失败]` placeholder.
- Do not claim PDF was generated if export failed.

## Dependencies

- Python + `python-pptx` for PPTX text/image extraction
- Python + `PyMuPDF` (`fitz`) for PDF text/image extraction
- Python + `python-docx` for DOCX text/image extraction
- `pandoc` (optional) for Markdown → PDF conversion
- Official `pdf`, `docx`, `pptx` skills for reading files
