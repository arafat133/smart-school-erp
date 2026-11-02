"""
Fix exact closing divs in pg-custom-reports
"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('id="pg-custom-reports"')
idx_next = html.find('<div class="page"', idx_start + 20)

sub = html[idx_start-20:idx_next]
print("=== pg-custom-reports sub (len", len(sub), ") ===")
open_d = sub.count('<div')
close_d = sub.count('</div>')
print(f"Open: {open_d}, Close: {close_d}")

# Strip 2 extra </div> at the end of sub
sub_fixed = sub.rstrip()
if sub_fixed.endswith('</div></div>'):
    sub_fixed = sub_fixed[:-12]

html = html[:idx_start-20] + sub_fixed + html[idx_next:]

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print("Updated HTML files successfully!")
