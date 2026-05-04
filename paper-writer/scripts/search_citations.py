"""Search academic papers for real citations.

Uses Semantic Scholar API (primary) with arXiv API as fallback.

Usage:
    python search_citations.py \
        --query "transformer attention mechanism" \
        --limit 5 \
        --output "outputs/paper/00_admin/citations.json"
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, List, Optional


def _format_citation(paper: Dict[str, Any]) -> str:
    """Format a paper dict into a citation string."""
    authors = paper.get("authors", [])
    if len(authors) > 3:
        author_str = ", ".join(authors[:2]) + ", et al."
    elif len(authors) > 1:
        author_str = ", ".join(authors[:-1]) + ", & " + authors[-1]
    else:
        author_str = authors[0] if authors else "Unknown"

    year = paper.get("year", "n.d.")
    title = paper.get("title", "Untitled")
    arxiv_id = paper.get("arxiv_id")

    if arxiv_id:
        return f"{author_str} ({year}). {title}. arXiv:{arxiv_id}."
    doi = paper.get("doi")
    if doi:
        return f"{author_str} ({year}). {title}. DOI:{doi}."
    return f"{author_str} ({year}). {title}."


def search_semantic_scholar(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Search Semantic Scholar for papers."""
    params = urllib.parse.urlencode({
        "query": query,
        "fields": "title,year,authors,abstract,externalIds,citationCount,url",
        "limit": limit,
    })
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?{params}"

    req = urllib.request.Request(url, headers={
        "User-Agent": "Auto-college/paper-writer (student project)"
    })

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Semantic Scholar error: {e}", file=sys.stderr)
        return []

    papers = []
    for item in data.get("data", []):
        ext_ids = item.get("externalIds", {}) or {}
        authors = [a["name"] for a in (item.get("authors") or [])]
        arxiv_id = ext_ids.get("ArXiv")

        paper = {
            "title": item.get("title", ""),
            "authors": authors,
            "year": item.get("year"),
            "arxiv_id": arxiv_id,
            "doi": ext_ids.get("DOI"),
            "citation_count": item.get("citationCount", 0),
            "abstract": (item.get("abstract") or "")[:300],
            "url": item.get("url", ""),
        }
        paper["formatted"] = _format_citation(paper)
        papers.append(paper)

    return papers


def search_arxiv(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Search arXiv API as fallback."""
    params = urllib.parse.urlencode({
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": limit,
        "sortBy": "relevance",
        "sortOrder": "descending",
    })
    url = f"http://export.arxiv.org/api/query?{params}"

    req = urllib.request.Request(url, headers={
        "User-Agent": "Auto-college/paper-writer (student project)"
    })

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_text = resp.read().decode("utf-8")
    except Exception as e:
        print(f"arXiv error: {e}", file=sys.stderr)
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)

    papers = []
    for entry in root.findall("atom:entry", ns):
        title = (entry.findtext("atom:title", "", ns) or "").strip()
        title = re.sub(r"\s+", " ", title)

        summary = (entry.findtext("atom:summary", "", ns) or "").strip()
        published = (entry.findtext("atom:published", "", ns) or "")
        year = int(published[:4]) if published[:4].isdigit() else None

        authors = []
        for author in entry.findall("atom:author", ns):
            name = author.findtext("atom:name", "", ns)
            if name:
                authors.append(name.strip())

        id_url = (entry.findtext("atom:id", "", ns) or "")
        arxiv_id = id_url.replace("http://arxiv.org/abs/", "").replace("https://arxiv.org/abs/", "")
        arxiv_id = re.sub(r"v\d+$", "", arxiv_id)

        paper = {
            "title": title,
            "authors": authors,
            "year": year,
            "arxiv_id": arxiv_id,
            "doi": None,
            "citation_count": 0,
            "abstract": summary[:300],
            "url": f"https://arxiv.org/abs/{arxiv_id}",
        }
        paper["formatted"] = _format_citation(paper)
        papers.append(paper)

    return papers


def search_citations(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """Search for papers, trying Semantic Scholar first, then arXiv."""
    papers = search_semantic_scholar(query, limit)
    if papers:
        return papers

    print("Semantic Scholar unavailable, trying arXiv...", file=sys.stderr)
    time.sleep(1)  # be polite to arXiv
    return search_arxiv(query, limit)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Search academic papers for citations")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--limit", type=int, default=5, help="Max results")
    parser.add_argument("--output", required=True, help="Output JSON path")
    args = parser.parse_args()

    papers = search_citations(args.query, args.limit)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Found {len(papers)} papers for: {args.query}")
    for i, p in enumerate(papers, 1):
        print(f"  [{i}] {p['formatted']}")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()
