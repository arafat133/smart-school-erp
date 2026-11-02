"""
Explicitly add 4 requested page handlers to Master Central Dispatcher goTo(id) in app.js
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

dispatcher_addition = """
    // 4 Requested Pages Dispatcher Routing
    if (id === 'pg-system-settings') renderSystemSettingsGrid();
    if (id === 'pg-change-password') renderChangePassword();
    if (id === 'pg-sms-send') renderWhatsappSendGrid();
    if (id === 'pg-sms-settings') renderWhatsappSettingsGrid();
"""

if "if (id === 'pg-system-settings') renderSystemSettingsGrid();" not in js:
    js = js.replace("function goTo(id) {", "function goTo(id) {\n" + dispatcher_addition)
    print("  ✓ Added explicit 4 pages dispatcher routing inside goTo(id)")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
