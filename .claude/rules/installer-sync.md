# Installer & README Sync Rules

## When to Update

After adding, removing, or renaming any skill, update **all** of the following:

1. **`setup.js`** — `SKILLS` array must list every installable skill
2. **`README.md`** — skills section must reflect current inventory
3. **`docs/<skill>.md`** — create or remove corresponding doc page

## Checklist

```text
□ SKILLS array in setup.js matches actual skill directories
□ README.md lists all skills with correct links to docs/
□ docs/ has a .md file for each skill
□ Skill descriptions and counts are accurate
```

## Why

Users install via `setup.js` (one-liner curl). If it's missing a skill, new users
won't get it. If README is stale, users won't know a skill exists.
