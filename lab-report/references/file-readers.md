# File Readers Reference

Strategies for reading experiment source materials in various formats.

## Official Anthropic Skills First

Before reading source materials, the orchestrator must check that the needed official
Anthropic skills are installed:

```bash
python lab-report/scripts/check_official_skills.py --source-files "<path1>|<path2>"
```

If the check reports missing skills, run:

```bash
python lab-report/scripts/check_official_skills.py --install --source-files "<path1>|<path2>"
```

This bootstraps OpenSkill through `npx -y skills add anthropics/skills@<skill> -g -y`. The supported
official file-processing skills are:

| Source format | Official skill | Use for |
|---------------|----------------|---------|
| `.pdf` | `pdf` | Reading/extracting text and tables from PDFs; OCR or image fallback for scanned pages |
| `.doc`, `.docx` | `docx` | Reading Word lab manuals, extracting tables/images, and producing DOCX outputs if requested |
| `.ppt`, `.pptx` | `pptx` | Reading slide decks, speaker notes, screenshots, and procedure slides |
| `.xls`, `.xlsx`, `.xlsm`, `.csv`, `.tsv` | `xlsx` | Reading data tables, experiment results, measurements, and spreadsheet outputs |

Use the official skill instructions as the primary source of extraction strategy. The
fallbacks below are only for environments where the relevant official skill is unavailable
or the official skill's preferred tool fails on a specific file.

## PDF Files (.pdf)

Primary skill: `pdf`. Prefer text extraction, fall back to vision:

1. **`pdftotext -layout`** (from poppler-utils) — best for text-based PDFs, preserves layout.
   ```bash
   pdftotext -layout document.pdf output.txt
   ```
2. **`pdfplumber`** (Python) — good for mixed text/tables.
   ```bash
   python -c "import pdfplumber; pdf = pdfplumber.open('doc.pdf'); print(pdf.pages[0].extract_text())"
   ```
3. **`PyPDF2` / `pypdf`** (Python) — basic text extraction.
4. **Vision fallback**: For image-based PDFs (scanned documents, slides exported as PDF), convert pages to images and use vision capabilities. Not all pages — sample enough to capture the procedure.

## Word Documents (.docx)

Primary skill: `docx`.

1. **`python-docx`** (Python) — best for structured extraction:
   ```python
   from docx import Document
   doc = Document('lab.docx')
   for para in doc.paragraphs:
       print(para.text)
   for table in doc.tables:
       for row in table.rows:
           print('\t'.join(cell.text for cell in row.cells))
   ```
2. **`pandoc`** — converts to markdown:
   ```bash
   pandoc --from docx --to markdown document.docx
   ```

## PowerPoint (.pptx)

Primary skill: `pptx`.

1. **`python-pptx`** (Python):
   ```python
   from pptx import Presentation
   prs = Presentation('slides.pptx')
   for i, slide in enumerate(prs.slides):
       print(f"--- Slide {i+1} ---")
       for shape in slide.shapes:
           if hasattr(shape, "text"):
               print(shape.text)
   ```
2. Note: Slide order matters — procedure steps may span multiple slides.
3. Check slide notes for additional instructor notes.

## Plain Text (.txt, .md)

Read directly with the Read tool. No conversion needed.

## Images (PNG, JPG, WebP)

Use the `mcp__MiniMax__understand_image` tool or the built-in vision capability to read text from:
- Photos of whiteboards / blackboards
- Screenshots of lab manuals
- Photos of experiment setups
- Scanned pages

Prompt the vision tool with: "Extract all text from this image. Focus on experimental procedures, equipment lists, and measurement instructions."

## Spreadsheets (.xlsx, .xlsm, .csv, .tsv)

Primary skill: `xlsx`.

Use the `xlsx` skill for spreadsheet inspection, table normalization, formulas, charts, and
CSV/TSV cleanup. For lab reports, extract:

1. Column names and units
2. Raw measurements
3. Calculated results and formulas
4. Table captions or sheet names that explain context
5. Charts or plotted trends when present

When the spreadsheet is malformed, use the `xlsx` skill's cleanup guidance before summarizing
the data. Do not silently discard rows with parse errors; record cleanup assumptions in
`procedure_summary.md`.

## Mixed Content

If a file contains both text and images (e.g., a DOCX with embedded screenshots):
1. Extract text first using the appropriate text tool.
2. For embedded images that contain procedural information, save them temporarily and read with vision.

## Extraction Priorities

When reading source materials, focus on extracting in this order:
1. **Experiment title / topic**
2. **Objective / purpose** — what the experiment aims to demonstrate or measure
3. **Equipment and materials** — software, hardware, reagents, tools
4. **Step-by-step procedure** — numbered steps with concrete commands or actions
5. **Expected results** — what should be observed, calculated, or measured
6. **Safety notes** — any precautions or warnings
