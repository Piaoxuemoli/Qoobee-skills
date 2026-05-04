# Auto-college

一套 Claude Code / Cursor Skills，让 AI 帮你搞定大学课程作业——实验报告、水课 PPT、小论文、读书报告、课堂展示稿、终端截图、开卷考试资料整理，从材料到成品一步到位。

A collection of Claude Code / Cursor Skills that automate college coursework — lab reports, lecture slides, short papers, reading reports, presentation scripts, terminal screenshots, and open-book exam preparation — from raw materials to polished deliverables in one step.

---

## 快速配置 / Quick Start

在你的**项目根目录**下，任选一种方式安装：

### 方式一：脚本一键安装

在项目根目录下执行（需要 [Node.js](https://nodejs.org/)）：

```bash
curl -fsSL https://raw.githubusercontent.com/Piaoxuemoli/Auto-college/master/setup.js | node
```

自动检测 Claude Code / Cursor，clone 仓库、复制 skills、清理临时文件，一步完成。

### 方式二：让 Agent 帮你装

对你的 Claude Code 或 Cursor Agent 说：

```text
帮我从 https://github.com/Piaoxuemoli/Auto-college 安装 skills 到当前项目
```

Agent 会自动 clone、复制、配置。

配置完成后，直接在对话中描述任务即可：

```text
帮我根据实验手册生成实验报告
```

```text
帮我写一篇关于分布式计算的1500字小论文，IEEE格式
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

### [lab-report](docs/lab-report.md)

实验报告全流程自动化：个人信息本地复用、材料目录一键导入、自动模式、课程模板记忆、证据映射。内置标准大学实验报告模板（10 节结构），导出 DOCX 自动应用学术排版。

**设计亮点：** 个人信息复用 · 课程模板记忆 · 证据映射 · 自动模式 · 三种报告路径

Automate lab reports with reusable profile data, material-folder intake, auto mode, course template memory, and evidence maps. Standard university format (10-section) with academic styling on DOCX export.

---

### [coursework-helper](docs/coursework-helper.md)

通识课 / 选修课作业一键生成：PPT（15 个模板 + 主题系统 + Slidev 可选）、小论文、读书报告、观后感、演讲稿。内置 PPT 引擎，Markdown slide card 直接导出带 speaker notes 的 PPTX。视频链接默认 Bilibili 等国内平台。

**设计亮点：** PPT 引擎（15 模板） · 多格式输出 · 国内适配 · Slidev 可选

Generate deliverables for general education coursework: slides (15 templates + theme system + optional Slidev), short papers, reading reports, reflection essays, and speech scripts. Built-in PPT engine exports styled PPTX with speaker notes from structured Markdown.

---

### [terminal-screenshot](docs/terminal-screenshot.md)

终端命令输出渲染为逼真 PNG 截图。支持 PowerShell、macOS zsh、Linux/SSH 高保真模板。自动配置渲染工具（Playwright → Edge/Chrome headless → 降级跳过）。

**设计亮点：** 高保真渲染 · 三平台模板 · 自动配置 · 优雅降级

Render terminal command outputs as realistic PNG screenshots. High-fidelity templates for PowerShell, macOS zsh, and Linux/SSH with auto-configuring rendering tools.

![terminal-screenshot 示例 / Example](terminal-screenshot/example.png)

---

### [study-index](docs/study-index.md)

将散乱的课程材料（PPT、PDF、文档、笔记）整理成一本带目录、带索引、带关键图片的速查手册。核心原则：不丢失信息——源材料中的全部文字内容完整保留，关键图片自动筛选并放到手册对应位置。脚本拼接全部文本，AI 只负责生成大纲。

**设计亮点：** 零信息丢失 · 关键图片筛选 · 自动索引 · 脚本拼接（非 AI 编写）

Organize scattered course materials into an indexed study handbook. Core principle: no information loss — all text preserved in full, key images auto-filtered and placed correctly. Scripts compile all text; AI only writes the outline.

---

### [paper-writer](docs/paper-writer.md)

学术论文路由器：不自己实现具体能力，而是按需从 **534 个专业 skills** 中加载所需能力，调度子代理执行，最后负责格式检查和 DOCX 导出。主 agent 只做路由，子代理自发现 skills 并全权执行。

**设计亮点：** 路由器架构（主 agent 零污染） · 534 个 skills 按需加载 · 格式检查 · DOCX 导出 · 多语种支持 · 署名可选

Academic paper router: loads from 534 professional skills on demand, dispatches sub-agents, handles format checking and DOCX export. Router architecture keeps the main agent context clean.

---

![GitHub stars](https://img.shields.io/github/stars/Piaoxuemoli/Auto-college?style=social)
![GitHub Created At](https://img.shields.io/github/created-at/Piaoxuemoli/Auto-college)
