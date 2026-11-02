"""
Inspect and complete Master Central Dispatcher in app.js for ALL 121 Page IDs!
"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

page_ids = re.findall(r'<div class="page" id="(pg-[^"]+)"', html)
print(f"Auditing {len(page_ids)} pages...")

# Check which functions exist in app.js
defined_funcs = set(re.findall(r'function\s+(render\w+)\s*\(', js))
print(f"Total render functions defined in app.js: {len(defined_funcs)}")

# Print mapping for each page ID
print("\n=== Page ID Mapping Verification ===")
unhandled_pages = []

for pid in page_ids:
    clean_name = pid.replace('pg-', '').replace('-', '_')
    # look for matching function name variations
    matches = [fn for fn in defined_funcs if clean_name in fn.lower() or fn.lower() in clean_name]
    if not matches and pid not in js:
        unhandled_pages.append(pid)
        print(f"❌ {pid}: NO RENDER FUNCTION OR JS HANDLER FOUND!")
    else:
        print(f"✅ {pid}: Handled by -> {matches[:2] or 'inline/generic'}")

print(f"\nTotal unhandled pages requiring fixes: {len(unhandled_pages)}")
if unhandled_pages:
    print("Unhandled List:", unhandled_pages)
