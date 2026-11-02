"""
Explicitly add all 9 missing page handlers to Master Central Dispatcher goTo(id) in app.js
"""
import re

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

dispatcher_addition = """
    // Specific Page Handlers Routing
    if (id === 'pg-school-info') renderSchoolInfo();
    if (id === 'pg-income-stmt') renderIncomeStmt();
    if (id === 'pg-audit-trail' || id === 'pg-audit') renderAuditGrid();
    if (id === 'pg-admin-password') renderAdminPassword();
    if (id === 'pg-parent-profile') renderParentProfile();
    if (id === 'pg-parent-fees') renderParentFees();
    if (id === 'pg-parent-attendance') renderParentAttendance();
    if (id === 'pg-parent-grades') renderParentGrades();
    if (id === 'pg-parent-homework') renderParentHomework();
"""

if "if (id === 'pg-school-info') renderSchoolInfo();" not in js:
    # Insert right inside goTo function
    js = js.replace("function goTo(id) {", "function goTo(id) {\n" + dispatcher_addition)
    print("  ✓ Added explicit dispatcher routing inside goTo(id)")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js successfully!")
