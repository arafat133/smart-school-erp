"""
Script to systematically ensure icons for all pages, headers, buttons, tabs, and modals
"""
import re
import time

print("Adding FontAwesome icons to all interfaces, buttons, tabs, and modals...")

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update buttons in HTML that lack icons
icon_replacements = [
    # Button text replacements with icons
    (r'<button class="btn-close"([^>]*)>\s*</button>', r'<button class="btn-close"\1><i class="fa-solid fa-xmark"></i></button>'),
    (r'>إلغاء</button>', r'><i class="fa-solid fa-xmark"></i> إلغاء</button>'),
    (r'>حفظ</button>', r'><i class="fa-solid fa-floppy-disk"></i> حفظ</button>'),
    (r'>تأكيد</button>', r'><i class="fa-solid fa-check"></i> تأكيد</button>'),
    (r'>إغلاق</button>', r'><i class="fa-solid fa-xmark"></i> إغلاق</button>'),
    (r'>بحث</button>', r'><i class="fa-solid fa-magnifying-glass"></i> بحث</button>'),
    (r'>تصفية</button>', r'><i class="fa-solid fa-filter"></i> تصفية</button>'),
    (r'>طباعة</button>', r'><i class="fa-solid fa-print"></i> طباعة</button>'),
    (r'>تحديث</button>', r'><i class="fa-solid fa-arrows-rotate"></i> تحديث</button>'),
]

for pattern, repl in icon_replacements:
    html = re.sub(pattern, repl, html)

# 2. Add icons to buttons in app.js edit/delete templates if missing
js_icon_replacements = [
    (r'onclick="openForm\(\'([^\']+)\'\)">\s*إضافة', r'onclick="openForm(\'\1\')"><i class="fa-solid fa-plus"></i> إضافة'),
    (r'onclick="openForm\(\'([^\']+)\'\)">إضافة', r'onclick="openForm(\'\1\')"><i class="fa-solid fa-plus"></i> إضافة'),
    (r'>تعديل</button>', r'><i class="fa-solid fa-pen-to-square"></i> تعديل</button>'),
    (r'>حذف</button>', r'><i class="fa-solid fa-trash"></i> حذف</button>'),
    (r'>حفظ</button>', r'><i class="fa-solid fa-floppy-disk"></i> حفظ</button>'),
    (r'>طباعة</button>', r'><i class="fa-solid fa-print"></i> طباعة</button>'),
]

for pattern, repl in js_icon_replacements:
    js = re.sub(pattern, repl, js)

# 3. Verify brace balance
opens = js.count('{')
closes = js.count('}')
print(f"app.js brace check: open={opens} close={closes} diff={opens-closes}")

# 4. Save updated files
with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Sync HTML files & update cache buster
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

print(f"Successfully added icons and synced HTML files with timestamp {ts}!")
