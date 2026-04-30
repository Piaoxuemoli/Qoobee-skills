# coursework-helper

面向大学通识课、选修课和低风险课程作业的交付物生成技能。适合快速完成 PPT、小论文、读书报告、观后感、课堂展示稿、演讲稿等任务。

Create practical deliverables for general education, elective, and low-stakes college
coursework: slides, short papers, reading reports, reflection essays, classroom presentations,
and speech scripts.

## 工作流 / Workflow

```text
入口判断 → 材料索引 → 任务规划 → 写作/PPT/演讲稿 → 润色与导出
Intake → Index materials → Plan → Draft paper/slides/script → Polish and export
```

| 路径 / Path | 适用场景 / Use case | 输出 / Output |
|-------------|---------------------|---------------|
| `slides` | 汇报 PPT、课堂展示 / presentation slides | `final_slides.md`, optional `.pptx` |
| `paper` | 小论文、课程论文、读书报告、观后感 / paper or reflection | `final_paper.md`, optional `.docx`/`.pdf` |
| `script` | 演讲稿、发言稿、课堂分享 / speech script | `final_script.md` |
| `mixed` | PPT + 小论文 + 演讲稿 / multiple deliverables | combined outputs |

PPT 默认页面大小固定为 16:9 widescreen，13.333 x 7.5 英寸（33.867 x 19.05 cm）。除非老师明确要求其他尺寸，所有 PPTX 都按这个尺寸导出并检查。

## 适用场景 / When To Use

可以直接这样说：

```text
帮我写一篇 1500 字通识课小论文，主题是人工智能与大学生学习。
```

```text
老师要求做 10 页 PPT，材料在 ./course-materials，帮我整理成课堂展示。
```

```text
这门水课要交读书报告，帮我根据这份 PDF 写得像正常学生作业一点。
```

## 材料索引 / Source Indexing

当用户给一个目录或多个文件时，skill 会生成 `source_manifest.json`：

```bash
python coursework-helper/scripts/index_source_files.py \
  --inputs "./course-materials" \
  --output "<output_dir>/source_manifest.json"
```

材料会被分类为：

- `requirement`: 作业要求、rubric、老师说明
- `reading`: 阅读材料、文章、书籍章节
- `slides`: 课堂 PPT
- `data`: 表格或数据
- `image`: 截图、图片
- `notes`: 用户笔记
- `other`: 其他文件

## 输出目录 / Output Structure

```text
coursework-helper/outputs/<assignment-name>/
├── assignment_context.json
├── source_manifest.json
├── outline.md
├── evidence_notes.md
├── final_paper.md
├── final_slides.md
├── final_script.md
├── delivery_manifest.json
└── assets/
```

## 子代理 / Agents

| Agent | 文件 / File | 职责 / Role |
|-------|-------------|-------------|
| Assignment Planner | `agents/assignment-planner.md` | 判断任务、整理要求、生成 outline 和证据计划 |
| Paper Writer | `agents/paper-writer.md` | 写小论文、读书报告、观后感、课程总结 |
| Slide Writer | `agents/slide-writer.md` | 写 PPT Markdown 和 speaker notes |
| Script Writer | `agents/script-writer.md` | 写演讲稿、发言稿、课堂分享稿 |
| Delivery Packager | `agents/delivery-packager.md` | 润色、导出 DOCX/PDF/PPTX、生成交付清单 |

## 风格原则 / Style

- 写得像正常学生作业，不要像公司白皮书。
- PPT 每页少字，解释放 speaker notes。
- 小论文要有明确结构，但避免空泛大话。
- 不伪造参考文献、页码、采访、实验或老师要求。
- 缺少材料时可以用合理默认，但要在 `delivery_manifest.json` 里提醒用户检查。

## 依赖 / Dependencies

- Anthropic official `pptx`, `docx`, `pdf`, `xlsx` skills for reading/exporting.
- Python 3 for initialization and material indexing scripts.
- Optional reuse of `lab-report/scripts/check_official_skills.py` for official skill checks.
