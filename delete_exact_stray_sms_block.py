"""
Delete exact stray SMS blocks around index 184601 in school.html
"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find AL-AMAL SCH
idx = html.find('AL-AMAL SCH')
if idx != -1:
    # Find the start of the block preceding it
    start_idx = html.rfind('<div class="stats-row"', 0, idx)
    if start_idx == -1:
        start_idx = html.rfind('<div class="page-header"', 0, idx)
    # Find end of table or page-container closing
    end_idx = html.find('</table>', idx) + 8
    if end_idx != -1:
        stray_block = html[start_idx:end_idx]
        print("Found exact stray block (length", len(stray_block), "):")
        print(stray_block[:200])
        html = html[:start_idx] + html[end_idx:]
        print("  ✓ Removed exact stray block!")

# Strip remaining <th>إجراءات</th> or <th>الاقراءات</th>
html = re.sub(r'<th[^>]*>.*?إجراءات.*?</th>', '', html, flags=re.IGNORECASE)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print("Updated HTML files successfully!")
