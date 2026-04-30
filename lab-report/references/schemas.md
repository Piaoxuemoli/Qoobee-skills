# Lab Report Schemas

Shared data contracts for `lab-report`. The orchestrator, scripts, and agents should use
these structures consistently.

## `profile.json`

Stored outside the repository:

```text
~/.qoobee-skills/lab-report/profile.json
```

```json
{
  "student_name": "王小明",
  "student_id": "2024000000",
  "class": "计科 1 班",
  "course": "计算机系统实验",
  "instructor": "李老师",
  "institution": "某某大学"
}
```

Rules:
- Profile fields are reusable defaults, not experiment results.
- Empty strings mean unknown.
- Use cached values silently unless the user asks to update them or current materials
  explicitly conflict with them.

## `report_context.json`

Created in every output directory by `scripts/init_output_dir.py`.

```json
{
  "experiment_name": "cuda-vector-add",
  "report_type": "standard-executable",
  "run_mode": "auto",
  "created_at": "2026-04-30T12:00:00",
  "profile_path": "C:/Users/name/.qoobee-skills/lab-report/profile.json",
  "profile_complete": true,
  "source_files": [
    "C:/path/to/manual.pdf"
  ],
  "language": "zh",
  "screenshot_preference": "key",
  "notes": ""
}
```

Allowed values:
- `report_type`: `standard-executable`, `data-provided`, `paper-only`
- `run_mode`: `manual`, `auto`
- `language`: `zh`, `en`, or empty when not inferred yet
- `screenshot_preference`: `key`, `all`, `none`

Rules:
- `report_context.json` records the current run's control decisions.
- Do not put personal profile fields here except profile status/path.
- Agents should read this file when they need run mode, report type, source files, or
  screenshot preference.

## `experiment_info.json`

Created during initialization and updated by `experiment-summarizer`.

```json
{
  "experiment_name": "cuda-vector-add",
  "title": "CUDA Vector Addition",
  "course": "并行计算实验",
  "student_name": "王小明",
  "student_id": "2024000000",
  "class": "计科 1 班",
  "date": "2026-04-30",
  "instructor": "李老师",
  "institution": "某某大学"
}
```

Rules:
- This file contains report-facing metadata only.
- Do not store `run_mode` or `report_type` here; those belong in `report_context.json`.
- `date` defaults to today's date and may be overridden if the source materials specify an
  experiment date.

## `procedure_summary.md`

Markdown structure produced by `experiment-summarizer`.

```markdown
# <Experiment Title>

## Report Type
standard-executable

## Objective
...

## Equipment / Environment
| Equipment/Software | Model/Version | Notes |
|--------------------|---------------|-------|

## Theory
...

## Procedure
### Step 1: <Step Name>
**Type:** executable
**Description:** ...
**Command:** `...`
**Expected outcome:** ...
**Data to collect:** ...

## Provided Data
| Source | Description | How to use |
|--------|-------------|------------|

## Writing Outline
1. ...

## Safety Notes
- ...
```

Path-specific expectations:
- `standard-executable`: include concrete executable steps with commands whenever possible.
- `data-provided`: include `Provided Data`; procedure may describe how the data was obtained
  rather than commands to run.
- `paper-only`: include `Writing Outline`; do not invent executable steps.

## `run_log.md`

Produced only for `standard-executable` when commands are run.

```markdown
# Run Log — <Experiment Title>

**Date:** <YYYY-MM-DD HH:MM>
**Environment:** <OS, shell, key tools>
**Run mode:** auto

---

### Step 1: <Step Name>
- **Command:** `<command>`
- **Status:** success | failed | skipped
- **Failure class:** none | blocking | non-blocking
- **Key output:** ...
- **Screenshot:** `screenshots/step1.png` | none | unavailable (no tool)
- **Raw output:** `raw_outputs/step1.txt`
- **Notes:** ...
```

Rules:
- Record exactly what happened.
- Do not rewrite command output to make it look successful.
- If a failure is `blocking`, stop the run and ask the user how to proceed.

## `report_draft.md`

Produced by `report-writer` template mode.

Rules:
- May contain `[TO BE FILLED]` placeholders for unknown result data.
- Should not contain fabricated results.
- For `paper-only`, avoid execution/screenshot placeholders unless the user provided
  supporting images.

## `final_report.md`

Produced by `report-writer` fill-in mode.

Rules:
- Must not contain unresolved `[TO BE FILLED]` or `[SCREENSHOT: ...]` markers.
- Must only use evidence from source materials, provided data, run logs, raw outputs, or user
  corrections.
- If key evidence is missing, stop and ask instead of inventing it.
