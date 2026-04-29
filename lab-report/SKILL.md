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

Automate the full experiment-report pipeline: extract procedures from source materials,
generate a report template, execute the experiment with terminal screenshots, and fill
in the final report with results.

## Overview

This skill uses three sub-agents to break down the report-writing process into a 4-phase
pipeline. Each phase must complete and get user confirmation before the next begins.

| Phase | Agent | What Happens |
|-------|-------|--------------|
| 0 — Setup | (none) | Initialize output directory |
| 1 — Summarize | `agents/experiment-summarizer.md` | Extract procedure from files, collect personal info |
| 2 — Template | `agents/report-writer.md` (template mode) | Generate report draft with placeholders |
| 3 — Execute | `agents/experiment-runner.md` | Run experiment step-by-step, capture screenshots |
| 4 — Complete | `agents/report-writer.md` (fill-in mode) | Fill placeholders with real data, finalize report |

**Important:** Complete each phase fully and get user confirmation before moving to the next.
Do not skip phases without asking the user.

## Phase 0: Output Directory Setup

Before any work begins, set up the output directory.

1. Ask the user: "What should we name this experiment?" Suggest a short slug based on context
   (e.g., `cuda-vector-add`, `chem-titration-lab3`, `ml-mnist-exp1`).
2. Run the setup script:
   ```bash
   python lab-report/scripts/init_output_dir.py <experiment-name>
   ```
   The script creates `outputs/<experiment-name>/` with `screenshots/` and `raw_outputs/`
   subdirectories, plus an `experiment_info.json` skeleton.
3. If the script errors (invalid name, directory exists), resolve the issue with the user
   and retry.

Store the output directory path as `output_dir` for all subsequent phases:
```
output_dir = lab-report/outputs/<experiment-name>
```

## Phase 1: Summarize Experiment

**Goal:** Extract a structured procedure from source materials and collect personal metadata.

1. Read `agents/experiment-summarizer.md` to load the sub-agent instructions.
2. Ask the user for their experiment source files: "Please provide your lab manual, PPT,
   Word document, PDF, or any other experiment materials (file paths)."
3. Launch the experiment-summarizer sub-agent with these parameters:
   - **source_files**: The file paths the user provided
   - **output_dir**: The `output_dir` from Phase 0
   - **context**: Any experiment description the user gave in conversation
4. The agent will:
   - Read and parse all source files (using strategies from `references/file-readers.md`)
   - Present extracted experiment info to the user
   - Collect personal metadata (name, student ID, class, date, instructor)
   - Write `experiment_info.json` and `procedure_summary.md`
5. After the agent completes, review its outputs with the user.
   Confirm the procedure is correct and the personal info is accurate.
6. **Do not proceed until the user confirms.** Accepted signals: "confirmed," "looks good,"
   "OK," "yes," "correct."

## Phase 2: Generate Report Template

**Goal:** Create a structured report draft with placeholders for results.

1. Read `agents/report-writer.md` to load the sub-agent instructions.
2. Launch the report-writer sub-agent in **template-generation mode** with:
   - **procedure_summary_path**: `output_dir/procedure_summary.md`
   - **experiment_info_path**: `output_dir/experiment_info.json`
   - **output_dir**: Same `output_dir`
   - **language**: `"zh"` if the user's conversation is in Chinese, `"en"` otherwise
3. The agent will:
   - Ask the user if they have a custom template (if yes, read and adapt it)
   - If no template: use the default from `references/report-template-zh.md` or
     `references/report-template-en.md`
   - Fill in known info (header, objective, equipment, theory, procedure steps)
   - Add `[TO BE FILLED]` placeholders for results, data, analysis, and conclusion
   - Add `[SCREENSHOT: step<N>]` placeholders for screenshots
   - Write `report_draft.md`
4. Present the draft to the user. Ask: "Does this structure look right? Anything to change?"
5. **Do not proceed until the user confirms the template.**

## Phase 3: Execute Experiment

**Goal:** Run the experiment step-by-step, capture outputs and screenshots.

1. Ask the user about screenshot preferences: "For screenshots, should I capture every step,
   only key output steps (default), or no screenshots?"
2. Read `agents/experiment-runner.md` to load the sub-agent instructions.
3. Launch the experiment-runner sub-agent with:
   - **procedure_summary_path**: `output_dir/procedure_summary.md`
   - **output_dir**: Same `output_dir`
   - **screenshot_preference**: `"key"` (default), `"all"`, or `"none"`
4. The agent will:
   - Present each step to the user for approval
   - Accept "yes," "run all," "skip," or "modify: <cmd>" per step
   - Execute commands and capture stdout/stderr
   - Use the **terminal-screenshot** skill to render key outputs as PNGs
   - Save screenshots to `screenshots/step<N>.png`
   - Save raw outputs to `raw_outputs/step<N>.txt`
   - Write `run_log.md` summarizing all steps
5. The user can approve steps one at a time or say "run all" for hands-off execution.
   Destructive commands ALWAYS require double confirmation regardless of mode.
6. After all steps complete, confirm with the user: "Experiment complete? Proceed to
   final report?"

**If the experiment has no executable steps** (theoretical / paper-only experiment):
Ask the user if they want to skip Phase 3. If yes, the user should provide their data
and results directly. Then proceed to Phase 4 with user-provided data in place of run_log.

## Phase 4: Complete Final Report

**Goal:** Fill in all placeholders with actual results and produce the final report.

1. Read `agents/report-writer.md` (again) to load the sub-agent instructions.
2. Launch the report-writer sub-agent in **fill-in mode** with:
   - **draft_path**: `output_dir/report_draft.md`
   - **run_log_path**: `output_dir/run_log.md`
   - **screenshots_dir**: `output_dir/screenshots/`
   - **raw_outputs_dir**: `output_dir/raw_outputs/`
   - **output_path**: `output_dir/final_report.md`
3. The agent will:
   - Read the draft and identify all `[TO BE FILLED]` and `[SCREENSHOT: ...]` placeholders
   - Extract actual data from `run_log.md` and raw outputs
   - Fill in results, data tables, analysis, and conclusion
   - Insert screenshots as inline images
   - Write `final_report.md`
4. Present the final report to the user.
5. Ask: "Would you like any revisions, or is this final?"
   - If revisions needed: note what the user wants changed, re-invoke the report-writer
     in fill-in mode with updated instructions.
   - If final: celebrate completion. Offer to convert to PDF: "Would you like me to
     convert this to PDF? (requires pandoc: `pandoc final_report.md -o final_report.pdf`)"

## Handling Variations

### Skip Phase 3 (No Execution)
If the user already has data or the experiment is theoretical:
- Skip Phase 3, ask the user to provide their results.
- In Phase 4, the report-writer works from user-provided data.

### Partial Rerun
If the user wants to redo a specific step:
- Re-launch the experiment-runner for only that step.
- Update `run_log.md` and redo Phase 4.

### Revise Report After Phase 4
Re-invoke the report-writer in fill-in mode with specific revision instructions.

## Output Directory Structure

All generated content goes under `outputs/<experiment-name>/`. This directory is gitignored
— it is strictly separated from the skill's own source code.

```
outputs/<experiment-name>/
├── experiment_info.json     # Personal metadata
├── procedure_summary.md     # Structured procedure
├── report_draft.md          # Template with placeholders
├── run_log.md               # Step-by-step execution record
├── final_report.md          # Completed report
├── screenshots/
│   └── step<N>.png          # Terminal screenshots
└── raw_outputs/
    └── step<N>.txt           # Raw command outputs
```

**Never write generated content to `agents/`, `references/`, `scripts/`, or the skill root.**

## Dependencies

- **terminal-screenshot skill**: Required for Phase 3 screenshot capture.
- **Python**: Required for `scripts/init_output_dir.py`.
- **File reading tools**: `pdftotext`, `python-docx`, `python-pptx`, `pandoc` (auto-detected,
  fall back gracefully if missing).
