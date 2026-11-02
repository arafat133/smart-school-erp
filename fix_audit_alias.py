"""
Fix renderAuditLogs alias in app.js
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace renderAuditLogs with renderAudit in dispatcher
js = js.replace("renderAuditLogs()", "renderAudit()")

if 'function renderAuditLogs' not in js:
    js += "\nfunction renderAuditLogs() { if (typeof renderAudit === 'function') renderAudit(); }\nwindow.renderAuditLogs = renderAuditLogs;\n"

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed renderAudit / renderAuditLogs successfully!")
