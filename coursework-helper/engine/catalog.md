# Coursework Slide Template Catalog

This catalog documents every template the coursework PPT engine can produce.
The delivery-packager and slide-writer use this to decide which template fits
a given slide card.

All templates accept these common optional kwargs:
`title`, `page_number`, `theme`.

---

## 1. Cover (`cover`)

**Use when:** First slide of the deck — title page with course, student, date.
**Don't use when:** Section dividers or content slides.
**Required inputs:**
- `title: str` — presentation title
**Optional inputs:**
- `subtitle: str`, `course: str`, `student: str`, `date: str`
**Example:**
```python
b.add("cover", title="人工智能导论", subtitle="课堂展示",
      course="CS101", student="张三", date="2026-05-02")
```

---

## 2. Bullet List (`bullet_list`)

**Use when:** Main content slide with 3-5 bullet points explaining one idea.
**Don't use when:** You have two distinct columns (use `two_column`) or a question (use `question`).
**Required inputs:**
- `title: str`
- `bullets: list[str]`
**Optional inputs:**
- `key_message: str` — highlighted summary line above bullets
**Example:**
```python
b.add("bullet_list", title="核心概念",
      bullets=["概念1: 定义", "概念2: 特点", "概念3: 应用"],
      key_message="三个核心概念构成理论基础")
```

---

## 3. Two Column (`two_column`)

**Use when:** Comparing two aspects of the same topic side by side.
**Don't use when:** Pros/cons with emotional valence (use `pros_cons`).
**Required inputs:**
- `title: str`
- `left_title: str`, `left_bullets: list[str]`
- `right_title: str`, `right_bullets: list[str]`
**Example:**
```python
b.add("two_column", title="理论对比",
      left_title="行为主义", left_bullets=["刺激-反应", "环境决定"],
      right_title="认知主义", right_bullets=["信息加工", "内在结构"])
```

---

## 4. Question (`question`)

**Use when:** Opening hook — a provocative question to engage the audience.
**Don't use when:** Content slides or conclusions.
**Required inputs:**
- `question: str`
**Optional inputs:**
- `subtitle: str`
**Example:**
```python
b.add("question", question="AI会取代人类吗？",
      subtitle="从技术与伦理角度探讨")
```

---

## 5. Section Divider (`section_divider`)

**Use when:** Transition between major sections of the deck.
**Required inputs:**
- `section_number: str` — e.g., "01", "Part I"
- `section_title: str`
**Optional inputs:**
- `subtitle: str`
**Example:**
```python
b.add("section_divider", section_number="02",
      section_title="技术原理", subtitle="深度学习基础")
```

---

## 6. Stat Hero (`stat_hero`)

**Use when:** Highlighting one big number or data point.
**Required inputs:**
- `stat: str` — the big number (e.g., "97%", "10亿")
- `stat_label: str` — what the number means
**Optional inputs:**
- `title: str`, `context: str`
**Example:**
```python
b.add("stat_hero", stat="97%", stat_label="模型准确率",
      context="在标准测试集上的表现")
```

---

## 7. Pros/Cons (`pros_cons`)

**Use when:** Presenting advantages and disadvantages.
**Required inputs:**
- `title: str`
- `pros: list[str]`, `cons: list[str]`
**Optional inputs:**
- `pros_label: str`, `cons_label: str`
**Example:**
```python
b.add("pros_cons", title="深度学习的优劣",
      pros=["自动特征提取", "高精度"],
      cons=["需要大量数据", "黑箱不可解释"])
```

---

## 8. Before/After (`before_after`)

**Use when:** Showing transformation or comparison of two states.
**Required inputs:**
- `title: str`
- `left_items: list[str]`, `right_items: list[str]`
**Optional inputs:**
- `left_label: str` (default "Before"), `right_label: str` (default "After")
**Example:**
```python
b.add("before_after", title="技术演进",
      left_label="传统方法", left_items=["手工特征", "规则驱动"],
      right_label="现代方法", right_items=["自动学习", "数据驱动"])
```

---

## 9. Process Flow (`process_flow`)

**Use when:** Showing a sequence of steps or workflow.
**Required inputs:**
- `title: str`
- `steps: list[str]` — 3-5 steps
**Example:**
```python
b.add("process_flow", title="研究方法",
      steps=["文献调研", "数据收集", "模型训练", "结果分析"])
```

---

## 10. Phases (`phases`)

**Use when:** Timeline with 3 phases, each with deliverables.
**Required inputs:**
- `title: str`
- `phases: list[{"label", "timeframe", "deliverables"}]`
**Example:**
```python
b.add("phases", title="项目进度",
      phases=[{"label": "准备", "timeframe": "第1-2周", "deliverables": ["开题报告"]},
              {"label": "实施", "timeframe": "第3-8周", "deliverables": ["实验数据"]},
              {"label": "总结", "timeframe": "第9-10周", "deliverables": ["论文"]}])
```

---

## 11. Three Takeaways (`three_takeaways`)

**Use when:** Final summary with 2-4 key points.
**Required inputs:**
- `takeaways: list[str]` — 2-4 items
**Optional inputs:**
- `title: str` (default "Summary")
**Example:**
```python
b.add("three_takeaways", title="核心结论",
      takeaways=["AI正在改变教育", "伦理问题不可忽视", "人机协作是未来方向"])
```

---

## 12. Closing (`closing`)

**Use when:** Last slide — thank you / Q&A.
**Optional inputs:**
- `title: str` (default "Thank You / Q&A")
- `message: str`
**Example:**
```python
b.add("closing", title="谢谢！", message="欢迎提问")
```

---

## 13. Quote (`quote`)

**Use when:** Presenting a notable quote from a source.
**Required inputs:**
- `quote: str`, `author: str`
**Optional inputs:**
- `title: str`
**Example:**
```python
b.add("quote", quote="科技是第一生产力", author="邓小平")
```

---

## 14. Diagram (`diagram`)

**Use when:** Visual framework with 2-6 components in a grid.
**Required inputs:**
- `title: str`
- `items: list[str]` — 2-6 items
**Example:**
```python
b.add("diagram", title="系统架构",
      items=["数据层", "模型层", "应用层", "用户层"])
```

---

## 15. Table (`table`)

**Use when:** Data comparison in tabular format.
**Required inputs:**
- `title: str`
- `headers: list[str]`, `rows: list[list[str]]`
**Example:**
```python
b.add("table", title="模型对比",
      headers=["模型", "准确率", "速度"],
      rows=[["BERT", "95%", "慢"], ["GPT", "97%", "中"]])
```

---

## Choosing Between Templates

| You have... | Use |
|-------------|-----|
| Title page | `cover` |
| One idea, several bullets | `bullet_list` |
| Two sides to compare | `two_column` |
| Pros and cons | `pros_cons` |
| Before and after | `before_after` |
| Steps in a process | `process_flow` |
| Timeline with phases | `phases` |
| One big number | `stat_hero` |
| A provocative question | `question` |
| A framework/model | `diagram` |
| Tabular data | `table` |
| Notable quote | `quote` |
| Section transition | `section_divider` |
| Final summary | `three_takeaways` |
| End/Q&A | `closing` |
