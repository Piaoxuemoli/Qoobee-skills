# HTML Templates for Terminal Screenshots

Production-ready HTML/CSS templates. Every template includes scrollbar suppression
and realistic terminal proportions (80-column width, tight line-height).

---

## Mandatory Base CSS

Every template MUST include this at the top of its `<style>` block:

```css
html, body {
  overflow: hidden;           /* never show scrollbars */
  margin: 0; padding: 0;
}
::-webkit-scrollbar { display: none; }
* { scrollbar-width: none; -ms-overflow-style: none; }
```

---

## Template A: Modern Dark Terminal with GNOME Window Frame

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8">
<style>
  html, body { overflow: hidden; margin: 0; padding: 0; }
  html { background: #2a2a2a; }
  ::-webkit-scrollbar { display: none; }
  * { scrollbar-width: none; -ms-overflow-style: none; }

  body {
    background: #2a2a2a; margin: 0; padding: 28px 20px;
    font-family: 'Consolas','Courier New','Microsoft YaHei',monospace;
  }
  .window {
    background: #1e1e1e; border-radius: 8px; overflow: hidden;
    box-shadow: 0 6px 24px rgba(0,0,0,0.5); border: 1px solid #3c3c3c;
    width: 740px; margin: 0 auto;
  }
  .titlebar {
    background: #2d2d2d; padding: 7px 14px; display: flex; align-items: center;
    border-bottom: 1px solid #3c3c3c;
  }
  .titlebar-text {
    color: #999; font-size: 11px; text-align: center; flex: 1;
    font-family: -apple-system,'Segoe UI','Microsoft YaHei',sans-serif;
  }
  .body {
    padding: 14px 18px; font-size: 14px; line-height: 1.4;
    white-space: pre-wrap; color: #d4d4d4;
  }
  .prompt { color: #569cd6; }
  .cmd { color: #d4d4d4; }
  .output { color: #cccccc; }
  .stderr { color: #f44747; }
  .highlight { color: #569cd6; font-weight: bold; }
</style></head>
<body>
<div class="window">
  <div class="titlebar">
    <span class="titlebar-text">a2023080901018@server:~</span>
  </div>
  <div class="body">
    <!-- CONTENT HERE -->
  </div>
</div>
</body></html>
```

---

## Template B: macOS Terminal Pro

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8">
<style>
  html, body { overflow: hidden; margin: 0; padding: 0; }
  html { background: #2a2a2a; }
  ::-webkit-scrollbar { display: none; }
  * { scrollbar-width: none; -ms-overflow-style: none; }

  body {
    background: #2a2a2a; margin: 0; padding: 28px 20px;
    font-family: 'Consolas','Courier New','Microsoft YaHei',monospace;
  }
  .window {
    background: #1e1e1e; border-radius: 8px; overflow: hidden;
    box-shadow: 0 6px 24px rgba(0,0,0,0.5);
    width: 740px; margin: 0 auto;
  }
  .titlebar {
    background: #323233; padding: 9px 14px; display: flex; align-items: center;
    gap: 8px;
  }
  .dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
  .dot.red    { background: #ff5f57; }
  .dot.yellow { background: #febc2e; }
  .dot.green  { background: #28c840; }
  .titlebar-text {
    flex: 1; text-align: center; color: #999; font-size: 11px;
    font-family: -apple-system,'SF Pro Text','Microsoft YaHei',sans-serif;
  }
  .body {
    padding: 14px 18px; font-size: 14px; line-height: 1.4;
    white-space: pre-wrap; color: #d4d4d4;
  }
  .prompt { color: #569cd6; }
  .cmd { color: #d4d4d4; }
  .output { color: #cccccc; }
  .stderr { color: #f44747; }
  .highlight { color: #569cd6; font-weight: bold; }
</style></head>
<body>
<div class="window">
  <div class="titlebar">
    <span class="dot red"></span>
    <span class="dot yellow"></span>
    <span class="dot green"></span>
    <span class="titlebar-text">username — -zsh — 80x24</span>
  </div>
  <div class="body">
    <!-- CONTENT HERE -->
  </div>
</div>
</body></html>
```

---

## Template C: Windows Terminal (optimized)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8">
<style>
  html, body { overflow: hidden; margin: 0; padding: 0; }
  html { background: #2a2a2a; }
  ::-webkit-scrollbar { display: none; }
  * { scrollbar-width: none; -ms-overflow-style: none; }

  body {
    background: #2a2a2a; margin: 0; padding: 28px 20px;
    font-family: 'Consolas','Courier New','Microsoft YaHei',monospace;
  }
  .window {
    background: #0c0c0c; border-radius: 8px; overflow: hidden;
    box-shadow: 0 6px 24px rgba(0,0,0,0.55);
    border: 1px solid #3c3c3c;
    width: 740px; margin: 0 auto;
  }
  .titlebar {
    background: #202020; display: flex; align-items: stretch;
    border-bottom: 1px solid #3c3c3c; height: 32px;
  }
  .tabs-area { display: flex; align-items: stretch; flex: 1; }
  .tab {
    background: #0c0c0c; color: #cccccc; padding: 0 14px; font-size: 12px;
    display: flex; align-items: center; border-right: 1px solid #3c3c3c;
    border-bottom: 1px solid #0c0c0c; gap: 6px;
    font-family: 'Segoe UI',-apple-system,'Microsoft YaHei',sans-serif;
  }
  .tab-active-line { background: #16c60c; height: 2px; align-self: flex-end; }
  .caption-buttons { display: flex; align-items: stretch; flex-shrink: 0; }
  .caption-btn {
    width: 46px; display: flex; align-items: center; justify-content: center;
    color: #888; font-size: 10px; font-family: 'Segoe UI',sans-serif;
  }
  .body {
    padding: 14px 18px; font-size: 14px; line-height: 1.4;
    white-space: pre-wrap; background: #0c0c0c; color: #cccccc;
  }
  .prompt { color: #569cd6; }
  .cmd { color: #cccccc; }
  .output { color: #aaaaaa; }
  .stderr { color: #f44747; }
  .highlight { color: #569cd6; font-weight: bold; }
</style></head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="tabs-area">
      <div class="tab">
        <span>&gt;_</span><span>PowerShell</span>
      </div>
    </div>
    <div class="caption-buttons">
      <span class="caption-btn">&#x2014;</span>
      <span class="caption-btn">&#x25A1;</span>
      <span class="caption-btn">&#x2715;</span>
    </div>
  </div>
  <div class="body">
    <!-- CONTENT HERE -->
  </div>
</div>
</body></html>
```

---

## Template D: Green Phosphor CRT with Monitor Bezel

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8">
<style>
  html, body { overflow: hidden; margin: 0; padding: 0; }
  html { background: #2a2a2a; }
  ::-webkit-scrollbar { display: none; }
  * { scrollbar-width: none; -ms-overflow-style: none; }

  body {
    background: #2a2a2a; margin: 0; padding: 28px 20px;
    font-family: 'Consolas','Courier New','Microsoft YaHei',monospace;
  }
  .monitor {
    background: #3a3a3a; padding: 22px 22px 32px 22px; border-radius: 10px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.5); display: inline-block;
  }
  .screen {
    background: #0a0a0a; padding: 18px 22px; border-radius: 6px;
    position: relative; overflow: hidden;
  }
  .screen::before {
    content: '';
    position: absolute; top:0; left:0; right:0; bottom:0;
    background: repeating-linear-gradient(
      0deg,
      rgba(0,0,0,0.12) 0px, rgba(0,0,0,0.12) 1px,
      transparent 1px, transparent 3px
    );
    pointer-events: none; z-index: 1;
  }
  .screen::after {
    content: '';
    position: absolute; top:0; left:0; right:0; bottom:0;
    background: radial-gradient(ellipse at center, transparent 55%, rgba(0,0,0,0.5) 100%);
    pointer-events: none; z-index: 2;
  }
  .content {
    position: relative; z-index: 0; font-size: 14px; line-height: 1.4;
    white-space: pre-wrap; color: #33ff33;
    text-shadow: 0 0 2px rgba(51,255,51,0.5), 0 0 6px rgba(51,255,51,0.15);
  }
  .monitor-label {
    text-align: center; color: #888; font-size: 9px; margin-top: 10px;
    letter-spacing: 2px;
    font-family: -apple-system,'Segoe UI','Microsoft YaHei',sans-serif;
  }
  .content .prompt { color: #33ff33; }
  .content .cmd { color: #66ff66; }
  .content .output { color: #33ff33; }
  .content .stderr { color: #ff5555; }
</style></head>
<body>
<div class="monitor">
  <div class="screen">
    <div class="content">
      <!-- CONTENT HERE -->
    </div>
  </div>
  <div class="monitor-label">IBM 3270 TERMINAL</div>
</div>
</body></html>
```

---

## Template E: Amber Phosphor CRT

Same structure as Template D with amber colors:

```css
.content { color: #ffb000;
  text-shadow: 0 0 2px rgba(255,176,0,0.5), 0 0 6px rgba(255,176,0,0.15); }
.content .prompt { color: #ffb000; }
.content .cmd { color: #ffcc33; }
.content .output { color: #ffb000; }
.content .stderr { color: #ff4444; }
```

Monitor label: `DEC VT220`

---

## Template F: No Window Frame (inline snippet)

For small outputs (<40 lines) — no window chrome, just the terminal content.

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8">
<style>
  html, body { overflow: hidden; margin: 0; padding: 0; }
  html { background: #2a2a2a; }
  ::-webkit-scrollbar { display: none; }
  * { scrollbar-width: none; -ms-overflow-style: none; }

  body {
    background: #2a2a2a; margin: 0; padding: 28px 20px;
    font-family: 'Consolas','Courier New','Microsoft YaHei',monospace;
  }
  .terminal {
    background: #1e1e1e; color: #d4d4d4; padding: 16px 20px; border-radius: 6px;
    font-size: 14px; line-height: 1.4; white-space: pre-wrap;
    display: inline-block;
  }
  .prompt { color: #569cd6; }
  .cmd { color: #d4d4d4; }
  .output { color: #cccccc; }
  .stderr { color: #f44747; }
  .highlight { color: #569cd6; font-weight: bold; }
</style></head>
<body>
<div class="terminal">
<!-- CONTENT HERE -->
</div>
</body></html>
```

---

## Content Formatting

| Class | Usage | Example |
|-------|-------|---------|
| `.prompt` | Shell prompt (`$`, `>`, `#`) | `<span class="prompt">$ </span>` |
| `.cmd` | User-typed command | `<span class="cmd">nvprof ./a.out</span>` |
| `.output` | Standard output | `<span class="output">PASSED</span>` |
| `.stderr` | Error/warning output | `<span class="stderr">warning: ...</span>` |
| `.highlight` | Titles, key values | `<span class="highlight">=== Step 1 ===</span>` |

For multi-command sessions, separate blocks with a blank line in the pre-formatted text.
For ASCII tables (nvidia-smi, nvprof), wrap the entire table in `.output`, preserving
exact whitespace and monospace alignment.

---

## Window Frame Decision

```
if line_count > 40 or has_multiple_commands:
    use Frame (Template A/B/C/D)
else:
    use No Frame (Template F)
```
