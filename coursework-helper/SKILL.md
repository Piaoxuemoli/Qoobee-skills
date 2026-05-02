---
name: coursework-helper
description: >
  Create low-friction coursework deliverables for general education, elective, and low-stakes
  college assignments, including PPT slides, short papers, reading reports, reflection essays,
  presentation scripts, discussion posts, and course summaries. Use this skill whenever the
  user mentions 水课, 通识课, 选修课, 小论文, 课程论文, 读书报告, 观后感, 汇报PPT, 课堂展示,
  演讲稿, or asks to turn scattered course materials into a polished student-style deliverable.
---

# Coursework Helper Skill

Produce practical course deliverables from messy prompts, readings, course slides, topic
requirements, and user notes. The goal is to help a busy student quickly get a usable PPT,
short paper, speech script, or reflection while keeping claims grounded in provided material.

## Architecture

```text
User request
  -> Intake: infer task type, deadline pressure, source materials, tone, and format
  -> Setup: index materials, check official file skills, initialize output directory
  -> Plan: choose deliverable path and create a lightweight outline
  -> Draft: produce content, slides/script, or paper
  -> Polish: add citations/evidence notes, fix tone, export requested formats
```

| Path | Use when | Primary output |
|------|----------|----------------|
| `slides` | PPT/class presentation/课堂展示/汇报 | `final_slides.md`, optional `.pptx`, speech script |
| `paper` | 小论文/课程论文/读书报告/观后感/心得体会 | `final_paper.md`, optional `.docx`/`.pdf` |
| `script` | 演讲稿/发言稿/答辩稿/课堂分享 | `final_script.md` |
| `mixed` | User asks for PPT + paper + script, or task is ambiguous | combined deliverables |

## Startup Layer

### 1. Low-Friction Intake

Infer as much as possible from the user's words and files. Ask only when the missing answer
would change the deliverable.

Collect or infer:

- `assignment_type`: slides, paper, script, or mixed
- `topic`: topic/title/theme
- `course`: course name if available
- `audience`: teacher/classmates/general reader
- `length`: pages, words, slides, minutes, or default
- `tone`: normal student, formal academic, casual reflection, presentation-friendly
- `source_files`: readings, PPT, PDF, Word, notes, links, screenshots
- `delivery_formats`: `md`, plus `pptx`, `docx`, or `pdf` if requested
- `run_mode`: `auto` by default for low-stakes coursework unless the user asks to review steps

Default assumptions:

| Missing item | Default |
|--------------|---------|
| Language | Chinese if the prompt is Chinese; English if the prompt is English |
| Paper length | 1200-1800 Chinese characters or 800-1200 English words |
| Slide count | 8-12 slides |
| PPT page size | 16:9 widescreen (13.333 x 7.5 in / 33.867 x 19.05 cm) |
| Presentation length | 3-5 minutes |
| Tone | believable student voice, not over-polished corporate prose |
| Citations | simple source notes when materials are provided; no fake references |

### 2. Initialize Workspace

Create an output directory:

```bash
python coursework-helper/scripts/init_output_dir.py <assignment-name> \
  --assignment-type <slides|paper|script|mixed> \
  --delivery-formats "md|pptx|docx|pdf" \
  --slide-size "widescreen-16-9" \
  --source-files "<path1>|<path2>"
```

The script creates:

```text
coursework-helper/outputs/<assignment-name>/
├── 00_admin/
│   ├── assignment_context.json
│   └── delivery_manifest.json
├── 01_sources/
│   └── source_manifest.json
├── 02_outline/
│   ├── outline.md
│   └── evidence_notes.md
├── 03_drafts/
│   ├── draft_paper.md
│   ├── draft_slides.md
│   └── draft_script.md
├── 04_final/
│   ├── final_paper.md
│   ├── final_slides.md
│   └── final_script.md
├── 05_exports/
│   ├── final_paper.docx
│   ├── final_slides.pptx
│   └── final_report.pdf
├── 06_qa/
│   └── qa_report.md
└── assets/
```

`assignment_context.json` includes an `output_paths` map. Agents should write to those paths
instead of inventing new locations. Keep root-level output files empty or absent; real
deliverables belong in the managed folders above.

If a directory or multiple files are provided, index them:

```bash
python coursework-helper/scripts/index_source_files.py \
  --inputs "<path1>|<path2>" \
  --output "<output_dir>/01_sources/source_manifest.json"
```

### 3. Check Official File Skills

Before reading source materials, ensure official Anthropic document skills are available:

| File type | Skill |
|-----------|-------|
| `.pdf` | `pdf` |
| `.doc`, `.docx` | `docx` |
| `.ppt`, `.pptx` | `pptx` |
| `.xls`, `.xlsx`, `.csv`, `.tsv` | `xlsx` |

If the repository's `lab-report/scripts/check_official_skills.py` is available, use it:

```bash
python lab-report/scripts/check_official_skills.py --install --source-files "<path1>|<path2>"
```

If not available, check installed skills manually and continue with fallback readers only when
the file can still be read reliably.

## Workflow

### Step 1: Analyze Assignment

Read `agents/assignment-planner.md`. It creates:

- `02_outline/outline.md`
- updated `assignment_context.json`
- initial `02_outline/evidence_notes.md`

It should classify the task, identify teacher requirements, choose structure, and decide what
claims need evidence.

### Step 2: Draft Deliverables

Use the matching agent:

- `agents/paper-writer.md` for `paper` or written sections
- `agents/slide-writer.md` for `slides`
- `agents/script-writer.md` for presentation scripts and speaking notes

For `mixed`, run the agents in the order that helps the student most:

1. Paper or content outline
2. Slides
3. Script/speaker notes

For PPT tasks, `final_slides.md` must be organized as structured slide cards with deck
sections, slide roles, layouts, key messages, visible content, speaker notes, and design notes.
The visible PPT should not become a flat sequence of same-looking bullet pages.

### Step 3: Polish and Package

Read `agents/delivery-packager.md`.

It should:

- make the output sound like a plausible student submission
- remove generic AI phrasing and empty slogans
- preserve required structure and word/slide counts
- enforce the preset PPT page size before PPTX delivery
- run slide organization checks before PPTX delivery when `final_slides.md` exists
- export requested DOCX/PDF/PPTX using official skills when available
- write `00_admin/delivery_manifest.json`

## Quality Bar

Good coursework output should be:

- fast to submit after light review
- aligned with the teacher's visible requirements
- concrete enough to avoid hollow filler
- not suspiciously overproduced for a low-stakes class
- clear about which claims came from materials and which are general framing
- easy to navigate in the output directory, with final files separated from drafts, exports,
  source indexes, and QA reports

## Safety and Honesty

- Do not fabricate real citations, page numbers, survey data, interviews, experiments, or
  teacher requirements.
- If the user asks for fake sources, create a citation-needed placeholder or use general
  source notes instead.
- Do not impersonate a specific real person beyond the user's own student voice.
- Avoid exam cheating, live quiz answers, or bypassing proctoring.
- For ordinary coursework, prioritize useful drafts and disclose gaps in `delivery_manifest.json`.

## Video and Media Links

- **Default to Chinese platforms**: Bilibili > Youku > Tencent Video.
- Only use YouTube if the user explicitly specifies it or the content is exclusively there.
- When a specific video URL is not known, provide a search link on the chosen platform.
- Include a fallback note in speaker notes: "如无法播放可提前下载到本地".

## Dependencies

- **PPT Engine** (`coursework-helper/engine/`): Local python-pptx engine for PPTX generation.
  15 templates, theme system, slide card parser. Primary PPTX export path.
- **Slidev Export** (`coursework-helper/engine/slidev_export.py`): Optional Slidev project
  generator. Converts slide specs to Slidev-compatible Markdown with animations, progressive
  disclosure, and browser preview. Requires Node.js + npm for `slidev export`.
- Official `pptx`, `docx`, `pdf`, and `xlsx` skills for reading files and fallback export.
- Python + `python-pptx` package for PPTX generation.
- `lab-report/scripts/check_official_skills.py` can be reused for official skill checks.
