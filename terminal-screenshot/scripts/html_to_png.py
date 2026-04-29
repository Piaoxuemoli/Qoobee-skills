#!/usr/bin/env python3
"""
Convert terminal HTML to PNG screenshot.

Auto-configures rendering tools: tries to install Playwright first (best quality),
retrying up to 3 times. Falls back to existing system tools if auto-config fails.
If nothing works, exits with code 2 so the caller can skip screenshots gracefully.

Usage:
    python html_to_png.py <input.html> [output.png] [--width W]

Exit codes:
    0 — screenshot generated successfully
    1 — input error (HTML not found, etc.)
    2 — no tool available, skip screenshot and continue
"""

import sys
import os
import subprocess
import shutil
import tempfile
import time


MAX_RETRIES = 3


def count_lines(html_path):
    """Count visible content lines inside the terminal body div only."""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            text = f.read()
        import re
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        m = re.search(r'<div class="(?:body|terminal|content)"[^>]*>(.*?)</div>\s*(?:</div>\s*)?</div>\s*</body>', text, flags=re.DOTALL)
        if not m:
            m = re.search(r'<div class="body"[^>]*>(.*?)</div>', text, flags=re.DOTALL)
        if m:
            body_text = m.group(1)
        else:
            body_text = text
        body_text = re.sub(r'<[^>]+>', '', body_text)
        body_text = body_text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
        lines = body_text.split('\n')
        return max(len(lines), 5)
    except Exception:
        return 40


def estimate_height(line_count):
    """Estimate needed viewport height from content lines."""
    content_px = line_count * 20
    chrome_px = 116
    return int(content_px + chrome_px)


# ---------------------------------------------------------------------------
# Auto-configuration: install Playwright
# ---------------------------------------------------------------------------

def _try_pip_install():
    """Try pip install playwright. Returns True on success."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "playwright"],
        capture_output=True, text=True, timeout=120
    )
    return result.returncode == 0


def _try_playwright_install_chromium():
    """Try playwright install chromium. Returns True on success."""
    result = subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        capture_output=True, text=True, timeout=300
    )
    return result.returncode == 0


def auto_configure_playwright():
    """
    Attempt to install Playwright + Chromium, retrying up to MAX_RETRIES times.
    Returns True if Playwright is usable after configuration.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"[auto-config] Attempt {attempt}/{MAX_RETRIES}: installing playwright...")

        if not _try_pip_install():
            print(f"[auto-config] pip install failed (attempt {attempt})", file=sys.stderr)
            if attempt < MAX_RETRIES:
                print("[auto-config] Retrying in 2 seconds...")
                time.sleep(2)
            continue

        if not _try_playwright_install_chromium():
            print(f"[auto-config] playwright install chromium failed (attempt {attempt})", file=sys.stderr)
            if attempt < MAX_RETRIES:
                print("[auto-config] Retrying in 2 seconds...")
                time.sleep(2)
            continue

        # Both installs succeeded — verify import works
        try:
            from playwright.sync_api import sync_playwright
            print("[auto-config] Playwright installed and ready.")
            return True
        except ImportError:
            print(f"[auto-config] Import failed after install (attempt {attempt})", file=sys.stderr)
            if attempt < MAX_RETRIES:
                time.sleep(2)

    return False


# ---------------------------------------------------------------------------
# Fallback: detect existing system tools
# ---------------------------------------------------------------------------

def detect_fallback_tools():
    """
    Detect available screenshot tools from the local system.
    Returns (tool_name, details) or (None, {}).
    Checks in order: Playwright (already installed), Edge headless, Chrome headless, wkhtmltoimage.
    """
    # 1. Playwright Python (may have been manually installed)
    try:
        from playwright.sync_api import sync_playwright
        return "playwright-python", {"sync_playwright": sync_playwright}
    except ImportError:
        pass

    # 2. Playwright via npx
    if shutil.which("npx"):
        try:
            result = subprocess.run(
                ["npx", "playwright", "--version"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                return "playwright-npx", {}
        except Exception:
            pass

    # 3. Puppeteer
    if shutil.which("node"):
        try:
            result = subprocess.run(
                ["node", "-e", "require('puppeteer')"],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                return "puppeteer", {}
        except Exception:
            pass

    # 4. Edge headless (Windows)
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    for edge_path in edge_paths:
        if os.path.exists(edge_path):
            return "edge-headless", {"path": edge_path}

    # 5. Chrome/Chromium headless
    for chrome_name in ["google-chrome", "chromium", "chromium-browser", "chrome"]:
        chrome_path = shutil.which(chrome_name)
        if chrome_path:
            return "chrome-headless", {"path": chrome_path}

    # 6. wkhtmltoimage
    wk_path = shutil.which("wkhtmltoimage")
    if wk_path:
        return "wkhtmltoimage", {"path": wk_path}

    return None, {}


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def render_playwright_python(html_path, png_path, width):
    """Render using Playwright Python API — clips to exact content height."""
    from playwright.sync_api import sync_playwright

    abs_html = "file:///" + os.path.abspath(html_path).replace("\\", "/")

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(channel="msedge", headless=True)
        except Exception:
            try:
                browser = p.chromium.launch(headless=True)
            except Exception:
                browser = p.chromium.launch(channel="chrome", headless=True)

        page = browser.new_page(viewport={"width": width, "height": 4800})
        page.goto(abs_html, wait_until="networkidle")
        page.wait_for_timeout(300)

        body = page.query_selector("body")
        if body:
            box = body.bounding_box()
            if box:
                clip = {
                    "x": max(0, box["x"] - 4),
                    "y": max(0, box["y"] - 4),
                    "width": box["width"] + 8,
                    "height": box["height"] + 8,
                }
                page.screenshot(path=png_path, clip=clip)
            else:
                page.screenshot(path=png_path, full_page=True)
        else:
            page.screenshot(path=png_path, full_page=True)

        browser.close()
    return True


def render_edge_headless(html_path, png_path, width, edge_path):
    """Render using Edge headless — no npm/python deps needed."""
    abs_html = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    abs_png = os.path.abspath(png_path)

    line_count = count_lines(html_path)
    height = int(estimate_height(line_count))

    result = subprocess.run(
        [
            edge_path, "--headless", "--disable-gpu",
            "--no-pdf-header-footer",
            f"--screenshot={abs_png}",
            f"--window-size={width},{height}",
            abs_html
        ],
        capture_output=True, text=True, timeout=60
    )

    if os.path.exists(abs_png):
        return True

    alt_name = os.path.basename(abs_png)
    if os.path.exists(alt_name):
        shutil.move(alt_name, abs_png)
        return True

    print(f"Edge stderr: {result.stderr}", file=sys.stderr)
    return False


def render_chrome_headless(html_path, png_path, width, chrome_path):
    """Render using Chrome/Chromium headless."""
    abs_html = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    abs_png = os.path.abspath(png_path)

    line_count = count_lines(html_path)
    height = int(estimate_height(line_count))

    subprocess.run(
        [
            chrome_path, "--headless", "--disable-gpu",
            f"--screenshot={abs_png}",
            f"--window-size={width},{height}",
            abs_html
        ],
        capture_output=True, text=True, timeout=60
    )
    return os.path.exists(abs_png)


def render_wkhtmltoimage(html_path, png_path, width):
    """Render using wkhtmltoimage."""
    abs_html = os.path.abspath(html_path)
    abs_png = os.path.abspath(png_path)

    subprocess.run(
        [
            "wkhtmltoimage",
            "--width", str(width),
            "--quality", "100",
            "--encoding", "UTF-8",
            abs_html, abs_png
        ],
        capture_output=True, text=True, timeout=60
    )
    return os.path.exists(abs_png)


def render_playwright_npx(html_path, png_path, width):
    """Render using npx playwright (Node.js)."""
    abs_html = os.path.abspath(html_path).replace("\\", "/")
    abs_png = os.path.abspath(png_path).replace("\\", "/")

    script = f"""
    const {{ chromium }} = require('playwright');
    (async () => {{
        const browser = await chromium.launch({{ headless: true }});
        const page = await browser.newPage({{ viewport: {{ width: {width}, height: 4800 }} }});
        await page.goto('file:///{abs_html}');
        await page.waitForTimeout(500);
        const body = await page.$('body');
        if (body) {{
            const box = await body.boundingBox();
            await page.screenshot({{
                path: '{abs_png}',
                clip: {{ x: Math.max(0, box.x - 4), y: Math.max(0, box.y - 4),
                         width: box.width + 8, height: box.height + 8 }}
            }});
        }} else {{
            await page.screenshot({{ path: '{abs_png}', fullPage: true }});
        }}
        await browser.close();
    }})();
    """

    with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write(script)
        script_path = f.name

    try:
        result = subprocess.run(
            ["node", script_path],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            print(f"Node stderr: {result.stderr}", file=sys.stderr)
        return os.path.exists(abs_png)
    finally:
        os.unlink(script_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    html_path = sys.argv[1]
    png_path = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(html_path)[0] + ".png"
    width = 800

    if not os.path.exists(html_path):
        print(f"ERROR: HTML file not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    # ---- Phase 1: Auto-configure Playwright (best quality) ----
    print("[auto-config] Attempting to install Playwright (best quality tool)...")
    configured = auto_configure_playwright()

    if configured:
        # Use the freshly installed Playwright
        try:
            from playwright.sync_api import sync_playwright
            success = render_playwright_python(html_path, png_path, width)
        except Exception as e:
            print(f"ERROR with auto-configured Playwright: {e}", file=sys.stderr)
            success = False

        if success and os.path.exists(png_path):
            size_kb = os.path.getsize(png_path) / 1024
            print(f"OK: {png_path} ({size_kb:.0f} KB)")
            sys.exit(0)
        else:
            print("[auto-config] Playwright install succeeded but render failed."
                  " Trying fallback...", file=sys.stderr)

    # ---- Phase 2: Fallback to existing system tools ----
    print("[fallback] Detecting existing system tools...")
    tool, details = detect_fallback_tools()

    if tool is None:
        # ---- Phase 3: Nothing works — skip screenshot ----
        print(
            "SKIP: No screenshot tool available.\n"
            "Auto-configuration (playwright install) failed after 3 attempts.\n"
            "No existing system tools (Edge, Chrome, wkhtmltoimage) found.\n"
            "Continuing without screenshot — no user action required.",
            file=sys.stderr
        )
        sys.exit(2)

    print(f"[fallback] Using existing tool: {tool}")

    success = False
    try:
        if tool == "playwright-python":
            success = render_playwright_python(html_path, png_path, width)
        elif tool == "playwright-npx":
            success = render_playwright_npx(html_path, png_path, width)
        elif tool == "puppeteer":
            success = render_playwright_npx(html_path, png_path, width)
        elif tool == "edge-headless":
            success = render_edge_headless(html_path, png_path, width, details["path"])
        elif tool == "chrome-headless":
            success = render_chrome_headless(html_path, png_path, width, details["path"])
        elif tool == "wkhtmltoimage":
            success = render_wkhtmltoimage(html_path, png_path, width)
    except Exception as e:
        print(f"ERROR with {tool}: {e}", file=sys.stderr)

    if success and os.path.exists(png_path):
        size_kb = os.path.getsize(png_path) / 1024
        print(f"OK: {png_path} ({size_kb:.0f} KB)")
        sys.exit(0)
    else:
        # Fallback render also failed — skip
        print(
            "SKIP: All tools failed to render screenshot.\n"
            "Continuing without screenshot — no user action required.",
            file=sys.stderr
        )
        sys.exit(2)


if __name__ == "__main__":
    main()
