"""Fix all remaining elements without icons"""
import re
import time

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = 0

# 1. Fix h2 headers without icons
html = html.replace('<h2>المدرسة الذكية</h2>', '<h2><i class="fa-solid fa-graduation-cap"></i> المدرسة الذكية</h2>')
count += 1

html = html.replace('<h2>نظام المدارس</h2>', '<h2><i class="fa-solid fa-school"></i> نظام المدارس</h2>')
count += 1

# 2. Fix buttons without icons
# Login button
html = html.replace('>دخول</button>', '><i class="fa-solid fa-right-to-bracket"></i> دخول</button>')
count += 1

# Cancel button  
html = html.replace('>إلغاء</button>', '><i class="fa-solid fa-xmark"></i> إلغاء</button>')
count += 1

# Save settings button
html = html.replace('>حفظ الإعدادات</button>', '><i class="fa-solid fa-floppy-disk"></i> حفظ الإعدادات</button>')
count += 1

# Change password button
html = html.replace('>تغيير كلمة المرور</button>', '><i class="fa-solid fa-key"></i> تغيير كلمة المرور</button>')
count += 1

# Recharge SMS balance
html = html.replace('>شحن الرصيد</button>', '><i class="fa-solid fa-coins"></i> شحن الرصيد</button>')
count += 1

print(f"Fixed {count} elements")

# Save
with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update cache buster and sync
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

print(f"Synced HTML files with cache v={ts}")

# Verify - run inspection again
print("\n--- VERIFICATION ---")
with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

all_btns = re.findall(r'<button[^>]*>(.*?)</button>', html2, re.DOTALL)
text_no_icon = []
for b in all_btns:
    if '<i ' not in b and '<img' not in b:
        text = re.sub(r'<[^>]+>', '', b).strip()
        if text and len(text) > 1:
            text_no_icon.append(text)

h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html2, re.DOTALL)
no_icon_h2 = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s if '<i ' not in h]

print(f"Buttons still without icon: {len(text_no_icon)} -> {text_no_icon}")
print(f"H2 headers still without icon: {len(no_icon_h2)} -> {no_icon_h2}")

sidebar = html2[html2.find('id="sidebarNav"'):html2.find('</nav>')]
links = re.findall(r'<a href="#"[^>]*>(.*?)</a>', sidebar, re.DOTALL)
no_icon_links = [re.sub(r'<[^>]+>', '', l).strip() for l in links if '<i ' not in l]
print(f"Sidebar links still without icon: {len(no_icon_links)} -> {no_icon_links}")
