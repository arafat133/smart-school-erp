"""
Implement Universal State Management & Component Mount Lifecycle Engine in app.js
"""
import re, time

print("=" * 60)
print("Injecting State Management & Initial Component Mount Lifecycle Engine...")
print("=" * 60)

with open('frontend/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

state_management_js = """
// ==================== UNIVERSAL STATE MANAGEMENT & COMPONENT MOUNT LIFECYCLE ENGINE ====================

function hydrateAndMountAllGrids() {
    if (typeof ensureAllDataPresent === 'function') ensureAllDataPresent();

    // Trigger all table grid renderers across all modules immediately
    try { if (typeof renderUsersGrid === 'function') renderUsersGrid(); } catch(e){}
    try { if (typeof renderAuditGrid === 'function') renderAuditGrid(); } catch(e){}
    try { if (typeof renderAlertsGrid === 'function') renderAlertsGrid(); } catch(e){}
    try { if (typeof renderArchiveGrid === 'function') renderArchiveGrid(); } catch(e){}
    try { if (typeof renderPostingGrid === 'function') renderPostingGrid(); } catch(e){}
    try { if (typeof renderSchoolInfo === 'function') renderSchoolInfo(); } catch(e){}
    try { if (typeof renderCurrenciesGrid === 'function') renderCurrenciesGrid(); } catch(e){}
    try { if (typeof renderCashboxInventoryGrid === 'function') renderCashboxInventoryGrid(); } catch(e){}
    try { if (typeof renderClosingsGrid === 'function') renderClosingsGrid(); } catch(e){}
    try { if (typeof renderBanksGrid === 'function') renderBanksGrid(); } catch(e){}
    try { if (typeof renderDemandLettersGrid === 'function') renderDemandLettersGrid(); } catch(e){}
    try { if (typeof renderSystemSettingsGrid === 'function') renderSystemSettingsGrid(); } catch(e){}
    try { if (typeof renderWhatsappSendGrid === 'function') renderWhatsappSendGrid(); } catch(e){}
    try { if (typeof renderWhatsappSettingsGrid === 'function') renderWhatsappSettingsGrid(); } catch(e){}
    try { if (typeof renderVouchers === 'function') renderVouchers(); } catch(e){}
    try { if (typeof renderJournalList === 'function') renderJournalList(); } catch(e){}
    try { if (typeof renderStudentRegister === 'function') renderStudentRegister(); } catch(e){}
    try { if (typeof renderPayrollMasterGrid === 'function') renderPayrollMasterGrid(); } catch(e){}
    try { if (typeof renderEmpAttendanceGrid === 'function') renderEmpAttendanceGrid(); } catch(e){}
    try { if (typeof renderInteractiveTimetable === 'function') renderInteractiveTimetable(); } catch(e){}
    try { if (typeof renderExamScheduleGrid === 'function') renderExamScheduleGrid(); } catch(e){}
    try { if (typeof renderInventoryItemsGrid === 'function') renderInventoryItemsGrid(); } catch(e){}
    try { if (typeof renderActivitiesGrid === 'function') renderActivitiesGrid(); } catch(e){}
    try { if (typeof renderTransportRoutesGrid === 'function') renderTransportRoutesGrid(); } catch(e){}
    try { if (typeof renderDashboard === 'function') renderDashboard(); } catch(e){}
}
window.hydrateAndMountAllGrids = hydrateAndMountAllGrids;

// Auto-Mount on Script Load, DOMContentLoaded, and Window Load
hydrateAndMountAllGrids();

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', hydrateAndMountAllGrids);
} else {
    hydrateAndMountAllGrids();
}
window.addEventListener('load', hydrateAndMountAllGrids);
"""

if 'function hydrateAndMountAllGrids()' not in js:
    js += "\n" + state_management_js + "\n"
    print("  ✓ Appended Universal State Management & Component Mount Lifecycle Engine to app.js")

# Modify goTo function to ALWAYS call hydrateAndMountAllGrids() on page change!
if "hydrateAndMountAllGrids();" not in js:
    js = js.replace("function goTo(id) {", "function goTo(id) {\n    hydrateAndMountAllGrids();\n")
    print("  ✓ Wired hydrateAndMountAllGrids() into goTo(id) dispatcher")

with open('frontend/app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Update cache timestamps
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

print(f"Updated app.js & HTML files with timestamp v={ts}!")
