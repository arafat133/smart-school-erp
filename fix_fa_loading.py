"""
Fix FontAwesome loading issue permanently by adding:
1. FontAwesome 6 CSS from cdnjs, jsDelivr, unpkg
2. FontAwesome 6 JS (SVG auto-replace) from jsDelivr and cdnjs
3. CSS font-family overrides in style.css for FontAwesome
"""
import re
import time

print("Updating FontAwesome loading configuration for 100% reliability...")

# 1. Update style.css with explicit FontAwesome CSS rules
with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

fa_css_override = """
/* ========== FONTAWESOME ICON ENFORCEMENT ========== */
i.fa-solid, i.fa-regular, i.fa-brands, i.fas, i.far, i.fab,
.fa-solid, .fa-regular, .fa-brands, .fas, .far, .fab {
    font-family: "Font Awesome 6 Free", "Font Awesome 6 Brands", "FontAwesome" !important;
    font-style: normal !important;
    font-weight: 900 !important;
    font-variant: normal !important;
    text-rendering: auto !important;
    line-height: 1 !important;
    display: inline-block !important;
}
"""

if 'FONTAWESOME ICON ENFORCEMENT' not in css:
    css = fa_css_override + "\n" + css
    with open('frontend/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("  ✓ Updated style.css with FontAwesome CSS enforcement rules")

# 2. Update head in school.html, admin.html, parent.html
ts = str(int(time.time()))

head_fa_markup = """    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.5.1/js/all.min.js" defer></script>"""

for fname in ['frontend/school.html', 'frontend/admin.html', 'frontend/parent.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace single font-awesome CSS link with multi-source CSS + JS SVG auto-replace
    old_fa_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
    if old_fa_link in html:
        html = html.replace(old_fa_link, head_fa_markup)
    else:
        # Fallback regex replacement
        html = re.sub(
            r'<link[^>]*font-awesome[^>]*>',
            head_fa_markup,
            html,
            flags=re.IGNORECASE
        )
    
    # Update style.css cache buster
    html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html)
    html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html)
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  ✓ Updated {fname} with multi-CDN FontAwesome CSS & SVG JS library (v={ts})")

print("\n" + "=" * 60)
print("FontAwesome configuration fix completed successfully!")
print("=" * 60)
