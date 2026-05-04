# Auto-college

一套 Claude Code / Cursor Skills，让 AI 帮你搞定大学课程作业——实验报告、水课 PPT、小论文、读书报告、课堂展示稿、终端截图、开卷考试资料整理，从材料到成品一步到位。

A collection of Claude Code / Cursor Skills that automate college coursework — lab reports, lecture slides, short papers, reading reports, presentation scripts, terminal screenshots, and open-book exam preparation — from raw materials to polished deliverables in one step.

---

## 快速配置 / Quick Start

在你的**项目根目录**下执行以下命令，将 skills 安装到当前项目：

| 环境 | 安装路径 |
|------|---------|
| Claude Code | `<项目根目录>/.claude/skills/` |
| Cursor | `<项目根目录>/.cursor/skills/` |

### Claude Code

```bash
# 在你的项目根目录下执行
git clone https://github.com/Piaoxuemoli/Auto-college.git /tmp/auto-college
mkdir -p .claude/skills
cp -r /tmp/auto-college/coursework-helper /tmp/auto-college/lab-report /tmp/auto-college/terminal-screenshot /tmp/auto-college/study-index .claude/skills/
rm -rf /tmp/auto-college
```

### Cursor

```bash
# 在你的项目根目录下执行
git clone https://github.com/Piaoxuemoli/Auto-college.git /tmp/auto-college
mkdir -p .cursor/skills
cp -r /tmp/auto-college/coursework-helper /tmp/auto-college/lab-report /tmp/auto-college/terminal-screenshot /tmp/auto-college/study-index .cursor/skills/
rm -rf /tmp/auto-college
```

配置完成后，直接在对话中描述任务即可：

```text
帮我根据实验手册生成实验报告
```

```text
帮我把这门通识课作业整理成 PPT 和小论文
```

```text
把这段 PowerShell 输出渲染成终端截图
```

```text
帮我整理这些 PPT 和文档，做成开卷考试速查手册
```

Agent 会自动匹配对应 skill。也可以明确指定：

```text
使用 terminal-screenshot skill，把这段终端输出做成 PNG
```

---

## Skills

### lab-report

实验报告全流程自动化：个人信息本地复用、材料目录一键导入、自动模式、课程模板记忆、证据映射。内置标准大学实验报告模板（10 节结构），导出 DOCX 自动应用学术排版。

Automate lab reports with reusable profile data, material-folder intake, auto mode, course template memory, and evidence maps. Standard university format (10-section) with academic styling on DOCX export.

### coursework-helper

通识课 / 选修课作业一键生成：PPT（15 个模板 + 主题系统 + Slidev 可选）、小论文、读书报告、观后感、演讲稿。内置 PPT 引擎，Markdown slide card 直接导出带 speaker notes 的 PPTX。视频链接默认 Bilibili 等国内平台。

Generate deliverables for general education coursework: slides (15 templates + theme system + optional Slidev), short papers, reading reports, reflection essays, and speech scripts. Built-in PPT engine exports styled PPTX with speaker notes from structured Markdown.

### terminal-screenshot

终端命令输出渲染为逼真 PNG 截图。支持 PowerShell、macOS zsh、Linux/SSH 高保真模板。

Render terminal command outputs as realistic PNG screenshots. High-fidelity templates for PowerShell, macOS zsh, and Linux/SSH.

![terminal-screenshot 示例 / Example](terminal-screenshot/example.png)

### study-index — [详细文档](docs/study-index.md)

将散乱的课程材料（PPT、PDF、文档、笔记）整理成一本带目录、带索引、带关键图片的速查手册。核心原则：不丢失信息——源材料中的全部文字内容完整保留，关键图片自动筛选并放到手册对应位置。输出 Markdown。

Organize scattered course materials (PPTs, PDFs, documents, notes) into an indexed study handbook with table of contents, key images, and keyword index. Core principle: no information loss — all text content is preserved in full, key images are auto-filtered and placed at the correct position. Outputs Markdown.

---

![GitHub stars](https://img.shields.io/github/stars/Piaoxuemoli/Auto-college?style=social)
![GitHub Created At](https://img.shields.io/github/created-at/Piaoxuemoli/Auto-college)
