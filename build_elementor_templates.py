#!/usr/bin/env python3
"""
Convert the static HTML pages (index.html, search.html, travel-guide.html) into
importable Elementor template JSON files.

Each top-level <section>, <header>, or <footer> in the page becomes its own
Elementor section containing a single HTML widget. This gives the user discrete,
reorderable, individually-editable blocks in the Elementor editor while
preserving the Tailwind-styled markup pixel-perfect.

Elementor template JSON format reference:
    https://developers.elementor.com/docs/import-export/
"""

import json
import re
import secrets
from pathlib import Path
from html.parser import HTMLParser

OUT_DIR = Path("/sessions/stoic-laughing-albattani/mnt/outputs/montenegrodrive/elementor-templates")
SRC_DIR = Path("/sessions/stoic-laughing-albattani/mnt/outputs")


def eid() -> str:
    """Elementor uses 7-char hex IDs."""
    return secrets.token_hex(4)[:7]


class SectionExtractor(HTMLParser):
    """
    Pull every top-level <section>, <header>, <footer>, and <main> block out
    of the page body.

    Strategy: <main> is opportunistically *unwrapped* — if it contains direct
    <section> children, we capture each section individually. If it doesn't
    (e.g. the search-results page whose body is a single grid layout), we fall
    back to capturing the <main> element itself so its content isn't lost.
    """

    BLOCK_TAGS = {"section", "header", "footer", "main", "nav"}

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.sections = []
        self.depth = 0
        self.buf = []
        self.current_tag = None
        self.in_body = False
        self.in_head = False

        # <main> bookkeeping: we may need to fall back to capturing main itself.
        self.in_main = False
        self.main_buf = []
        self.main_section_count_at_entry = 0
        self.main_attrs = None

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.in_body = True
            return
        if tag == "head":
            self.in_head = True
            return
        if not self.in_body or self.in_head:
            return

        # Mirror everything that happens inside <main> into main_buf so we
        # can capture the whole thing as a fallback if no sections were found inside it.
        if self.in_main and self.depth == 0:
            self.main_buf.append(self._format_tag(tag, attrs, closing=False))

        if self.depth > 0:
            self.buf.append(self._format_tag(tag, attrs, closing=False))
            self.depth += 1
            return

        if tag == "main":
            self.in_main = True
            self.main_attrs = attrs
            self.main_buf = []
            self.main_section_count_at_entry = len(self.sections)
            return

        if tag in self.BLOCK_TAGS and tag != "main":
            self.current_tag = tag
            self.buf = [self._format_tag(tag, attrs, closing=False)]
            self.depth = 1

    def handle_endtag(self, tag):
        if tag == "body":
            self.in_body = False
            return
        if tag == "head":
            self.in_head = False
            return
        if not self.in_body or self.in_head:
            return

        # End of <main>: if no sections were captured while inside it, fall back
        # to treating the whole <main> contents as a single section.
        if tag == "main" and self.in_main and self.depth == 0:
            if len(self.sections) == self.main_section_count_at_entry and self.main_buf:
                main_html = (
                    self._format_tag("main", self.main_attrs or [], closing=False)
                    + "".join(self.main_buf)
                    + "</main>"
                )
                self.sections.append(("main", main_html))
            self.in_main = False
            self.main_buf = []
            self.main_attrs = None
            return

        if self.in_main and self.depth == 0:
            self.main_buf.append(f"</{tag}>")

        if self.depth == 0:
            return

        if tag != "br" and tag not in {"img", "input", "meta", "link", "hr"}:
            self.buf.append(f"</{tag}>")
            self.depth -= 1

        if self.depth == 0:
            self.sections.append((self.current_tag, "".join(self.buf)))
            self.buf = []
            self.current_tag = None

    def handle_startendtag(self, tag, attrs):
        if not self.in_body or self.in_head:
            return
        rendered = self._format_tag(tag, attrs, closing=True)
        if self.depth > 0:
            self.buf.append(rendered)
        if self.in_main and self.depth == 0:
            self.main_buf.append(rendered)

    def handle_data(self, data):
        if self.depth > 0:
            self.buf.append(data)
        if self.in_main and self.depth == 0:
            self.main_buf.append(data)

    def handle_entityref(self, name):
        if self.depth > 0:
            self.buf.append(f"&{name};")
        if self.in_main and self.depth == 0:
            self.main_buf.append(f"&{name};")

    def handle_charref(self, name):
        if self.depth > 0:
            self.buf.append(f"&#{name};")
        if self.in_main and self.depth == 0:
            self.main_buf.append(f"&#{name};")

    def handle_comment(self, data):
        if self.depth > 0:
            self.buf.append(f"<!--{data}-->")
        if self.in_main and self.depth == 0:
            self.main_buf.append(f"<!--{data}-->")

    @staticmethod
    def _format_tag(tag, attrs, *, closing):
        attr_str = "".join(
            f' {k}="{v}"' if v is not None else f" {k}"
            for k, v in attrs
        )
        if closing or tag in {"img", "input", "meta", "link", "br", "hr"}:
            # HTML5: self-closing slash is optional. Keep it for void tags so the
            # markup looks tidy in Elementor's HTML widget.
            return f"<{tag}{attr_str}/>"
        return f"<{tag}{attr_str}>"


def html_widget(html_content: str, section_label: str) -> dict:
    """Build an Elementor section -> column -> html widget tree."""
    return {
        "id": eid(),
        "elType": "section",
        "settings": {
            "structure": "10",
            "stretch_section": "section-stretched",
            "content_width": {"unit": "px", "size": 1280},
            "gap": "no",
            "padding": {"unit": "px", "top": 0, "right": 0, "bottom": 0, "left": 0, "isLinked": False},
            "_title": section_label,
        },
        "elements": [
            {
                "id": eid(),
                "elType": "column",
                "settings": {
                    "_column_size": 100,
                    "_inline_size": None,
                },
                "elements": [
                    {
                        "id": eid(),
                        "elType": "widget",
                        "widgetType": "html",
                        "settings": {
                            "html": html_content,
                            "_title": section_label,
                        },
                    }
                ],
                "isInner": False,
            }
        ],
        "isInner": False,
    }


def label_for(tag: str, idx: int, html_snippet: str) -> str:
    """Best-effort human label by scanning for headings and known markers in the HTML."""
    if tag == "header":
        return "Header / Navigation"
    if tag == "footer":
        return "Footer"

    # Try to extract a hint from class names or the first heading
    h_match = re.search(r"<h[1-3][^>]*>(.+?)</h[1-3]>", html_snippet, re.S | re.I)
    if h_match:
        text = re.sub(r"<[^>]+>", " ", h_match.group(1))
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            return text[:60]

    if "hero-gradient" in html_snippet or 'class="relative h-' in html_snippet:
        return "Hero"
    if "filter-checkbox" in html_snippet:
        return "Search Filters & Results"
    if "Trust" in html_snippet or "Verified Providers" in html_snippet:
        return "Trust Bar"
    if "Newsletter" in html_snippet:
        return "Newsletter"

    return f"Section {idx + 1}"


def page_settings_block() -> dict:
    """Page-level settings: full-width, transparent header friendly."""
    return {
        "template": "elementor_canvas",
        "background_background": "classic",
        "background_color": "#f7f9fb",
    }


def build_template(html_path: Path, title: str, doc_type: str = "page") -> dict:
    html = html_path.read_text(encoding="utf-8")

    parser = SectionExtractor()
    parser.feed(html)
    parser.close()

    if not parser.sections:
        raise RuntimeError(f"No <section>/<header>/<footer> found in {html_path}")

    content = []
    for idx, (tag, snippet) in enumerate(parser.sections):
        label = label_for(tag, idx, snippet)
        # Trim leading/trailing whitespace for cleaner HTML widget contents.
        snippet = snippet.strip()
        content.append(html_widget(snippet, label))

    return {
        "version": "0.4",
        "title": title,
        "type": doc_type,
        "content": content,
        "page_settings": page_settings_block(),
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pages = [
        ("index.html",                     "MontenegroDrive — Home",             "home.json"),
        ("search.html",                    "MontenegroDrive — Search Results",   "search-results.json"),
        ("travel-guide.html",              "MontenegroDrive — Travel Guide",     "travel-guide.json"),
        ("support.html",                   "MontenegroDrive — Support & Contact","support.json"),
        ("manage-booking.html",            "MontenegroDrive — Manage Booking",   "manage-booking.json"),
        ("locations.html",                 "MontenegroDrive — Locations",        "locations.json"),
        ("monte-club.html",                "MontenegroDrive — Monte Club",       "monte-club.json"),
        ("legal.html",                     "MontenegroDrive — Legal",            "legal.json"),
        ("article-road-trip-tips.html",    "Article — 10 Tips for Your Montenegro Road Trip", "article-road-trip-tips.json"),
        ("article-panoramic-routes.html",  "Article — Best Panoramic Routes in Europe",       "article-panoramic-routes.json"),
        ("article-driving-rules.html",     "Article — Driving in Montenegro",                 "article-driving-rules.json"),
        ("article-prokletije.html",        "Article — Prokletije: The Cursed Mountains",      "article-prokletije.json"),
        ("article-sinjajevina.html",       "Article — The Sinjajevina Highlands",             "article-sinjajevina.json"),
        ("article-komovi.html",            "Article — The Circular Komovi Route",             "article-komovi.json"),
    ]

    for src, title, dest in pages:
        src_path = SRC_DIR / src
        template = build_template(src_path, title)
        out_path = OUT_DIR / dest
        out_path.write_text(json.dumps(template, indent=2), encoding="utf-8")
        size_kb = out_path.stat().st_size / 1024
        print(f"  ✓ {dest:<24} {len(template['content']):>2} sections  {size_kb:>6.1f} KB")


if __name__ == "__main__":
    print("Generating Elementor template JSON files...")
    main()
    print("Done.")
