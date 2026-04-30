# Default English Lab Report Template

Use this template when the user does not provide a custom template.

## Template Structure

```markdown
# <Experiment Title>

**Name:** <Student Name>
**Student ID:** <ID>
**Class:** <Class Name>
**Experiment Date:** <Date>
**Instructor:** <Instructor Name>

---

## 1. Objective

<Extracted from procedure_summary.md>

## 2. Equipment and Environment

| Equipment/Software | Model/Version | Quantity/Notes |
|--------------------|---------------|----------------|
| <Equipment 1>      | <Model 1>     | <Notes>        |

<Extracted from procedure_summary.md>

## 3. Theory

<Brief description of core principles, formulas, algorithms>

## 4. Procedure

### Step 1: <Step Name>

<Step description and commands to execute>

```bash
<command>
```

### Step 2: <Step Name>

<Step description and commands to execute>

```bash
<command>
```

<!-- Add more steps as needed -->

## 5. Results

### Step 1 Results

[TO BE FILLED]

[SCREENSHOT: step1]

### Step 2 Results

[TO BE FILLED]

[SCREENSHOT: step2]

<!-- Add more step results as needed -->

### Data Summary

| Metric | Value |
|--------|-------|
| <Metric 1> | [TO BE FILLED] |
| <Metric 2> | [TO BE FILLED] |

## 6. Analysis and Discussion

[TO BE FILLED]

## 7. Conclusion

[TO BE FILLED]
```

## Usage Notes

- `[TO BE FILLED]` placeholders are replaced by the report-writer agent during final fill-in with actual data and analysis.
- `[SCREENSHOT: stepN]` placeholders are replaced with inline screenshots.
- Personal info fields are auto-filled from `experiment_info.json`.
- Objective, equipment, and procedure are filled from `procedure_summary.md`.
