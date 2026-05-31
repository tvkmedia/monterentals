#!/usr/bin/env python3
"""
Inject favicon + per-page SEO meta tags + SVG logo into every HTML page.

Idempotent — re-runs safely. Uses sentinel comments so we know what's been
added previously and replace cleanly.

Run after build_pages.py, BEFORE build_elementor_templates.py (so the Elementor
JSON picks up the new logo markup in the header).
"""

import re
from pathlib import Path

OUT = Path("/sessions/stoic-laughing-albattani/mnt/outputs")
SITE_URL = "https://montenegrodrive.com"          # placeholder canonical domain
SITE_NAME = "MontenegroDrive"
DEFAULT_OG_IMAGE = f"{SITE_URL}/screenshot.png"

# --------------------------------------------------------------------
#  Per-page SEO metadata
# --------------------------------------------------------------------
# Keyed by filename. Fields:
#   title  — used for <title> + og:title + twitter:title
#   desc   — used for meta description, og:description, twitter:description
#   slug   — used for canonical URL
#   image  — og:image / twitter:image (defaults to DEFAULT_OG_IMAGE)
#   type   — og:type (default "website"; articles use "article")
META = {
    "index.html": {
        "title": "MontenegroDrive — Best Car Rental in Montenegro",
        "desc":  "Premium car rental across Montenegro. No hidden fees, free cancellation, 24/7 multilingual support. Counters at Tivat & Podgorica airports.",
        "slug":  "/",
    },
    "search.html": {
        "title": "Search Cars — MontenegroDrive",
        "desc":  "Browse 24+ rental cars in Budva, Kotor, Tivat and across Montenegro. Filter by category, fuel, supplier — economy from €45/day.",
        "slug":  "/search/",
    },
    "travel-guide.html": {
        "title": "Montenegro Travel Guide — MontenegroDrive",
        "desc":  "Road-trip tips, panoramic routes, border-crossing rules, and the best 4x4 trails in Montenegro — written by drivers who live here.",
        "slug":  "/travel-guide/",
    },
    "locations.html": {
        "title": "Locations in Montenegro — Cities, Parks & Things to Do",
        "desc":  "Nine must-visit cities, five national parks, and what to do across Montenegro — Budva, Kotor, Podgorica, Tivat, Herceg Novi and more.",
        "slug":  "/locations/",
    },
    "support.html": {
        "title": "Support & Contact — MontenegroDrive",
        "desc":  "24/7 multilingual support in English, Russian and Montenegrin. Phone, email, and live chat for booking changes, billing, lost & found.",
        "slug":  "/support/",
    },
    "manage-booking.html": {
        "title": "Manage Booking — MontenegroDrive",
        "desc":  "Sign in or look up by reference to change dates, upgrade your vehicle, add extras, or cancel a MontenegroDrive booking.",
        "slug":  "/manage-booking/",
    },
    "monte-club.html": {
        "title": "Monte Club — Earn Money With Your Idle Car",
        "desc":  "List your unused car with MontenegroDrive. We handle bookings, cleaning, insurance and customers. Indicative €450–950/month per economy car.",
        "slug":  "/monte-club/",
    },
    "legal.html": {
        "title": "Legal — Privacy, Terms & Cookies",
        "desc":  "MontenegroDrive's Privacy Policy, Terms of Service and Cookie Policy. GDPR-compliant.",
        "slug":  "/legal/",
    },
    "article-road-trip-tips.html": {
        "title": "10 Tips for Your Montenegro Road Trip — MontenegroDrive",
        "desc":  "From hidden gas stations to viewpoints worth the detour — ten things we tell every customer before they drive off in Montenegro.",
        "slug":  "/blog/10-tips-montenegro-road-trip/",
        "type":  "article",
    },
    "article-panoramic-routes.html": {
        "title": "Best Panoramic Routes in Europe — Montenegro Edition",
        "desc":  "Eight scenic drives in and around Montenegro — Kotor serpentine, Lovćen ring, Tara Canyon, Llogara Pass and more.",
        "slug":  "/blog/best-panoramic-routes-europe/",
        "type":  "article",
    },
    "article-driving-rules.html": {
        "title": "Driving in Montenegro — Rules, Speed Limits & Safety Guide",
        "desc":  "Licence requirements, speed limits, alcohol policy, insurance, required equipment, and what to do if you have an accident.",
        "slug":  "/blog/driving-in-montenegro/",
        "type":  "article",
    },
    "article-prokletije.html": {
        "title": "Prokletije: The Cursed Mountains — 4x4 Route Guide",
        "desc":  "A 60 km circuit through the wildest range in the Balkans. Vehicle requirements, key stops, practical notes.",
        "slug":  "/blog/prokletije-4x4-route/",
        "type":  "article",
    },
    "article-sinjajevina.html": {
        "title": "The Sinjajevina Highlands — Europe's 2nd-Largest Mountain Pasture",
        "desc":  "120 km² of rolling alpine plateau, shepherd huts, glacial lakes, and almost no other cars. A 50 km gravel route from Boan.",
        "slug":  "/blog/sinjajevina-highlands/",
        "type":  "article",
    },
    "article-komovi.html": {
        "title": "The Circular Komovi Route — Three Peaks, One 48 km Loop",
        "desc":  "A perfect mix of forest trails and limestone rock crawls around three of Montenegro's most iconic peaks.",
        "slug":  "/blog/komovi-circular-route/",
        "type":  "article",
    },
}


def seo_block(filename: str) -> str:
    """Generate the SEO + favicon block for a given page."""
    m = META[filename]
    canonical = f"{SITE_URL}{m['slug']}"
    og_image  = m.get("image", DEFAULT_OG_IMAGE)
    og_type   = m.get("type", "website")
    title     = m["title"]
    desc      = m["desc"]

    return f"""<!-- BEGIN SEO -->
<meta name="description" content="{desc}"/>
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1"/>
<meta name="theme-color" content="#001835"/>
<link rel="canonical" href="{canonical}"/>

<!-- Open Graph -->
<meta property="og:type" content="{og_type}"/>
<meta property="og:site_name" content="{SITE_NAME}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:image" content="{og_image}"/>
<meta property="og:locale" content="en_US"/>

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{desc}"/>
<meta name="twitter:image" content="{og_image}"/>

<!-- Favicon (SVG with raster fallback) -->
<link rel="icon" type="image/svg+xml" href="favicon.svg"/>
<link rel="apple-touch-icon" sizes="180x180" href="favicon.svg"/>
<link rel="mask-icon" href="favicon.svg" color="#001835"/>
<!-- END SEO -->"""


# JSON-LD structured data — only included on home page.
JSONLD_HOME = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "AutoRental",
  "name": "MontenegroDrive",
  "url": "{SITE_URL}",
  "logo": "{SITE_URL}/logo.svg",
  "image": "{SITE_URL}/screenshot.png",
  "description": "Premium car rental across Montenegro. No hidden fees, free cancellation, 24/7 multilingual support.",
  "telephone": "+382-20-123-456",
  "email": "support@montenegrodrive.example",
  "priceRange": "€€",
  "areaServed": {{ "@type": "Country", "name": "Montenegro" }},
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Bulevar Sv. Petra Cetinjskog 130",
    "addressLocality": "Podgorica",
    "postalCode": "81000",
    "addressCountry": "ME"
  }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "2500",
    "bestRating": "5"
  }},
  "sameAs": []
}}
</script>"""


# --------------------------------------------------------------------
#  Logo markup (SVG + wordmark, used in <header>)
# --------------------------------------------------------------------
LOGO_SVG = '''<a href="index.html" class="flex items-center gap-3 group" aria-label="MontenegroDrive — Home">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" class="w-10 h-10 flex-shrink-0 transition-transform group-hover:scale-105" aria-hidden="true">
          <rect width="40" height="40" rx="8" fill="#001835"/>
          <text x="20" y="29" font-family="'Plus Jakarta Sans', system-ui, sans-serif"
                font-size="26" font-weight="800" text-anchor="middle" fill="#FF5722">M</text>
        </svg>
        <span class="font-h2 text-h2 font-bold text-primary leading-none">MontenegroDrive</span>
      </a>'''


# --------------------------------------------------------------------
#  Patching helpers
# --------------------------------------------------------------------
SEO_RE   = re.compile(r"<!-- BEGIN SEO -->.*?<!-- END SEO -->", re.DOTALL)
JSONLD_RE = re.compile(r'<script type="application/ld\+json">.*?</script>', re.DOTALL)


def inject_seo(html: str, filename: str) -> str:
    """Insert (or replace) the SEO block right before </head>."""
    block = seo_block(filename)
    if SEO_RE.search(html):
        html = SEO_RE.sub(block, html)
    else:
        html = html.replace("</head>", f"{block}\n</head>", 1)

    # JSON-LD only on home
    if filename == "index.html":
        if JSONLD_RE.search(html):
            html = JSONLD_RE.sub(JSONLD_HOME, html)
        else:
            html = html.replace("</head>", f"{JSONLD_HOME}\n</head>", 1)

    return html


# Two distinct logo-anchor patterns appear across the pages.
# Pattern A: <a href="..." class="font-h2 text-h2 font-bold text-primary">MontenegroDrive</a>
# Pattern B: <div class="font-h2 ... ">MontenegroDrive</div>
LOGO_RE_A = re.compile(
    r'<a\s+href="index\.html"\s+class="font-h2\s+text-h2\s+font-bold\s+text-primary"\s*>\s*MontenegroDrive\s*</a>',
)
LOGO_RE_B = re.compile(
    r'<a\s+href="index\.html"\s+class="flex\s+items-center\s+gap-3\s+group"[^>]*aria-label[^>]*>.*?</a>',
    re.DOTALL,
)


def inject_logo(html: str) -> str:
    """Replace the plain text 'MontenegroDrive' header logo with the SVG version.
    Idempotent: re-running re-replaces an existing logo block."""
    # If the logo is already there, refresh it.
    if LOGO_RE_B.search(html):
        return LOGO_RE_B.sub(LOGO_SVG, html, count=1)
    # Otherwise look for the plain-text version and upgrade it.
    if LOGO_RE_A.search(html):
        return LOGO_RE_A.sub(LOGO_SVG, html, count=1)
    # No header logo present — give up silently rather than corrupting the file.
    return html


def main():
    files = sorted(p for p in OUT.glob("*.html"))
    for f in files:
        if f.name not in META:
            print(f"  · {f.name}  (no SEO metadata defined — skipping)")
            continue
        html = f.read_text(encoding="utf-8")
        html2 = inject_seo(html, f.name)
        html3 = inject_logo(html2)
        if html3 != html:
            f.write_text(html3, encoding="utf-8")
            print(f"  ✓ {f.name}")
        else:
            print(f"  · {f.name}  (no changes needed)")

    # --- robots.txt + sitemap.xml ---
    (OUT / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n",
        encoding="utf-8",
    )
    print("  ✓ robots.txt")

    urls = []
    for fname, meta in META.items():
        urls.append(f"  <url>\n"
                    f"    <loc>{SITE_URL}{meta['slug']}</loc>\n"
                    f"    <changefreq>{'weekly' if meta.get('type') != 'article' else 'monthly'}</changefreq>\n"
                    f"    <priority>{'1.0' if meta['slug'] == '/' else '0.7'}</priority>\n"
                    f"  </url>")
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n"
        '</urlset>\n'
    )
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print("  ✓ sitemap.xml")


if __name__ == "__main__":
    print("Injecting SEO + favicon + logo...")
    main()
    print("Done.")
