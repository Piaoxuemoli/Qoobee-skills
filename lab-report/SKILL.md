---
name: lab-report
description: >
  Write experiment and lab reports from source materials (lab manuals, PPT, Word, PDF).
  Use this skill whenever the user needs to write a lab report, experiment report,
  course report, 实验报告, 课程报告, or any structured academic/technical writeup based
  on experiment procedures. Proactively suggest this skill when the user mentions
  "lab report," "experiment report," "实验报告," or describes running an experiment
  that needs documenting.
---

# Lab Report Skill

Automate experiment and course reports from source materials. The orchestrator owns the
conversation, local profile setup, report-path selection, and phase transitions. Sub-agents
do the specialized work: summarize materials, execute experiments, and write reports.

## Architecture

The skill is organized as a startup layer followed by one of three report paths.

```text
User request
  -> Startup: intake wizard, load profile, choose mode, index materials, create output directory
  -> Classify path:
       standard-executable | data-provided | paper-only
  -> Run the selected path
  -> Deliver final_report.md plus optional DOCX/PDF and evidence map
```

| Report path | Use when | Runner needed |
|-------------|----------|---------------|
| `standard-executable` | Materials contain concrete commands or executable steps | Yes |
| `data-provided` | User already has result data, tables, screenshots, logs, or observations | No |
| `paper-only` | The task is theoretical, reflective, or writeup-only | No |

## Startup Layer

### 1. Run Student-Friendly Intake

Start with the user's natural request, file attachments, or material directory. Prefer
inference over forms. Only ask short questions when the answer changes the workflow.

Infer or ask for:

| Decision | Default |
|----------|---------|
| Has source materials? | use attached files or paths from the request |
| Experiment already completed? | infer from result files/logs/screenshots; otherwise no |
| Should commands be executed? | yes for concrete executable manuals; no for provided-data or paper-only |
| Report language | Chinese when the request is Chinese, English when the request is English |
| Delivery formats | `md`, plus `docx`/`pdf` if requested by the user or course template |

Useful startup prompt when needed:

```text
我可以直接整理材料并生成报告。请确认：1) 是否需要我运行实验命令；2) 最终是否要 Word/PDF；3) 是否要记住这门课的模板？
```

### 2. Load Local Profile

Run:

```bash
python lab-report/scripts/profile_config.py status
```

The profile is stored outside the repository:

```text
~/.qoobee-skills/lab-report/profile.json
```

If required fields are missing, ask for only those fields once, then save them:

```bash
python lab-report/scripts/profile_config.py write \
  --student-name "..." \
  --student-id "..." \
  --class "..." \
  --course "..." \
  --instructor "..." \
  --institution "..."
```

Do not ask for cached profile fields again unless the user asks to update them or the
current report explicitly conflicts with them.

### 3. Choose Confirmation Mode

Ask once at startup:

```text
是否进入无需确认的自动模式？进入后我会自动推进模板、普通实验步骤和最终报告生成；只有缺少关键信息、命令失败或危险操作时才打断。
```

Set `run_mode`:

- `manual`: review routine phase outputs before proceeding.
- `auto`: skip routine phase/template/ordinary-step confirmations.

Auto mode still stops for:

- missing or unreadable source materials
- ambiguous steps that cannot be executed or written about safely
- destructive or high-risk commands
- unresolved placeholders or missing key data in the final report

In auto mode, ordinary command failures are recorded, skipped when possible, and summarized in
final delivery instead of repeatedly interrupting the user. Manual mode pauses and asks whether
to retry, modify, skip, or use user-provided results.

Set `failure_policy`:

- `auto-skip`: default for auto mode.
- `manual-pause`: default for manual mode.

### 4. Gather Inputs and Classify Report Path

Collect or infer:

- `source_files`: lab manual, PPT, Word, PDF, images, logs, data files, or notes
- `source_manifest_path`: generated when inputs include directories or multiple materials
- `context`: user's natural-language task description
- `report_type`: `standard-executable`, `data-provided`, or `paper-only`
- `experiment_name`: slug for the output folder
- `delivery_formats`: `md`, optionally `docx`, `pdf`
- `course_template_id`: matched reusable course template if any

Prefer inference over extra questions. Ask only when classification is ambiguous or required
inputs are missing.

If the user provides a directory or several files, plan to create:

```text
lab-report/outputs/<experiment-name>/source_manifest.json
```

Create the file after the output directory is initialized. Use the manifest to separate
manuals, slides, data, images, logs, code, and other files.

### 5. Check Official File Skills

Before parsing source files, check whether the user has the official Anthropic document
skills required for those file types:

```bash
python lab-report/scripts/check_official_skills.py --source-files "<path1>|<path2>"
```

If any required skill is missing, install it automatically through OpenSkill:

```bash
python lab-report/scripts/check_official_skills.py --install --source-files "<path1>|<path2>"
```

The check covers:

| File type | Required official skill |
|-----------|-------------------------|
| `.pdf` | `pdf` |
| `.doc`, `.docx` | `docx` |
| `.ppt`, `.pptx` | `pptx` |
| `.xls`, `.xlsx`, `.xlsm`, `.csv`, `.tsv` | `xlsx` |

If OpenSkill cannot run because `npx`/Node.js is unavailable, stop and tell the user that
official file skills could not be installed automatically. Do not pretend to support an
unsupported file type; ask the user to install Node.js or provide the material in a readable
format.

This controlled startup dependency repair is allowed because it is limited to official
Anthropic document skills needed to read user-provided files. Do not use it to install
unrelated skills or project dependencies.

### 6. Match Course Template

If the profile or materials identify a course, check reusable course templates:

```bash
python lab-report/scripts/course_templates.py get --course "<course-name>"
```

If the user says to remember a template for this course, save it:

```bash
python lab-report/scripts/course_templates.py save \
  --course "<course-name>" \
  --template-path "<template.md>"
```

Use the matched `course_template_id` in `report_context.json`. Do not store experiment
results in course templates.

### 7. Initialize Output Directory

Run:

```bash
python lab-report/scripts/init_output_dir.py <experiment-name> \
  --report-type <report_type> \
  --run-mode <run_mode> \
  --source-files "<path1>|<path2>" \
  --source-manifest-path "<manifest-path>" \
  --delivery-formats "md|docx|pdf" \
  --course-template-id "<template-id>" \
  --failure-policy <failure_policy>
```

Store:

```text
output_dir = lab-report/outputs/<experiment-name>
```

The initializer creates `experiment_info.json`, `report_context.json`, `screenshots/`, and
`raw_outputs/`. Material indexing may also create `source_manifest.json`. See
`references/schemas.md` for required fields.

After initialization, create the material manifest when needed:

```bash
python lab-report/scripts/index_source_files.py \
  --inputs "<path1>|<path2>" \
  --output "<output_dir>/source_manifest.json"
```

## Path A: standard-executable

Use this path when the experiment has commands or steps that can be run.

1. **Summarize materials**
   - Read `agents/experiment-summarizer.md`.
   - Inputs: `source_files`, `source_manifest.json`, `output_dir`, `context`,
     `report_context_path`, `profile_status`, `run_mode`, `report_type`.
   - Outputs: `procedure_summary.md`, `evidence_map.md`, updated `experiment_info.json`.
   - Manual mode: review the summary. Auto mode: proceed if steps are concrete.

2. **Generate report draft**
   - Read `agents/report-writer.md`.
   - Template mode inputs: `procedure_summary.md`, `experiment_info.json`,
     `report_context.json`, `output_dir`, `run_mode`, language.
   - Output: `report_draft.md`.

3. **Execute experiment**
   - Read `agents/experiment-runner.md`.
   - Inputs: `procedure_summary.md`, `report_context.json`, `output_dir`,
     `screenshot_preference`, `run_mode`, `failure_policy`.
   - Outputs: `run_log.md`, updated `evidence_map.md`, `raw_outputs/`, `screenshots/`.
   - Auto mode behaves like `run all` for ordinary commands and skips failed independent
     steps when possible.

4. **Complete final report**
   - Read `agents/report-writer.md` again.
   - Fill-in mode inputs: draft, run log, raw outputs, screenshots, context, evidence map.
   - Output: `final_report.md`, optional DOCX/PDF, `delivery_manifest.json`.

## Path B: data-provided

Use this path when the user already has data, screenshots, tables, logs, or observations.

1. Summarize source materials and imported data with `experiment-summarizer`.
2. Generate `report_draft.md` with placeholders only where data is genuinely missing.
3. Skip `experiment-runner`.
4. Run `report-writer` fill-in mode using:
   - user-provided data files
   - copied screenshots, if any
   - notes recorded in `report_context.json`

If required result data is missing, stop and ask even in auto mode.

## Path C: paper-only

Use this path for theoretical reports, course reports, reflections, or non-executable
writeups.

1. Use `experiment-summarizer` to turn materials and prompt context into a structured outline.
2. Use `report-writer` template mode to create a draft without execution placeholders.
3. Skip `experiment-runner`.
4. Use `report-writer` fill-in mode to produce `final_report.md` from the outline and
   source materials.

Do not invent experiment results. If the task needs claims that are not supported by the
materials, ask the user or mark them as not provided.

## Safety and Failure Policy

### Ordinary confirmations

Manual mode asks before phase transitions and ordinary command execution. Auto mode does not.

### Blocking failures

Stop and ask the user when:

- a source file cannot be read and no fallback content exists
- a required dataset/result/table is absent
- final report generation would leave unresolved placeholders
- manual mode command execution fails and the next action needs user choice

### Non-blocking failures

Record and continue when:

- optional screenshots cannot be rendered
- a nonessential setup command fails but later required data already exists
- optional metadata is missing and the report can still be correct without it
- auto mode command execution fails but later independent steps and the report can still be
  completed honestly

### Destructive or high-risk commands

Always require explicit confirmation, even in auto mode:

- deletion or formatting: `rm`, `rmdir`, `del`, `format`, `dd`, `mkfs`
- privilege escalation: `sudo`, `su`, root shell
- permission ownership changes: `chmod 777`, `chown`
- system state changes: `shutdown`, `reboot`, `poweroff`
- destructive database operations: `DROP`, `DELETE`, `TRUNCATE`
- global package installation or environment mutation, except the controlled official
  document-skill repair in Startup Step 5

Never run destructive commands outside the project directory without explicit permission.

## Output Structure

All generated content goes under `lab-report/outputs/<experiment-name>/`. This directory is
gitignored and must stay separate from skill source files.

```text
outputs/<experiment-name>/
├── report_context.json
├── source_manifest.json
├── experiment_info.json
├── procedure_summary.md
├── evidence_map.md
├── report_draft.md
├── run_log.md
├── final_report.md
├── delivery_manifest.json
├── screenshots/
└── raw_outputs/
```

Never write generated content to `agents/`, `references/`, `scripts/`, or the skill root.

## Dependencies

- **terminal-screenshot skill**: required for screenshot capture in `standard-executable`.
- **Python**: required for `scripts/init_output_dir.py` and `scripts/profile_config.py`.
- **Official document skills**: `pdf`, `docx`, `pptx`, `xlsx` for reading and final exports.
- **File reading tools**: `pdftotext`, `python-docx`, `python-pptx`, `pandoc` when available;
  fall back gracefully if missing.
