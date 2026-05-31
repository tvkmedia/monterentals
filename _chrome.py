"""
Shared page chrome (head/header/footer) used by every static HTML page in this
project. Keeps nav and footer markup identical across files so any future link
change is a one-place edit.

Usage:
    from _chrome import head, header, footer, end

    html = head("Page Title", active_nav="support") + header(active_nav="support") + \
           "<section>...</section>" + footer() + end()
    open("support.html", "w").write(html)
"""

TAILWIND_CONFIG = """
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "secondary-container":"#d3e2ed","on-secondary":"#ffffff","inverse-on-surface":"#eff1f3",
        "surface-variant":"#e0e3e5","background":"#f7f9fb","surface-tint":"#455f87",
        "on-surface-variant":"#43474e","secondary-fixed":"#d6e5ef","primary-fixed-dim":"#adc8f5",
        "surface-container-low":"#f2f4f6","surface-dim":"#d8dadc","on-tertiary-fixed":"#2e1500",
        "on-primary-fixed":"#001b3b","on-error":"#ffffff","on-tertiary":"#ffffff",
        "on-tertiary-fixed-variant":"#663d16","on-primary-container":"#7b95c0",
        "on-secondary-fixed":"#0f1d25","tertiary-container":"#472400","error":"#ba1a1a",
        "surface":"#f7f9fb","on-primary-fixed-variant":"#2d476e","outline-variant":"#c4c6cf",
        "on-surface":"#191c1e","outline":"#74777f","surface-container":"#eceef0",
        "surface-bright":"#f7f9fb","on-background":"#191c1e","tertiary":"#291300",
        "primary-fixed":"#d5e3ff","inverse-primary":"#adc8f5","on-tertiary-container":"#bf895b",
        "on-secondary-container":"#56656e","surface-container-highest":"#e0e3e5",
        "surface-container-high":"#e6e8ea","secondary":"#526069","secondary-fixed-dim":"#bac9d3",
        "on-error-container":"#93000a","tertiary-fixed-dim":"#f6ba88","tertiary-fixed":"#ffdcc1",
        "primary":"#001835","inverse-surface":"#2d3133","on-primary":"#ffffff",
        "error-container":"#ffdad6","primary-container":"#0f2d52",
        "surface-container-lowest":"#ffffff","on-secondary-fixed-variant":"#3b4951",
        "brand-accent":"#FF5722"
      },
      borderRadius: { DEFAULT:"0.25rem", lg:"0.5rem", xl:"0.75rem", "2xl":"1rem", "3xl":"1.5rem", full:"9999px" },
      spacing: {
        "gutter":"24px","margin-mobile":"16px","stack-sm":"8px","stack-lg":"32px",
        "container-max":"1280px","stack-md":"16px","section-padding":"80px"
      },
      fontFamily: {
        "body-md":["Inter"],"body-sm":["Inter"],"label-bold":["Inter"],
        "h2":["Plus Jakarta Sans"],"body-lg":["Inter"],"h3":["Plus Jakarta Sans"],
        "h1":["Plus Jakarta Sans"],"price-display":["Plus Jakarta Sans"]
      },
      fontSize: {
        "body-md":["16px",{ lineHeight:"1.5", fontWeight:"400" }],
        "body-sm":["14px",{ lineHeight:"1.5", fontWeight:"400" }],
        "label-bold":["14px",{ lineHeight:"1.2", fontWeight:"600" }],
        "h2":["32px",{ lineHeight:"1.3", fontWeight:"700" }],
        "body-lg":["18px",{ lineHeight:"1.6", fontWeight:"400" }],
        "h3":["24px",{ lineHeight:"1.4", fontWeight:"600" }],
        "h1":["48px",{ lineHeight:"1.2", letterSpacing:"-0.02em", fontWeight:"700" }],
        "price-display":["28px",{ lineHeight:"1", letterSpacing:"-0.01em", fontWeight:"700" }]
      }
    }
  }
};
"""

EXTRA_STYLES = """
.material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; vertical-align: middle; }
.shadow-ambient { box-shadow: 0 4px 20px rgba(15, 45, 82, 0.08); }
"""

# Mapping of active nav key → which top nav item gets the underline.
NAV_ITEMS = [
    ("fleet",        "Fleet",        "search.html"),
    ("travel",       "Travel Guide", "travel-guide.html"),
    ("rentals",      "Rentals",      "search.html"),
    ("locations",    "Locations",    "locations.html"),
]


def head(title, *, extra_css="") -> str:
    return f"""<!DOCTYPE html>
<html class="light" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title} — MontenegroDrive</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script>{TAILWIND_CONFIG}</script>
<style>{EXTRA_STYLES}{extra_css}</style>
</head>
<body class="bg-background text-on-background font-body-md antialiased">
"""


def header(active="") -> str:
    nav_html = []
    for key, label, href in NAV_ITEMS:
        if key == active:
            nav_html.append(
                f'<a class="text-primary font-label-bold border-b-2 border-primary transition-all duration-200" href="{href}">{label}</a>'
            )
        else:
            nav_html.append(
                f'<a class="text-secondary font-body-md hover:text-primary-container transition-colors" href="{href}">{label}</a>'
            )
    nav = "\n        ".join(nav_html)

    support_class = (
        "hidden md:block text-primary font-label-bold border-b-2 border-primary"
        if active == "support" else
        "hidden md:block text-secondary font-label-bold hover:text-primary transition-colors"
    )

    return f"""
<!-- TopNavBar -->
<header class="fixed top-0 w-full z-50 bg-surface shadow-sm">
  <div class="max-w-container-max mx-auto flex justify-between items-center px-gutter py-4">
    <div class="flex items-center gap-10">
      <a href="index.html" class="font-h2 text-h2 font-bold text-primary">MontenegroDrive</a>
      <nav class="hidden md:flex gap-6">
        {nav}
      </nav>
    </div>
    <div class="flex items-center gap-4">
      <a class="{support_class}" href="support.html">Support</a>
      <a class="bg-primary text-on-primary px-6 py-2.5 rounded-lg font-label-bold hover:shadow-lg transition-all" href="manage-booking.html">Manage Booking</a>
    </div>
  </div>
</header>
<main class="pt-[72px]">
"""


def footer() -> str:
    return """
</main>

<!-- Footer -->
<footer class="w-full py-section-padding px-gutter flex flex-col items-center gap-stack-lg bg-primary text-on-primary">
  <div class="max-w-container-max w-full flex flex-col md:flex-row justify-between items-start gap-12 border-b border-on-primary/10 pb-12">
    <div class="flex flex-col gap-4 max-w-[320px]">
      <span class="font-h3 text-h3 font-bold text-on-primary">MontenegroDrive</span>
      <p class="text-body-sm opacity-80">Premium car rental in Montenegro for business travelers and tourists. We guarantee safety, quality, and the best prices.</p>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-12">
      <div class="flex flex-col gap-4">
        <h5 class="font-label-bold text-tertiary-fixed uppercase tracking-wider">Explore</h5>
        <ul class="flex flex-col gap-2 opacity-80 text-body-sm">
          <li><a class="hover:text-secondary-fixed transition-opacity" href="search.html">Fleet</a></li>
          <li><a class="hover:text-secondary-fixed transition-opacity" href="locations.html">Locations</a></li>
          <li><a class="hover:text-secondary-fixed transition-opacity" href="travel-guide.html">Travel Guide</a></li>
        </ul>
      </div>
      <div class="flex flex-col gap-4">
        <h5 class="font-label-bold text-tertiary-fixed uppercase tracking-wider">Support</h5>
        <ul class="flex flex-col gap-2 opacity-80 text-body-sm">
          <li><a class="hover:text-secondary-fixed transition-opacity" href="support.html">Contact Us</a></li>
          <li><a class="hover:text-secondary-fixed transition-opacity" href="support.html#faq">FAQ</a></li>
          <li><a class="hover:text-secondary-fixed transition-opacity" href="manage-booking.html">Manage Booking</a></li>
        </ul>
      </div>
      <div class="flex flex-col gap-4">
        <h5 class="font-label-bold text-tertiary-fixed uppercase tracking-wider">Monte Club</h5>
        <p class="text-body-sm opacity-80">Partner with us to grow your car rental business in the region. Do you have a car that you don't use and want to earn money?</p>
        <a class="border border-on-primary px-5 py-2 rounded-lg font-label-bold hover:bg-on-primary hover:text-primary transition-all w-fit text-center text-body-sm" href="monte-club.html">Join Monte Club</a>
      </div>
      <div class="flex flex-col gap-4">
        <h5 class="font-label-bold text-tertiary-fixed uppercase tracking-wider">Legal</h5>
        <ul class="flex flex-col gap-2 opacity-80 text-body-sm">
          <li><a class="hover:text-secondary-fixed transition-opacity" href="legal.html#privacy">Privacy Policy</a></li>
          <li><a class="hover:text-secondary-fixed transition-opacity" href="legal.html#terms">Terms of Service</a></li>
          <li><a class="hover:text-secondary-fixed transition-opacity" href="legal.html#cookies">Cookie Policy</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="flex flex-col md:flex-row justify-between w-full max-w-container-max pt-2 opacity-70 text-body-sm gap-4">
    <p>© 2024 MontenegroDrive Car Rentals. All rights reserved.</p>
    <div class="flex gap-6 items-center">
      <a href="#" aria-label="Facebook" class="hover:text-secondary-fixed"><span class="material-symbols-outlined">public</span></a>
      <a href="#" aria-label="Instagram" class="hover:text-secondary-fixed"><span class="material-symbols-outlined">photo_camera</span></a>
      <a href="#" aria-label="Share" class="hover:text-secondary-fixed"><span class="material-symbols-outlined">share</span></a>
    </div>
  </div>
</footer>
"""


def end() -> str:
    return """
</body>
</html>
"""
