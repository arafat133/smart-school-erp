"""
Fix sidebar overlap across school.html, admin.html, parent.html:
1. In school.html: Keep ONLY the comprehensive school sidebarNav. Remove saasNav and parentNav.
2. In admin.html: Keep ONLY saasNav (clean Admin sidebar). Remove sidebarNav and parentNav.
3. In parent.html: Keep ONLY parentNav (clean Parent portal sidebar). Remove sidebarNav and saasNav.
4. Clean up CSS for nav-item to ensure white-space: nowrap; overflow: hidden; text-overflow: ellipsis; so text never wraps or clips awkwardly.
"""
import re, time

print("=" * 60)
print("Fixing role-based sidebars across HTML files...")
print("=" * 60)

# Read school.html
with open('frontend/school.html', 'r', encoding='utf-8') as f:
    school_html = f.read()

# Extract the clean school sidebarNav block
sidebar_nav_match = re.search(r'<nav class="sidebar-nav" id="sidebarNav">.*?</nav>', school_html, re.DOTALL)
school_sidebar_nav = sidebar_nav_match.group(0) if sidebar_nav_match else ''

# 1. Clean school.html sidebar block
school_sidebar_block = f"""
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-logo"><i class="fa-solid fa-shield-halved"></i></div>
                <h2><i class="fa-solid fa-school"></i> نظام المدارس الذكي</h2>
                <button class="btn-sidebar-close" id="sidebarCloseBtn"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            {school_sidebar_nav}
            
            <div class="sidebar-footer">
                <button class="btn-logout" onclick="logout()"><i class="fa-solid fa-right-from-bracket"></i> تسجيل الخروج</button>
            </div>
        </aside>
"""

school_html = re.sub(r'<aside class="sidebar" id="sidebar">.*?</aside>', school_sidebar_block.strip(), school_html, flags=re.DOTALL)
print("  ✓ Cleaned school.html sidebar")


# 2. Clean admin.html sidebar block (SaaS Admin Portal)
admin_sidebar_block = """
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-logo"><i class="fa-solid fa-user-gear"></i></div>
                <h2><i class="fa-solid fa-server"></i> بوابة إدارة النظام</h2>
                <button class="btn-sidebar-close" id="sidebarCloseBtn"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <nav class="sidebar-nav" id="saasNav" style="display:flex;flex-direction:column;gap:8px;padding:14px 12px;">
                <a href="#" class="nav-item direct-item active" onclick="goTo('pg-saas-admin')" style="background:linear-gradient(135deg,rgba(59,130,246,0.25),rgba(37,99,235,0.25));border:1px solid rgba(59,130,246,0.4);color:#fff;">
                    <i class="fa-solid fa-server" style="color:#60a5fa;"></i>
                    <span>إدارة المدارس والإحصائيات</span>
                </a>
                <a href="#" class="nav-item direct-item" onclick="goTo('pg-admin-password')">
                    <i class="fa-solid fa-key" style="color:#38bdf8;"></i>
                    <span>تغيير كلمة السر</span>
                </a>
            </nav>
            
            <div class="sidebar-footer">
                <button class="btn-logout" onclick="logout()"><i class="fa-solid fa-right-from-bracket"></i> تسجيل الخروج</button>
            </div>
        </aside>
"""

with open('frontend/admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

admin_html = re.sub(r'<aside class="sidebar" id="sidebar">.*?</aside>', admin_sidebar_block.strip(), admin_html, flags=re.DOTALL)
admin_html = admin_html.replace('id="userType" value="school"', 'id="userType" value="admin"')
print("  ✓ Cleaned admin.html sidebar")


# 3. Clean parent.html sidebar block (Parent Portal)
parent_sidebar_block = """
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-logo"><i class="fa-solid fa-people-roof"></i></div>
                <h2><i class="fa-solid fa-graduation-cap"></i> بوابة ولي الأمر</h2>
                <button class="btn-sidebar-close" id="sidebarCloseBtn"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <nav class="sidebar-nav" id="parentNav" style="display:flex;flex-direction:column;gap:8px;padding:14px 12px;">
                <a href="#" class="nav-item direct-item active" onclick="goTo('pg-parent-dashboard')" style="background:linear-gradient(135deg,rgba(59,130,246,0.25),rgba(37,99,235,0.25));border:1px solid rgba(59,130,246,0.4);color:#fff;">
                    <i class="fa-solid fa-house" style="color:#60a5fa;"></i>
                    <span>الرئيسية (لوحة الاستعلام)</span>
                </a>
                <a href="#" class="nav-item direct-item" onclick="goTo('pg-parent-profile')">
                    <i class="fa-solid fa-id-card" style="color:#38bdf8;"></i>
                    <span>البيانات الشخصية</span>
                </a>
                <a href="#" class="nav-item direct-item" onclick="goTo('pg-parent-fees')">
                    <i class="fa-solid fa-coins" style="color:#fbbf24;"></i>
                    <span>الملخص المالي والرسوم</span>
                </a>
                <a href="#" class="nav-item direct-item" onclick="goTo('pg-parent-attendance')">
                    <i class="fa-solid fa-calendar-check" style="color:#34d399;"></i>
                    <span>سجل الحضور والغياب</span>
                </a>
                <a href="#" class="nav-item direct-item" onclick="goTo('pg-parent-grades')">
                    <i class="fa-solid fa-ranking-star" style="color:#f472b6;"></i>
                    <span>النتائج والمحصلات</span>
                </a>
                <a href="#" class="nav-item direct-item" onclick="goTo('pg-parent-homework')">
                    <i class="fa-solid fa-book-open-reader" style="color:#a78bfa;"></i>
                    <span>الواجبات اليومية</span>
                </a>
            </nav>
            
            <div class="sidebar-footer">
                <button class="btn-logout" onclick="logout()"><i class="fa-solid fa-right-from-bracket"></i> تسجيل الخروج</button>
            </div>
        </aside>
"""

with open('frontend/parent.html', 'r', encoding='utf-8') as f:
    parent_html = f.read()

parent_html = re.sub(r'<aside class="sidebar" id="sidebar">.*?</aside>', parent_sidebar_block.strip(), parent_html, flags=re.DOTALL)
parent_html = parent_html.replace('id="userType" value="school"', 'id="userType" value="parent"')
print("  ✓ Cleaned parent.html sidebar")


# Sync Cache version timestamps
ts = str(int(time.time()))
school_html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, school_html)
school_html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, school_html)

admin_html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, admin_html)
admin_html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, admin_html)

parent_html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, parent_html)
parent_html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, parent_html)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(school_html)

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)

with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

# 4. Update style.css to format direct-item and prevent text clipping or wrapping
with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

direct_item_css = """
/* Direct item styling for single links in sidebar */
.sidebar-nav .nav-item.direct-item {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    padding: 12px 14px !important;
    border-radius: 10px !important;
    color: #f8fafc !important;
    text-decoration: none !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    transition: all 0.25s ease !important;
}

.sidebar-nav .nav-item.direct-item:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    border-color: rgba(255, 255, 255, 0.2) !important;
    color: #ffffff !important;
    transform: translateX(-4px) !important;
}

.sidebar-nav .nav-item.direct-item i {
    font-size: 1.1rem !important;
    width: 22px !important;
    text-align: center !important;
}

.sidebar-footer {
    padding: 14px !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
    background: rgba(15, 23, 42, 0.9) !important;
    margin-top: auto !important;
}

.sidebar-footer .btn-logout {
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    padding: 10px 14px !important;
    border-radius: 10px !important;
    background: rgba(239, 68, 68, 0.15) !important;
    border: 1px solid rgba(239, 68, 68, 0.3) !important;
    color: #f87171 !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}

.sidebar-footer .btn-logout:hover {
    background: rgba(239, 68, 68, 0.3) !important;
    color: #ffffff !important;
}
"""

if 'Direct item styling for single links in sidebar' not in css:
    css += "\n" + direct_item_css.strip() + "\n"

with open('frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print(f"Cleaned role-based sidebars and updated CSS! Timestamp v={ts}")
