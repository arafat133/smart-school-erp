"""
Execute all user requested fixes:
1. Remove stray Audit block sitting outside pg-audit
2. Completely remove pg-checks and pg-simple-register
3. Remove horizontal scrollbars and make all tables 100% fluid responsive
"""
import re, time

print("=" * 60)
print("Executing All User Requested Fixes...")
print("=" * 60)

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Remove stray Audit block sitting outside pg-audit
# Search for the stray block right after </div>\n<!-- Security KPI Header Cards -->
stray_audit_pattern = r'</div>\s*<!-- Security KPI Header Cards -->.*?<!-- Audit Filter & Search Bar -->.*?(?=<div class="page"|<!-- =====|\Z)'
if re.search(stray_audit_pattern, html, flags=re.DOTALL):
    html = re.sub(stray_audit_pattern, '</div>\n', html, flags=re.DOTALL)
    print("  ✓ Removed stray Audit Log block sitting outside pg-audit!")

# 2. Delete pg-checks and pg-simple-register from HTML
pattern_checks = r'<div class="page" id="pg-checks">.*?</div>\s*(?=<div class="page"|<!--|\Z)'
pattern_simple_reg = r'<div class="page" id="pg-simple-register">.*?</div>\s*(?=<div class="page"|<!--|\Z)'

if 'id="pg-checks"' in html:
    html = re.sub(pattern_checks, '', html, flags=re.DOTALL)
    print("  ✓ Removed pg-checks page from HTML")

if 'id="pg-simple-register"' in html:
    html = re.sub(pattern_simple_reg, '', html, flags=re.DOTALL)
    print("  ✓ Removed pg-simple-register page from HTML")

# Remove sidebar links to pg-checks & pg-simple-register
html = re.sub(r'<li[^>]*onclick="goTo\(\'pg-checks\'\)"[^>]*>.*?</li>', '', html, flags=re.DOTALL)
html = re.sub(r'<li[^>]*onclick="goTo\(\'pg-simple-register\'\)"[^>]*>.*?</li>', '', html, flags=re.DOTALL)

# Update HTML cache timestamps
ts = str(int(time.time()))
html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html)
html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

# Clean up app.js for deleted pages
js = js.replace("if (id === 'pg-simple-register') renderSimpleRegister();", "")
js = js.replace("if (id === 'pg-checks') renderChecks();", "")
with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("  ✓ Updated app.js & HTML files")

# 3. Update style.css to remove horizontal scrollbars & enforce 100% fluid responsive tables
with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

fluid_tables_css = """

/* ==================== 100% FLUID RESPONSIVE TABLES & NO HORIZONTAL SCROLLBAR ==================== */
html, body {
    max-width: 100vw !important;
    overflow-x: hidden !important;
    margin: 0 !important;
    padding: 0 !important;
    box-sizing: border-box !important;
}

.app-container {
    display: flex !important;
    width: 100vw !important;
    max-width: 100vw !important;
    overflow-x: hidden !important;
    box-sizing: border-box !important;
}

.sidebar {
    width: 260px !important;
    min-width: 260px !important;
    max-width: 260px !important;
    position: fixed !important;
    top: 0 !important;
    right: 0 !important;
    height: 100vh !important;
    z-index: 1000 !important;
    overflow-y: auto !important;
}

.main-content {
    flex: 1 !important;
    margin-right: 260px !important;
    width: calc(100vw - 260px) !important;
    max-width: calc(100vw - 260px) !important;
    overflow-x: hidden !important;
    box-sizing: border-box !important;
    min-height: 100vh !important;
}

.page-container {
    width: 100% !important;
    max-width: 100% !important;
    padding: 16px !important;
    box-sizing: border-box !important;
    overflow-x: hidden !important;
}

.page {
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    overflow-x: hidden !important;
}

.toolbar {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 10px !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    margin-bottom: 14px !important;
}

.table-wrapper {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: hidden !important;
    overflow-y: auto !important;
    display: block !important;
    box-sizing: border-box !important;
    background: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    margin-bottom: 20px !important;
    padding: 2px !important;
}

.table-wrapper table {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    table-layout: auto !important;
    border-collapse: collapse !important;
    box-sizing: border-box !important;
}

.table-wrapper table th, .table-wrapper table td {
    white-space: normal !important;
    word-wrap: break-word !important;
    word-break: break-word !important;
    font-size: 0.76rem !important;
    padding: 6px 4px !important;
    text-align: center !important;
}

/* HIDE HORIZONTAL SCROLLBAR GLOBALLY */
::-webkit-scrollbar:horizontal {
    height: 0px !important;
    display: none !important;
}
* {
    scrollbar-width: thin !important;
}
"""

if '100% FLUID RESPONSIVE TABLES & NO HORIZONTAL SCROLLBAR' not in css:
    css += "\n" + fluid_tables_css + "\n"
    print("  ✓ Appended 100% Fluid Responsive Tables CSS to style.css")

with open('frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print(f"Completed all fixes with timestamp v={ts}!")
