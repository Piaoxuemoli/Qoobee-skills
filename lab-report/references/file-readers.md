# File Readers Reference

Strategies for reading experiment source materials in various formats.

## PDF Files (.pdf)

Prefer text extraction, fall back to vision:

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
