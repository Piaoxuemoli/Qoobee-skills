# Coursework Helper Schemas

Shared data contracts for `coursework-helper`.

## `assignment_context.json`

Created by `scripts/init_output_dir.py`.

```json
{
  "assignment_name": "marxism-reading-report",
  "assignment_type": "paper",
  "created_at": "2026-04-30T12:00:00",
  "source_files": ["C:/course/materials/book.pdf"],
  "source_manifest_path": "",
  "language": "zh",
  "course": "思想道德与法治",
  "topic": "青年责任与社会实践",
  "audience": "course instructor",
  "tone": "normal-student",
  "length_hint": "1500 Chinese characters",
  "slide_size": "widescreen-16-9",
  "delivery_formats": ["md", "docx"],
  "output_paths": {
    "assignment_context": "outputs/name/00_admin/assignment_context.json",
    "source_manifest": "outputs/name/01_sources/source_manifest.json",
    "outline": "outputs/name/02_outline/outline.md",
    "evidence_notes": "outputs/name/02_outline/evidence_notes.md",
    "draft_paper": "outputs/name/03_drafts/draft_paper.md",
    "draft_slides": "outputs/name/03_drafts/draft_slides.md",
    "draft_script": "outputs/name/03_drafts/draft_script.md",
    "final_paper": "outputs/name/04_final/final_paper.md",
    "final_slides": "outputs/name/04_final/final_slides.md",
    "final_script": "outputs/name/04_final/final_script.md",
    "delivery_manifest": "outputs/name/00_admin/delivery_manifest.json",
    "qa_report": "outputs/name/06_qa/qa_report.md",
    "exports_dir": "outputs/name/05_exports",
    "assets_dir": "outputs/name/assets"
  },
  "notes": ""
}
```

Allowed values:
- `assignment_type`: `slides`, `paper`, `script`, `mixed`
- `language`: `zh`, `en`, or empty
- `tone`: `normal-student`, `formal-academic`, `casual-reflection`, `presentation-friendly`
- `slide_size`: `widescreen-16-9` by default; use another value only when the teacher requires it
- `delivery_formats`: any of `md`, `pptx`, `docx`, `pdf`
- `output_paths`: canonical destinations for all generated files

## Output Directory Layout

Generated coursework files must be organized by lifecycle stage:

```text
outputs/<assignment-name>/
├── 00_admin/      # context and manifest files
├── 01_sources/    # source index and extracted source notes
├── 02_outline/    # outline and evidence notes
├── 03_drafts/     # intermediate drafts
├── 04_final/      # final Markdown deliverables
├── 05_exports/    # PPTX, DOCX, PDF exports
├── 06_qa/         # QA reports and checks
└── assets/        # images or temporary visual assets
```

Rules:
- Agents must prefer paths from `assignment_context.json.output_paths`.
- Final Markdown belongs in `04_final/`.
- Binary exports belong in `05_exports/`.
- QA and validation reports belong in `06_qa/`.
- Do not place generated deliverables in the output root.

## `01_sources/source_manifest.json`

Produced by `scripts/index_source_files.py`.

```json
{
  "created_at": "2026-04-30T12:00:00",
  "input_paths": ["C:/course/task"],
  "files": [
    {
      "path": "C:/course/task/requirements.docx",
      "name": "requirements.docx",
      "extension": ".docx",
      "category": "requirement",
      "size_bytes": 12345
    }
  ],
  "counts": {
    "requirement": 1,
    "reading": 1,
    "slides": 1,
    "data": 0,
    "image": 0,
    "notes": 1,
    "other": 0
  }
}
```

Categories:
- `requirement`: assignment prompt, rubric, teacher requirements
- `reading`: article, book chapter, PDF, Word material
- `slides`: course PPT/PPTX
- `data`: spreadsheet, table, CSV, JSON
- `image`: screenshots/photos
- `notes`: markdown/txt notes
- `other`: review only when needed

## `02_outline/outline.md`

```markdown
# <Assignment Title>

## Task Type
paper

## Requirements
- ...

## Proposed Structure
1. ...

## Evidence Plan
| Section | Evidence needed | Source |
|---------|-----------------|--------|

## Style Notes
- ...
```

## `02_outline/evidence_notes.md`

```markdown
# Evidence Notes — <Assignment Title>

| Output section | Claim/content | Source | Confidence | Notes |
|----------------|---------------|--------|------------|-------|
```

Rules:
- Use `high` confidence for content directly supported by provided materials.
- Use `medium` confidence for general course framing.
- Use `low` confidence for placeholders or unsupported claims that need user review.
- Do not invent formal citations or page numbers.

## Final Outputs

Depending on `assignment_type`, agents write:

- `04_final/final_paper.md`
- `04_final/final_slides.md`
- `04_final/final_script.md`

For slide markdown, use:

```markdown
# Slide 1: Title
- Bullet
- Bullet

Speaker notes:
...
```

## `00_admin/delivery_manifest.json`

```json
{
  "created_at": "2026-04-30T12:00:00",
  "requested_formats": ["md", "pptx", "docx"],
  "delivered_files": [
    "04_final/final_slides.md",
    "05_exports/final_slides.pptx",
    "04_final/final_script.md"
  ],
  "warnings": ["No teacher rubric was provided; used default structure."],
  "review_suggestions": ["Check whether the teacher requires references."],
  "evidence_notes": "evidence_notes.md"
}
```

Rules:
- Include generated files and failed exports.
- List missing requirements, unsupported claims, and user-review items.
- Keep warnings practical and student-facing.
