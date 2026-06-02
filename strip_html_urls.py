#!/usr/bin/env python3
"""
Strip the `.html` suffix from every internal link across all 14 HTML pages.

Examples:
    href="search.html"           →  href="/search"
    href="article-komovi.html"   →  href="/article-komovi"
    href="support.html#faq"      →  href="/support#faq"
    href="index.html"            →  href="/"            (home)

Leaves alone:
    href="https://…"             external URLs
    href="mailto:…"              mail links
    href="tel:…"                 phone links
    href="#anchor"               same-page anchors
    href="/path"                 already-clean paths
    src="foo.html"               (only href is rewritten)
"""

import re
from pathlib import Path

OUT = Path("/sessions/stoic-laughing-albattani/mnt/outputs")

# All the .html files that currently exist in the project root.
PAGES = {p.stem for p in OUT.glob("*.html")}   # {'index', 'search', 'travel-guide', ...}

# Match  href="<page>.html"  or  href="<page>.html#<anchor>"
# - page is alphanumeric, hyphens, no slashes or colons (so we don't catch URLs)
# - optional anchor preserved verbatim
PATTERN = re.compile(r'href="([A-Za-z0-9_\-]+)\.html(#[^"]*)?"')


def rewrite(match: re.Match) -> str:
    page    = match.group(1)
    anchor  = match.group(2) or ""

    # Only rewrite if it's a page we actually have.
    if page not in PAGES:
        return match.group(0)

    # Home page collapses to "/"; everything else becomes "/page".
    new_href = "/" if page == "index" else f"/{page}"
    return f'href="{new_href}{anchor}"'


def main():
    changed_pages = 0
    total_links = 0

    for f in sorted(OUT.glob("*.html")):
        original = f.read_text(encoding="utf-8")
        rewritten, n = PATTERN.subn(rewrite, original)
        if n:
            f.write_text(rewritten, encoding="utf-8")
            changed_pages += 1
            total_links += n
            print(f"  ✓ {f.name:<32} {n} link(s) cleaned")
        else:
            print(f"  · {f.name:<32} (no changes)")

    print(f"\n{total_links} links rewritten across {changed_pages} pages.")


if __name__ == "__main__":
    print("Stripping .html from internal links...")
    main()
    print("Done.")
