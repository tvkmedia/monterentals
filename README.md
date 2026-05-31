# MontenegroDrive

Premium car-rental site for Montenegro, with a matching Elementor-ready WordPress theme.

The repo holds two parallel deliverables built from the same source:
1. A **static HTML site** (14 pages) for fast preview and hand-off.
2. A **WordPress theme** (`montenegrodrive/`) for Elementor Pro, with all 14 pages
   bundled as importable Elementor template JSON files.

## Project layout

```
.
├── index.html                  ── 14 static HTML pages (the live site)
├── search.html
├── travel-guide.html
├── support.html
├── manage-booking.html
├── locations.html
├── monte-club.html
├── legal.html
├── article-*.html              (6 travel-guide articles)
│
├── favicon.svg                 ── shared site assets (also copied into theme)
├── logo.svg
├── robots.txt
├── sitemap.xml
│
├── montenegrodrive/            ── WordPress theme (zip + upload to wp-admin)
│   ├── style.css               theme header + design tokens
│   ├── functions.php           Elementor support, asset enqueue
│   ├── theme.json              block-editor color/font integration
│   ├── header.php, footer.php  Elementor-aware (yields to Theme Builder if active)
│   ├── *.php                   page templates
│   ├── screenshot.png          theme thumbnail
│   ├── README.md               install / Elementor import instructions
│   └── elementor-templates/    14 importable Elementor JSON files
│
├── build_pages.py              ── build scripts (see "How to rebuild" below)
├── build_seo.py
├── build_elementor_templates.py
├── _chrome.py                  shared head/header/footer for generated pages
│
└── .gitignore
```

## How to rebuild

The static HTML in this repo is the source of truth. After editing any page,
run the build pipeline to regenerate the SEO meta + Elementor templates:

```bash
python3 build_pages.py                  # regenerate generated pages from _chrome.py
python3 build_seo.py                    # inject favicon + SEO + logo into all pages
python3 build_elementor_templates.py    # convert HTML pages to Elementor JSON

# Re-package the WordPress theme:
cp favicon.svg logo.svg robots.txt sitemap.xml montenegrodrive/
zip -rq montenegrodrive.zip montenegrodrive -x "*.DS_Store" -x "*/__pycache__/*"
```

The `montenegrodrive.zip` archive is git-ignored — it's a build artifact you
regenerate from sources.

## Deploying

**Static site**: drop the root `.html` / `.svg` / `.txt` / `.xml` files onto
any static host (Netlify, Vercel, Cloudflare Pages, S3, etc.). No build needed.

**WordPress theme**: from wp-admin go to **Appearance → Themes → Add New →
Upload Theme**, pick `montenegrodrive.zip`, activate, then follow
`montenegrodrive/README.md` for Elementor template import + page setup.

## Design system

Brand: Adriatic Blue `#001835` · Vibrant Orange `#FF5722` · Sky Blue `#d3e2ed`.
Type: Plus Jakarta Sans (headings), Inter (body).

Tailwind config is mirrored in:
- `<head>` of every static HTML page
- `functions.php` → `montenegrodrive_get_tailwind_config_js()`
- `theme.json` (for block editor)

When editing colors or fonts, update all three places — or edit
`montenegrodrive/style.css` `:root` variables and use them with `var(--md-*)`.

## License

Theme code is GPL v2 or later (WordPress requirement). Bundled third-party
images / fonts / icons retain their original licenses (most are CC, SIL OFL,
Apache 2.0, MIT) — verify before commercial use.
