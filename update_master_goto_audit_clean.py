"""
Update Master goTo Dispatcher in app.js:
1. Ensure pg-audit calls renderAuditGrid()
2. Remove pg-permissions / renderPermissions handler
"""
import re, time

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update dispatcher
js = js.replace("if (id === 'pg-permissions') renderPermissions();", "// pg-permissions removed")
js = js.replace("if (id === 'pg-audit') renderAudit();", "if (id === 'pg-audit') renderAuditGrid();")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated Master Central Dispatcher in app.js!")
