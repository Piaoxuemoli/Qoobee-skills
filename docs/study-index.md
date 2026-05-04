# study-index

将散乱的课程材料（PPT、PDF、文档、笔记）整理成一本带目录、带索引、带关键图片的速查手册。适用于开卷考试复习、课程笔记整理、知识收藏整理。

Organize scattered course materials (PPTs, PDFs, documents, notes) into an indexed study handbook with table of contents, key images, and keyword index. For open-book exam prep, course note organization, and knowledge curation.

## 工作流 / Workflow

```text
输入材料 → 提取文字+图片 → 过滤装饰图 → AI生成大纲 → 脚本拼接全部内容 → 输出 Markdown
Input → Extract → Filter images → AI outline → Script compiles all text → Markdown
```

核心原则：**不丢失信息**。源材料中的全部文字内容完整保留（不总结、不删减），关键图片自动筛选并放到手册对应位置。

## 适用场景 / When To Use

可以直接这样说：

```text
帮我整理这些 PPT 和文档，做成开卷考试速查手册
```

```text
这几章的课件太散了，帮我整理成一个带目录的复习资料
```

```text
把这些 PDF 和 PPT 合并成一份完整的考试复习资料
```

## 输出结构 / Output Structure

```text
study-index/outputs/<course-name>/
├── 00_admin/
│   ├── study_context.json
│   └── extract_manifest.json
├── 01_extracted/          # 按来源分目录，每页/每节一个 txt + 图片
├── 01_filtered/           # 过滤后的图片（去掉装饰图）
├── 02_outline/
│   └── outline.md         # 知识结构大纲（章节→源文件映射）
├── 04_final/
│   └── final_handbook.md  # 完整手册（全部原文 + 图片 + 索引）
└── 06_qa/
    └── qa_report.md
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

1. **目录**：按章节组织，带锚点链接
2. **各章内容**：每个源文件的**完整文字内容**（不总结），按章节归类
3. **关键图片**：从源材料自动筛选，放在对应文字位置
4. **关键词索引**：关键词 → 所在源文件

## 依赖 / Dependencies

- Python + `python-pptx`（PPTX 提取）
- Python + `PyMuPDF`（PDF 提取，`pip install pymupdf`）
- Python + `python-docx`（DOCX 提取）
- Python + `Pillow`（图片筛选）
- 官方 `pdf`、`docx`、`pptx` skills（读取文件）
