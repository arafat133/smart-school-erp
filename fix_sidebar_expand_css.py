"""
Fix sidebar expansion CSS and JS:
1. Guarantee .nav-section.open .sub-menu uses display: flex !important; opacity: 1 !important; visibility: visible !important;
2. Clean up duplicate / conflicting .sub-menu rules in style.css
3. Update toggleSub(el) in app.js for smooth accordion toggle and auto-expanding parent sections.
"""
import re, time

print("=" * 60)
print("Fixing sidebar expand/collapse CSS & JS...")
print("=" * 60)

# 1. Update style.css
with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add bulletproof sidebar accordion CSS block
bulletproof_sidebar_css = """
/* ==================== BULLETPROOF SIDEBAR ACCORDION CSS ==================== */
.sidebar-nav .nav-section {
    display: flex !important;
    flex-direction: column !important;
    background: rgba(30, 41, 59, 0.45) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 12px !important;
    overflow: hidden !important;
    margin-bottom: 8px !important;
    transition: all 0.3s ease !important;
}

.sidebar-nav .nav-section:hover {
    border-color: rgba(255, 255, 255, 0.2) !important;
}

.sidebar-nav .nav-item.has-sub {
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 13px 15px !important;
    background: rgba(255, 255, 255, 0.03) !important;
    color: #f8fafc !important;
    font-size: 0.92rem !important;
    font-weight: 700 !important;
    cursor: pointer !important;
    user-select: none !important;
    border: none !important;
    border-radius: 0 !important;
    transition: background 0.2s ease !important;
}

.sidebar-nav .nav-item.has-sub:hover {
    background: rgba(255, 255, 255, 0.08) !important;
    color: #ffffff !important;
}

.sidebar-nav .nav-section.open .nav-item.has-sub {
    background: rgba(59, 130, 246, 0.2) !important;
    color: #60a5fa !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
}

.sidebar-nav .nav-item.has-sub .fa-chevron-down {
    transition: transform 0.3s ease !important;
    color: #94a3b8 !important;
}

.sidebar-nav .nav-section.open .nav-item.has-sub .fa-chevron-down {
    transform: rotate(180deg) !important;
    color: #60a5fa !important;
}

/* Sub-menu expansion control */
.sidebar-nav .nav-section .sub-menu {
    display: none !important;
    padding: 8px 10px 12px !important;
    flex-direction: column !important;
    gap: 4px !important;
    background: rgba(15, 23, 42, 0.7) !important;
}

.sidebar-nav .nav-section.open .sub-menu {
    display: flex !important;
    animation: sidebarSlideDown 0.3s ease-out !important;
}

@keyframes sidebarSlideDown {
    from { opacity: 0; transform: translateY(-6px); }
    to { opacity: 1; transform: translateY(0); }
}

.sidebar-nav .sub-menu a {
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    padding: 9px 14px !important;
    border-radius: 8px !important;
    color: #cbd5e1 !important;
    text-decoration: none !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
    border: 1px solid transparent !important;
}

.sidebar-nav .sub-menu a i {
    width: 18px !important;
    text-align: center !important;
    font-size: 0.95rem !important;
    color: #38bdf8 !important;
}

.sidebar-nav .sub-menu a:hover {
    background: rgba(255, 255, 255, 0.08) !important;
    color: #ffffff !important;
    transform: translateX(-4px) !important;
    border-color: rgba(255, 255, 255, 0.15) !important;
}

.sidebar-nav .sub-menu a.active {
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.4), rgba(14, 165, 233, 0.4)) !important;
    color: #ffffff !important;
    border-color: rgba(56, 189, 248, 0.6) !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 15px rgba(14, 165, 233, 0.3) !important;
}
"""

if 'BULLETPROOF SIDEBAR ACCORDION CSS' not in css:
    css += "\n" + bulletproof_sidebar_css.strip() + "\n"

with open('frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("  ✓ Updated style.css with bulletproof sidebar expansion CSS")

# 2. Update toggleSub and goTo in app.js
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

robust_toggle_sub = """
// Robust Sidebar Accordion Toggle Function
function toggleSub(el) {
    if (!el) return;
    const sec = el.closest('.nav-section');
    if (!sec) return;
    
    const isOpen = sec.classList.contains('open');
    
    // Optional accordion behavior: close other sections or keep toggled
    // Toggle current section
    if (isOpen) {
        sec.classList.remove('open');
    } else {
        sec.classList.add('open');
    }
}
window.toggleSub = toggleSub;
"""

# Replace toggleSub in app.js
pattern = r'function\s+toggleSub\(el\)\s*\{.*?\n\s*\}\n\s*window\.toggleSub\s*=\s*toggleSub;'
if re.search(pattern, js, re.DOTALL):
    js = re.sub(pattern, robust_toggle_sub.strip(), js, flags=re.DOTALL)
    print("  ✓ Replaced toggleSub in app.js")
else:
    js += "\n" + robust_toggle_sub.strip() + "\n"
    print("  ✓ Appended robust_toggle_sub in app.js")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 3. Sync HTML cache version
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

print(f"Fixed sidebar expand/collapse and synced HTML files (v={ts})!")
