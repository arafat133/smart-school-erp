"""
Comprehensive Audit of All Pages, Render Functions, DB Datasets, Forms, Deletes, Searches
"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

page_ids = re.findall(r'<div class="page" id="(pg-[^"]+)"', html)
print(f"Total HTML Pages found: {len(page_ids)}")
print("Page IDs:", page_ids)

print("\n=== Master Central Dispatcher Check ===")
dispatcher_match = re.search(r'function goTo\s*\([^)]*\)\s*\{(.*?)\n\}', js, re.DOTALL)
if dispatcher_match:
    disp_code = dispatcher_match.group(1)
    print("Found goTo function")

missing_renders = []
for pid in page_ids:
    if pid not in js:
        print(f"⚠️ Page ID {pid} not found in app.js!")
    else:
        # Check if goTo handles this page
        if pid not in disp_code:
            print(f"❓ Page ID {pid} is in app.js but not explicitly in goTo dispatcher!")

print("\n=== Checking DB datasets ===")
db_match = re.search(r'const DB = \{(.*?)\};', js, re.DOTALL)
if db_match:
    db_keys = re.findall(r'(\w+):\s*\[', db_match.group(1))
    print(f"Total DB arrays found ({len(db_keys)}):", db_keys)
