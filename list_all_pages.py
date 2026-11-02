import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

pages = sorted(set(re.findall(r'id="(pg-[^"]+)"', html)))
print(f"Total pages found in school.html: {len(pages)}")
for p in pages:
    print(" ", p)
