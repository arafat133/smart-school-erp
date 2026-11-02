"""
Add active school badge & selector to topbar in school.html, admin.html, parent.html
"""
import re, time

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add active school display badge in topbar next to user profile or logo
school_badge_html = """
        <div id="schoolTenantBadge" style="display:flex;align-items:center;gap:8px;background:rgba(59,130,246,0.15);border:1px solid rgba(59,130,246,0.4);padding:5px 12px;border-radius:20px;font-size:0.85rem;font-weight:700;color:#60a5fa;margin-right:auto;">
            <i class="fa-solid fa-school-flag" style="color:#3b82f6;"></i>
            <span id="activeSchoolDisplay">مدرسة المتفوقين الأهلية</span>
        </div>
"""

if 'id="schoolTenantBadge"' not in html:
    # Insert inside topbar right section
    html = html.replace('<div class="user-profile">', school_badge_html + '\n        <div class="user-profile">')
    print("  ✓ Added Active School Tenant Badge to Topbar")

# Update cache timestamps
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

print(f"Updated HTML files with school tenant badge & timestamp v={ts}!")
