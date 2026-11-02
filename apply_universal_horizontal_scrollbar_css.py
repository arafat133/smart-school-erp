"""
Apply universal responsive layout constraints and horizontal scrollbar CSS rules in style.css
"""
import re, time

print("=" * 60)
print("Applying Universal Horizontal Scrollbar & Viewport Constraint CSS...")
print("=" * 60)

with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

universal_layout_css = """

/* ==================== UNIVERSAL VIEWPORT & HORIZONTAL SCROLLBAR ENGINE ==================== */
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
    padding: 20px !important;
    box-sizing: border-box !important;
    overflow-x: hidden !important;
}

.page {
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    overflow-x: hidden !important;
}

.page.active {
    display: block !important;
}

.toolbar {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 10px !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    margin-bottom: 16px !important;
}

.table-wrapper {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: auto !important;
    overflow-y: auto !important;
    display: block !important;
    box-sizing: border-box !important;
    background: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    margin-bottom: 20px !important;
    padding: 2px !important;

    /* Firefox horizontal scrollbar */
    scrollbar-width: thin !important;
    scrollbar-color: rgba(59, 130, 246, 0.8) rgba(15, 23, 42, 0.7) !important;
}

.table-wrapper table {
    min-width: 950px !important; /* Guarantees horizontal scrollbar for wide tables! */
    width: 100% !important;
    border-collapse: collapse !important;
    box-sizing: border-box !important;
}

/* UNIVERSAL PROMINENT HORIZONTAL SCROLLBAR */
::-webkit-scrollbar {
    width: 8px !important;
    height: 10px !important; /* Horizontal scrollbar thickness */
}

::-webkit-scrollbar-track {
    background: rgba(15, 23, 42, 0.8) !important;
    border-radius: 6px !important;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(90deg, #3b82f6, #2563eb) !important;
    border-radius: 6px !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.6) !important;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(90deg, #60a5fa, #3b82f6) !important;
}

::-webkit-scrollbar-corner {
    background: rgba(15, 23, 42, 0.8) !important;
}
"""

if 'UNIVERSAL VIEWPORT & HORIZONTAL SCROLLBAR ENGINE' not in css:
    css += "\n" + universal_layout_css + "\n"
    print("  ✓ Appended Universal Viewport & Horizontal Scrollbar Engine to style.css")

with open('frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update HTML cache timestamps
with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

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

print(f"Updated HTML files with timestamp v={ts}!")
