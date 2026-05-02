# Handbook Writer Agent

The handbook is compiled by `scripts/compile_handbook.py` — this agent only
handles QA verification after compilation.

## Role

After `compile_handbook.py` produces `04_final/final_handbook.md`, verify that
the output is complete and correct.

## Process

### Step 1: Verify Completeness

Read the outline (`02_outline/outline.md`) and check that every source directory
listed appears in the handbook.

### Step 2: Verify Image References

Check that all `![...](...)` image paths in the handbook point to files that
actually exist.

### Step 3: Write QA Report

Write `06_qa/qa_report.md`:

```markdown
# QA Report

## Content Coverage
- Source directories in outline: N
- Source directories in handbook: N
- Missing: [list, if any]

## Image References
- Total image references: N
- Valid (file exists): N
- Broken (file missing): [list, if any]

## Content Size
- Total characters: N
- Total lines: N

## Issues
- [any problems found]
```

## Rules

- Do NOT modify the handbook — only report issues.
- The script is the source of truth for content. If something is missing,
  the outline needs to be updated and the script re-run.
