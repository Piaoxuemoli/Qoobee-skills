---
name: study-index
description: >
  整理课程材料为带目录索引的速查手册。适用于开卷考试复习资料、课程笔记整理、
  知识收藏整理。输入多个 PPT/PDF/文档，输出结构化 Markdown（全部内容+索引）。
  Use when the user mentions 开卷考试, 复习资料, 考试速查, 知识整理, 整理笔记,
  资料汇总, 速查手册, or asks to organize scattered course materials into an
  indexed handbook for studying or open-book exams.
  Proactively suggest this skill when the user has multiple course files (PPTs,
  PDFs, documents) and needs to consolidate them for review or exam preparation.
---

# Study Index Skill

将散乱的课程材料（PPT、PDF、文档、笔记）整理成一本**包含全部原文内容**的速查手册。

核心原则：**不丢失信息**——源材料中的所有文字内容必须完整保留（不总结、不删减），
关键图片、公式、图表必须提取并放到手册对应位置。

**关键：使用脚本自动拼接所有文本内容，而不是让 AI 来"写"手册。AI 只负责生成大纲。**

## Architecture

```text
User provides course materials
  -> Extract: pull text + images from each source file (extract_content.py)
  -> Filter: remove decorative images (filter_images.py)
  -> Organize: AI groups sources by chapter, writes outline (knowledge-organizer)
  -> Compile: script concatenates ALL text into handbook (compile_handbook.py)
```

## Startup Layer

### 1. Intake

Infer from user input:

- `course_name`: course or topic name
- `source_files`: list of PPT/PDF/DOCX/MD/TXT files or directories
- `purpose`: exam prep (default), review, reference
- `language`: Chinese if prompt is Chinese, English if English

Default assumptions:

| Missing item | Default |
|--------------|---------|
| Language | Chinese if prompt is Chinese |
| Output format | Markdown |
| Organization | By chapter/topic (auto-detected from source structure) |
| Images | Extract all, keep key images in final handbook |

### 2. Initialize Workspace

```bash
python study-index/scripts/init_output_dir.py <course-name> \
  --source-files "<path1>|<path2>" \
  --delivery-formats "md"
```

Creates:

```text
study-index/outputs/<course-name>/
├── 00_admin/
│   ├── study_context.json
│   └── extract_manifest.json
├── 01_extracted/          # text + images by source (all images)
│   ├── <source-1>/
│   │   ├── slide_01.txt
│   │   ├── slide_01_img_01.png
│   │   └── ...
│   └── <source-2>/
│       ├── page_01.txt
│       └── ...
├── 01_filtered/           # filtered images (decorative removed)
│   └── <source-1>/
│       └── slide_01_img_01.png
├── 02_outline/
│   └── outline.md
├── 04_final/
│   └── final_handbook.md  # complete handbook with ALL content + index
└── 06_qa/
    └── qa_report.md
```

### 3. Check Official Skills

Ensure document reading skills are available:

| File type | Skill |
|-----------|-------|
| `.pdf` | `pdf` |
| `.doc`, `.docx` | `docx` |
| `.ppt`, `.pptx` | `pptx` |
| `.xls`, `.xlsx` | `xlsx` |

## Workflow

### Step 1: Extract Content

Read `agents/material-extractor.md`.

```bash
python study-index/scripts/extract_content.py \
  --inputs "<source1>|<source2>|..." \
  --output "<output_dir>/01_extracted/" \
  --manifest "<output_dir>/00_admin/extract_manifest.json"
```

### Step 2: Filter Images

```bash
python study-index/scripts/filter_images.py \
  --input-dir "<output_dir>/01_extracted/" \
  --output-dir "<output_dir>/01_filtered/" \
  --report "<output_dir>/00_admin/filter_report.json"
```

### Step 3: Organize Knowledge (AI)

Read `agents/knowledge-organizer.md`.

- Read extracted text to understand course structure
- Group source directories by chapter/topic
- Write `02_outline/outline.md` with the mapping:
  ```
  ## Chapter 1: <title>
  - 来源: source_dir_1, source_dir_2
  ```

### Step 4: Compile Handbook (Script)

```bash
python study-index/scripts/compile_handbook.py \
  --outline "<output_dir>/02_outline/outline.md" \
  --extracted "<output_dir>/01_extracted/" \
  --filtered "<output_dir>/01_filtered/" \
  --output "<output_dir>/04_final/final_handbook.md" \
  --course-name "<course name>"
```

This script:
- Reads the outline to get chapter-to-source mapping
- For each chapter, reads ALL text files from the source directories
- Inserts corresponding images at the right positions
- Adds table of contents and keyword index
- **Preserves every character** from the source files — no summarization

## Quality Bar

A good study handbook should:

- **Contain ALL text content** from source materials — not a summary, but a compilation
- Every source file's full text appears in the handbook
- Include key images, formulas, and diagrams from the sources
- Have a clear table of contents for quick navigation
- Have a keyword index for quick lookup during exams
- **Test**: A student reading only the handbook should have ≥ the information in the originals

## Safety and Honesty

- Do not fabricate content not present in source materials.
- If a source file cannot be read, record the failure in `extract_manifest.json` and continue.
- If an image cannot be extracted, note it in the output with a `[图片提取失败]` placeholder.

## Dependencies

- Python + `python-pptx` for PPTX text/image extraction
- Python + `PyMuPDF` (`fitz`) for PDF text/image extraction
- Python + `python-docx` for DOCX text/image extraction
- Python + `Pillow` for image filtering
- Official `pdf`, `docx`, `pptx` skills for reading files
