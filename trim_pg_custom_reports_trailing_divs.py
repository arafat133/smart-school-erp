"""
Trim exact 2 extra closing divs from pg-custom-reports in school.html
"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx_start = html.find('id="pg-custom-reports"')
idx_next = html.find('<div class="page"', idx_start + 20)

sub = html[idx_start-20:idx_next]
print("=== End of pg-custom-reports block ===")
print(sub[-300:])

# Replace trailing </div>\n</div>\n</div> with </div>\n
sub_new = re.sub(r'(\s*</div>){3,}\s*\Z', '\n</div>\n', sub)
html = html[:idx_start-20] + sub_new + html[idx_next:]

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print("Updated HTML files successfully!")
