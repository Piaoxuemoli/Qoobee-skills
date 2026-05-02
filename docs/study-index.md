# study-index

将散乱的课程材料（PPT、PDF、文档、笔记）整理成一本带目录、带索引、带例题、带关键图片的速查手册。适用于开卷考试复习、课程笔记整理、知识收藏整理。

Organize scattered course materials (PPTs, PDFs, documents, notes) into an indexed study handbook with table of contents, key images, formulas, and example problems. For open-book exam prep, course note organization, and knowledge curation.

## 工作流 / Workflow

```text
输入材料 → 提取文字+图片 → 按主题归类 → 写速查手册 → 导出 PDF
Input → Extract text+images → Organize by topic → Write handbook → Export PDF
```

核心原则：**不丢失信息**。源材料中的关键图片、公式、图表必须提取并放到手册对应位置。

## 适用场景 / When To Use

可以直接这样说：

```text
帮我整理这些 PPT 和文档，做成开卷考试速查手册
```

```text
这几章的课件太散了，帮我整理成一个带目录的复习资料
```

```text
把这些 PDF 和 PPT 合并成一份可以打印的考试速查手册
```

## 输出结构 / Output Structure

```text
study-index/outputs/<course-name>/
├── 00_admin/
│   ├── study_context.json
│   └── extract_manifest.json
├── 01_extracted/          # 按来源分目录，每页/每节一个 txt + 图片
├── 02_outline/
│   └── outline.md         # 知识结构大纲（带图片引用）
├── 03_drafts/
│   └── draft_handbook.md
├── 04_final/
│   └── final_handbook.md  # 最终手册（图片用相对路径引用）
├── 05_exports/
│   └── final_handbook.pdf
├── 06_qa/
│   └── qa_report.md
└── assets/
```

## 支持的输入格式 / Supported Input Formats

| 格式 | 文字提取 | 图片提取 |
|------|---------|---------|
| PPT/PPTX | python-pptx | shape.image.blob |
| PDF | PyMuPDF (fitz) | page.get_images() |
| DOCX | python-docx | inline_shapes |
| Markdown/文本 | 直接读取 | — |

## 手册结构 / Handbook Structure

最终手册 `final_handbook.md` 包含：

1. **封面**：课程名 + 使用说明
2. **目录**：按章节组织，带锚点链接
3. **各章内容**：
   - 知识点描述
   - 关键公式/定理（引用块）
   - 关键图片（从源材料提取，内嵌）
   - 例题（从源材料提取）
4. **关键词索引**：关键词 → 章节位置

## 依赖 / Dependencies

- Python + `python-pptx`（PPTX 提取）
- Python + `PyMuPDF`（PDF 提取，`pip install pymupdf`）
- Python + `python-docx`（DOCX 提取）
- `pandoc`（可选，Markdown → PDF 导出）
- 官方 `pdf`、`docx`、`pptx` skills（读取文件）
