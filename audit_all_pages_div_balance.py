"""
Audit div balance for every <div class="page" id="..."> in school.html
"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

page_starts = [m.start() for m in re.finditer(r'<div class="page" id="([^"]+)"', html)]
print(f"Total page containers in school.html: {len(page_starts)}")

unbalanced_pages = []

for i in range(len(page_starts)):
    start = page_starts[i]
    end = page_starts[i+1] if i+1 < len(page_starts) else html.find('</div>\n</div>\n</body>')
    
    page_sub = html[start:end]
    page_id = re.search(r'id="([^"]+)"', page_sub).group(1)
    
    open_d = page_sub.count('<div')
    close_d = page_sub.count('</div>')
    
    if open_d != close_d:
        unbalanced_pages.append((page_id, open_d, close_d))
        print(f"❌ Page '{page_id}': Open divs = {open_d}, Close divs = {close_d} (Diff: {open_d - close_d})")

if not unbalanced_pages:
    print("✅ All page containers in school.html have 100% BALANCED <div> and </div> tags!")
