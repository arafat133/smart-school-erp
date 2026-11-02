"""
Replace all onclick="window.print()" with onclick="triggerOfficialPrint()" in school.html, admin.html, parent.html
"""
import re, time

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace window.print() with triggerOfficialPrint() in HTML
html_updated = html.replace('onclick="window.print()"', 'onclick="triggerOfficialPrint()"')
html_updated = html_updated.replace("onclick='window.print()'", "onclick='triggerOfficialPrint()'")

# Update cache timestamps
ts = str(int(time.time()))
html_updated = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html_updated)
html_updated = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html_updated)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html_updated)

admin_html = html_updated.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html_updated.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print("  ✓ Replaced all print buttons to use triggerOfficialPrint()")
print(f"Updated HTML files with timestamp v={ts}!")
