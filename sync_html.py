import time
import re

ts = str(int(time.time()))

with open('frontend/school.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'style\.css\?v=\d+', 'style.css?v=' + ts, html)
html = re.sub(r'app\.js\?v=\d+', 'app.js?v=' + ts, html)

with open('frontend/school.html', 'w', encoding='utf-8') as f:
    f.write(html)

admin_html = html.replace('id="userType" value="school"', 'id="userType" value="admin"')
parent_html = html.replace('id="userType" value="school"', 'id="userType" value="parent"')

with open('frontend/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)

with open('frontend/parent.html', 'w', encoding='utf-8') as f:
    f.write(parent_html)

print(f"Successfully synced HTML files with timestamp {ts}")
