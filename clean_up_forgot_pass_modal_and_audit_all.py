"""
Clean up forgotPassModal location and audit all 119 page containers
"""
import re

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace forgotPassModal inside pg-custom-reports
modal_match = re.search(r'<!-- ===== MODAL: نسيت كلمة المرور ===== -->.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
if modal_match:
    modal_str = modal_match.group(0)
    html = html.replace(modal_str, '')

# Append modal_str right before </body>
html = html.replace('</body>', '\n<!-- ===== MODAL: نسيت كلمة المرور ===== -->\n' + '</div></div>\n</body>')

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print("Updated HTML files successfully!")
