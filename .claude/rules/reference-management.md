# Reference Code Management

## Purpose

External reference projects (high-star GitHub repos used for inspiration or code reuse)
are stored in `references/` at the project root. This keeps them isolated from project
code and prevents accidental commits of third-party source.

## Rules

- All external reference code goes under `references/<project-name>/`.
- `references/` is listed in `.gitignore` — never commit it.
- Each reference project keeps its original directory structure (no flattening).
- `references/README.md` documents what each project is, why it was cloned, and what
  parts are most useful.
- Project code (`coursework-helper/`, `lab-report/`, `terminal-screenshot/`) must never
  contain files copied wholesale from references. Only adapted/dervied code belongs there.
- When adapting code from a reference, add a comment noting the source:
  ```python
  # Adapted from references/mckinsey-pptx/mckinsey_pptx/theme.py (MIT License)
  ```

## Adding New References

```bash
cd references
git clone --depth 1 <url> <short-name>
```

Then update `references/README.md` with the new entry.
