# MontenegroDrive — WordPress Theme for Elementor Pro

A premium car-rental theme for Montenegro travel agencies. Built on the **Montenegro Elite Travel** design system (Adriatic Blue + Vibrant Orange palette, Plus Jakarta Sans + Inter typography), with three importable Elementor Pro page templates.

---

## What's included

```
montenegrodrive/
├── style.css                         Theme metadata + design tokens
├── functions.php                      Theme setup, asset enqueue, Elementor support
├── theme.json                         Block editor color/font integration
├── header.php / footer.php            Fallback header & footer (used when Elementor
│                                      Pro Theme Builder hasn't built one yet)
├── index.php                          Blog index fallback
├── page.php                           Standard page template
├── page-elementor-canvas.php          Custom canvas template (no header / no footer)
├── single.php / search.php / 404.php  Standard supporting templates
├── searchform.php / comments.php
├── screenshot.png                     Theme thumbnail shown in Appearance → Themes
├── assets/css/theme-tokens.css        Design token reference
└── elementor-templates/                14 importable page templates:
    ├── home.json                       Home — Hero, Search, Trust, Features, Destinations
    ├── search-results.json             Search Results — Filters + listings + pagination
    ├── travel-guide.json               Travel Guide — Featured stories + 4x4 routes
    ├── support.json                    Support & Contact (combined) — contact channels,
    │                                   contact form, FAQ accordion, office info
    ├── manage-booking.json             Manage Booking — sign-in OR ref-lookup tabs,
    │                                   plus a demo "logged-in" booking dashboard
    ├── locations.json                  Locations — 9 cities, 5 national parks, what-to-do
    ├── monte-club.json                 Monte Club (partner programme) — "earn money
    │                                   with your idle car", 3-step process, application form
    ├── legal.json                      Legal — Privacy / Terms / Cookies anchored sections
    └── article-*.json (6 files)        Travel-guide article pages:
                                          • article-road-trip-tips      (10 tips, long-form)
                                          • article-panoramic-routes    (8 scenic drives)
                                          • article-driving-rules       (safety guide)
                                          • article-prokletije          (4x4 route)
                                          • article-sinjajevina         (4x4 route)
                                          • article-komovi              (4x4 route)
```

---

## Requirements

| Plugin / Software                | Version          | Required? |
|----------------------------------|------------------|-----------|
| WordPress                        | 6.0 or newer     | Yes       |
| PHP                              | 7.4 or newer     | Yes       |
| **Elementor** (free)             | 3.18 or newer    | Yes       |
| **Elementor Pro**                | 3.18 or newer    | Yes (for Forms, Theme Builder, Posts widgets) |

---

## Installation

### 1. Install Elementor + Elementor Pro

In wp-admin:
1. **Plugins → Add New** → search for "Elementor" → Install and activate.
2. Upload Elementor Pro (`elementor-pro.zip` from your account at elementor.com): **Plugins → Add New → Upload Plugin**.

### 2. Upload the theme

1. Zip the `montenegrodrive/` folder so you have `montenegrodrive.zip` at the top level (the included archive is already zipped — skip if you downloaded the .zip).
2. In wp-admin: **Appearance → Themes → Add New Theme → Upload Theme**.
3. Choose `montenegrodrive.zip` → **Install Now** → **Activate**.

You'll see a yellow admin notice at the top of every screen reminding you to install Elementor if it isn't already active.

### 3. Import the Elementor templates

For each of the fourteen template JSON files in `elementor-templates/`:

1. Go to **Templates → Saved Templates** (in the wp-admin sidebar).
2. Click **Import Templates** at the top of the page.
3. Drag in or upload one of the `.json` files from `wp-content/themes/montenegrodrive/elementor-templates/`.
4. Repeat for the other two.

The imported templates appear in the Saved Templates list with their titles ("MontenegroDrive — Home", etc.).

### 4. Create your pages

For each page (Home / Search Results / Travel Guide):

1. **Pages → Add New** → give it a title (e.g. "Home").
2. In the right sidebar, set **Page Attributes → Template = "Elementor Canvas (MontenegroDrive)"** to get the full-bleed layout without theme header/footer.
   *(Alternatively, set it to "Default Template" if you want the theme's header/footer wrapper. Choice is yours.)*
3. Click **Edit with Elementor**.
4. In the Elementor editor, click the **folder icon** in the canvas (or **Add Template** button) → **My Templates** tab → find the corresponding `MontenegroDrive — *` template → **Insert**.
5. Confirm "Apply Document Settings" when prompted (this carries over the page settings from the template).
6. Click **Update** to save.

### 5. Set the home page

**Settings → Reading → Your homepage displays = "A static page"** → set **Homepage = Home**.

### 6. (Recommended) Build a Theme Builder header & footer

To get the same sticky navigation across every page, build them once via Elementor Pro's Theme Builder:

1. **Templates → Theme Builder → Header → Add New**.
2. Drag in a Site Logo, Nav Menu (linked to the WordPress menu you'll create), and a Button widget.
3. **Publish → Display Conditions = "Entire Site"**.
4. Repeat for **Footer**.

Once a Theme Builder header/footer exists, the theme automatically yields to it (header.php and footer.php check for `elementor_theme_do_location()` and skip the fallback markup).

---

## Customising colors & fonts

The Stitch design tokens are exposed in three places — pick whichever you prefer:

| Where                              | What it controls                                       |
|------------------------------------|--------------------------------------------------------|
| `style.css` (`:root` variables)    | CSS variables (`--md-primary`, etc.) — usable in any Elementor "Custom CSS" panel as `color: var(--md-primary);` |
| `functions.php` → `montenegrodrive_get_tailwind_config_js()` | Tailwind utility class colors (`text-primary`, `bg-brand-accent`, etc.) |
| `theme.json`                       | Block editor / Site Editor color palette + font sizes  |
| **Elementor → Site Settings → Global Colors** | Visual editor — overrides the above for any new widget you add. Recommended for most edits. |

The brand palette:

| Token                | Hex       | Use                                              |
|----------------------|-----------|--------------------------------------------------|
| `--md-primary`       | `#001835` | Adriatic Blue — headers, primary buttons, body   |
| `--md-secondary-container` | `#d3e2ed` | Sky Blue — chip backgrounds, hover states  |
| `--md-brand-accent`  | `#FF5722` | Vibrant Orange — primary CTAs only               |
| `--md-background`    | `#f7f9fb` | Page canvas                                       |

---

## Tailwind: CDN vs. compiled

The theme loads Tailwind from `cdn.tailwindcss.com` for zero-config startup. That's fine for staging and small sites, but for production you'll want a compiled stylesheet:

1. Run `npm init -y && npm install -D tailwindcss && npx tailwindcss init` in the theme folder.
2. Copy the config from `functions.php → montenegrodrive_get_tailwind_config_js()` into `tailwind.config.js`.
3. Add `content: ["./**/*.php", "./elementor-templates/*.json"]` so unused utility classes are purged.
4. Run `npx tailwindcss -i ./assets/css/input.css -o ./assets/css/tailwind.min.css --minify`.
5. In `functions.php`, comment out the `montenegrodrive-tailwind` `wp_enqueue_script` calls and add `wp_enqueue_style('montenegrodrive-tailwind', get_template_directory_uri() . '/assets/css/tailwind.min.css');`.

This drops the ~3 MB CDN runtime down to a ~40 KB minified stylesheet.

---

## Updating the destination images

The home page card images load via Wikimedia Commons' `Special:FilePath` redirect endpoint, with a JavaScript `onerror` fallback chain to alternate filenames and finally to a guaranteed Unsplash photo. If you'd prefer to use your own photos:

1. Edit the Home page in Elementor → click the destination card image → **Choose Image** → upload your photo to the Media Library.

The HTML widget content in `home.json` is plain HTML, so swapping `<img src="...">` works exactly like editing static HTML.

---

## Template structure (Elementor)

Each imported template is built as a stack of **Elementor Sections**, with each section containing a single **HTML widget**. This means you can:

- **Reorder** sections by drag-and-drop in Elementor's Navigator
- **Duplicate / hide / delete** any section individually
- **Replace** an HTML widget with a native Elementor widget composition (e.g. swap the hero HTML for an Elementor Hero with a Form widget) without touching the rest
- **Edit** the Tailwind-styled HTML directly in the HTML widget if you want pixel-level control

Section labels visible in the Elementor Navigator:

| Template          | Sections                                                                                              |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Home              | Header · Hero · Trust Bar · Features · Popular Destinations · Footer                                  |
| Search Results    | Header · Filters & Listings · Footer                                                                  |
| Travel Guide      | Header · Hero · Featured Stories · Best 4x4 Routes · Border Crossing Rules · Roll-out CTA · Newsletter · Footer |
| Support           | Header · Hero · Contact channels · Contact form · FAQ accordion · Footer                              |
| Manage Booking    | Header · Sign-in / lookup tabs · Demo booking dashboard · Footer                                      |
| Locations         | Header · Hero · Must-visit cities · National parks · What to do · CTA · Footer                        |
| Monte Club        | Header · Hero · How it works · Why partner · Application form · Footer                                |
| Legal             | Header · Privacy / Terms / Cookies · Footer                                                           |
| Articles (×6)     | Header · Hero · Body · Related articles · Footer                                                      |

**Recommended page-creation map** for wp-admin **Pages → Add New**:

| WP page title         | Slug              | Template to apply (Page Attributes)        | Elementor template to insert |
|-----------------------|-------------------|---------------------------------------------|------------------------------|
| Home                  | `/`               | Elementor Canvas (MontenegroDrive)          | MontenegroDrive — Home       |
| Search Results        | `/search/`        | Elementor Canvas (MontenegroDrive)          | MontenegroDrive — Search Results |
| Travel Guide          | `/travel-guide/`  | Elementor Canvas (MontenegroDrive)          | MontenegroDrive — Travel Guide |
| Support               | `/support/`       | Default Template (header & footer wrapper)  | MontenegroDrive — Support & Contact |
| Manage Booking        | `/manage-booking/`| Elementor Canvas (MontenegroDrive)          | MontenegroDrive — Manage Booking |
| Locations             | `/locations/`     | Default Template                            | MontenegroDrive — Locations  |
| Monte Club            | `/monte-club/`    | Default Template                            | MontenegroDrive — Monte Club |
| Legal                 | `/legal/`         | Default Template                            | MontenegroDrive — Legal      |
| (6 article pages)     | `/blog/<slug>/`   | Default Template                            | Article — *                  |

Then in **Appearance → Menus → Primary Menu**, add: Fleet (→ Search), Travel Guide, Rentals (→ Search), Locations. Save and assign to "Primary Menu" location.

---

## Troubleshooting

**Q: Tailwind classes aren't applying / I see a flash of unstyled content.**
The Tailwind CDN script runs after page load. Switch to a compiled stylesheet (see "Tailwind: CDN vs. compiled" above) to eliminate the flash.

**Q: The destination images on the home page show broken-image icons.**
The Wikimedia Commons filenames in the fallback chain may have changed. Open the home page in Elementor, click each destination image, and upload your own to the Media Library. The included `onerror` chain falls back to an Unsplash photo if all Wikimedia URLs 404.

**Q: I imported a template but it looks unstyled in the editor.**
Make sure the page is set to **Page Attributes → Template = "Elementor Canvas (MontenegroDrive)"** OR that you've previewed the page on the front-end (Tailwind CDN only runs on the front-end, not inside Elementor's editor iframe by default).

**Q: How do I add a contact form to the page?**
Elementor Pro → drag the **Form** widget into an existing section, configure recipients in Form Settings, save. The form will pick up the theme's colors via Site Settings → Global Colors.

---

## Licensing

- Theme code: GPL v2 or later
- Plus Jakarta Sans & Inter fonts: SIL Open Font License
- Material Symbols (Google): Apache 2.0
- Tailwind CSS: MIT
- Sample images: Wikimedia Commons (verify the license per image; most are CC BY-SA), Unsplash (free for commercial use)

Replace any placeholder text and images with your own content before launch.
