"""
Initialize output directory for coursework-helper.

Usage:
    python init_output_dir.py <assignment-name> --assignment-type paper --delivery-formats "md|docx"
"""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import re
from pathlib import Path
import sys


ASSIGNMENT_TYPES = {"slides", "paper", "script", "mixed"}
DELIVERY_FORMATS = {"md", "pptx", "docx", "pdf"}
TONES = {"normal-student", "formal-academic", "casual-reflection", "presentation-friendly"}
SLIDE_SIZES = {"widescreen-16-9"}


def validate_name(name: str) -> bool:
    return bool(name and len(name) <= 64 and re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name))


def split_pipe_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split("|") if item.strip()]


def normalize_formats(value: str | None, assignment_type: str) -> list[str]:
    default_by_type = {
        "slides": "md|pptx",
        "paper": "md|docx",
        "script": "md",
        "mixed": "md|pptx|docx",
    }
    formats = [item.lower() for item in split_pipe_list(value or default_by_type[assignment_type])]
    invalid = [item for item in formats if item not in DELIVERY_FORMATS]
    if invalid:
        print(f"ERROR: Invalid delivery format(s): {', '.join(invalid)}", file=sys.stderr)
        sys.exit(1)
    return list(dict.fromkeys(formats))


def init_output_dir(
    assignment_name: str,
    base_dir: str | None,
    assignment_type: str,
    source_files: list[str],
    delivery_formats: list[str],
    language: str,
    course: str,
    topic: str,
    audience: str,
    tone: str,
    length_hint: str,
    slide_size: str,
    source_manifest_path: str,
    notes: str,
) -> Path:
    if not validate_name(assignment_name):
        print("ERROR: Assignment name must be lowercase letters, digits, and hyphens.", file=sys.stderr)
        sys.exit(1)
    if assignment_type not in ASSIGNMENT_TYPES:
        print(f"ERROR: Invalid assignment type: {assignment_type}", file=sys.stderr)
        sys.exit(1)
    if tone not in TONES:
        print(f"ERROR: Invalid tone: {tone}", file=sys.stderr)
        sys.exit(1)
    if slide_size not in SLIDE_SIZES:
        print(f"ERROR: Invalid slide size: {slide_size}", file=sys.stderr)
        sys.exit(1)

    skill_root = Path(base_dir).resolve() if base_dir else Path(__file__).resolve().parents[1]
    output_dir = skill_root / "outputs" / assignment_name
    if output_dir.exists():
        print(f"ERROR: Output directory already exists: {output_dir}", file=sys.stderr)
        sys.exit(1)

    (output_dir / "assets").mkdir(parents=True)

    context = {
        "assignment_name": assignment_name,
        "assignment_type": assignment_type,
        "created_at": datetime.now().replace(microsecond=0).isoformat(),
        "source_files": source_files,
        "source_manifest_path": source_manifest_path,
        "language": language,
        "course": course,
        "topic": topic,
        "audience": audience or "course instructor",
        "tone": tone,
        "length_hint": length_hint,
        "slide_size": slide_size,
        "delivery_formats": delivery_formats,
        "notes": notes,
    }
    with (output_dir / "assignment_context.json").open("w", encoding="utf-8") as f:
        json.dump(context, f, ensure_ascii=False, indent=2)
        f.write("\n")

    for filename in [
        "source_manifest.json",
        "outline.md",
        "evidence_notes.md",
        "final_paper.md",
        "final_slides.md",
        "final_script.md",
        "delivery_manifest.json",
    ]:
        (output_dir / filename).touch()

    print(f"Created coursework output directory: {output_dir}")
    return output_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize coursework-helper output directory.")
    parser.add_argument("assignment_name")
    parser.add_argument("--base-dir", default=None)
    parser.add_argument("--assignment-type", choices=sorted(ASSIGNMENT_TYPES), default="paper")
    parser.add_argument("--source-files", default="")
    parser.add_argument("--delivery-formats", default=None)
    parser.add_argument("--language", default="")
    parser.add_argument("--course", default="")
    parser.add_argument("--topic", default="")
    parser.add_argument("--audience", default="")
    parser.add_argument("--tone", choices=sorted(TONES), default="normal-student")
    parser.add_argument("--length-hint", default="")
    parser.add_argument("--slide-size", choices=sorted(SLIDE_SIZES), default="widescreen-16-9")
    parser.add_argument("--source-manifest-path", default="")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    init_output_dir(
        args.assignment_name,
        args.base_dir,
        args.assignment_type,
        split_pipe_list(args.source_files),
        normalize_formats(args.delivery_formats, args.assignment_type),
        args.language,
        args.course,
        args.topic,
        args.audience,
        args.tone,
        args.length_hint,
        args.slide_size,
        args.source_manifest_path,
        args.notes,
    )


if __name__ == "__main__":
    main()
