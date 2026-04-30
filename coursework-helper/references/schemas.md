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
  "notes": ""
}
```

Allowed values:
- `assignment_type`: `slides`, `paper`, `script`, `mixed`
- `language`: `zh`, `en`, or empty
- `tone`: `normal-student`, `formal-academic`, `casual-reflection`, `presentation-friendly`
- `slide_size`: `widescreen-16-9` by default; use another value only when the teacher requires it
- `delivery_formats`: any of `md`, `pptx`, `docx`, `pdf`

## `source_manifest.json`

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

## `outline.md`

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

## `evidence_notes.md`

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

- `final_paper.md`
- `final_slides.md`
- `final_script.md`

For slide markdown, use:

```markdown
# Slide 1: Title
- Bullet
- Bullet

Speaker notes:
...
```

## `delivery_manifest.json`

```json
{
  "created_at": "2026-04-30T12:00:00",
  "requested_formats": ["md", "pptx", "docx"],
  "delivered_files": ["final_slides.md", "final_slides.pptx", "final_script.md"],
  "warnings": ["No teacher rubric was provided; used default structure."],
  "review_suggestions": ["Check whether the teacher requires references."],
  "evidence_notes": "evidence_notes.md"
}
```

Rules:
- Include generated files and failed exports.
- List missing requirements, unsupported claims, and user-review items.
- Keep warnings practical and student-facing.
