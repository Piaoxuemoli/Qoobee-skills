"""
Initialize output directory structure for a lab-report experiment.

Usage:
    python init_output_dir.py <experiment-name> [--base-dir <path>]

Creates:
    outputs/<name>/
    outputs/<name>/screenshots/
    outputs/<name>/raw_outputs/

Validates experiment name: lowercase letters, digits, hyphens, max 64 chars.
"""

import argparse
import json
import os
import re
import sys


def validate_name(name: str) -> bool:
    """Validate experiment name: a-z, 0-9, hyphens, 1-64 chars."""
    if not name or len(name) > 64:
        return False
    return bool(re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', name))


def init_output_dir(experiment_name: str, base_dir: str | None = None) -> str:
    """Create output directory structure. Returns the experiment directory path."""
    if not validate_name(experiment_name):
        print(f"ERROR: Invalid experiment name '{experiment_name}'.")
        print("       Must be lowercase letters, digits, and hyphens (1-64 chars).")
        print("       Examples: cuda-vector-add, chem-titration-lab3, ml-mnist-exp1")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = base_dir or os.path.dirname(script_dir)
    exp_dir = os.path.join(skill_root, "outputs", experiment_name)

    if os.path.exists(exp_dir):
        print(f"ERROR: Experiment directory already exists: {exp_dir}")
        print("       Choose a different name or remove the existing directory.")
        sys.exit(1)

    screenshots_dir = os.path.join(exp_dir, "screenshots")
    raw_outputs_dir = os.path.join(exp_dir, "raw_outputs")

    os.makedirs(screenshots_dir)
    os.makedirs(raw_outputs_dir)

    # Create skeleton experiment_info.json
    info = {
        "experiment_name": experiment_name,
        "title": "",
        "course": "",
        "student_name": "",
        "student_id": "",
        "class": "",
        "date": "",
        "instructor": "",
        "institution": ""
    }
    info_path = os.path.join(exp_dir, "experiment_info.json")
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    print(f"Created experiment directory:")
    print(f"  {exp_dir}/")
    print(f"    experiment_info.json")
    print(f"    screenshots/")
    print(f"    raw_outputs/")
    return exp_dir


def main():
    parser = argparse.ArgumentParser(
        description="Initialize output directory for a lab-report experiment."
    )
    parser.add_argument(
        "experiment_name",
        help="Experiment name slug (a-z, 0-9, hyphens). e.g., cuda-vector-add"
    )
    parser.add_argument(
        "--base-dir",
        default=None,
        help="Base skill directory (default: parent of scripts/)."
    )
    args = parser.parse_args()
    init_output_dir(args.experiment_name, args.base_dir)


if __name__ == "__main__":
    main()
