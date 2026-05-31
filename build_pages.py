#!/usr/bin/env python3
"""
Generate all the new pages (support, manage-booking, locations, monte-club,
travel-guide articles, legal) using the shared _chrome helpers.

Run from /sessions/.../outputs/ — writes static HTML next to it.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _chrome import head, header, footer, end  # noqa: E402

OUT = Path("/sessions/stoic-laughing-albattani/mnt/outputs")


# ----------------------------------------------------------------------
# Reusable section helpers
# ----------------------------------------------------------------------

def hero(title: str, subtitle: str, bg_url: str, badge: str = "") -> str:
    badge_html = (
        f'<span class="inline-block bg-secondary-container text-on-secondary-container px-4 py-1.5 rounded-full font-label-bold mb-stack-md">{badge}</span>'
        if badge else ""
    )
    return f"""
<section class="relative h-[460px] flex items-center overflow-hidden">
  <div class="absolute inset-0 z-0">
    <img class="w-full h-full object-cover" alt="" src="{bg_url}"/>
    <div class="absolute inset-0 bg-gradient-to-r from-primary/80 via-primary/50 to-primary/30"></div>
  </div>
  <div class="relative z-10 max-w-container-max mx-auto px-gutter w-full">
    <div class="max-w-3xl">
      {badge_html}
      <h1 class="font-h1 text-h1 text-white mb-stack-md drop-shadow-md">{title}</h1>
      <p class="font-body-lg text-body-lg text-white/90 leading-relaxed">{subtitle}</p>
    </div>
  </div>
</section>
"""


# ----------------------------------------------------------------------
# Support / Contact page
# ----------------------------------------------------------------------

def write_support():
    body = hero(
        "We're here to help",
        "Talk to our 24/7 multilingual support team about a booking, billing question, or anything in between. Average response time: under 2 hours.",
        "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?q=80&w=1800&auto=format&fit=crop",
        badge="Support &amp; Contact",
    )

    body += """
<!-- Contact channels -->
<section class="py-section-padding px-gutter">
  <div class="max-w-container-max mx-auto grid grid-cols-1 md:grid-cols-3 gap-6">
    <div class="bg-white rounded-xl p-8 shadow-ambient border border-outline-variant/30 text-center">
      <div class="w-14 h-14 mx-auto mb-stack-md bg-secondary-container rounded-full flex items-center justify-center text-primary">
        <span class="material-symbols-outlined text-[28px]">call</span>
      </div>
      <h3 class="font-h3 text-h3 text-primary mb-2">Call us</h3>
      <p class="text-secondary mb-4">24/7 in English, Russian and Montenegrin.</p>
      <a href="tel:+38220123456" class="text-primary font-label-bold">+382 20 123 456</a>
    </div>
    <div class="bg-white rounded-xl p-8 shadow-ambient border border-outline-variant/30 text-center">
      <div class="w-14 h-14 mx-auto mb-stack-md bg-secondary-container rounded-full flex items-center justify-center text-primary">
        <span class="material-symbols-outlined text-[28px]">mail</span>
      </div>
      <h3 class="font-h3 text-h3 text-primary mb-2">Email us</h3>
      <p class="text-secondary mb-4">Replies within 2 business hours.</p>
      <a href="mailto:support@montenegrodrive.example" class="text-primary font-label-bold">support@montenegrodrive.example</a>
    </div>
    <div class="bg-white rounded-xl p-8 shadow-ambient border border-outline-variant/30 text-center">
      <div class="w-14 h-14 mx-auto mb-stack-md bg-secondary-container rounded-full flex items-center justify-center text-primary">
        <span class="material-symbols-outlined text-[28px]">chat</span>
      </div>
      <h3 class="font-h3 text-h3 text-primary mb-2">Live chat</h3>
      <p class="text-secondary mb-4">Average wait time: 38 seconds.</p>
      <button class="text-primary font-label-bold underline underline-offset-4">Open chat window</button>
    </div>
  </div>
</section>

<!-- Contact form -->
<section class="py-section-padding px-gutter bg-surface-container-low">
  <div class="max-w-container-max mx-auto grid grid-cols-1 lg:grid-cols-5 gap-12">
    <div class="lg:col-span-2">
      <h2 class="font-h2 text-h2 text-primary mb-stack-md">Send us a message</h2>
      <p class="text-secondary font-body-md mb-stack-lg">
        Fill out the form and a member of our customer-care team will get back to you within two business hours. For urgent booking changes within 24 hours of pick-up, please call us instead.
      </p>
      <div class="flex items-start gap-4 mb-stack-md">
        <span class="material-symbols-outlined text-primary bg-secondary-container p-2 rounded-lg">location_on</span>
        <div>
          <p class="font-label-bold text-primary">Head office</p>
          <p class="text-body-sm text-secondary">Bulevar Sv. Petra Cetinjskog 130, 81000 Podgorica, Montenegro</p>
        </div>
      </div>
      <div class="flex items-start gap-4">
        <span class="material-symbols-outlined text-primary bg-secondary-container p-2 rounded-lg">schedule</span>
        <div>
          <p class="font-label-bold text-primary">Counter hours</p>
          <p class="text-body-sm text-secondary">Mon–Sun · 06:00–24:00 (TIV) · 24/7 phone &amp; chat</p>
        </div>
      </div>
    </div>
    <form class="lg:col-span-3 bg-white p-8 rounded-xl shadow-ambient flex flex-col gap-4">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Full name</span>
          <input type="text" required class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Email</span>
          <input type="email" required class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Booking number (optional)</span>
          <input type="text" placeholder="MNE-XXXXXX" class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Topic</span>
          <select class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary bg-white">
            <option>Booking change or cancellation</option>
            <option>Billing &amp; refunds</option>
            <option>Damage or insurance claim</option>
            <option>Lost &amp; found</option>
            <option>Corporate / fleet enquiry</option>
            <option>Press / partnership</option>
            <option>Other</option>
          </select>
        </label>
      </div>
      <label class="flex flex-col gap-2">
        <span class="font-label-bold text-on-surface-variant text-sm">Message</span>
        <textarea rows="6" required class="px-4 py-3 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary resize-y"></textarea>
      </label>
      <label class="flex items-start gap-3 text-body-sm text-secondary">
        <input type="checkbox" class="mt-1 rounded border-outline-variant"/>
        <span>I agree to the <a href="legal.html#privacy" class="text-primary underline">Privacy Policy</a> and consent to MontenegroDrive contacting me about my request.</span>
      </label>
      <button type="submit" class="bg-[#FF5722] hover:bg-[#E64A19] text-white font-label-bold h-14 rounded-lg shadow-lg transition-all uppercase tracking-wide">
        Send message
      </button>
    </form>
  </div>
</section>

<!-- FAQ accordion -->
<section id="faq" class="py-section-padding px-gutter">
  <div class="max-w-3xl mx-auto">
    <div class="text-center mb-stack-lg">
      <h2 class="font-h2 text-h2 text-primary mb-stack-sm">Frequently asked questions</h2>
      <p class="text-secondary font-body-md">Quick answers to the questions we hear most often.</p>
    </div>
    <div class="flex flex-col gap-4">
"""
    faqs = [
        ("What documents do I need to rent a car?",
         "A valid passport or national ID, your full driver's licence (held for at least one year), and the credit card you used to book. EU citizens are fine with their EU licence; everyone else should bring an International Driving Permit alongside their national licence."),
        ("Can I drive my rental into Croatia, Bosnia or Albania?",
         "Yes — we issue a Green Card (mandatory cross-border insurance) free of charge as long as you tell us at pick-up. Some categories (luxury and 4x4) have a small daily cross-border fee. Kosovo is excluded across the entire fleet."),
        ("Is the price I see the final price?",
         "Yes. Our prices always include unlimited mileage, basic insurance with collision damage waiver, theft protection, airport surcharge, and VAT. Optional extras (additional driver, child seats, GPS, full insurance) are clearly priced at checkout."),
        ("How does the fuel policy work?",
         "Full to full — you pick the car up with a full tank and return it full. Save your last fuel receipt; we ask for it on return. If you're short on time we can refuel for you at the local pump rate plus a €15 service fee."),
        ("Can I cancel or change my booking?",
         "Free cancellation until 48 hours before pick-up — no questions asked, full refund within 5 business days. Inside the 48-hour window we charge one day's rental. You can modify dates and pick-up location any time, subject to availability."),
        ("What happens if I'm late picking the car up?",
         "We hold your booking for 90 minutes after the scheduled time at no charge. After that please call the local counter — flight delays and ferry hold-ups are common and we'll always try to accommodate you."),
    ]
    for q, a in faqs:
        body += f"""
      <details class="bg-white rounded-xl shadow-sm border border-outline-variant/30 group">
        <summary class="cursor-pointer px-6 py-5 flex justify-between items-center font-label-bold text-primary text-base">
          <span>{q}</span>
          <span class="material-symbols-outlined text-primary transition-transform group-open:rotate-180">expand_more</span>
        </summary>
        <div class="px-6 pb-5 text-secondary text-body-md leading-relaxed">{a}</div>
      </details>"""
    body += """
    </div>
  </div>
</section>
"""

    html = head("Support &amp; Contact") + header(active="support") + body + footer() + end()
    (OUT / "support.html").write_text(html, encoding="utf-8")
    print("  ✓ support.html")


# ----------------------------------------------------------------------
# Manage Booking page
# ----------------------------------------------------------------------

def write_manage_booking():
    body = """
<section class="py-section-padding px-gutter min-h-[calc(100vh-72px)] bg-gradient-to-br from-primary via-primary-container to-primary">
  <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">

    <!-- Left: marketing copy -->
    <div class="text-white">
      <span class="inline-block bg-white/15 backdrop-blur-sm px-4 py-1.5 rounded-full font-label-bold mb-stack-md text-white/90 border border-white/20">
        Self-service portal
      </span>
      <h1 class="font-h1 text-h1 mb-stack-md drop-shadow-md">Manage your booking in seconds</h1>
      <p class="font-body-lg text-body-lg text-white/85 mb-stack-lg leading-relaxed">
        Sign in with the email you booked under and your booking number to change dates, upgrade your vehicle, add extras, request an invoice, or cancel.
      </p>
      <ul class="flex flex-col gap-stack-md">
        <li class="flex items-start gap-4">
          <span class="material-symbols-outlined text-tertiary-fixed-dim mt-1">edit_calendar</span>
          <div>
            <p class="font-label-bold">Change dates &amp; pick-up location</p>
            <p class="text-body-sm text-white/75">Free until 48 hours before pick-up.</p>
          </div>
        </li>
        <li class="flex items-start gap-4">
          <span class="material-symbols-outlined text-tertiary-fixed-dim mt-1">upgrade</span>
          <div>
            <p class="font-label-bold">Upgrade your vehicle</p>
            <p class="text-body-sm text-white/75">Pay only the difference if availability allows.</p>
          </div>
        </li>
        <li class="flex items-start gap-4">
          <span class="material-symbols-outlined text-tertiary-fixed-dim mt-1">receipt_long</span>
          <div>
            <p class="font-label-bold">Download your VAT invoice</p>
            <p class="text-body-sm text-white/75">Issued from our Podgorica office.</p>
          </div>
        </li>
        <li class="flex items-start gap-4">
          <span class="material-symbols-outlined text-tertiary-fixed-dim mt-1">cancel</span>
          <div>
            <p class="font-label-bold">Cancel for a full refund</p>
            <p class="text-body-sm text-white/75">No questions asked outside the 48h window.</p>
          </div>
        </li>
      </ul>
    </div>

    <!-- Right: login card -->
    <div class="bg-white rounded-2xl shadow-2xl p-8 md:p-10">
      <div class="flex gap-2 mb-stack-lg p-1 bg-surface-container-low rounded-lg">
        <button id="tab-login"  type="button" class="flex-1 py-2.5 rounded-md bg-primary text-on-primary font-label-bold transition-all">Sign in</button>
        <button id="tab-lookup" type="button" class="flex-1 py-2.5 rounded-md text-secondary font-label-bold hover:bg-white transition-all">Look up by ref</button>
      </div>

      <!-- Sign-in form -->
      <form id="form-login" class="flex flex-col gap-4">
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Email address</span>
          <input type="email" required placeholder="you@example.com" class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Password</span>
          <input type="password" required placeholder="••••••••" class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
        <div class="flex justify-between items-center text-body-sm">
          <label class="flex items-center gap-2 text-secondary"><input type="checkbox" class="rounded border-outline-variant"/> Remember me</label>
          <a href="support.html" class="text-primary font-label-bold">Forgot password?</a>
        </div>
        <button type="button" onclick="document.getElementById('demo-booking').scrollIntoView({behavior:'smooth'})"
                class="bg-[#FF5722] hover:bg-[#E64A19] text-white font-label-bold h-12 rounded-lg shadow-lg transition-all uppercase tracking-wide">
          Sign in
        </button>
        <p class="text-center text-body-sm text-secondary">Don't have an account? <a href="search.html" class="text-primary font-label-bold">Book your first car →</a></p>
      </form>

      <!-- Reference lookup -->
      <form id="form-lookup" class="hidden flex-col gap-4">
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Booking reference</span>
          <input type="text" required placeholder="MNE-123456" class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary uppercase tracking-wider"/>
        </label>
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Email used at booking</span>
          <input type="email" required class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
        <button type="button" onclick="document.getElementById('demo-booking').scrollIntoView({behavior:'smooth'})"
                class="bg-primary hover:bg-primary-container text-white font-label-bold h-12 rounded-lg shadow-lg transition-all uppercase tracking-wide">
          Find my booking
        </button>
      </form>
    </div>
  </div>
</section>

<!-- Demo booking dashboard (shown after "login") -->
<section id="demo-booking" class="py-section-padding px-gutter bg-background">
  <div class="max-w-container-max mx-auto">
    <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-stack-lg gap-4">
      <div>
        <span class="text-body-sm text-secondary">Booking reference</span>
        <h2 class="font-h2 text-h2 text-primary">MNE-298714</h2>
      </div>
      <span class="bg-secondary-container text-on-secondary-container px-4 py-2 rounded-full font-label-bold uppercase tracking-wider text-xs">Confirmed</span>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Car card -->
      <div class="bg-white rounded-xl shadow-ambient overflow-hidden">
        <img class="w-full h-44 object-cover" alt="Volkswagen Polo" src="https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?q=80&amp;w=1200&amp;auto=format&amp;fit=crop"/>
        <div class="p-6">
          <h3 class="font-h3 text-h3 text-primary mb-1">Volkswagen Polo</h3>
          <p class="text-body-sm text-secondary mb-stack-md">Economy · Manual · A/C · 5 seats</p>
          <button class="text-primary font-label-bold flex items-center gap-2 hover:gap-3 transition-all">
            Upgrade vehicle <span class="material-symbols-outlined text-[18px]">arrow_right_alt</span>
          </button>
        </div>
      </div>

      <!-- Itinerary -->
      <div class="bg-white rounded-xl shadow-ambient p-6 lg:col-span-2 flex flex-col gap-4">
        <h3 class="font-h3 text-h3 text-primary mb-2">Your itinerary</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="border border-outline-variant/40 rounded-lg p-4">
            <p class="text-body-sm text-secondary uppercase tracking-wider mb-1">Pick-up</p>
            <p class="font-label-bold text-primary text-base">Tivat Airport (TIV)</p>
            <p class="text-body-sm text-secondary">Sat, 7 Jun 2025 · 14:30</p>
          </div>
          <div class="border border-outline-variant/40 rounded-lg p-4">
            <p class="text-body-sm text-secondary uppercase tracking-wider mb-1">Drop-off</p>
            <p class="font-label-bold text-primary text-base">Podgorica Airport (TGD)</p>
            <p class="text-body-sm text-secondary">Sat, 14 Jun 2025 · 11:00</p>
          </div>
        </div>
        <div class="flex flex-wrap gap-2 mt-2">
          <button class="border border-primary text-primary font-label-bold px-4 py-2 rounded-lg hover:bg-primary hover:text-on-primary transition-all flex items-center gap-2">
            <span class="material-symbols-outlined text-[18px]">edit_calendar</span> Change dates
          </button>
          <button class="border border-primary text-primary font-label-bold px-4 py-2 rounded-lg hover:bg-primary hover:text-on-primary transition-all flex items-center gap-2">
            <span class="material-symbols-outlined text-[18px]">add_location</span> Change location
          </button>
          <button class="border border-primary text-primary font-label-bold px-4 py-2 rounded-lg hover:bg-primary hover:text-on-primary transition-all flex items-center gap-2">
            <span class="material-symbols-outlined text-[18px]">add</span> Add extras
          </button>
        </div>
      </div>

      <!-- Price summary -->
      <div class="bg-white rounded-xl shadow-ambient p-6 lg:col-span-2 flex flex-col gap-3">
        <h3 class="font-h3 text-h3 text-primary mb-2">Price breakdown</h3>
        <div class="flex justify-between text-body-md"><span class="text-secondary">7 days @ 45 €/day</span><span>315.00 €</span></div>
        <div class="flex justify-between text-body-md"><span class="text-secondary">Cross-border (Croatia)</span><span>21.00 €</span></div>
        <div class="flex justify-between text-body-md"><span class="text-secondary">Additional driver</span><span>35.00 €</span></div>
        <div class="flex justify-between text-body-md text-error"><span>Loyalty discount</span><span>−18.00 €</span></div>
        <div class="border-t border-outline-variant/40 my-2"></div>
        <div class="flex justify-between font-h3 text-h3 text-primary"><span>Total paid</span><span>353.00 €</span></div>
        <button class="text-primary font-label-bold underline underline-offset-4 text-left">Download VAT invoice</button>
      </div>

      <!-- Quick actions -->
      <div class="bg-primary-container text-on-primary rounded-xl p-6 text-white flex flex-col gap-3">
        <h3 class="font-h3 text-h3">Need help?</h3>
        <p class="text-body-sm opacity-90">Talk to a real human in under a minute.</p>
        <a href="tel:+38220123456" class="bg-[#FF5722] hover:bg-[#E64A19] text-white font-label-bold px-6 py-3 rounded-lg text-center">Call +382 20 123 456</a>
        <a href="support.html" class="border border-white/40 text-white font-label-bold px-6 py-3 rounded-lg text-center hover:bg-white hover:text-primary transition-all">Open a chat</a>
        <button class="text-white/80 hover:text-white text-body-sm underline underline-offset-4 mt-2 text-left">Cancel this booking</button>
      </div>
    </div>
  </div>
</section>

<script>
  // Tiny tab toggle between the sign-in and ref-lookup forms.
  (function () {
    var login = document.getElementById('form-login');
    var lookup = document.getElementById('form-lookup');
    var tabL = document.getElementById('tab-login');
    var tabR = document.getElementById('tab-lookup');
    function show(which) {
      if (which === 'login') {
        login.classList.remove('hidden'); login.classList.add('flex');
        lookup.classList.add('hidden'); lookup.classList.remove('flex');
        tabL.classList.add('bg-primary','text-on-primary');
        tabL.classList.remove('text-secondary');
        tabR.classList.remove('bg-primary','text-on-primary');
        tabR.classList.add('text-secondary');
      } else {
        lookup.classList.remove('hidden'); lookup.classList.add('flex');
        login.classList.add('hidden'); login.classList.remove('flex');
        tabR.classList.add('bg-primary','text-on-primary');
        tabR.classList.remove('text-secondary');
        tabL.classList.remove('bg-primary','text-on-primary');
        tabL.classList.add('text-secondary');
      }
    }
    tabL && tabL.addEventListener('click', function(){ show('login'); });
    tabR && tabR.addEventListener('click', function(){ show('lookup'); });
  })();
</script>
"""

    # No standard hero here (custom split layout) — start <main> with the section.
    html = head("Manage Booking") + header() + body + footer() + end()
    (OUT / "manage-booking.html").write_text(html, encoding="utf-8")
    print("  ✓ manage-booking.html")


# ----------------------------------------------------------------------
# Locations page
# ----------------------------------------------------------------------

CITY_CARDS = [
    ("Budva", "Walled medieval old town, sandy beaches, the liveliest nightlife on the Adriatic.",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Old_Town_of_Budva.jpg?width=1200", 142),
    ("Kotor", "UNESCO World Heritage bay with a Venetian-era fortified town and cliff-side fortifications.",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Kotor,_Montenegro.jpg?width=1200", 98),
    ("Podgorica", "The modern capital. Millennium Bridge, café culture, and the gateway to the lakes.",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Most_Milenijum_Podgorica.jpg?width=1200", 215),
    ("Tivat", "Porto Montenegro super-yacht marina and the country's busiest international airport.",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Porto_Montenegro,_Tivat.jpg?width=1200", 167),
    ("Herceg Novi", "Fortress city at the mouth of the Bay of Kotor — botanical gardens and old steps.",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Herceg_Novi.jpg?width=1200", 76),
    ("Cetinje", "The old royal capital. Monasteries, museums and the start of the Lov&#263;en climb.",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Cetinje_Montenegro.jpg?width=1200", 42),
    ("Bar", "Olive-tree groves, the Stari Bar ruins and the ferry link to Bari, Italy.",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Stari_Bar.jpg?width=1200", 58),
    ("Ulcinj", "Long sandy beaches, an Ottoman-era citadel and Montenegro's Albanian-speaking south.",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Ulcinj_Montenegro.jpg?width=1200", 64),
    ("&#381;abljak", "Highest town in the Balkans — gateway to Durmitor National Park and the Tara Canyon.",
     "https://commons.wikimedia.org/wiki/Special:FilePath/Zabljak,_Montenegro.jpg?width=1200", 31),
]

PARK_CARDS = [
    ("Durmitor National Park", "Glacial lakes, 48 peaks above 2,000 m, and the second-deepest canyon on Earth.",
     "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1400&auto=format&fit=crop"),
    ("Lov&#263;en National Park", "The black mountain that gave Montenegro its name. Drive the 25-hairpin road to Njegoš's mausoleum.",
     "https://images.unsplash.com/photo-1486494427891-2bcfb5b8f1ab?q=80&w=1400&auto=format&fit=crop"),
    ("Biogradska Gora", "One of the last three primeval forests in Europe — and a swimmable glacial lake at its centre.",
     "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=1400&auto=format&fit=crop"),
    ("Skadar Lake", "The largest lake in southern Europe. Vineyards, wetland birdlife, and stone fishing villages.",
     "https://images.unsplash.com/photo-1502301103665-0b95cc738daf?q=80&w=1400&auto=format&fit=crop"),
    ("Prokletije National Park", "The &quot;Cursed Mountains.&quot; Wild, lightly trafficked, and shared with Albania and Kosovo.",
     "https://images.unsplash.com/photo-1454942901704-3c44c11b2ad1?q=80&w=1400&auto=format&fit=crop"),
]

THINGS_TO_DO = [
    ("waves",  "Beaches",              "Mogren, Jaz, Plavi Horizonti, Veliki Pijesak — sandy coves to broad Adriatic strands."),
    ("hiking", "Hiking",               "Durmitor's Bobotov Kuk, Lov&#263;en's Štirovnik, the Peaks of the Balkans trail."),
    ("castle", "Old towns",            "Kotor, Budva Stari Grad, Perast, Stari Bar, Ulcinj's Kalaja citadel."),
    ("wine_bar","Wineries",            "Plantaže's Šipčanik wine cellar, Skadar Lake boutique producers."),
    ("paragliding","Adventure sports", "Tara River rafting, Lov&#263;en paragliding, canyoning in Nev&#380;asti."),
    ("local_dining","Local food",      "Njegoški pršut, Boka oysters, Lake Skadar carp, Negu&#353;ki sir cheese."),
]


def write_locations():
    body = hero(
        "Find your Montenegro",
        "A country smaller than Connecticut, packed with UNESCO old towns, glacier lakes, super-yacht marinas, and roads that genuinely belong on a postcard. Pick a base, pick up a car, and start driving.",
        "https://images.unsplash.com/photo-1591286574655-19eaf805d2ea?q=80&w=2000&auto=format&fit=crop",
        badge="Locations",
    )

    # Must-visit cities
    body += """
<section class="py-section-padding px-gutter">
  <div class="max-w-container-max mx-auto">
    <div class="mb-stack-lg">
      <h2 class="font-h2 text-h2 text-primary mb-stack-sm">Must-visit cities</h2>
      <p class="text-secondary font-body-md max-w-2xl">From the walled medieval towns of the coast to the modern capital inland, every city has its own character — and its own MontenegroDrive pick-up counter.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
"""
    for name, blurb, img, count in CITY_CARDS:
        body += f"""
      <a href="search.html" class="group bg-white rounded-xl shadow-ambient overflow-hidden border border-outline-variant/30 hover:shadow-lg transition-all">
        <div class="h-56 overflow-hidden bg-surface-container-low">
          <img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" alt="{name}" src="{img}"
               onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&amp;w=1200&amp;auto=format&amp;fit=crop'"/>
        </div>
        <div class="p-6">
          <h3 class="font-h3 text-h3 text-primary mb-2">{name}</h3>
          <p class="text-secondary text-body-md mb-4">{blurb}</p>
          <p class="text-body-sm text-primary flex items-center gap-2 font-label-bold">
            <span class="material-symbols-outlined text-[18px]">car_rental</span>
            {count} cars available
          </p>
        </div>
      </a>"""
    body += """
    </div>
  </div>
</section>
"""

    # National parks
    body += """
<section class="py-section-padding px-gutter bg-surface-container-low">
  <div class="max-w-container-max mx-auto">
    <div class="mb-stack-lg">
      <h2 class="font-h2 text-h2 text-primary mb-stack-sm">National parks</h2>
      <p class="text-secondary font-body-md max-w-2xl">Five protected areas cover almost 10% of the country. Most are within a two-hour drive of the coast — easy day trips with the right vehicle.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
"""
    for name, blurb, img in PARK_CARDS:
        body += f"""
      <div class="bg-white rounded-xl shadow-ambient overflow-hidden border border-outline-variant/30">
        <div class="h-48 overflow-hidden"><img class="w-full h-full object-cover" alt="{name}" src="{img}"/></div>
        <div class="p-6">
          <h3 class="font-h3 text-h3 text-primary mb-2">{name}</h3>
          <p class="text-secondary text-body-md">{blurb}</p>
        </div>
      </div>"""
    body += """
    </div>
  </div>
</section>
"""

    # Things to do
    body += """
<section class="py-section-padding px-gutter">
  <div class="max-w-container-max mx-auto">
    <div class="mb-stack-lg">
      <h2 class="font-h2 text-h2 text-primary mb-stack-sm">What to do</h2>
      <p class="text-secondary font-body-md max-w-2xl">However you like to travel, Montenegro has a version of it. Mix and match across coast, mountains and lakes within a single week.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
"""
    for icon, name, blurb in THINGS_TO_DO:
        body += f"""
      <div class="flex gap-4 p-6 bg-white rounded-xl shadow-sm border border-outline-variant/30 hover:shadow-md transition-all">
        <div class="w-12 h-12 flex-shrink-0 rounded-full bg-secondary-container text-primary flex items-center justify-center">
          <span class="material-symbols-outlined">{icon}</span>
        </div>
        <div>
          <h4 class="font-h3 text-[20px] text-primary mb-1">{name}</h4>
          <p class="text-body-sm text-secondary">{blurb}</p>
        </div>
      </div>"""
    body += """
    </div>
  </div>
</section>

<!-- CTA -->
<section class="py-section-padding px-gutter bg-primary text-on-primary">
  <div class="max-w-container-max mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
    <div>
      <h2 class="font-h2 text-h2 mb-stack-md">Pick a city. Pick a car. Go.</h2>
      <p class="font-body-lg text-white/85 mb-stack-lg">
        We have counters at every airport and major city in Montenegro, plus free pick-up from most coastal hotels. Free cancellation until 48 hours before pick-up.
      </p>
      <a href="search.html" class="bg-[#FF5722] hover:bg-[#E64A19] text-white px-8 py-4 rounded-lg font-label-bold shadow-lg inline-flex items-center gap-2">
        Find a car <span class="material-symbols-outlined">arrow_forward</span>
      </a>
    </div>
    <div class="grid grid-cols-2 gap-4">
      <div class="bg-white/10 backdrop-blur-sm border border-white/20 rounded-xl p-6">
        <p class="font-price-display text-price-display text-tertiary-fixed-dim mb-2">9</p>
        <p class="text-body-sm text-white/80">Pick-up cities</p>
      </div>
      <div class="bg-white/10 backdrop-blur-sm border border-white/20 rounded-xl p-6">
        <p class="font-price-display text-price-display text-tertiary-fixed-dim mb-2">5</p>
        <p class="text-body-sm text-white/80">National parks</p>
      </div>
      <div class="bg-white/10 backdrop-blur-sm border border-white/20 rounded-xl p-6">
        <p class="font-price-display text-price-display text-tertiary-fixed-dim mb-2">2,500+</p>
        <p class="text-body-sm text-white/80">Five-star reviews</p>
      </div>
      <div class="bg-white/10 backdrop-blur-sm border border-white/20 rounded-xl p-6">
        <p class="font-price-display text-price-display text-tertiary-fixed-dim mb-2">24/7</p>
        <p class="text-body-sm text-white/80">Multilingual support</p>
      </div>
    </div>
  </div>
</section>
"""

    html = head("Locations") + header(active="locations") + body + footer() + end()
    (OUT / "locations.html").write_text(html, encoding="utf-8")
    print("  ✓ locations.html")


# ----------------------------------------------------------------------
# Monte Club page
# ----------------------------------------------------------------------

def write_monte_club():
    body = hero(
        "Earn money with your idle car",
        "Monte Club is MontenegroDrive's partner programme. Do you have a car that you don't use? List it with us, we handle the customers, insurance, cleaning and maintenance — you collect a monthly payout.",
        "https://images.unsplash.com/photo-1503376780353-7e6692767b70?q=80&w=2000&auto=format&fit=crop",
        badge="Monte Club · Partner programme",
    )

    body += """
<!-- How it works -->
<section class="py-section-padding px-gutter">
  <div class="max-w-container-max mx-auto">
    <div class="text-center mb-stack-lg">
      <h2 class="font-h2 text-h2 text-primary mb-stack-sm">How it works</h2>
      <p class="text-secondary font-body-md max-w-xl mx-auto">Three steps, two visits to our office, and your car starts paying for itself.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white rounded-xl p-8 shadow-ambient border border-outline-variant/30 relative">
        <div class="absolute -top-5 -left-5 w-12 h-12 rounded-full bg-[#FF5722] text-white font-h3 text-h3 flex items-center justify-center shadow-lg">1</div>
        <h3 class="font-h3 text-h3 text-primary mb-3 mt-2">Apply online</h3>
        <p class="text-secondary text-body-md">Fill out the short form below with your car's details. We'll get back within 48 hours with an estimated monthly earning range based on category, age and pick-up city.</p>
      </div>
      <div class="bg-white rounded-xl p-8 shadow-ambient border border-outline-variant/30 relative">
        <div class="absolute -top-5 -left-5 w-12 h-12 rounded-full bg-[#FF5722] text-white font-h3 text-h3 flex items-center justify-center shadow-lg">2</div>
        <h3 class="font-h3 text-h3 text-primary mb-3 mt-2">Bring the car in</h3>
        <p class="text-secondary text-body-md">Drop the car at our Podgorica or Tivat office. We do a full inspection, photograph it for the fleet, hand you the partner agreement, and add the vehicle to availability.</p>
      </div>
      <div class="bg-white rounded-xl p-8 shadow-ambient border border-outline-variant/30 relative">
        <div class="absolute -top-5 -left-5 w-12 h-12 rounded-full bg-[#FF5722] text-white font-h3 text-h3 flex items-center justify-center shadow-lg">3</div>
        <h3 class="font-h3 text-h3 text-primary mb-3 mt-2">Get paid monthly</h3>
        <p class="text-secondary text-body-md">We pay 65% of net rental income on the 5th of each month, straight to your bank account, with a detailed booking-by-booking statement. Cancel any month with 30 days' notice.</p>
      </div>
    </div>
  </div>
</section>

<!-- Benefits -->
<section class="py-section-padding px-gutter bg-surface-container-low">
  <div class="max-w-container-max mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
    <div>
      <h2 class="font-h2 text-h2 text-primary mb-stack-md">Why partner with us?</h2>
      <p class="font-body-lg text-secondary mb-stack-lg">
        Owning a car in Montenegro is expensive — insurance, technical inspection, parking, the road tax. Monte Club turns that cost centre into a revenue stream while we shoulder the operational work.
      </p>
      <ul class="space-y-4">
"""
    for icon, title, desc in [
        ("shield",       "Full insurance, on us",     "Comprehensive coverage including zero-excess collision and theft — at no cost to you."),
        ("local_car_wash","Cleaning &amp; maintenance",   "Every return: deep clean, fluids check, tyre pressure. Service intervals tracked and paid for."),
        ("euro_symbol",  "Transparent monthly payouts","65/35 revenue share, detailed statement, paid on the 5th — no withholdings, no hidden deductions."),
        ("calendar_month","Block your own dates",     "Need the car for a weekend? Block dates in the partner portal and the listing pauses automatically."),
        ("verified_user","Verified, vetted renters",  "Every driver passes our document and credit-card checks before they get the keys to your vehicle."),
    ]:
        body += f"""
        <li class="flex gap-4 items-start">
          <span class="material-symbols-outlined text-primary bg-secondary-container p-2 rounded-lg flex-shrink-0">{icon}</span>
          <div>
            <p class="font-label-bold text-primary text-base">{title}</p>
            <p class="text-body-sm text-secondary">{desc}</p>
          </div>
        </li>"""
    body += """
      </ul>
    </div>
    <div class="bg-primary text-on-primary rounded-2xl p-10 shadow-2xl">
      <span class="text-body-sm uppercase tracking-widest text-tertiary-fixed-dim">Indicative monthly earnings</span>
      <p class="font-price-display text-[64px] leading-none text-white font-bold mt-2 mb-stack-md">€450–950</p>
      <p class="text-white/80 mb-stack-lg">Per economy-segment car, per month, based on 2024 partner statements. Premium and SUV categories earn more.</p>
      <div class="grid grid-cols-3 gap-4 text-center">
        <div class="bg-white/10 rounded-lg p-4">
          <p class="text-tertiary-fixed-dim font-h3 text-h3">82%</p>
          <p class="text-body-sm text-white/75 mt-1">Average occupancy May–Oct</p>
        </div>
        <div class="bg-white/10 rounded-lg p-4">
          <p class="text-tertiary-fixed-dim font-h3 text-h3">€0</p>
          <p class="text-body-sm text-white/75 mt-1">Up-front cost to join</p>
        </div>
        <div class="bg-white/10 rounded-lg p-4">
          <p class="text-tertiary-fixed-dim font-h3 text-h3">30d</p>
          <p class="text-body-sm text-white/75 mt-1">Notice to cancel, no penalty</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Application form -->
<section class="py-section-padding px-gutter">
  <div class="max-w-3xl mx-auto">
    <div class="text-center mb-stack-lg">
      <h2 class="font-h2 text-h2 text-primary mb-stack-sm">Apply now</h2>
      <p class="text-secondary font-body-md">Takes about 3 minutes. We respond within 48 hours.</p>
    </div>
    <form class="bg-white p-8 rounded-xl shadow-ambient flex flex-col gap-4 border border-outline-variant/30">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Full name</span>
          <input type="text" required class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Phone (with country code)</span>
          <input type="tel" required placeholder="+382 ..." class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
      </div>
      <label class="flex flex-col gap-2">
        <span class="font-label-bold text-on-surface-variant text-sm">Email</span>
        <input type="email" required class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
      </label>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Car make</span>
          <input type="text" required placeholder="e.g. Volkswagen" class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Car model</span>
          <input type="text" required placeholder="e.g. Polo" class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Year</span>
          <input type="number" min="2010" max="2025" required class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Pick-up city</span>
          <select class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary bg-white">
            <option>Podgorica</option>
            <option>Tivat</option>
            <option>Budva</option>
            <option>Kotor</option>
            <option>Bar</option>
            <option>Herceg Novi</option>
          </select>
        </label>
        <label class="flex flex-col gap-2">
          <span class="font-label-bold text-on-surface-variant text-sm">Approx. days available per month</span>
          <input type="number" min="1" max="31" placeholder="20" class="h-12 px-4 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary"/>
        </label>
      </div>
      <label class="flex flex-col gap-2">
        <span class="font-label-bold text-on-surface-variant text-sm">Anything else we should know?</span>
        <textarea rows="4" class="px-4 py-3 rounded-lg border border-outline-variant focus:border-primary focus:ring-1 focus:ring-primary resize-y"></textarea>
      </label>
      <label class="flex items-start gap-3 text-body-sm text-secondary">
        <input type="checkbox" required class="mt-1 rounded border-outline-variant"/>
        <span>I confirm I am the legal owner of this vehicle and agree to the Monte Club partner terms.</span>
      </label>
      <button type="submit" class="bg-[#FF5722] hover:bg-[#E64A19] text-white font-label-bold h-14 rounded-lg shadow-lg uppercase tracking-wide">
        Submit application
      </button>
    </form>
  </div>
</section>
"""

    html = head("Monte Club") + header() + body + footer() + end()
    (OUT / "monte-club.html").write_text(html, encoding="utf-8")
    print("  ✓ monte-club.html")


# ----------------------------------------------------------------------
# Travel guide article pages
# ----------------------------------------------------------------------

def article_template(*, slug, title, eyebrow, lede, hero_img, body_blocks, related):
    """Build a magazine-style article page."""
    body = f"""
<article>
  <section class="relative h-[520px] flex items-end overflow-hidden">
    <div class="absolute inset-0 z-0">
      <img class="w-full h-full object-cover" alt="" src="{hero_img}"/>
      <div class="absolute inset-0 bg-gradient-to-t from-primary/95 via-primary/40 to-primary/10"></div>
    </div>
    <div class="relative z-10 max-w-container-max mx-auto px-gutter w-full pb-stack-lg">
      <span class="inline-block bg-secondary-container text-on-secondary-container px-3 py-1 rounded-md text-body-sm font-label-bold uppercase tracking-wider mb-stack-md">{eyebrow}</span>
      <h1 class="font-h1 text-h1 text-white max-w-4xl mb-stack-md drop-shadow-md">{title}</h1>
      <p class="text-white/85 font-body-lg max-w-2xl">{lede}</p>
      <div class="flex items-center gap-6 mt-stack-md text-white/80 text-body-sm">
        <span class="flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">edit</span> By MontenegroDrive Editorial</span>
        <span class="flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">schedule</span> 8 min read</span>
      </div>
    </div>
  </section>

  <div class="max-w-3xl mx-auto px-gutter py-section-padding">
    <a href="travel-guide.html" class="text-primary font-label-bold flex items-center gap-2 mb-stack-lg hover:gap-3 transition-all">
      <span class="material-symbols-outlined text-[18px]">arrow_back</span> Back to Travel Guide
    </a>
    {''.join(body_blocks)}

    <div class="mt-stack-lg pt-stack-lg border-t border-outline-variant/40 flex flex-col sm:flex-row justify-between items-start gap-4">
      <div>
        <p class="font-label-bold text-primary mb-1">Ready to drive it yourself?</p>
        <p class="text-body-sm text-secondary">Get a car at any of our 9 pick-up locations across Montenegro.</p>
      </div>
      <a href="search.html" class="bg-[#FF5722] hover:bg-[#E64A19] text-white font-label-bold px-6 py-3 rounded-lg shadow-lg">Find a car</a>
    </div>
  </div>

  <section class="py-section-padding px-gutter bg-surface-container-low">
    <div class="max-w-container-max mx-auto">
      <h2 class="font-h2 text-h2 text-primary mb-stack-lg">Continue reading</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {related}
      </div>
    </div>
  </section>
</article>
"""
    html = head(title) + header(active="travel") + body + footer() + end()
    (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
    print(f"  ✓ {slug}.html")


def p(text): return f'<p class="text-body-lg text-on-surface-variant leading-relaxed mb-stack-md">{text}</p>'
def h(text, lvl=2): return f'<h{lvl} class="font-h{lvl} text-h{lvl} text-primary mt-stack-lg mb-stack-md">{text}</h{lvl}>'
def li_block(items):
    out = '<ul class="space-y-3 mb-stack-md">'
    for txt in items:
        out += f'<li class="flex gap-3 items-start"><span class="material-symbols-outlined text-primary mt-1">check_circle</span><span class="text-body-md text-on-surface-variant leading-relaxed">{txt}</span></li>'
    return out + '</ul>'

def tip(num, title, body):
    return f"""
    <div class="bg-white rounded-xl p-6 mb-stack-md border border-outline-variant/30 shadow-sm">
      <div class="flex items-baseline gap-3 mb-2">
        <span class="font-h3 text-h3 text-brand-accent font-bold">#{num:02d}</span>
        <h3 class="font-h3 text-[20px] text-primary">{title}</h3>
      </div>
      <p class="text-body-md text-on-surface-variant leading-relaxed">{body}</p>
    </div>"""

def quote(text, attrib=""):
    a = f'<footer class="mt-3 text-body-sm text-secondary not-italic">— {attrib}</footer>' if attrib else ''
    return f"""
    <blockquote class="border-l-4 border-brand-accent bg-secondary-container/30 p-6 my-stack-lg italic text-h3 text-[20px] text-primary">
      {text}
      {a}
    </blockquote>"""


# Mini related-article card factory.
def related_card(href, title, excerpt, img):
    return f"""
        <a href="{href}" class="group bg-white rounded-xl overflow-hidden shadow-sm border border-outline-variant/30 hover:shadow-md transition-all block">
          <div class="aspect-video overflow-hidden"><img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" alt="" src="{img}"/></div>
          <div class="p-5">
            <h4 class="font-h3 text-[18px] text-primary mb-2">{title}</h4>
            <p class="text-body-sm text-secondary">{excerpt}</p>
          </div>
        </a>"""


def write_articles():
    # ---- 10 Tips for Your Montenegro Road Trip (long-form) -----------
    tip_blocks = "".join([
        tip(1, "Bring an International Driving Permit",
            "EU and UK licences are fine on their own. North American, Australian, Asian and most other licences should be paired with an IDP — it's not strictly enforced at pick-up but the police can fine you €70 at a roadside check."),
        tip(2, "Fuel up before the mountain roads",
            "Petrol stations cluster along the coast and the E80. Above 1,000 m elevation — Durmitor, Lov&#263;en, the Tara Canyon — they become rare. Fill up in &#381;abljak or Pluzine before heading into Durmitor."),
        tip(3, "Respect the serpentine roads",
            "The Kotor–Cetinje road has 25 hairpin turns in 8 km. The road to Sveti Stefan is narrow and shared with tour buses. Take it slow, hug the inside of blind corners, and use the horn before tight bends — locals do."),
        tip(4, "Best viewpoints worth the detour",
            "Lov&#263;en's Štirovnik summit, the Vidikovac restaurant above Kotor, the Pavlova Strana hairpin on the Skadar road, and Sveti Jovan above Budva for sunset over the old town."),
        tip(5, "Old town parking is restricted",
            "You cannot drive into Kotor, Budva or Perast old towns. Use the paid car parks just outside the walls — €1–3 per hour, €15–25 per day in peak season. Free street parking exists 10 minutes' walk away."),
        tip(6, "Watch for the Sozina Tunnel toll",
            "The 4.2 km Sozina Tunnel cuts the Podgorica–Bar drive by 30 minutes. €3.50 per car each way — keep small notes ready or use the contactless lane."),
        tip(7, "Cross the Bay of Kotor by ferry",
            "The Kamenari–Lepetane ferry saves an hour over driving around the bay. €5 per car including driver, runs every 15 minutes 24/7, no booking needed. Just pay the attendant on the ramp."),
        tip(8, "Border crossings: pick your moment",
            "Debeli Brijeg (Croatia) backs up to 90 minutes in July–August. Cross before 9am or after 8pm. The Albanian border at Sukobin and Bosnian crossings at Šćepan Polje rarely have queues."),
        tip(9, "Save these phone numbers",
            "Police 122. Ambulance 124. AMS roadside assistance 19807 (works anywhere in Montenegro, English support). MontenegroDrive 24/7 line: +382 20 123 456."),
        tip(10, "The under-rated stops",
            "The Old Royal Capital Cetinje (museums, 30 min from Kotor). The Ostrog monastery carved into a cliff face (1 hour from Podgorica). Lake Skadar's Rijeka Crnojevi&#263;a viewpoint at dusk. Add at least one to your itinerary."),
    ])

    article_template(
        slug="article-road-trip-tips",
        title="10 Tips for Your Montenegro Road Trip",
        eyebrow="Guide · 8 min read",
        lede="From hidden gas stations to the most beautiful viewpoints along the coast — everything we wish someone had told us before our first drive through Montenegro.",
        hero_img="https://images.unsplash.com/photo-1502301103665-0b95cc738daf?q=80&w=2000&auto=format&fit=crop",
        body_blocks=[
            p("Montenegro is 13,800 km² — about the size of Connecticut, or roughly a fifth of Tasmania. You can drive from the Adriatic coast to a 2,000-metre summit in under two hours, cross into three different countries before lunch, and finish the day swimming in a glacial lake. The catch is that the roads weren't built for tourists; they were built for goats."),
            p("Here are the ten things we tell every customer the moment they pick up their keys at our Tivat or Podgorica counter."),
            *tip_blocks.split("</div>")[:-1],  # already-built tip blocks
        ] if False else [  # use the joined block directly instead
            p("Montenegro is 13,800 km² — about the size of Connecticut, or roughly a fifth of Tasmania. You can drive from the Adriatic coast to a 2,000-metre summit in under two hours, cross into three different countries before lunch, and finish the day swimming in a glacial lake. The catch is that the roads weren't built for tourists; they were built for goats."),
            p("Here are the ten things we tell every customer the moment they pick up their keys at our Tivat or Podgorica counter."),
            tip_blocks,
            quote("If you only remember one thing: in Montenegro the road IS the destination. Build extra time into every leg.", "Marko, MontenegroDrive head of operations"),
            h("Before you set off"),
            li_block([
                "Download offline maps for the whole country — mobile coverage drops in canyons.",
                "Photograph the car at pick-up (all four corners + the dashboard) so any pre-existing scratches are documented.",
                "Note your booking reference and our 24/7 line in your phone.",
                "Keep €30 in coins for tolls, parking and ferry fares.",
            ]),
            p("Drive safe — and send us a photo from your favourite viewpoint."),
        ],
        related="".join([
            related_card("article-panoramic-routes.html", "Best Panoramic Routes in Europe", "Eight scenic drives that genuinely earn the cliché.",
                         "https://images.unsplash.com/photo-1566127992631-137a642a90f4?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-driving-rules.html", "Driving in Montenegro: What You Need to Know", "Speed limits, alcohol policy, road conditions.",
                         "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-prokletije.html", "Prokletije: The Cursed Mountains", "A 4x4 guide to the Balkans' most dramatic range.",
                         "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200&auto=format&fit=crop"),
        ]),
    )

    # ---- Best Panoramic Routes in Europe -----------------------------
    article_template(
        slug="article-panoramic-routes",
        title="Best Panoramic Routes in Europe",
        eyebrow="Routes · 7 min read",
        lede="Eight scenic drives that genuinely earn the cliché — four in Montenegro, four within easy reach across the border.",
        hero_img="https://images.unsplash.com/photo-1566127992631-137a642a90f4?q=80&w=2000&auto=format&fit=crop",
        body_blocks=[
            p("The eastern Adriatic has more panoramic road per kilometre than almost anywhere in Europe. Limestone karst, glacial valleys and a coastline that pleats back on itself mean every drive is a slow reveal. These are the eight we put on a printed itinerary for our customers, ranked by jaw-drop ratio."),
            h("1. Kotor → Cetinje serpentine"),
            p("Twenty-five hairpins climbing 900 m in 8 km. Park at the third lookout for the bay-and-old-town shot you've seen on every postcard. Allow 90 minutes round-trip from Kotor — not because of distance, but because of the photo stops."),
            h("2. Lov&#263;en ring (Cetinje → Njegoš Mausoleum → Ivanova Korita)"),
            p("A 35 km loop through Lov&#263;en National Park. Climb the 461 steps to Petar II Petrović-Njegoš's mausoleum at 1,657 m for a 360° view that covers half the country on a clear day."),
            h("3. Sveti Stefan coastal drive"),
            p("The 9 km between Budva and Petrovac threads above a string of pink-sand coves. Park at the Sveti Stefan viewpoint pull-out for the famous fortified-island shot."),
            h("4. Durmitor Ring Road (P-14)"),
            p("Eighty-two kilometres of single-lane mountain road inside Durmitor National Park. Black Lake, Sušica Canyon, the Tara River bridge — budget half a day."),
            h("5. Mali Ston → Dubrovnik (Croatia)"),
            p("Sixty kilometres of Dalmatian coast with the Pelješac peninsula on one side and the Elaphiti islands on the other. Cross the border at Karasovi&#263;i; queues are short outside July–August."),
            h("6. The Tara Canyon road (Šćepan Polje → Žabljak)"),
            p("Europe's deepest canyon (1,300 m) with the road carved into one wall. Stop at the Tara Bridge — it was blown up in 1942, rebuilt, and you can bungee-jump from it now."),
            h("7. Logarska Dolina (Slovenia)"),
            p("A 7 km glacial valley reachable in a day from northern Montenegro. The road dead-ends at the Rinka waterfall — 90 m straight down."),
            h("8. Llogara Pass (Albania)"),
            p("The road from Vlorë to Saranda crosses the 1,027 m Llogara Pass. From the top: Greek islands on one side, the Albanian Riviera on the other. Three hours from Ulcinj."),
            quote("On the Lov&#263;en road I had to pull over twice because my passenger kept gasping. That's the marker of a good drive."),
        ],
        related="".join([
            related_card("article-road-trip-tips.html", "10 Tips for Your Montenegro Road Trip", "Everything from gas stations to viewpoints.",
                         "https://images.unsplash.com/photo-1502301103665-0b95cc738daf?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-driving-rules.html", "Driving in Montenegro: What You Need to Know", "Speed limits, alcohol policy, road conditions.",
                         "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-komovi.html", "The Circular Komovi Route", "A perfect mix of forest trails and limestone rock crawls.",
                         "https://images.unsplash.com/photo-1454942901704-3c44c11b2ad1?q=80&w=1200&auto=format&fit=crop"),
        ]),
    )

    # ---- Driving in Montenegro: What You Need to Know ---------------
    article_template(
        slug="article-driving-rules",
        title="Driving in Montenegro: What You Need to Know",
        eyebrow="Safety guide · 6 min read",
        lede="The rules of the road, in plain English. What the police will and won't fine you for, and what to do if something goes wrong.",
        hero_img="https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=2000&auto=format&fit=crop",
        body_blocks=[
            p("Montenegro drives on the right. Most rules will feel familiar to anyone who has driven in mainland Europe. There are, however, a few local quirks that catch people out — and a handful of fines that can spoil a trip."),
            h("Licence requirements"),
            li_block([
                "EU/EEA/UK licence: valid as-is, no IDP required.",
                "Most other licences: bring your national licence AND an International Driving Permit (IDP). The IDP must be the 1949 Geneva or 1968 Vienna convention type.",
                "Minimum driving age: 18. Most rental categories require 21+ with one year of licence history; luxury categories require 25+.",
            ]),
            h("Speed limits"),
            li_block([
                "Urban: 50 km/h (sometimes signed 40 in residential zones).",
                "Open road: 80 km/h.",
                "Expressway (M-2 Podgorica–Mateševo): 100 km/h.",
                "Adriatic Highway (E-80): 80 km/h except where signed otherwise.",
            ]),
            p("Speed cameras are common on the E-80 and around Podgorica. Fines start at €40 for up to 20 km/h over, rising to €200 + court summons above that."),
            h("Alcohol policy"),
            p("Blood alcohol limit is 0.03% — effectively a one-drink limit. For new drivers (licence under 2 years) and professional drivers, the limit is zero. Random roadside breath tests are routine on Friday and Saturday nights."),
            h("Required equipment"),
            li_block([
                "Reflective vest (one per passenger).",
                "Warning triangle.",
                "First-aid kit.",
                "Spare bulb set.",
                "Tow rope.",
                "Snow chains (Nov 15 – Apr 15 if travelling above 700 m, regardless of road conditions).",
            ]),
            p("All MontenegroDrive vehicles come with the full required kit in the boot. Check it's there before driving off."),
            h("Insurance &amp; the Green Card"),
            p("Your rental includes mandatory third-party (TPL) insurance and a Collision Damage Waiver. The Green Card is mandatory for cross-border driving in Croatia, BiH, Albania, Slovenia and onwards — we include it free of charge if you tell us at pick-up. Kosovo is excluded entirely; you must rent there separately."),
            h("Road conditions"),
            p("The coastal Adriatic Highway and the new M-2 Bar–Boljare expressway (currently open Podgorica–Mateševo) are smooth two- and three-lane highways. The Lov&#263;en road, the Durmitor Ring and most roads above 800 m are narrow, single-lane and locally maintained. After winter, expect potholes until late May."),
            h("What to do if you have an accident"),
            li_block([
                "Stop, switch hazards on, deploy the warning triangle 50 m back.",
                "Photograph everything — both vehicles, plates, surroundings, damage close-ups.",
                "Call police (122) if anyone is injured or vehicles can't move under their own power.",
                "Exchange details with the other driver: full name, address, licence number, insurance.",
                "Call us on +382 20 123 456 — we'll coordinate next steps, including a replacement vehicle if needed.",
            ]),
            quote("90% of customer drama on Montenegrin roads is parking fines in old towns. Read the blue/yellow line colour code before you walk away from the car."),
        ],
        related="".join([
            related_card("article-road-trip-tips.html", "10 Tips for Your Montenegro Road Trip", "Everything from gas stations to viewpoints.",
                         "https://images.unsplash.com/photo-1502301103665-0b95cc738daf?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-panoramic-routes.html", "Best Panoramic Routes in Europe", "Eight scenic drives that earn the cliché.",
                         "https://images.unsplash.com/photo-1566127992631-137a642a90f4?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-sinjajevina.html", "The Sinjajevina Highlands", "Europe's second-largest mountain pasture.",
                         "https://images.unsplash.com/photo-1486494427891-2bcfb5b8f1ab?q=80&w=1200&auto=format&fit=crop"),
        ]),
    )

    # ---- Prokletije: The Cursed Mountains ----------------------------
    article_template(
        slug="article-prokletije",
        title="Prokletije: The Cursed Mountains",
        eyebrow="4x4 route · 5 min read",
        lede="A 60 km circuit through the wildest range in the Balkans. Suitable for a high-clearance SUV with low-range gearing.",
        hero_img="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2000&auto=format&fit=crop",
        body_blocks=[
            p("Prokletije — &quot;the cursed&quot; in Serbo-Croatian — straddles Montenegro, Albania and Kosovo. It's the southernmost and most rugged section of the Dinaric Alps, with vertical limestone walls dropping straight from 2,500 m summits into glacial cirques. There are no cable cars, two paved roads, and a population density of roughly four people per square kilometre."),
            h("The route"),
            p("Start in Plav (1,000 m), drive 12 km of paved road up to the village of Vusanje, then turn onto the gravel forestry road towards the Albanian border. The track climbs through beech forest to the Bjeluha pasture (1,840 m), drops into the Ropojana valley, and exits back into Plav via Gusinje. Total distance 58 km, total time 4–5 hours with stops."),
            h("Vehicle requirements"),
            li_block([
                "High clearance (200 mm+).",
                "Low-range transfer case — there is one rocky climb where you'll need first-gear-low.",
                "All-terrain tyres preferred over road tyres.",
                "Spare wheel mounted and inflated.",
            ]),
            p("From the MontenegroDrive fleet: Dacia Duster 4x4, Suzuki Jimny, Jeep Renegade Trailhawk. The Polo and front-wheel-drive crossovers are not suitable."),
            h("Stops worth making"),
            li_block([
                "Volušnica lookout (Vusanje) — first view of the Karanfili wall.",
                "Grebaje valley meadow — alpine wildflowers, June only.",
                "The Ali-paša springs — turquoise water out of the rock face, swim if you dare (4°C).",
                "Ropojana wild horse herd — usually grazing the upper meadow late afternoon.",
            ]),
            h("Practical notes"),
            p("You're driving along the Albanian border for 8 km — keep your passport and rental documents in the door pocket. There is no fuel between Plav and Gusinje (35 km apart). Mobile coverage drops between Vusanje and Ropojana for about 90 minutes; download offline maps. Don't attempt this route between November and May — the upper sections are under snow."),
        ],
        related="".join([
            related_card("article-sinjajevina.html", "The Sinjajevina Highlands", "Europe's second-largest mountain pasture.",
                         "https://images.unsplash.com/photo-1486494427891-2bcfb5b8f1ab?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-komovi.html", "The Circular Komovi Route", "Forest trails and limestone rock crawls.",
                         "https://images.unsplash.com/photo-1454942901704-3c44c11b2ad1?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-driving-rules.html", "Driving in Montenegro", "Rules, speed limits, and what to do if something goes wrong.",
                         "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1200&auto=format&fit=crop"),
        ]),
    )

    # ---- The Sinjajevina Highlands -----------------------------------
    article_template(
        slug="article-sinjajevina",
        title="The Sinjajevina Highlands",
        eyebrow="4x4 route · 5 min read",
        lede="Europe's second-largest mountain pasture: 120 km² of rolling alpine plateau, ancient shepherd huts, and almost no other cars.",
        hero_img="https://images.unsplash.com/photo-1486494427891-2bcfb5b8f1ab?q=80&w=2000&auto=format&fit=crop",
        body_blocks=[
            p("If Durmitor is Montenegro's celebrity mountain, Sinjajevina is its understudy. Same elevation, same scale, a tenth of the visitors. The reason: there's exactly one paved road through it, and it's a dead end."),
            h("The route"),
            p("From the village of Boan (Kola&#353;in side, 1,300 m), the asphalt ends and a graded gravel track climbs onto the plateau. The road runs north-east for 22 km across the pasture before it peters out at a shepherd hut cluster on the Pošćenska Jezera lakes. Turn back the way you came — total distance 50 km round-trip, 3 hours."),
            h("What to expect"),
            li_block([
                "Wide-open grassland at 1,700–1,800 m, dotted with limestone outcrops.",
                "Working shepherd huts (katuni) selling fresh cheese and yoghurt in summer.",
                "Wild horses, sheep flocks, and the occasional bear track (unlikely encounter).",
                "Endless wildflower meadows in late June and July.",
                "Cold, clean air. Bring a fleece even in August.",
            ]),
            h("Vehicle requirements"),
            p("Any all-wheel-drive vehicle with decent clearance is fine. The road is graded for the shepherds and stays dry from June through October. After heavy rain, sections get washboard-rough but never impassable."),
            h("Practical notes"),
            p("Pošćenska Jezera (Pošćenje Lakes) are a chain of three glacial lakes at the end of the route. You can swim in the largest one — it warms to 18°C by August. There's a small fee (€2) to the shepherds for parking near their huts; pay it cheerfully, it's appreciated. Pack lunch — there is nothing commercial up there."),
            quote("Sinjajevina has been proposed as Montenegro's sixth national park for two decades. Until that happens, it's a national secret."),
        ],
        related="".join([
            related_card("article-prokletije.html", "Prokletije: The Cursed Mountains", "A 4x4 guide to the wildest range in the Balkans.",
                         "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-komovi.html", "The Circular Komovi Route", "Forest trails and limestone rock crawls.",
                         "https://images.unsplash.com/photo-1454942901704-3c44c11b2ad1?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-panoramic-routes.html", "Best Panoramic Routes in Europe", "Eight scenic drives that earn the cliché.",
                         "https://images.unsplash.com/photo-1566127992631-137a642a90f4?q=80&w=1200&auto=format&fit=crop"),
        ]),
    )

    # ---- The Circular Komovi Route -----------------------------------
    article_template(
        slug="article-komovi",
        title="The Circular Komovi Route",
        eyebrow="4x4 route · 5 min read",
        lede="Three of Montenegro's most photogenic peaks, a perfect mix of forest trails and limestone rock crawls, all in a single 48 km loop.",
        hero_img="https://images.unsplash.com/photo-1454942901704-3c44c11b2ad1?q=80&w=2000&auto=format&fit=crop",
        body_blocks=[
            p("The Komovi massif sits in eastern Montenegro between Andrijevica and Kola&#353;in. Three peaks dominate: Kom Vasojevi&#263;ki (2,461 m), Kom Kuča&#269;ki (2,487 m), and the smaller Lje&#353;tanski Kom. The circular route hits the saddle between all three, with two lookout detours that add maybe 30 minutes each."),
            h("The route"),
            p("Start in Andrijevica. Take the paved road towards &#352;tavna (8 km, sealed). At the &#352;tavna katun, turn right onto the gravel forestry road. The road climbs to the Carine saddle (1,950 m), drops into the &#352;ekular valley, and rejoins the asphalt at Trepča. Total 48 km, 3.5 hours, no significant exposure."),
            h("Two recommended detours"),
            li_block([
                "Vasojevi&#263;ki Kom summit hike: from the Carine saddle, a 90-minute marked walk to the top of the most popular Komovi peak.",
                "Eko-katun Štavna: working cheese-makers' settlement at 1,800 m. Stop for &#382;u&#263;enica salad and rakija.",
            ]),
            h("Vehicle requirements"),
            p("All-wheel drive recommended but not strictly required — the route is doable in a 2WD crossover during dry summer conditions. Avoid after sustained rain. Any of our SUV-category vehicles (Duster, RAV4, Renegade) will handle it comfortably."),
            h("When to go"),
            p("June through September. The katuni are operational from late May to early October. Snow blocks the saddle from November onwards and well into May."),
            p("Pair this route with a night in Andrijevica or Plav — both have small family-run hotels under €60/night, and you're well-placed to tackle the Prokletije route the next morning."),
        ],
        related="".join([
            related_card("article-prokletije.html", "Prokletije: The Cursed Mountains", "A 4x4 guide to the wildest range in the Balkans.",
                         "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-sinjajevina.html", "The Sinjajevina Highlands", "Europe's second-largest mountain pasture.",
                         "https://images.unsplash.com/photo-1486494427891-2bcfb5b8f1ab?q=80&w=1200&auto=format&fit=crop"),
            related_card("article-road-trip-tips.html", "10 Tips for Your Montenegro Road Trip", "Everything from gas stations to viewpoints.",
                         "https://images.unsplash.com/photo-1502301103665-0b95cc738daf?q=80&w=1200&auto=format&fit=crop"),
        ]),
    )


# ----------------------------------------------------------------------
# Legal page (single page with anchors)
# ----------------------------------------------------------------------

def write_legal():
    body = """
<section class="py-section-padding px-gutter max-w-4xl mx-auto">
  <h1 class="font-h1 text-h1 text-primary mb-stack-lg">Legal</h1>
  <nav class="mb-stack-lg flex flex-wrap gap-3">
    <a href="#privacy" class="px-4 py-2 rounded-full bg-secondary-container text-on-secondary-container font-label-bold hover:bg-primary hover:text-on-primary transition-all">Privacy Policy</a>
    <a href="#terms" class="px-4 py-2 rounded-full bg-secondary-container text-on-secondary-container font-label-bold hover:bg-primary hover:text-on-primary transition-all">Terms of Service</a>
    <a href="#cookies" class="px-4 py-2 rounded-full bg-secondary-container text-on-secondary-container font-label-bold hover:bg-primary hover:text-on-primary transition-all">Cookie Policy</a>
  </nav>

  <article id="privacy" class="mb-section-padding">
    <h2 class="font-h2 text-h2 text-primary mb-stack-md">Privacy Policy</h2>
    <p class="text-body-lg text-on-surface-variant mb-stack-md leading-relaxed">Last updated: 1 January 2024.</p>
    <p class="text-body-md text-on-surface-variant mb-stack-md leading-relaxed">MontenegroDrive d.o.o. (&quot;we&quot;, &quot;us&quot;) processes personal data in line with the General Data Protection Regulation (GDPR), Montenegro's Law on Personal Data Protection (Official Gazette 79/08), and our own internal data-handling standards. This policy explains what we collect, why, who we share it with, and how to exercise your rights.</p>
    <h3 class="font-h3 text-h3 text-primary mt-stack-lg mb-stack-sm">What we collect</h3>
    <p class="text-body-md text-on-surface-variant mb-stack-md leading-relaxed">Booking-related personal data (full name, date of birth, address, phone, email, driver's licence number and expiry, payment card details), vehicle telematics (location, mileage, fuel level — for fleet operations only), and website analytics (anonymised IP, browser, pages viewed).</p>
    <h3 class="font-h3 text-h3 text-primary mt-stack-lg mb-stack-sm">Your rights</h3>
    <p class="text-body-md text-on-surface-variant mb-stack-md leading-relaxed">You may request access to, correction of, or deletion of your data at any time by emailing <a href="mailto:privacy@montenegrodrive.example" class="text-primary underline">privacy@montenegrodrive.example</a>. We respond within 30 days. You also have the right to lodge a complaint with the Montenegrin Agency for Personal Data Protection.</p>
  </article>

  <article id="terms" class="mb-section-padding">
    <h2 class="font-h2 text-h2 text-primary mb-stack-md">Terms of Service</h2>
    <p class="text-body-lg text-on-surface-variant mb-stack-md leading-relaxed">By making a booking with MontenegroDrive you agree to the following terms. The full rental agreement is provided in writing at the time of vehicle collection.</p>
    <h3 class="font-h3 text-h3 text-primary mt-stack-lg mb-stack-sm">Bookings and cancellations</h3>
    <p class="text-body-md text-on-surface-variant mb-stack-md leading-relaxed">All bookings are confirmed upon receipt of the deposit. Free cancellation until 48 hours before scheduled pick-up time. Cancellations inside the 48-hour window are charged at one day's rental rate.</p>
    <h3 class="font-h3 text-h3 text-primary mt-stack-lg mb-stack-sm">Driver requirements</h3>
    <p class="text-body-md text-on-surface-variant mb-stack-md leading-relaxed">Minimum driver age 21 with at least 1 year of valid driving licence. Luxury and premium categories: 25+ with 2+ years. International Driving Permit required for non-EU/UK licences. Additional drivers must be registered on the contract.</p>
    <h3 class="font-h3 text-h3 text-primary mt-stack-lg mb-stack-sm">Liability</h3>
    <p class="text-body-md text-on-surface-variant mb-stack-md leading-relaxed">The renter is liable for damage up to the excess amount stated on the rental agreement. Full-insurance options remove this liability for collision and theft (negligence excluded).</p>
  </article>

  <article id="cookies">
    <h2 class="font-h2 text-h2 text-primary mb-stack-md">Cookie Policy</h2>
    <p class="text-body-md text-on-surface-variant mb-stack-md leading-relaxed">We use three categories of cookies: <strong>essential</strong> (booking session, language preference — required, cannot be disabled), <strong>analytics</strong> (Plausible.io — anonymised, opt-in), and <strong>marketing</strong> (Meta and Google retargeting — opt-in only). You can manage your preferences via the cookie banner shown on your first visit, or by clearing cookies and reloading the site.</p>
  </article>
</section>
"""
    html = head("Legal") + header() + body + footer() + end()
    (OUT / "legal.html").write_text(html, encoding="utf-8")
    print("  ✓ legal.html")


def main():
    print("Generating pages...")
    write_support()
    write_manage_booking()
    write_locations()
    write_monte_club()
    write_articles()
    write_legal()
    print("Done.")


if __name__ == "__main__":
    main()
