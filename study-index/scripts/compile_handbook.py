"""Compile all extracted text into a single handbook with index.

Reads the outline to map chapters to source directories, then concatenates
ALL text files from each source directory into one complete handbook.
No summarization — every character from every source file is preserved.

Usage:
    python compile_handbook.py \
        --outline "outputs/course/02_outline/outline.md" \
        --extracted "outputs/course/01_extracted/" \
        --filtered "outputs/course/01_filtered/" \
        --output "outputs/course/04_final/final_handbook.md"
"""
from __future__ import annotations
import argparse
import os
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Dict, List, Tuple


def _parse_outline(outline_path: Path) -> List[Dict]:
    """Parse outline.md to extract chapter-to-source mapping.

    Expected format in outline:
        ## Chapter 1: <title>
        - 来源: source_dir_1, source_dir_2

    Returns list of:
        {"chapter": "第一章 <title>", "sources": ["dir1", "dir2"], "subsections": [...]}
    """
    text = outline_path.read_text(encoding="utf-8")
    chapters = []
    current_chapter = None

    for line in text.splitlines():
        line = line.strip()

        # match chapter heading: ## Chapter N: Title or ## 第N章 Title
        ch_match = re.match(r"^##\s+(.+)", line)
        if ch_match and not line.startswith("###"):
            heading = ch_match.group(1).strip()
            # skip non-chapter headings like "## 关键词索引"
            if re.match(r"(Chapter|第)", heading, re.IGNORECASE):
                current_chapter = {
                    "chapter": heading,
                    "sources": [],
                    "subsections": [],
                }
                chapters.append(current_chapter)
            else:
                current_chapter = None
            continue

        if current_chapter is None:
            continue

        # match source line: - 来源: dir1, dir2
        src_match = re.match(r"^-\s*来源:\s*(.+)", line)
        if src_match:
            dirs = [d.strip() for d in src_match.group(1).split(",") if d.strip()]
            current_chapter["sources"] = dirs
            continue

        # match subsection: ### N.M Title
        sub_match = re.match(r"^###\s+(.+)", line)
        if sub_match:
            current_chapter["subsections"].append(sub_match.group(1).strip())

    return chapters


def _get_text_files(src_dir: Path) -> List[Path]:
    """Get all text files from a source directory, sorted naturally."""
    txt_files = sorted(src_dir.glob("*.txt"))
    return txt_files


def _get_images_for_text(txt_file: Path, filtered_dir: Path | None,
                          extracted_dir: Path) -> List[Path]:
    """Find images corresponding to a text file.

    For slide_05.txt -> look for slide_05_img_*.png in the same directory.
    Search filtered first, fall back to extracted.
    """
    stem = txt_file.stem  # e.g. "slide_05" or "page_01"
    parent_name = txt_file.parent.name  # source dir name

    images = []
    # search filtered first
    search_dirs = []
    if filtered_dir:
        fdir = filtered_dir / parent_name
        if fdir.is_dir():
            search_dirs.append(fdir)
    search_dirs.append(txt_file.parent)  # fallback to extracted

    for sdir in search_dirs:
        for ext in ("*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp", "*.webp"):
            for img in sorted(sdir.glob(f"{stem}_img_*{ext[1:]}")):
                if img not in images:
                    images.append(img)
        if images:
            break  # found in filtered, don't check extracted

    return images


def _chapter_sort_key(chapter: Dict) -> Tuple[int, int]:
    """Sort chapters by their number."""
    name = chapter["chapter"]
    # extract first number
    nums = re.findall(r"\d+", name)
    if nums:
        return (int(nums[0]), 0)
    return (999, 0)


def _build_keyword_index(chapters_text: str) -> str:
    """Extract a simple keyword index from the handbook text."""
    keywords = {}

    # common course keywords to look for
    kw_patterns = [
        r"Amdahl", r"CGMA", r"CUDA", r"Flynn", r"MPI", r"MSI",
        r"PCAM", r"Warp|线程束", r"共享内存", r"控制分歧", r"前缀和|Prefix Sum|Scan",
        r"加速比", r"域分解|功能分解", r"数据竞态|Data Race", r"缓存一致性",
        r"超立方体|Hypercube", r"素数筛选|Sieve", r"矩阵乘法",
        r"网络直径|对分宽度", r"负载均衡", r"循环分配|块分配",
        r"尴尬的并行|Embarrassingly Parallel", r"私有化直方图",
        r"SIMD|MIMD|SISD|MISD", r"原子操作|Atomic",
        r"并行规约|Reduction", r"内存合并|Coalescing",
        r"分块矩阵|Tiled", r"伪共享|False Sharing",
    ]

    lines = chapters_text.splitlines()
    for kw_pat in kw_patterns:
        for i, line in enumerate(lines):
            if re.search(kw_pat, line, re.IGNORECASE):
                # find the nearest heading above this line
                heading = ""
                for j in range(i, -1, -1):
                    hm = re.match(r"^(#{1,3})\s+(.+)", lines[j])
                    if hm:
                        heading = hm.group(2).strip()
                        break
                if heading:
                    base_kw = kw_pat.split("|")[0]
                    if base_kw not in keywords:
                        keywords[base_kw] = heading
                break  # first match is enough per keyword

    if not keywords:
        return ""

    idx_lines = ["\n---\n\n## 关键词索引\n", "| 关键词 | 位置 |", "|--------|------|"]
    for kw, loc in sorted(keywords.items(), key=lambda x: x[0]):
        idx_lines.append(f"| {kw} | {loc} |")

    return "\n".join(idx_lines) + "\n"


def compile_handbook(outline_path: Path, extracted_dir: Path,
                     filtered_dir: Path | None, output_path: Path,
                     course_name: str) -> Dict:
    """Compile all extracted content into a single handbook."""
    chapters = _parse_outline(outline_path)

    if not chapters:
        print("Warning: no chapters parsed from outline, using all source dirs",
              file=sys.stderr)
        # fallback: one chapter per source directory
        for src_dir in sorted(extracted_dir.iterdir()):
            if src_dir.is_dir():
                chapters.append({
                    "chapter": src_dir.name,
                    "sources": [src_dir.name],
                    "subsections": [],
                })

    # sort chapters
    chapters.sort(key=_chapter_sort_key)

    # build handbook
    parts = []

    # header
    parts.append(f"# {course_name} — 速查手册\n")
    parts.append(f"> 本手册包含课程所有资料的完整内容，按章节组织。\n")
    parts.append("> 每个章节下列出对应的源文件，内容为原文完整保留。\n")

    # table of contents
    toc = ["## 目录\n"]
    for ch in chapters:
        ch_name = ch["chapter"]
        anchor = re.sub(r"[^\w\u4e00-\u9fff]+", "-", ch_name).strip("-").lower()
        toc.append(f"- [{ch_name}](#{anchor})")
    toc.append("- [关键词索引](#关键词索引)")
    parts.append("\n".join(toc) + "\n")

    # chapters
    for ch in chapters:
        ch_name = ch["chapter"]
        parts.append(f"\n---\n\n## {ch_name}\n")

        for src_name in ch["sources"]:
            src_dir = extracted_dir / src_name
            if not src_dir.is_dir():
                parts.append(f"\n> ⚠️ 源目录未找到: {src_name}\n")
                continue

            parts.append(f"\n### 📁 {src_name}\n")

            txt_files = _get_text_files(src_dir)
            if not txt_files:
                parts.append("\n> （无文本内容）\n")
                continue

            for txt_file in txt_files:
                # read text content
                try:
                    content = txt_file.read_text(encoding="utf-8").strip()
                except Exception:
                    content = f"[读取失败: {txt_file.name}]"

                if content:
                    parts.append(f"\n{content}\n")

                # insert corresponding images
                images = _get_images_for_text(txt_file, filtered_dir, extracted_dir)
                for img in images:
                    # relative path from output .md file to image
                    rel = os.path.relpath(img, output_path.parent)
                    # normalize to forward slashes for Markdown
                    rel = PurePosixPath(Path(rel).as_posix())
                    parts.append(f"\n![{img.stem}]({rel})\n")

    # keyword index
    all_text = "\n".join(parts)
    index_text = _build_keyword_index(all_text)
    if index_text:
        parts.append(index_text)

    # write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    handbook = "\n".join(parts)
    output_path.write_text(handbook, encoding="utf-8")

    return {
        "chapters": len(chapters),
        "total_sources": sum(len(ch["sources"]) for ch in chapters),
        "total_chars": len(handbook),
        "output_path": str(output_path),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compile all extracted content into a complete handbook")
    parser.add_argument("--outline", required=True,
                        help="Path to outline.md")
    parser.add_argument("--extracted", required=True,
                        help="01_extracted/ directory")
    parser.add_argument("--filtered", default=None,
                        help="01_filtered/ directory (optional, for filtered images)")
    parser.add_argument("--output", required=True,
                        help="Output handbook .md path")
    parser.add_argument("--course-name", default="课程",
                        help="Course name for the header")
    args = parser.parse_args()

    result = compile_handbook(
        outline_path=Path(args.outline),
        extracted_dir=Path(args.extracted),
        filtered_dir=Path(args.filtered) if args.filtered else None,
        output_path=Path(args.output),
        course_name=args.course_name,
    )

    print(f"Handbook compiled: {result['chapters']} chapters, "
          f"{result['total_sources']} sources, "
          f"{result['total_chars']:,} chars")
    print(f"Output: {result['output_path']}")


if __name__ == "__main__":
    main()
