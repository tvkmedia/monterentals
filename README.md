# MontenegroDrive (monterentals)

Premium car-rental site for Montenegro — 14 static HTML pages, Tailwind for styling, bundled with **Vite** for production builds. Deploys cleanly to Hostinger Build & Deploy (or Netlify / Vercel / Cloudflare Pages / any static host).

## Project layout

```
.
├── index.html              ← Home
├── search.html             ← Search results
├── travel-guide.html       ← Travel guide
├── locations.html          ← Cities, parks, what to do
├── support.html            ← Support & contact
├── manage-booking.html     ← Sign-in + booking dashboard
├── monte-club.html         ← Partner programme
├── legal.html              ← Privacy / Terms / Cookies
├── article-*.html          ← 6 travel-guide articles
│
├── public/                 ← Static assets copied as-is
│   ├── favicon.svg
│   ├── logo.svg
│   ├── robots.txt
│   └── sitemap.xml
│
├── package.json            ← npm scripts + Vite dependency
├── vite.config.js          ← multi-page build config
│
├── build_pages.py          ← (optional) Python source-of-truth for some pages
├── build_seo.py            ← injects SEO meta tags + favicon links
├── _chrome.py              ← shared head/header/footer for generated pages
│
└── .gitignore
```

## Quick start

```bash
# Install (Node 18+)
npm install

# Local dev server with hot reload (http://localhost:5173)
npm run dev

# Production build → dist/
npm run build

# Preview the production build
npm run preview
```

## Deploy to Hostinger

### Option A: Build & Deploy from Git (recommended)

1. In Hostinger hPanel → **Hosting → Websites → Manage** → **Deployments** (or **Build & Deploy**).
2. Connect your GitHub account, select the `tvkmedia/monterentals` repo, branch `main`.
3. Hostinger detects the Vite framework automatically from `package.json`. Verify the settings:
   - **Build command:** `npm run build`
   - **Output directory:** `dist`
   - **Node version:** 18 or 20
4. Click **Deploy**. Every `git push` to `main` triggers a new build.

### Option B: Upload built files via File Manager

```bash
npm run build
# Now zip the dist/ folder contents (NOT the folder itself):
cd dist && zip -r ../site.zip . && cd ..
```

In hPanel → **File Manager** → `public_html` → drag in `site.zip` → right-click → Extract.

### Option C: Other static hosts

Netlify, Vercel, Cloudflare Pages all auto-detect Vite. Connect the repo, accept defaults, deploy.

## How edits work

You edit `.html` files directly — there's no JSX, no components, no build step beyond what Vite bundles. Tailwind is loaded via CDN, so utility classes work instantly without compilation. If you want to optimize for production, you can later swap the CDN for a compiled Tailwind stylesheet (see "Optional: switch from Tailwind CDN to compiled" below).

For pages that share a head/header/footer (support, manage-booking, locations, monte-club, legal, article-*), they were originally generated from `_chrome.py` + `build_pages.py`. To regenerate after editing the shared chrome:

```bash
npm run pages        # rebuilds the generated pages
npm run seo          # re-injects SEO meta tags + favicon
npm run build        # vite build
```

The static index.html, search.html, and travel-guide.html were hand-written — edit them directly.

## SEO

All 14 pages have:
- Per-page `<title>` + `<meta name="description">`
- Open Graph + Twitter Card tags
- `<link rel="canonical">` pointing to `https://montenegrodrive.com/<slug>/` (placeholder — update in `build_seo.py` constant once you have a real domain)
- `robots` meta = `index, follow, max-image-preview:large`
- Theme-color for mobile browser chrome
- JSON-LD structured data on the home page (AutoRental schema)
- `public/robots.txt` and `public/sitemap.xml` served at the site root

After your real domain is live, update `SITE_URL` in `build_seo.py`, run `npm run seo`, commit, push.

## Design system

| | |
|---|---|
| Adriatic Blue | `#001835` (primary, headers, body) |
| Vibrant Orange | `#FF5722` (primary CTAs only) |
| Sky Blue | `#d3e2ed` (chips, hover states) |
| Soft Background | `#f7f9fb` |

Type: **Plus Jakarta Sans** (headings), **Inter** (body). Both loaded from Google Fonts.

The Tailwind config (colors, spacing tokens, font sizes) is mirrored inline inside the `<head>` of every page. To change a brand color globally, search-and-replace the hex value across all `.html` files, then `npm run build`.

## Optional: switch from Tailwind CDN to compiled

The site currently loads Tailwind via `cdn.tailwindcss.com`. That's ~3 MB and shows a "production warning" in the console. To compile a minimal stylesheet (~40 KB):

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
# Edit tailwind.config.js: copy the theme.extend from any .html file's <script>
# Add content: ["./*.html"]
# Create src/input.css with @tailwind base; @tailwind components; @tailwind utilities;
# Add to package.json scripts: "build:css": "tailwindcss -i src/input.css -o public/tailwind.css --minify"
# In every .html, replace the CDN <script> tag with: <link rel="stylesheet" href="/tailwind.css">
```

## License

Site code: yours. Bundled third-party images / fonts / icons retain their original licenses (Plus Jakarta Sans + Inter: SIL OFL; Material Symbols: Apache 2.0; Tailwind: MIT; destination photos: verify per image).
