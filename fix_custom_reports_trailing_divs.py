"""
Fix exact div count for pg-custom-reports
"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('id="pg-custom-reports"')
idx_next = html.find('<!-- ===== MODAL', idx_start)
if idx_next == -1:
    idx_next = html.find('</body>', idx_start)

sub = html[idx_start-20:idx_next]
open_d = sub.count('<div')
close_d = sub.count('</div>')
diff = close_d - open_d
print(f"pg-custom-reports block: Open {open_d}, Close {close_d}, Diff {diff}")

if diff > 0:
    # Remove `diff` occurrences of </div> at the end of sub
    sub_trimmed = sub
    for _ in range(diff):
        pos = sub_trimmed.rfind('</div>')
        if pos != -1:
            sub_trimmed = sub_trimmed[:pos] + sub_trimmed[pos+6:]
    
    html = html[:idx_start-20] + sub_trimmed + html[idx_next:]

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print("Updated HTML files successfully!")
