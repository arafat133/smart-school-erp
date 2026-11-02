"""
Add missing dispatcher aliases to app.js
"""
with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

aliases = """
// ==================== DISPATCHER ALIASES ====================
if (typeof renderExamScheduleGrid !== 'function') {
    function renderExamScheduleGrid() { if (typeof renderExamSchedule === 'function') renderExamSchedule(); }
    window.renderExamScheduleGrid = renderExamScheduleGrid;
}
if (typeof renderStudentRegister !== 'function') {
    function renderStudentRegister() { if (typeof renderStudents === 'function') renderStudents(); }
    window.renderStudentRegister = renderStudentRegister;
}
if (typeof renderSimpleRegister !== 'function') {
    function renderSimpleRegister() { if (typeof renderStudents === 'function') renderStudents(); }
    window.renderSimpleRegister = renderSimpleRegister;
}
if (typeof renderPermissions !== 'function') {
    function renderPermissions() { if (typeof renderUserGroups === 'function') renderUserGroups(); }
    window.renderPermissions = renderPermissions;
}
if (typeof renderAuditLogs !== 'function') {
    function renderAuditLogs() { if (typeof renderAuditGrid === 'function') renderAuditGrid(); }
    window.renderAuditLogs = renderAuditLogs;
}
"""

if 'window.renderAuditLogs = renderAuditLogs' not in js:
    js += "\n" + aliases + "\n"
    print("  ✓ Added missing dispatcher aliases")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated app.js with missing aliases!")
