# Git Branching Rules

## Branch Strategy

- Always create a feature branch from `master` before starting work:
  ```bash
  git checkout master && git pull && git checkout -b feature/<short-description>
  ```
- Never commit directly to `master`.
- Branch naming: `feature/<desc>`, `fix/<desc>`, `refactor/<desc>`, `docs/<desc>`.

## Commit Discipline

- Make small, logical commits — one logical change per commit.
- Commit message format: `<type>: <description>`
  - Types: `feat`, `fix`, `refactor`, `docs`, `chore`, `test`
  - Description: imperative mood, lowercase, no period at end
  - Examples:
    - `feat: add PPT engine theme system`
    - `fix: correct Chinese font fallback in slide-writer`
    - `refactor: extract slide card parser from delivery-packager`
    - `docs: update README with PPT engine usage`

## Merge

- Merge feature branch into `master` via PR or explicit merge commit.
- Delete feature branch after merge.
