"""Cover slide — title page for coursework presentations."""
from __future__ import annotations
from typing import Optional

from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

from ..base import (
    blank_slide, add_rect, add_line, add_textbox, write_paragraph,
    enable_text_shrink, add_title, add_footer,
)
from ..theme import Theme, DEFAULT_THEME


def add_cover(prs, *,
              title: str,
              subtitle: Optional[str] = None,
              course: Optional[str] = None,
              student: Optional[str] = None,
              date: Optional[str] = None,
              page_number=None,
              theme: Theme = DEFAULT_THEME):
    """First-page cover: large title, subtitle, course/student/date metadata."""
    slide = blank_slide(prs)

    pal, typo, layout = theme.palette, theme.typography, theme.layout

    # Accent stripe on right edge
    stripe_w = 0.35
    add_rect(slide, layout.slide_width_in - stripe_w, 0,
             stripe_w, layout.slide_height_in, fill=pal.primary)

    # Big title, centered vertically
    title_left = layout.margin_left_in + 0.15
    title_top = 2.2
    title_w = layout.slide_width_in - layout.margin_left_in - 1.2
    tb = add_textbox(slide, title_left, title_top, title_w, 1.8)
    write_paragraph(tb.text_frame, title,
                    size=typo.title_size + 18, bold=True,
                    color=pal.text_dark, family=typo.family, first=True)
    enable_text_shrink(tb.text_frame)

    # Subtitle
    if subtitle:
        tb = add_textbox(slide, title_left, title_top + 1.7, title_w, 0.8)
        write_paragraph(tb.text_frame, subtitle,
                        size=typo.title_size - 4,
                        color=pal.text_secondary, family=typo.family,
                        first=True)

    # Bottom line + metadata
    add_line(slide, title_left, layout.slide_height_in - 1.3,
             title_left + 6.0, layout.slide_height_in - 1.3,
             color=pal.primary, width_pt=1.0)
    meta_y = layout.slide_height_in - 1.15
    meta_lines = [v for v in [course, student, date] if v]
    for i, line in enumerate(meta_lines):
        tb = add_textbox(slide, title_left, meta_y + i * 0.32, 6.0, 0.30)
        write_paragraph(tb.text_frame, line,
                        size=typo.body_size if i > 0 else typo.body_size + 1,
                        bold=(i == 0), color=pal.text_dark,
                        family=typo.family, first=True)
    return slide
