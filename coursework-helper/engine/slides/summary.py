"""Summary slides — three takeaways, closing, quote."""
from __future__ import annotations
from typing import Sequence, Optional

from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

from ..base import (
    blank_slide, add_chrome, add_rect, add_line, add_textbox,
    write_paragraph, add_oval, add_footer,
)
from ..theme import Theme, DEFAULT_THEME


def add_three_takeaways(prs, *,
                        title: str = "Summary",
                        takeaways: Sequence[str],
                        page_number=None,
                        theme: Theme = DEFAULT_THEME):
    """Three key takeaway cards with numbered circles."""
    slide = blank_slide(prs)
    add_chrome(slide, title=title, theme=theme, page_number=page_number)
    pal, typo, layout = theme.palette, theme.typography, theme.layout

    width = layout.slide_width_in - layout.margin_left_in - layout.margin_right_in
    body_top = layout.body_top_in + 0.3
    n = min(len(takeaways), 4)
    card_gap = 0.3
    card_w = (width - card_gap * (n - 1)) / n
    card_h = layout.footer_top_in - body_top - 0.5

    for i, tk in enumerate(takeaways[:4]):
        x = layout.margin_left_in + i * (card_w + card_gap)
        # Card background
        add_rect(slide, x, body_top, card_w, card_h, fill=pal.soft_gray,
                 line=pal.primary, line_width=1.0)
        # Number circle
        num_d = 0.6
        cx = x + card_w / 2 - num_d / 2
        cy = body_top + 0.3
        add_oval(slide, cx, cy, num_d, num_d, fill=pal.primary)
        tb = add_textbox(slide, cx, cy, num_d, num_d,
                         anchor=MSO_ANCHOR.MIDDLE)
        write_paragraph(tb.text_frame, str(i + 1),
                        size=typo.title_size - 4, bold=True,
                        color=pal.white, family=typo.family,
                        align=PP_ALIGN.CENTER, first=True)
        # Takeaway text
        tb = add_textbox(slide, x + 0.2, cy + num_d + 0.3,
                         card_w - 0.4, card_h - num_d - 1.0)
        write_paragraph(tb.text_frame, tk, size=typo.body_size + 1,
                        color=pal.text_dark, family=typo.family,
                        align=PP_ALIGN.CENTER, first=True)
    return slide


def add_closing(prs, *,
                title: str = "Thank You / Q&A",
                message: Optional[str] = None,
                page_number=None,
                theme: Theme = DEFAULT_THEME):
    """Closing/Q&A slide with centered text on accent background."""
    slide = blank_slide(prs)
    pal, typo, layout = theme.palette, theme.typography, theme.layout

    # Full-bleed primary color background
    add_rect(slide, 0, 0, layout.slide_width_in, layout.slide_height_in,
             fill=pal.primary)

    # Title centered
    tb = add_textbox(slide, layout.margin_left_in, 2.5,
                     layout.slide_width_in - layout.margin_left_in - layout.margin_right_in,
                     1.5, anchor=MSO_ANCHOR.MIDDLE)
    write_paragraph(tb.text_frame, title,
                    size=typo.title_size + 20, bold=True,
                    color=pal.white, family=typo.family,
                    align=PP_ALIGN.CENTER, first=True)

    if message:
        tb = add_textbox(slide, 2.0, 4.2,
                         layout.slide_width_in - 4.0, 1.0)
        write_paragraph(tb.text_frame, message,
                        size=typo.body_size + 2,
                        color=pal.white, family=typo.family,
                        align=PP_ALIGN.CENTER, first=True)
    return slide


def add_quote(prs, *,
              quote: str,
              author: str,
              title: Optional[str] = None,
              page_number=None,
              theme: Theme = DEFAULT_THEME):
    """Pull-quote slide with large quotation marks."""
    slide = blank_slide(prs)
    if title:
        add_chrome(slide, title=title, theme=theme, page_number=page_number)
        body_top = 2.0
    else:
        body_top = 1.5
    pal, typo, layout = theme.palette, theme.typography, theme.layout

    # Big opening quote mark
    tb = add_textbox(slide, 0.8, body_top, 1.5, 1.5)
    write_paragraph(tb.text_frame, "\u201C",
                    size=typo.title_size + 60, bold=True,
                    color=pal.primary, family=typo.family, first=True)

    # Quote body
    q_left = 2.0
    q_w = layout.slide_width_in - q_left - layout.margin_right_in - 0.5
    tb = add_textbox(slide, q_left, body_top + 0.4, q_w, 3.5)
    write_paragraph(tb.text_frame, quote,
                    size=typo.title_size, color=pal.text_dark,
                    family=typo.family, first=True)

    # Attribution
    attr_y = body_top + 4.0
    add_line(slide, q_left, attr_y, q_left + 0.6, attr_y,
             color=pal.primary, width_pt=2.0)
    tb = add_textbox(slide, q_left, attr_y + 0.1, q_w, 0.35)
    write_paragraph(tb.text_frame, author,
                    size=typo.body_size + 2, bold=True,
                    color=pal.text_dark, family=typo.family, first=True)
    return slide
